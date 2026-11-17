<!-- gaap-vs-ifrs-conversion · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The chart of accounts — the scoping instrument** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Source balances at the conversion date** | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Source equity and balance sheet, both periods** | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| **Source net income** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Movement detail behind a difference area | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Legal name, currency, country, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no accounting policy manual, no lease register, no fixed-asset register, no actuarial report and
no valuation on this surface.**

---

## Plain-language glossary

- **US GAAP** — the American rulebook. **IFRS** — the international one, used in most of the rest of the
  world. **Local GAAP** — a country's own rules.
- **Conversion adjustment** — the entry that changes a figure from one rulebook's answer to the other's.
- **Reconciliation / bridge** — the line-by-line explanation of how one framework's profit or equity becomes
  the other's.
- **LIFO / FIFO / weighted average** — assumptions about which units of stock were sold first. **LIFO is
  allowed in the US and banned under IFRS**, which is why it is the largest single conversion item.
- **Revaluation model** — carrying assets at current value rather than cost. **IFRS optional; US GAAP not
  permitted.**
- **Component depreciation** — depreciating parts of an asset separately because they wear out at different
  rates.
- **Impairment** — writing something down because it is worth less than its book value. **IFRS lets you
  reverse it later; US GAAP generally does not.**
- **Value in use** — what an asset is worth to you from continued use, discounted.
- **Research vs. development** — investigating versus building. **IFRS capitalises qualifying development;
  US GAAP generally expenses both.**
- **CECL / IFRS 9** — the two expected-loss models for estimating bad debts and credit losses.
- **Provision** — a liability of uncertain timing or amount. **The threshold for recognising one differs
  between the frameworks.**
- **Deferred tax** — tax arising because book and tax treatments differ in timing. **Nearly every conversion
  adjustment creates one.**
- **IFRS 1** — the standard governing your first IFRS accounts, with exemptions that make the transition
  practical.
- **Transition date** — the start of the earliest period presented under the new framework; where the
  cumulative adjustment lands.
- **Deemed cost** — an IFRS 1 exemption letting you treat a valuation as if it were original cost, avoiding
  a full retrospective rebuild.
- **Converged standards** — rules the two boards wrote together. **Converged is not identical.**
