<!-- fraud-detection-and-forensics · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Engagement type and boundaries clear; objectivity and escalation emphasized up front**
- **Fraud risk assessed by scheme type against controls**
- **Analytical tests applied appropriately, with anomalies prioritized** — **indicators, not conclusions**
- **Benford's and statistical screens used within their valid limits**
- **Investigation framework preserves evidence and follows the money objectively**
- **Loss quantification (if any) uses defensible, documented methods**
- **Control failures identified with remediation**
- **Individuals never accused; findings are factual and evidence-based**
- **Qualified forensic professionals and legal counsel flagged as required for real investigations**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- **The engagement type was settled before any query ran**, and an existing allegation triggered escalation
  rather than analysis
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**, with
  the note that **an unexamined entity is not a clean entity**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Every test that could not run is listed in Sheet 9**, with what it would have shown and how to obtain
  it — **bank-account matching, payroll tests and corruption indicators named explicitly**
- **Every analytical result states its population and sample size**, and Benford's results are reported only
  for populations within the test's valid limits
- **Every flagged item is presented as a question**, with the evidence still needed — never as a conclusion
  about a person
- **The false-positive expectation is stated** alongside any wide screen
- **No loss figure is presented for an unsubstantiated indicator**
- **No inference is drawn about any individual's pressure, motive or circumstances**
- **The report states that Mosofin reads are analysis, not preserved evidence**, and names the point where a
  fund trace leaves the ledger
- **The authorized recipients were confirmed before the output was produced**
- The approver for gated data access was agreed in advance where an allegation exists
- In a multi-entity run, **cross-entity patterns were tested** — shared vendors, shared individuals,
  cross-entity duplicates, intercompany disposal routes — and every result is labelled with its entity
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no anomaly is reported from mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No findings, flagged items, anomalies, suspicions or personal identifying details are persisted** into
  a skill bundle or a preference file — **the method is stored; the results never are**
- Nothing was written back to any system — no record altered, and nothing done that could tip anyone off
