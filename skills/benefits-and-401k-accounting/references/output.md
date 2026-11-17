<!-- benefits-and-401k-accounting · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- Benefits correctly categorized (DC / DB / short-term / compensated absences)
- DC contributions / match expensed as earned; **employee contributions kept as withholdings**
- PTO accrued where it vests / carries over, at current rates, with a maintained roll-forward
- Short-term benefits expensed, with IBNR accruals where self-insured
- **DB / OPEB structured per the correct framework and populated only from actuarial input (never
  fabricated)**
- Vesting and forfeitures handled
- Liabilities reconciled and contributions tied to payroll
- Disclosure figures provided
- Actuarial-dependent items clearly flagged
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that
  tool's policy, in the coverage sheet
- **The unremitted-contribution check was performed and its age reported** against the confirmed
  deadline
- **The employee-withholding-in-employer-expense test was performed** and its result stated
- Every `[manual]` item names what the user must supply and who owns it; **actuarial items name
  the actuary**
- Account names in every proposed JE are the **real names from the connected chart of accounts**
- `mock` status is reported wherever it applies, and no accrual, disclosure figure or compliance
  assertion rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence;
  the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term
  kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No employee names, individual PTO balances, pay rates or contribution amounts are persisted**
  into a skill bundle; every persisted preference states the datasource and `display_name` it
  covers
- Nothing was written back to any system — every entry is a proposal for a human to post
