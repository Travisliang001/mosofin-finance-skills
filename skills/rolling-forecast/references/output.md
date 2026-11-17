<!-- rolling-forecast · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- Horizon, granularity, refresh cadence
- **Months locked as actual, and whether each was verified closed**
- Years of history available, and how many support the seasonality derivation
- Date and time of the reads
- **Fixture flag** — any `mock: true`? In bold: **seasonality, bias and the challenge tests all need real history, and generated data has none.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Steps 2, 5, 6 and 7's actuals line were automatic and Steps 3, 4 and 8 were not.**

**Section D — What was not done, and why**
- **The projection itself** — **a forecast is an assertion about the future; the ledger records the past**
- **Pipeline and bookings** — **CRM data, not ledger data**
- **The headcount plan** — HR
- **Known future events** — contracts, launches, price changes
- **The FX assumption** — a forecast rate, never supplied here
- **The budget**, where it lives in a spreadsheet rather than the book
- **Any external guidance.** Management guides; Mosofin does not

**Section E — Unknowns carried forward**
Months not locked because the close was incomplete. Implied accelerations not yet explained. Seasonality assumptions unsupported by history. Bridge residual not fully attributed. Drivers where realised and assumed diverge without comment.

**Section F — Parameters used**
Horizon. Lines forecast. Seasonality basis and years used. Accuracy horizons tracked. Budget source. FX assumption. Volatility window for scenario widths. **Comparability across refreshes is the entire point of a rolling forecast**, and it depends on these staying stable — or on changes being recorded when they are not.
