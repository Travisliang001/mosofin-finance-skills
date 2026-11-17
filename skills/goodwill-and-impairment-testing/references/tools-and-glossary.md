<!-- goodwill-and-impairment-testing · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| Goodwill, intangible, PP&E and impairment accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The carrying amounts** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Segment performance trend — the triggering-event evidence** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department`, `location` |
| **Prior impairments and their dates** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Customer attrition and concentration** | `search_customers` / `search_invoices` | `query`/`name`; `start_date`, `end_date` (required) |
| Cash movements by segment | `get_cash_flow_statement` | `start_date`, `end_date` |
| **Candidate unit-of-account structure** | `search_classes` / `search_departments` / `search_locations` | `query`/`name`, `active_only` |
| Legal name, currency, **year-end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no valuation, no cash flow forecast, no discount rate and no market capitalization on this
surface.**

---

## Plain-language glossary

- **Impairment** — recognising that something on the balance sheet is worth less than its recorded value.
- **Goodwill** — the premium paid for a business above the value of its identifiable assets. **Never
  amortized; tested every year instead.**
- **Carrying amount / book value** — what the accounts say it is worth.
- **Fair value** — what it could be sold for between willing parties.
- **Recoverable amount (IFRS)** — the higher of what you could sell it for and what it is worth to you from
  continued use.
- **Value in use** — the present value of the cash the asset will generate for you.
- **Reporting unit (US GAAP)** — an operating segment or one level below.
- **CGU (cash-generating unit, IFRS)** — **the smallest group of assets generating largely independent cash
  inflows.** A cash test, not an org-chart test.
- **Asset group (US GAAP, long-lived)** — the same idea for non-goodwill assets.
- **Triggering event** — something that suggests a test is needed before the annual one.
- **Qualitative assessment ("Step 0")** — a US GAAP shortcut: if impairment is not *more likely than not*,
  you can skip the calculation.
- **More likely than not** — greater than 50% probability.
- **DCF (discounted cash flow)** — valuing something by forecasting its cash and discounting it back.
- **WACC** — the blended cost of a business's debt and equity funding; the usual discount rate.
- **Pre-tax vs. post-tax rate** — the discount rate must match whether the cash flows are before or after
  tax. **Mixing them is a common and material error.**
- **Terminal value** — the value assumed beyond the forecast period.
- **Undiscounted** — cash flows added up without discounting. **The US GAAP recoverability test uses these
  deliberately, as a higher bar.**
- **ASU 2017-04** — the change that removed the old two-step goodwill test in US GAAP.
- **Reversal** — writing an impairment back up. **IFRS allows it except for goodwill; US GAAP does not.**
