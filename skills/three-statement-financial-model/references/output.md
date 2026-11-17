<!-- three-statement-financial-model · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`)
- **Entity-level or consolidated**, and where eliminations came from
- **Periods of history read, and observations behind each measured driver**
- Forecast horizon and granularity
- **Circularity method**
- **Fixture flag** — any `mock: true`? In bold: **a model on a fixture base is a template.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict, with the computed/read split**
Every step. **A reader should see which parts of this model would be identical with no workspace connected** — which is the question "were these drivers measured?" is asking.

**Section D — What was not done, and why**
- **The forecast** — **a model is an assertion about the future; the ledger records the past**
- **The capex plan**
- **Debt terms, rates and repayment schedules** — **in the loan agreements**
- **Planned equity transactions**
- **The FX assumption**
- **Stock compensation forecasts** — **no cap table on this surface**
- **The lease schedule**
- **Eliminations**, where consolidation is performed outside
- **Inspection of an existing workbook's formulas** — **Mosofin cannot open and audit a spreadsheet; see a financial model review**

**Section E — Unknowns carried forward**
Assumptions departing from history without explanation. Balance check failures unresolved. Circularity untested at the extremes. Facilities assumed but unconfirmed. Seasonality detected but not modelled at the right granularity.

**Section F — Parameters used**
Every driver, with its measured basis and its assumed value. History window. Circularity method. Days convention. Horizon. **A model that cannot be reproduced cannot be diligence-tested**, and this one will be.
