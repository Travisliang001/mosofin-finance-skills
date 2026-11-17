# QuickBooks read-only capability reference — Mosofin gateway

Orientation for the QuickBooks Online read surface as it is reached **through the Mosofin gateway**. Use it to understand the *shape* of what QuickBooks offers: which reports exist, what arguments they take, what they will and will not tell you.

> ## This file is orientation. It is not authority.
>
> **`get_datasource_tools` is authority.** Read it every run, read the `effective_policy` on every tool you intend to call, and take tool names from the response rather than from this document.
>
> The version of this reference that shipped with the original skill listed concrete tool identifiers of the form `mcp__codex_apps__intuit_quickbooks_...`, several with build hashes in them. **Those are removed here and must not be reintroduced.** Two reasons, and the second is the important one:
>
> 1. They are the wrong path. Under Mosofin, QuickBooks is a **datasource behind the gateway**, not a directly installed MCP server. Its capabilities are enumerated by `get_datasource_tools` and invoked through `invoke_datasource_api_tool` carrying a `data_source_id`. A client-side namespaced identifier will not resolve.
> 2. They go stale silently. A hashed identifier written into a document is a snapshot of one build. When the build changes, the document does not — it keeps confidently naming a tool that no longer exists, and a reader trusting it will get `UNKNOWN_TOOL` with no idea why.
>
> The original file gave the right instinct — *"resolve tools by the stable capability description rather than depending on a full hashed name"* — and then undercut it by printing the hashed names anyway. This version keeps the instinct and drops the names.
>
> The same applies to **availability**. Nothing in this file tells you whether a capability is available to you today. Only `effective_policy` does: `enabled` → `[auto]`, `permission` → `[gated]`, `disabled` → `[manual]`.

---

## Core capabilities

### Company information

- **Purpose**: identify the connected QuickBooks company.
- **Arguments**: none.
- **Binding**: the capability whose description identifies the connected company.
- **Order**: call it before the accounting-report capabilities — **but after Gate 0 and Gate 1.** Confirming the company is not the same as confirming the workspace, and under Mosofin the workspace comes first. Match the returned name against the `display_name` from `get_agent_datasources`.

### A/R Aging Summary

- **Purpose**: independent customer and bucket totals, for reconciliation against the detail.
- **Arguments**:
  - `as_of_date` — optional `YYYY-MM-DD`; defaults to today. **Pass it explicitly** so that detail and summary provably share a date.
  - `customer_name` — optional, exact, case-insensitive.
  - `min_days_overdue` — optional; one of `0`, `1`, `31`, `61`, `91`.
  - `min_overdue_amount` — optional number.
  - `top_n` — optional number.
- **Restriction**: use **only one** of `min_days_overdue`, `min_overdue_amount`, `top_n` in a single call.
- **For reconciliation, omit every threshold and ranking filter.** A filtered summary is not an independent total and cannot tie to a full detail.
- **Binding**: the capability whose description identifies the A/R Aging Summary report.
- **Presentation variants may exist** (a standard presentation and a plain-text one). Prefer the standard presentation unless the task specifically needs plain text.
- **Accounting basis**: the original asserted accrual-only. **Do not assert it — check.** Read the parameters the capability actually returns at Gate 2. If a basis parameter exists, the constraint has changed. If none exists, the constraint holds for this connector today and a cash-basis request must be declined and explained, not silently served an accrual report.

### A/R Aging Detail

- **Purpose**: line-level open transactions — customer, transaction type, due date, amount, aging grouping.
- **Arguments**:
  - `as_of_date` — optional `YYYY-MM-DD`; defaults to today.
  - `customer_name` — optional, exact, case-insensitive.
  - `transaction_type` — optional; values such as `invoice`, `credit memo`, `payment`, `journal entry`, `sales receipt`, `refund`, `charge`, `statement`.
- **For the primary invoice population, pass `transaction_type: "invoice"`.**
- **For reconciliation diagnostics, make a second unfiltered call** when the invoice-only detail does not tie to the summary. The non-invoice rows — credits, payments on account, journal entries — are usually the whole explanation, and they matter for collections as well as for the tie-out: a customer with an unapplied credit may not owe what the invoice-only view says.
- **Binding**: the capability whose description identifies the A/R Aging Detail report.

### Get invoices

- **Purpose**: enrich **known** invoices with detail — line items, customer information, due date, balance, payment status.
- **Arguments**: `customer_id`; `doc_numbers` (visible invoice numbers); `invoice_ids` (internal ids); `limit` (up to 1000); `order_by` (`Id`, `DocNumber`, `TxnDate`, `DueDate`, `TotalAmt`, `Balance`, optionally with ` DESC`); `transaction_date` (a date-filter object where supported).
- **Critical restriction, preserved with emphasis**: an unbounded call **defaults to a recent transaction window**. **Never use it as the sole A/R population.** The invoices it omits are the oldest unpaid ones — precisely the population a collections run exists to find. An aging built this way looks complete and is not.

---

## Optional read-only capabilities

### Customer search

- **Arguments**: `customer_name`, optional `customer_email`.
- Use for **fuzzy resolution or a single selected draft only.** It is not a complete customer-master export and must not be used to enumerate the customer base.
- If no customer is found, **ask the user.** Do not invoke any create-customer workflow — and note that under the Mosofin gateway there is no create path at all.

### Profit and loss

