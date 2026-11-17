#!/usr/bin/env node
// Builds workflows/<name>/ (workflow.json, README.md, schemas, samples) from specs.js + lib.js,
// and self-tests each workflow by running its Compute logic in Node on the sample input.
// Usage: node .github/workflows-src/build.js [name ...]      (no args = all)
//        node .github/workflows-src/build.js --check         (fail if regenerating changes workflows/)
const fs = require('fs'), path = require('path'), os = require('os');
const SRC = __dirname;
const ROOT = path.join(SRC, '..', '..');
const OUT = path.join(ROOT, 'workflows');
const LIB = fs.readFileSync(path.join(SRC, 'lib.js'), 'utf8');
const SPECS = require('./specs.js');
const GATEWAY = 'https://mcp.mosofin.com/mcp';
const SET = "$('Settings').first().json.settings";

// The Compute logic: lib + the workflow's own function. The same text runs in n8n and in the self-test.
function computeSource(spec) {
  return `// ${spec.name}: compute. Every configurable value is in the Settings node, not here.
${LIB}
// ---- this workflow ----
const FILE_SPEC = ${JSON.stringify(spec.fileSpec || {}, null, 2)};
function compute(S, files, R) {
  const V = validateFiles(files, FILE_SPEC, S);
  const covered = [], sources = [];
  // src(readKey, fileRole, columnMap): Mosofin read first, uploaded file as fallback.
  const src = (key, role, map) => {
    const r = key && R[key], ok = !!(r && !r.error && r.rows.length), f = role && V.byRole[role];
    const rows = ok ? r.rows : f ? rowsOf(f) : [];
    if (key && !ok && f) covered.push(key);
    const from = ok ? 'Mosofin ' + key : f ? 'file ' + f.name : null;
    if (from && !sources.includes(from)) sources.push(from);
    return { rows: map ? pick(rows, map) : rows, from, have: !!from };
  };
  let o;
  try { o = (${spec.compute.toString().replace(/^compute\s*\(/, "function (")})(); }
  catch (e) { o = { status: 'error', blocked: true, summary: 'The workflow could not compute: ' + e.message }; }
  const unused = Object.keys(R).filter((k) => R[k] && R[k].error && !covered.includes(k));
  o.read_errors = unused.map((k) => 'Mosofin read ' + k + ' unavailable (' + R[k].error + ')' + (${JSON.stringify((spec.optionalReads || []))}.includes(k) ? '; step skipped' : ''));
  o.not_done = (o.not_done || []).concat(V.verdicts.filter((v) => v.verdict === 'rejected').map((v) => 'file ' + v.file + ' rejected: ' + v.reason));
  o.validation = V.verdicts; o.mock = o.mock || Object.values(R).some((v) => v && v.mock);
  o.sources = (o.sources || []).concat(sources); o.settings_used = S;
  if (V.missingRequired.length) { o.missing = V.missingRequired; if (${!!spec.blockOnMissing}) { o.status = 'error'; o.blocked = true; } }
  return envelope(${JSON.stringify(spec.name)}, S, o);
}
`;
}

function n8nComputeCode(spec) {
  return computeSource(spec) + `
// ---- n8n glue ----
const S = ${SET};
const input = $('Parse Input').first().json;
const R = {};
${(spec.reads || []).map((r) => `try { R[${JSON.stringify(r.key)}] = unwrap($('Mosofin: ${r.key}').first().json); } catch (e) { R[${JSON.stringify(r.key)}] = { rows: [], error: 'not reached' }; }`).join('\n')}
return [{ json: compute(S, input.files || [], R) }];
`;
}

function settingsCode(spec) {
  return `// ${spec.name}: Settings. EVERY configurable value for this workflow lives here; edit this node only.
// Any of them can also be overridden for one run by sending { "settings": { ... } } in the webhook body.
const settings = ${JSON.stringify(spec.settings, null, 2)};
const trig = $input.first().json || {};
const body = trig.body && typeof trig.body === 'object' ? trig.body : {};
if (body.settings && typeof body.settings === 'object') Object.assign(settings, body.settings);
settings.run_at = new Date().toISOString();
return [{ json: { settings, body } }];
`;
}

