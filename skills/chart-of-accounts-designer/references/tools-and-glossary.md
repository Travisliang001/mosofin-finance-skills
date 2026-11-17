<!-- chart-of-accounts-designer · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The full chart of accounts, incl. inactive** | `search_accounts` | `query`/`name`, `active_only`, `max_results`, `offset` |
| One account's type, sub-type, parent, status | `get_account` | `id` |
| **Usage per account: counts, values, last activity** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Balances, to pair with usage | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| How accounts roll up in reporting today | `get_profit_and_loss` / `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by` |
| **Dimensions actually in use** | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| **Tax structure actually in use** | `search_tax_codes` / `search_tax_rates` / `search_tax_agencies` | `query`/`name`, `active_only` |
| How revenue is really segmented | `search_items` / `get_customer_sales` | `query`/`name`; `start_date`, `end_date`, `customer` |
| Manual entries revealing workaround accounts | `search_journal_entries` | `start_date`, `end_date` (required) |
| Vendors and customers, for other-receivable design | `search_vendors` / `search_customers` | `query`/`name`, `active_only` |
| Industry, currency, legal name | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Chart of accounts (COA)** — the list of buckets every transaction is sorted into.
- **Account type** — the top-level nature: asset, liability, equity, revenue, expense.
- **Detail type / sub-type** — the platform's finer classification within a type.
- **Normal balance** — whether an account usually carries a debit or a credit.
- **Contra account** — an account that reduces another (accumulated depreciation against fixed
  assets; allowance for doubtful accounts against receivables).
- **Dimension** — an extra tag on a transaction (class, department, location, project) used to slice
  reports without creating more accounts.
- **Sub-ledger** — a detailed record behind one account, such as the list of unpaid invoices behind
  receivables.
- **Right-of-use (ROU) asset** — the asset recorded when you lease something.
- **CTA (cumulative translation adjustment)** — the equity account holding FX differences from
  translating a foreign business.
- **Retainage** — money a customer withholds from a construction payment until completion.
- **WIP (work in progress)** — partly finished work or production.
- **Costs / billings in excess** — the construction accounts recording whether you have billed ahead
  of or behind the work done.
- **CAM recoveries** — common area maintenance charges recharged to tenants.
- **Percentage-of-completion (POC)** — recognising revenue as a contract progresses.
- **Restricted vs. unrestricted net assets** — nonprofit funds with and without donor conditions.
- **Elimination account** — used to cancel intercompany amounts on consolidation.
- **Migration journal entry** — the entry needed to move a balance when accounts are merged or
  renumbered.
