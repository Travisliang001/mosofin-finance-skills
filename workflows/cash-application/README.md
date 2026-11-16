# Cash application matcher

Proposes which open invoices each customer payment pays: invoice numbers in the remittance first, then an exact single-invoice amount, then a combination of up to three of that customer's invoices. Anything ambiguous is left for a person with the candidates listed.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-cash-application` |
| Mosofin reads | `search_invoices`, `search_payments` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `payments` | customer receipts / remittance list | `payer` / `customer` / `customer_name`, `amount`, `date` | no |
| `invoices` | open A/R invoice list | `customer` / `customer_name`, `invoice` / `invoice_no` / `doc_number`, `balance` / `open_balance` / `amount_due` | no |

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
| `amount_tolerance` | `0.01` | Amounts this close count as equal |
| `max_combination` | `3` | Largest number of invoices one payment may be split across (2 or 3) |

## What it does

- Payments and open invoices come from Mosofin, or from files.
- Order of evidence: invoice numbers quoted in the remittance (must sum to the payment); one invoice of that customer with exactly the amount; a combination of up to `max_combination` of that customer's invoices.
- Never picks between equal candidates: several same-amount invoices is an `ambiguous_match` for a person.

## Output

- `proposed_actions[]`: `apply_payment` with the invoices and the basis for each match.
- `findings[]`: `ambiguous_match`, `unapplied_payment` (with the customer's open invoices to choose from).
