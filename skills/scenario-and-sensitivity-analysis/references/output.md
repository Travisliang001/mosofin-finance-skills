<!-- scenario-and-sensitivity-analysis · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- **Periods of history read, and the number of observations per driver**
- Output metric(s) targeted
- **Range basis**: measured / supplied / mixed
- **Whether Mosofin had the model's structure or only its outputs**
- **Fixture flag** — any `mock: true`? In bold: **generated ledgers are smooth; measured volatility from fixture data is near zero and every range derived from it is fictitious.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict, with the computed/read split**
Every step marked `[auto: computed]`, `[auto: read]`, `[gated]` or `[manual]`. **A reader should see which parts of this workbook would have been identical with no workspace connected** — which is the question "were these ranges measured?" is really asking.

**Section D — What was not done, and why**
- **The model itself** — **a spreadsheet; Mosofin cannot execute it**
- **The base case** — management's
- **Scenario definitions** — coherent stories are authored
- **The stress shock** — **deliberately beyond the data**
- **Probabilities and distributions** — beliefs about the future
- **Covenant definitions** — **from the credit agreement**
- **The recommendation of what to do** — strategy, appetite and options are not in a ledger
- **Any forward-looking statement**

**Section E — Unknowns carried forward**
Drivers with too few observations to range credibly. Correlations observed over short histories. Thresholds whose definitions are outstanding. Model behaviour untested at the extremes of the range.

**Section F — Parameters used**
Drivers, ranges and their bases. History window. Percentile convention. Grid steps. Iteration count and distributions. Metric targeted. **A sensitivity analysis that cannot be reproduced is not evidence**, and this one will be re-run next quarter against a longer history.
