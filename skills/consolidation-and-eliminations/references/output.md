<!-- consolidation-and-eliminations · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Consolidation scope determined per control criteria**
- **Currency translation method correct** (current-rate vs. temporal) with CTA / remeasurement routed
  correctly
- **Every elimination entry balances and is documented**
- **Intercompany balances and P&L fully eliminated**
- **Unrealized intercompany profit eliminated**
- **NCI calculated and rolled forward**
- Equity-method investments carried as single lines
- **Consolidated statements balance and tie across**
- File naming consistent
- **No unmatched intercompany amount eliminated (reconcile first)**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- **Every group member is named by `display_name` with its role and ownership percentage**; every
  connected file **out of scope** is named as excluded; **every group member with no connected file is
  named as a gap**
- The capability map was discovered **this run** via Gate 2, **per entity** — never recalled from a
  previous conversation or from this file
- **Every trial balance was pulled at the same date and on the same accounting method**, and both are
  stated on the workpaper
- **Every entity result was labelled with its entity on receipt**, and each entity's legal name
  cross-checked against the trial balance attributed to it
- **Every intercompany mismatch is quantified and investigated before elimination**, and unresolved
  differences are reported rather than eliminated
- **Every FX rate carries its source and date**; none is supplied from memory
- Account mappings across differing charts are **shown, not applied silently**
- Intercompany cash movements are eliminated from the consolidated cash flow statement
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that tool's
  policy, in the coverage sheet, **per entity**
- **Which entities' figures were read and which were supplied is stated**, so the assurance level is
  visible
- `mock` status is reported **per entity**, and consolidated statements resting on mock data are not
  presented as reportable
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line grouped by datasource and entity
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No FX rates, balances or consolidated statements are persisted** into a skill bundle; every
  persisted preference states the datasource, `display_name` and role it covers
- Nothing was written back to any system — every elimination is a proposal and the statements are a
  deliverable
