<!-- inventory-costing-fifo-lifo-wavg · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The item master, quantity on hand, average cost** | `search_items` / `search_products` / `get_item` | `query`/`name`, `active_only`; `id` |
| **Purchases with date, quantity and unit cost — the layer inputs** | `search_purchases` / `search_bills` / `get_bill` | `start_date`, `end_date` (required); `id` |
| **Sales with date, quantity and price — consumption and the NRV anchor** | `search_invoices` / `search_sales_receipts` / `get_invoice` | `start_date`, `end_date` (required); `id` |
| **The inventory balance, opening and closing** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **COGS as recorded, and whether it posts per sale** | `get_profit_and_loss` / `get_general_ledger` | `start_date`, `end_date`, `account` |
| Inventory, COGS, freight-in and write-down accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Legal name, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no layer stack, no replacement cost, no standard cost variance report and no physical count on
this surface.**

---

## Plain-language glossary

- **Cost flow assumption** — the convention deciding which purchase cost attaches to which sale. **Not a
  claim about which physical unit moved.**
- **FIFO** — oldest costs go to COGS; newest stay in inventory.
- **LIFO** — newest costs go to COGS; oldest stay in inventory. **Banned under IFRS.**
- **Weighted-average** — everything blended. **Periodic** blends once per period; **moving-average**
  re-blends after every purchase.
- **Specific identification** — tracking each individual item. Practical only for unique or high-value
  goods.
- **Layer** — a batch of units bought at one price on one date. **The stack of layers is what FIFO and LIFO
  consume from.**
- **Periodic vs. perpetual** — COGS worked out once at period end, or recorded with every sale.
- **LIFO reserve** — the difference between LIFO inventory and what it would be under FIFO. **The bridge
  between the two.**
- **LIFO liquidation** — selling more than you buy, so old cheap layers hit COGS and margins look
  artificially good. **Not repeatable.**
- **Dollar-value LIFO** — LIFO applied to pools of dollars adjusted by a price index, rather than to units.
- **NRV (net realizable value)** — what you will get for it, **less what it will cost to finish and sell
  it.**
- **LCM (lower of cost or market)** — the older US rule using replacement cost, with a ceiling and floor.
  **Still applies to LIFO and retail-method inventory.**
- **Write-down** — reducing inventory to NRV. **IFRS lets you reverse it if things recover; US GAAP does
  not.**
- **Conversion costs** — labour and production overhead added to raw materials to make finished goods.
- **Normal capacity** — the production level used to allocate fixed overhead. **Allocating on actual low
  output would push idle-capacity cost into inventory, which is not allowed.**
- **Standard costing** — using planned costs day to day and correcting to actual through variances at period
  end.
- **Consigned inventory** — goods physically with one party but owned by another. **Ownership decides whose
  balance sheet it is on, not location.**
- **FOB shipping point / destination** — whether title passes when goods leave the seller or when they
  arrive. **Decides who owns goods in transit at period end.**
