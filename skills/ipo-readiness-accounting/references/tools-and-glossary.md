<!-- ipo-readiness-accounting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Historical statements — the comparable-data check** | `get_profit_and_loss` / `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| **The close-timing and manual-entry population** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| **Movement by posting date versus transaction date** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **The chart across years; suspense and uncategorized accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Year-end positions | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Legal name, year-end, industry** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no cap table, no valuation, no contract, no control documentation and no audit opinion on this
surface.**

---

## Plain-language glossary

- **IPO** — selling shares to the public for the first time, which brings a regulator, a filing calendar and
  personal accountability for the numbers.
- **S-1** — the US registration document filed before an IPO. **Contains audited financial statements for
  multiple years.**
- **10-Q / 10-K** — the quarterly and annual reports a public company files thereafter, **to deadlines
  measured in days.**
- **Close** — the process of finishing a period's accounts. **A private company's takes as long as it takes;
  a public company's cannot.**
- **Close calendar / RACI** — who does what, by when, and who reviews it.
- **ICFR (internal control over financial reporting)** — the controls that make the numbers reliable.
  **SOX** — the law requiring them to be documented, tested and attested.
- **PCAOB** — the body setting audit standards for public companies. **A PCAOB audit is a higher bar than a
  private-company audit**, and prior years often have to be re-audited to it.
- **Segregation of duties** — no one person controlling a process end to end.
- **Cap table** — the record of who owns what, including options and convertibles. **Everything about EPS
  depends on it.**
- **409A valuation** — a US private-company share valuation used to price options. **Its history has to
  stand up.**
- **Diluted EPS** — earnings per share assuming options and convertibles are exercised.
- **Complex equity instruments** — preferred stock, convertible notes, warrants, down-round provisions.
  **They routinely delay IPO timetables.**
- **Accounting policy memo** — a written analysis of how the entity accounts for something and why.
  **Auditors expect them; private companies rarely have them.**
- **Tie-out** — proving figures agree across statements and to supporting records.
- **Certification** — named officers personally attesting the accounts. **A legal obligation, not a
  formality.**
- **Material non-public information** — information that would move the share price and is not public.
  **An IPO plan is exactly this.**
