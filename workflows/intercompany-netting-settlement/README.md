# Intercompany reconciliation and netting

Checks that each pair of group entities agrees on what they owe each other, lists the mismatches, and proposes the fewest settlement payments that clear the agreed balances.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 8 26 * *` + webhook `POST /webhook/mosofin-intercompany-netting-settlement` |
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
| `balances` | intercompany balances by entity and counterparty | `entity`, `counterparty`, `balance` / `amount` | yes |

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
| `tolerance` | `1` | Pair differences at or below this are treated as agreed |
| `entities` | `[]` | Limit to these entities; empty = every entity in the file |

## What it does

- File-driven: one row per entity per counterparty; positive = receivable from the counterparty, negative = payable.
- Each pair must mirror (A says +x, B says -x) within `tolerance`; mismatched pairs are listed and left out of netting.
- Agreed balances become net positions per entity, settled greedily largest-first: the fewest payments for this set.

## Output

- `findings[]`: `pair_does_not_agree` with both sides and the difference.
- `proposed_actions[]`: `settlement_payment` from, to, amount.
- `totals.net_positions`: each entity's net receivable (+) or payable (-).
