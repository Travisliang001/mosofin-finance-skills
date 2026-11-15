<!-- healthcare-revenue-cycle-accounting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 7. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Revenue, contra revenue, AR, bad debt and charity care accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Gross charges, contra revenue, net revenue — the realization series** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department` |
| **Adjustment and write-off volumes over time** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **GL AR and reserve balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **AR aging by payer** | `get_aged_receivables` | `as_of_date`, `aging_period`, `num_periods` |
| **Cash received, and unapplied amounts** | `search_deposits` / `search_payments` | `start_date`, `end_date` (required) |
| **Payers, where set up as customers — payer level only** | `search_customers` | `query`/`name`, `active_only` |
| Adjustments raised as credits | `search_credit_memos` | `start_date`, `end_date` (required) |
| Legal name, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no billing system, no payer contract, no denial reason code and no clinical record on this
surface.**

---

## Plain-language glossary

- **Revenue cycle** — everything from recording that care was given to the money finally arriving.
- **Charge capture** — recording what was done, so it can be billed.
- **Chargemaster / gross charges** — the provider's list price. **Almost nobody pays it.**
- **Claim** — the bill sent to an insurer. **Adjudication** — the insurer deciding what it will pay.
- **Remittance** — the insurer's payment and the explanation that comes with it.
- **Contractual allowance / adjustment** — the gap between list price and the contracted rate. **Contra
  revenue: a deduction, not an expense.**
- **Net patient service revenue** — what the care actually earned, after those deductions.
- **Payer** — whoever pays: an insurer, a government programme, the patient. **Payer mix** — the proportions,
  which drives realization.
- **Patient responsibility** — the share the patient owes: deductible, co-pay, coinsurance.
- **Denial** — the insurer refusing a claim. **Some are appealable; the reason code says which.**
- **Charity care / financial assistance** — care given to patients who qualify for free or reduced-cost
  treatment. **Never bad debt** — the entity chose not to pursue payment.
- **Bad debt** — amounts expected to be collected that were not.
- **Implicit price concession** — under the revenue standard, an amount the provider never really expected
  to collect, which **reduces revenue rather than creating an expense.**
- **Realization rate** — net revenue as a proportion of gross charges.
- **Unapplied cash** — money received that has not been matched to a claim.
- **AR days** — how many days of revenue are sitting unpaid. **The headline revenue cycle metric.**
- **PHI (protected health information)** — health data about an identifiable person, legally protected.
