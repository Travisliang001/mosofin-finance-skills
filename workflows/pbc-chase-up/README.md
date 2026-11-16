# Audit PBC chase-up

Tracks a prepared-by-client (PBC) request list: what is received, overdue or due soon. Drafts one reminder per owner listing only their open items.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 9 * * 1-5` + webhook `POST /webhook/mosofin-pbc-chase-up` |
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
| `pbc_list` | PBC request list | `item` / `request` / `description`, `owner`, `due` / `due_date` | yes |
| `received` | list of documents received | `item` / `request` | no |

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
| `due_soon_days` | `3` | Items due within this many days are included as due soon |
| `engagement` | `"year-end audit"` | Engagement name used in drafts |
| `sender_name` | `"Finance"` | Signature |
| `subject_template` | `"{{engagement}}: {{count}} open request(s) for you"` | Reminder subject |
| `body_template` | `"Hi {{owner}},\n\nFor the {{engagement}}, these requests are still open:\n\n{{lines}}\n\nPlease upload them or let me know what is holding them up.\n\nThanks,\n{{sender}}"` | Reminder body; {{lines}} lists the items |

## What it does

- File-driven: the PBC list (with optional `status`) plus an optional received-documents list.
- An item is received if its status says so or it appears on the received list.
- Open items are overdue, due within `due_soon_days`, or missing a due date; later items are left alone.
- One reminder per owner with only their items.

## Output

- `proposed_actions[]`: `email_draft` per owner.
- `findings[]`: `overdue`, `due_soon`, `no_due_date`.
