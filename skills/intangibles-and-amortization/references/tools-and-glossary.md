<!-- intangibles-and-amortization · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 13. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Intangible, accumulated amortization, expense and R&D accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Cost and accumulated amortization, opening and closing** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Capitalizations and disposals — every intangible account movement** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Development spend by project and month — the Step 4 population** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department` |
| **Contractor and external development invoices** | `search_bills` / `search_purchases` / `get_bill` | `start_date`, `end_date` (required); `id` |
| **The project dimension** | `search_classes` / `search_departments` / `search_projects` | `query`/`name`, `active_only` |
| Legal name, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no intangible register, no useful life, no stage determination and no valuation on this
surface.**

---

## Plain-language glossary

- **Intangible asset** — something the business owns that has no physical form but will earn money for
  years: a brand, a patent, a customer list, software.
- **Identifiable** — separable from the business, or arising from legal rights. **What is not identifiable
  ends up in goodwill.**
- **Amortization** — the intangible equivalent of depreciation: spreading the cost over its useful life.
- **Finite vs. indefinite life** — whether it runs out. **Indefinite-lived intangibles are never amortized
  but must be impairment-tested every year.**
- **Residual value** — what it will be worth at the end. **Almost always zero for intangibles.**
- **Internally developed** — built rather than bought. **The costs of building count only in certain
  stages.**
- **Preliminary / application development / post-implementation** — the three phases of a software project.
  **Only the middle one is capitalized.**
- **Technological feasibility** — the point in a for-sale software project after which costs may be
  capitalized.
- **Research vs. development** — investigating versus building. **Research is always expensed.**
- **The six IFRS criteria** — technical feasibility, intent, ability, benefits, resources, measurement.
  **All six, or it is expensed.**
- **In-process R&D (IPR&D)** — an unfinished project acquired with a business; carried as indefinite-lived
  until it finishes or is abandoned.
- **Order backlog** — signed orders not yet fulfilled; a short-lived acquired intangible.
- **Non-compete agreement** — a paid promise not to compete; amortized over its term.
- **Built vs. acquired brands** — **a brand you bought is on the balance sheet; a brand you built is not.**
  The cost of building it could never be measured reliably.
- **Cloud computing arrangement** — software accessed as a service. **Implementation costs may be a prepaid
  asset rather than an intangible.**
- **Change in estimate, prospective** — revising a useful life affects future periods only; you do not go
  back and restate.
