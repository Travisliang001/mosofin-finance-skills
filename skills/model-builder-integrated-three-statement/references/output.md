<!-- model-builder-integrated-three-statement · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Quality Bar

**The original's Quality Bar, kept as stated, plus the Mosofin additions.**

**The model is not complete until:**

- **Historical statements tie to source**
- **Forecast assumptions are visible and editable**
- **No required forecast line is a static pasted value without explanation**
- **The balance sheet balances across all periods**
- **Cash flow ending cash links to balance sheet cash**
- **The model clearly separates inputs, calculations, outputs, and checks**

**Mosofin additions:**

- The workspace was confirmed **by name**, and **the entity or group the model represents was settled before
  any historical was pulled**
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**, and
  **an incomplete group is stated before building**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **All five Step 2 validations were run before any forecast layer was built**, and **where any failed, a
  source issue list was produced and the build paused**
- **Mapping completeness was tested explicitly** — mapped total against trial balance total — and any
  unmapped account named
- **Historicals were pulled at the model's own cadence**, not derived from a coarser period
- **The opening balance sheet is the last closed period**, and it is stated
- **Every driver's historical value is presented beside its assumption field**, across at least three
  periods
- **No assumption was generated**; every forward input is the user's, and the build notes say so
- **Forecast lines with no historical anchor are labelled as unanchored**
- **Checks run across historical and forecast periods in the same row**, so breaks are attributable
- **The control panel records the workspace, the entity and the source as-at date**, and **the source tab
  records the tool calls**, so the model is refreshable and auditable
- **Formulas are preserved**, and the model recalculates on assumption change
- In a consolidated build, **intercompany is eliminated before the historicals enter**, group drivers are
  computed from group figures, an FX assumption exists for forecast periods, and non-controlling interests
  are carried through equity
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no model intended for a decision rests on mock data**
- Every historical figure traces to a tool result; every forecast figure traces to a schedule, a historical
  row or a named assumption; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No historical figures, driver values, assumptions, forecasts or model contents are persisted** into a
  skill bundle; every persisted preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — the model is a file, and the books are unchanged
