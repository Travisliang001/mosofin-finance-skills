<!-- cohort-and-unit-economics · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Revenue per customer per period — the cohort triangle** | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` (Month) |
| **First-invoice dates (acquisition) and invoice detail** | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Customer master, status, geography | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Revenue with no invoice (transactional models) | `search_sales_receipts` | `start_date`, `end_date` (required), `customer_id` |
| Credits and refunds reducing cohort revenue | `search_credit_memos` / `search_refund_receipts` | `start_date`, `end_date` (required), `customer_id` |
| **S&M spend and gross margin, by month** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| Which accounts constitute acquisition cost | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Detail behind the S&M accounts | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Plan / product tier, for segmentation | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Exposure per customer (context) | `get_customer_balance` | `report_date`, `customer` |
| Currency and fiscal calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no acquisition-channel tool in an accounting datasource.**

---

## Plain-language glossary

- **Cohort** — a group of customers who arrived in the same period.
- **Cohort triangle** — the table with cohorts down the side and months-since-joining across the top.
- **Logo retention** — the share of *customers* still around. **Revenue retention** — the share of
  *revenue* still coming in.
- **Net revenue retention (NRR)** — revenue retention including upsell; above 100% means existing
  customers are growing faster than others leave.
- **Churn** — customers or revenue lost. **Expansion / upsell** — existing customers spending more.
- **Survivorship** — only the customers who lasted appear in later columns, which flatters averages if
  not handled.
- **LTV (lifetime value)** — total contribution a customer produces over their whole relationship.
- **CAC (customer acquisition cost)** — what it cost to win a customer.
- **Fully-loaded CAC** — including sales salaries and overheads, not just advertising.
- **Blended CAC** — averaged across all channels, hiding differences between them.
- **CAC payback** — how long it takes to earn back the acquisition cost, on a margin basis.
- **Contribution margin** — revenue minus the variable cost of serving that customer.
- **Cost-to-serve** — what it actually costs to deliver to a given customer.
- **Survival probability** — the chance a customer is still there at a given age.
- **Discount factor / NPV** — reducing future amounts to today's value.
- **Take rate** — the share of transaction value a marketplace keeps.
