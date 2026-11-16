# Bank reconciliation

Matches a bank statement against the cash account in the books. Exact-amount matches within a date window are paired; everything else is an exception on one side. Bank-only fees and interest come back as proposed journal entries.

**Read-only.** Reads Mosofin and the files sent on the trigger; posts, sends, pays and changes nothing.
Whatever should happen next comes back in `proposed_actions[]`, each with `requires_approval: true`,
for a downstream step (email connector, chat, another MCP tool) to act on once a person approves.

| | |
|---|---|
| Trigger | webhook `POST /webhook/mosofin-bank-reconciliation` |
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
| `bank_statement` | bank statement | `date` / `posted_date` / `transaction_date`, `amount`, `description` / `memo` / `payee` / `details` | yes |
| `gl_cash` | cash account ledger | `date` / `txn_date`, `amount` / `net`, `description` / `memo` / `name`, `ref` / `num` / `doc_number` / `type` | no |

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
| `cash_account` | `"1000 Operating Cash"` | GL cash account to reconcile (name or number as Mosofin returns it) |
| `period_start` | `""` | First day of the period (YYYY-MM-DD) |
| `period_end` | `""` | Last day of the period (YYYY-MM-DD) |
| `date_window_days` | `5` | Max days between bank and book dates for an exact-amount match |
| `bank_charge_keywords` | `["fee","charge","interest","service"]` | Bank-only lines whose description contains one of these get a proposed journal entry |
| `bank_fee_account` | `"6900 Bank Charges"` | Debit account for proposed fee entries |
| `interest_income_account` | `"4900 Interest Income"` | Credit account for proposed interest entries |
| `statement_closing_balance` | `null` | Optional; with book_closing_balance, proves the reconciliation ties |
| `book_closing_balance` | `null` | Optional; GL cash balance at period end |

## What it does

- Validates the statement first; without a usable statement the run stops with `status: "error"`.
- Pairs bank and book lines with the exact same amount within `date_window_days`, closest date first.
- Unmatched bank lines: fees/interest (by `bank_charge_keywords`) get a proposed journal entry; the rest are listed with any same-amount candidates outside the window.
- Unmatched book lines become outstanding payments or deposits in transit.
- With both closing balances set, proves the reconciliation ties and reports any unexplained difference.

## Output

- `proposed_actions[]`: `journal_entry` (balanced lines) for bank-only fees and interest only.
- `findings[]`: `bank_charge_not_in_books`, `in_bank_not_in_books`, `outstanding_payment`, `deposit_in_transit`, `reconciliation_does_not_tie`.
- `totals.matched_pairs` lists every pairing.
