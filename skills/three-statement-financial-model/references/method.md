<!-- three-statement-financial-model · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Architect the model
- Step 2 — Build the income statement
- Step 3 — Build the supporting schedules
- Step 3b — Measure the drivers before assuming them *(Mosofin addition)*
- Step 4 — Build the cash flow statement (the integrator)
- Step 5 — Build the balance sheet and make it balance
- Step 6 — Resolve circularity (if any)
- Step 7 — Add outputs and checks
- Step 8 — Scenarios and sensitivity
- Step 9 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

This skill uses the refinement introduced in `recurring-transaction-builder`, because a large block of the work needs no ledger:

- **`[auto: computed]`** — model construction and arithmetic. Works with no datasource connected.
- **`[auto: read]`** — requires a live read: the historical base and the measured drivers.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a model.** The gateway is read-only. Mosofin posts nothing and forecasts nothing on its own authority.

---

## Inputs

All ten preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Historical financials (3 statements)** | At least 1–2 years for a base | **Required** | **Live read, exact, and as long a history as exists** | **`[auto: read]`** |
| **Forecast horizon** | Years/months | **Required** | Not in the books | `[manual]` |
| **Operating assumptions / drivers** | Revenue, margins, opex, working capital terms | **Required** | **Historical values measurable; forward values not** | Split |
| **Capex plan** | By period | **Required** | **A plan. Not in the books.** | `[manual]` |
| **Depreciation policy** | Per `fixed-asset-register-and-depreciation` | **Required** | **Depreciation on existing assets is already determined** | `[auto: read]` in part |
| **Debt schedule** | Existing debt, planned issuances/repayments, rates | **Required if debt exists** | **Opening balance is a fact; terms are in the agreements** | Split |
| Equity transactions | Raises, buybacks, dividends | Recommended | Historical readable; planned not | Split |
| **Tax rate / approach** | Effective rate or detailed | **Required** | **Realised effective rate computable** | `[auto: read]` in part |
| **Working capital assumptions** | DSO, DPO, DIO | **Required** | **All three measurable, per period, across the history** | **`[auto: read]`** |
| **Functional currency** | ISO code | **Required** | Company record | `[auto: read]` |

---

## Workflow

### Step 1 — Architect the model

**`[auto: computed]`.** All four components preserved.

> **A well-built model separates inputs, calculations and outputs.**

- **Assumptions / Drivers tab**: **every input the user can change, in one place, clearly labelled. No hardcoded numbers buried in formulas.**
- **Supporting schedules**: working capital, debt, PP&E and depreciation, equity, tax — each builds the detail.
- **Three statements**: IS, BS, CF — **driven entirely by the schedules and assumptions, no manual entry.**
- **Outputs / Dashboard**: key metrics, ratios, charts.

> **Colour convention (standard modelling practice): blue for inputs, black for formulas, green for links across tabs. Document the convention.**

**One Mosofin addition to the convention**, and it earns its place: **a fourth colour, or a marker, for inputs that were measured from the ledger rather than assumed.** A reader — and a diligence team especially — should be able to see at a glance which blue cells are somebody's judgment and which are the client's own history. **They carry very different evidential weight**, and a convention that treats them identically hides the model's strongest feature.

Document it on the cover tab alongside the standard three.

---

### Step 2 — Build the income statement

`[auto: computed]` for the structure; **`[auto: read]` for the historical columns**; `[manual]` for the forward drivers.

```
Revenue (from driver model)
- COGS (from margin or unit-cost assumptions)
= Gross profit
- Operating expenses (by category, driver-based)
= EBITDA
- Depreciation & amortization (from the PP&E and intangibles schedules)
= EBIT
- Interest expense (from the debt schedule)
+ Interest income (from cash balance x rate)
= Pre-tax income
- Income tax (from the tax schedule / effective rate)
= Net income
```

Link to `budget-builder` logic for the operating build.

**Note the two lines that create the circularity** — interest expense and interest income both depend on balances that depend on net income. Step 6 handles it, and the fact that it originates here is worth knowing when debugging.

---

### Step 3 — Build the supporting schedules

All five preserved, each with its verdict.

**Working capital schedule** — `[auto: computed]` structure, **`[auto: read]` drivers:**
```
Accounts Receivable = Revenue x (DSO / days in period)
Inventory           = COGS x (DIO / days in period)
Accounts Payable    = COGS x (DPO / days in period)
Other working capital items per assumptions
Change in net working capital flows to the cash flow statement
```

**PP&E and depreciation schedule** — `[auto: read]` for the opening position and committed depreciation, `[manual]` for capex:
```
Opening PP&E (gross)
+ Capex (from assumptions)
- Disposals
= Closing PP&E (gross)

Depreciation: per policy
Accumulated depreciation rolls forward
Net PP&E = gross - accumulated depreciation -> to balance sheet
Capex -> cash flow investing; depreciation -> income statement
```

