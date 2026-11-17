// Shared helpers, inlined into every workflow's Compute node. No dependencies; runs in n8n's Code node and in Node.
const num = (v) => { if (typeof v === 'number') return v; const n = parseFloat(String(v ?? '').replace(/[, $£€]/g, '')); return isNaN(n) ? 0 : n; };
const r2 = (n) => Math.round(n * 100) / 100;
const day = (s) => { const d = new Date(String(s).slice(0, 10) + 'T00:00:00Z'); return isNaN(d) ? null : d; };
const daysBetween = (a, b) => { const x = day(a), y = day(b); return x && y ? Math.round((y - x) / 86400000) : null; };
const normNo = (s) => String(s ?? '').toUpperCase().replace(/^(INV|BILL|NO|#)[-\s]*/i, '').replace(/[^A-Z0-9]/g, '').replace(/^0+/, '');
const normName = (s) => String(s ?? '').toUpperCase().replace(/\b(INC|LTD|LLC|LLP|CO|CORP|LIMITED|GROUP|GRP)\b\.?/g, '').replace(/[^A-Z0-9]/g, '');
const sum = (a, f) => r2(a.reduce((t, x) => t + num(f ? f(x) : x), 0));

function parseCSV(text) {
  const rows = []; let row = [], cell = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"' && text[i + 1] === '"') { cell += '"'; i++; } else if (c === '"') q = false; else cell += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cell); cell = ''; }
    else if (c === '\n' || c === '\r') { if (c === '\r' && text[i + 1] === '\n') i++; row.push(cell); cell = ''; if (row.some((x) => x !== '')) rows.push(row); row = []; }
    else cell += c;
  }
  if (cell !== '' || row.length) { row.push(cell); rows.push(row); }
  if (!rows.length) return [];
  const head = rows[0].map((h) => h.trim());
  return rows.slice(1).map((r) => Object.fromEntries(head.map((h, i) => [h, (r[i] ?? '').trim()])));
}

// A supplied file is { name, role, rows | content (CSV text) | text | fields }.
const rowsOf = (f) => (f ? (Array.isArray(f.rows) ? f.rows : f.content ? parseCSV(f.content) : []) : []);

// Rename source columns to the names the logic uses. `map` is { logicName: [candidate source names] }.
function pick(rows, map) {
  return rows.map((r) => {
    const keys = Object.keys(r), o = { _raw: r };
    for (const [k, cands] of Object.entries(map)) {
      const hit = [].concat(cands).find((c) => keys.find((x) => x.toLowerCase() === String(c).toLowerCase()));
      const key = hit && keys.find((x) => x.toLowerCase() === String(hit).toLowerCase());
      o[k] = key ? r[key] : undefined;
    }
    return o;
  });
}

// Unwrap a Mosofin gateway reply (MCP tools/call over HTTP) into an array of rows. Tolerant of shape.
function unwrap(resp) {
  if (resp == null) return { rows: [], error: 'no response' };
  if (typeof resp.data === 'string' && /^\s*(event|data):/m.test(resp.data)) {
    // Streamable-HTTP reply delivered as server-sent events: take the last data: line.
    const last = resp.data.split('\n').filter((l) => l.startsWith('data:')).pop();
    try { resp = JSON.parse(last.slice(5)); } catch (e) { return { rows: [], error: 'event-stream reply was not JSON' }; }
  }
  if (resp.error) return { rows: [], error: typeof resp.error === 'string' ? resp.error : (resp.error.message || JSON.stringify(resp.error)) };
  let v = resp.result ?? resp;
  if (v.isError) return { rows: [], error: (v.content && v.content[0] && v.content[0].text) || 'tool error' };
  if (v.structuredContent) v = v.structuredContent;
  else if (Array.isArray(v.content) && v.content[0] && v.content[0].text) { try { v = JSON.parse(v.content[0].text); } catch (e) { return { rows: [], error: 'reply was not JSON' }; } }
  if (v && v.status && /approval_required|tool_policy_disabled|entity_required/.test(v.status)) return { rows: [], error: v.status };
  const mock = !!(v && v.mock);
  if (Array.isArray(v)) return { rows: v, mock };
  for (const k of ['rows', 'data', 'items', 'results', 'records']) if (v && Array.isArray(v[k])) return { rows: v[k], mock };
  return { rows: v ? [v] : [], mock };
}

// The validation gate: every supplied file is checked on its content before any work.
// spec: { role: { required: bool, columns: [[alternatives...], ...], what: 'bank statement' } }
function validateFiles(files, spec, settings) {
  const verdicts = [], byRole = {};
  for (const f of files || []) {
    const s = spec[f.role];
    if (!s) { verdicts.push({ file: f.name, role: f.role || null, verdict: 'set aside', reason: 'no step of this workflow uses it' }); continue; }
    const rows = rowsOf(f), cols = rows.length ? Object.keys(rows[0]).map((c) => c.toLowerCase()) : [];
    const isText = s.text && (f.text || f.fields);
    const missing = isText ? [] : (s.columns || []).filter((alts) => ![].concat(alts).some((a) => cols.includes(String(a).toLowerCase()))).map((a) => [].concat(a)[0]);
    if (!isText && !rows.length) { verdicts.push({ file: f.name, role: f.role, verdict: 'rejected', reason: 'no readable rows' }); continue; }
    if (missing.length) { verdicts.push({ file: f.name, role: f.role, verdict: 'rejected', reason: `not a ${s.what}: missing column(s) ${missing.join(', ')}` }); continue; }
    const named = f.company || (rows[0] && rows[0].company);
    if (named && settings.company && normName(named) !== normName(settings.company)) { verdicts.push({ file: f.name, role: f.role, verdict: 'rejected', reason: `names a different company: ${named}` }); continue; }
    verdicts.push({ file: f.name, role: f.role, verdict: named ? 'accepted' : 'accepted with a limit', reason: named ? `${s.what}, ${rows.length} rows` : `${s.what}, ${rows.length || 1} rows; company and period are as stated by the caller` });
    byRole[f.role] = f;
  }
  const missingRequired = Object.entries(spec).filter(([role, s]) => s.required && !byRole[role]).map(([role, s]) => ({ role, what: s.what }));
  return { verdicts, byRole, missingRequired };
}

// The one output shape every workflow returns.
function envelope(workflow, settings, o) {
  const errors = (o.read_errors || []).concat((o.missing || []).map((m) => `required input missing or rejected: ${m.what} (role "${m.role}")`));
  const status = o.status || (errors.length && o.blocked ? 'error' : errors.length || (o.not_done || []).length ? 'partial' : 'ok');
  return {
    workflow, version: '1.0', run_id: `${workflow}-${settings.run_at || new Date().toISOString()}`,
    company: settings.company || null, currency: settings.currency || null, period: o.period || settings.as_at || null,
    status, summary: o.summary || '', read_only: true,
    validation: o.validation || [], findings: o.findings || [], proposed_actions: (o.proposed_actions || []).map((a) => ({ requires_approval: true, ...a })),
    totals: o.totals || {}, not_done: (o.not_done || []).concat(errors),
    sources: o.sources || [], mock_data: !!o.mock, settings_used: o.settings_used || {},
  };
}
const fill = (tpl, v) => String(tpl).replace(/\{\{\s*(\w+)\s*\}\}/g, (_, k) => (v[k] ?? ''));
