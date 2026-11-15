<!-- model-builder-integrated-three-statement · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Historical P&L at the model's cadence** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `accounting_method` |
| **Historical and opening balance sheets** | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| Historical cash flow | `get_cash_flow_statement` | `start_date`, `end_date` |
| **Mapping completeness** | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The chart with types, for the account-to-line mapping** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Working capital drivers — DSO and DPO** | `get_aged_receivables` / `get_aged_payables` | `as_of_date`, `aging_period` |
| Debt, equity and fixed asset roll-forwards | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Revenue drivers — volume and price** | `search_invoices` / `get_invoice` | `start_date`, `end_date` (required); `id` |
| Customer counts | `search_customers` | `query`/`name`, `active_only` |
| Headcount history | `search_employees` | `query`/`name`, `active_only` |
| Legal name, **currency, year-end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no forecast, no assumption support, no debt schedule and no cap table on this surface.**

---

## Plain-language glossary

- **Three-statement model** — P&L, balance sheet and cash flow, linked so a change in one flows through all
  three.
- **Integrated / linked** — the statements are connected by formulas, not typed separately. **The whole
  point.**
- **Driver-based** — the forecast comes from underlying rates and volumes, not from a growth percentage
  applied to last year's total.
- **Assumption** — an input the user controls. **Should live in one visible place, never inside a formula.**
- **Hardcode** — a number typed into a formula. **The thing that silently stops a model working.**
- **Source historicals** — the imported past. **Immutable**: forecast formulas never write into it.
- **Mapping** — which accounts make up which model line. **The commonest source of a model that quietly
  disagrees with the accounts.**
- **Roll-forward** — opening, plus movements, equals closing. Used for cash, retained earnings, debt and
  fixed assets.
- **DSO / DIO / DPO** — days to collect, days of inventory, days to pay. **The core working capital
  drivers, and all computable from history.**
- **ARPU** — average revenue per user. **Cash sweep** — surplus cash automatically repaying debt.
- **NOL** — a tax loss carried forward.
- **Circularity** — interest depending on debt depending on cash depending on interest. **Common,
  manageable, and always worth flagging.**
- **PASS / WARNING / HOLD** — the check dashboard's verdicts. **HOLD means the model is not ready.**
- **Opening balance sheet** — the last actual position the forecast starts from. **The join between history
  and forecast.**
