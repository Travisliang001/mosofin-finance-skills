<!-- scenario-and-sensitivity-analysis · method.md · read for: Stages 3–6 — the scenarios and sensitivities themselves. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Clarify the question
- Step 2 — Identify and isolate the drivers
- Step 2b — Ground the ranges in observed history *(Mosofin addition)*
- Step 3 — Discrete scenarios (best / base / worst)
- Step 4 — Single-variable sensitivity
- Step 5 — Tornado analysis
- Step 6 — Two-variable data tables
- Step 7 — Threshold / breakeven analysis
- Step 8 — Probability-weighted / expected value
- Step 9 — Monte Carlo (optional)
- Step 10 — Synthesize the insight
- Step 11 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

This skill uses the same refinement as `recurring-transaction-builder`, because it applies for the same reason — a large block of the work needs no ledger at all:

- **`[auto: computed]`** — pure calculation from the model and the ranges. Works with no datasource connected.
- **`[auto: read]`** — requires a live read of the workspace. This is where the ranges come from.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is analysis.** The gateway is read-only. Mosofin posts nothing, and it does not decide what the future holds.

---

## Inputs

All seven preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Underlying model or plan** | A three-statement model, a budget, or similar | **Required** | **Not in the books. A spreadsheet.** Mosofin cannot execute it. | `[manual]` |
| **Output metric(s) of interest** | Net income, EBITDA, FCF, cash runway, valuation, covenant ratio | **Required** | Not in the books as a choice; **current values are readable** | `[manual]` to choose, `[auto: read]` for the level |
| **Key drivers / assumptions to vary** | Revenue growth, margin, churn, price, costs, FX | **Required** | `[manual]` to choose; **realised values readable** | `[manual]` + `[auto: read]` |
| **Ranges for each driver** | Plausible low/high, or % swings | **Required** | **This is the contribution — see Step 2b** | **`[auto: read]` to propose, `[manual]` to accept** |
| Scenario definitions, if discrete | Assumption sets per named scenario | Recommended | **Not in the books.** A coherent story is authored. | `[manual]` |
| Probability weights | Likelihood of scenarios / distributions | Optional | Not in the books | `[manual]` |
| Constraints / thresholds | Covenant levels, minimum cash, breakeven | Recommended | **Covenant definitions from the agreement; current position is a live read** | `[manual]` + `[auto: read]` |

---

## Workflow

### Step 1 — Clarify the question

`[manual]`. All five mappings preserved — **different techniques answer different questions:**

| Question | Technique | Verdict |
|---|---|---|
| **"How bad could it get?"** | Downside scenario / stress test | `[manual]` to author |
| **"Which assumption matters most?"** | Tornado / sensitivity ranking | `[auto: computed]` — **but only meaningful with grounded ranges** |
| **"What's the range of likely outcomes?"** | Scenarios with probabilities, or Monte Carlo | `[auto: computed]`, `[manual]` for distributions |
| **"At what point do we breach X?"** | Breakeven / threshold analysis | `[auto: computed]`, with `[auto: read]` starting position |
| **"What if these two things both move?"** | Two-variable data table | `[auto: computed]` |

> **Pick the technique(s) to match the question.**

Preserved, and it is the first quality standard. **The commonest failure in this skill is producing all seven sheets when the decision needed one** — a board that asked "are we going to breach the covenant" does not need a Monte Carlo, it needs Step 7 and a headroom figure.

---

### Step 2 — Identify and isolate the drivers

`[manual]` to select. All five categories preserved.

> **The model should already have assumptions isolated**.

| Category | Drivers | Realised value readable? |
|---|---|---|
| **Revenue** | Growth rate, volume, price, churn, new customers | **Yes** — growth and price directly; churn and new customers from customer-level invoice history |
| **Costs** | COGS %, key input prices, headcount, wage inflation | **Yes** — COGS % directly; input prices where units are on purchase lines; payroll cost directly |
| **Working capital** | DSO, DPO, DIO | **Yes** — all three computable per period |
| **Capital** | Capex, financing terms | **Capex yes; financing terms are in the agreements** |
| **External** | FX rates, interest rates, tax rate | **Realised effective rates yes; forward rates no** |

> **Confirm each driver is a clean input that flows through the model — changing it shouldn't break links.**

`[manual]`, and it belongs to the model, not the ledger.

