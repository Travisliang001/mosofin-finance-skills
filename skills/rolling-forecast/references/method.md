<!-- rolling-forecast · method.md · read for: Stages 3–6 — the forecast itself: verdicts, inputs, Steps 1–9, output quality, what to persist, anti-patterns. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Set the rolling window
- Step 2 — Lock actuals to date
- Step 3 — Update the drivers
- Step 3b — Challenge the forecast with its own arithmetic *(Mosofin addition)*
- Step 4 — Project forward
- Step 5 — Build the full-year (and beyond) view
- Step 6 — Track forecast accuracy
- Step 7 — Reconcile forecast changes
- Step 8 — Scenario overlay (optional)
- Step 9 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. **And a further boundary specific to this skill: Mosofin does not author a forecast.** It locks actuals, derives patterns, computes consequences and asks questions. The projection is the client's, and where it is used for external guidance, **no forward-looking statement is ever authored here.**

---

## Inputs

All nine preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Forecast horizon** | Rolling 12 or 18 months | **Required** | Not in the books; persist after first agreement | `[manual]` |
| **Actuals to date** | By month, by line | **Required** | **Live read — this is the skill's core automatic input** | `[auto]` |
| Prior forecast, if updating | The forecast being refreshed | Recommended | **Not in the books. Persisted from the last run** — see the lifecycle section | `[manual]`, then automatic once persisted |
| Original budget | For reference | Recommended | **`[auto]` if the budget is loaded into the book; `[manual]` if it lives in a spreadsheet.** Check — do not assume | `[auto]` in part |
| **Drivers and assumptions** | Updated for latest information | **Required** | Not in the books | `[manual]` |
| Pipeline / bookings | For revenue forecasting | Recommended | **Not in the books.** A CRM metric. | `[manual]` |
| Headcount plan | Hires, attrition | Recommended | **The plan is not in the books; the current payroll run-rate is** | `[manual]`, `[auto]` in part |
| Known future events | Contracts, launches, price changes | Recommended | Not in the books | `[manual]` |
| Functional currency | ISO code | **Required** | Company record | `[auto]` |

---

## Workflow

### Step 1 — Set the rolling window

`[manual]` to choose; `[auto]` to apply thereafter.

A rolling forecast projects N periods forward from the current point. **As each month closes, the forecast rolls forward one month — the just-closed month becomes actual, and a new month is added at the far end.**

Define all three:

- **Horizon** — 12, 18 or 24 months
- **Granularity** — monthly typically; sometimes quarterly beyond twelve months
- **Refresh cadence** — monthly after close, sometimes quarterly

**Once these are agreed they belong in the profile.** The roll itself is then mechanical: `[auto]` to determine which months are closed, which are projected, and which new month enters the far end of the window.

---

### Step 2 — Lock actuals to date

**`[auto]`, and this is the mechanic that makes the skill worth connecting.**

Replace the forecast for closed periods with actuals:

```
Forecast = [actuals for closed months] + [projection for remaining months]
```

> **This is the key feature: the forecast continuously incorporates real results, improving accuracy as the year progresses.**

`[auto]` in full — read the closed months, by line, and substitute. What was a monthly manual export-and-paste becomes a read.

#### Step 2b — Verify the month is actually closed *(Mosofin addition)*

`[auto]`, and it must run **before** the lock, not after.

**A month is not closed because the calendar has moved past it.** Before locking a period as actual, check:

- **Do the recurring entries appear?** Depreciation, prepaid amortisation, accruals. A month missing them is a month that will grow. See `recurring-transaction-builder` and `prepaid-amortization-schedule`.
- **Are there accruals with no reversal, or reversals with no accrual?** See `journal-entry-review`.
- **Has anything been posted into the month since it was declared closed?** A quarter-end close runs the same test.
- **Does the month's activity look complete** against the preceding months — a materially lower transaction count is a month still being worked on.

**Why this matters more here than elsewhere.** Locking an unfinished month does two kinds of damage. It puts a wrong number into the current forecast, which is recoverable. And it **puts a wrong outturn into the accuracy tracker**, which is not — because Step 6 will forever score prior forecasts against a figure that was never the real result. **A corrupted accuracy history is worse than none**, since it produces confident bias corrections in the wrong direction.

