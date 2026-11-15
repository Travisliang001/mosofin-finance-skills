<!-- tax-planning-and-projections · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Project the income/profit base
- Step 2 — Compute the projected tax
- Step 3 — Compute estimated / quarterly payments
- Step 4 — Tax set-aside planning
- Step 5 — Evaluate planning options
- Step 6 — Distinguish legitimate planning from evasion
- Step 7 — Sensitivity to assumptions
- Step 8 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is an illustration.** The gateway is read-only. **Mosofin files nothing, pays nothing, and advises nobody.**

---

## Inputs

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Taxpayer type and jurisdiction** | Individual/corporate, country/state | **Required** | Not in the books | `[manual]` |
| **Projected income/profit** | By source or type | **Required** | **YTD is a live read; the forward half is not** | Split — see Step 1 |
| **Current rates, brackets, allowances, rules** | User-supplied or current-sourced | **Required** | **Never from this file. Never carried forward.** | `[manual]` |
| **Payments already made** | Withholding, prior estimates | **Required for estimates** | **Live read** | `[auto]` |
| Prior year tax | For safe-harbour estimates | Recommended | **Live read** where the prior charge is in the books | `[auto]` |
| Decisions under consideration | Investments, timing, structure, contributions | If planning specific moves | Not in the books | `[manual]` |
| Available reliefs / deductions / credits | Pension, R&D, capital allowances | Recommended | **Some are evidenced** — R&D spend, pension payments, asset additions | `[auto]` in part |
| Cash flow context | To plan tax set-aside | Recommended | **Live read — cash balance and burn** | `[auto]` |

---

## Workflow

### Step 1 — Project the income/profit base

**Split: `[auto]` for the year to date, `[manual]` for the rest and for the adjustments.**

**For businesses**: projected profit, **adjusted toward taxable income using the book-to-tax logic** from `tax-return-prep-corporate` — depreciation against capital allowances, disallowables, and so on.

**For individuals**: projected income **by type** — employment, self-employment, investment, capital gains — per `personal-tax-return-prep`.

> **Use the entity's forecast — link to `rolling-forecast` or `budget-builder` for businesses — rather than a guess.**

**Preserved and reinforced**, because the workspace makes it easier to comply with: the forecast's actuals half is already being read by `rolling-forecast`, and **using the same base for both keeps the tax projection consistent with the financial one.** Two different profit projections in one business is a common and avoidable confusion.

**What the workspace gives Step 1** `[auto]`:

- **Year-to-date profit or income, exactly**, by account and by source
- **The comparable period last year**, which is the best available guide to how the rest of the year typically runs
- **Seasonality**, derivable from history exactly as in `rolling-forecast` — **a straight-line annualisation of nine months is wrong in a seasonal business, and the ledger knows the shape**
- **Evidence for several of the adjustments**: asset additions bearing on capital allowances, expense categories that are commonly disallowable, R&D spend (`r-and-d-tax-credit`), pension contributions paid

**What it does not give**: the adjustments themselves, which are determinations, and the forward half, which is a forecast.

**Mark the basis on the face of the output.** A projection on book profit with the adjustments still outstanding is a legitimate interim answer **and must say which it is** — see the near-substitute note.

---

### Step 2 — Compute the projected tax

`[auto]` for the arithmetic; **`[manual]` for every parameter.**

> **Apply current-year rates, brackets and rules — confirm; never assume.**

- Project taxable income **after reliefs and allowances**
- Apply the **rate structure**
- Apply **credits**
- Arrive at the **projected tax liability**

> **Show the projected effective tax rate and the marginal rate — the rate on the next dollar, which is key for planning decisions.**

**Both rates, always.** The original's first edge case is about exactly this confusion, and showing only one is how it happens.

#### Step 2b — The threshold map *(Mosofin addition)*

**`[auto]` given the brackets, and it is the most directly actionable output of the whole skill.**

The second edge case says: *some decisions push income across a threshold — a higher bracket, the loss of an allowance, a surcharge.* **Model the cliff effect, not just a smooth rate.**

Given the projected base and the supplied thresholds, **compute the distance to each one**:

| Output | Example |
|---|---|
| **Headroom to each threshold** | *"Projected taxable income is 14,200 below the point at which [allowance] begins to be withdrawn."* |
| **The cost of crossing** | *"Income between X and Y is effectively taxed at Z% because of the withdrawal, not at the headline rate."* |
| **Where an effective marginal rate spikes** | Threshold withdrawals frequently create a band with a **higher effective marginal rate than the top rate**, which is invisible in a bracket table and decisive for a timing decision. |

