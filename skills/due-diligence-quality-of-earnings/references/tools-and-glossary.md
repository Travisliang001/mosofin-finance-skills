<!-- due-diligence-quality-of-earnings · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Multi-year monthly earnings; the recurring-item test** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` (Month), `accounting_method` |
| **Monthly working capital series** | `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by` (Month) |
| Account-level detail at each year end | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The transactions behind the numbers** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Revenue by customer — concentration and churn** | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` |
| Capex and actual cash generation | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| **Debt, cash, debt-like and fixed-asset accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Related-party and owner spend** | `get_vendor_expenses` / `search_vendors` | `start_date`, `end_date`, `vendor`; `query`/`name` |
| Receivable and payable quality | `get_aged_receivables` / `get_aged_payables` | `report_date` |
| **Period-end invoicing pattern (cutoff proxy)** | `search_invoices` / `search_credit_memos` | `start_date`, `end_date` (required), `customer_id` |
| Product and service mix, pricing | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| **Manual entries around period ends** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Backlog and pipeline | `search_estimates` / `search_purchase_orders` | `start_date`, `end_date` (required) |
| Legal name, year-end, industry | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **QofE (quality of earnings)** — a critical review asking which reported profits are real and repeatable.
- **Adjusted / normalized EBITDA** — reported profit adjusted for one-offs and owner-specific items; the
  number the price is usually a multiple of.
- **Add-back** — an amount added back to profit as non-recurring.
- **LTM / TTM** — the last twelve months.
- **Run-rate** — the annualised level implied by a recent period.
- **Pro-forma** — presented as if a transaction had happened earlier.
- **Owner compensation normalization** — restating the owner's pay to what the role would cost at market.
- **Related party** — a person or business connected to the owners, whose dealings may not be at market
  prices.
- **Bill-and-hold / channel stuffing** — recognising revenue on goods not yet delivered, or pushing stock
  to distributors to hit a number.
- **Cutoff** — whether transactions landed in the right period.
- **Working capital target / peg** — the agreed normal level of working capital delivered with the
  business; deviations at close adjust the price.
- **Cash-free debt-free** — the pricing convention where the buyer takes the business without its cash or
  its debt.
- **Net debt** — debt minus cash. **Debt-like items** — obligations that behave like debt even if not
  called it.
- **Maintenance vs. growth capex** — spending to stand still, versus spending to expand.
- **DSO / DIO / DPO** — days to collect, days of inventory, days to pay. **Cash conversion cycle** —
  the three combined.
- **Carve-out** — selling a division that has never had its own financial statements.
- **Stranded costs** — costs left behind with the seller after a carve-out.
- **Escrow / indemnity / representation** — the deal mechanisms for handling identified risks.
- **Nexus** — the connection that creates a tax obligation in a jurisdiction.
