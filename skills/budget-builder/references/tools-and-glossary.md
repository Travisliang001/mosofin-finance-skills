<!-- budget-builder · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 10. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **Monthly actuals over several years** (base, seasonality, ratios) | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` (Month), `accounting_method`, `department`, `class` |
| **An existing budget already in the system** | `search_budgets` | `name`, `active`/`limit`, `include_details`, `detail_start_date`, `detail_end_date`, `detail_account`, `detail_rollup` |
| Chart of accounts (structure the budget on real lines) | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Detail behind a line; payroll-loading derivation | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Revenue by customer (retention, concentration) | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` |
| Units, prices, product mix | `search_items` / `search_invoices` / `read_invoice` | `query`/`name`; `start_date`, `end_date` (required); `id` |
| Point-of-sale revenue (AOV, transaction counts) | `search_sales_receipts` | `start_date`, `end_date` (required), `customer_id` |
| Billable hours (utilization, bill rate) | `search_time_activities` | `start_date`, `end_date` (required), `customer_id` |
| Recurring vendor spend (committed cost base) | `get_vendor_expenses` | `start_date`, `end_date`, `vendor`, `summarize_column_by` |
| Current roster | `search_employees` / `get_employee` | `query`/`name`, `active_only`; `id` |
| Department / class structure | `search_departments` / `search_classes` | `query`/`name`, `active_only` |
| Opening position; depreciation-bearing assets | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method`, `summarize_column_by` |
| Historical cash movement | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| Fiscal calendar and base currency | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Budget** — next year's plan expressed in money.
- **Driver** — the underlying thing that makes a number what it is (customers, units, headcount).
- **Incremental budgeting** — start from last year and adjust.
- **Zero-based budgeting (ZBB)** — start from nothing and justify every line.
- **Driver-based budgeting** — build each line as a formula on its driver.
- **ARR / MRR** — annual / monthly recurring revenue: the run-rate of subscriptions in force.
- **Bookings** — new business signed. **Pipeline** — deals in progress. **Close rate** — the share
  that convert.
- **Churn** — revenue lost from customers leaving. **Contraction** — from customers downgrading.
  **Expansion / upsell** — the reverse.
- **ASP (average selling price)** — revenue divided by units.
- **Utilization** — the share of available staff time that is billable. **Bill rate** — the price
  charged per hour.
- **Conversion** — the share of visitors who buy. **AOV (average order value)** — revenue per
  order.
- **Same-store growth** — growth excluding new locations.
- **COGS** — cost of goods sold: the direct cost of what you sold.
- **Gross margin** — gross profit as a percentage of revenue.
- **EBIT** — earnings before interest and tax: profit from operating the business.
- **Effective tax rate** — tax as a percentage of pre-tax profit.
- **Loading / burden rate** — employer payroll taxes and benefits as a percentage of wages.
- **CAC** — customer acquisition cost. **LTV** — lifetime value. **CAC payback** — how long to earn
  back what you spent winning a customer.
- **Capex** — spending on long-lived assets, which becomes depreciation over time.
- **Run-rate** — the annualised level implied by a recent period.
- **Flex** — showing how the budget changes if a driver changes.
- **Seasonality** — the recurring within-year pattern of a business.
- **Plug** — a figure inserted to force a total. **Never acceptable.**
