<!-- consolidation-and-eliminations · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on discovery; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections — **the candidate consolidation group**. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (**required — check every entity**) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call — and the correct entity's**), `approved` |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 11. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog, per entity**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **Each entity's trial balance, same date and method** | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| Cross-check and statement build | `get_balance_sheet` / `get_profit_and_loss` | `start_date`, `end_date`, `accounting_method` |
| **Locate IC accounts, investment and equity accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Transactions behind an IC balance — mismatch investigation** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Intercompany revenue and expense, both sides** | `search_invoices` / `search_bills` | `start_date`, `end_date` (required), `customer_id` / `vendor_id` |
| Identify which counterparties are group entities | `search_customers` / `search_vendors` | `query`/`name`, `active_only` |
| One-sided intercompany journals | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| IC balances by counterparty | `get_customer_balance` / `get_vendor_balance` | `report_date`, `customer` / `vendor` |
| Consolidated cash flow inputs | `get_cash_flow` / `search_transfers` | `start_date`, `end_date` |
| Inventory held (unrealised profit) | `search_items` / `read_item` | `query`/`name`; `id` |
| **Legal name, base currency, fiscal year end, per entity** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no FX rate tool and no ownership register in an accounting datasource.**

---

## Plain-language glossary

- **Consolidation** — presenting a group of companies as if it were one business.
- **Elimination** — removing what group companies did with each other, so only outside-world
  transactions remain.
- **Control** — the power to direct a business's activities. It, not ownership percentage alone,
  decides consolidation.
- **VIE / primary beneficiary** — an entity controlled by contract rather than shares, and the party
  that controls it.
- **Significant influence** — less than control, typically 20–50% ownership; leads to the equity
  method.
- **Equity method** — carrying an investment as one line that moves with your share of the investee's
  profits.
- **Non-controlling interest (NCI) / minority interest** — the part of a subsidiary owned by someone
  outside the group.
- **Full vs. partial goodwill** — whether NCI is measured at fair value or at its share of net assets.
- **Functional currency** — the currency of the environment an entity mainly operates in.
  **Presentation currency** — the currency the group reports in.
- **Current rate method** — translating a subsidiary at closing rates, with the difference to OCI.
- **Temporal / remeasurement method** — translating by item type, with the difference to profit.
- **Closing / average / historical rate** — the rate at period end, the period's average, and the rate
  on the date a specific transaction happened.
- **CTA (cumulative translation adjustment)** — the accumulated translation difference, held in OCI.
- **OCI** — gains and losses that bypass the profit and loss account.
- **Monetary vs. non-monetary items** — amounts fixed in currency (cash, debt) versus things
  (inventory, equipment).
- **Unrealised profit** — profit on a sale within the group that the group has not yet made from the
  outside world.
- **Stepped-up basis** — a higher carrying value after an intragroup sale, which must be unwound.
- **Push-down accounting** — recording acquisition fair values in the subsidiary's own books.
- **Deconsolidation** — removing a subsidiary from the group on disposal.
- **Coterminous** — having the same period end.
- **Reciprocal shareholding** — a subsidiary owning shares in its own parent.
- **Hyperinflationary economy** — one where prices rise so fast that financial statements must be
  restated before translation.
