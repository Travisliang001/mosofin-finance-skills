<!-- notes-to-financial-statements · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Disclosure checklist tailored to the entity's framework and activities**
- **Accounting policy notes reflect the entity's actual policies, not assumed**
- **Account-detail notes tie to the primary statements**
- **Roll-forwards and maturity tables complete**
- **Commitments and contingencies flagged for legal review where needed**
- **Related party and subsequent events covered**
- **Comparatives consistent or restated with disclosure**
- **Open items requiring management / legal input clearly flagged**
- **File naming consistent**
- **No invented policy, contingency outcome, or legal opinion**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**, and
  **an incomplete group is stated before drafting**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The checklist was scoped from the chart**, and **notes ruled out are listed with their evidence** rather
  than silently omitted
- **Every note carries a verdict** in the checklist, so a note drafted from management input is
  distinguishable from one built on a tie-out
- **Every note total is tied to the statement face**, with the difference reported including zero, and
  **each figure records the tool call behind it**
- **Comparatives were checked against the filed prior year**, not only against the ledger
- **Stated accounting policies were tested against what the data shows**, and any divergence flagged
- **No policy was asserted from an inferred pattern** — inferences are put as questions
- **The subsequent events candidate population was produced from post-period activity**, with materiality
  and Type 1 / Type 2 classification left to management, **and events leaving no ledger trace asked about
  explicitly**
- **Related parties were tested by name matching, not built from it**, and matches are reported as matters
  to investigate
- **Concentration disclosures are computed** rather than asserted
- **No contingency outcome was characterised and no unestimated loss was estimated**; the only `[auto]`
  contribution is whether a provision was recorded
- **The issuance date is stated**, since it bounds the subsequent events window
- In a multi-entity run, **notes are consolidated with intercompany eliminated**, and **whether these notes
  accompany consolidated or statutory statements is confirmed**, because it changes the related party note
  entirely
- Every note carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no published note rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No figures, roll-forwards, drafted note text, contingency descriptions or related party transaction
  detail are persisted** into a skill bundle; every persisted preference states the datasource and
  `display_name` it covers
- Nothing was written back to any system
