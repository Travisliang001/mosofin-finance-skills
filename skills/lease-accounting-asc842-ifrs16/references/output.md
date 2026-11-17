<!-- lease-accounting-asc842-ifrs16 · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Lease vs. service confirmed; lessee / lessor perspective set**
- **Term and payments determined with documented option judgments**
- **Discount rate sourced (implicit or IBR), not fabricated**
- **ASC 842 classification performed; IFRS 16 single model applied** — no improper classification
- **ROU asset and liability measured correctly at inception**
- **Liability schedule on effective-interest; ROU amortization correct per type** — operating-lease plug
  handled
- **Periodic entries match the framework and classification**
- **Modifications / reassessments remeasured correctly**
- **Practical expedients applied consistently**
- **Disclosure data (maturity, weighted averages, expense, cash) produced**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The completeness search was run and reported before measurement** — rent expense without an ROU asset,
  recurring payment candidates by vendor, and the short-term population
- **Candidates are reported as candidates**, with the vendor, pattern and value, never as concluded leases
- **The schedule ties to the ledger at both ends** — closing balances to the balance sheet, period interest
  and amortization to the P&L — with each difference reported including zero
- **For ASC 842 operating leases, total expense was verified to be level**, and any front-loading is
  reported as a plug-mechanic error
- **Every discount rate carries its source and date**, and none was fabricated; borrowing-cost context is
  labelled as context rather than as the IBR
- **Framework contradictions are raised before measurement** — classification asserted under IFRS 16, for
  instance
- **Mid-term payment changes are surfaced** as possible escalations, reassessments or unremeasured
  modifications
- **Cash paid for leases is taken from the ledger**, not estimated from the schedule
- **A multi-year short-term population is questioned** rather than accepted
- In a multi-entity run, **the completeness search runs per entity**, the IBR is entity-specific,
  intra-group leases are identified for elimination, and **foreign-currency leases retranslate the liability
  but not the ROU asset**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no liability feeding a covenant rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No lease terms, payment amounts, rates, balances or schedules are persisted** into a skill bundle, and
  **no commercially sensitive contract terms are stored**; every persisted preference states the datasource
  and `display_name` it covers
- Nothing was written back to any system — no lease recognised, schedule posted or remeasurement recorded