**Working capital deserves a note**, because it is the category most often left out of scenario work and it is fully measurable: DSO, DPO and DIO each have an observed history, they each move, and in a cash-constrained business **their variability frequently dominates the cash outcome** even though revenue dominates the P&L outcome. A tornado run on a cash metric with working capital drivers omitted is missing the drivers that matter. See `working-capital-optimization` and `dso-and-working-capital-analysis`.

---

### Step 2b — Ground the ranges in observed history *(Mosofin addition)*

**`[auto: read]`. The core contribution of this conversion.**

For each selected driver, compute from the longest available history:

| Measure | Purpose |
|---|---|
| **Realised value per period** | The series itself — plotted, so the user can see it rather than take a summary on trust |
| **Median, and 5th / 95th percentiles** | A defensible low/high, **naturally asymmetric** |
| **Full observed minimum and maximum** | The realised extremes, which matter for the stress conversation |
| **Standard deviation, and coefficient of variation** | Comparable volatility across drivers measured in different units — **this is what makes a tornado's ranges commensurable** |
| **Number of observations** | **Always reported.** Thirty-six monthly points is thin, and twelve is not a distribution. |
| **Trend** | Whether the driver has drifted, which means the historical mean is not the current central value |

**Then propose ranges** — and propose them as a **starting point for the user to accept, adjust or reject**, never as the answer:

> *"Gross margin has ranged from 31.2% to 44.8% over 52 months, with a median of 38.1%; the 5th–95th percentile band is 33.4%–42.0%. Proposed range: −4.7pp / +3.9pp against a base of 38.1%. Note the downside is wider than the upside, and margin has drifted down about 2pp over the last eight quarters."*

That paragraph is worth more than a ±10% assumption, and every figure in it is a fact.

#### Step 2c — Measure the correlations *(Mosofin addition)*

**`[auto: read]`, and it serves the original's first edge case directly.**

> **Drivers that aren't independent**: if revenue growth and margin are correlated — scale economies, say — **don't flex them independently as if uncorrelated.** Model the relationship or use coherent scenarios.

**Correlation is measurable.** Compute the pairwise correlation between the selected drivers across the available history and report the material ones with their strength and their observation count.

**Two ways to use it, and both are legitimate:**

- **In scenarios**: correlated drivers move together, which is exactly what makes a scenario a coherent story rather than an arbitrary combination. If margin has historically fallen when growth slowed, the downside case should reflect that — and now there is evidence for it rather than an assertion.
- **In sensitivities and tornado**: single-variable sensitivity **deliberately** holds other drivers at base, which is the technique's purpose — isolating individual impact. But where drivers are strongly correlated, **the isolated sensitivity understates the real-world effect**, because in reality the other driver moves too. Flag it; do not silently combine.

**The caveat, and it is the standard one:** correlation over a short history is unstable, and correlation is not causation. Report the observation count. A strong correlation over eighteen months is a hypothesis.

---

### Step 3 — Discrete scenarios (best / base / worst)

`[manual]` to author. `[auto: computed]` to run. All four preserved.

> **Define coherent assumption sets — not just one variable moved, but a consistent story.**

| Scenario | Definition | Verdict |
|---|---|---|
| **Base case** | The expected plan — the model's central assumptions | `[manual]` — **the client's, per `rolling-forecast`** |
| **Upside case** | A plausible favourable combination: faster growth + better margins + favourable FX. **Internally consistent — do not combine impossibilities.** | `[manual]`, informed by observed correlations |
| **Downside case** | A plausible adverse combination: slower growth + margin compression + higher costs. **Often the most decision-relevant.** | `[manual]`, informed by observed correlations |
| **Stress / break case** | A severe but possible shock — recession, loss of a major customer, financing failure | **`[manual]`, and deliberately beyond observed history** — see below |

> **For each scenario, run the full model and capture the output metrics. Keep the scenarios internally consistent — a recession scenario shouldn't have rising prices and rising volumes.**

**Step 2c's correlations are how internal consistency stops being a matter of taste.** "Margin falls when growth slows" is either true of this business or it is not, and the history says which.

#### The stress case must leave the data behind

**Deliberately `[manual]`, and this is where the near-substitute warning becomes operational.**

Every other range in this skill is grounded in what has happened. **A stress case is about what has not.** If the entity has never lost its largest customer, that loss appears nowhere in the volatility measurement — and it remains entirely possible.

So:

- **`[auto: read]` supplies the ingredients**: what is the largest customer worth? What proportion of revenue is the top five? What is the fixed cost base that does not flex when volume falls? **Concentration is measurable and it is the raw material of most stress scenarios.**
- **`[manual]` supplies the shock.** How severe, how sudden, how long.

