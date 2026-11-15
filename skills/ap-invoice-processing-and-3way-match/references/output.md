<!-- ap-invoice-processing-and-3way-match · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

*The original did not carry a Quality Standards section; these are Mosofin additions, plus
the standards implied by the workflow.*

- Every invoice examined shows its match verdict (matched / within tolerance / exception) and
  the tolerance applied
- **The match is labelled 2-way or 3-way according to the evidence actually available**, never
  aspirationally
- Every inferred PO-to-bill match is recorded as inferred
- Every exception carries its type, its owner, and what evidence would close it
- Duplicate testing covers near-duplicates and split vendor records, not just exact matches
- Tax checks state the code and rate applied, and whether recoverability was confirmed
- KPIs state the population and date range they were computed over
- Proposed postings use the real account and dimension names from the connected books
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task in Steps 1–7 carries its verdict, the tool used, and that tool's policy, in the
  coverage sheet
- **Controls Mosofin cannot perform — approvals, bank-detail change control, tax forms on
  file, physical receipts — are recorded as gaps with named owners, never as checks that
  passed**
- `mock` status is reported wherever it applies, and no invoice is cleared for payment on mock
  data
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional
  term kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- No vendor bank details, tax identification numbers, or invoice images are persisted
- Every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — every posting, approval and resolution is a
  proposal for a human
