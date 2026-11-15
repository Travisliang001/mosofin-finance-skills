<!-- business-combinations-asc805 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on discovery; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections and their `connected` flag. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (**required here — check both entities**) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call — and the correct entity's**), `approved` |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 11. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Acquiree's book values **at** the acquisition date | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| Acquiree's results **since** the acquisition date (disclosure) | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Acquiree's prior-period results (pro-forma input) | `get_profit_and_loss` | `start_date`, `end_date` |
| Detail behind an acquired balance | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Both charts of accounts, for mapping | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Deal costs, to test they were expensed** | `search_bills` / `get_vendor_expenses` / `search_purchases` | `start_date`, `end_date` (required), `vendor_id`, `vendor` |
| Any acquisition entry already posted | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Customer base evidencing customer-relationship intangibles | `search_customers` / `get_customer_sales` | `query`/`name`; `start_date`, `end_date`, `customer` |
| Order backlog evidencing a backlog intangible | `search_estimates` / `search_purchase_orders` | `start_date`, `end_date` (required) |
| Acquired inventory items (step-up population) | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Assumed payables and receivables | `get_aged_payables` / `get_aged_receivables` | `report_date`, `vendor`/`customer` |
| Legal name, currency, year-end, for each entity | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no valuation tool in this table because none exists.**

---

## Plain-language glossary

- **Business combination** — one business acquiring control of another.
- **Acquisition method** — the required way of accounting for it: revalue everything acquired,
  recognise goodwill for the excess.
- **Acquirer** — the one obtaining control. **Acquiree** — the one acquired.
- **Acquisition date** — the date control passes. Everything is measured on it.
- **Purchase price allocation (PPA)** — spreading what you paid across everything you bought.
- **Fair value** — what something would sell for between willing parties, not what it is carried at.
- **Goodwill** — the excess paid over the fair value of the identifiable things acquired.
- **Bargain purchase** — paying less than that; rare, and usually a sign of an error.
- **Identifiable intangible** — something without physical form that can be separated and sold, or
  arises from a contract or legal right.
- **Contractual-legal / separability criterion** — the two tests for recognising an intangible
  apart from goodwill.
- **IPR&D** — in-process research and development acquired part-finished.
- **Order backlog** — orders received but not yet fulfilled.
- **Assembled workforce** — a trained team. Valuable, but specifically **not** recognised separately.
- **Contingent consideration / earnout** — extra payment owed if the acquired business hits targets.
- **Step acquisition** — gaining control when you already held a stake.
- **Non-controlling interest (NCI)** — the share of a subsidiary someone else owns.
- **Full goodwill / partial goodwill** — whether NCI is measured at fair value or at its share of
  net assets.
- **Measurement period** — up to a year to finalise provisional values, using facts that existed at
  the acquisition date.
- **Provisional amount** — a value recorded before the final one is known.
- **Step-up** — increasing an asset's carrying amount to fair value.
- **Reverse acquisition** — the legal buyer is, in accounting terms, the one acquired.
- **Common control** — both parties already controlled by the same person or group.
- **Carryover basis** — keeping existing book values rather than revaluing.
- **Pro forma** — figures showing what results would have looked like had the deal happened earlier.
- **NOL / DTA / valuation allowance** — tax losses carried forward, the asset they create, and the
  provision against it if it may not be used.
