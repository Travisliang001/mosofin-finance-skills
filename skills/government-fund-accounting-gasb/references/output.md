<!-- government-fund-accounting-gasb · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Funds categorized correctly** — governmental / proprietary / fiduciary
- **Right measurement basis applied per fund type**
- **Modified accrual mechanics** — available period, no capital / long-term in governmental funds —
  **correctly applied**
- **Fund balance classified into the constraint-based categories**
- **Government-wide statements presented on full accrual with capital and long-term items**
- **Reconciliations between fund and government-wide perspectives complete and clear**
- **Pensions and OPEB sourced from actuarial reports, not fabricated**
- **Nonexchange revenue recognized per the specific GASB rules**
- **Budgetary comparison provided where required**
- **Major fund determinations made**
- **Current standards confirmed for the framework**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**; the
  **primary government and any component units are distinguished**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Whether a fund dimension exists is stated**, and where none does, fund-level reporting is reported as
  not producible rather than approximated
- **Which basis the books are kept on is stated on the face of every statement**, and every statement is
  marked as book-basis or conversion
- **Each fund dimension was tested for self-balancing**, and any that fails is identified as a cost tag
  rather than a fund
- **The accounting method used on every read is recorded**, and both periods use the same one
- **Interfund transfers were read and proved to net to zero**, with unmatched items listed
- **The major fund determination was computed this period**, with the working shown, and not carried forward
- **The fund-to-government-wide reconciliation quantifies and sources every item**, with no unexplained
  residual
- **Every fund balance classification names the constraint document** supporting it
- **Proprietary cash flows use the four GASB categories**, rebuilt rather than relabelled
- **Fiduciary funds are excluded from the government-wide statements**
- Pension and OPEB figures are **`[manual]` from an actuary**, with the report date, and never estimated
- Capital asset and debt detail is **marked `[auto]` from the books or `[manual]` from an outside register**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no publicly filed statement rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No fund balances, net position, pension liabilities or statement figures are persisted** into a skill
  bundle, and **no individual beneficiary is ever identified**; every persisted preference states the
  datasource and `display_name` it covers
- Nothing was written back to any system — no entry, transfer, closing or reclassification posted