**Depreciation splits into two parts and only one is an assumption**: depreciation on **assets already owned** is determined by the existing register and is a fact for the whole forecast horizon; depreciation on **planned capex** is a forecast. Model them separately. See `fixed-asset-register-and-depreciation`.

**Debt schedule** — `[auto: read]` opening, `[manual]` terms:
```
Opening debt
+ New borrowings (from assumptions)
- Repayments (scheduled amortization + optional prepayments)
= Closing debt
Interest expense = average (or opening) balance x interest rate -> income statement
Principal movements -> cash flow financing
```

> **Include a revolver / cash-sweep mechanism** if modelling a financing where excess cash pays down debt or a shortfall draws the revolver. **This is what makes the BS balance — the revolver is often the "plug".**

**The word "plug" here is doing something different from the prohibited plug in the quality standards, and the distinction matters.** A revolver is a **modelled financing response** — an economic mechanism with a real-world counterpart, drawing when cash is short and repaying when it is not. **A hardcoded plug is a number typed in to force a tie.** The first is correct modelling; the second is the thing edge case 11 forbids. **Both are called plugs and they are opposites.**

**Equity schedule** — `[auto: read]` historical, `[manual]` planned:
```
Opening equity
+ Net income (from income statement)
+ Equity raises
- Buybacks
- Dividends
+/- OCI
= Closing equity -> balance sheet
```

**Tax schedule:**
- **Simple**: effective rate × pre-tax income — `[auto: read]` for the **realised** effective rate as the starting evidence
- **Detailed**: book-tax differences, deferred taxes — `[manual]`; link to the tax provision work

**State which.** And note from the corporate tax return preparation: **the realised effective rate embeds this year's particular adjustments**, so it is evidence for the assumption rather than the assumption itself.

---

### Step 3b — Measure the drivers before assuming them *(Mosofin addition)*

**`[auto: read]`. The contribution that changes the model's quality rather than its speed.**

For each driver the model needs, compute from the full available history:

| Driver | Measured as | Why it matters |
|---|---|---|
| **DSO** | Receivables ÷ revenue × days, per period | A required input. **Its realised range is the honest basis for the assumption.** |
| **DPO** | Payables ÷ COGS × days, per period | Same — and **a DPO assumption above the realised range is an assumption that the business will start paying suppliers later**, which is a decision, not a forecast. |
| **DIO** | Inventory ÷ COGS × days, per period | Same. |
| **Gross margin** | Per period | The range and the trend. |
| **Opex as % of revenue**, by category | Per period | Shows which costs actually flex with revenue and which do not — **frequently different from how the model assumes they behave.** |
| **Effective tax rate** | Tax ÷ pre-tax income, per period | Starting evidence for the tax assumption. |
| **Capex as % of revenue** | Per period | A sanity check on the capex plan. |

**Report for each: the range, the median, the trend, and the number of periods observed.** Then set the assumption **beside** the measurement on the assumptions tab, so the two are visible together.

**Why this is worth doing properly.** A model's assumptions are the first thing a diligence team attacks, and *"we assumed 45 days"* is a much weaker answer than *"the business has run between 38 and 52 days over three years, averaging 44; we assumed 45."* **The second answer is available for free whenever the workspace is connected**, and the difference is entirely in whether anyone looked.

**Two cautions.** **Historical volatility is not future risk** — the same warning `scenario-and-sensitivity-analysis` carries; the measured range is evidence about the driver, not a guarantee. And **a deliberate departure from history is legitimate and often the whole point of the plan** — a business intending to improve collections *should* model a lower DSO. **The requirement is that the departure be visible and deliberate**, not that it be avoided.

---

### Step 4 — Build the cash flow statement (the integrator)

`[auto: computed]`. Indirect method, per `cash-flow-statement-indirect-method`.

```
Operating:
  Net income (from IS)
  + D&A (from schedules)
  +/- changes in working capital (from WC schedule)
  + other non-cash
Investing:
  - Capex (from PP&E schedule)
  +/- other investing
Financing:
  +/- debt movements (from debt schedule)
  +/- equity movements (from equity schedule)
  - dividends
= Net change in cash
Ending cash = Beginning cash + net change -> to balance sheet
```

> **The cash flow statement links the IS and BS.**

**It is the integrator, and it is where linking errors concentrate**, because every line comes from somewhere else. When the balance check fails, this is the first place to look — a working capital movement with the wrong sign is the classic cause and it is easy to make.

---

### Step 5 — Build the balance sheet and make it balance

`[auto: computed]` for the structure; **`[auto: read]` for the opening balance sheet.**

