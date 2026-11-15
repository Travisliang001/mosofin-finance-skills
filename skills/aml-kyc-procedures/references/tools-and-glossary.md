<!-- aml-kyc-procedures · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| Customer population (screening list, risk register) | `search_customers` | `query`/`name`, `active_only`, `max_results`, `offset` |
| One customer's full record (name, address, country) | `get_customer` | `id` |
| Vendor population (the payment-out side) | `search_vendors` | `query`/`name`, `active_only` |
| One vendor's full record | `get-vendor` | `id` |
| Activity by customer (profile vs behaviour) | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` |
| Exposure by customer | `get_customer_balance` | `report_date`, `customer` |
| Money in — invoices, receipts, payments, deposits | `search_invoices` / `search_sales_receipts` / `search_payments` / `search_deposits` | `start_date`, `end_date` (required), `customer_id`, `max_results` |
| Money out — purchases and bill payments | `search_purchases` / `search_bill_payments` | `start_date`, `end_date` (required), `vendor_id` |
| Movements between own accounts (layering signal) | `search_transfers` | `start_date`, `end_date` (required) |
| Credits and refunds (round-tripping signal) | `search_credit_memos` / `search_refund_receipts` | `start_date`, `end_date` (required), `customer_id` |
| Full transaction detail for pattern analysis | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Cash and bank accounts (cash-intensity risk) | `search_accounts` | `query`/`name`, `active_only` |
| Products / services offered (product risk) | `search_items` | `query`/`name`, `active_only` |
| Attachment metadata (evidence a document exists) | `search_attachables` / `get_attachable` | `query`/`name`; `id` |
| The entity's own profile | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description
wins.

**There is no screening tool in this table because none exists.** Do not look for one, and do
not substitute another tool for it.

---

## Plain-language glossary

- **AML** — anti-money-laundering: stopping criminal money being passed off as legitimate.
- **CFT** — countering the financing of terrorism; travels with AML in most regimes.
- **KYC** — know your customer: establishing who you are actually dealing with.
- **CDD / EDD** — customer due diligence (the standard check) / enhanced due diligence (the
  heavier check for higher-risk relationships).
- **Obliged entity** — a business the law specifically requires to run AML controls.
- **MLRO / BSA officer** — the named person accountable for AML decisions and filings
  (money laundering reporting officer; officer under the US Bank Secrecy Act).
- **FATF** — the international body that sets AML standards countries adopt locally.
- **Risk-based approach** — put effort where the risk is, rather than treating everyone alike.
- **PEP** — politically exposed person: someone holding or having held a prominent public
  function, so more exposed to bribery and corruption risk. **Not an accusation** — a risk
  factor.
- **Beneficial owner** — the real human being who ultimately owns or controls a customer,
  behind any companies or trusts.
- **Nominee** — a person or company holding something on someone else's behalf, hiding the
  real owner.
- **Layering** — moving money through many accounts or entities to break the audit trail.
- **Source of funds / source of wealth** — where this particular money came from / how the
  customer became wealthy at all.
- **Sanctions** — official prohibitions on dealing with named parties. **Strict liability**:
  breaching them is an offence regardless of whether you meant to.
- **Adverse media** — negative news suggesting financial crime risk.
- **Watchlist** — any other list of parties warranting caution.
- **False positive** — an innocent name collision flagged by screening.
- **Structuring / smurfing** — breaking a big amount into small ones to stay under a
  reporting threshold.
- **Pass-through** — money arriving and leaving almost immediately, leaving little behind.
- **SAR / STR** — suspicious activity report / suspicious transaction report: the filing made
  to the authorities.
- **Tipping off** — telling the customer they are under suspicion or that a report was filed.
  Typically a criminal offence.
- **Retention period** — how long records must be kept, set by local regulation.
- **Enterprise-wide risk assessment** — the whole-business view of money-laundering exposure.
