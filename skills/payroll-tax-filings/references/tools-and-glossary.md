<!-- payroll-tax-filings · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Every payroll tax liability account** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The liability balances at each period end** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Accruals and remittances with dates — the central read** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Deposits made, by payee and date** | `search_payments` / `search_checks` | `start_date`, `end_date` (required) |
| **The tax authorities as payees** | `search_vendors` / `get_vendor` | `query`/`name`, `active_only`; `id` |
| Wages and employer cost expense, for context | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| **Legal name — the employer of record**, country, fiscal calendar | `get_company_info` | none (uses the connected company) |

**Where a payroll platform is a connected datasource**, its register, wage base and YTD tools appear in
**its own** Gate 2 catalog. **Resolve them there; do not assume names.**

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no rate, ceiling, schedule, form, deadline, registration record or authority acknowledgement on
this surface.**

---

## Plain-language glossary

- **Withholding** — tax deducted from an employee's pay and owed to the authority. **The employer holds it
  briefly on someone else's behalf.**
- **Employer contribution** — what the employer owes on top of wages: social charges, levies, unemployment.
- **Remittance / deposit** — paying it over. **Deposit schedule** — how often you must, set by the
  authority and **based on your size or history, not your preference.**
- **Periodic return** — the report of wages and taxes for a period, usually quarterly.
- **Wage statement** — the annual summary each employee receives for their own tax return.
- **Taxable wage base** — what a particular tax is charged on. **Not gross.**
- **Wage-base ceiling / cap** — an annual limit above which a contribution stops. **Per employee.**
- **Three-way tie** — wage statements, periodic returns and the general ledger all agreeing. **Required
  before statements go out.**
- **Employer of record** — the legal entity that employs the people and carries the obligations.
- **Registration** — being enrolled with the authority. **You cannot file where you are not registered**,
  and having employees there creates the obligation regardless.
- **Amended filing** — correcting something already filed. **Slow, visible, and often penalised.**
- **Trust fund taxes** — money withheld from employees, held on their behalf. **In many jurisdictions
  directors and officers are personally liable for failing to remit them**, which is why late deposits
  matter so much more here than for ordinary payables.
- **Contractor vs. employee classification** — getting it wrong means the employer owes contributions and
  withholding it never collected.
