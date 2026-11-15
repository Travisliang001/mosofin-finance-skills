<!-- model-auditor-financial-model-review · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Historical P&L, every period in the model** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| **Historical and opening balance sheets** | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| **Line-level mapping support** | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| Opening and ending cash | `get_cash_flow_statement` | `start_date`, `end_date` |
| Debt, equity and specially treated lines | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **The chart, for mapping model lines to accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Legal name, **currency, year-end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no model, no formula, no cap table and no assumption support on this surface.**

---

## Plain-language glossary

- **Model** — a spreadsheet that projects a business forward from its history, usually to support a
  decision.
- **Source tie-out** — proving each historical figure in the model matches the accounts it came from.
- **Balance break** — the balance sheet not balancing in some period. **Always a serious finding.**
- **Circular reference** — a formula that depends on itself, usually via interest on a balance that depends
  on interest. **Sometimes deliberate, always worth flagging.**
- **Hardcode** — a number typed inside a formula rather than referenced from an assumption cell. **The
  commonest way a model quietly stops recalculating.**
- **Roll-forward** — opening balance, plus movements, equals closing balance. **Checked period by period.**
- **Sensitivity table / data table** — a grid showing how an output changes as inputs vary.
- **Scenario switch** — a control that flips the whole model between cases. **It should change every
  dependent output, and often does not.**
- **Materiality threshold** — the size below which a difference is not worth chasing. **Without one, every
  rounding difference is a failure.**
- **TIED / IMMATERIAL DIFF / OPEN / FAIL** — agrees; differs but immaterially; not yet checked; materially
  wrong.
- **STALE** — agrees to the version of the accounts the model was built from, but not to the accounts today.
- **PASS / PASS WITH COMMENTS / HOLD** — the review's conclusion. **HOLD means it does not go out.**
- **Vintage** — when the model's actuals were extracted. **The single best predictor of what a tie-out will
  find.**