**This is arithmetic, it is specific, and it is exactly what a planning conversation needs** — *"you have 14,200 of headroom"* is more useful than a projected liability, because it is the number a decision moves against.

**It is not advice.** Present the map; the professional advises on what to do with it.

---

### Step 3 — Compute estimated / quarterly payments

`[auto]` for two of the four sub-steps, and both automatic ones are practically important.

> **Most jurisdictions require pre-payment of tax during the year.**

| Sub-step | Verdict |
|---|---|
| **Determine the required estimated payments** from the projection and/or a **safe harbour** — often based on prior-year tax; **confirm the jurisdiction's rule** | `[manual]` for the rule; **`[auto]` for the prior-year tax**, which is the safe-harbour base and is readable |
| **Schedule the payment amounts and due dates** | `[manual]` for due dates; `[auto]` for the arithmetic |
| **Compare to payments already made; identify shortfall or overpayment** | **`[auto]`** — see below |
| **Flag underpayment-penalty risk** where estimates are too low — **do not compute punitive figures without confirming rules** | `[auto]` to flag the shortfall; **`[manual]` for any penalty computation.** The original's caution is preserved: flagging a risk is not the same as quoting a penalty, and quoting one on unconfirmed rules is worse than saying nothing. |

#### The payments-made check

**`[auto]`, one query, and it finds something no projection does.**

**Read the tax payments actually made in the period.** Then compare to the schedule.

| Finding | Meaning |
|---|---|
| Payments made on schedule | Good. Compare against the current projection for adequacy. |
| **A scheduled payment with no corresponding payment in the ledger** | **A missed instalment.** Interest usually runs from the due date, and it is running now. |
| Payments made, but below the required amount | A shortfall accruing. |
| Payments materially above requirement | An overpayment sitting with the authority — a cash-flow question. |

**A missed estimated payment is the kind of thing that is discovered when a notice arrives.** It is one read, and finding it early is worth more than the projection it accompanies.

---

### Step 4 — Tax set-aside planning

`[auto]` for the schedule; **`[auto]` for the affordability test**, which the original does not include and which is the practical heart of this step for a small business.

> **For businesses and the self-employed, translate the projection into a cash-set-aside plan:**
> - **How much of each period's income to reserve for tax**
> - **Timing aligned with payment due dates**
> - **Integrate with `cash-flow-forecast-13-week`** so tax payments appear in the cash plan

#### Step 4b — Can the tax actually be paid? *(Mosofin addition)*

**`[auto]`. Two reads, and it converts a projection into an answer to the question people are actually asking.**

*"How much should I set aside for tax"* is rarely a request for a number. It is a request to know whether the business is in trouble.

- **What is the current cash balance?** Live read.
- **Is there a designated tax reserve account, and what is in it?** Live read where one exists.
- **What is the accumulated shortfall?** Required set-aside to date, less what is actually reserved.
- **At the current cash generation rate, will the cash be there on the due date?** Computable from the burn and the payment schedule.

**The finding, when it is bad, is specific and early**: *"The projected liability due on [date] is 84,000. Cash currently stands at 31,000 and the trailing three-month net cash generation is 6,000 a month. On that trajectory the balance at the due date is approximately 49,000."*

**That is a fact, stated with its inputs, and it is a fact a business can act on with two months' notice rather than two days'.** See `cash-flow-forecast-13-week` for the short-horizon view and `rolling-forecast` for the longer one.

**Two cautions.** The projection depends on `[manual]` parameters, so the liability figure carries their uncertainty. And **the cash trajectory is an extrapolation** — label it as one, per `rolling-forecast`'s rule that a run-rate is a benchmark and not a forecast.

---

### Step 5 — Evaluate planning options

`[auto]` for the modelling; **`[manual]` for availability, for the decision, and for the advice.**

> **For each option the user is weighing, model the tax impact. Availability is jurisdiction-specific — confirm.**

All eight levers preserved:

