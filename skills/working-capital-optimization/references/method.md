<!-- working-capital-optimization · method.md · read for: Stages 3–6 — the diagnostic itself: verdicts, inputs, Steps 1–10, output quality, what to persist, anti-patterns. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Diagnose: compute the cash conversion cycle
- Step 1b — Separate growth, seasonality and deterioration *(Mosofin addition)*
- Step 2 — Diagnose: AR — where is collection slow?
- Step 3 — Diagnose: Inventory — where is it stuck?
- Step 4 — Diagnose: AP — are we leaving cash on the table?
- Step 5 — Identify levers per component
- Step 6 — Quantify and prioritise the opportunities
- Step 7 — Address the trade-offs honestly
- Step 8 — Build the implementation roadmap
- Step 9 — Set KPIs and monitoring
- Step 10 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is analysis and proposal.** The gateway is read-only. **Mosofin changes no terms, pays nobody, and contacts no supplier or customer.**

---

## Inputs

All nine preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Balance sheet history** | Monthly AR, inventory, AP, accruals — **24+ months** | **Required** | **`[auto]`, exactly, for as long a history as exists** | **`[auto]`** |
| **Revenue and COGS history** | For days computations | **Required** | **`[auto]`** | **`[auto]`** |
| **AR ageing** | Current detail | **Required** | **`[auto]`** — see `ar-aging-and-collections` | **`[auto]`** |
| **Inventory detail** | By category, slow-moving / obsolete | **Required** | **`[auto]` only if item-level data is exposed** — see Gate 2 | Conditional |
| **AP detail** | By vendor, terms, payment history | **Required** | **`[auto]`** | **`[auto]`** |
| **Customer payment terms** | Standard and exceptions | **Required** | **Recorded terms `[auto]`; agreed terms `[manual]`** — and they differ | Split |
| **Supplier payment terms** | Standard and exceptions | **Required** | Same | Split |
| Industry benchmarks | DSO/DIO/DPO for the industry | Recommended | **Not on this surface** | `[manual]` |
| Cost of capital | For valuing the cash unlock | Recommended | Not in the books | `[manual]` |

---

## Workflow

### Step 1 — Diagnose: compute the cash conversion cycle

**`[auto]`, completely.** All four formulas preserved.

```
DSO (Days Sales Outstanding)     = (AR / Revenue) x Period days
DIO (Days Inventory Outstanding) = (Inventory / COGS) x Period days
DPO (Days Payable Outstanding)   = (AP / COGS or Purchases) x Period days

Cash Conversion Cycle (CCC) = DSO + DIO - DPO
```

> **The CCC is the number of days between paying suppliers and collecting from customers — the time cash is "out the door" funding operations. Lower, or negative, CCC = less cash tied up.**

> **Compute trends, seasonality, and compare to industry benchmarks where available. Identify which component is the largest opportunity.**

`[auto]` for trends and seasonality — **monthly, across the full history**, derived the way a rolling forecast derives its seasonal indices. `[manual]` for the benchmarks.

**Quantify the cash impact**, preserved:

> **A one-day improvement in DSO ≈ one day of revenue in cash; one day in DIO ≈ one day of COGS; one day in DPO ≈ one day of COGS or purchases. Multiply by the entity's daily volume to dollar-value the opportunity.**

`[auto]`, and **note the DPO denominator choice matters**: purchases is the more accurate base, COGS the more available one, and **they differ in a business whose inventory is moving.** State which was used — a DPO computed on COGS in a business building stock overstates payment days.

---

### Step 1b — Separate growth, seasonality and deterioration *(Mosofin addition)*

**`[auto]`, and it prevents two of the source's own edge cases from being misread.**

A working capital balance moves for three quite different reasons, and **only one of them is a problem.**

| Cause | What it means | How to see it |
|---|---|---|
| **Volume** | More revenue means more receivables at the same DSO | **Days are flat; balances grow** — edge case 5 |
| **Seasonality** | The annual cycle | **Days move and return** — edge case 4 |
| **Days deterioration** | Collection, stocking or payment behaviour changed | **Days move and stay moved** — the actual finding |

**Decompose the movement arithmetically**: hold days constant and revalue at current volume to isolate the volume effect; compare to the same month last year to isolate seasonality; **the residual is the deterioration.**

> **Do not interpret growing working capital investment as inefficiency if it is funding growth.**