If a month is not properly closed, **say so and do not lock it.** Run `month-end-close-checklist` first.

---

### Step 3 — Update the drivers

**`[manual]` in substance — and it is the step the original correctly identifies as where the value is.**

> **This is where the rolling forecast earns its value — re-examine assumptions in light of actuals.**

**Revenue drivers** — all four preserved:

| Driver | Question | Verdict |
|---|---|---|
| Pipeline | **Has the pipeline changed?** Update bookings projections. | `[manual]` — CRM, not ledger |
| Churn | **Has churn run higher or lower than assumed?** Update retention. | **`[auto]` in part** — customers who invoiced last year and not this year are readable; *why* they left is not |
| Ramp | **Are new customers ramping as expected?** | **`[auto]` in part** — revenue per customer by months-since-first-invoice is computable |
| Pricing | **Has pricing held?** | **`[auto]` in part** — realised price per unit, where units are on the invoice lines |

**Cost drivers** — all three preserved:

| Driver | Question | Verdict |
|---|---|---|
| Hiring | **Is hiring on pace?** Update headcount timing. | **`[auto]` for the payroll run-rate**; `[manual]` for the plan |
| Unit costs | **Have unit costs moved?** | `[auto]` where units are on purchase lines |
| Discretionary | **Are discretionary spends tracking?** | `[auto]` against budget where the budget is in the book |

> **Do not just re-spread the original budget — incorporate what the actuals are telling you. If Q1 revenue ran 10% below plan due to slower bookings, the rolling forecast should reflect a revised bookings trajectory, not blindly hold the annual number.**

**Preserved with full emphasis. It is the discipline the whole skill exists to impose, and Step 3b is how a connected workspace enforces it.**

Note the pattern in the tables above: **for four of the seven drivers, the workspace can compute what actually happened, and none of the seven can it decide what will happen next.** Churn is measurable; whether it continues is a judgment. Realised pricing is measurable; whether the next price increase sticks is not. That is the right split, and presenting the measured half is what makes the judgment half better informed.

---

### Step 3b — Challenge the forecast with its own arithmetic *(Mosofin addition)*

**`[auto]`. Three tests, and the first is the one that makes the last quality standard real.**

**Test A — The implied acceleration, or "hockey stick," test.**

The original's third edge case and its final quality standard both say the same thing: **the forecast must reflect reality rather than defend the budget.** That is easy to write and hard to enforce, because a forecast that quietly holds the annual number looks perfectly normal on the page.

**It is not normal in the arithmetic.** If year-to-date revenue is behind plan and the full-year forecast is unchanged, **the remaining months must be carrying the shortfall**, and the size of what they are carrying can be computed exactly:

```
Implied remaining-period growth
  = (Full-year forecast - Actuals YTD) / Remaining months
    compared with
    Actuals YTD / Elapsed months
```

State the result as a plain sentence with a number in it: *"The forecast requires the remaining five months to run 34% above the average of the seven months to date. The last time that was achieved was never."*

**That sentence is a fact, not an opinion**, and it is the single most useful thing this skill can say. It does not conclude that the forecast is wrong — a genuine step-change, a signed contract, a launch, a seasonal peak can all justify it, and Step 3 is where those are captured. **It requires the acceleration to be explained rather than assumed**, which is exactly what "no defending the budget" means in practice.

Run the same test on costs, where the bias runs the other way: a cost forecast that requires spending to *fall* for the rest of the year, with no identified action to make that happen, is the same phenomenon inverted.

**Test B — The seasonality check.** `[auto]`

**Seasonality is derivable from the ledger**, and this is a genuine contribution the original treats as a user input. With two or more years of monthly history:

- compute a **monthly seasonal index** by line — each month's share of its year, averaged across available years
- report **how many years support it**, because two years is a thin basis and one is none
- compare the **forecast's implied seasonality** against the historical pattern

