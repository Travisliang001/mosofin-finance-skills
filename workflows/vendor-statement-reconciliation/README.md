# Vendor statement reconciliation

Reconciles a supplier's statement to the bills and payments in the books for that vendor: items on the statement but not in the books, items in the books not on the statement, and amount differences on the same reference.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-vendor-statement-reconciliation` |
| Mosofin reads | `search_bills` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `statement` | supplier statement | `date`, `reference` / `invoice` / `invoice_no` / `doc`, `amount` / `debit` | yes |
| `ap_ledger` | A/P ledger for the vendor | `reference` / `bill_no` / `invoice` / `doc_number`, `amount` / `total` | no |

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
| `vendor` | `""` | Vendor whose statement this is (as named in the books) |
| `as_at` | `""` | As-at date (YYYY-MM-DD); empty = run date |
| `amount_tolerance` | `0.01` | Differences at or below this are ignored |

## What it does

- The statement is required; the vendor's bills come from Mosofin (A/P ledger file as fallback).
- Statement lines matched to book records by normalised reference.
- Lists statement-only items, book-only items and same-reference amount differences, then proves those explain the total difference.

## Output

- `proposed_actions[]`: `vendor_query` per item that needs the vendor (missing documents, amount differences).
- `findings[]`: `on_statement_not_in_books`, `in_books_not_on_statement`, `amount_differs`.
- `totals.unexplained` must be 0 for the reconciliation to be complete.