Preserved, and this decomposition is what makes it operational rather than a caveat.

**And the window-dressing detection** `[auto]`, which serves edge cases 6 and 12: **look at the shape within the period, not just the period end.** A DSO that drops sharply in the last week of each quarter and rebounds in the first week of the next is **a collection push, not an improvement** — the cash is real and it is not repeatable. **Report the intra-period pattern**; it distinguishes a process change from an effort, which is exactly what edge case 6 asks for.

---

### Step 2 — Diagnose: AR — where is collection slow?

**`[auto]` for all eight diagnostics.** From `ar-aging-and-collections`.

| Diagnostic | Verdict |
|---|---|
| **AR ageing buckets** — current, 1–30, 31–60, 61–90, 90+ past due | `[auto]` |
| **DSO by customer segment** | `[auto]` where segments are a dimension |
| **Disputed / credit-held invoices** | `[manual]` — **dispute status is not an accounting field**; see `ar-aging-and-collections` |
| **Pattern by customer** — chronically slow payers, recent deterioration | **`[auto]`** — days-to-pay per customer, trended |
| **Time from invoice generation to issuance** — internal delay | **`[auto]` — see below** |
| **Time from issuance to acceptance / PO match** — process delay | `[auto]` in part |
| **Time from due date to actual payment** — collection delay | **`[auto]`** |
| **Past-due composition** — true delinquency versus process or dispute issues | `[auto]` for the ageing; `[manual]` for the classification |

**Root causes**, all five preserved: **slow invoicing; disputed billings; lax follow-up; customer payment behaviour beyond terms; concentration on a few large slow payers.**

`[auto]` evidences the first, fourth and fifth directly; the second and third are `[manual]`.

#### Decomposing DSO is the highest-value diagnostic here

**`[auto]`, and it is the analysis the original asks for that almost nobody performs**, because by hand it means opening hundreds of invoices.

**"DSO is 52 days" is not actionable. This is:**

```
Order to invoice date        7 days   <- internal
Invoice date to issue        2 days   <- internal
Issue to due date           30 days   <- terms
Due date to payment         13 days   <- collection
                            -------
                            52 days
```

**Nine of those days are entirely within the client's control and involve no customer conversation whatsoever.** Fixing them requires no negotiation, risks no relationship, and — per Step 8 — is the definition of a quick win. **It is also invisible in a DSO figure**, which is why Step 5's first AR lever is *invoice faster* and why it is so often skipped in favour of harder collections.

**Compute each stage from the transaction dates.** Where order dates are not recorded, say which stages are measurable and which are not.

---

### Step 3 — Diagnose: Inventory — where is it stuck?

**Conditional on Gate 2: `[auto]` where item-level data is exposed, `[manual]` where it is not.** All eight diagnostics preserved.

| Diagnostic | Verdict |
|---|---|
| **Inventory by category and location** | `[auto]` if item-level; **location is often not in the accounting system** |
| **Inventory turns by SKU / category** | `[auto]` if item-level |
| **ABC analysis** — A items (high value, tightly managed), B (medium), C (low value, sometimes overlooked) | `[auto]` if item-level |
| **Slow-moving** (>X days without movement) **and obsolete inventory** | `[auto]` if movement dates exist — **the highest-value inventory read** |
| **Excess against forecasted demand** | `[manual]` — **needs the forecast** |
| **Safety stock levels** — appropriate versus excessive | `[manual]` — appropriateness is a service-level judgment |
| **In-transit / work-in-process** | `[auto]` where accounted separately |
| **Supplier lead times and minimum order quantities** driving stock levels | **`[manual]`** — commercial terms, not ledger data |

**Root causes**, all six preserved: **forecasting errors (over-ordering); long supplier lead times forcing high safety stock; slow-moving SKUs not pruned; production batch sizes; service-level expectations; one-time buys and supplier discount-driven over-ordering.**

**Only the third is directly measurable.** The rest require the forecast, the supply agreements, or the operating policy — **so the inventory half of this skill is materially more manual than the AR and AP halves**, and the diagnostic depends on data that frequently lives outside the accounting system entirely.

**Say which, rather than producing a thin inventory section that looks like a complete one.** Note that **the slow-moving analysis feeds a provisioning question as well as a cash one.**

---

### Step 4 — Diagnose: AP — are we leaving cash on the table?