A forecast that spreads revenue evenly across twelve months, in a business whose history shows a decisive December, is not maintaining seasonality — and the original's quality standard requires that it does. This test also covers the horizon-boundary edge case: **when the rolling window rolls into a new seasonal cycle, the newly added months should carry the seasonal pattern**, and it is easy to add a flat month at the far end without noticing.

**Test C — The run-rate benchmark.** `[auto]`

Compute the simple annualised run-rate from actuals and show it beside the forecast. **This is not a forecast** — see the near-substitute note — and it must be labelled as a benchmark. But the gap between a naive run-rate and the forecast is precisely the amount of judgment the forecast contains, and making that quantity visible is useful. A forecast very close to run-rate is barely forecasting; one far from it is carrying a lot of assumption, and either can be right.

---

### Step 4 — Project forward

`[manual]` for the projection. `[auto]` for the mechanics and the historical inputs.

**Revenue** — all three models preserved, using the same driver models as the annual budget, with refreshed inputs:

```
- SaaS:     roll ARR forward with updated new / expansion / churn
- Units:    updated volume x price
- Services: updated capacity x utilization x rate
```

`[auto]` for the historical values of each of those inputs — realised churn, realised price, realised utilisation — where the data is in the book. **`[manual]` for the forward values**, which is the forecast itself. And note: **ARR is a contract metric, not a ledger metric**; the ledger informs it and does not contain it.

**Costs** — all four categories preserved:

| Category | Treatment | Verdict |
|---|---|---|
| **Variable costs** | Flex with updated volume | `[auto]` for the historical variable rate; `[manual]` for the volume |
| **Personnel** | From the updated headcount plan | `[auto]` for current run-rate; `[manual]` for the plan |
| **Fixed / committed costs** | Carry forward | **`[auto]`** — the most reliably projectable line in any forecast, and readable directly |
| **Discretionary** | Per the latest plan | `[manual]` |

> **Maintain seasonality patterns.**

`[auto]` — Test B supplies the pattern, from history, per line.

---

### Step 5 — Build the full-year (and beyond) view

**`[auto]` for the arithmetic and both comparisons.**

```
Full-year forecast = Actuals YTD + Projection for remaining months
```

Compare to — both preserved:

- **The original budget** — *are we going to hit it?* `[auto]` where the budget is in the book; `[manual]` where it is in a spreadsheet. **Check which; do not assume.** See `budget-vs-actual-analysis`.
- **The prior forecast** — *what changed since the last refresh?* `[auto]` **once prior forecasts are persisted** — which is the lifecycle point, and the reason run one cannot do this and run six can.

For the rolling horizon beyond the current year, project the additional months. `[manual]`, with `[auto]` seasonality applied.

---

### Step 6 — Track forecast accuracy

**The strongest lifecycle case in the skill, and the step organisations most often skip — precisely because it requires having kept the old forecasts.**

> **A discipline that improves the process over time.**

```
Forecast accuracy = 1 - |Actual - Forecast| / Actual
```

**By line and in aggregate.** `[auto]` for the computation; the actuals are a live read and the prior forecasts come from the persisted history.

**Identify systematic bias** — both preserved:

- **Consistently over-forecasting revenue?** (optimism bias)
- **Consistently under-forecasting costs?**

`[auto]`, and this is arithmetic over a series: not whether one forecast missed, but **whether the misses have a direction.** A forecast that is wrong by 8% in random directions is noisy. One that is wrong by 8% in the same direction eleven times running is **biased**, and bias is correctable in a way that noise is not.

> **Use the accuracy track record to calibrate future forecasts.**

**Three notes on doing this honestly:**

- **Score the same horizon consistently.** A one-month-ahead forecast and a twelve-month-ahead forecast are not comparable, and mixing them flatters the record. Track accuracy **by horizon**: how good is this organisation one month out, three months out, twelve months out? The answer is usually very different, and knowing it tells you how much weight the far end of the window deserves.
- **Score against final actuals**, which is why Step 2b matters.
- **Report the record whether or not it is flattering.** An accuracy tracker that only appears in good quarters is not a tracker.

**On run one this step is empty**, and it should say so rather than being omitted — an empty accuracy tracker with a note that collection has started is a promise; a missing sheet is nothing.

---

