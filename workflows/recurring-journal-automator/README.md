# Recurring journal check

Checks that each recurring entry (rent, depreciation, subscriptions, amortisation) was posted this period at its usual amount. Missing ones come back as proposed journal entries; amounts that drifted are flagged.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 28 * *` + webhook `POST /webhook/mosofin-recurring-journal-automator` |
| Mosofin reads | `get_general_ledger` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `gl` | general ledger detail | `account`, `amount` / `debit` | no |

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
| `period_start` | `""` | First day of the period (YYYY-MM-DD) |
| `period_end` | `""` | Last day of the period (YYYY-MM-DD) |
| `drift_pct` | `5` | Posted amount differing from the rule by more than this percent is flagged |
| `recurring_rules` | `[{"name":"Office rent","debit_account":"6100 Rent","credit_account":"2000 Accounts Payable","amount":4400},{"name":"Monthly depreciation","debit_account":"6800 Depreciation","credit_account":"1590 Accumulated Depreciation","amount":3125},{"name":"Software subscriptions","debit_account":"6150 Software","credit_account":"2100 Accrued Liabilities","amount":7300}]` | The recurring entries: { name, debit_account, credit_account, amount } |

## What it does

- `recurring_rules` holds every recurring entry; edit it, nothing is hardcoded.
- For each rule, sums what was posted to its debit account in the period.
- Nothing posted: proposes the entry. Posted but more than `drift_pct` off: flags the drift.

## Output

- `proposed_actions[]`: `journal_entry` (balanced) for each missing recurring entry.
- `findings[]`: `recurring_entry_missing`, `amount_drift`.
