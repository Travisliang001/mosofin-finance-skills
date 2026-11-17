<!-- bad-debt-and-write-offs · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| A/R aging now — and **at past dates**, for loss rates | `get_aged_receivables` | `report_date`, `customer`, `aging_method`, `days_per_aging_period`, `num_periods` |
| Balance per customer | `get_customer_balance` | `report_date`, `customer` |
| Allowance / bad-debt / recovery accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Movement on those accounts (write-offs, recoveries) | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Existing allowance balance | `get_trial_balance` / `get_balance_sheet` | `start_date`, `end_date`, `accounting_method` |
| Prior allowance true-ups and write-off entries | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Recoveries after a write-off | `search_payments` / `get_payment` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Credits that may explain a balance | `search_credit_memos` / `get_credit_memo` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Invoice dates (statute of limitations) and tax on them | `search_invoices` / `read_invoice` | `start_date`, `end_date` (required), `customer_id`; `id` |
| Customer master | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Sales by customer (concentration, exposure) | `get_customer_sales` | `start_date`, `end_date`, `customer` |
| Tax codes on the original invoice | `search_tax_codes` / `search_tax_rates` | `query`/`name`, `active_only` |
| Industry, year-end, base currency | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and
failure envelopes. Where this table and the live description disagree, the live description wins.

---

## Plain-language glossary

- **Bad debt** — money owed to you that you no longer expect to collect.
- **Write-off** — removing a specific uncollectible balance from the books.
- **Allowance for doubtful accounts** — an estimate set aside for receivables you probably won't
  collect, without naming who.
- **Provision** — the amount added to the allowance in a period.
- **True-up** — adjusting the allowance to the newly required level.
- **Release** — reducing the allowance because less is now expected to be lost.
- **CECL (ASC 326)** — the US rule requiring you to estimate lifetime expected losses up front.
- **IFRS 9 ECL** — the international equivalent. **Staging** classifies receivables by how much
  credit risk has worsened; **12-month** and **lifetime** are the two measurement horizons.
- **Provision matrix** — a table of loss rates by aging bucket.
- **Vintage analysis** — tracking each period's receivables through their whole life to see how
  much was eventually lost.
- **Roll-rate analysis** — measuring how much of each aging bucket moves into the next one.
- **PD × LGD** — probability of default (how likely a customer fails) × loss given default (how
  much you lose when they do).
- **Loss rate** — the proportion of a bucket's balance historically not collected.
- **Statute of limitations** — the legal deadline after which a debt can no longer be enforced.
- **Dividend (in insolvency)** — the portion of a debt creditors eventually receive.
- **Output tax** — sales tax / VAT / GST you charged a customer and remitted to the authorities.
- **Recovery** — money received after a balance was already written off.
- **Direct write-off** — expensing a bad debt immediately, without an allowance.
- **Roll-forward** — opening balance, movements, closing balance.
- **Control account** — the single A/R total in the general ledger.
- **Journal entry (JE)** — the balanced two-sided record. **DR** = debit, **CR** = credit.
