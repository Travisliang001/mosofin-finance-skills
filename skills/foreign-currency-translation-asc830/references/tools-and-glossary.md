<!-- foreign-currency-translation-asc830 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Legal name and home currency, per entity** | `get_company_info` | none (uses the connected company) |
| **Trial balance in local currency, per entity** | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Opening and closing net assets — for the CTA proof** | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| **Earnings, and their spread across the period** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Account names and types, for classification | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Intercompany, equity and CTA movements** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Intercompany populations, both sides | `search_invoices` / `search_bills` | `start_date`, `end_date` (required) |
| Functional-currency evidence — who is billed, who is paid | `search_customers` / `search_vendors` | `query`/`name`, `active_only` |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no exchange rate service and no historical rate table on this surface.**

---

## Plain-language glossary

- **Functional currency** — the currency of the environment an entity really operates in. **An accounting
  conclusion, not a setting.**
- **Reporting / presentation currency** — the currency the group publishes in.
- **Home currency** — what the accounting file is configured in. **Usually the functional currency, not
  always.**
- **Remeasurement** — converting foreign-currency transactions into the entity's own functional currency.
  **Gains and losses hit profit.**
- **Translation** — converting a whole entity's statements into the group's reporting currency. **Differences
  go to OCI, not profit.**
- **Monetary items** — a fixed number of currency units: cash, receivables, payables, loans.
- **Nonmonetary items** — everything else: inventory, fixed assets, prepayments, **deferred revenue**.
- **Spot rate** — today's rate. **Closing rate** — the rate at period end. **Average rate** — a period
  average, used for income and expenses. **Historical rate** — the rate when the item first arose.
- **CTA (cumulative translation adjustment)** — the accumulated difference from translating at different
  rates. **Sits in equity via OCI, and is computed as a balancing figure — which is why it must be proved
  separately.**
- **OCI (other comprehensive income)** — gains and losses recorded in equity rather than profit.
- **Net investment** — an intercompany balance that is really part of the parent's investment rather than a
  debt to be repaid. **Its FX difference goes to CTA, not earnings.**
- **Hyperinflationary economy** — one with extreme cumulative inflation, where normal translation gives
  meaningless results and a different method is required.
- **Repatriation** — bringing cash back to the parent's country.
- **Plug** — a figure derived by making something else balance. **A plug never fails, which is exactly the
  problem.**
