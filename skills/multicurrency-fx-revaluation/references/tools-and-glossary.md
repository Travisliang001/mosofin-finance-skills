<!-- multicurrency-fx-revaluation · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Home currency, per entity** | `get_company_info` | none (uses the connected company) |
| **The balance population** | `get_trial_balance` / `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| **The chart with types; FX and CTA accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **What was actually posted to FX and CTA** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Open versus settled balances — the realized / unrealized split** | `search_invoices` / `search_bills` / `search_payments` | `start_date`, `end_date` (required) |
| The FX result recorded | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no FX rate service, no hedge documentation and no functional currency determination on this
surface.**

---

## Plain-language glossary

- **Functional currency** — the currency an entity really operates in. **A determination, not a choice, and
  not the same thing as the currency its software is set to.**
- **Presentation currency** — the currency the accounts are published in.
- **Transaction FX** — gains and losses from dealing in a currency that is not yours. **Hits profit.**
- **Translation** — converting a whole entity's accounts into another currency. **Hits OCI, not profit.**
- **Remeasurement** — restating individual balances into the functional currency.
- **Monetary items** — a fixed number of currency units: cash, receivables, payables, debt. **Revalued.**
- **Non-monetary items** — inventory, fixed assets, prepayments, **deferred revenue**, equity. **Not
  revalued** — they settle in goods or services, not money.
- **Realized FX** — the gain or loss when a balance actually settles. **Unrealized FX** — the paper movement
  on a balance still outstanding. **Unrealized reverses if rates move back; realized does not.**
- **Spot rate** — today's. **Closing rate** — at period end. **Average rate** — over the period.
  **Historical rate** — when the item first arose.
- **CTA (cumulative translation adjustment)** — the accumulated translation difference, held in OCI until
  the operation is sold.
- **Current-rate method** — the usual translation method for a foreign sub. **Temporal method** — used when
  the sub's functional currency is really the parent's.
- **Net investment hedge** — a foreign-currency borrowing designated to offset the CTA on a foreign
  subsidiary. **Only with documented designation.**
- **Hedge accounting** — special treatment matching a hedge to what it hedges. **Requires designation and
  documentation in advance; it cannot be applied retrospectively.**
- **Hyperinflationary economy** — one where normal translation gives meaningless results and restatement is
  required first.
