# Expense receipt checker

Checks a batch of employee expense lines against policy: per-category limits, a receipt over a set amount, weekend spend and duplicates within the batch. Returns the clean lines per employee for approval and the exceptions for a person.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-expense-receipts` |
| Mosofin reads | none (file-driven) |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `expenses` | expense report lines | `employee` / `name`, `date`, `merchant` / `vendor`, `category`, `amount` | yes |

Every file is validated on its **content** before any work: right kind of document, right company,
usable. A rejected required file stops the run (`status: "error"`); a rejected optional file is
skipped and named in `not_done` (`status: "partial"`).

## Settings

All in the **Settings** node; any can be overridden per run via `settings` in the body.

| Setting | Default | Meaning |
|---|---|---|
| `company` | `""` | Company the run is for; a file naming another company is rejected |
| `currency` | `"USD"` | Reporting currency, echoed in the envelope |
| `datasource` | `"quickbooks"` | Mosofin datasource name (e.g. quickbooks, xero) |
| `data_source_id` | `""` | Mosofin data source id; sent on every Mosofin call |
| `category_limits` | `{"meals":75,"hotel":250,"taxi":60,"mileage":200,"other":500}` | Per-line limit by category; a category not listed uses `other` |
| `receipt_required_over` | `25` | Lines above this need a receipt |
| `flag_weekends` | `true` | Flag spend dated Saturday or Sunday |
| `duplicate_window_days` | `0` | Same employee, merchant and amount within this many days is a duplicate (0 = same day) |

## What it does

- File-driven: one CSV of expense lines (a `receipt` yes/no column is read if present).
- Per line: category limit, receipt over `receipt_required_over`, weekend date.
- Across the batch: same employee + merchant + amount within `duplicate_window_days`.
- Clean lines are proposed for reimbursement per employee; a line with any exception is held.

## Output

- `proposed_actions[]`: `approve_reimbursement` per employee (clean lines only, held amount shown).
- `findings[]`: `over_policy_limit`, `missing_receipt`, `weekend_expense`, `duplicate_in_batch`.
