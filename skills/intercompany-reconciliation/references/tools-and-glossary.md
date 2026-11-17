<!-- intercompany-reconciliation · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Legal name and functional currency, per entity** | `get_company_info` | none (uses the connected company) |
| **The intercompany accounts in each entity** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The IC ledger at transaction level, with references** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **IC balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The documents behind the entries, with their numbers** | `search_invoices` / `search_bills` / `get_invoice` / `get_bill` | `start_date`, `end_date` (required); `id` |
| **Journal entries posted direct to IC accounts** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| **How each entity names the other group members** | `search_customers` / `search_vendors` | `query`/`name`, `active_only` |
| IC balance ageing | `get_aged_receivables` / `get_aged_payables` | `as_of_date`, `aging_period`, `num_periods` |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no FX rate service, no intercompany agreement and no inventory holding report on this surface.**

---

## Plain-language glossary

- **Intercompany (IC)** — between companies in the same group. **From the group's point of view these
  transactions never happened** — which is why they are eliminated on consolidation.
- **Entity pair** — two group companies that trade with each other. **Reconciliation happens pair by pair.**
- **Mirror / equal-and-opposite** — one side's receivable is the other's payable, same amount.
- **Matching** — pairing a line in one ledger with the line in the other that represents the same
  transaction.
- **Reference matching** — using an invoice or document number. **The most reliable basis**, because it
  survives timing and rate differences.
- **1:N and N:N matching** — one entry on one side against several on the other, or several against several.
- **Cut-off timing** — one side posted this period and the other next. **Not an error; it resolves itself.**
- **True mismatch** — a difference that will not resolve on its own. **The only kind that needs fixing.**
- **Settlement** — actually paying the net balance between two entities.
- **Netting** — offsetting what each owes the other to a single payment.
- **Elimination entry** — a consolidation-only entry removing intercompany amounts. **It never touches
  either entity's own books.**
- **Unrealized intercompany profit** — mark-up on goods sold within the group that the buyer still holds.
  **Not real profit until sold outside the group.**
- **Withholding tax (WHT)** — tax the payer deducts and remits on the recipient's behalf. **A frequent
  cause of mismatch**, because the payer records the net and the recipient should record the gross.
- **Transfer pricing** — the price charged between group companies, and the rules governing it.
- **True-up** — a year-end adjustment bringing intercompany pricing to a target margin.
- **CTA (cumulative translation adjustment)** — where genuine FX differences land at consolidation.