**`[auto]` for all five, and this is the fastest win in the skill.** From `ap-aging-and-payment-runs`.

| Diagnostic | Verdict |
|---|---|
| **Payment timing versus terms** — paying early (giving up float), on terms, or late | **`[auto]` — see below** |
| **Standard terms by vendor; recent vendor-by-vendor history** | **`[auto]`** for behaviour; `[manual]` for agreed terms |
| **Available early-payment discounts captured or not** | `[auto]` where discount terms are recorded |
| **Concentration on key vendors** — where payment behaviour most affects the relationship | **`[auto]`** — spend concentration |
| **Late-payment penalties incurred** | `[auto]` where charged and coded |

**Root causes**, all four preserved: **paying before terms (wastes float); inconsistent payment runs; inability to capture discounts (process or cash constraint); sub-optimal terms with key vendors.**

#### Paying early is the low-effort win, and it is one query

**`[auto]`. For every bill: days from invoice date to payment date, against the recorded terms.**

| Pattern | Meaning |
|---|---|
| **Paid materially before terms** | **Float given away for nothing.** No negotiation required to fix; no relationship consequence. |
| **Paid on terms** | Correct. |
| **Paid after terms** | Already stretching — **and Step 7's warning applies before recommending more.** |

**Quantify the early-payment population**: how many days early, on what value, and therefore what the cash is worth. **The source calls it "a common low-effort win" and it is** — the only change required is when the payment run executes.

**Two cautions.** Some early payments are **deliberate**, to capture a discount — which is correct, and Step 5's AP levers say so. **Check for a discount before flagging.** And some suppliers are on **direct debit or card**, where the timing is not the client's to choose.

**And the discount arithmetic, preserved**: **2/10 net 30 equates to a very high annualised return on holding cash; usually worth taking.** `[auto]` to compute discounts available against discounts captured — **and the gap is money that was on the table.**

---

### Step 5 — Identify levers per component

**`[manual]` to implement — every one of these is an operational or commercial decision.** `[auto]` to size, per Step 6, **with the asymmetry caveat.**

All twenty-five levers preserved.

**AR (reducing DSO)** — all nine:

| Lever | Note |
|---|---|
| **Invoice faster** | Shorten order-to-invoice; **same-day as shipment.** **Step 2's decomposition sizes this exactly, and it needs no customer conversation.** |
| **Invoice accurately** | Reduce disputes — correct pricing, PO match, billing detail. **A disputed invoice doesn't get paid.** |
| **Make it easy to pay** | Clear instructions, electronic methods, customer portal |
| **Terms** | Tighten where possible — shorter standard terms, deposits, progress billings, milestones |
| **Discounts for early payment** | Offer customer discounts — **cost versus cash benefit; calibrate** |
| **Collections rigor** | Structured sequence: **reminder before due date**, at due, past-due cadence. See `ar-aging-and-collections` |
| **Credit limits and customer risk** | **Stop extending credit to chronic slow payers.** A credit-limit review owns that decision |
| **Factoring / receivables financing** | **Convert AR to cash at a cost. Use selectively; not free.** |
| **Resolve disputes quickly** | A dedicated dispute resolution process |

**Note the first two are internal and risk-free; the fourth and seventh touch customers directly.** That distinction should drive the sequencing in Step 8, and it is not the same as the size of the prize.

**Inventory (reducing DIO)** — all ten: **improve forecasting; reduce lead times with key suppliers (closer suppliers, dual-source, contract terms); smaller and more frequent orders where supplier and logistics permit; SKU rationalisation — eliminate slow movers, consolidate similar SKUs; just-in-time / Kanban where appropriate; vendor-managed inventory (VMI); consignment — supplier ships but title transfers on use; liquidate obsolete inventory — even at a loss, it frees cash and stops carrying cost; tighter safety stock targets at appropriate service levels; faster production cycles to reduce WIP.**

**All `[manual]`.** These are supply chain and operations decisions, and **`[auto]` contributes only the sizing** — plus the slow-mover list that makes SKU rationalisation and liquidation concrete.

**AP (extending DPO judiciously)** — all six:

