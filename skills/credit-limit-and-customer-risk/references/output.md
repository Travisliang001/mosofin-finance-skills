<!-- credit-limit-and-customer-risk · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Every recommendation has a documented rationale**
- **Tier assignment is supported by both quantitative and qualitative factors**
- **Recommended limit method is stated**
- **Monitoring triggers are specific and actionable**
- **Concentration analysis explicit**
- **No reliance on any single metric or score in isolation**
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**,
  with the understated-exposure consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **No metric about the customer's own financial position is presented unless their financials were
  supplied** — nothing is computed from your books and labelled as theirs
- **The payment-experience analysis is presented alongside the financial analysis**, not beneath it, and
  **every days-to-pay figure states its sample size**
- **The tier states which evidence supported it** — the customer's financials, your payment experience, or
  both
- **The proposed limit is cross-checked against current and peak historic exposure**
- **Terms actually applied are compared against terms on record**
- **Whether the customer is also a vendor was tested**, and any netting states whether a right of set-off
  exists
- **Write-off history was checked across every connected entity**
- The automated monitoring triggers were run across the customer base, not only the customer under review
- In a multi-entity run, **exposure and concentration are aggregated at group level** and the limit is set
  at group level before allocation
- Every input carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used,
  and its sample size, in the coverage sheet
- `mock` status is reported wherever it applies, and **no adverse assessment of a named business rests on
  mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No credit assessments, tier assignments, bureau data, customer financials or exposure amounts are
  persisted** into a skill bundle; every persisted preference states the datasource and `display_name` it
  covers
- Nothing was written back to any system — no limit was set, no hold placed, no terms changed
