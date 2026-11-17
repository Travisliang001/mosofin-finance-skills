<!-- debt-and-covenant-tracking · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Debt, lease, interest and cash accounts; the debt-like sweep** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Debt balances and cash at the testing date** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Draws, repayments and interest, movement by movement** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Book EBITDA components and interest charged (TTM)** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| **Payments to lenders — actual debt service** | `search_bill_payments` / `search_purchases` / `search_transfers` | `start_date`, `end_date` (required), `vendor_id` |
| Lenders as counterparties | `search_vendors` / `get-vendor` / `get_vendor_expenses` | `query`/`name`; `start_date`, `end_date`, `vendor` |
| Cash generation, for coverage ratios | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| Interest accruals and debt reclassifications | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Dividends and distributions, against a basket | `get_general_ledger` | `account`, `start_date`, `end_date` |
| Legal name, currency, period end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no loan agreement, interest rate, or covenant definition in an accounting datasource.**

---

## Plain-language glossary

- **Facility** — an agreed borrowing arrangement: a loan, a revolver, a bond.
- **Revolver** — a facility you can draw, repay and redraw. **Undrawn capacity** — what is still available.
- **Bullet / balloon / scheduled amortization** — repaid all at the end, mostly at the end, or in
  instalments.
- **Covenant** — a promise to the lender. **Financial covenants** are measured; **affirmative** ones say
  what you must do; **negative** ones say what you must not.
- **Leverage ratio** — net debt divided by EBITDA: how many years of profit it would take to repay.
- **Interest coverage** — how many times profits cover the interest bill.
- **Fixed charge / debt service coverage** — whether cash generated covers everything you must pay.
- **EBITDA** — earnings before interest, tax, depreciation and amortisation. **In a loan agreement it is a
  defined term with addbacks, and is not the same as book EBITDA.**
- **Addback** — an amount added back to profit in the agreement's definition, often capped.
- **TTM (trailing twelve months)** — the last twelve months, the usual covenant testing period.
- **Headroom** — how much room is left before a breach.
- **Event of default** — something that lets the lender demand repayment.
- **Acceleration** — the lender making the whole loan immediately repayable.
- **Cross-default** — a breach on one facility triggering default on another.
- **MAC (material adverse change)** — a catch-all default clause based on judgment.
- **Equity cure** — a right to fix a breach by injecting equity.
- **Pro-forma adjustment** — treating an acquisition as if it had been owned all year.
- **Maturity wall** — a year with a large amount falling due at once.
- **Subordinated / mezzanine / second-lien** — debt ranking behind senior lenders, usually at a higher
  rate.
- **Intercreditor agreement** — the deal between lenders about who gets paid first.
- **Compliance certificate** — a periodic signed statement that you meet your covenants.
