<!-- petty-cash-management · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **The reconciliation formula is explicit and visible**
- **Differences are surfaced, not absorbed**
- **Every voucher has a GL account from the user's COA**
- **Replenishment amount equals voucher total to the penny**
- **Receipt and approval gaps clearly flagged**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**; each
  float is identified by location or custodian
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The imprest invariant was tested and its result reported before the reconciliation**, and a fund not run
  as an imprest float is identified as such
- **The GL balance was compared to the authorised float**, and any difference resolved first
- **The physical count is recorded as `[manual]` with its date and the person who performed it**, and its
  absence is reported as a finding rather than worked around
- **No receipt threshold or shortage tolerance was assumed**; absent a stated threshold, **every
  receipt-less voucher is flagged**
- **The replenishment history and frequency are reported**, with an observation on whether the float is
  correctly sized
- **The Cash Over/Short trend is reported per float across periods**, and a persistent same-direction
  shortage is presented **as a pattern with its period count, never as an allegation**
- **A dormant float is identified** and still scheduled for a count
- **IOUs are reported separately from vouchers**, with ageing where the Due from Employee balance is
  readable
- In a multi-entity run, **each float is reconciled separately**, the shortage trend runs per float rather
  than aggregated, and **a float funded across entities is raised as intercompany**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no reconciliation is presented as complete against mock
  data
- Every ledger figure traces to a tool result; the count and vouchers trace to the person who supplied them;
  the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No counts, differences, voucher details, payee names or custodian names are persisted** into a skill
  bundle; every persisted preference states the datasource, `display_name` and float it covers
- Nothing was written back to any system — no replenishment, expense or discrepancy posted
