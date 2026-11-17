# Sales tax nexus monitor

Totals sales and transaction counts by ship-to state over a trailing window and compares them with each state's economic-nexus thresholds. Flags states crossed where the company is not registered, and states approaching the line.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 2 * *` + webhook `POST /webhook/mosofin-sales-tax-compliance-monitor` |
| Mosofin reads | `search_invoices` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `sales` | sales by invoice with ship-to state | `state` / `ship_to_state` / `shipping_state`, `amount` / `total` | no |

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
| `window_start` | `""` | Start of the measurement window (e.g. 12 months back) |
| `as_at` | `""` | As-at date (YYYY-MM-DD); empty = run date |
| `warn_pct` | `80` | Flag a state once sales or transactions reach this percent of its threshold |
| `registered_states` | `[]` | States where the company already collects and files |
| `thresholds` | `{"default":{"amount":100000,"transactions":200},"CA":{"amount":500000,"transactions":null},"TX":{"amount":500000,"transactions":null},"NY":{"amount":500000,"transactions":100}}` | Per-state { amount, transactions } (null = no count test); `default` for states not listed. Confirm against current state rules before relying on them. |

## What it does

- Sales by ship-to state over `window_start`..`as_at` from Mosofin invoices (file fallback).
- Each state is tested on sales and, where the state has one, transaction count; the higher percentage counts.
- Crossed and not in `registered_states` → registration review; at or above `warn_pct` → approaching.
- Thresholds are settings, not law: the README and every action say to confirm them.

## Output

- `findings[]`: `nexus_crossed_not_registered`, `approaching_nexus`, `nexus_registered`, `sales_without_state`.
- `proposed_actions[]`: `registration_review` per crossed state.
- `totals.by_state[]`: sales and counts per state.
