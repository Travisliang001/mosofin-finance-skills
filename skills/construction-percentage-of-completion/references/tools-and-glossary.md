<!-- construction-percentage-of-completion · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 12. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **The job codes — and whether jobs are tagged at all** | `search_classes` / `search_departments` / `search_customers` | `query`/`name`, `active_only` |
| **Cost and revenue per job** | `get_profit_and_loss` | `start_date`, `end_date`, `class`, `department`, `customer`, `summarize_column_by` |
| **Costs incurred to date, by category and job** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Subcontractor and materials cost by job | `search_bills` / `search_purchases` / `get-bill` | `start_date`, `end_date` (required), `vendor_id`; `id` |
| **Committed but unincurred cost (estimate cross-check)** | `search_purchase_orders` / `get_purchase_order` | `start_date`, `end_date` (required), `vendor_id`; `id` |
| Labour hours by job (hours input method) | `search_time_activities` | `start_date`, `end_date` (required), `customer_id` |
| **Billings to date per contract** | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Quoted contract values | `search_estimates` / `get_estimate` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Contract asset / liability / provision accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Amounts outstanding per customer | `get_customer_balance` / `get_aged_receivables` | `report_date`, `customer` |
| Retentions held (often a separate account) | `search_accounts` / `get_general_ledger` | `query`/`name`; `account` |
| Currency and fiscal calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no estimate-at-completion in an accounting datasource.**

---

## Plain-language glossary

- **Percentage of completion (POC)** — recognising revenue as a long contract progresses. Now formally
  "over-time recognition".
- **Over-time vs. point-in-time** — recognising as you work, versus all at once on delivery.
- **Measure of progress** — how you decide how far through you are.
- **Cost-to-cost** — measuring progress as costs incurred divided by total costs expected.
- **Input vs. output method** — measuring by what you have put in, versus by what you have produced.
- **Estimate at completion** — the total cost you now expect the whole contract to take.
- **Cumulative catch-up** — adjusting this period for a revised estimate, rather than restating the past.
- **Transaction price** — the total you expect to be entitled to, including variable elements.
- **Variable consideration** — amounts not yet fixed: variations, claims, bonuses, penalties.
- **The constraint** — the rule that you only include variable amounts that are highly probable not to
  reverse.
- **Liquidated damages** — pre-agreed penalties for late completion.
- **Variation** — an agreed change to the scope or price. **Claim** — an amount you are seeking but the
  customer has not agreed.
- **Standalone selling price** — what each part of a contract would sell for on its own.
- **Significant financing component** — the interest element when payment and performance are far apart.
- **WIP (work in progress)** — work done but not yet billed, or billed but not yet done.
- **Contract asset / CIE** — you have earned more than you have billed (costs and estimated earnings in
  excess of billings).
- **Contract liability / BIE** — you have billed more than you have earned (billings in excess).
- **Contract asset vs. receivable** — a receivable is unconditional; a contract asset still depends on
  more than the passage of time.
- **Onerous contract** — one expected to lose money.
- **Backlog / remaining performance obligations** — contracted work not yet done.
- **Uninstalled materials** — bought and on site, but not yet fitted.
- **Retention / retainage** — money the customer withholds until the job is signed off.
- **Cost-plus contract** — priced at cost plus an agreed fee, rather than a fixed sum.
- **Joint venture / joint operation** — shared delivery structures with their own accounting.
