<!-- esg-sustainability-reporting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 5. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Legal name, currency, country, industry | `get_company_info` | none (uses the connected company) |
| **Expense categories — the spend-based raw material** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Spend by category, and by site where classed** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class`, `department`, `location` |
| **The supplier list, for Scope 3 engagement** | `search_vendors` / `get_vendor` | `query`/`name`, `active_only`; `id` |
| **Spend by supplier and category** | `search_bills` / `search_expenses` / `search_purchases` | `start_date`, `end_date` (required) |
| Utility, fuel, travel and freight account movements | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Headcount — the intensity denominator** | `search_employees` / `get_employee` | `query`/`name`, `active_only`; `id` |
| Site or segment structure | `search_locations` / `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Vehicles and plant — Scope 1 indicators | `search_fixed_assets` / `get_balance_sheet` | varies; `start_date`, `end_date` |
| Ownership percentages for equity-share boundary | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no emission factor database, no meter reading, no HR system and no safety register on this
surface.**

---

## Plain-language glossary

- **ESG** — environmental, social and governance: the three headings under which non-financial performance
  is reported.
- **GHG (greenhouse gas)** — the emissions being counted, expressed as **tCO₂e**, tonnes of carbon dioxide
  equivalent, so that different gases can be added together.
- **Scope 1** — emissions from things you burn directly: your boilers, your vehicles.
- **Scope 2** — emissions from the energy you buy, chiefly electricity.
- **Scope 3** — everything else in your value chain: what you buy, how staff travel, how products are used
  and disposed of. **Usually the largest and the hardest to measure.**
- **Emission factor** — the multiplier converting an activity into emissions: per kWh, per litre, per
  tonne, or per unit of spend.
- **Spend-based method** — estimating emissions from money spent × a factor. **Legitimate, standard, and
  the least accurate tier** — it cannot distinguish a price rise from a volume rise.
- **Activity data** — the underlying measure being multiplied by the factor: kWh, litres, kilometres, or
  currency.
- **Organizational boundary** — which entities count as yours.
- **Operational boundary** — which activities count, by Scope.
- **Equity share approach** — count emissions in proportion to ownership.
- **Control approach** — count all of what you control, none of what you do not.
- **Intensity metric** — emissions divided by something: per employee, per unit of revenue. Lets you
  compare across sizes and years.
- **Assurance** — independent checking of reported figures, the ESG equivalent of an audit. **Limited**
  assurance is a lower bar than **reasonable** assurance.
- **Data quality tier** — how good the number is: measured, calculated, or estimated.
- **DEI** — diversity, equity and inclusion.
- **Materiality (ESG sense)** — which topics matter enough to report. **Note it is not the financial
  definition** — the same word, a different test.
- **Greenwashing** — presenting environmental performance more favourably than the evidence supports,
  including by accident.
- **Restatement** — reissuing prior-year figures after a boundary or method change, so the series stays
  comparable.
