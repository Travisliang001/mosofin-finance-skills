<!-- rolling-forecast · overview.md · read for: background — why a rolling forecast fits a live connection, and related skills; read when a user asks why. Edit here, not in SKILL.md. -->

# Rolling Forecast — Mosofin Seed

Builds and maintains a rolling forecast: a continuously updated projection that always looks a fixed horizon ahead — twelve or eighteen months — blending actuals-to-date with forward projections. Unlike a static budget, it is refreshed each period as new actuals arrive.

This skill is **driver-based** and **industry-aware**. It is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## Why this skill fits a live connection better than any other forecasting skill

A forecast is an assertion about the future. A ledger is a record of the past. That would normally make forecasting a poor fit for a read-only connection, and for most of the forecasting skills in this pack it does.

**A rolling forecast is different, because of what makes it rolling.**

Its defining mechanic — Step 2, *lock actuals to date* — is **exactly a live read.** The whole apparatus exists to consume closed-period results as they arrive, and its refresh cadence is "monthly, after the close." That is a description of a workspace connection.

So the division here is unusually favourable:

- **The "rolling" is automatic.** Locking actuals, re-anchoring the full-year view, computing what changed, deriving seasonality, scoring the last forecast against outturn — all `[auto]`.
- **The "forecast" is not.** Pipeline, hiring plans, pricing decisions, known future events, the judgment that bookings will recover — all `[manual]`, and none of it is in an accounting system.

And there is a third contribution the original could not have: **the workspace can challenge the forecast with the client's own numbers.** That is Step 3b, and it is what makes the last quality standard enforceable rather than aspirational.

### A near-substitute is not a substitute

**A run-rate is not a forecast.** Annualising year-to-date is arithmetic. It ignores seasonality, the pipeline, known events, price changes and everything else a forecast exists to incorporate. **It is, however, an excellent thing to test a forecast against** — so this skill computes run-rates and presents them as a *challenge*, never as a projection.

**A closed month is not necessarily a final month.** Step 2 locks actuals for closed periods. If the close is not actually complete — accruals not raised, recurring entries not run, a subledger not reconciled — then the "actuals" being locked will still move. **Locking unfinished actuals corrupts the forecast and, worse, permanently corrupts the accuracy tracker**, because the outturn it scores against was never real. `[auto]` to check before locking; see Step 2.

**Actuals-to-date are not the forecast either.** The full-year view is actuals plus projection, and the two must remain visibly distinguishable at every point — which is the first quality standard, and the reason Sheet 1 shades one of them.

---

## Related skills

| Skill | Relationship |
|---|---|
| `budget-vs-actual-analysis` | Variance against plan; the comparison in Step 5. |
| `cash-flow-forecast-13-week` | Short-term cash, explicitly out of scope. |
| `month-end-close-checklist` | Must be complete before a month is locked as actual. |
| `journal-entry-review` / `recurring-transaction-builder` | The close-completeness checks behind Step 2b. |
| `fixed-asset-register-and-depreciation` | The already-determined depreciation that the forecast inherits. |
| `kpi-dashboard-builder` | Where the forecast's key metrics are presented. |

Skills for the annual budget, scenario analysis, three-statement modelling, MD&A, quarter-end close, FX revaluation and consolidation are queued for this library and will be linked here when they ship.