| Lever | Note |
|---|---|
| **Pay on terms, not earlier** | **A common low-effort win** — Step 4 quantifies it |
| **Renegotiate terms with key suppliers** | Longer terms **in exchange for volume, commitment, or a price concession** |
| **Supply chain financing / dynamic discounting** | Third-party programmes: suppliers paid earlier, buyer pays per extended terms. **Has a cost** — edge case 7 |
| **Centralise payment runs** | Consistent timing reduces ad hoc early payments |
| **Capture worthwhile discounts** | 2/10 net 30 typically yes; smaller discounts vary |
| **Do NOT simply stretch beyond terms without supplier agreement** | **Damages relationships, can affect supply, creates disputes** |

**The last row is a prohibition, not a lever**, and it is preserved as the source wrote it — in bold, as the thing not to do. **It is also the single easiest recommendation for a tool to generate**, because the arithmetic is identical to the legitimate levers and the ledger cannot see why it is different. **Never propose it.**

---

### Step 6 — Quantify and prioritise the opportunities

`[auto]` for two of the five; **`[manual]` for the three that matter most.** All five preserved.

| Criterion | Verdict |
|---|---|
| **Estimated days impact** (DSO/DIO/DPO change) | `[auto]` to model |
| **Dollar cash unlock** (days × daily volume) | **`[auto]`** |
| **Implementation effort and time** | `[manual]` |
| **Risk to customer / supplier relationships, operations or service** | **`[manual]` — and there is no ledger proxy for it** |
| **Net benefit prioritisation** | `[manual]`, informed by all four |

> **Build a ranked opportunity list. The biggest unlocks aren't always the highest-priority — relationship and operational risk matter.**

**Preserved, and it is the sentence that governs this step.** `[auto]` can rank by dollars, and **a ranking by dollars is not a priority list** — it is one input to one.

**Two Mosofin requirements for the opportunity sheet:**

**Every dollar figure sits beside a risk column with no number in it.** The asymmetry from the top of this file made structural: the benefit column is precise, the risk column is a description, and **the sheet must not let precision be mistaken for weight.**

**Internal levers are marked as internal.** Invoice faster, invoice accurately, pay on terms, centralise payment runs, capture discounts — **these require no counterparty conversation and carry no relationship risk.** They are a different class from renegotiating terms, and separating them makes the genuinely safe opportunities visible rather than buried in a list ranked by size.

---

### Step 7 — Address the trade-offs honestly

**`[manual]`, entirely — and it is the most important step in the skill.**

> **Working capital improvement has real trade-offs — be honest about them.**

All four preserved:

- **Stretching AP too far**: **damages supplier relationships, can lose preferred terms, can cause supply disruption, can result in COD-only terms — the reverse of the goal**
- **Tightening AR terms**: **can lose customers to competitors with looser terms; can damage relationships**
- **Cutting inventory too far**: **stockouts hurt sales and customer satisfaction; lost sales > inventory carrying cost**
- **Squeezing in a downturn**: **customers' financial stress can mean stretching AR; tightening collections then can accelerate customer failures or relationship damage**

> **The goal is optimisation, not maximisation. Define service-level and relationship guardrails. The "right" working capital level is the one that funds operations adequately without trapping cash unnecessarily — not zero.**

**Preserved in full and it is the skill's ethical core.**

**Why this step needs stating more forcefully in a connected version, not less.** Every trade-off above describes a cost that is **real, material, and entirely absent from the ledger.** Meanwhile the benefits are computed to the dollar. **A working capital analysis produced from live data is more persuasive and no better informed about the downside** — and persuasiveness without symmetry is how a company ends up on COD terms with its principal supplier.

**Three Mosofin additions to this step:**

- **The guardrails are named before the opportunities are sized**, not after. A guardrail introduced after a number has been presented rarely survives it.
- **Every recommendation touching a counterparty is marked as such**, and Step 6 separates them from the internal ones.
- **The fourth trade-off deserves a live check**: in a downturn, **`[auto]` can show whether customers' payment behaviour is deteriorating generally** — which is the signal that tightening collections would be pressing on businesses already under stress. **A general deterioration is a different situation from one slow payer**, and the response should differ.

---

### Step 8 — Build the implementation roadmap

`[manual]` for the plan; `[auto]` for sizing and baselines. All three horizons preserved.

- **Quick wins** — low effort, low risk, near-term: **enforcing payment on terms (not earlier); same-day invoicing; capturing existing early-payment discounts**
- **Medium-term** — process and system changes: **collections cadence, dispute process, demand planning, SKU rationalisation**
- **Longer-term** — negotiated changes: **renegotiating supplier and customer terms, supply chain financing, system investments**

