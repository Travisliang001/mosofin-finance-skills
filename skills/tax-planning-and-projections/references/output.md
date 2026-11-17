<!-- tax-planning-and-projections · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`), and **who the taxpayer is**
- Jurisdiction and taxpayer type
- **Basis of the projection** — book or tax-adjusted
- **Every rate, bracket and threshold used, with its source and the date confirmed**
- Period, and the proportion of the year that is actual rather than projected
- **Fixture flag** — any `mock: true`? In bold: **the affordability test passes by construction on generated data.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that every parameter was supplied and only the base was read.**

**Section D — What was not done, and why**
- **Every rate, bracket, threshold, allowance and relief** — **current-sourced, never from this file**
- **The book-to-tax adjustments**, where not yet determined
- **The forward half of the income projection**
- **Personal circumstances** — filing status, other income, residency, allowances already used
- **The combined corporate-plus-personal analysis** for extraction decisions
- **Safe-harbour rules, due dates and filing frequencies**
- **Penalty computations** — flagged as risk, never quantified on unconfirmed rules
- **Any assessment of a transaction's substance** — **not visible in a ledger**
- **The decision, and the advice.** **A qualified professional signs off before anybody acts**
- **Filing and payment.** The gateway is read-only

**Section E — Unknowns carried forward**
Parameters unconfirmed. Adjustments outstanding. Missed instalments unresolved. Set-aside shortfall unaddressed. Reliefs identified but not claimed. Options modelled but not advised on.

**Section F — Parameters used**
Every rate and threshold with source and date. Basis. Periods. Seasonality assumption. Sensitivity ranges and their derivation. **Next quarter's re-run must be comparable**, and every parameter must be re-confirmed rather than reused.
