<!-- cost-accounting-job-order · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 8. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **The job codes and phase dimensions** | `search_classes` / `search_departments` / `search_customers` | `query`/`name`, `active_only` |
| **Cost and revenue per job** | `get_profit_and_loss` | `start_date`, `end_date`, `class`, `department`, `customer`, `summarize_column_by` |
| **All direct-cost postings — tagged and untagged** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Materials, subcontractors, other direct costs | `search_bills` / `search_purchases` / `get-bill` | `start_date`, `end_date` (required), `vendor_id`; `id` |
| **Labour hours by job** | `search_time_activities` | `start_date`, `end_date` (required), `customer_id` |
| Committed but unincurred job cost (cutoff test) | `search_purchase_orders` / `get_purchase_order` | `start_date`, `end_date` (required); `id` |
| WIP, applied-overhead, variance and pool accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| WIP balance carried | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| Budgeted overhead and base (predetermined rate) | `search_budgets` | `name`, `include_details`, `detail_account`, `detail_start_date`, `detail_end_date` |
| Job billings, for margin | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Items consumed on jobs | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Labour population | `search_employees` | `query`/`name`, `active_only` |
| Currency and calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Job order costing** — accumulating costs against each individual job, because every job is
  different.
- **Job / phase / cost code** — levels of detail: the whole job, a stage of it, and a category of cost
  within that stage.
- **Direct cost** — a cost you can point at a specific job. **Indirect cost / overhead** — a cost that
  keeps the business running but belongs to no single job.
- **Overhead pool** — the bucket of indirect costs waiting to be spread across jobs.
- **Allocation base** — the measure used to spread them: hours worked, wages paid, machine time.
- **Predetermined rate** — an overhead rate set in advance from budgets, so jobs can be costed as they
  go rather than waiting for year end.
- **Applied overhead** — overhead charged to jobs using that rate. **Actual overhead** — what was really
  incurred.
- **Under-applied / over-applied** — you charged jobs less, or more, overhead than you actually spent.
- **Burden** — the employer's on-costs added to a wage: taxes, benefits, insurance.
- **WIP (work in progress)** — cost sitting on jobs that are not yet finished or not yet charged out.
- **Relieved to COGS** — moving cost out of WIP into cost of sales when the job completes or ships.
- **FG (finished goods)** — completed but unsold production.
- **Prorate** — spreading a variance across WIP, finished goods and cost of sales in proportion.
- **T&M (time and materials)** — billing for hours and materials used, rather than a fixed price.
- **Cutoff** — making sure costs land in the right period.
