<!-- contingencies-and-litigation-asc450 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 6. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Accrual, legal, warranty and recovery accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Existing accruals, movement, settlements paid** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Accrued contingency balance carried | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Legal spend by firm, by month — the completeness signal** | `get_vendor_expenses` | `start_date`, `end_date`, `vendor`, `summarize_column_by` |
| **Identify counsel; spot a newly added firm** | `search_vendors` / `get-vendor` | `query`/`name`, `active_only`; `id` |
| Individual legal invoices and descriptions | `search_bills` / `get-bill` | `start_date`, `end_date` (required), `vendor_id`; `id` |
| Settlement payments made directly | `search_purchases` / `get_purchase` | `start_date`, `end_date` (required); `id` |
| **Insurance recoveries received** | `search_deposits` / `get_deposit` | `start_date`, `end_date` (required); `id` |
| Prior accrual and release entries | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Legal and professional fee trend | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Legal name and currency | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no tool that assesses legal probability, and none will be substituted for one.**

---

## Plain-language glossary

- **Contingency** — a possible obligation that depends on something not yet settled.
- **Loss contingency** — one that would cost you money. **Gain contingency** — one that would earn you
  money; generally **not** recognised until realised.
- **Probable / reasonably possible / remote** — the three likelihood tiers under US GAAP, in decreasing
  order.
- **Reasonably estimable** — you can put a number, or at least a range, on it.
- **Accrue** — record it in the accounts. **Disclose** — describe it in the notes without recording an
  amount.
- **Range of loss** — a low and high figure where no single amount is more likely than another.
- **Best estimate** — the single most likely amount, where one exists.
- **Provision** — the IFRS term for an accrued contingency.
- **Legal letter** — outside counsel's written response about pending matters, used as audit evidence.
- **Privilege** — the legal protection that keeps advice between a client and its lawyers confidential.
- **Netting** — offsetting an expected recovery against the loss. Generally not permitted unless the
  recovery is assured.
- **Realizable** — the recovery is certain enough to be recorded.
- **Warranty contingency** — the expected cost of honouring product guarantees.
- **Assessment** — a demand from a tax or regulatory authority.
- **Completeness** — the assertion that *all* matters are captured, not just the ones on the list. The
  hardest one to prove here.
