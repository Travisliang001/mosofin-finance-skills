# Fixed asset rollforward

Rolls the fixed asset register forward for the period (opening cost, additions, disposals, closing) and checks straight-line depreciation posted per asset against what the register says it should be. Missing depreciation comes back as a proposed entry.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 28 * *` + webhook `POST /webhook/mosofin-fixed-asset-rollforward` |
| Mosofin reads | `get_general_ledger` |
| Output | one JSON envelope v1.0 ([output.schema.json](output.schema.json), example [sample-output.json](sample-output.json)) |

## Input

Webhook body ([input.schema.json](input.schema.json), example [sample-input.json](sample-input.json)):

```json
{ "settings": { "<setting>": "<value for this run>" },
  "files": [ { "name": "file.csv", "role": "<role>", "content": "<CSV text>" } ] }
```

| File role | What it must be | Columns it needs | Required |
|---|---|---|---|
| `register` | fixed asset register | `asset_id` / `asset`, `cost`, `in_service_date` / `in_service` / `acquired`, `life_months` / `useful_life_months` | yes |
| `depreciation_gl` | depreciation postings | `amount` / `debit`, `memo` / `description` / `asset_id` | no |

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
| `depreciation_account` | `"6800 Depreciation"` | Expense account depreciation is posted to (read from the GL) |
| `accumulated_account` | `"1590 Accumulated Depreciation"` | Credit side of proposed depreciation entries |
| `materiality` | `1` | Differences below this per asset are ignored |

## What it does

- The register is required (asset id, cost, in-service date, life in months; salvage and disposal date optional).
- Cost rollforward: opening + additions - disposals = closing for the period.
- Expected depreciation: straight line, full month from the in-service month, stops at end of life or the disposal month.
- Posted depreciation is attributed to an asset when its memo contains the asset id; differences over `materiality` are flagged.

## Output

- `totals`: the cost rollforward and expected vs posted depreciation.
- `proposed_actions[]`: `journal_entry` for each asset with no depreciation posted.
- `findings[]`: `depreciation_not_posted`, `depreciation_variance`, `unattributed_depreciation`.
