<!-- internal-audit-workpaper · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| The accounts relevant to the area | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The transaction population for the area and period** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Document-level populations** | `search_bills` / `search_purchases` / `search_invoices` | `start_date`, `end_date` (required) |
| **Manual entries — always worth examining** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Master data — vendors, customers, employees | `search_vendors` / `search_customers` / `search_employees` | `query`/`name`, `active_only` |
| **Analytical comparatives** | `get_profit_and_loss` / `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by` |
| Dimensions used in the area | `search_classes` / `search_departments` / `search_locations` | `query`/`name`, `active_only` |
| Legal name, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no confirmation capability, no physical observation and no interview on this surface.**

---

## Plain-language glossary

- **Internal audit** — the organisation independently checking its own processes and reporting to
  governance. **Not the external audit of the financial statements.**
- **IIA / IPPF** — the professional body and framework internal audit works to.
- **Assurance vs. consulting** — giving an independent opinion, versus advising. **Doing both on the same
  area creates an independence problem.**
- **Objective** — what the audit is trying to assess. **Every procedure should link to one.**
- **Criteria** — what *should* be happening: the policy, rule or standard. **Without criteria there is no
  finding, only an observation.**
- **Condition** — what *is* happening.
- **Root cause** — why the gap exists. **Not the same as the symptom**, and the reason weak recommendations
  fail.
- **Consequence** — what it could cost or risk.
- **The 5 C's** — condition, criteria, cause, consequence, corrective action.
- **Workpaper** — the record of a procedure, complete enough that someone else could redo it and agree.
- **Re-performance** — redoing the work yourself rather than taking someone's word for it.
- **Walkthrough** — following one transaction end to end to confirm you understand the process.
- **Population** — every item that could be tested. **Sample** — the subset actually tested.
- **Sampling risk** — the chance the sample was unrepresentative. **Zero if you test everything.**
- **Completeness** — whether everything that should have been recorded was. **The assertion a ledger cannot
  test on its own**, because what is missing leaves no trace in it.
- **Scope limitation** — evidence you could not get, and what it means for the conclusion.
- **Repeat finding** — the same problem found again after it was supposed to be fixed. **Rates higher.**
- **Risk acceptance** — management deciding to live with a risk. **A decision to be recorded, not a fix.**
