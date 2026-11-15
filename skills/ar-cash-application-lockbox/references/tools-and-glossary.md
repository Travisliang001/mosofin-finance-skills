<!-- ar-cash-application-lockbox · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 6. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Open invoices to match against | `search_invoices` | `start_date`, `end_date` (required), `customer_id`, `query`/`name` (DocNumber), `max_results`, `offset` |
| One invoice in full (incl. customer PO) | `read_invoice` | `id` |
| What is open and how old | `get_aged_receivables` | `report_date`, `customer`, `aging_method`, `num_periods` |
| Customer receipts as recorded | `search_payments` | `start_date`, `end_date` (required), `customer_id` |
| One receipt and what it was applied to | `get_payment` | `id` |
| How receipts were banked (batches) | `search_deposits` / `get_deposit` | `start_date`, `end_date` (required); `id` |
| Point-of-sale receipts with no invoice | `search_sales_receipts` / `get_sales_receipt` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Credits that may explain a short-pay | `search_credit_memos` / `get_credit_memo` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Refunds issued | `search_refund_receipts` / `get_refund_receipt` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Customer master (payer identification) | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Total owed per customer (tie-out) | `get_customer_balance` | `report_date`, `customer` |
| Payment methods in use | `search_payment_methods` / `get_payment_method` | `query`/`name`, `active_only`; `id` |
| Unapplied cash and bank accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Movement on those accounts | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| A/R control balance | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| Transfers between own accounts | `search_transfers` | `start_date`, `end_date` (required) |
| Base currency and time zone | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description
wins.

---

## Plain-language glossary

- **Cash application** — working out which invoices each incoming payment was meant to settle.
- **Lockbox** — a bank service that receives and banks your customer payments for you.
- **Remittance advice** — the note from a customer saying which invoices a payment covers.
- **ACH / wire / card** — ways money moves electronically.
- **EDI** — a structured electronic format larger customers use to send remittance data.
- **Bank trace identifier** — the bank's own reference for a transfer, used to find it later.
- **Short-pay** — the customer paid less than the invoice.
- **Deduction** — the amount a customer withheld, and the case opened to resolve it.
- **Reason code** — a short label for *why* a customer short-paid (shipping, pricing, quantity,
  discount, damage).
- **Overpay** — the customer paid more than the invoice.
- **Unapplied cash** — money received that has not yet been matched to an invoice.
- **Write-off** — deciding not to chase a small difference and removing it from the books.
- **Batch split** — one deposit covering many receipts, or one day's receipts banked in
  several deposits.
- **Gross vs net** — before and after fees deducted.
- **Tie-out** — the proof that two sets of numbers agree.
- **Accounts receivable (A/R)** — money customers owe you.
- **Journal entry** — the balanced two-sided record. **DR** = debit, **CR** = credit.
