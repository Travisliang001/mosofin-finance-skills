# Month-end close status

Checks the close from evidence, not from ticks: the trial balance balances, suspense and clearing accounts are empty, and each checklist task has a status. Lists what blocks the close and nudges each owner.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 1-7 * *` + webhook `POST /webhook/mosofin-month-end-close-orchestrator` |
| Mosofin reads | `get_trial_balance` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `trial_balance` | trial balance | `account`, `debit` / `balance` / `amount` | no |
| `task_status` | close task status list | `task`, `status` | no |

Every file is validated on its **content** before any work: right kind of document, right company,
usable. A rejected required file stops the run (`status: "error"`); a rejected optional file is
skipped and named in `not_done` (`status: "partial"`). Where a role mirrors a Mosofin read, the Mosofin data is used first and the file is the fallback.

## Settings

All in the **Settings** node; any can be overridden per run via `settings` in the body.

| Setting | Default | Meaning |
|---|---|---|
| `company` | `""` | Company the run is for; a file naming another company is rejected |
| `currency` | `"USD"` | Reporting currency, echoed in the envelope |
| `datasource` | `"quickbooks"` | Mosofin datasource name (e.g. quickbooks, xero) |
| `data_source_id` | `""` | Mosofin data source id; sent on every Mosofin call |
| `period_end` | `""` | Last day of the period (YYYY-MM-DD) |
| `tolerance` | `0.01` | Rounding tolerance for the trial-balance check |
| `suspense_accounts` | `["suspense","ask my accountant","uncategorized","clearing"]` | Account-name fragments treated as suspense/clearing; must be zero |
| `checklist` | `[{"task":"Bank reconciliations","owner":"AP lead","check":"status"},{"task":"Accruals posted","owner":"GL accountant","check":"status"},{"task":"Payroll reconciled","owner":"Payroll","check":"status"},{"task":"Depreciation posted","owner":"GL accountant","check":"status"},{"task":"Trial balance balances","owner":"Controller","check":"tb_balances"},{"task":"Suspense accounts cleared","owner":"Controller","check":"suspense_zero"}]` | Close tasks: { task, owner, check } where check is `status` (from the task_status file), `tb_balances` or `suspense_zero` |

## What it does

- `checklist` is fully configurable: each task has an owner and a check type.
- `tb_balances`: trial balance debits = credits within `tolerance`.
- `suspense_zero`: every account whose name contains a `suspense_accounts` fragment is zero.
- `status`: read from an uploaded task-status list; a task with no status is "not evidenced", never assumed done.

## Output

- `totals.checklist[]`: every task with status `done` / `open` / `blocked` / `not evidenced`.
- `proposed_actions[]`: `owner_nudge` per owner with their outstanding tasks.
- `findings[]`: `trial_balance_out_of_balance`, `suspense_not_cleared`, `task_open`, `task_blocked`, `task_not_evidenced`.