**A stress test built only from historical variability is not a stress test.** State that on the sheet, so nobody reads the grounded ranges as covering the tail.

---

### Step 4 — Single-variable sensitivity

`[auto: computed]`, with `[auto: read]` ranges.

Vary one driver at a time across its range, holding others at base:

```
Revenue growth:   -10%   -5%   Base   +5%   +10%
EBITDA:           $X     $Y    $Z     $A    $B
```

**Repeat for each key driver. This isolates each driver's individual impact.**

**With grounded ranges the increments are the driver's own**, not a uniform grid — a driver whose observed band is −4.7pp/+3.9pp is stepped across that band, not across ±10%. Label the steps with what they represent (percentile, or standard deviations) so a reader can see that the columns are not arbitrary.

**And per the edge case on non-linearity**: sample finely enough to catch inflections. A covenant breach is a cliff, and a five-point grid will step straight over it.

---

### Step 5 — Tornado analysis

`[auto: computed]` — **and read the section at the top of this file before presenting one.**

For each driver, compute the output's swing from low to high, holding others at base. **Sort by the magnitude of the impact.** The widest bars at the top are the drivers that matter most.

```
Driver               Output at Low    Output at High    Swing
Revenue growth       $X               $Y                |Y-X|   <- widest
Gross margin         ...              ...               ...
Churn rate           ...              ...               ...
FX rate              ...              ...               ...     <- narrowest
```

> **This tells management where to focus attention and risk management — the top drivers are where forecast error hurts most.**

**That sentence is only true when the ranges are real.** With mechanical ranges, the tornado tells management which drivers the model is most *arithmetically* sensitive to — which is a fact about the spreadsheet.

**Two Mosofin requirements for any tornado this skill produces:**

- **Every bar's range is labelled with its source and basis** — observed percentile band, observed min/max, or user-supplied — **on the chart's data sheet.** A tornado without its ranges attached is not interpretable.
- **Where ranges are mixed** — some measured, some supplied — **say so.** A tornado comparing a measured 4.7pp margin band against a supplied ±20% revenue assumption is comparing two different kinds of thing, and the ranking it produces is not a risk ranking.

---

### Step 6 — Two-variable data tables

`[auto: computed]`.

When two drivers interact, build a grid:

```
                        Revenue growth
              -10%    -5%    Base    +5%    +10%
Gross   -3pp   ...    ...    ...     ...    ...
margin  -1pp   ...    ...    ...     ...    ...
        Base   ...    ...    [base]  ...    ...
        +1pp   ...    ...    ...     ...    ...
        +3pp   ...    ...    ...     ...    ...
```

Each cell is the output metric at that combination. **Useful for showing trade-offs — revenue against margin, for instance.**

`[auto: read]` addition: **shade the cells that fall outside the jointly observed region.** Where the correlation from Step 2c says two drivers have never both been at their adverse extremes simultaneously, the bottom-left corner of the grid is a combination that has not happened. It is not impossible — and it should be visibly distinguished from the cells the business has actually lived in.

---

### Step 7 — Threshold / breakeven analysis

**`[auto: computed]` for the solve; `[auto: read]` for the starting position — which makes this the most immediately useful step for most clients.**

Solve for the driver value at which a constraint is hit. All four preserved:

| Question | Live inputs | Verdict |
|---|---|---|
| **At what revenue does the entity break even?** | Current fixed cost base and contribution margin, both readable | `[auto: read]` + `[auto: computed]` |
| **At what point does cash hit the minimum threshold / runway expire?** | **Current cash and actual burn rate — both live reads** | `[auto: read]` + `[auto: computed]` |
| **At what EBITDA does a covenant breach?** | Current EBITDA readable; **the covenant definition is in the agreement** | `[auto: read]` + `[manual]` |
| **What price or volume is needed to hit the target?** | Current price and volume readable where units are on invoice lines | `[auto: read]` + `[auto: computed]` |

> **Present the "headroom" — how far the base case is from each threshold.**

**Runway deserves emphasis**, because it is the single most decision-relevant number in many businesses and **both of its inputs are live reads.** Current cash is a balance. Actual burn is the trailing operating cash movement. Neither requires the model at all, and the answer — *"at the trailing six-month burn rate, cash reaches the minimum in month nine"* — is available in one query, before any scenario work begins.

