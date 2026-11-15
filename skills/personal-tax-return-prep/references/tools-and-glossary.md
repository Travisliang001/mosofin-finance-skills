<!-- personal-tax-return-prep · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 11 — **and this skill stores almost nothing.** | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **Business net profit — the self-employment starting figure** | `get_profit_and_loss` | `start_date`, `end_date`, `accounting_method` |
| **Owner drawings, loan or capital account and its movement** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Distributions or dividends declared and paid** | `get_general_ledger` / `search_payments` | `start_date`, `end_date`; `account` |
| The owner's capital position | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| Owner salary, where on the business payroll | `get_profit_and_loss` / `search_payments` | `start_date`, `end_date` |
| Legal name, **fiscal year end**, country | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no personal income statement, no brokerage record, no rate table and no allowance on this
surface.**

---

## Plain-language glossary

- **Taxable income** — what remains after every deduction the law allows. **Not the same as what you
  earned.**
- **Residency / domicile** — where you are taxed and on what. **Residency usually decides whether worldwide
  income is caught; domicile can matter separately.**
- **Filing status** — single, married filing jointly, and so on. **Changes rates, allowances and credits.**
- **Basket** — a category of income taxed at its own rate: ordinary, dividends, capital gains. **The order
  allowances attach to baskets changes the answer.**
- **Personal allowance / standard deduction** — an amount everyone can earn or subtract before tax.
- **Itemising** — claiming actual deductions instead of the standard amount, where the jurisdiction allows
  a choice.
- **Non-refundable credit** — reduces tax to nil but no further. **Refundable credit** — can produce a
  repayment.
- **Withholding** — tax already taken at source. **Estimated payments** — instalments paid during the year.
- **Safe harbour** — paying enough during the year to avoid an underpayment penalty, even if the final bill
  is higher.
- **Carryforward** — a loss or allowance unused this year and available later.
- **Drawings** — money an owner takes from their own business. **What it is for tax — income, capital, or a
  loan — depends on the entity type and the jurisdiction.**
- **Director's or owner's loan account** — the running record of what the owner owes the business or the
  business owes them. **Overdrawn can have tax consequences of its own.**
- **Basis period** — which of the business's accounting periods falls into which personal tax year. **Not
  always obvious, and it has changed in some jurisdictions.**
- **Benefit in kind / fringe benefit** — non-cash reward with a taxable value that has to be computed.
