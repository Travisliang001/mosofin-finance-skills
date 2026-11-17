<!-- flux-analysis · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on discovery; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections and their `connected` flag. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (required when several files are live) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call**), `approved` (only after an explicit yes, reads only) |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 7. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Income statement for each period, or a monthly trend | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| Balance sheet at each date | `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| Balances by account when no statement grouping is needed | `get_trial_balance` | `start_date`, `end_date` |
| Postings behind a movement | `get_general_ledger` | `start_date`, `end_date`, `account`, `accounting_method` |
| Manual entries, who posted them and when | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date`; `id` |
| Real account names for proposed entries | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Base currency, fiscal calendar, accounting method | `get_company_info` | none |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments. Where
this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Flux / fluctuation analysis** — comparing balances between periods and explaining the
  changes.
- **MoM / YoY** — month on month / year on year.
- **Threshold** — the size a movement must reach, in percent and in amount, to be explained.
- **Driver** — the reason a number moved: volume, price, mix, timing, one-time, or error.
- **Timing difference** — the activity happened, but it was recorded in another period.
- **Accrual** — recording a cost in the period it belongs to before the bill is paid or posted.
- **Gross margin** — revenue minus cost of sales, as a share of revenue.
- **Reclassification** — moving an amount from one account to another; two equal and opposite
  movements.
- **Cash proof** — showing that the change in cash equals profit adjusted for the balance sheet
  movements.
- **Journal entry (JE)** — the balanced two-sided record. **DR** = debit, **CR** = credit.
