<!-- audit-prep-pbc-list · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on discovery; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections and their `connected` flag. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (required when several files are live) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call**), `approved` (only after an explicit yes) |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 9. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Trial balance (the foundational schedule) | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| Balance sheet / P&L / cash flow | `get_balance_sheet` / `get_profit_and_loss` / `get_cash_flow` | `start_date`, `end_date`, `accounting_method`, `summarize_column_by` |
| Transaction detail behind any balance | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Chart of accounts (area mapping) | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| A/R and A/P agings (subledger support) | `get_aged_receivables` / `get_aged_payables` | `report_date`, `customer`/`vendor`, `aging_method`, `num_periods` |
| Subledger totals for the GL tie-out | `get_customer_balance` / `get_vendor_balance` | `report_date`, `customer`/`vendor` |
| Revenue by month and by customer | `get_profit_and_loss` / `get_customer_sales` | `start_date`, `end_date`, `summarize_column_by`, `customer` |
| Sample invoices and their detail | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Credit memos and refunds | `search_credit_memos` / `search_refund_receipts` | `start_date`, `end_date` (required) |
| Post-period bills (unrecorded liabilities search) | `search_bills` / `search_bill_payments` | `start_date`, `end_date` (required), `vendor_id` |
| Manual journal entries (audit focus) | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Item master (inventory listing) | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Customers and vendors (related-party starting point) | `search_customers` / `search_vendors` | `query`/`name`, `active_only` |
| Classes and departments (segment support) | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Attachment metadata (a document exists) | `search_attachables` / `get_attachable` | `query`/`name`; `id` |
| Industry, year-end, base currency | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description
wins.

---

## Plain-language glossary

- **PBC (prepared by client)** — the list of schedules and documents the auditors ask *you* to
  prepare.
- **Audit / review / compilation** — decreasing levels of assurance. An audit gathers evidence
  and gives an opinion; a review applies analytics and enquiry; a compilation just presents the
  numbers.
- **Fieldwork** — the period when the auditors are actively testing, usually on site.
- **Trial balance (TB)** — every account and its balance; the foundation everything ties to.
- **General ledger (GL)** — the full transaction-level record behind those balances.
- **Subledger** — the detailed list behind a control account (e.g. the A/R aging behind the A/R
  balance).
- **Tie-out** — the proof that a schedule agrees with the audited number.
- **Roll-forward** — opening balance, movements, closing balance.
- **Control account** — the single summary total in the GL that a subledger must agree with.
- **Confirmation** — a letter the auditor sends to a bank, customer or lender asking them
  directly to confirm a balance. **Auditor-initiated** — you supply contacts and authorization,
  not the reply.
- **Search for unrecorded liabilities** — the auditor's procedure of looking at what was paid
  after year-end to find costs that belonged before it.
- **Subsequent events** — things happening after period end that affect the period's numbers.
- **Management letter** — the auditor's written observations on weaknesses found.
- **Audit adjustment** — a correction the auditor proposes to the draft numbers.
- **Materiality** — the size above which a misstatement would change a reader's decision.
- **Allowance / reserve** — an estimate set aside for money you may not collect or stock you may
  not sell.
- **Impairment** — an asset being worth less than the value carried in the books.
- **Contingency** — a possible obligation that depends on a future event, such as a lawsuit.
- **Going concern** — whether the entity can keep operating for the foreseeable future.
- **Related party** — a person or business connected to the entity (an owner, a director, an
  affiliate) whose transactions need separate disclosure.
- **Component auditor** — an auditor of one entity within a group audit.
- **Provenance** — the record of exactly which call produced a figure, with what parameters and
  when.
