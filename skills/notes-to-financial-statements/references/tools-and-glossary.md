<!-- notes-to-financial-statements · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The tie-out targets, current and comparative** | `get_balance_sheet` / `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| Both period ends | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The chart — scoping which notes apply** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The roll-forward populations** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Revenue disaggregation and concentration** | `get_profit_and_loss` / `search_invoices` | `start_date`, `end_date`, `summarize_column_by`, `class` |
| **Concentration and related-party name matching** | `search_customers` / `search_vendors` / `search_employees` | `query`/`name`, `active_only` |
| **The subsequent events candidate population** | `search_journal_entries` / `get_general_ledger` | `start_date`, `end_date` (required) |
| Ageing for credit risk disclosure | `get_aged_receivables` / `get_aged_payables` | `as_of_date`, `aging_period` |
| **Legal name, currencies, year-end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no policy manual, no legal file, no contract and no valuation on this surface.**

---

## Plain-language glossary

- **Notes / footnotes** — the explanatory material accompanying the statements. **Usually most of the
  document.**
- **Accounting policy** — the method chosen where a standard permits more than one. **A decision, not a
  number.**
- **Significant judgment / estimation uncertainty** — where the numbers depend on assumptions that could
  reasonably have been different.
- **Roll-forward** — opening balance, movements, closing balance. **The commonest note format.**
- **Maturity analysis** — what falls due when, usually undiscounted and by year.
- **Disaggregation** — breaking a total down by category, geography, customer type or timing.
- **Concentration** — reliance on a small number of customers, suppliers, products or places. **Disclosable
  when significant, and measurable.**
- **Commitment** — something contractually agreed but not yet in the accounts. **Contingency** — something
  that might happen.
- **Probable / reasonably possible / remote** — the recognition ladder for contingencies. **Accrue, disclose,
  or say nothing.**
- **Related party** — anyone whose relationship could influence terms: parent, subsidiaries, directors, key
  management, their families and their other businesses.
- **Arm's length** — on the terms two unconnected parties would have agreed.
- **Subsequent event** — something happening between the reporting date and the day the accounts are issued.
  **Type 1** — the condition already existed, so adjust. **Type 2** — it arose afterwards, so only disclose.
- **Issuance date** — when the accounts are authorised for issue. **It closes the subsequent events window.**
- **Fair value hierarchy** — Level 1 is a quoted price, Level 2 is derived from observable data, **Level 3 is
  built from assumptions** and needs the most disclosure.
- **Reduced disclosure framework** — the shorter set of requirements available to private or smaller
  entities.
