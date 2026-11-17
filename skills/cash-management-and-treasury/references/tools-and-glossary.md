<!-- cash-management-and-treasury · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 11. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **Every cash, bank and investment account** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Balances per account** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Movement per account — dormancy detection** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Inflow / outflow volumes and shape | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| Inflow mechanics | `search_deposits` / `search_payments` / `search_sales_receipts` | `start_date`, `end_date` (required) |
| Outflow mechanics and payment-run pattern | `search_bill_payments` / `search_purchases` | `start_date`, `end_date` (required), `vendor_id` |
| **Transfers between own accounts — informal concentration** | `search_transfers` / `get_transfer` | `start_date`, `end_date` (required); `id` |
| Payment methods actually used | `search_payment_methods` | `query`/`name`, `active_only` |
| **New payees shortly before large payments (BEC signal)** | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| Bank fees and interest earned (KPIs) | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Transactional FX exposure | `search_invoices` / `search_bills` | `start_date`, `end_date` (required) |
| Working capital, for the liquidity floor | `get_aged_receivables` / `get_aged_payables` | `report_date` |
| Legal name, base currency, country | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no tool for signatories, bank access permissions, approval records, or facility terms
because none exists.**

---

## Plain-language glossary

- **Treasury** — the function that manages how cash is held, moved and protected.
- **Operating account** — the account day-to-day money flows through.
- **Concentration account** — an account cash is swept into, so it sits in one place.
- **Cash pooling** — combining balances across entities. **Physical pooling** actually moves the
  money; **notional pooling** only offsets balances for interest purposes.
- **In-house bank** — a group entity that acts as banker to its affiliates.
- **Sweep** — an automatic transfer of surplus cash into a concentration or investment account.
- **Trapped cash** — cash that cannot legally or practically be moved out of an entity or country.
- **Counterparty risk** — the risk that the bank holding your cash fails.
- **Deposit insurance** — the government-guaranteed portion of a bank balance.
- **Days of cash on hand** — cash divided by average daily operating outflow; how long you could run
  on what you have.
- **Idle cash** — balances earning nothing.
- **Commercial paper / money market fund / time deposit / repo** — short-term places to park surplus
  cash, in decreasing order of familiarity.
- **Weighted-average maturity (WAM)** — how long, on average, the portfolio is tied up.
- **Positive pay** — a bank service that checks each cheque against a list you sent.
- **Dual control** — requiring two people to release a payment.
- **Segregation of duties** — the person who sets up a payment is not the person who approves it.
- **Business email compromise (BEC)** — fraud where someone impersonates a supplier or executive to
  redirect a payment. The leading corporate payment fraud.
- **Callback verification** — phoning a known number to confirm new bank details, never the number
  in the email.
- **Transactional vs. translational FX exposure** — risk from money owed in another currency, versus
  risk from owning a foreign business.
- **Hedge accounting** — matching the accounting for a hedge to the thing it hedges.
- **Thin capitalisation** — tax rules limiting deductions where a group entity is funded mostly by
  intercompany debt.
- **Arm's-length interest** — the rate unrelated parties would charge, required on intercompany
  loans.
- **Authority matrix** — the table of who may do what, up to what value.
