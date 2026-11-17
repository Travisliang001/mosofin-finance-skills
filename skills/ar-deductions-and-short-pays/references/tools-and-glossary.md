<!-- ar-deductions-and-short-pays · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on discovery; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections and their `connected` flag. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (required when several files are live) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call**), `approved` (only after an explicit yes, reads only) |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 7. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Invoices behind each deduction | `search_invoices` / `get_invoice` | `start_date`, `end_date`, `customer_id`; `id` |
| The short payments and their memos | `search_payments` / `get_payment` | `start_date`, `end_date`, `customer_id`; `id` |
| Credits already issued | `search_credit_memos` / `get_credit_memo` | `start_date`, `end_date`, `customer_id`; `id` |
| Receivables the log must sit inside | `get_aged_receivables` | `report_date`, `aging_method` |
| Customer terms and contacts | `search_customers` / `get_customer` | `query`/`name`; `id` |
| Deduction account balance | `get_general_ledger` | `start_date`, `end_date`, `account` |
| Real account names for proposed entries | `search_accounts` | `query`/`name`, `active_only` |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments. Where
this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Deduction / short pay** — an amount a customer held back from a payment, with a reason.
- **Reason code** — the customer's label for why they deducted.
- **Proof of delivery (POD)** — the delivery note signed by the customer on receipt; it shows
  what arrived and in what condition.
- **Carrier exception / damage report** — the carrier's record that goods arrived damaged or
  short.
- **Promotion agreement** — a written deal giving the customer a discount for set dates, rate and
  products.
- **FOB origin / FOB destination** — who owns the goods, and pays freight, in transit: the
  customer from the seller's dock (origin), or the seller until delivery (destination).
- **Credit memo** — a document reducing what the customer owes.
- **Write-off** — removing a small balance from receivables as not worth recovering, under a
  policy limit.
- **Dispute window** — how long a customer accepts a challenge to a deduction.
- **Journal entry (JE)** — the balanced two-sided record. **DR** = debit, **CR** = credit.
