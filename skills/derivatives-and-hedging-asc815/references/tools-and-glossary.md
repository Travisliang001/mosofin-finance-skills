<!-- derivatives-and-hedging-asc815 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 7. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Derivative, OCI and gain / loss accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Recorded derivative positions and OCI balance** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Every movement, including OCI reclassifications** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Derivative gains and losses recognised, and where | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| **Cash settlements to and from counterparties** | `search_purchases` / `search_bill_payments` / `search_deposits` / `search_transfers` | `start_date`, `end_date` (required) |
| Counterparty banks | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| **Mark-to-market and reclassification entries** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| The hedged item, where it is interest-rate debt | `get_general_ledger` | `account`, `start_date`, `end_date` |
| Legal name, base currency, reporting dates | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no valuation service, no discount curve and no contract repository on this surface.**

---

## Plain-language glossary

- **Derivative** — a contract whose value moves with something else: a rate, a price, an index.
- **Notional** — the reference amount a derivative is calculated on. It is not usually exchanged.
- **Underlying** — the rate or price the derivative depends on.
- **Embedded derivative** — a derivative hidden inside an ordinary-looking contract. **The hardest thing
  to find in this area.**
- **Host contract** — the ordinary contract the embedded derivative sits inside.
- **ISDA / confirmation** — the master agreement and the trade-specific terms.
- **Hedge accounting** — optional treatment that lines up the timing of the derivative's gains and losses
  with the thing it protects. **Conditional on contemporaneous documentation.**
- **Designation** — formally nominating a derivative as a hedge of a specific item, in writing, at the
  outset.
- **Cash flow hedge** — hedging future cash flows; the effective part goes to OCI and is released later.
- **Fair value hedge** — hedging the value of something you already hold; both sides go through earnings.
- **Net investment hedge** — hedging the currency exposure of owning a foreign business.
- **Effective / ineffective portion** — how much of the hedge actually offsets, and how much does not.
  The ineffective part hits earnings immediately.
- **Prospective / retrospective testing** — will it work, and did it work.
- **Dollar-offset / regression** — two ways of measuring effectiveness numerically.
- **Dedesignation** — ending a hedge relationship; hedge accounting stops from that point.
- **Mark-to-market** — revaluing to current market value.
- **CVA / DVA** — adjustments for the risk that the counterparty, or you, fail to pay.
- **OCI** — gains and losses parked in equity rather than run through profit.
- **Reclassification / recycling** — moving those amounts from OCI into profit when the time comes.
- **Discount curve** — the set of rates used to value future cash flows.
