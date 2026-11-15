<!-- nonprofit-fund-accounting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The chart — net asset classes and the natural expense axis** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The candidate functional dimension** | `search_classes` / `search_departments` / `search_locations` | `query`/`name`, `active_only` |
| **The functional matrix, where function is tracked** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department` |
| **Net assets by restriction class** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `class`, `accounting_method` |
| **The roll-forward and release entries** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Donors and funders, where set up as customers | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Contributions received | `search_deposits` / `search_payments` | `start_date`, `end_date` (required) |
| **Pledges receivable** | `get_aged_receivables` | `as_of_date`, `aging_period` |
| Legal name, **fiscal year end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no donor agreement, no endowment deed, no fair value and no allocation study on this surface.**

---

## Plain-language glossary

- **Net assets** — the nonprofit equivalent of equity. **Split by whether a donor tied the money up.**
- **Without / with donor restrictions** — the two required classes. **Only a donor creates a restriction.**
- **Board-designated** — money the board has earmarked. **Still unrestricted**, because the board can change
  its mind.
- **Purpose restriction** — must be spent on a stated thing. **Time restriction** — cannot be used until a
  date. **Perpetuity** — the capital must be kept for ever.
- **Release from restriction** — moving money between the two classes once the condition is met. **Nets to
  zero overall**; it is a reclassification, not income.
- **Condition vs. restriction** — a barrier that must be cleared before there is revenue at all, versus a
  limit on how revenue already recognised may be used. **The most confused pair in the sector.**
- **Exchange transaction** — the funder gets something of commensurate value back. **Not a contribution.**
- **Endowment** — a gift whose capital is kept and whose income is spent. **Corpus** — the original capital.
  **Underwater** — worth less than the original gift.
- **UPMIFA** — the US law governing how endowment funds may be spent.
- **Natural classification** — what the money was spent on: salaries, rent, supplies. **Functional
  classification** — what it was spent *for*: program, management & general, fundraising.
- **Statement of Functional Expenses** — the matrix of the two. **Required for all NFPs.**
- **Program percentage** — the share of expense going to program services. **Watched closely by funders and
  regulators, which is precisely why over-allocation is improper.**
- **Joint costs** — costs of an activity serving more than one function, such as an appeal that also
  educates. **Specific allocation rules apply.**
- **In-kind** — donated goods or services. **Services count only if specialised and otherwise purchased.**
- **Liquidity disclosure** — a required note showing what resources are actually available within a year.
