# Vendor onboarding check

Checks new-vendor details before setup: required fields present, TIN in a valid format, and no existing vendor with the same name or TIN. Clean vendors are proposed for creation; the rest get a request for the missing information.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-vendor-onboarding` |
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
| `new_vendors` | new vendor form / W-9 data | `legal_name` / `name`, `tin` / `ein` / `tax_id` | yes |
| `vendors` | existing vendor list | `name` / `vendor` / `display_name` | no |

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
| `required_fields` | `["legal_name","tin","address","email","payment_terms","tax_classification"]` | Columns that must be filled for a vendor to be set up |
| `tin_digits` | `9` | Digits a TIN must have (US EIN/SSN: 9) |

## What it does

- One row per new vendor; columns named as in `required_fields`.
- Checks completeness, TIN format (digit count, not all one digit), and duplicates against existing vendors by name or TIN.
- Only the last four TIN digits appear in the output.

## Output

- `proposed_actions[]`: `create_vendor` when clean; `information_request` when fields are missing or the TIN is malformed.
- `findings[]`: `missing_fields`, `tin_invalid_format`, `possible_duplicate_vendor`.
