<!-- equity-compensation-accounting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| SBC expense, APIC, common stock, liability accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Expense recorded, and its functional split** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `department`, `class` |
| **Every SBC and equity movement** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| APIC and common stock balances; cash-settled liability | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The SBC journals themselves** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| **Cash received on option exercises** | `search_deposits` / `get_deposit` | `start_date`, `end_date` (required); `id` |
| Recipient population and leaver signals | `search_employees` / `get_employee` | `query`/`name`, `active_only`; `id` |
| Functional lines for allocation | `search_departments` / `search_classes` | `query`/`name`, `active_only` |
| Legal name, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no cap table, option-pricing model or share price on this surface.**

---

## Plain-language glossary

- **Share-based / stock-based compensation (SBC)** — paying people in shares or options rather than cash.
- **ASC 718 / IFRS 2** — the US and international standards governing it.
- **Option** — the right to buy a share at a fixed **strike** price. **RSU** — a promise of a share once
  vested. **RSA** — a share issued up front but forfeitable. **ESPP** — a scheme letting staff buy shares,
  usually at a discount. **SAR** — a right to the *increase* in value, without buying the share.
- **Phantom stock** — a cash bonus tracking the share price; no shares involved.
- **Equity-settled vs. cash-settled** — settled in shares (valued once, at grant) or in cash (revalued
  every period).
- **Grant-date fair value** — what the award was worth on the day it was given. **The measurement date for
  equity-settled awards.**
- **Vesting** — earning the award by staying or by hitting a target. **Cliff** — all at once.
  **Graded** — in instalments.
- **Requisite service period** — the time the employee must work to earn it.
- **Attribution method** — how the total cost is spread across the vesting period.
- **Service / performance / market condition** — vest by staying / by hitting a business target / by the
  share price doing something. **Only the first two can reverse the expense.**
- **TSR (total shareholder return)** — share price growth plus dividends; a common market condition.
- **Forfeiture** — losing an unvested award, usually by leaving.
- **True-up** — correcting an estimate once the actual outcome is known.
- **Black-Scholes-Merton / lattice / Monte Carlo** — option-pricing models, in increasing order of
  flexibility and complexity.
- **Expected term, volatility, risk-free rate, dividend yield** — the inputs those models need.
- **Look-back** — an ESPP feature letting the purchase price be based on the lower of two dates.
- **APIC (additional paid-in capital)** — the equity account where share-based credits accumulate.
- **Par value** — the nominal value of a share, usually trivial.
- **Intrinsic value** — the gain if exercised today: share price minus strike.
- **Modification / repricing** — changing an award's terms after grant.
- **409A valuation** — a US private-company share valuation used for setting strike prices.
- **Unrecognised compensation cost** — the expense still to come on awards already granted.
