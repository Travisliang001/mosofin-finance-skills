#!/usr/bin/env node
// Conformance for workflows/: every n8n workflow is read-only and keeps the envelope contract.
// Usage: node .github/validate-workflows.js [workflows]
const fs = require('fs'), path = require('path');
const root = process.argv[2] || 'workflows';
const GATEWAY = 'https://mcp.mosofin.com/mcp';
const FILES = ['workflow.json', 'README.md', 'input.schema.json', 'output.schema.json', 'sample-input.json', 'sample-output.json'];
// Node types that send, post or write somewhere. None may appear: the workflow hands off, it never acts.
const WRITERS = /gmail|emailSend|microsoftOutlook|slack|telegram|discord|twilio|googleSheets|airtable|notion|quickbooks|xero|postgres|mysql|mongo|ftp|awsS3|googleDrive|executeCommand|writeBinaryFile|readWriteFile/i;
const ALLOWED = new Set(['n8n-nodes-base.scheduleTrigger', 'n8n-nodes-base.webhook', 'n8n-nodes-base.code', 'n8n-nodes-base.httpRequest', 'n8n-nodes-base.respondToWebhook']);
const WRITE_TOOL = /tool_name:\s*'(create|update|delete|post|send|void|pay|approve|apply|write|record|submit)_/;
let fail = 0, count = 0;
const err = (w, m) => { fail++; console.log(`FAIL  ${w}: ${m}`); };
for (const w of fs.readdirSync(root).filter((d) => fs.statSync(path.join(root, d)).isDirectory()).sort()) {
  count++;
  const dir = path.join(root, w);
  for (const f of FILES) if (!fs.existsSync(path.join(dir, f))) err(w, `missing ${f}`);
  let wf; try { wf = JSON.parse(fs.readFileSync(path.join(dir, 'workflow.json'), 'utf8')); } catch (e) { err(w, 'workflow.json is not JSON'); continue; }
  if (!(wf.meta && wf.meta.mosofin && wf.meta.mosofin.read_only === true)) err(w, 'meta.mosofin.read_only is not true');
  const names = wf.nodes.map((n) => n.name);
  for (const need of ['Settings', 'Parse Input', 'Compute']) if (!names.includes(need)) err(w, `no ${need} node`);
  for (const n of wf.nodes) {
    if (WRITERS.test(n.type) || !ALLOWED.has(n.type)) err(w, `node "${n.name}" has type ${n.type}, which is not allowed`);
    if (n.type === 'n8n-nodes-base.httpRequest') {
      if (n.parameters.url !== GATEWAY) err(w, `HTTP node "${n.name}" calls ${n.parameters.url}, not the Mosofin gateway`);
      const body = n.parameters.jsonBody || '';
      if (!/invoke_datasource_api_tool/.test(body)) err(w, `HTTP node "${n.name}" does not use invoke_datasource_api_tool`);
      if (!/data_source_id/.test(body)) err(w, `HTTP node "${n.name}" does not send data_source_id`);
      if (WRITE_TOOL.test(body)) err(w, `HTTP node "${n.name}" calls a write tool`);
      if (/approved\s*:/.test(body)) err(w, `HTTP node "${n.name}" pre-approves a call`);
      if (!(n.credentials && n.credentials.httpHeaderAuth)) err(w, `HTTP node "${n.name}" has no header credential (the API key must not be inline)`);
    }
    if (n.parameters.jsCode && /(api[_-]?key|bearer)\s*[:=]\s*['"][A-Za-z0-9_\-]{12,}/i.test(n.parameters.jsCode)) err(w, `node "${n.name}" appears to hold a secret`);
  }
  try {
    const out = JSON.parse(fs.readFileSync(path.join(dir, 'sample-output.json'), 'utf8'));
    if (out.read_only !== true) err(w, 'sample output read_only is not true');
    if (out.version !== '1.0') err(w, 'sample output is not envelope v1.0');
    if (!['ok', 'partial', 'error'].includes(out.status)) err(w, `sample output status ${out.status}`);
    if ((out.proposed_actions || []).some((a) => a.requires_approval !== true)) err(w, 'a proposed action lacks requires_approval: true');
    for (const k of ['validation', 'findings', 'proposed_actions', 'not_done', 'sources']) if (!Array.isArray(out[k])) err(w, `sample output ${k} is not an array`);
  } catch (e) { err(w, 'sample-output.json is not JSON'); }
  const readme = fs.existsSync(path.join(dir, 'README.md')) ? fs.readFileSync(path.join(dir, 'README.md'), 'utf8') : '';
  if (!/\*\*Read-only\.\*\*/.test(readme)) err(w, 'README does not open with the read-only statement');
}
console.log(`${count} workflow(s) checked, ${fail} problem(s)`);
process.exit(fail ? 1 : 0);
