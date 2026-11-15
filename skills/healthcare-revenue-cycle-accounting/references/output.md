<!-- healthcare-revenue-cycle-accounting · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original has no Output Quality Standards section. Everything below is a Mosofin addition**, drawn
from the original's own workflow and outputs and from the workspace model.

**From the original workflow and outputs:**

- **The revenue cycle flow is mapped**, from charge capture through to collections
- **Net patient service revenue is estimated**, with contractual allowances based on payer contracts and
  historical realization
- **Contractual adjustments, bad debt and charity care are separated** and presented per policy
- **Subledger AR ties to GL AR**, and **cash receipts tie to bank deposits**, with **unapplied cash
  tracked**
- **All three reserves are calculated** — contractual allowance, denials and recoveries, bad debt on an
  expected-credit-loss basis consistent with policy
- **Close controls are performed** — cutoff testing for late charges and late remits, payer mix review,
  trend analysis of adjustments and denials
- The deliverables include the **net revenue model, the AR roll-forward and tie-out, the reserve
  calculations, and the control checklist with a close calendar**

**Mosofin additions:**

- **No patient identifier, balance, date of service, diagnosis or clinical detail appears anywhere in the
  output**, and the workpaper states that it is aggregate-level by design
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The revenue cycle map marks the two stages the ledger cannot see** — claim submission and adjudication
- **Historical realization is computed from the ledger where gross charges are recorded**, presented as a
  series, and **compared against the assumption in use**; where gross charges are not recorded, that limit
  is stated rather than worked around
- **The AR tie-out quantifies the difference** between GL and subledger, even at zero, and lists reconciling
  items
- **Unapplied cash is reported with its ageing**
- **Each reserve is back-tested against prior-period outcomes**
- **Payer AR and patient AR are aged separately**
- **Shifts between contractual, charity care and bad debt across periods are highlighted**
- **Write-off concentrations are reported as patterns, never as allegations**
- **Payer mix change is measured and fed back into the realization estimate**
- In a multi-entity run, **realization is computed per entity and never carried across**, and PC / MSO or
  hospital / physician-group structures are identified so that no entity's margin is read alone
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no reserve or revenue figure rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No PHI of any kind is persisted**, and no realization rate, reserve balance, AR figure or write-off
  amount is stored; every persisted preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — no adjustment, reserve or write-off posted