const parseInputCode = `// Input envelope: { settings?, parameters?, files?: [{ name, role, content (CSV) | rows | text | fields, company? }] }
const body = $input.first().json.body || {};
return [{ json: { parameters: body.parameters || {}, files: Array.isArray(body.files) ? body.files : [] } }];
`;

function jsonBody(r) {
  const params = Object.entries(r.params || {}).map(([k, v]) => `${k}: ${typeof v === 'string' && v.startsWith('$') ? `${SET}.${v.slice(1)}` : JSON.stringify(v)}`).join(', ');
  return `={{ JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name: 'invoke_datasource_api_tool', arguments: { datasource: ${SET}.datasource, data_source_id: ${SET}.data_source_id, tool_name: '${r.tool}', params: { ${params} } } } }) }}`;
}

function buildWorkflowJson(spec) {
  let n = 0; const id = () => `${spec.id}-${String(++n).padStart(2, '0')}`;
  const nodes = [], connections = {};
  const connect = (from, to) => { (connections[from] = connections[from] || { main: [[]] }).main[0].push({ node: to, type: 'main', index: 0 }); };
  let x = 0; const pos = (y = 300) => [x += 260, y];
  const entries = [];
  if (spec.trigger.includes('schedule')) {
    nodes.push({ id: id(), name: 'Schedule', type: 'n8n-nodes-base.scheduleTrigger', typeVersion: 1.2, position: [0, 200], parameters: { rule: { interval: [{ field: 'cronExpression', expression: spec.schedule }] } } });
    entries.push('Schedule');
  }
  if (spec.trigger.includes('webhook')) {
    nodes.push({ id: id(), name: 'Webhook', type: 'n8n-nodes-base.webhook', typeVersion: 2, position: [0, 400], webhookId: `mosofin-${spec.name}`, parameters: { httpMethod: 'POST', path: `mosofin-${spec.name}`, responseMode: 'responseNode', options: {} } });
    entries.push('Webhook');
  }
  nodes.push({ id: id(), name: 'Settings', type: 'n8n-nodes-base.code', typeVersion: 2, position: pos(), parameters: { jsCode: settingsCode(spec) } });
  entries.forEach((e) => connect(e, 'Settings'));
  nodes.push({ id: id(), name: 'Parse Input', type: 'n8n-nodes-base.code', typeVersion: 2, position: pos(), parameters: { jsCode: parseInputCode } });
  connect('Settings', 'Parse Input');
  let prev = 'Parse Input';
  for (const r of spec.reads || []) {
    const name = `Mosofin: ${r.key}`;
    nodes.push({
      id: id(), name, type: 'n8n-nodes-base.httpRequest', typeVersion: 4.2, position: pos(), notes: `Read-only Mosofin read: ${r.tool}`,
      credentials: { httpHeaderAuth: { id: '', name: 'Mosofin API Key' } },
      parameters: {
        method: 'POST', url: GATEWAY, authentication: 'genericCredentialType', genericAuthType: 'httpHeaderAuth',
        sendHeaders: true, headerParameters: { parameters: [{ name: 'Accept', value: 'application/json, text/event-stream' }] },
        sendBody: true, specifyBody: 'json', jsonBody: jsonBody(r),
        options: { response: { response: { neverError: true } } },
      },
    });
    connect(prev, name); prev = name;
  }
  nodes.push({ id: id(), name: 'Compute', type: 'n8n-nodes-base.code', typeVersion: 2, position: pos(), parameters: { jsCode: n8nComputeCode(spec) } });
  connect(prev, 'Compute');
  if (spec.trigger.includes('webhook')) {
    nodes.push({ id: id(), name: 'Respond', type: 'n8n-nodes-base.respondToWebhook', typeVersion: 1.1, position: pos(), parameters: { respondWith: 'json', responseBody: '={{ JSON.stringify($json) }}', options: {} } });
    connect('Compute', 'Respond');
  }
  return {
    name: `Mosofin: ${spec.title}`,
    nodes, connections, settings: { executionOrder: 'v1' }, pinData: {},
    meta: { mosofin: { workflow: spec.name, version: '1.0', read_only: true, output: 'one JSON envelope (v1.0) returned to the caller; posts, sends and pays nothing' } },
  };
}

