<!-- equity-compensation-accounting · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Awards correctly classified equity- vs. cash-settled** (drives remeasurement)
- **Grant-date fair value used for equity-settled** (no improper remeasurement)
- **Vesting conditions classified** (service / performance / market) **and treated correctly — market
  conditions in fair value, expense stands**
- **Attribution method applied consistently** (graded vs. straight-line)
- **Forfeitures handled per the entity's policy with true-ups**
- **Period expense allocated to functional lines**
- **Exercises, settlements, and modifications accounted for** (incremental fair value on modifications)
- **Award roll-forward and disclosure figures complete**
- **Feeds equity, tax, and cash-flow skills**
- **Complex valuations / modifications flagged for a specialist**
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**;
  **the issuing entity is identified**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The recorded expense was reconciled to the schedule**, and any difference reported
- **Cumulative expense was reconciled to the APIC movement**, and **exercise proceeds to cash received**
- **No award population figure is derived from the equity accounts** — the cap table is named as the source
- **Every grant-date fair value carries its source and valuation date**, and grants priced off a stale
  valuation are flagged
- The settlement classification is cross-checked against whether the accounts carry a liability or an
  equity credit
- The attribution method and forfeiture policy applied are stated, and consistency with the prior period
  confirmed
- In a multi-entity run, **the expense sits with the employer and the equity credit with the issuer**, any
  recharge arrangement is stated, and the group total reconciles to the plan's total
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no expense, disclosure or add-back rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No individual grants, recipient names, share counts, strike prices, fair values or cap table data are
  persisted** into a skill bundle; every persisted preference states the datasource and `display_name` it
  covers
- Nothing was written back to any system — no award granted, vested, exercised or settled
