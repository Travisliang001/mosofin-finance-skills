<!-- derivatives-and-hedging-asc815 · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

*The original did not carry a Quality Standards section; these are Mosofin additions, plus the standards
implied by the workflow.*

- **Every hedge relationship has a documented designation with a date**, and that date is checked against
  when the instrument first appeared in the accounts
- **No hedge accounting is applied to a period before documentation existed**
- **Every valuation names its source, its date and its methodology**; **none is taken from the recorded
  carrying value**
- **The entry proposed is the movement** from the recorded carrying value to the new valuation, not the
  valuation itself
- **Effective and ineffective portions are split**, with the ineffective portion going to earnings
- **The OCI reclassification check was run**, and any amount stranded after the hedged item occurred is
  reported
- **The settlement completeness sweep was run**, and its result stated including when nil
- **Whether hedge accounting is applied at all is established before the work begins**
- Embedded derivatives are addressed explicitly, with the statement that only contract review can find them
- Effectiveness testing states the method and the period assessed; a failure produces a dedesignation entry
  in the exception log
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- In a multi-entity run, **the instrument and the hedged item are confirmed to sit in the same entity**,
  and internal derivatives are excluded as hedging instruments for group reporting
- Account names in every proposed JE are the **real names from the connected chart of accounts**
- `mock` status is reported wherever it applies, and no designation or disclosure rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No valuations, mark-to-market positions, notionals with counterparty names or effectiveness results
  are persisted** into a skill bundle; every persisted preference states the datasource and `display_name`
  it covers
- Nothing was written back to any system — no trade executed, no hedge designated, no entry posted