const outputSchema = {
  $schema: 'https://json-schema.org/draft/2020-12/schema', title: 'Mosofin workflow output envelope v1.0', type: 'object',
  required: ['workflow', 'version', 'run_id', 'status', 'summary', 'read_only', 'validation', 'findings', 'proposed_actions', 'totals', 'not_done', 'sources', 'mock_data', 'settings_used'],
  properties: {
    workflow: { type: 'string' }, version: { const: '1.0' }, run_id: { type: 'string' },
    company: { type: ['string', 'null'] }, currency: { type: ['string', 'null'] }, period: { type: ['string', 'null'] },
    status: { enum: ['ok', 'partial', 'error'], description: 'ok: everything ran; partial: ran with something skipped (see not_done); error: stopped, nothing to act on' },
    summary: { type: 'string' }, read_only: { const: true },
    validation: { type: 'array', items: { type: 'object', required: ['file', 'verdict', 'reason'], properties: { verdict: { enum: ['accepted', 'accepted with a limit', 'rejected', 'set aside'] } } } },
    findings: { type: 'array', items: { type: 'object', required: ['type'] } },
    proposed_actions: { type: 'array', items: { type: 'object', required: ['type', 'requires_approval'], properties: { requires_approval: { const: true } } } },
    totals: { type: 'object' }, not_done: { type: 'array', items: { type: 'string' } },
    sources: { type: 'array', items: { type: 'string' } }, mock_data: { type: 'boolean' }, settings_used: { type: 'object' },
  },
};

function inputSchema(spec) {
  return {
    $schema: 'https://json-schema.org/draft/2020-12/schema', title: `${spec.name} input envelope`, type: 'object',
    properties: {
      settings: { type: 'object', description: 'Per-run overrides of any setting.', properties: Object.fromEntries(Object.entries(spec.settings).map(([k, v]) => [k, { default: v }])) },
      parameters: { type: 'object' },
      files: { type: 'array', items: { type: 'object', required: ['name', 'role'], properties: {
        name: { type: 'string' }, role: { enum: Object.keys(spec.fileSpec || {}) }, content: { type: 'string', description: 'CSV text, first row = headers' },
        rows: { type: 'array', items: { type: 'object' } }, company: { type: 'string', description: 'company the file belongs to, if known' } } } },
    },
  };
}

function readme(spec) {
  const fs_ = Object.entries(spec.fileSpec || {});
  const cols = (c) => (c || []).map((a) => [].concat(a).map((x) => `\`${x}\``).join(' / ')).join(', ');
  return `# ${spec.title}

${spec.description}

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in \`proposed_actions[]\`, each with \`requires_approval: true\`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | ${[spec.trigger.includes('schedule') ? `schedule \`${spec.schedule}\`` : '', spec.trigger.includes('webhook') ? `webhook \`POST /webhook/mosofin-${spec.name}\`` : ''].filter(Boolean).join(' + ')} |
| Mosofin reads | ${(spec.reads || []).map((r) => `\`${r.tool}\``).join(', ') || 'none (file-driven)'} |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

\`\`\`json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
\`\`\`
${fs_.length ? `
| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
${fs_.map(([role, f]) => `| \`${role}\` | ${f.what} | ${cols(f.columns)} | ${f.required ? 'yes' : 'no'} |`).join('\n')}

Every file is validated on its **content** before any work: right kind of document, right company,
usable. A rejected required file stops the run (\`status: "error"\`); a rejected optional file is
skipped and named in \`not_done\` (\`status: "partial"\`).${(spec.reads || []).length ? ' Where a role mirrors a Mosofin read, the Mosofin data is used first and the file is the fallback.' : ''}
` : ''}
## Settings

All in the **Settings** node; any can be overridden per run via \`settings\` in the body.

| Setting | Default | Meaning |
|---|---|---|
${Object.entries(spec.settings).map(([k, v]) => `| \`${k}\` | \`${JSON.stringify(v).replace(/\|/g, '\\|')}\` | ${(spec.settingNotes || {})[k] || COMMON_NOTES[k] || ''} |`).join('\n')}

## What it does

${spec.logic.map((l) => `- ${l}`).join('\n')}

## Output