**Covenant headroom** carries the standing caution from `debt-and-covenant-tracking`: **ledger EBITDA is not covenant EBITDA.** The agreement defines the term, with its add-backs and exclusions. Compute headroom on the agreement's definition or say which definition was used.

---

### Step 8 — Probability-weighted / expected value

`[auto: computed]`; `[manual]` for the probabilities.

```
Expected outcome = Sum of (scenario probability x scenario outcome)
```

> **Also show the distribution — not just the mean. The range and the downside tail matter for risk decisions.**

Preserved and important. **An expected value can be a number that no scenario produces** and that nobody plans around. A 60/30/10 weighting across three scenarios yields a mean the business will almost certainly not experience. Show the scenarios beside it.

**Probabilities are `[manual]`.** They are beliefs about the future, and there is nothing in a ledger that supplies one.

---

### Step 9 — Monte Carlo (optional)

`[auto: computed]` to run; **`[manual]` for the distributions**, with a genuine `[auto: read]` contribution.

If the user wants a full distribution:

- **Assign probability distributions to key uncertain drivers** — normal, triangular, uniform, and so on — **based on the user's view**
- **Run many iterations** sampling from them
- **Produce the output distribution**: mean, median, percentiles (P10/P50/P90), and the **probability of breaching thresholds**

> **This requires the user to specify distributions, not just point ranges. Build with a clear simulation engine; document the distributions and the iteration count.**

**And the edge case, which is the discipline that matters:**

> **Monte Carlo without real distributions**: **do not run Monte Carlo with made-up distributions presented as precise.** The output looks rigorous but is only as good as the input distributions — document assumptions and their basis.

`[auto: read]` genuinely helps here: **a distribution fitted to observed history is not made up.** The realised series gives an empirical shape — its spread, its skew, whether it looks anything like normal — and that is a far better basis than a triangular distribution chosen because it was easy.

**But it does not remove the caveat, and this must be said in the same breath.** Fitting to thirty-six observations gives a decent read on the middle of a distribution and **almost nothing about its tails** — and a Monte Carlo's whole selling point is the tails. Report the observation count next to every fitted distribution, and **use empirical resampling of the actual history in preference to a fitted parametric shape** where the history is short: it makes fewer claims.

**If the client wants P99 from thirty-six data points, the honest answer is that the data does not support it.**

---

### Step 10 — Synthesize the insight

**`[manual]`. The most important step, and the least automatable.**

> **The analysis isn't the numbers — it's the conclusion:**
> - **Which drivers dominate the outcome** (from tornado)
> - **How much downside risk exists** (from worst case / P10)
> - **How close the plan is to breaking** (from thresholds)
> - **What management should monitor and hedge**
>
> **Write a concise summary of the key findings.**

Preserved in full, and the fourth bullet is where a tool must stop. **Mosofin can say which driver has the widest bar and how much headroom remains. It cannot say what management should do about it** — that is a decision involving the business's strategy, appetite and options, none of which are in a ledger.

Present the findings and the figures. Recommend where the evidence genuinely points — that revenue error hurts more than FX error, say, which is a fact about the tornado. Stop before the strategy.

**And never author a forward-looking statement.**

---

### Step 11 — Output

An `.xlsx` analysis workbook. All seven of the original's sheets, plus two additions.

**Sheet 1: Summary of Findings**
Key insights, ranked drivers, downside risk, threshold headroom. `[manual]` for the synthesis. **Header carries the range basis** — measured, supplied, or mixed — and the fixture flag.

**Sheet 2: Scenarios**
Best / base / worst / stress with **full assumption sets** and output metrics side by side. **Each assumption labelled with its basis**, and the stress case marked as deliberately beyond observed history.

**Sheet 3: Single-Variable Sensitivities**
One table per key driver, **stepped across that driver's own band** with the steps labelled.

**Sheet 4: Tornado Analysis**
Driver impact ranking and chart data. **Every bar's range shown with its source.** Mixed-basis ranges flagged.

**Sheet 5: Two-Variable Data Tables**
For the key interacting pairs, **with jointly-unobserved cells shaded.**

**Sheet 6: Threshold / Breakeven**
Breakeven points and headroom. **Runway computed from live cash and actual burn**, stated separately from any model-derived figure.

**Sheet 7: Probability-Weighted / Monte Carlo** (if applicable)
Distribution outputs, **with distributions, their basis and the observation count documented**, and the iteration count.

