<!-- cost-accounting-process-costing · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The departments / processes** | `search_departments` / `search_classes` | `query`/`name`, `active_only` |
| **Costs added by department** | `get_profit_and_loss` | `start_date`, `end_date`, `department`, `class`, `summarize_column_by` |
| **Production cost postings by department** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **WIP per department, finished goods, COGS accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Opening and closing WIP and FG balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Transfers between WIP accounts and out to FG** | `get_general_ledger` | `account`, `start_date`, `end_date` |
| Materials purchased into the process | `search_bills` / `search_purchases` | `start_date`, `end_date` (required), `vendor_id` |
| Labour hours by department, where tracked | `search_time_activities` | `start_date`, `end_date` (required) |
| Finished-goods item master | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Prior period cost-flow entries | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Currency and calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no unit count or completion percentage in an accounting datasource.**

---

## Plain-language glossary

- **Process costing** — costing continuous production by averaging a period's costs over the output,
  rather than tracking individual jobs.
- **Department / process** — a stage of production that costs are accumulated against.
- **Equivalent units (EU)** — part-finished units expressed as whole ones: two units half-done equal one
  equivalent unit.
- **Direct materials** — the physical inputs. **Conversion costs** — labour plus overhead, the cost of
  turning materials into product.
- **Material addition point** — where in the process materials enter: all at the start, at a stage, or
  evenly.
- **Weighted-average method** — blends last period's part-finished costs with this period's.
- **FIFO method** — separates out this period's own work, giving a cleaner current cost.
- **Units to account for / units accounted for** — what went in and what came out. They must agree.
- **Transferred out** — units finished in one department and passed to the next.
- **WIP (work in process)** — cost sitting in part-finished production.
- **FG (finished goods)** — completed but unsold production.
- **Relieved to COGS** — cost moving out of inventory when goods are sold.
- **Normal loss / spoilage** — expected wastage, absorbed into the cost of good units. **Abnormal loss**
  — unexpected wastage, expensed as it happens.
- **Yield** — how much good output you get from a given input.
- **Transfer price** — the value at which one department or entity passes goods to another.
