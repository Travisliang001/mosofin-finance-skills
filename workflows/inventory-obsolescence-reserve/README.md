# Inventory obsolescence reserve

Ages each item by days since its last sale, applies a tiered reserve percentage, and compares the required reserve with the one on the books. Proposes the adjusting entry.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 25 3,6,9,12 *` + webhook `POST /webhook/mosofin-inventory-obsolescence-reserve` |
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
| `items` | inventory listing with last-sale dates | `sku` / `item`, `qty` / `on_hand` / `quantity`, `unit_cost` / `cost`, `last_sale` / `last_sale_date` / `last_sold` | yes |

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
| `as_at` | `""` | As-at date (YYYY-MM-DD); empty = run date |
| `aging_tiers` | `[{"days":180,"reserve_pct":25},{"days":365,"reserve_pct":50},{"days":540,"reserve_pct":100}]` | Days since last sale -> reserve percent; the highest tier reached applies |
| `never_sold_pct` | `100` | Reserve percent for items with no sale date |
| `existing_reserve` | `0` | Reserve balance on the books now |
| `reserve_account` | `"1390 Inventory Reserve"` | Contra-inventory account |
| `expense_account` | `"5050 Inventory Obsolescence"` | P&L account for the adjustment |

## What it does

- File-driven: an inventory listing with quantity, unit cost and last-sale date.
- Days since last sale picks the highest `aging_tiers` tier reached; no sale date uses `never_sold_pct`.
- Required reserve minus `existing_reserve` is the proposed adjustment (either direction).

## Output

- `findings[]`: `slow_moving` / `never_sold` per item with value, age, percent and reserve, largest first.
- `proposed_actions[]`: one balanced `journal_entry` for the adjustment.
