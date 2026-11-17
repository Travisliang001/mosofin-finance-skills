# Duplicate invoice detection

Scans bills (open and paid) for likely duplicates: the same vendor with the same invoice number once punctuation and prefixes are stripped, or the same vendor and amount within a few days. Each pair comes back with a proposed hold on the later bill.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 6 * * *` + webhook `POST /webhook/mosofin-duplicate-invoice-detection` |
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
| `bills` | bill register | `vendor` / `vendor_name`, `bill_no` / `invoice` / `doc_number` / `bill`, `amount` / `total`, `date` / `bill_date` | no |

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
| `as_at` | `""` | As-at date (YYYY-MM-DD); empty = run date |
| `lookback_days` | `365` | Only bills dated within this many days of as_at are compared |
| `near_days` | `7` | Same vendor + same amount within this many days counts as a possible duplicate |
| `amount_tolerance` | `0.01` | Amounts this close count as equal |

## What it does

- Takes bills from Mosofin (file fallback) within `lookback_days`, open and paid alike.
- A pair is flagged when the vendor matches and either the invoice numbers match after normalising (`INV-4471` = `INV4471` = `4471`), or the amounts match within `near_days`.
- Confidence is high when both number and amount match.

## Output

- `findings[]`: `same_invoice_number` / `same_amount_near_date` with both bills side by side.
- `proposed_actions[]`: `hold_bill` on the later bill (or a refund note if it is already paid).
