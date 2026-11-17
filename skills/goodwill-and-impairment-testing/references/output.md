<!-- goodwill-and-impairment-testing · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Scope and framework determined; unit of account (reporting units / CGUs) identified**
- **Triggering events assessed; qualitative shortcut (US GAAP) used appropriately**
- **Quantitative test mechanics match framework** — goodwill: carrying vs. FV with cap (US GAAP) / carrying
  vs. recoverable (IFRS); long-lived: two-step (US GAAP) / one-step (IFRS)
- **Fair value / recoverable amount uses defensible projections, discount rate, and assumptions**, with
  sensitivity shown
- **Impairment computed and allocated correctly within CGU / group**
- **Reversal handled per framework** — IFRS non-goodwill only
- **Disclosure data including key assumptions and sensitivity prepared**
- **Valuation specialist flagged where material**
- **File naming consistent**
- **No fabricated cash flows, discount rates, or fair values**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The test was scoped from the balance sheet**, and tests that do not apply are documented as not
  applying, with the evidence
- **Carrying amounts are `[auto]` with their as-at date**; **every valuation input is `[manual]` with its
  source and date**, and the two sides of the comparison are as at the same date
- **No impairment is concluded from ledger data alone** — a declining segment is reported as an indicator
- **The two quantitative triggering events are measured and trended**, with magnitude and duration, and the
  remaining six are recorded with owners
- **The unit of account states how it was identified**, and a segment dimension used as a proxy is
  identified as a proposal pending the definitional test
- **The goodwill allocation basis is stated and consistent with the prior period**
- **The projection is compared to actual historical results**, and any divergence is stated as an
  observation
- **The discount rate basis (pre-tax / post-tax) is stated and matched to the cash flow basis**
- **The IFRS allocation floor is applied and shown**, and the US GAAP undiscounted / discounted distinction
  is preserved
- In a multi-entity run, **goodwill carried in one file against a business in another is stated explicitly**,
  and impairment is recorded where the goodwill sits
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no impairment conclusion rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No fair values, recoverable amounts, projections, rates, carrying amounts or impairment conclusions are
  persisted** into a skill bundle; every persisted preference states the datasource and `display_name` it
  covers
- Nothing was written back to any system — no impairment, reversal or write-down recorded
