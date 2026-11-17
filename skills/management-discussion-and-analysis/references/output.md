<!-- management-discussion-and-analysis · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Every figure ties to the financial statements**
- **Period-over-period changes explained by drivers, not just restated**
- **Margins and key ratios discussed with their movements**
- **Liquidity section is specific and forward-looking**
- **Critical estimates describe judgment and sensitivity, not just method**
- **Non-GAAP measures reconciled, GAAP given prominence**
- **Forward-looking statements flagged for safe-harbor and legal review**
- **Balanced tone** — favorable and unfavorable both covered
- **File naming consistent**
- **No promotional language, no ungrounded claims, no independent guidance**

**Mosofin additions:**

- **The draft is marked DRAFT FOR MANAGEMENT REVIEW**, and the narrative is presented as management's, not
  as analysis produced here
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**, and
  **an incomplete group is stated before drafting**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Every cited figure records the tool, the parameters, the entity and the as-at date** in the tie-out
  sheet, so the grounding is reproducible
- **Every driver is classified as computed or management-asserted**, and none is invented
- **The revenue movement is decomposed into price, volume and mix** where line detail allows, with the
  method stated; where it does not, that limit is stated rather than the driver asserted
- **Every "one-time" characterisation and every non-GAAP adjustment was tested for recurrence**, with the
  count reported
- **The comparative was checked against the filed prior year**, and any difference reported before drafting
- **Critical estimates were scoped and sized from the balance sheet**, with sensitivity marked `[manual]`
- **Cash is not presented as liquidity** without addressing restricted, trapped and committed amounts
- **Every forward-looking statement traces to a management statement**, appears in the Sheet 4 log with its
  source, and is marked in the draft itself; **no guidance is generated**
- **Seasonality, customer concentration and currency effects are measured rather than asserted** where the
  data allows
- In a multi-entity run, **the narrative is grounded in consolidated figures with intercompany eliminated**,
  cash is reported by entity where availability differs, and constant-currency analysis separates FX from
  performance
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no published figure rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No figures, narrative text, drafts, drivers or forward-looking statements are persisted** into a skill
  bundle — **the structure and method are stored; every word is redrafted**; every persisted preference
  states the datasource and `display_name` it covers
- Nothing was written back to any system
