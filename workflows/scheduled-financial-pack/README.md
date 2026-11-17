# Scheduled financial pack

Each month, assembles the P&L and balance sheet with prior-period comparatives and highlights, as structured data for a downstream renderer, dashboard or email step. Checks the balance sheet balances before anything goes out.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 9 5 * *` + webhook `POST /webhook/mosofin-scheduled-financial-pack` |
| Mosofin reads | `get_profit_and_loss`, `get_profit_and_loss`, `get_balance_sheet` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `pl` | P&L by account | `account`, `amount` / `total` | no |
| `pl_prior` | prior-period P&L by account | `account`, `amount` / `total` | no |
| `bs` | balance sheet by account | `account`, `amount` / `balance` / `total` | no |

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
| `prior_start` | `""` | Comparison period start |
| `prior_end` | `""` | Comparison period end |
| `highlight_pct` | `10` | Line movements over this percent AND highlight_abs are highlighted |
| `highlight_abs` | `5000` | Absolute movement threshold for highlights |
| `recipients` | `[]` | Who the downstream step should send the pack to (passed through, never sent from here) |

## What it does

- Reads the P&L for the period and the comparison period, and the balance sheet at period end (files as fallback).
- Classifies accounts by type (or by account-number range when no type is given) and totals revenue, COGS, gross profit and margin, expenses, net income.
- Highlights lines whose movement passes both `highlight_pct` and `highlight_abs`.
- If the balance sheet does not balance, no delivery is proposed.

## Output

- `proposed_actions[]`: one `deliver_report` whose `payload` has the P&L lines with comparatives, totals, balance sheet and highlights, plus the configured `recipients`.
- `findings[]`: `highlight`, `balance_sheet_does_not_balance`.