**The three quick wins named in the source are exactly the three things Step 2 and Step 4 measure**, which is a useful convergence: **the fastest wins are also the ones the workspace sizes precisely and which carry no relationship risk.** Lead with them.

For each initiative, all five fields preserved: **owner; timeline; target metric and improvement; dependencies; KPI checkpoints.**

`[auto]` for the **baseline** of every target metric, so improvement is measured from a real starting point rather than an assumed one.

---

### Step 9 — Set KPIs and monitoring

**`[auto]` for six of the eight; `[manual]` for the two guardrails — which is itself the point.** All eight preserved.

| KPI | Verdict |
|---|---|
| **CCC and components (DSO/DIO/DPO) trending** | **`[auto]`** |
| **Ageing-bucket distribution** (AR and AP) | **`[auto]`** |
| **Inventory turns and slow-mover trends** | `[auto]` if item-level |
| **Discounts captured versus available** | `[auto]` |
| **Disputed invoice resolution time** | `[manual]` — dispute data |
| **Forecast accuracy** (driving inventory) | `[manual]` — needs the forecast |
| **Service-level / stockout rate** — **guardrail** | **`[manual]` — not in the accounting system** |
| **Supplier satisfaction / on-time payment %** — **guardrail** | **On-time payment % is `[auto]`; satisfaction is not** |

> **Integrate into `kpi-dashboard-builder` and `cash-flow-forecast-13-week` — the WC plan should reflect in the cash forecast.**

**Note what the verdicts say about the guardrails**, because it is the asymmetry appearing one final time: **the improvement metrics are automatic and the guardrails are not.**

A dashboard built only from what the workspace supplies will show DSO falling, DPO rising, and inventory turns improving — **and will show nothing about stockouts or supplier goodwill.** It will look like unambiguous progress right up until the point it is not.

**So the guardrail KPIs must be on the dashboard even though they must be entered by hand**, and **a guardrail with no data is reported as unmonitored, not as satisfied.** On-time payment percentage is the one guardrail that is automatic — use it, because it is the early warning on the supplier side.

---

### Step 10 — Output

An `.xlsx` working capital workbook. All ten of the original's sheets, plus two additions.

**Sheet 1: Executive Summary**
Current CCC and components, total opportunity in cash and days, top initiatives, **risks and guardrails.** **Guardrails appear on the same sheet as the opportunity**, not in an appendix. Header carries the fixture flag.

**Sheet 2: Cash Conversion Cycle Diagnostic**
Monthly DSO/DIO/DPO/CCC trend; component contribution; industry benchmarks. **`[auto]`, with the Step 1b decomposition** — volume, seasonality, deterioration — **and the DPO denominator stated.**

**Sheet 3: AR Diagnostic**
Ageing, by-customer DSO, dispute analysis, root causes. **With the DSO stage decomposition**, which is the sheet's most actionable content.

**Sheet 4: Inventory Diagnostic**
Turns by category and SKU, ABC analysis, slow-moving and obsolete, root causes. **Header states whether item-level data was available**; a value-only inventory section says so rather than presenting thin analysis as complete.

**Sheet 5: AP Diagnostic**
Payment timing versus terms, discounts available and captured, by-vendor, root causes. **With the early-payment population quantified.**

**Sheet 6: Lever-by-Lever Opportunity Sizing**
Each lever: estimated days and dollar impact, effort, risk, priority. **Internal levers separated from counterparty-facing ones. Risk column carries no number.**

**Sheet 7: Trade-Offs / Guardrails**
Customer, supplier and service-level constraints. **`[manual]`, and completed before Sheet 6 is presented.**

**Sheet 8: Implementation Roadmap**
Initiative, owner, timeline, target, dependencies, KPI checkpoints, **with `[auto]` baselines.**

**Sheet 9: KPI Dashboard**
Monitoring metrics with targets. **Guardrails present; unmonitored guardrails marked unmonitored.**

**Sheet 10: Cash Forecast Integration**
Expected improvement reflected in the 13-week and longer cash plan. See `cash-flow-forecast-13-week`.

