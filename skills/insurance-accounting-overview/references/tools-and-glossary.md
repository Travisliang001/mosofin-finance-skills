<!-- insurance-accounting-overview · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 8. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **The account signature — reserves vs. commissions vs. trust** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **UPR, reserves, recoverables, DAC, trust balances** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Commission and fee income, or premium and losses** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `class` |
| **Reserve, recoverable and trust account movements** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Premium receivable and insurer payable ageing** | `get_aged_receivables` / `get_aged_payables` | `as_of_date`, `aging_period`, `num_periods` |
| Commission billings and insurer settlements | `search_invoices` / `search_bills` | `start_date`, `end_date` (required) |
| Receipts, including unallocated client money | `search_deposits` / `search_payments` | `start_date`, `end_date` (required) |
| Legal name, currency, **country** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no policy system, no claims system, no treaty, no actuarial valuation and no credit rating on
this surface.**

---

## Plain-language glossary

- **Carrier / insurer** — the party actually taking the risk. **Broker** — arranges cover for the client.
  **MGA (managing general agent)** — acts for the insurer under delegated authority, and may bind cover.
- **Premium** — what the policyholder pays. **GWP (gross written premium)** — all premium written in the
  period, before anything is ceded or earned.
- **Written vs. earned** — written when the policy is sold; **earned as the cover period passes.**
- **UPR (unearned premium reserve)** — the part of premium covering time that has not happened yet. **A
  liability.**
- **Case reserve** — the estimated cost of a specific known claim.
- **IBNR (incurred but not reported)** — claims that have already happened **that nobody has told the
  insurer about yet.** **Actuarial by definition.**
- **LAE (loss adjustment expenses)** — the cost of investigating and settling claims.
- **Loss development triangle** — how claims from one period have grown as they settled, used to project
  the rest. **Needs claims data by accident year.**
- **Reinsurance** — insurance for insurers. **Ceded** premium is what is passed on. **Recoverable** is what
  the reinsurer owes you.
- **Treaty** — the reinsurance contract setting what is ceded and on what terms.
- **DAC (deferred acquisition costs)** — commission and selling costs spread over the policy period, to
  match the premium being earned.
- **Clawback** — commission repaid when a policy is cancelled early.
- **Client money / fiduciary funds** — premium held on behalf of clients and insurers. **Not the firm's
  money**, usually held in a segregated trust account under regulatory rules.
- **Shortfall** — trust money held is less than what is owed. **A regulatory breach.**
- **Unallocated receipt** — money in, not yet matched to a policy or client. **The usual cause of a
  shortfall.**
