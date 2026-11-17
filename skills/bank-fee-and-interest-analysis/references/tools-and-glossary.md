<!-- bank-fee-and-interest-analysis · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 7. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Locate fee, interest, merchant and cash accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Every posted fee, line by line | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Monthly fee trend at summary level | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| Fees posted as expenses or card charges | `search_purchases` / `get_purchase` | `start_date`, `end_date` (required); `id` |
| Deposit counts, and the netting check | `search_deposits` / `get_deposit` | `start_date`, `end_date` (required); `id` |
| Transfers between own accounts (wire driver) | `search_transfers` / `get_transfer` | `start_date`, `end_date` (required); `id` |
| Outbound payment counts (ACH / cheque driver) | `search_bill_payments` / `get_bill_payment` | `start_date`, `end_date` (required); `id` |
| Inbound receipt counts (merchant-fee driver) | `search_payments` / `search_sales_receipts` | `start_date`, `end_date` (required), `customer_id` |
| How payment methods are labelled here | `search_payment_methods` / `get_payment_method` | `query`/`name`, `active_only`; `id` |
| Average cash balances (interest and ECR base) | `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by` |
| Cash movement over the period | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| Fee entries posted as journals | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Dimensions, for miscoding checks | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Base currency and calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Account analysis statement** — the bank's own itemised monthly breakdown of every service and
  charge. Far more useful than a normal statement, and worth asking for by name.
- **ACH** — a low-cost electronic bank-to-bank payment. **Wire** — a faster, much more expensive
  one.
- **Lockbox** — a bank service that receives and banks your customer payments for you.
- **Treasury management services** — bank add-ons like sweeps, positive pay and reporting.
- **Positive pay** — a fraud control where the bank checks each cheque against a list you sent.
- **Merchant discount rate** — the percentage of each card sale the processor keeps.
- **Per-item fee** — a flat charge per transaction, on top of any percentage.
- **Chargeback** — a customer's card issuer reversing a payment, usually with a fee attached.
- **Interchange-plus / flat-rate / tiered** — three ways card processing is priced. Which is
  cheapest depends on your transaction mix.
- **ECR (earnings credit rate)** — a notional interest rate banks apply to your average balance
  and use to offset fees instead of paying interest.
- **Netted fee** — a charge deducted before the money reaches you, so it never appears as an
  expense.
- **Gross up** — recording the full amount received and the fee separately, rather than just the
  net.
- **Driver** — what makes a cost change: a **fixed** fee is charged regardless of activity, a
  **volume** fee scales with transactions.
- **Unit rate** — cost per transaction; the fee divided by the count.
- **MoM / YoY** — month on month / year on year.
- **Dimension** — an extra coding tag on a transaction (department, class, project).
- **Journal entry (JE)** — the balanced two-sided record. **DR** = debit, **CR** = credit.