```
ASSETS
  Cash (from cash flow statement ending cash)
  AR (from WC schedule)
  Inventory (from WC schedule)
  Other current assets
  Net PP&E (from PP&E schedule)
  Intangibles, goodwill
  Other assets
LIABILITIES
  AP (from WC schedule)
  Accrued liabilities
  Debt (from debt schedule)
  Other liabilities
EQUITY
  (from equity schedule)
```

> **The balance check**: **Total Assets − (Total Liabilities + Total Equity) must equal zero in every period. Build an explicit balance check row.** If it is non-zero, **the model has an error** — usually a cash flow item not linked, a schedule not flowing, or double-counting.
>
> **The cash balance and the revolver / cash-sweep are what make it balance**: if everything else is linked correctly, cash is the residual that makes Assets = Liabilities + Equity.

**Preserved in full — and read the inversion at the top of this file before interpreting the result.**

**In the forecast columns this is a real test.** There is no double entry in a spreadsheet; the model balances only because the links are right, and a failure points to a specific, findable error.

**In the historical columns it is guaranteed**, because those figures came from a ledger that could not have produced anything else.

**So `[auto: read]` adds a specific check the original does not have: verify the historical columns against the ledger, not against themselves.** The historical balance sheet will balance regardless; **what matters is whether it is the client's actual balance sheet.** Compare line by line to the source. A model whose history has been re-keyed, rounded, reclassified or pulled from a different period will balance perfectly and be built on the wrong foundation.

**And check the transition period first.** The boundary between the last actual and the first forecast is where two construction methods meet, and it is the single most common location for a linking error.

---

### Step 6 — Resolve circularity (if any)

**`[manual]` — a design decision.** All three options preserved.

> **A common circularity: interest expense depends on the debt/cash balance, which depends on net income, which depends on interest expense.**

| Option | Note |
|---|---|
| **Enable iterative calculation** (Excel setting) | **Document it and use with care** — it can converge to different answers, or not converge at all |
| **Use opening balances for interest** | **Breaks the circularity cleanly — often preferred** |
| **Build a circularity switch to toggle** | Lets the model be tested both ways |

> **State which approach is used.**

**And carry across the warning from `scenario-and-sensitivity-analysis`**, because it is the practical consequence: **a model that converges at the base case can oscillate or fail at the extremes of a scenario range.** If the model will be flexed — and Step 8 says it will — **the circularity handling must be stable across the whole range**, not just at base. Test it there, not only at the centre.

---

### Step 7 — Add outputs and checks

`[auto: computed]`, with `[auto: read]` historical comparatives.

**Key metrics** — all nine preserved: **revenue growth, gross / EBITDA / net margins, FCF, FCF conversion, ROE, ROIC, leverage (debt/EBITDA), interest coverage, working capital days.**

**`[auto: read]` addition worth making**: show **the historical value of every metric alongside the forecast.** A model projecting an ROIC the business has never come close to achieving is making a claim, and the claim is much more visible when the history sits next to it.

**Model integrity checks** — all six preserved, all `[auto: computed]`, each showing PASS/FAIL:

| Check | Note |
|---|---|
| **Balance sheet balances (every period)** | **Real in forecast columns, guaranteed in historical ones** |
| **Cash flow ending cash = balance sheet cash** | A genuine link test |
| **Net income IS = net income in equity roll** | A genuine link test |
| **Retained earnings ties** | Genuine |
| **No #REF or #DIV/0 errors** | Mechanical, and worth automating because they hide |
| **Sources = uses** | Genuine |

**Two Mosofin additions to the checks:**

- **Historical columns agree with the ledger**, line by line — **the check that the guaranteed balance check cannot perform.**
- **Every assumption is on the assumptions tab**, with no constant embedded in a statement formula. This is the mechanical half of the "no hardcoded forecast figures" standard.

**And note what the check block does and does not do**: **all six checks can pass on a model whose assumptions are nonsense.** They test construction. Step 3b and the historical comparatives are what test plausibility.

---

### Step 8 — Scenarios and sensitivity

`[auto: computed]` for the structure; `[manual]` for the scenarios.

> **Build the model so key drivers can flex; hand off scenario and sensitivity structure to `scenario-and-sensitivity-analysis`. At minimum, allow toggling between base, upside and downside assumption sets.**

**`[auto: read]` feeds directly into that handoff**: the measured driver ranges from Step 3b are exactly the grounded ranges that skill needs, and passing them through means the sensitivity is built on observed variability rather than a mechanical ±10%. **The two skills share the same measurement**, and doing it once is better than doing it twice differently.

**And build the model to be flexed**, which means: no assumption buried in a formula, every driver on one tab, and the circularity stable across the range.

---

### Step 9 — Output

An `.xlsx` workbook. All the original's tabs preserved, plus two additions.

**Tab 1: Cover / Instructions** — colour conventions **including the measured-input marker**, how to use, key switches, **the circularity approach**, and the fixture flag.

