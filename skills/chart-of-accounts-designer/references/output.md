<!-- chart-of-accounts-designer · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Every account has Type, Sub-type, Description, and Reporting Tag**
- Account numbers consistent within each section
- **No duplicates, no overlapping descriptions**
- **Industry-specific accounts only if the industry is confirmed**
- **Tax accounts only if the jurisdiction is confirmed**
- **Migration map is complete (every old account has an action)**
- File formatted to the target system's import template (or generic if the system is unknown)
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- **Every account is marked as existing (read from the connected system) or proposed**
- **Every Retire and Merge recommendation carries its evidence** — transaction count, last activity
  date and balance — and **the lookback window is stated**
- **Accounts are classified on usage, never on balance**; inactive accounts are included in the read
- **A dormant account holding a balance is investigated, not retired**
- Accounts whose names encode a dimension are surfaced as consolidation candidates
- Where the target system differs from the connected one, **approximate type mappings are labelled as
  approximate**
- In a harmonisation run, **no group retire list is built from one entity's activity**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that tool's
  policy, in the coverage sheet
- `mock` status is reported wherever it applies, and no retire recommendation rests on mock usage
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence;
  the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- No balances or transaction values are persisted into a skill bundle; every persisted preference
  states the datasource and `display_name` it covers
- Nothing was written back to any system — no account was created, renamed, merged or deactivated

---

## Design Principles

1. **Fewer accounts, more dimensions.** Reach for class / department / location / project before
   adding a new account.
2. **One account per concept.** If "Software" and "Subscriptions" overlap in practice, use one.
3. **Numbering supports reporting.** Group accounts so a P&L in account-number order reads logically.
4. **Don't design for hypothetical future complexity.** Add accounts when the need arises.
5. **Match the system's native taxonomy.** Each platform has constraints — design with them, not
   against them.
6. **Document the intent.** A COA without descriptions decays quickly.

**A seventh, Mosofin-specific:**

7. **Design against measured usage, not remembered usage.** What people believe an account is for and
   what actually posts to it diverge quickly. Read the ledger before redesigning the chart — the
   evidence is one call away, and it changes the answer more often than not.
