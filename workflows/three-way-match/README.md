# Three-way match

Checks each bill line against its purchase order and goods-received record. Price and quantity variances over tolerance, bills with no PO line, and billing beyond what was received come back as exceptions with a proposed hold.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-three-way-match` |
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
| `purchase_orders` | purchase order lines | `po` / `po_number`, `item` / `sku`, `qty` / `quantity`, `unit_price` / `price` | yes |
| `receipts` | goods received lines | `po` / `po_number`, `item` / `sku`, `qty_received` / `qty` / `quantity` | no |
| `bills` | bill lines | `bill` / `bill_no` / `invoice`, `po` / `po_number`, `item` / `sku`, `qty` / `quantity`, `unit_price` / `price` | no |

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
| `price_tolerance_pct` | `2` | Allowed unit-price difference vs the PO, in percent |
| `qty_tolerance` | `0` | Units a bill may exceed the received (or ordered) quantity by |

## What it does

- Purchase orders are required; bill lines come from Mosofin, or a file if Mosofin has none.
- Each bill line is matched to its PO line by PO number + item.
- Price: flags a unit-price difference over `price_tolerance_pct`.
- Quantity: billed vs received (three-way). With no receipts file it checks billed vs ordered and says plainly that it is two-way only.

## Output

- `proposed_actions[]`: `hold_bill` per bill with an exception.
- `findings[]`: `price_variance`, `billed_more_than_received` / `billed_more_than_ordered`, `no_matching_po_line`, `two_way_only`.
