# AR collections sequencer

Weekly: reads open receivables, nets unapplied credits, and drafts one collection email per overdue customer, toned by how late the oldest item is. Flags customers over their credit limit.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | schedule `0 7 * * 1` + webhook `POST /webhook/mosofin-ar-collections` |
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
| `ar_open` | open A/R invoice list | `customer` / `customer_name`, `invoice` / `invoice_no` / `doc_number`, `balance` / `open_balance` / `amount_due`, `due_date` / `due` | no |
| `credits` | unapplied credits / payments list | `customer` / `customer_name`, `amount` / `unapplied` | no |

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
| `as_at` | `""` | As-at date (YYYY-MM-DD); empty = run date |
| `buckets` | `[30,60,90]` | Aging bucket upper bounds in days; the oldest overdue item picks the bucket |
| `min_balance` | `50` | No draft when the net overdue balance is below this |
| `exclude_customers` | `[]` | Customer names never chased (e.g. in dispute, legal) |
| `credit_limits` | `{}` | { "Customer": limit } — flagged when the open balance exceeds it |
| `tones` | `{"1-30":"friendly reminder","31-60":"firm reminder","61-90":"final notice","90+":"escalation: account on hold pending payment","default":"reminder"}` | Tone per bucket label; used in the subject and body |
| `sender_name` | `"Accounts Receivable"` | Signature on the draft |
| `subject_template` | `"{{company}}: {{currency}} {{net}} overdue ({{tone}})"` | Email subject; {{placeholders}} filled per customer |
| `body_template` | `"Hello {{customer}},\n\nOur records show the following invoices are past due:\n\n{{lines}}\n\nAfter credits of {{currency}} {{credit}}, {{currency}} {{net}} is outstanding. Please arrange payment or let us know if anything is in dispute.\n\nThank you,\n{{sender}}"` | Email body; {{lines}} lists the overdue invoices |

## What it does

- Groups open invoices by customer; ages each against `as_at`.
- Nets unapplied credits off the overdue amount; skips customers whose net is below `min_balance` and anyone on `exclude_customers`.
- One draft per customer listing every overdue invoice; the oldest item picks the bucket and the tone.
- Flags any customer whose open balance exceeds their `credit_limits` entry.

## Output

- `proposed_actions[]`: `email_draft` with `to`, `subject`, `body`, `amount_due`, `invoices[]` — ready for an email connector after approval.
- `findings[]`: `over_credit_limit`, `unapplied_credit_netted`, `below_min_balance`, `excluded_customer`, `no_email_on_file`.
