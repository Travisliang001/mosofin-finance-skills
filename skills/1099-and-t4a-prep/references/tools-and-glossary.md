<!-- 1099-and-t4a-prep · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays them as:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on the discovery call; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections and their `connected` flag. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists a datasource's read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (required when several company files are live) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call**), `approved` (only after an explicit yes) |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 8. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools for this skill — **resolve the real names and policies from your
Gate 2 catalog**; these are pointers, and both the names and the policies vary by workspace:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Vendor master | `search_vendors` | `query`/`name`, `active_only`, `max_results`, `offset` |
| One vendor's full record | `get-vendor` | `id` |
| Spend per vendor for the year | `get_vendor_expenses` | `start_date`, `end_date`, `vendor`, `accounting_method`, `summarize_column_by` |
| Outstanding vendor balances | `get_vendor_balance` | `report_date`, `vendor` |
| Bills recorded | `search_bills` | `start_date`, `end_date` (required), `vendor_id`, `max_results` |
| Payments actually made against bills | `search_bill_payments` | `start_date`, `end_date` (required), `vendor_id` |
| Direct expenses / cheques / card spend | `search_purchases` | `start_date`, `end_date` (required), `max_results` |
| Vendor credits to net off | `search_vendor_credits` | `start_date`, `end_date` (required), `vendor_id` |
| Account-level transaction detail (tie-out) | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Chart of accounts, for box mapping | `search_accounts` | `query`/`name`, `active_only` |
| Attachment metadata (evidence a form exists) | `search_attachables` / `get_attachable` | `query`/`name`; `id` |
| Payer's own details | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
its failure envelopes. Where this table and the live description disagree, the live
description wins.

---

## Plain-language glossary

- **Information return** — a report you file *about someone else's* income (what you paid
  them), rather than about your own.
- **Payer / filer** — you, the business doing the reporting.
- **Reportable vendor** — a supplier or contractor whose payments must appear on a return.
- **Threshold** — the amount above which a vendor must be reported. Set by the jurisdiction,
  changes over time, always supplied by the user.
- **Box / line** — a numbered slot on a form. Each kind of payment belongs in a specific one.
- **Non-employee compensation** — money paid to someone who works for you but is not on
  payroll.
- **Gross proceeds paid to an attorney** — money routed through a lawyer (e.g. a settlement)
  that is reported even though it is not the lawyer's fee income.
- **Golden parachute** — an outsized payout triggered by a change of ownership.
- **W-9 / W-8** — US forms on which a vendor certifies their name, tax ID, and entity type.
  W-9 for US persons, W-8 series for non-US.
- **TIN / SIN / BN / UTR** — tax identification numbers (US / Canadian personal / Canadian
  business / UK).
- **EIN** — a US employer identification number; the business equivalent of a TIN.
- **Backup withholding** — holding back a slice of a payment and remitting it to the tax
  authority because the vendor did not certify their details.
- **CIS (Construction Industry Scheme)** — a UK regime where the main contractor deducts tax
  from subcontractor payments and reports monthly. Statuses: standard, higher, gross.
- **Treaty rate** — a reduced withholding rate available under a tax treaty between two
  countries.
- **Cash basis** — count it when the money moves. **Accrual basis** — count it when the
  obligation arises. Information returns often use cash basis even when the books use accrual.
- **General ledger (GL)** — the complete account-by-account record of every transaction.
- **Tie-out** — the proof that two sets of numbers agree; here, that the filing list matches
  the books.
- **Corrected return** — a re-filing that fixes an error on a return already submitted.
- **1042-S / NR4** — US and Canadian forms used for payments to non-residents, instead of a
  1099 / T4A.