- **Arguments**: `periodStart`, `periodEnd`. Presentation variants may exist.
- Use **only** when the user wants DSO and has accepted total accrual-basis income as a proxy for credit sales. **Label the result approximate.**
- **Before falling back to the proxy, check whether credit sales are separable.** If the surface distinguishes invoices from sales receipts, credit sales for the period is a live read and the DSO is exact. The proxy is a fallback, not a default.

### Sales settings

- Can expose payment-term definitions, and sometimes a global reminder template, where the schema supports it.
- **Do not update settings** — and again, there is no update path through the gateway.
- **The due date on the aging detail remains authoritative for the aging calculation.** Terms are for drafting language, not for recomputing what the report already states.

---

## Forbidden capabilities in this skill

Do not call any capability that sends reminders, creates or updates invoices or customers, changes payment terms, applies payments, writes off balances, or otherwise mutates QuickBooks.

**The presence of such a tool in the listing does not grant permission to use it** — and neither does an `effective_policy` of `enabled`. Policy says what the gateway permits; this skill's scope says what it does. They are different questions, and this skill's answer is: read only, send nothing.

---

## QuickBooks-to-output mapping

| Output field | Preferred source | Transformation |
|---|---|---|
| Workspace | `list_workspaces` | Name only — **never the numeric id** |
| Company | `get_agent_datasources` + company information | `display_name` — **never the `data_source_id`** |
| As-of date | Aging report request/header | Normalize to `YYYY-MM-DD` |
| Customer | A/R Aging Detail | Preserve the returned display name |
| Customer ID | A/R Aging Detail or invoice enrichment | Preserve as text; blank if absent |
| Invoice # | A/R Aging Detail | **Preserve as text** — a leading zero lost to numeric coercion is an invoice nobody can find |
| Invoice ID | A/R Aging Detail or invoice enrichment | Preserve as text; blank if absent |
| Invoice date | A/R Aging Detail | Normalize the format without changing the date |
| Due date | A/R Aging Detail | Normalize the format without changing the date |
| Open balance | A/R Aging Detail | Use the returned outstanding amount, **not the original total** |
| Days past due | Calculated | `as_of_date − due_date`, calendar days |
| Custom bucket | Calculated | Apply the ranges in SKILL.md |
| Native bucket | A/R report | **Preserve** — it is the reconciliation counterpart |
| Currency | Report or invoice response | Preserve; ask before presenting unlabeled multi-currency totals |
| Original amount | Invoice enrichment | Blank when unavailable; **never substitute open balance** |
| Dispute / credit hold / strategic tier | The user, or another authoritative system | **Never infer from lateness or from notes** |
| Days-to-pay history | Calculated from settled invoices | Derived, lagging, and excludes non-payers — carry the caveats with the figure |
| Fixture flag | `mock: true` on any response | Propagate to the file name, the provenance sheet, and every draft |

---

## Failure and fallback behaviour

| Failure | Required response |
|---|---|
| **Workspace not confirmed** | Stop. Gate 0 precedes everything. |
| No authentication / `reconnect_url` returned | Tell the user the connection needs their attention; do not proceed on partial data |
| Wrong company | Ask the user to select the intended company file **by `display_name`**; do not analyse the wrong file and caveat afterwards |
| `approval_required` envelope | Explain what you want to read and why, obtain consent, re-invoke with `approved=true` (**reads only — never for a write**) **and the `data_source_id`** |
| `tool_policy_disabled` | The capability is `[manual]` here. Request the smallest equivalent export and label it user-supplied |
| `UNKNOWN_TOOL` | The name is wrong. **Re-read `get_datasource_tools`** — do not try a near-miss |
| `entity_required` | Ask which company file, **by `display_name`** |
| Cash-basis aging requested | Explain that this connector's aging is accrual-only **as observed at Gate 2**, and ask whether accrual is acceptable |
| A/R Aging Detail unavailable | Request the smallest equivalent export. **Do not replace it with a recent-only invoice pull** |
| Summary unavailable | Continue if still useful, label totals as detail-derived, and **disclose the absence of an independent tie-out** |
| Missing due dates | Ask for terms or due dates on the affected invoices, or classify them as exceptions. **Do not invent terms** |
| Detail-summary mismatch | Pull unfiltered detail, identify the non-invoice rows, **disclose any remaining variance. Never force a tie** |
| Missing policy flags | Ask once, if they affect the requested priority or drafts. Otherwise omit and disclose — **never treat an absent flag as a negative finding** |
| `mock: true` on any response | Label as fixture-derived everywhere, and **do not hand over draft letters** — the customers are not real |

---

## Official Intuit references

- [Run reports](https://developer.intuit.com/app/developer/qbo/docs/workflows/run-reports) — the `AgedReceivables` and `AgedReceivableDetail` Reports API capabilities and the report response structure.
- [Explore the QuickBooks Online API](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api) — entities, reports, read and query operations, authorization context.
- [Query operations and syntax](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/data-queries) — query constraints, pagination, invoice and customer examples.
- [Invoice entity](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice)
- [CompanyInfo entity](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/companyinfo)

**The live capability schema returned by `get_datasource_tools` is the authority for exact arguments.** The Intuit REST documentation explains the underlying data model and is useful for understanding what a field means. It **must not be used to invent parameters** the gateway does not expose — the REST API is a superset of what any given connector surfaces, and a parameter that exists in Intuit's documentation but not in the returned schema will simply fail.
