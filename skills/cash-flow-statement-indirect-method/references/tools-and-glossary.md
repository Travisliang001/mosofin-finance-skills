<!-- cash-flow-statement-indirect-method · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Balance sheet at both period ends** | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method`, `summarize_column_by` |
| Net income and non-cash charges | `get_profit_and_loss` | `start_date`, `end_date`, `accounting_method`, `summarize_column_by` |
| **The platform's own cash flow report (cross-check)** | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| Account-level detail behind both balance sheets | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Classify accounts; find cash, restricted, debt, equity** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Capex vs disposals vs depreciation; debt and equity roll-forwards** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Non-cash entries, reclassifications, write-downs | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Transfers between own accounts (not cash flows) | `search_transfers` / `get_transfer` | `start_date`, `end_date` (required); `id` |
| Direct-method: cash received from customers | `search_payments` / `search_sales_receipts` / `search_deposits` | `start_date`, `end_date` (required) |
| Direct-method: cash paid to suppliers | `search_bill_payments` / `search_purchases` | `start_date`, `end_date` (required) |
| Working-capital components in detail | `get_aged_receivables` / `get_aged_payables` | `report_date`, `customer`/`vendor` |
| Currency, fiscal calendar, legal name | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Statement of cash flows** — the statement explaining why cash changed, split into operating,
  investing and financing.
- **Indirect method** — starting from profit and adjusting to cash. **Direct method** — listing
  actual cash receipts and payments.
- **Operating / investing / financing** — cash from running the business / from buying and selling
  long-term assets / from owners and lenders.
- **Cash equivalents** — investments so short and safe they are treated as cash (original maturity
  three months or less).
- **Restricted cash** — cash you cannot freely use.
- **Working capital** — receivables, inventory, payables and similar: the money tied up in
  day-to-day trading.
- **Non-cash item** — an expense or gain that never moved money, such as depreciation.
- **Capex** — spending on long-lived assets.
- **Roll-forward** — opening balance, movements, closing balance.
- **Gross vs net presentation** — showing draws and repayments separately rather than the net change.
- **ROU asset** — the asset recorded when you lease something.
- **SBC (stock-based compensation)** — pay settled in shares; a cost that uses no cash.
- **Deferred tax** — tax recognised now but payable later, or vice versa. Non-cash.
- **Capitalized interest** — interest added to the cost of an asset rather than expensed.
- **Discontinued operations** — a business being exited, reported separately.
- **Bank overdraft** — a negative bank balance; treated as cash under IFRS in some cases, as
  borrowing under US GAAP.
- **Tie-out** — the proof that the statement's total equals the actual change in cash.
- **Plug** — a figure inserted to force agreement. **Never acceptable.**
