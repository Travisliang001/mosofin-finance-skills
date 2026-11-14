<!-- customer-credit-and-collections-policy · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The aging, by customer and bucket** | `get_aged_receivables` | `report_date`, `customer`, `aging_method`, `days_per_aging_period`, `num_periods` |
| The customer base and terms held | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| **Revenue and concentration by customer** | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` |
| **Invoice history (days-to-pay numerator)** | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| **Payment history (days-to-pay denominator)** | `search_payments` / `get_payment` | `start_date`, `end_date` (required), `customer_id`; `id` |
| **Credits issued — dispute proxy** | `search_credit_memos` / `search_refund_receipts` | `start_date`, `end_date` (required), `customer_id` |
| **Write-off history — bad debt %** | `get_general_ledger` / `search_journal_entries` | `account`; `start_date`, `end_date` (required) |
| Exposure per customer | `get_customer_balance` | `report_date`, `customer` |
| **Terms catalogue actually in use** | `search_terms` / `get_term` | `query`/`name`, `active_only`; `id` |
| **Revenue, for DSO and bad debt %** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| A/R control balance | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| Currency, calendar, industry | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Credit policy** — the rules deciding who gets to pay later, how much, and on what terms.
- **Collections** — the work of getting invoiced money in.
- **Aging bucket** — a band of lateness (0-15, 16-30, 31-60, 61-90, 90+ days).
- **Cadence** — the scheduled sequence of chasing actions, by bucket.
- **DSO (days sales outstanding)** — the average number of days it takes to get paid. Moves with sales
  volume and mix as well as with collections performance.
- **CEI (collection effectiveness index)** — how much of what was collectable was actually collected, as a
  percentage. **A fairer measure of the collections team than DSO**, because it is not distorted by sales
  growth.
- **% current A/R** — the share of receivables not yet overdue.
- **Bad debt %** — write-offs as a share of revenue.
- **Days-to-pay** — how long a specific customer actually takes.
- **Promise-to-pay** — a customer's commitment to pay by a date; the "kept rate" measures whether they do.
- **Deduction / short-pay** — the customer pays less than invoiced and withholds the difference.
- **Reason code** — a short label for why a deduction or credit happened.
- **SLA** — the agreed turnaround time for resolving something.
- **Order hold** — refusing new supply until the account is brought into line.
- **Credit committee** — the group that approves limits and exceptions.
- **Separation of duties** — the person granting credit is not the person writing it off or applying the
  cash.
- **Concentration** — how much of the book sits with a few customers.