| Lever | Note | Verdict |
|---|---|---|
| **Timing** — accelerating or deferring income or deductions between periods | Deferring a sale, prepaying deductible expenses | `[auto]` to model, **`[manual]` for availability** |
| **Retirement / pension contributions** — often deductible or relieved **up to limits** | `[auto]` for contributions already made; **`[manual]` for the limits** | Split |
| **Capital allowances / depreciation elections** — timing of asset purchases and expensing elections | `[auto]` for asset additions to date; `[manual]` for the elections. See `fixed-asset-register-and-depreciation` | Split |
| **Loss utilisation** — timing to use losses efficiently | `[auto]` for losses in the books; **`[manual]` for the rules**, which are intricate and restrictive | Split |
| **Entity structure** — salary versus dividend, entity type; **significant for owner-managed businesses** | **`[manual]`** — spans two taxpayers; see Gate 1 | `[manual]` |
| **Charitable giving**, where relief is available | `[auto]` for giving to date; `[manual]` for relief | Split |
| **Capital gains planning** — annual exemptions, loss harvesting, holding-period thresholds | `[auto]` for realised gains in the books; **`[manual]` for exemptions and the anti-avoidance interaction** | Split |
| **Credits** — ensuring available credits are captured, e.g. R&D | **`[auto]` to detect candidate spend**; `[manual]` for the claim. See `r-and-d-tax-credit` | Split |

> **For each option: show the tax with and without, the net benefit, the cash impact, and the timing. Compare options side by side.**

`[auto]` for all four columns once the parameters are supplied.

**And the discipline from edge case 3 belongs in the comparison itself**: **state, per option, whether it is a permanent saving or a deferral.** A deferral has a cash benefit and no tax saving, and the two are routinely presented together as though equivalent. **Add "permanent or timing?" as a column**, not a footnote.

**The credits lever deserves a note**, because it is the one where the workspace can find something unprompted: **reading the cost ledger for spend that looks like qualifying R&D, or for reliefs the business is entitled to and has not claimed**, is a completeness sweep of the kind `r-and-d-tax-credit` describes. **Under-claiming is invisible** — nobody audits a return for the relief it omitted — so this is unambiguously in the client's favour.

---

### Step 6 — Distinguish legitimate planning from evasion

**`[manual]` in judgment, and preserved without any weakening.**

> **This skill only addresses legitimate tax planning — arranging affairs efficiently within the law, using reliefs as intended, sensible timing, appropriate structure.**
>
> **It does NOT facilitate:**
> - **Concealing income or inflating deductions**
> - **Sham transactions or arrangements lacking substance**
> - **Anything constituting evasion or abusive avoidance**
>
> **Where a "plan" strays toward aggressive avoidance, flag the anti-avoidance risk — general anti-avoidance rules exist in many jurisdictions — and recommend specialist advice. Stay firmly on the legitimate side.**

**Three Mosofin points that follow from having a live connection:**

**Mosofin reads and cannot conceal.** There is no write path: no transaction can be altered, removed or reclassified through this gateway. That is a structural property, not a policy.

**A request outside the line is not a planning request.** If what is asked amounts to concealment, inflated deductions, or a transaction constructed without substance, **it is outside this skill.** Say so plainly, once, and do not produce a partial version or a version with a caveat attached — a caveated version of the wrong thing is still the wrong thing.

**Substance is not visible in a ledger, and that cuts against complacency.** A transaction lacking commercial substance posts exactly like one that has it. **Mosofin cannot distinguish them**, which means an arrangement's substance is a `[manual]` question every time, and the absence of a red flag in the data is not evidence that the arrangement is sound.

---

### Step 7 — Sensitivity to assumptions

`[auto]`, and it connects to a skill that does this properly.

> **Tax projections depend on income assumptions and rules:**
> - **Show how the projected tax changes if income comes in higher or lower** — link to `scenario-and-sensitivity-analysis`
> - **Note where a rule change or threshold could shift the result**
> - **Keep the projection updatable as the year progresses**

**All three preserved, and each gains something from the connection:**

- **Income sensitivity** `[auto]`, with the ranges grounded in the client's own observed variability rather than a mechanical ±10% — which is exactly the contribution `scenario-and-sensitivity-analysis` makes, and it applies here directly.
- **Threshold effects** `[auto]` — Step 2b's map already identifies where the cliffs are, so the sensitivity can be sampled finely around them instead of stepping over them.
- **"Keep the projection updatable as the year progresses"** — **`[auto]`, and this is the strongest structural point.** The projection's base is a live read, so **re-running it monthly costs one query.** A tax projection prepared in month three and never revisited is the normal state of affairs and it is usually wrong by month nine. **Re-run it as the actuals arrive**, exactly as `rolling-forecast` re-anchors each month.

---

### Step 8 — Output

An `.xlsx` planning workbook. All seven of the original's sheets, plus two additions.

**Sheet 1: Tax Projection Summary**
Projected income → taxable base → tax → credits → net liability; **effective and marginal rates.** **Header states the basis** — book or tax-adjusted — and carries every parameter's source and confirmation date, plus the fixture flag.

**Sheet 2: Income/Profit Projection**
The base build by source. **YTD actual and projected balance shown separately and shaded differently**, per `rolling-forecast`.

