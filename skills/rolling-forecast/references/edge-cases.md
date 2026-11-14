<!-- rolling-forecast · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All ten preserved, in order.

**First rolling forecast (no prior to bridge from)**: **start from the budget as the baseline; future refreshes will bridge from this one.** `[manual]`. And say plainly what is not yet available: **no bridge, and no accuracy tracker.** This is the run that starts the history rather than benefiting from it — which is a reason to persist properly, not a reason to skip the sheets.

**Mid-year strategy change**: a pivot, a new product, a major customer change **requires rebuilding driver models, not just tweaking. Document the step-change.** `[manual]`. **And exempt it explicitly from Test A** — a genuine step-change legitimately implies an acceleration, and the challenge test must not be allowed to argue against a real event. That is what the "question for management" column is for.

**Actuals reveal the budget was wrong**: **the rolling forecast should reflect reality, not defend the budget. If revenue is structurally below plan, forecast the lower trajectory — and the budget-versus-forecast gap is the story to tell management.** `[manual]` to conclude; **`[auto]` to make it unavoidable** via Test A. This is the edge case the hockey-stick test exists to serve.

**Highly volatile or early-stage business**: **wide forecast ranges; refresh more frequently; emphasise scenarios over a single point forecast.** `[auto]` for the observed volatility that should set the width of those ranges — and note that an early-stage business has little history, so the seasonality derivation will be thin and must say so.

**Seasonality at the horizon boundary**: **when the rolling window spans into a new seasonal cycle, ensure the added months carry the right seasonal pattern.** `[auto]` — Test B checks exactly this, and the far-end month is where a flat number slips in unnoticed.

**Lumpy revenue (project or deal-based)**: **forecast specific deals and projects with probability weighting rather than smooth trends. Update as deals close or slip.** `[manual]` for the deals and probabilities — pipeline is CRM data. **`[auto]` for one useful history: how often deals in this book have actually landed in the month first expected**, where prior forecasts are persisted. That is a slip rate, computed from the client's own record rather than assumed.

**Headcount-driven cost base**: **the single biggest forecast lever for many companies. Keep the hiring plan current — delayed hires materially change the cost forecast.** `[auto]` for the current payroll run-rate and for the actual joiner timing versus the plan, where the plan was persisted; `[manual]` for the plan. **Hires slip more often than they accelerate**, and a plan-versus-actual timing record is the honest input to next quarter's assumption.

**FX volatility**: **hold a forecast FX assumption; show sensitivity. Update the assumption as rates move materially.** `[manual]` for the rate — **never supplied here and never carried forward**, consistent with `recurring-transaction-builder`. `[auto]` for the sensitivity arithmetic and for the realised average rate in the actuals.

**Capex and its P&L and cash effects**: capex changes flow to depreciation and cash. The full integrated view is a three-statement model. `[auto]` for the depreciation consequence of existing assets, which is already determined; `[manual]` for planned capex. See `fixed-asset-register-and-depreciation`.

**Forecast used for external guidance**: **extra rigour; flag forward-looking elements; coordinate with whoever owns public disclosure for any guidance.** `[manual]`, and the rule is absolute: **Mosofin never authors a forward-looking statement.** It supplies the actuals, the patterns and the challenge. Management guides.
