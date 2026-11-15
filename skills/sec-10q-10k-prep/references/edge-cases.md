<!-- sec-10q-10k-prep · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section.)*

**Filer status changes.** Crossing into large accelerated filer status shortens the deadline and adds requirements; falling out of it does the reverse. **It is re-tested annually against public float, which is not in the books.** `[manual]`, and the commonest way a calendar is built to last year's deadline.

**A first filing after an IPO.** Different content requirements, no comparable prior filing to bridge from, and predecessor financial statements to carry. `[manual]`.

**The 10-K is the annual filing, not a fourth 10-Q.** Q4 has no separate 10-Q; the fourth quarter is subsumed in the annual report. **Use `year-end-close` for the Q4 close**, not `quarter-end-close`, and expect the annual disclosure set rather than the interim one.

**A material subsequent event between the balance sheet date and filing.** Recognised (Type 1) adjusts; non-recognised (Type 2) discloses. **`[manual]` for completeness** — most Type 2 events are not transactions. See `subsequent-events-asc855`.

**An auditor adjustment arrives after the lock.** The exact case Step 4b detects. **Re-perform the affected tie-outs**; do not assume the rest are unaffected, because an adjustment to one line frequently moves a subtotal that several tie-outs depend on.

**A restatement in flight.** The comparatives check has found a material difference and the correction is not yet concluded. **The filing cannot simply carry whichever figure is convenient.** Route to `restatement-and-prior-period-adjustment` and treat the filing timetable as dependent on that conclusion — non-reliance timetables run in parallel with filing ones and can override them.

**Segments that exist in management reporting but not in the chart.** The segment note must be reconcilable to the consolidated total. **Where segments are assembled outside the books, the reconciliation is `[manual]` and will not tie by construction** — which is where segment disclosures most often go wrong. See `segment-reporting`.

**Non-GAAP measure introduced or redefined mid-year.** Requires disclosure of the change and, generally, restated prior-period presentation of the measure. `[auto]` to detect the definitional drift; `[manual]` to handle.

**A component ledger tie-out mistaken for a consolidated one.** See Gate 1. **This is the failure this skill is most likely to produce**, because a component tie-out agrees perfectly and looks exactly like success.

**XBRL tagging diverging from the document.** The tagged data and the human-readable statements must agree. `[manual]` — neither is on this surface. See `xbrl-tagging-checklist`.

**The close is not finished when the calendar says Day 0.** `[auto]` to detect. A filing calendar counting from an unfinished close is already behind, and the slippage compounds through every downstream milestone.
