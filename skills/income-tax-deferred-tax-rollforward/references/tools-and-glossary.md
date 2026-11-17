<!-- income-tax-deferred-tax-rollforward · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 9. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **The accounts carrying each book basis, and the deferred tax accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Book bases, and opening / closing deferred balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Cumulative results — the valuation allowance evidence** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| **Deferred tax and valuation allowance movements** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| The deferred tax entries themselves | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Legal name, currency, **year-end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no tax return, no tax basis, no tax depreciation schedule, no enacted rate table and no NOL
register on this surface.**

---

## Plain-language glossary

- **Book basis** — what the accounts say something is worth. **Tax basis** — what the tax rules say it is
  worth. **The gap between them is the whole subject.**
- **Temporary difference** — a gap that will unwind: the same amount eventually goes through both, just at
  different times.
- **Permanent difference** — a gap that never unwinds, such as a non-deductible fine. **It creates no
  deferred tax.**
- **DTA (deferred tax asset)** — future tax saving from a **deductible** difference.
  **DTL (deferred tax liability)** — future tax cost from a **taxable** difference.
- **Enacted rate** — the rate actually written into law at the reporting date. **Not the proposed one, and
  not necessarily today's.**
- **Reversal pattern** — when a difference is expected to unwind, which decides which rate applies.
- **NOL (net operating loss)** — a tax loss carried forward to offset future profits. **Often has an expiry
  date, and the expiry is as important as the amount.**
- **Valuation allowance** — a reduction of a DTA to the amount **more likely than not** to be realised. **You
  cannot bank a tax saving you will never make.**
- **Positive and negative evidence** — the things pointing towards and away from being able to use a DTA.
  **Objectively verifiable evidence, like a track record of losses, outweighs a forecast.**
- **Cumulative loss position** — losses over recent years taken together. **The heaviest single piece of
  negative evidence.**
- **Rate change** — new legislation revaluing every deferred balance at once, through the provision.
- **Rate reconciliation** — the bridge from the statutory rate to the actual effective rate. **Where deferred
  tax errors show up.**
- **Rollforward** — opening balance, movements, closing balance. **Here it must tie to the balance sheet at
  both ends.**
