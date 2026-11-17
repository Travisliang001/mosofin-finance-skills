<!-- credit-limit-and-customer-risk · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| Customer record: name, address, terms, status | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| **Current exposure** | `get_customer_balance` | `report_date`, `customer` |
| **Exposure aging — how overdue** | `get_aged_receivables` | `report_date`, `customer`, `aging_method`, `num_periods` |
| **Invoice history (days-to-pay numerator)** | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| **Payment history (days-to-pay denominator)** | `search_payments` / `get_payment` | `start_date`, `end_date` (required), `customer_id`; `id` |
| **Trading volume and trend; concentration** | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` |
| Disputes and credits issued | `search_credit_memos` / `search_refund_receipts` | `start_date`, `end_date` (required), `customer_id` |
| **Whether the customer is also a vendor** | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| Net exposure if they are also a vendor | `get_vendor_balance` / `get_aged_payables` | `report_date`, `vendor` |
| **Prior write-off history** | `get_general_ledger` / `search_journal_entries` | `account`; `start_date`, `end_date` (required) |
| Terms currently granted, and terms actually applied | `search_terms` / `get_term` / `read_invoice` | `query`/`name`; `id` |
| Orders in the pipeline (forward exposure) | `search_estimates` / `search_purchase_orders` | `start_date`, `end_date` (required), `customer_id` |
| Your entity's currency and calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no credit bureau, sanctions list, or customer-financials datasource here.**

---

## Plain-language glossary

- **Trade credit** — invoicing a customer and letting them pay later; effectively an unsecured loan.
- **Credit limit** — the most you are willing to have outstanding with one customer at a time.
- **Credit hold** — pausing further supply until the balance comes down.
- **Days-to-pay** — how long a customer actually takes to pay, measured from invoice or from due date.
- **Exposure** — the amount currently at risk with a customer.
- **Peak exposure** — the most they have ever owed you.
- **Current ratio / quick ratio / cash ratio** — three increasingly strict tests of whether a business can
  meet its short-term bills.
- **Debt-to-equity / debt-to-assets** — how much of the business is funded by borrowing.
- **Interest coverage** — how many times over profits cover the interest bill.
- **ROA / ROE** — return on assets / on equity.
- **Free cash flow** — cash left after running and reinvesting in the business.
- **Credit bureau** — an agency selling assessments of a company's creditworthiness.
- **Trade reference** — another supplier's account of how the customer pays them.
- **Tier** — a risk band that determines how much credit and what monitoring.
- **Letter of credit** — a bank's guarantee of payment, used where the customer's own promise is not
  enough.
- **Credit insurance** — insuring receivables against customer default; the insurer sets its own limit.
- **Personal / parent guarantee** — someone else promising to pay if the customer does not.
- **Security interest** — a legal claim over the customer's assets if they default.
- **Net exposure** — what a counterparty owes you minus what you owe them.
- **Concentration** — how much of your total receivables sits with one customer.
- **Capital controls** — government restrictions on moving money out of a country.
- **COD (cash on delivery)** — no credit at all.
