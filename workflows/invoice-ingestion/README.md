# Invoice ingestion and coding

Turns supplier invoice lines into bill drafts: matches the vendor to the vendor list, codes each line to a GL account by keyword rules, and flags unknown vendors and lines no rule covers. Proposes the bills; enters nothing.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-invoice-ingestion` |
| Mosofin reads | `search_vendors` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `invoice_lines` | supplier invoice lines | `vendor` / `supplier`, `invoice_no` / `invoice` / `number`, `description` / `item`, `amount` / `line_amount` / `total` | yes |
| `vendors` | vendor list | `name` / `vendor` / `display_name` | no |

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
| `default_expense_account` | `"6999 Uncategorised: review"` | Account used when no rule matches; such lines are flagged |
| `coding_rules` | `[{"keyword":"software\|subscription\|licen","account":"6150 Software"},{"keyword":"freight\|shipping\|courier","account":"5200 Freight In"},{"keyword":"rent\|lease","account":"6100 Rent"},{"keyword":"repair\|maintenance","account":"6170 Repairs and Maintenance"},{"keyword":"pallet\|wrap\|packag\|corner board","account":"5100 Packaging"}]` | Ordered list of { keyword (regex), account }; first match codes the line |

## What it does

- Input is invoice lines as CSV/rows. Scanned PDFs or images need an extraction step first (for example an LLM node before the webhook) that produces these columns.
- Groups lines into invoices by vendor + invoice number.
- Vendor checked against Mosofin vendors (file fallback); an unknown vendor gets a proposed `create_vendor`.
- Each line coded by the first matching `coding_rules` keyword; unmatched lines go to `default_expense_account` and are flagged.

## Output

- `proposed_actions[]`: `bill_draft` per invoice (coded lines, basis per line), `create_vendor` for unknown vendors.
- `findings[]`: `unknown_vendor`, `uncoded_line`.
