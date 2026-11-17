<!-- management-discussion-and-analysis · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Results, current and comparative, and by month** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class` |
| **Balances at both period ends** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The liquidity section's spine** | `get_cash_flow_statement` | `start_date`, `end_date` |
| **Invoice line detail — the price / volume / mix bridge** | `search_invoices` / `get_invoice` | `start_date`, `end_date` (required); `id` |
| **New versus existing customers, and concentration** | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Debt, reserve and allowance movements | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Working capital movement | `get_aged_receivables` / `get_aged_payables` | `as_of_date`, `aging_period` |
| Headcount, an opex driver | `search_employees` | `query`/`name`, `active_only` |
| **The chart, for scoping critical estimates** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Legal name**, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no forecast, no facility agreement, no market data and no management intent on this surface.**

---

## Plain-language glossary

- **MD&A** — the narrative in which management explains the numbers: what happened, why, and what may
  happen next. **Management's own words, with legal weight.**
- **Reg S-K Item 303** — the SEC rule setting out what an MD&A must cover.
- **Results of operations** — the line-by-line explanation of the income statement.
- **Driver** — the reason a number moved. **Not the movement itself.**
- **Price / volume / mix** — whether revenue changed because of what you charged, how much you sold, or what
  you sold.
- **Constant currency** — restating this year at last year's exchange rates, so growth is not confused with
  currency movement.
- **Organic vs. acquired growth** — growth from the existing business versus from buying another one.
- **Non-GAAP measure** — a figure the entity defines itself, like adjusted EBITDA. **Must be reconciled to
  the nearest official figure, which must be at least as prominent.**
- **Critical accounting estimate** — a judgment big enough and uncertain enough that a different reasonable
  assumption would change the statements materially.
- **Sensitivity** — how much the figure would move under a different assumption. **The part MD&A actually
  asks for.**
- **Liquidity** — the ability to meet obligations as they fall due. **Not the same as the cash balance.**
- **Undrawn facility** — borrowing available but not taken. **A source of liquidity that appears nowhere on
  the balance sheet.**
- **Forward-looking statement** — anything about the future. **Requires cautionary language and legal
  review.**
- **Safe harbour** — the legal protection for forward-looking statements made with proper caveats.
- **Guidance** — management's public forecast. **Never generated here.**
- **Off-balance-sheet arrangement** — an obligation or exposure that does not appear as a liability.
