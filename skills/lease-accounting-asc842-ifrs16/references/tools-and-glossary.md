<!-- lease-accounting-asc842-ifrs16 · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 12. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| ROU, liability, amortization, lease and interest expense accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **ROU and liability balances — the tie-out target** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Lease expense by month — the level-expense verification** | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Movements on the ROU, liability and expense accounts | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Recurring payments by vendor — the completeness search, and cash paid** | `search_bills` / `search_payments` / `get_bill` | `start_date`, `end_date` (required); `id` |
| Lessor identification | `search_vendors` / `get_vendor` | `query`/`name`, `active_only`; `id` |
| Legal name, **functional currency**, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no lease register, no contract, no discount rate and no fair value on this surface.**

---

## Plain-language glossary

- **Lease** — the right to control the use of a specific asset for a period, in exchange for payment.
  **Not the same as a service**, where the supplier decides how the asset is used.
- **Lessee / lessor** — the one using it, and the one owning it.
- **ROU (right-of-use) asset** — the asset created by having the right to use something you do not own.
- **Lease liability** — the present value of what you have committed to pay.
- **Lease term** — the non-cancellable period plus any options you are **reasonably certain** to take.
  **The judgment that moves the numbers most.**
- **Reasonably certain** — a high threshold, well above "more likely than not".
- **Discount rate / IBR (incremental borrowing rate)** — the rate used to bring future payments to today's
  value. **What you would pay to borrow the same amount, for the same term, against similar security.**
- **Finance vs. operating lease (ASC 842)** — economically a purchase, or genuinely a rental. **Same balance
  sheet, different expense shape.**
- **The plug** — under ASC 842 operating leases, the ROU amortization is **whatever makes total expense
  level**, not independent depreciation. **The mechanical trap in this skill.**
- **Front-loaded expense** — more cost early, because interest is highest when the liability is largest.
  **What IFRS 16 produces for every lease.**
- **Variable payments** — amounts depending on usage or sales. **Excluded from the liability and expensed as
  incurred.**
- **In-substance fixed** — payments dressed up as variable that are unavoidable in practice. **Included.**
- **Residual value guarantee** — a promise about what the asset will be worth at the end.
- **Practical expedient** — a permitted simplification. **Short-term** — twelve months or less.
  **Low-value** — IFRS 16 only.
- **Reassessment vs. modification** — circumstances changed under the same contract, versus the contract
  itself changed. **Different mechanics.**
- **Maturity analysis** — the undiscounted payments due, year by year.
