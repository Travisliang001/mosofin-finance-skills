<!-- benefits-and-401k-accounting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| Locate benefit expense and liability accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Cost and liability movement; roll-forwards | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Liability balances carried | `get_trial_balance` / `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| Benefit cost trend by month | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| **Remittances to the plan / insurer** | `search_bill_payments` / `get_bill_payment` | `start_date`, `end_date` (required), `vendor_id`; `id` |
| Provider and insurer invoices | `search_bills` / `get-bill` | `start_date`, `end_date` (required), `vendor_id`; `id` |
| Direct payments and card charges for benefits | `search_purchases` / `get_purchase` | `start_date`, `end_date` (required); `id` |
| Plan administrator / insurer as a vendor | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| Spend per benefit provider | `get_vendor_expenses` | `start_date`, `end_date`, `vendor`, `summarize_column_by` |
| Employee population and active status | `search_employees` / `get_employee` | `query`/`name`, `active_only`; `id` |
| Prior accruals and true-ups | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Cost allocation dimensions | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Year-end and base currency | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description wins.

**There is no actuarial tool in this table because none exists.**

---

## Plain-language glossary

- **Defined contribution (DC)** — the employer pays in a set amount; whatever it grows into is the
  employee's. The employer's obligation ends at the contribution.
- **Defined benefit (DB)** — the employer promises a set future benefit and carries the risk of
  funding it.
- **401(k)** — a common US defined-contribution retirement plan.
- **OPEB** — other post-employment benefits, such as retiree healthcare.
- **PTO / compensated absences** — paid time off employees earn as they work.
- **Vesting** — the point at which an entitlement becomes unconditional.
- **Forfeiture** — an unvested employer contribution lost when an employee leaves early.
- **Withholding** — money deducted from an employee's pay; it is theirs, not an employer cost.
- **Actuary / actuarial valuation** — a specialist calculation of long-term benefit costs, using
  assumptions about lifespans, salary growth and discount rates.
- **PBO / DBO** — projected or defined benefit obligation: today's value of the future promise.
- **Plan assets** — money set aside to fund the promise.
- **Funded status** — plan assets minus the obligation. Positive is overfunded, negative
  underfunded.
- **Net periodic benefit cost** — the year's total pension charge, built from several components.
- **Service cost** — the benefit earned by employees this year. **Interest cost** — the obligation
  growing closer.
- **Prior service cost** — the cost of improving benefits for past service.
- **Actuarial gain / loss** — the effect of reality differing from the assumptions.
- **Corridor method** — a US GAAP option to defer and spread actuarial gains and losses.
- **OCI (other comprehensive income)** — gains and losses recorded in equity rather than through
  profit. **Remeasurement** — the IAS 19 amounts sent there permanently.
- **Self-insured** — the employer pays claims directly rather than buying insurance.
- **IBNR (incurred but not reported)** — claims already run up but not yet billed.
- **Multiemployer plan** — one plan shared by several unrelated employers, usually under a
  collective agreement.
- **Curtailment / settlement** — a plan being cut short, or an obligation being discharged early.
- **Journal entry (JE)** — the balanced two-sided record. **DR** = debit, **CR** = credit.
