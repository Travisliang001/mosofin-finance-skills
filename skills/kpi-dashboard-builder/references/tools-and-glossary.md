<!-- kpi-dashboard-builder · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The trend base for every income metric** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department` |
| **The trend base for every balance metric and ratio** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| Cash flow and free cash flow | `get_cash_flow_statement` | `start_date`, `end_date` |
| **DSO and DPO** | `get_aged_receivables` / `get_aged_payables` | `as_of_date`, `aging_period`, `num_periods` |
| Drill-down behind any financial metric | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| The chart, for definitions that name accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Segment dimensions for by-segment metrics | `search_classes` / `search_departments` / `search_locations` | `query`/`name`, `active_only` |
| Headcount for per-employee metrics | `search_employees` | `query`/`name`, `active_only` |
| Inventory metrics | `search_items` | `query`/`name`, `active_only` |
| Legal name, currency, **fiscal calendar**, industry | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no billing system, no CRM, no web analytics, no time system and no production data on this
surface.**

---

## Plain-language glossary

- **KPI** — a figure chosen because decisions depend on it. **Vanity metric** — a figure chosen because it
  goes up.
- **MRR / ARR** — monthly or annual recurring revenue: **contracted subscription value**, not accounting
  revenue.
- **Churn** — customers or revenue lost. **Logo churn** counts customers; **revenue churn** counts money.
- **NRR / GRR** — how much revenue from existing customers survives, **with** and **without** counting
  upsells.
- **CAC** — what it costs to win a customer. **LTV** — what they are worth over their life. **Payback** —
  how long CAC takes to come back.
- **Rule of 40** — growth percentage plus profit margin; a rough health test for software businesses.
- **Magic number** — new revenue produced per unit of sales and marketing spend.
- **ARPA / ARPU** — average revenue per account or user.
- **AOV** — average order value. **Sell-through** — the proportion of stock received that has sold.
- **Utilization** — the share of staff time that is billable. **Realization** — the share of billable time
  actually invoiced.
- **OEE** — how much of a machine's potential output is actually achieved.
- **DSO / DPO / DIO** — days to collect, days to pay, days of inventory. **Cash conversion cycle** —
  DSO + DIO − DPO: how long cash is tied up.
- **Runway** — how long the cash lasts at the current burn.
- **Trailing twelve months (TTM)** — the last twelve months rolled together, which removes seasonality.
- **Cohort** — a group of customers who started at the same time, followed over time.
- **Definition drift** — the same metric quietly measured differently in different periods. **The thing that
  ruins dashboards.**
