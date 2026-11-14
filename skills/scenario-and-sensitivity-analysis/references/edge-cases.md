<!-- scenario-and-sensitivity-analysis · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All nine preserved, in order.

**Drivers that aren't independent**: **do not flex correlated drivers independently as if uncorrelated — model the relationship or use coherent scenarios.** **`[auto: read]`** — Step 2c measures the correlations, which turns this from an instruction into a check.

**Non-linear model responses**: some outputs respond non-linearly — **a covenant breach is a cliff, not a slope. Sensitivity tables should sample finely enough to catch the inflection.** `[auto: computed]`, and worth doing deliberately: **solve for the inflection point (Step 7) and place a grid step either side of it**, rather than hoping a uniform grid lands near it.

**Circularity in the underlying model**: scenario runs can amplify circularity — interest on cash. **Ensure the model's circularity handling is stable across the scenario range.** `[manual]` — it is a property of the model. **A model that converges at base and oscillates at the downside extreme will produce a downside number that is an artifact.**

**Unrealistic combinations**: **a naive worst case combining every adverse assumption at its extreme may be implausibly severe. Calibrate to a coherent, plausible scenario, not the arithmetic worst.** `[manual]`, with `[auto: read]` support — the correlations and the jointly-observed region show which combinations the business has actually experienced. **And note this cuts both ways**: an arithmetic worst case is easy to dismiss, and a dismissed downside is worse than a modest one taken seriously.

**Symmetric versus asymmetric ranges**: **downside is often larger than upside — use asymmetric ranges where appropriate rather than mechanical ±10%.** **`[auto: read]`** — observed percentiles are asymmetric by nature. This edge case is delivered as a by-product of Step 2b.

**Output metric choice matters**: **sensitivity of net income, cash runway and valuation can rank drivers differently. Be clear which metric the analysis targets.** `[manual]` to choose, `[auto: computed]` to demonstrate — **and demonstrating it is worth doing**: running the tornado against two metrics and showing the rankings differ is often the most useful single exhibit, because it stops a P&L-derived priority being applied to a cash problem.

**Monte Carlo without real distributions**: **the output looks rigorous but is only as good as the inputs — document assumptions and their basis.** `[manual]`, with `[auto: read]` empirical fitting and **the observation-count caveat travelling with it.**

**Stress test for covenant or lender purposes**: **align the stress scenario with what the lender or regulator expects — sometimes prescribed shocks.** `[manual]`. A prescribed shock overrides both judgment and history; use the prescription.

**Time dimension**: **a driver shock might be temporary — one bad year — or permanent. Model the duration, not just the magnitude.** `[manual]` for the duration; `[auto: read]` for evidence — **how long past adverse movements in this driver actually persisted.** A cost spike that historically reverted within two quarters is a different risk from one that never came back, and the history says which happened last time.
