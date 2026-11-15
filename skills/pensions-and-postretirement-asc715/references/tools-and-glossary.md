<!-- pensions-and-postretirement-asc715 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| Pension liability, expense and AOCI accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The recorded position, both period ends** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Liability and AOCI movements, and the annual entry** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Employer contributions paid to the plan** | `search_payments` / `search_checks` | `start_date`, `end_date` (required) |
| **Pension expense recognised, and its split** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| **The pension entry — almost always a manual journal** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Headcount, as context only | `search_employees` | `query`/`name`, `active_only` |
| Legal name, currency, **year-end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no actuarial report, no plan asset valuation, no assumption set and no trustee statement on this
surface.**

---

## Plain-language glossary

- **Defined benefit plan** — a promise of a specified retirement income. **The employer carries the risk
  that it costs more than expected.** **Defined contribution plan** — the employer pays in a fixed amount
  and the risk sits with the employee. **Only the first is in scope here.**
- **PBO / APBO** — the present value of the promise: **projected benefit obligation** for pensions,
  **accumulated postretirement benefit obligation** for other benefits like retiree healthcare.
- **Plan assets** — the fund set aside to meet the promise, held separately from the employer.
- **Funded status** — plan assets less the obligation. **Positive is a surplus, negative a deficit**, and it
  goes on the balance sheet.
- **Service cost** — the cost of the extra promise earned by employees working this year. **An operating
  cost.**
- **Interest cost** — the obligation growing simply because retirement is a year closer.
- **Expected return on plan assets** — under ASC 715, the anticipated return used in the expense.
  **Net interest** — under IAS 19, interest on the net position at the discount rate instead. **Different
  answers from identical facts.**
- **Actuarial gain or loss** — the effect of assumptions turning out wrong, or being changed.
- **Remeasurement** — the collective term for those effects. **Goes to OCI, not profit.**
- **Prior service cost** — the effect of changing the promise, usually by a plan amendment.
- **Corridor approach** — an older method deferring recognition of gains and losses within a band.
- **Settlement / curtailment** — paying off part of the obligation, or cutting off future accrual. **Both
  trigger immediate recognition.**
- **Discount rate** — the rate converting future promises to a value today. **The single most influential
  assumption**; a small change moves the obligation a long way.
- **Asset ceiling** — a limit on recognising a surplus as an asset, because a surplus you cannot access is
  not worth its face value.
- **Measurement date** — the date the actuary valued everything. **It should be the reporting date.**