${spec.outputNotes.map((l) => `- ${l}`).join('\n')}
`;
}

const COMMON_NOTES = {
  company: 'Company the run is for; a file naming another company is rejected',
  currency: 'Reporting currency, echoed in the envelope',
  datasource: 'Mosofin datasource name (e.g. quickbooks, xero)',
  data_source_id: 'Mosofin data source id; sent on every Mosofin call',
  as_at: 'As-at date (YYYY-MM-DD); empty = run date',
  period_start: 'First day of the period (YYYY-MM-DD)',
  period_end: 'Last day of the period (YYYY-MM-DD)',
};

function selfTest(spec) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'mosofin-wf-'));
  const mod = path.join(dir, spec.name + '.js');
  fs.writeFileSync(mod, computeSource(spec) + '\nmodule.exports = compute;\n');
  const compute = require(mod);
  fs.rmSync(dir, { recursive: true, force: true });
  const S = { ...spec.settings, ...(spec.sampleInput.settings || {}), run_at: '2025-10-01T07:00:00.000Z' };
  const R = {};
  for (const r of spec.reads || []) R[r.key] = spec.sampleReads && spec.sampleReads[r.key] ? { rows: spec.sampleReads[r.key] } : { rows: [], error: 'not connected in the sample run' };
  const env = compute(S, spec.sampleInput.files || [], R);
  const p = [];
  if (env.read_only !== true) p.push('read_only not true');
  if (env.proposed_actions.some((a) => a.requires_approval !== true)) p.push('proposed action without requires_approval');
  const e = spec.expect || {};
  if (e.status && env.status !== e.status) p.push(`status ${env.status}, expected ${e.status}`);
  for (const t of e.find || []) if (!env.findings.some((f) => f.type === t)) p.push(`no finding of type ${t}`);
  for (const t of e.actions || []) if (!env.proposed_actions.some((a) => a.type === t)) p.push(`no proposed action of type ${t}`);
  for (const fn of e.rejected || []) if (!env.validation.some((v) => v.file === fn && v.verdict === 'rejected')) p.push(`file ${fn} not rejected`);
  if (e.check) { const m = e.check(env); if (m) p.push(m); }
  return { env, p };
}

function files(spec) {
  const { env, p } = selfTest(spec);
  const sampleOut = { ...env, run_id: `${spec.name}-2025-10-01T07:00:00.000Z` };
  return {
    out: {
      'workflow.json': JSON.stringify(buildWorkflowJson(spec), null, 2) + '\n',
      'README.md': readme(spec),
      'input.schema.json': JSON.stringify(inputSchema(spec), null, 2) + '\n',
      'output.schema.json': JSON.stringify(outputSchema, null, 2) + '\n',
      'sample-input.json': JSON.stringify(spec.sampleInput, null, 2) + '\n',
      'sample-output.json': JSON.stringify(sampleOut, null, 2) + '\n',
    }, env, p,
  };
}

const args = process.argv.slice(2), check = args.includes('--check');
const names = args.filter((a) => !a.startsWith('--'));
const todo = names.length ? SPECS.filter((s) => names.includes(s.name)) : SPECS;
let bad = 0, drift = [];
for (const spec of todo) {
  const { out, env, p } = files(spec);
  const dir = path.join(OUT, spec.name);
  if (check) {
    for (const [f, txt] of Object.entries(out)) { const fp = path.join(dir, f); if (!fs.existsSync(fp) || fs.readFileSync(fp, 'utf8') !== txt) drift.push(`${spec.name}/${f}`); }
  } else {
    fs.mkdirSync(dir, { recursive: true });
    for (const [f, txt] of Object.entries(out)) fs.writeFileSync(path.join(dir, f), txt);
  }
  if (p.length) bad++;
  console.log(`${p.length ? 'FAIL' : 'PASS'}  ${spec.id} ${spec.name.padEnd(34)} status=${env.status.padEnd(7)} findings=${String(env.findings.length).padEnd(3)} actions=${env.proposed_actions.length}${p.length ? '  <- ' + p.join('; ') : ''}`);
}
if (drift.length) { console.log('\nOut of date (run node .github/workflows-src/build.js):\n  ' + drift.join('\n  ')); bad++; }
process.exit(bad ? 1 : 0);
