<!-- inventory-obsolescence-and-reserve · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The item master: SKU, quantity, cost, location** | `search_items` / `search_products` / `get_item` | `query`/`name`, `active_only`; `id` |
| **Movement by SKU — the core input** | `search_invoices` / `search_sales_receipts` / `get_invoice` | `start_date`, `end_date` (required); `id` |
| **Last receipt dates and purchase prices** | `search_purchases` / `search_bills` | `start_date`, `end_date` (required) |
| **Inventory and reserve balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Prior additions and write-offs — the back-test population** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Obsolescence expense by period | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Inventory, reserve and expense accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Legal name, currency, industry | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no demand forecast, no lot condition and no physical inspection on this surface.**

---

## Plain-language glossary

- **Obsolete** — will never sell at anything like cost: superseded, expired, out of fashion.
  **Slow-moving** — still sells, just rarely. **Excess** — good stock, far too much of it. **Three different
  problems needing three different answers.**
- **E&O (excess and obsolete)** — the usual collective name.
- **Reserve / provision** — an allowance held against inventory that will not realise its cost. **The
  inventory stays on the books at cost with the reserve netted against it.**
- **Write-off** — actually removing the item. **Uses the reserve; does not create new expense if reserved
  properly.**
- **Aging bucket** — how long stock has been held, in bands.
- **Days on hand / months of supply** — how long current stock would last at the recent rate of sale.
- **No-move** — nothing sold or issued in a defined period.
- **LCNRV (lower of cost or net realizable value)** — carry it at cost, or at what you will really get for
  it, whichever is less.
- **NRV** — expected selling price **less costs to complete and sell**.
- **S&OP forecast** — the sales and operations plan: what the business expects to sell. **Not in the
  accounting system.**
- **Specific identification** — reserving named items rather than applying a percentage.
- **End-of-life** — a product being discontinued, often with a final buy of spares that will legitimately
  sit for years.
- **Roll-forward** — opening reserve, additions, usage, closing reserve.
- **Back-test** — checking whether last period's estimate turned out to be right.