**Sheet 3: Estimated Payments Schedule**
Required payments, due dates, paid to date, shortfall or overpayment. **With the payments-made check result**, and missed instalments flagged at the top.

**Sheet 4: Tax Set-Aside Plan**
Per-period reserve aligned to cash flow. **With the Step 4b affordability test.**

**Sheet 5: Planning Options Comparison**
Each option modelled: with and without, net benefit, timing, cash impact — **and a "permanent or timing?" column.**

**Sheet 6: Sensitivity**
Tax under different income scenarios, **with ranges from observed variability where available**, and finer sampling near thresholds.

**Sheet 7: Open Items / Professional Advice**
**Rules confirmed and still needed; anti-avoidance flags; items for professional sign-off.** Every `[manual]` parameter appears here with its status.

**Sheet 8: Threshold Map** *(Mosofin addition)*
| Threshold | Value (source, date) | Projected position | Headroom | Effective marginal rate in band | Note |
|---|---|---|---|---|---|

**Sheet 9: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Tax_Planning_[YYYY]_[Name].xlsx`

**Every sheet carries the professional-advice statement.** If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All eleven preserved.

- **Projection built from a real income or profit forecast, not a guess.** `[auto]` for the YTD base; **the same base as the financial forecast.**
- **Current-year rates, brackets and rules confirmed, not assumed.** `[manual]`, **and nothing persisted supplies one.**
- **Effective and marginal rates both shown.** `[auto]`
- **Estimated payments scheduled with due dates and safe-harbour consideration.** `[auto]` for the prior-year base and **the payments-made check.**
- **Tax set-aside integrated with cash planning.** `[auto]`, **including whether the cash will actually be there.**
- **Planning options modelled side by side** — with and without, net benefit, timing, **deferral versus saving.** `[auto]`
- **Only legitimate planning; anti-avoidance risks flagged.** `[manual]`
- **Sensitivity to income assumptions shown.** `[auto]`, with grounded ranges.
- **No hardcoded tax parameters.** `[manual]`
- **Clear recommendation for qualified professional advice before acting.** **On every sheet.**
- **File naming consistent.** `[auto]`

**Five Mosofin additions:**

- **The basis is stated** — book profit or tax-adjusted — and never blurred.
- **Missed estimated payments are flagged**, since interest is already running.
- **Affordability is tested**, not just the liability computed.
- **The threshold map is produced**, because headroom is what a decision moves against.
- **The projection is re-run as actuals arrive**, rather than prepared once.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and every tax parameter.** The original forbids it and it is the discipline of the skill.

**What is worth persisting into the workspace-scoped skill:**

1. **The account mapping** — which accounts feed the taxable base, which are commonly disallowable, which represent qualifying spend.
2. **The book-to-tax adjustment pattern** for this business: which adjustments recur, and roughly how large. **The pattern, not the amounts.**
3. **The payment schedule shape** — due dates and instalment convention for this taxpayer.
4. **Whether a designated tax reserve account exists**, and which one.
5. **Seasonality**, shared with `rolling-forecast`.
6. **The safe-harbour rule that applies**, and where it was sourced.
7. **Reliefs the client is entitled to and habitually claims** — so the completeness sweep starts from a known list.
8. **Options previously modelled and declined, with the reason**, so the same suggestion is not re-made annually.
9. **Which professional signs off**, and what they need to see.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and a tax position is among the most sensitive things a client has.

**Store where the parameters come from, never the parameters.** That is the difference between a skill that gets faster and one that gets wrong.

---

## Anti-patterns

- **Applying a rate to book profit and calling it a tax projection.** The adjustments are the point.
- **Confusing the accounting provision with the cash payable.**
- **Annualising year-to-date in a seasonal business.**
- **Showing only the effective rate.** Decisions run on the marginal one.
- **Modelling a smooth rate across a threshold.** The cliff is the whole point.
- **Presenting a deferral as a saving.**
- **Modelling the corporate layer alone** for an extraction decision.
- **Omitting social contributions** and understating the burden.
- **Quoting a penalty on unconfirmed rules.**
- **Preparing the projection once in month three.** Re-run it; the base is a live read.
- **Computing the liability without checking the cash.** The client is asking whether they are in trouble.
- **Missing that an instalment was never paid.** It is one query and interest is running.
- **Carrying a rate or bracket forward.** The original forbids it; so does this file.
- **Treating the absence of a red flag as evidence of substance.** Substance is invisible in a ledger.
- **Producing a caveated version of a request that falls outside Step 6.** It is still the wrong thing.
- **Presenting projections as advice.** A qualified professional signs off before anybody acts.