### Step 7 — Reconcile forecast changes

`[auto]` for one of the three lines — **and that one anchors the other two.**

```
Prior forecast full-year revenue             $X
+/- Change from actuals coming in different  $A
+/- Change from revised assumptions          $B
+/- Change from new information              $C
= Current forecast full-year revenue         $X + A + B + C
```

| Line | Verdict | Note |
|---|---|---|
| Prior forecast | `[auto]` once persisted | From the history |
| **Change from actuals coming in different** | **`[auto]`** | Forecast versus actual for the closed months. Pure arithmetic, exact. |
| Change from revised assumptions | `[manual]` | A decision somebody made |
| Change from new information | `[manual]` | An event somebody learned of |
| Current forecast | `[auto]` | The sum |

**Why the automatic line does more work than it appears to.**

Both ends of the bridge are known — the prior forecast is persisted, the current one is being produced — and **the actuals variance is computable exactly.** So the remaining movement is a **residual that must be explained by assumption changes and new information**, and its size is known before anyone writes a word.

**That turns the bridge from a narrative into a constraint.** If 400,000 of movement remains after the actuals variance, then 400,000 of assumption change has been made, and it has to be named. In manual practice this is where a bridge quietly acquires an "other" line that absorbs whatever did not get explained. **With the residual computed, "other" is visibly the unexplained portion of a decision somebody made**, which is a much harder thing to leave in a board pack.

> **A "bridge" between forecast versions so stakeholders understand the movement.**

---

### Step 8 — Scenario overlay (optional)

`[manual]`. Layer scenarios on the base forecast — best, base, worst — and leave the full treatment to a dedicated scenario analysis. A rolling forecast often carries a base case plus upside and downside ranges.

`[auto]` contribution: **historical volatility by line**, which is a defensible basis for the width of the range. How much have revenue and each major cost line actually varied month to month over the available history? A downside case narrower than the business's own observed variability is not a downside case. See the early-stage edge case, which asks for exactly this.

---

### Step 9 — Output

An `.xlsx` rolling forecast workbook. All seven of the original's sheets, plus two additions.

**Sheet 1: Rolling Forecast Summary**
The full horizon — **actuals shaded, blending into forecast** — with key metrics. `[auto]` for the actuals block and the shading boundary. **The boundary must be unmistakable**; it is the first quality standard and the commonest way a forecast gets quoted as if it were a result.

**Sheet 2: Monthly Detail (P&L)**
Every line across the rolling window, **actuals versus forecast clearly distinguished.** `[auto]` for actuals.

**Sheet 3: Current Year Outlook**
Actuals YTD plus remaining forecast equals full-year, compared to budget and prior forecast. `[auto]`.

**Sheet 4: Driver Assumptions (Updated)**
Current assumptions with **changes from the prior forecast highlighted.** `[manual]` for the assumptions; `[auto]` for the highlighting, against the persisted prior set — and `[auto]` for a **Realised** column showing what each driver actually did, beside what it is assumed to do next.

**Sheet 5: Forecast Bridge**
Prior forecast to current forecast, by driver of change. **The actuals line computed; the residual computed; the explanation required.**

**Sheet 6: Forecast Accuracy Tracker**
Historical forecast versus actual, accuracy percentage, bias analysis. **By horizon.** `[auto]` from persisted history. On run one: present and empty, with a note.

**Sheet 7: Scenario Range** (if applicable), with historical volatility alongside.

**Sheet 8: Forecast Challenge** *(Mosofin addition)*
The Step 3b tests:

| Test | Line | Finding | Figure | Question for management |
|---|---|---|---|---|

Implied remaining-period acceleration. Seasonality against history, with the years of support. Run-rate benchmark and the gap. **Each row ends in a question, not a verdict** — the forecast is management's and the challenge is evidence for their discussion.

**Sheet 9: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet, including **which months were locked and whether each was verified closed.**

> **Build with live formulas so actuals can be dropped in and the forecast rolls automatically.**

Preserved — and note the Mosofin twist: **the actuals no longer need dropping in.** They are read. The live formulas still matter, because the workbook goes to people who will flex it themselves, but the monthly re-keying that the original is designing around is gone.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Rolling_Forecast_[YYYY-MM]_[EntityName].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All nine preserved.

