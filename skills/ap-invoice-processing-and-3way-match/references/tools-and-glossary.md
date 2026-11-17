<!-- ap-invoice-processing-and-3way-match · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 8. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Bills in scope (duplicates, population) | `search_bills` | `start_date`, `end_date` (required), `vendor_id`, `max_results`, `offset` |
| One bill: lines, tax, terms, PO reference | `get-bill` | `id` |
| Purchase orders to match against | `search_purchase_orders` | `start_date`, `end_date` (required), `vendor_id` |
| One PO's lines: item, qty, unit price | `get_purchase_order` | `id` |
| Vendor status, terms, remit-to | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| Payment terms and due-date rules | `search_terms` / `get_term` | `query`/`name`, `active_only`; `id` |
| Coding structure: accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Coding dimensions: classes, departments | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Items being ordered and billed | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Tax codes and rates | `search_tax_codes` / `search_tax_rates` | `query`/`name`, `active_only` |
| Payments made (cycle-time KPI) | `search_bill_payments` / `get_bill_payment` | `start_date`, `end_date` (required); `id` |
| Vendor credits against a disputed bill | `search_vendor_credits` | `start_date`, `end_date` (required), `vendor_id` |
| Attachment metadata (a document exists) | `search_attachables` / `get_attachable` | `query`/`name`; `id` |
| A/P balance for the tie-out | `get_balance_sheet` / `get_vendor_balance` | `start_date`, `end_date`; `report_date`, `vendor` |
| Coding detail behind posted bills | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Base currency and calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description
wins.

---

## Plain-language glossary

- **Accounts payable (A/P)** — money you owe suppliers.
- **PO (purchase order)** — the order you placed, agreeing what and at what price.
- **GRN / receipt** — the record that the goods or services actually arrived.
- **GRNI** — "goods received, not invoiced": it arrived, the bill hasn't. See
  `ap-accrual-cutoff`.
- **2-way match** — order vs bill.
- **3-way match** — order vs receipt vs bill. The receipt is the leg that proves you got what
  you are paying for.
- **Tolerance** — the small variance accepted without investigation, usually a percentage
  with an absolute floor.
- **After-the-fact PO** — an order raised after the goods were already bought, to regularise
  a purchase that skipped the process.
- **Remit-to** — the name and address a supplier wants payment sent to, which is not always
  the name on the invoice.
- **Approval matrix** — who may approve spend up to what value.
- **Dimensions** — the extra coding tags on a transaction (department, project, class) beyond
  the account itself.
- **Recoverable VAT / input tax** — sales tax on purchases that you can reclaim, so it is not
  a cost.
- **SOP** — standard operating procedure: the written routine.
- **SLA** — service level agreement: the agreed turnaround time.
- **Cycle time** — how long a bill takes from arrival to payment.
- **First-pass match rate** — the share of invoices that match with no exception.
- **Journal entry** — the balanced two-sided record. **DR** = debit, **CR** = credit.
