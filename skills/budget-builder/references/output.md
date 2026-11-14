<!-- budget-builder · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- Every revenue and major cost line built from documented drivers
- **Headcount plan with timing, comp, and loaded costs (loading rate from the entity, not
  assumed)**
- Monthly granularity with seasonality
- Assumptions register complete and sourced
- Gross and operating margins computed and sanity-checked
- Live formulas so drivers can be adjusted
- Reconciliation to targets and prior year
- File naming consistent
- **No single-rate growth applied where drivers are available; no assumed inflation / tax /
  loading rates**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- **Any budget already held in the system was read before building**, and the new budget states
  whether it extends or replaces it
- **Seasonality is derived from the entity's own monthly history**, with the periods used stated —
  or declared unevidenced
- **The payroll loading rate is derived from the entity's own ledger**, with the derivation and
  period shown
- **Every assumption in the register is marked** as derived from history, supplied by the user, or
  not evidenced
- Every line carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and the
  periods it drew on, in the coverage sheet
- Budget lines use the **real account and department names from the connected books**
- `mock` status is reported wherever it applies, and no committed budget rests on mock data
- Every historical figure traces to a tool result in this conversation; the answer ends with a
  single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term
  kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No salaries, individual compensation, hiring plans or budget figures are persisted** into a
  skill bundle; every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — the workbook is a deliverable, and loading it is a
  human action
