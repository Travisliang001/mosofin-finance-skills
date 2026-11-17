<!-- cohort-and-unit-economics · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **LTV computed on contribution margin, never revenue**
- **Both logo and revenue retention shown**
- **Retention derived from actual cohort curves, not just 1/churn**
- **CAC clearly labeled** (fully-loaded vs. paid; blended vs. by-channel)
- Payback period computed **on a margin basis**
- **LTV/CAC benchmark stated as a guideline, not an invented target**
- **Incomplete (recent) cohorts flagged**
- Segment views where data allows
- **Every metric precisely defined**
- File naming consistent
- **Honest health verdict, including where unit economics are weak**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**,
  with the sample-bias consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- **The acquisition definition and the "active" test are stated explicitly** and carried into the
  definitions sheet
- **The earliest cohort available is stated**, and ages not reached by every cohort are marked on the
  curves
- **Where acquisition channel could not be analysed, that is said plainly** — blended CAC is never
  presented as the complete picture
- **Where one company-wide gross margin was applied to all customers, that is stated**, with its
  effect on finding negative-contribution customers named
- Credits and refunds are netted from cohort revenue
- Both fully-loaded and paid-only CAC are shown where the accounts allow
- In a multi-entity run, **shared customers are matched before any aggregation**, and cross-sell is
  treated as expansion rather than acquisition
- Every metric carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and the periods
  it drew on, in the coverage sheet
- `mock` status is reported wherever it applies, and no health verdict rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No customer names, customer-level revenue or cohort tables are persisted** into a skill bundle;
  every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — the analysis is a deliverable for a human to act on
