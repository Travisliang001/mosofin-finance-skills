<!-- customer-credit-and-collections-policy · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

*The original did not carry a Quality Standards section; these are Mosofin additions, plus the standards
implied by the workflow.*

- **The segmentation is populated with the real customer base**, with counts and values per segment
- **Payment behaviour is measured, not inferred from the current aging**, and **every days-to-pay figure
  states its sample size**
- **Any segmentation dimension that could not be measured is named as unmeasured**, not filled with a
  uniform figure
- **The four automated KPIs carry a stated baseline and the periods used**; the two manual ones are named
  as requiring a system that captures them
- **DSO states its denominator**, and the same denominator is used every period
- **CEI is explained as the collections-performance measure** and DSO as the working-capital one
- **The proposed hold rule was tested against the current base** and the number of affected customers
  stated
- **The reason code catalogue reflects the credits actually issued**, and the credit-memo proxy is
  described as a proxy
- **Every policy step is marked `[auto]`, `[gated]` or `[manual]` in this workspace**, so the SOP
  describes a process that can run
- **Governance and separation of duties are marked designed, not verified**
- Outreach templates are marked **`REVIEW REQUIRED - NOT SENT`**
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- In a multi-entity run, **customers are matched across entities before segmentation**, and whether one
  policy governs all is stated
- `mock` status is reported wherever it applies, and no segment or baseline rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No customer names with segments, payment behaviour, dispute history or KPI values are persisted** into
  a skill bundle; every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — no limit set, no hold placed, no message sent
