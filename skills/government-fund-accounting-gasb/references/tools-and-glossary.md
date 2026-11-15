<!-- government-fund-accounting-gasb · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The candidate fund dimension — read first** | `search_classes` / `search_departments` / `search_locations` | `query`/`name`, `active_only` |
| **Trial balance by fund** | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Fund balance sheets, and the self-balancing test** | `get_balance_sheet` | `start_date`, `end_date`, `class`, `department`, `accounting_method` |
| **Revenues and expenditures by fund** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department` |
| **Interfund transfers, and post-year-end collections for the availability test** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Allocations and closing entries between funds | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Capital asset, debt and net position accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Legal name, **fiscal year end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no actuarial valuation, no capital asset register, no bond schedule and no budget ordinance on
this surface.**

---

## Plain-language glossary

- **Fund** — a **separate fiscal and accounting entity with its own self-balancing set of accounts**, set up
  because money given for one purpose may not be spent on another. **Not a category or a tag.**
- **Governmental funds** — the tax-funded core: general operations, capital projects, debt service.
- **Proprietary funds** — the parts that run like a business and charge for what they provide.
- **Fiduciary funds** — money held for other people. **Not the government's own, and excluded from
  government-wide statements.**
- **Modified accrual** — revenue counted when it is **measurable and available** to pay this period's bills;
  **capital assets and long-term debt stay off the balance sheet.**
- **Available** — collectible soon enough to pay current-period liabilities; **often 60 days.**
- **Full accrual / economic resources focus** — the commercial way: everything owned and owed on the balance
  sheet.
- **Measurement focus** — *what* you are measuring: this year's spendable resources, or everything.
- **Government-wide statements** — the whole government on full accrual, in one place.
- **Net position** — the government-wide equivalent of equity. **Fund balance** — the governmental fund
  equivalent.
- **Nonspendable / restricted / committed / assigned / unassigned** — fund balance ranked by **how binding
  the constraint is**, from the form of the asset, through outsiders, through the governing body, down to
  intent and residual.
- **Nonexchange revenue** — money received without giving something of equal value back: taxes, grants.
- **Interfund transfer** — moving money between the government's own funds. **Not revenue.**
- **Component unit** — a legally separate body the government is accountable for. **Blended** — presented as
  if part of the government. **Discretely presented** — shown in its own column.
- **Major fund** — a fund big enough to be shown on its own rather than lumped with others. **A size test,
  recomputed annually.**
- **ACFR (formerly CAFR)** — the full annual report: statements, notes, required supplementary information
  and a statistical section.
- **RSI** — schedules required alongside the statements but outside them.
- **OPEB** — retiree benefits other than pensions, mainly healthcare.
- **Modified approach (infrastructure)** — not depreciating roads and bridges, on condition that they are
  maintained at a stated condition level and that this is documented.
