<!-- aml-kyc-procedures · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- Risk-based approach applied; effort proportionate to assessed risk
- CDD identifies and verifies the customer and beneficial owners; EDD applied to
  high-risk/PEPs with senior approval
- Sanctions screening treated as mandatory and strict; positive matches escalated
  immediately, never risk-rated away
- Transaction monitoring detects patterns, including structuring
- Suspicious activity routed to the responsible officer; the filing determination left to
  them; the tipping-off prohibition respected
- Recordkeeping and program pillars (policy, officer, training, testing, risk assessment)
  addressed
- No hardcoded thresholds / forms / retention periods — confirmed locally
- MLRO / BSA officer and legal counsel involvement flagged as mandatory
- Documentation objective; risk factors not treated as accusations
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any customer data was
  read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the monitoring-coverage consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task in Steps 1–8 carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool
  used, and that tool's policy, in the coverage sheet
- **Screening is recorded as `[manual]` with its gap named** — never presented as performed,
  and never inferred from any accounting tool
- The transaction-monitoring section states the accounts and date range actually covered, and
  names what fell outside — including unrecorded cash
- `mock` status is reported wherever it applies, and **no risk rating, alert disposition, or
  escalation rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional
  term kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- Persisted preferences hold **procedures and decisions only** — never customer personal
  data, identity documents, beneficial-owner details, or escalation contents
- Every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system; no filing was made, and no determination of
  suspicion was asserted
