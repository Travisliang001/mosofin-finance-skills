<!-- scenario-and-sensitivity-analysis · overview.md · read for: background — what a ledger can and cannot contribute to a scenario analysis; read when a user asks why. Edit here, not in SKILL.md. -->

# Scenario and Sensitivity Analysis — Mosofin Seed

Tests how financial outcomes change as assumptions vary. Builds discrete scenarios, single- and two-variable sensitivity tables, tornado analysis to rank driver impact, and stress tests. Helps decision-makers understand risk and which assumptions matter.

**This skill operates on top of an existing model or plan. It is analysis, not model-building.** That boundary is the original's and it is preserved.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## What a live ledger changes here — and it is one thing, not many

Most of this skill needs no accounting system. Scenario arithmetic, data tables, tornado computation and Monte Carlo iteration are all pure calculation — they were automatable before any connector existed, and the gateway is irrelevant to them.

**The workspace changes exactly one input, and it happens to be the input that determines whether the output means anything: the ranges.**

The original's Inputs table asks for *"Ranges for each driver — plausible low/high, or % swings — **Required**."* In practice these are almost always made up. Somebody picks ±10%, or ±20% for the scary one, and the analysis proceeds on top of a set of numbers nobody can defend.

**A connected ledger knows what each driver has actually done.** Gross margin's observed range across forty-eight months. Revenue growth's realised variability. DSO's actual spread. The month-to-month movement in key input costs. All `[auto: read]`, all specific to this business rather than to businesses in general.

### Why this matters far more than it sounds: the tornado depends on the ranges

This is the technical point that justifies the whole conversion, and the original does not state it.

**A tornado chart ranks drivers by the swing they produce — and the swing is a function of the range you gave each driver.** Flex revenue ±20% and FX ±2%, and revenue will top the tornado. That is not a finding about the business. **It is a restatement of the ranges you chose.**

So a tornado built on mechanical ±10% across every driver is not ranking drivers by risk. It is ranking them by **their coefficient in the model** — by how much the output moves per unit of input — which is a property of the model's structure, not of the world.

**A tornado is only a risk ranking when the ranges reflect how much each driver actually varies.** Revenue that has never moved more than 4% in a year and an input cost that routinely swings 30% should be flexed by 4% and 30%, not by 10% and 10%. Do that, and the ranking changes — often dramatically, and usually in a direction that surprises management.

**That is what the workspace supplies**, and it is the difference between a chart that looks analytical and one that tells you where to look.

### And it directly serves an edge case the original flags

> **Symmetric versus asymmetric ranges**: downside is often larger than upside — costs can spike more than they can fall. **Use asymmetric ranges where appropriate rather than mechanical ±10%.**

Observed history is **naturally asymmetric**, because real business variables are. A driver's realised 5th and 95th percentiles will rarely be equidistant from its median, and using them delivers the edge case's requirement as a by-product rather than as an act of will.

### A near-substitute is not a substitute

**Historical volatility is not future risk**, and this caveat must travel with every grounded range this skill produces.

The observed range is **evidence about** the range. It is not the range. It systematically misses:

- **regime changes** — a business that has just changed its pricing model has no relevant history
- **events that have not happened yet** — a company that has never lost a major customer has no such loss in its data, and the absence is not reassurance
- **thin history** — three years of monthly data is thirty-six observations, and the tails of a thirty-six-point sample are not tails

**So grounded ranges are defensible, not correct.** And there is one place where history must deliberately be abandoned:

**The stress case has to go beyond observed history by design.** A stress test that replays the worst thing that has already happened is not a stress test — it is a memory. Step 3's stress scenario is `[manual]` precisely because its whole purpose is to consider something the data does not contain.

**Two further boundaries**, stated plainly:

- **Mosofin cannot execute the user's model.** If the model is a spreadsheet of formulas, Mosofin does not open it and recalculate it. It supplies grounded ranges, computes scenario arithmetic on a model structure it has been given, and structures the analysis. Where the model must be run, the user runs it.
- **The base case is the client's.** Consistent with `rolling-forecast`: Mosofin does not author a forecast, and the central assumptions of the model are management's.

---

## Related skills

| Skill | Relationship |
|---|---|
| `rolling-forecast` | Where the base case comes from, and the scenario overlay it hands here. |
| `debt-and-covenant-tracking` | Covenant definitions and headroom — and why ledger EBITDA is not covenant EBITDA. |
| `cash-flow-forecast-13-week` | Short-horizon runway, where the threshold analysis becomes operational. |
| `working-capital-optimization` / `dso-and-working-capital-analysis` | The working-capital drivers that dominate cash outcomes and get left out. |
| `kpi-dashboard-builder` | Where the resulting headroom and driver rankings are monitored. |

Other skills this one touches are queued for this library and will be linked here when they ship.
