<!-- business-valuation · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Purpose, standard of value, premise, level of value, and valuation date defined**
- Multiple approaches applied where appropriate; rationale for the chosen approaches and weighting
- DCF: defensible forecast, **WACC built from current inputs with sources**, TV with both methods
  reconciled, discounting correct
- Comps: peer set justified, multiples computed and statistics shown, range applied with rationale
- Precedent transactions: deal multiples sourced, **control-premium nature acknowledged**
- **EV → equity bridge with itemized debt and cash treatment**
- Control premium / DLOM / minority discount applied appropriately (**not stacked carelessly**) and
  supported
- Sensitivities shown for key drivers
- **No hardcoded market inputs — current-sourced**
- Specialist involvement required and flagged for high-stakes / regulated uses
- **Ranges, not false precision, presented as conclusions**
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- **Every company figure was read as at the valuation date**, not as at today
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- **Every market input carries an external source and a date**, or is listed as outstanding. **None
  is supplied from memory**
- **The net debt bridge is itemised**, with debt-like items and restricted cash identified by
  account
- The **historical FCFF series** is shown alongside the forecast as a reality check
- EBITDA states whether it is reported or normalised, and names the adjustments if normalised
- Diluted share counts state their source and are never taken from the equity accounts
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source
  used, and the as-of date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no valuation conclusion rests on mock data**
- Every subject-company figure traces to a tool result in this conversation; the answer ends with a
  single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No market data values, concluded values, forecasts or cap table detail are persisted** into a
  skill bundle; every persisted preference states the datasource and `display_name` it covers
- The report carries a limiting condition naming which figures came from the connected accounting
  records, as at what date, and stating that no market data was drawn from them