**Sheet 8: Driver History and Ranges** *(Mosofin addition)*
The evidence behind every range:

| Driver | Periods observed | Min | P5 | Median | P95 | Max | Std dev | CoV | Trend | Proposed range | Range used | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Plus the correlation matrix from Step 2c with observation counts.

**This sheet is what makes the rest of the workbook defensible.** Without it a tornado is a chart; with it, it is an argument.

**Sheet 9: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

> **Link to the underlying model so scenarios recompute when the base model changes.**

Preserved — **and note the boundary: Mosofin cannot execute the model.** Where the workbook links to a live model, the recomputation happens in the user's spreadsheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Scenario_Sensitivity_[EntityName]_[YYYY-MM-DD].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name, on Sheet 1, and **on Sheet 8 beside every measured range.**

---

## Output Quality Standards

All ten preserved.

- **Technique matched to the decision question.** `[manual]` — **and not all seven sheets when one was needed.**
- **Scenarios internally consistent — coherent stories, not arbitrary combinations.** `[manual]`, **evidenced by measured correlations.**
- **Single-variable sensitivities isolate each driver.** `[auto: computed]`, **with the correlation caveat flagged where drivers move together.**
- **Tornado ranks drivers by impact.** `[auto: computed]` — **and every range is labelled with its basis, because the ranking is a function of the ranges.**
- **Thresholds and breakevens solved, headroom shown.** `[auto: computed]`, with `[auto: read]` starting position.
- **Probability-weighting or Monte Carlo documents distributions and assumptions.** `[manual]`, **with observation counts.**
- **Synthesis identifies which drivers matter and how much risk exists.** `[manual]`
- **Linked to the underlying model.** `[manual]` — **Mosofin cannot execute it.**
- **File naming consistent.** `[auto: computed]`
- **No false precision; no implausible combined-extreme scenarios presented as the base downside.** **`[manual]`, and the standard that governs the rest.**

**Four Mosofin additions:**

- **Every range carries its basis** — measured with its observation count, or supplied.
- **The stress case is marked as deliberately beyond observed history.** Grounded ranges do not cover the tail.
- **Runway is computed from live cash and actual burn**, independently of the model.
- **Historical volatility is never presented as future risk.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and any range.** A range measured last year is last year's volatility, and the whole argument for measuring is that it reflects *this* business *now*.

**What is worth persisting into the workspace-scoped skill:**

1. **The driver definitions** — which ledger accounts and dimensions constitute each driver in this book. Expensive to establish, stable, and the basis of every future measurement.
2. **The history window and percentile convention**, so successive analyses are comparable.
3. **Ranges the user accepted, adjusted or rejected, and why.** A client who has explained twice that their FX exposure is hedged should not be shown an FX range a third time.
4. **The correlation structure observed**, refreshed as history lengthens.
5. **Covenant definitions and thresholds**, shared with `debt-and-covenant-tracking`.
6. **Which output metrics the client actually decides on.**
7. **Prescribed lender or regulator stress scenarios**, which recur unchanged.
8. **The model's structure**, where it has been shared, so scenarios can be computed rather than handed back.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed.**

**Persist the method, re-measure the values.** Every run has more history than the last, and the ranges should improve accordingly — which is the one respect in which this analysis genuinely gets better with age.

---

## Anti-patterns

- **Mechanical ±10% on every driver.** It makes the tornado a ranking of model coefficients.
- **Presenting a tornado without its ranges.** The chart is uninterpretable without them.
- **Mixing measured and supplied ranges in one tornado** without saying so.
- **Symmetric ranges by default.** Real drivers are asymmetric and the history shows it.
- **Treating measured volatility as covering the tail.** A business that has never had a crisis has no crisis in its data.
- **A stress case built only from history.** That is a memory, not a stress test.
- **Flexing correlated drivers independently** and calling the result a scenario.
- **A five-point grid across a cliff.** Solve for the inflection and sample around it.
- **Monte Carlo P99 from thirty-six observations.** The data does not support it.
- **Fitting a parametric distribution to a short series** when empirical resampling claims less and says more.
- **Reporting an expected value with no distribution.** The mean is often an outcome nobody will experience.
- **Omitting working capital drivers from a cash-metric tornado.**
- **Running a downside on a model that only converges at base.**
- **Producing all seven sheets when the board asked one question.**
- **Recommending what management should do.** Show which driver dominates; stop there.
- **Measuring volatility from fixture data.** It is zero, and it looks like an answer.
