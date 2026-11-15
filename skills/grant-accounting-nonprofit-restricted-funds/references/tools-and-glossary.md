<!-- grant-accounting-nonprofit-restricted-funds · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **The grant, fund and program dimensions** | `search_classes` / `search_departments` / `search_locations` | `query`/`name`, `active_only` |
| **Grant-tagged expenditure — the core data** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department` |
| **Expenditure detail, and release entries already posted** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Restricted and unrestricted net assets, grants receivable** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `class`, `accounting_method` |
| Net asset, contribution revenue and receivable accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Cash received by funder** | `search_deposits` / `search_payments` | `start_date`, `end_date` (required) |
| Funders, often set up as customers | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Grant billings raised as invoices | `search_invoices` / `get_invoice` | `start_date`, `end_date` (required); `id` |
| Legal name, **fiscal year end** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no grant agreement, no allowable cost rule and no indirect cost rate on this surface.**

---

## Plain-language glossary

- **Contribution** — money given without the giver receiving equivalent value back. **Exchange
  transaction** — money given *for* something, which is ordinary revenue.
- **Condition** — a **barrier** the organisation must clear, plus a **right of return** if it does not.
  **A conditional contribution is not revenue yet**, however firmly it has been promised.
- **Restriction** — a limit on **how or when** the money may be used. **Restricted money is still revenue
  now** — it just sits in a different class of net assets.
- **Net assets with / without donor restrictions** — the nonprofit equivalent of equity, split by whether
  outsiders have tied it up.
- **Release from restriction** — moving money from restricted to unrestricted once the purpose or the time
  condition has been satisfied. **Not a receipt and not revenue** — a transfer between classes.
- **Purpose restriction** — must be spent on a stated thing. **Released as qualifying costs are incurred.**
- **Time restriction** — cannot be used until a stated period. **Released when the date arrives.**
- **Refundable advance** — cash received for a conditional grant, held as a liability because it may have to
  go back.
- **Allowable / unallowable costs** — what the funder will and will not pay for. Commonly excluded:
  entertainment, alcohol, lobbying, fundraising.
- **Indirect cost rate** — the agreed percentage covering overheads that cannot be traced to one grant.
  **De minimis** — a standard fallback rate where none has been negotiated.
- **Variance power** — the discretion to redirect funds to a different purpose or recipient. **Decides
  whether a fiscal sponsor reports the money as its own revenue.**
- **Single Audit** — the additional audit required of organisations spending above a threshold of federal
  funds in a year; **it tests grant compliance, not just the financial statements.**
- **Grant register** — the master list of awards, terms and deadlines.