**Tab 2: Assumptions / Drivers** — **every input in one place.** **Measured values shown beside assumed ones**, with range, median, trend and observation count.

**Tab 3: Income Statement** — historical and forecast, **visibly distinguished.**

**Tab 4: Balance Sheet** — **with the balance check row**, and the historical columns marked as guaranteed.

**Tab 5: Cash Flow Statement**

**Tab 6+: Supporting Schedules** — working capital, PP&E and depreciation, debt, equity, tax. **Committed depreciation shown separately from capex depreciation.**

**Tab: Outputs / Dashboard** — metrics and ratios, **each with its historical value alongside.**

**Tab: Checks** — all integrity checks, each **PASS/FAIL**, including the two Mosofin additions.

**Tab: Driver History** *(Mosofin addition)* — the Step 3b measurements in full, with the series behind each so a reader can see the shape rather than trust a summary.

**Tab: Coverage and Provenance** *(Mosofin addition)* — the mandatory coverage sheet.

> **Build everything with live formulas and cross-tab links — no hardcoded forecast numbers in the statements.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `3Statement_Model_[EntityName]_[YYYY-MM-DD].xlsx`

Entity `display_name` on the cover and every statement tab. If any read returned `mock: true`, say so in the file name and on the cover.

---

## Output Quality Standards

All ten preserved.

- **Balance sheet balances in every period** — explicit check row = 0. **`[auto: computed]`, real in the forecast columns.**
- **Cash flow ending cash = balance sheet cash.** `[auto: computed]`
- **All three statements linked by formula; no hardcoded forecast figures in the statements.** `[auto: computed]` to enforce.
- **Assumptions isolated on one tab; colour conventions applied.** `[auto: computed]`, **with measured inputs distinguished from assumed ones.**
- **Supporting schedules drive the statements.** `[auto: computed]`
- **Circularity handled explicitly with a documented method.** `[manual]`, **and stable across the scenario range.**
- **Revolver / cash-sweep mechanism keeps cash plausible.** `[auto: computed]`, with a **realistic** minimum and an **existing** facility.
- **Integrity checks built in and passing.** `[auto: computed]` — **and they test construction, not plausibility.**
- **File naming consistent.** `[auto: computed]`
- **No balance-sheet plug to force the tie.** **`[auto: computed]` to detect.**

**Five Mosofin additions:**

- **The historical base is verified against the ledger**, not merely against itself.
- **Every measurable driver is measured**, and the measurement sits beside the assumption.
- **Departures from history are visible and deliberate**, not accidental.
- **Committed depreciation is separated from capex depreciation.**
- **The transition period is checked first**, being where linking errors concentrate.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and any driver value.** A DSO measured last year is last year's DSO, and the entire argument for measuring is that it reflects this business now.

**What is worth persisting into the workspace-scoped skill:**

1. **The account-to-line mapping** — which chart accounts feed which statement line. Established once; every subsequent model builds its historical base automatically.
2. **The driver definitions** — which accounts constitute each measured driver, and the days convention used. Shared with `scenario-and-sensitivity-analysis` and `rolling-forecast`, and they must agree.
3. **The model architecture** agreed with the client — horizon, granularity, level of tax detail, whether leases are modelled.
4. **The circularity method.**
5. **Assumptions previously set and the reasoning where they departed from history**, so a deliberate improvement plan is not re-flagged as an anomaly every quarter.
6. **Facilities that actually exist**, and their limits.
7. **Whether the balance sheet is dimensioned** for entity-level work.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — a financial model is among the most commercially sensitive documents a business produces.

**Persist the method and the mapping; re-measure the values.** Every run has more history than the last.

---

## Anti-patterns

- **Assuming a driver the client's own history could have measured.** It is the easiest thing for a diligence team to take apart.
- **Reading the historical balance check as validation.** Those columns inherit double entry; only the forecast columns test anything.
- **Skipping the check that the historical columns match the ledger.** They will balance whether or not they are the right numbers.
- **Testing the balance check only at the base case.** Test the transition period, and test the extremes.
- **Confusing a revolver with a plug.** One is a modelled mechanism; the other is a typed number.
- **Plugging the balance sheet.** If it does not balance, there is an error and it is findable.
- **Treating passing integrity checks as a validated model.** They test construction, not assumptions.
- **Depreciating the existing asset base as an assumption.** It is already determined.
- **Assuming a facility the company does not have.**
- **A round-number cash floor** when the business's actual minimum is known.
- **An annual model in a seasonal business.** Peak working capital determines the facility needed.
- **Omitting leases.** It understates assets and debt, and leverage is what a lender reads first.
- **Summing group entities without eliminations**, then compounding it forward.
- **Claiming to audit an existing model.** Mosofin cannot read a workbook's formulas.
- **Burying an assumption in a statement formula.**