**Sheet 11: Measured Baselines** *(Mosofin addition)*
Every measured series behind the diagnostic — monthly days by component, by-customer days-to-pay, by-vendor payment behaviour, stage decomposition — **with observation counts.** The evidence sheet that makes the rest defensible.

**Sheet 12: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Working_Capital_Optimization_[YYYY-MM]_[EntityName].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All twelve preserved.

- **CCC and components diagnosed with monthly trend and seasonality.** **`[auto]`**
- **Each component's opportunity quantified in days and dollars.** `[auto]`, **with the risk column carrying no number.**
- **Root causes identified, not just symptoms.** `[auto]` for the measurable ones — **especially the DSO stage decomposition**; `[manual]` for the rest.
- **Lever inventory complete per component.** All twenty-five, `[manual]` to implement.
- **Opportunities ranked by net benefit** — size × feasibility × risk. **`[auto]` for size only.**
- **Trade-offs and guardrails explicit.** `[manual]`, **and completed before the opportunities are presented.**
- **Roadmap sequenced with owners, timelines and KPI checkpoints.** `[manual]`, `[auto]` baselines.
- **KPIs include both improvement metrics and relationship/service guardrails.** **`[auto]` for the improvement metrics; the guardrails are not, and unmonitored ones are marked unmonitored.**
- **Integration with cash forecast and dashboard.** `[auto]`
- **Honest about trade-offs — no "free lunch" framing of supplier stretching.** **`[manual]`, and the standard that governs the rest.**
- **File naming consistent.** `[auto]`
- **Goal framed as optimisation, not maximisation.** `[manual]`

**Five Mosofin additions:**

- **Balance movements are decomposed** into volume, seasonality and deterioration.
- **DSO is decomposed by stage**, so internal delay is visible and separable.
- **Early payment is quantified**, since it is float given away for nothing.
- **Internal levers are separated from counterparty-facing ones.**
- **The benefit/cost asymmetry is stated on the opportunity sheet**, not assumed understood.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and any benchmark or days target.**

**What is worth persisting into the workspace-scoped skill:**

1. **The measured baseline** — every series in Sheet 11, with the date. **The roadmap's progress is measured against it**, and a baseline that shifts makes improvement unprovable.
2. **The driver definitions and days convention**, shared with any financial model, scenario analysis or rolling forecast built on the same books — **they must agree**, or the working capital plan will not reconcile to the forecast that reflects it.
3. **The guardrails**, once defined — service levels, untouchable relationships, minimum stock commitments.
4. **Agreed terms by customer and supplier**, since recorded terms and agreed terms differ and the comparison is the diagnostic.
5. **Suppliers on direct debit or card**, so their timing is not flagged as early payment.
6. **Levers already declined and why** — a client who has explained that a key supplier will not renegotiate should not be shown it again.
7. **Seasonality indices**, refreshed as history lengthens.
8. **The initiative list with owners and baselines**, so each period reports movement rather than restating the diagnosis.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — this analysis names slow-paying customers and suppliers whose terms are targets.

**The evolved version reports movement against baseline**, not a fresh diagnosis: which days moved, whether it was volume or behaviour, which initiatives are on track, and whether any guardrail has been breached.

---

## Anti-patterns

- **Presenting a computed cash unlock next to an unquantified risk** as though they were comparable. They are not, and the precision is on the wrong side.
- **Recommending stretching payables beyond terms.** The source forbids it and the ledger cannot see the cost.
- **Ranking opportunities by dollars and calling it a priority list.**
- **Reading rising working capital as inefficiency** in a growing business.
- **Using a period-end snapshot.** It is the least representative point in the month.
- **Treating a quarter-end collection push as an improvement.**
- **Reporting a mean DSO** over a concentrated, skewed customer base.
- **Chasing collections harder in a general downturn** without checking whether the deterioration is systemic.
- **Cutting inventory without a service-level guardrail.** The cost of a stockout is invisible in the financials.
- **Flagging deliberate discount-capturing early payments** as float given away.
- **Presenting factoring as free cash.** It is financing with a rate.
- **Using a generic industry benchmark.** Worse than none.
- **A dashboard of improvement metrics with no guardrails**, because only the improvement metrics are automatic.
- **Paying a fragile sole-source supplier later** because the metric says so.
- **Skipping the DSO decomposition.** Nine days of internal delay need no negotiation and are invisible in the headline figure.
- **Saying "implemented".** Mosofin analyses; people change terms and processes.
