# GL flux monitor

Compares each P&L account this period with the prior period and flags movements over both a percentage and an absolute threshold, plus accounts that went to zero or appeared from nothing. Asks the account owner for an explanation.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 3 * *` + webhook `POST /webhook/mosofin-gl-flux-monitor` |
| Mosofin reads | `get_profit_and_loss`, `get_profit_and_loss` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `current` | P&L by account (current period) | `account`, `amount` / `total` / `balance` | no |
| `prior` | P&L by account (prior period) | `account`, `amount` / `total` / `balance` | no |

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
| `prior_start` | `""` | First day of the comparison period |
| `prior_end` | `""` | Last day of the comparison period |
| `flux_pct` | `15` | Percent change that trips a flag (both thresholds must trip) |
| `flux_abs` | `2500` | Absolute change that trips a flag |
| `account_owners` | `{}` | { "account": "owner" } for explanation requests |
| `default_owner` | `"Controller"` | Owner when an account has none |

## What it does

- Reads the P&L by account for the period and the comparison period (files as fallback).
- Flags an account when the change passes BOTH `flux_pct` and `flux_abs`; also `went_to_zero` and `new_activity` above `flux_abs`.
- Groups flagged accounts by owner into one explanation request each.

## Output

- `findings[]`: `increase`, `decrease`, `went_to_zero`, `new_activity` with both figures and the change.
- `proposed_actions[]`: `explanation_request` per owner, with a ready message.
