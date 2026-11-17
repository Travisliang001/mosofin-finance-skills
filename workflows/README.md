# Mosofin n8n workflows

Eighteen n8n workflows that run accounting checks on Mosofin data on a schedule or on demand. Each
returns **one JSON envelope** for the next step to use: an email connector, a chat post, a dashboard,
or another MCP tool.

**Read-only.** No workflow posts, sends, pays or changes anything. The only outbound calls are reads
through the Mosofin gateway. Anything that should happen next (an email, a journal entry, a hold, a
payment) comes back in `proposed_actions[]` with `requires_approval: true`, and a person approves it
before a downstream step acts on it.

## The workflows

| # | Workflow | Trigger | Mosofin reads | Proposes |
|---|---|---|---|---|
| 01 | [invoice-ingestion](invoice-ingestion/) | webhook | `search_vendors` | bill drafts with GL coding, new vendors |
| 02 | [bank-reconciliation](bank-reconciliation/) | webhook | `get_general_ledger` | entries for bank-only fees and interest |
| 03 | [three-way-match](three-way-match/) | webhook | `search_bills` | holds on bills with exceptions |
| 04 | [duplicate-invoice-detection](duplicate-invoice-detection/) | daily + webhook | `search_bills` | holds on likely duplicates |
| 05 | [ar-collections](ar-collections/) | weekly + webhook | `search_invoices`, `search_payments` | one collection email draft per customer |
| 06 | [expense-receipts](expense-receipts/) | webhook | none | reimbursement of clean lines |
| 07 | [month-end-close-orchestrator](month-end-close-orchestrator/) | days 1–7 + webhook | `get_trial_balance` | nudges to task owners |
| 08 | [recurring-journal-automator](recurring-journal-automator/) | monthly + webhook | `get_general_ledger` | missing recurring entries |
| 09 | [cash-application](cash-application/) | webhook | `search_invoices`, `search_payments` | payment-to-invoice applications |
| 10 | [pbc-chase-up](pbc-chase-up/) | weekdays + webhook | none | one reminder per owner |
| 11 | [vendor-onboarding](vendor-onboarding/) | webhook | `search_vendors` | vendor set-up or an information request |
| 12 | [scheduled-financial-pack](scheduled-financial-pack/) | monthly + webhook | `get_profit_and_loss`, `get_balance_sheet` | the pack, ready to deliver |
| 13 | [gl-flux-monitor](gl-flux-monitor/) | monthly + webhook | `get_profit_and_loss` | explanation requests per owner |
| 14 | [vendor-statement-reconciliation](vendor-statement-reconciliation/) | webhook | `search_bills` | queries to the vendor |
| 15 | [fixed-asset-rollforward](fixed-asset-rollforward/) | monthly + webhook | `get_general_ledger` | missing depreciation entries |
| 16 | [inventory-obsolescence-reserve](inventory-obsolescence-reserve/) | quarterly + webhook | none | reserve adjustment entry |
| 17 | [sales-tax-compliance-monitor](sales-tax-compliance-monitor/) | monthly + webhook | `search_invoices` | registration reviews |
| 18 | [intercompany-netting-settlement](intercompany-netting-settlement/) | monthly + webhook | none | settlement payments |

Each folder has `workflow.json` (import into n8n), a README (settings, inputs, logic, output),
`input.schema.json`, `output.schema.json`, and a sample input with the real output it produces.

## Shape of every workflow

```
Schedule / Webhook → Settings → Parse Input → Mosofin: <read> … → Compute → Respond
```

- **Settings**: the only node you edit. Every threshold, account, period, template, list and the
  Mosofin datasource and `data_source_id` are here. Nothing configurable is hardcoded anywhere else.
  Any setting can be overridden for one run by sending `{ "settings": { … } }` in the webhook body.
- **Mosofin reads**: HTTP Request to `https://mcp.mosofin.com/mcp` calling
  `invoke_datasource_api_tool` with a read tool, `data_source_id` on every call. If a read fails or
  the tool is disabled, the workflow uses a matching uploaded file if there is one. Otherwise it
  reports the gap in `not_done`.
- **Compute**: checks every uploaded file before any work (right kind of document, right company,
  usable, needed), then does the arithmetic in plain code. A rejected required file stops the run.
  A rejected optional file is skipped and reported.

## Input envelope

```json
{ "settings":   { "as_at": "2025-09-30" },
  "parameters": {},
  "files": [ { "name": "open-invoices.csv", "role": "ar_open", "content": "customer,invoice_no,…", "company": "Northbrook Trading Ltd" } ] }
```

A file is CSV text in `content`, or parsed `rows`. Each workflow's README lists its file roles and
the columns each one needs (alternative column names are accepted).

## Output envelope (v1.0, same for all 18)

| Field | Meaning |
|---|---|
| `workflow`, `version`, `run_id` | what ran |
| `company`, `currency`, `period` | the scope it ran for |
| `status` | `ok` everything ran · `partial` ran with something skipped (see `not_done`) · `error` stopped; nothing to act on |
| `summary` | one line for a person |
| `read_only` | always `true` |
| `validation[]` | one verdict per uploaded file: `accepted`, `accepted with a limit`, `rejected`, `set aside`, with the reason |
| `findings[]` | what the workflow found; each has a `type` plus the figures |
| `proposed_actions[]` | what should happen next, each with `requires_approval: true` |
| `totals` | the headline numbers |
| `not_done[]` | every step skipped and why |
| `sources[]` | where the data came from (Mosofin read or file name) |
| `mock_data` | `true` if any Mosofin reply was flagged as mock data |
| `settings_used` | the exact settings for this run |

Downstream steps should check `status` first, show `summary`, and act only on `proposed_actions[]`
once a person has approved them.

## Set up in n8n

1. Import `workflow.json` (Workflows → Import from file).
2. Create a **Header Auth** credential named `Mosofin API Key` with your Mosofin service token. The
   key never goes into the workflow itself.
3. Open the **Settings** node and set `company`, `datasource`, `data_source_id` and the workflow's
   own settings.
4. Activate it. Call the webhook with the input envelope, or let the schedule run.

## Changing a workflow

Don't edit the generated files. The source is `.github/workflows-src/`:
`specs.js` holds one spec per workflow (settings, reads, file roles, compute logic, sample data);
`lib.js` holds the shared helpers and the envelope; `build.js` generates every folder and runs each
workflow's logic on its sample input. Then:

```bash
node .github/workflows-src/build.js
node .github/validate-workflows.js
```

CI fails if a generated file is out of date or a workflow breaks a read-only rule.
