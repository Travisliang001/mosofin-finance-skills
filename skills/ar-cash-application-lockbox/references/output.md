<!-- ar-cash-application-lockbox · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

*The original did not carry a Quality Standards section; these are Mosofin additions, plus the
standards implied by the workflow.*

- **Every match records the hierarchy level (1–6) that produced it**, so its confidence is
  visible
- **No fuzzy match is auto-accepted**; each is presented with its reason and confidence
- Every short-pay is checked against outstanding credit memos before being called a deduction
- Every overpay is checked for a duplicate payment before a credit is proposed
- Every deduction carries a reason code from the user's own code set, and its position relative
  to the write-off threshold
- **Unapplied cash is aged**, not just totalled
- **The tie-out states which side was evidenced** — book-to-book, or genuinely to the bank
- Receipts are recorded gross with fees shown separately, never netted
- Proposed entries use the real account names from the connected books
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task in Steps 1–5 carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool
  used, and that tool's policy, in the coverage sheet
- **Evidence Mosofin cannot see — lockbox files, bank statements, remittance advices, bank
  trace identifiers — is recorded as a gap, never as a check that passed**
- The research queue is presented as an output, not suppressed to make the match rate look
  better
- `mock` status is reported wherever it applies, and no application or write-off rests on mock
  data
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term
  kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- No bank account numbers, trace identifiers, or receipt-level data are persisted into a skill
  bundle; every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — every match, credit, write-off and reclassification
  is a proposal for a human to post
