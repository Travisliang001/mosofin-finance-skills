<!-- corporate-tax-provision-asc740 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 12. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **Pre-tax book income; and the multi-year loss history** | `get_profit_and_loss` | `start_date`, `end_date`, `accounting_method`, `summarize_column_by`, `class`, `department` |
| **Deferred tax, tax payable and tax expense accounts; permanent-difference candidates** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Opening and closing deferred balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Deferred tax movement, and whether it hit P&L, OCI or equity** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Book side of the temporary differences | `get_general_ledger` / `get_balance_sheet` | `account`; `start_date`, `end_date` |
| Prior provision entries and true-ups | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| **Tax actually paid**, for the payable reconciliation | `search_bill_payments` / `search_purchases` | `start_date`, `end_date` (required), `vendor_id` |
| Tax authority as a vendor | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| Jurisdiction dimensions | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Legal name, country, fiscal year end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no tax-rate tool and no tax-return datasource.**

---

## Plain-language glossary

- **Tax provision** — the tax charge in the accounts, which is not the same as the tax paid.
- **Current tax** — tax on this year's taxable profit. **Deferred tax** — the tax effect of timing
  differences that will unwind later.
- **Permanent difference** — a book/tax difference that never reverses; it changes the effective rate.
- **Temporary difference** — a timing difference that will reverse; it creates deferred tax.
- **Tax basis** — an asset's or liability's value for tax purposes, which usually differs from its book
  value.
- **DTA / DTL** — deferred tax asset (a future deduction) / liability (a future charge).
- **Valuation allowance** — a reduction to a DTA that may not be usable.
- **More likely than not** — greater than 50% probability; the US GAAP threshold.
- **Enacted rate** — a rate written into law. **Substantively enacted** — the IFRS equivalent, where the
  remaining steps are formalities.
- **Statutory rate** — the headline legal rate. **Effective tax rate (ETR)** — the tax charge as a
  percentage of pre-tax profit.
- **Foreign rate differential** — the ETR effect of subsidiaries taxed at other rates.
- **NOL (net operating loss)** — a tax loss carried forward to offset future profits.
- **Carryforward / carryback** — using a loss or credit in a later or an earlier year.
- **UTP (uncertain tax position)** — a filing position that may not survive challenge. **FIN 48** is the
  US GAAP framework; **IFRIC 23** the IFRS one.
- **Intraperiod allocation** — splitting the tax charge across continuing operations, discontinued
  operations, OCI and equity.
- **Backwards tracing** — the IFRS requirement to put tax where the underlying item was recognised.
- **Return-to-provision true-up** — correcting the estimate once the actual return is filed.
- **Outside basis difference** — the tax difference in the value of a subsidiary itself, as opposed to
  its assets.
- **Indefinite reinvestment assertion** — a US GAAP position that foreign earnings will not be
  repatriated, avoiding a deferred tax liability.
- **Pillar Two / global minimum tax** — international rules imposing a minimum effective rate on large
  groups.
- **Tax holiday** — a temporary reduced or zero rate offered by a jurisdiction.
- **Discrete item** — something recognised entirely in the interim period it occurs, rather than spread
  through the annual rate.