- **Actuals-to-date locked in and clearly distinguished from forecast.** `[auto]` — **and each locked month verified closed first** (Step 2b).
- **Drivers updated based on actuals, not just re-spread budget.** `[manual]` to update; **`[auto]` to demonstrate whether it happened**, via Test A.
- **Full-year outlook = actuals YTD + remaining forecast.** `[auto]`
- **Forecast bridge explains changes from the prior version.** `[auto]` for the actuals line and the residual; **`[manual]` for the explanation, which the computed residual makes unavoidable.**
- **Forecast accuracy tracked and bias identified.** `[auto]` from persisted history, **by horizon.**
- **Seasonality maintained across the horizon.** `[auto]` to derive from history and to test, **with the years of support stated.**
- **Live formulas for rolling refresh.** `[auto]` — though the actuals now arrive by read rather than by hand.
- **File naming consistent.** `[auto]`
- **No defending the budget against contradicting actuals.** **`[auto]` to enforce.** Test A quantifies the acceleration a defended budget requires, and requires it to be explained.

**Four Mosofin additions:**

- **No month is locked until it is verified closed**, because a corrupted accuracy history is worse than none.
- **Measured and assumed are always distinguished** — realised churn beside assumed churn, realised price beside assumed price.
- **Every challenge is a question, not a verdict.** The forecast belongs to management.
- **No forward-looking statement is ever authored.**

---

## Seed to evolved: what happens on the first real run

**This skill has the strongest lifecycle case in the pack**, and it is structural rather than convenient: **Steps 6 and 7 cannot function on run one.** An accuracy tracker with no prior forecasts is empty. A bridge with no prior version has nothing to bridge from. Both become more valuable every single period, and only if the history is kept.

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — and **any FX or inflation assumption.**

**What must be persisted after every run:**

1. **The forecast itself, in full, with its date and horizon.** This is not optional housekeeping — **it is the input to the next run's bridge and to every future accuracy score.** A rolling forecast process that discards its own history is a monthly re-spreading exercise wearing the name.
2. **The driver set and assumptions**, so Sheet 4 can highlight what changed.
3. **The horizon, granularity and cadence.**
4. **The derived seasonality indices**, with the years supporting them, refreshed as history lengthens.
5. **The accuracy record by horizon**, accumulating.
6. **The bias correction observed**, and whether it has been applied.
7. **Deal slip rates and hire timing slippage**, computed from plan-versus-actual over time — these are the client's own empirical corrections and they exist nowhere else.
8. **Whether the budget is in the book or in a spreadsheet.**
9. **Step 3b findings and their explanations**, so a challenge already answered is not re-raised identically next month.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed.**

**Run one produces a forecast. Run twelve produces a forecast, its bridge, its accuracy record, its measured bias, and a challenge grounded in a year of this company's own behaviour.** That gap is the entire argument for the lifecycle, and this is the skill where it is most visible.

---

## Anti-patterns

- **Locking a month that is not closed.** It corrupts the forecast recoverably and the accuracy tracker permanently.
- **Re-spreading the budget and calling it a re-forecast.** Test A will show what that costs.
- **Holding the annual number when actuals are behind**, without naming the acceleration required.
- **Presenting a run-rate as a forecast.** It is a benchmark.
- **Quoting a blended actual-plus-forecast figure as a result.** The boundary must be unmistakable.
- **Flat-lining the far end of the window** and losing the seasonal pattern.
- **Deriving seasonality from one year** without saying so.
- **Scoring accuracy across mixed horizons.** One month out and twelve months out are different skills.
- **Showing the accuracy tracker only when it is flattering.**
- **Letting an "other" line absorb the bridge residual.** The residual is computable; the explanation is owed.
- **Discarding the prior forecast.** It is the input to everything that makes this skill improve.
- **A downside scenario narrower than the business's observed volatility.**
- **Carrying an FX assumption forward** from a prior run.
- **Summing group entities without eliminations**, then compounding it across the horizon.
- **Authoring a forward-looking statement.** Management guides.
