<!-- valuation-agent-dcf-comps-football-field · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Anchor the valuation
- Step 2 — Build the DCF
- Step 3 — Make WACC visible and editable
- Step 4 — Calculate terminal value
- Step 5 — Build comparable screens
- Step 6 — Build the football field
- Step 6b — The bridge, which is where the workspace earns its place *(Mosofin addition)*
- Step 7 — Deliver the valuation package
- Quality Bar
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is analysis.** The gateway is read-only. **Mosofin posts nothing and issues no opinion of value.**

---

## Inputs

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Forecast model or forecast financials** | Integrated model / XLSX / CSV | Required | **Not in the books.** An assertion about the future. **Its history is tie-backable.** | `[manual]`, `[auto]` to tie back |
| **Valuation date** | Date | Required | Not in the books; **it selects which balance sheet to read** | `[manual]` |
| **Purpose of valuation** | M&A / fundraising / board / internal planning / financial reporting / tax | Required | Not in the books; **determines whether a specialist is required** | `[manual]` |
| **Company profile** | Industry, geography, revenue model, size, growth, margin, stage | Required | **Size, growth and margin measurable; the rest is not** | Split |
| **Net debt and equity bridge items** | Debt, cash, leases, preferred stock, minority interest, options, warrants | Required | **Mostly `[auto]` — see Step 6b. Options and warrants are not.** | **Mostly `[auto]`** |
| **WACC inputs** | Risk-free rate, ERP, beta, target capital structure, cost of debt, tax rate | Required for DCF | **Market data — not on this surface.** Actual cost of debt is readable. | `[manual]`, `[auto]` in part |
| **Comparable universe** | User-provided list or screen criteria | Required for comps | **Not on this surface.** | `[manual]` |
| Transaction universe | User-provided list or screen criteria | Recommended | **Not on this surface.** | `[manual]` |

> **For current market prices, rates, betas, or public comparable data, verify with current external sources before finalising if browsing or data access is available. If current data cannot be verified, label it as user-provided or placeholder.**

**Preserved exactly, and it is the right instinct** — the same family as the no-hardcoding rules in the tax skills. **Market data is dated data**, and a beta or a risk-free rate carried over from a previous engagement is wrong in a way nobody will notice.

---

## Workflow

### Step 1 — Anchor the valuation

`[manual]` for the anchoring decisions; **`[auto]` for one thing that matters.**

Document all seven:

- **Valuation date**
- **Purpose and audience**
- **Entity being valued**
- **Enterprise value versus equity value basis**
- **Currency and units**
- **Forecast source used**
- **Whether assumptions are management-provided, market-derived, or analyst-selected**

> **The valuation date controls market data. Do not mix market data from different dates without flagging it.**

**Preserved — and the same rule applies to the balance sheet.** `[auto]`: **read the balance sheet at the valuation date, not at the most recent period end.** The two are frequently different, and a bridge built on a period end three months after the valuation date imports a quarter of cash generation, debt repayment and working capital movement that did not exist at the date being valued.

Where the valuation date is not a period end, **say what basis was used** — the nearest close, or a computed position — because the bridge's precision claim depends on it.

**The seventh item deserves emphasis**, because it is the one that makes a valuation reviewable: **labelling each assumption as management's, the market's, or the analyst's.** A reader assessing a valuation needs to know whose judgment each number represents. **Mosofin adds a fourth label — measured from the accounts** — for the bridge components and the historical evidence, which carry different weight again.

---

### Step 2 — Build the DCF

**`[auto: computed]` arithmetic; `[manual]` for the forecast; `[auto]` for the tie-backs.**

Start from forecast operating results and calculate unlevered free cash flow:

```
EBIT
- Cash taxes on EBIT
= NOPAT
+ D&A and other noncash charges
- Capital expenditures
- Change in net working capital
= Unlevered free cash flow
```

> **Tie DCF cash flows back to the model.**

All five tie-backs preserved:

| Tie-back | Verdict |
|---|---|
| **EBIT ties to forecast P&L** | `[auto: computed]` |
| **D&A ties to the fixed asset schedule or P&L support** | `[auto: computed]` |
| **Capex ties to the capex schedule** | `[auto: computed]` |
| **Working capital ties to forecast balance sheet movements** | `[auto: computed]` |
| **Tax rate ties to the tax assumptions** | `[auto: computed]` — **and see the near-substitute on which rate** |

> **If the model is levered-only, convert to unlevered cash flows before applying WACC.**

**Preserved, and it is a real error when missed**: discounting levered cash flows at WACC double-counts the financing benefit, because WACC already reflects the capital structure. **The result is an overvaluation, and it looks entirely normal.**

#### Step 2b — Tie the model's history to the accounts *(Mosofin addition)*

`[auto]`, and it is the tie-back the original does not have.

The five tie-backs above check the DCF against **the model.** **None of them check the model against reality.**

> **A DCF that ties perfectly to a model whose historical columns do not match the accounts is precisely consistent with the wrong numbers.**

So: **read the actual historical results and balance sheet, and compare them line by line to the model's historical columns.** This is the check `three-statement-financial-model` builds in, and it matters more here because a valuation is what the model is *for* — and because **a diligence team will run exactly this comparison**, usually as their first substantive step.

Report differences with amounts. **Re-keyed, rounded, reclassified or wrong-period history is common** and it is far better found now.

#### Step 2c — Evidence the cash flow assumptions *(Mosofin addition)*

`[auto]`. Every line of the UFCF build has a measurable history:

| Line | Historical evidence |
|---|---|
| **EBIT margin** | The realised range, per period, with its trend |
| **Cash taxes** | The realised effective rate — **as evidence, not as the rate** |
| **D&A** | Historical D&A, **and the portion already committed** on assets owned |
| **Capex** | **Capex as a percentage of revenue, historically** — the single best sanity check on a capex forecast |
| **Change in net working capital** | **DSO, DPO, DIO** and the resulting working capital movement per period |

**Present the assumption beside the history.** A forecast assuming capex at 2% of revenue, in a business that has run at 6% for four years, is making a claim about a change in capital intensity — **which may be entirely right, and needs to be visible and deliberate.** Terminal value in particular is highly sensitive to the assumed steady-state capex and working capital, and **a terminal year that quietly assumes better economics than the business has ever achieved is where DCFs most often inflate.**

Shared with `scenario-and-sensitivity-analysis` and `three-statement-financial-model` — **and the three should use the same measurements**, or the valuation will not reconcile to the model it came from.

---

### Step 3 — Make WACC visible and editable

**`[manual]` for the inputs — market data is not on this surface.**

Show each component separately. All seven preserved:

| Component | Verdict |
|---|---|
| **Risk-free rate** | `[manual]` — market |
| **Equity risk premium** | `[manual]` — market |
| **Beta, or unlevered/relevered beta** | `[manual]` — market, and it requires comparables |
| **Size, country or company-specific risk adjustments if used** | `[manual]` — **and explicitly judgment** |
| **Pre-tax cost of debt** | `[manual]` for the market rate — **`[auto]` for the actual rate the company pays**, which is evidence |
| **Tax rate** | `[manual]`, with `[auto]` evidence |
| **Target debt/equity capital structure** | `[manual]` for target; **`[auto]` for the actual current structure** |

```
WACC = Cost of Equity x Equity Weight + After-Tax Cost of Debt x Debt Weight
```

> **Use source notes for every market-derived input. If an input is a judgment call, label it as judgment.**

**Preserved, and it is the discipline that distinguishes a defensible WACC from a plausible one.** The company-specific risk premium in particular is pure judgment, frequently sizeable, and frequently presented without acknowledgement.

**`[auto]` supplies two reality checks**, both worth showing beside the assumptions:

- **The actual pre-tax cost of debt** — interest expense over average debt. Where the target cost of debt differs materially from what the company actually pays, that difference is an assumption about future financing and should be stated as one.
- **The actual capital structure** at the valuation date, from the bridge. **A target structure far from the actual one is a claim about recapitalisation**, and it changes the WACC materially.

---

### Step 4 — Calculate terminal value

`[auto: computed]` arithmetic; `[manual]` for the inputs; **`[auto]` for two of the three sanity checks.**

Both methods preserved:

- **Gordon growth method**: `final year FCF x (1 + g) / (WACC - g)`
- **Exit multiple method**: `terminal metric x selected exit multiple`

> **Keep terminal growth rate, exit multiple and terminal year metric visible.**

**Sanity checks**, all three preserved:

| Check | Verdict |
|---|---|
| **Terminal growth should not exceed long-term sustainable growth without clear rationale** | `[manual]` — **a macroeconomic judgment.** A perpetual growth rate above long-run economic growth implies the business eventually becomes the economy. |
| **Exit multiple should be consistent with comps and the forecast margin/growth profile** | `[manual]` for the comps side; **`[auto]` for the forecast profile side** — is the terminal year's margin and growth consistent with the business's history? |
| **Terminal value as a percentage of enterprise value should be reviewed for reasonableness** | **`[auto: computed]`** |

**The third check deserves emphasis**, because it is the one most often computed and least often acted on. **Terminal value routinely represents 60–80% of a DCF's enterprise value**, which means the valuation is mostly a statement about a single growth rate or multiple applied to a single year — and the elaborate explicit forecast period contributes the minority of the answer.

**Compute and display the percentage.** Where it is very high, **that is not necessarily wrong** — it is normal for a growing business — but it tells the reader where to concentrate their scepticism, and it makes the sensitivity analysis in the deliverable the main event rather than an appendix.

**`[auto]` addition worth making**: **an implied exit multiple from the Gordon growth result, and an implied growth rate from the exit multiple result.** Running both methods and cross-checking them is standard practice; **making each method state what the other would have to assume** is the quickest way to see when one of them is out of line.

---

### Step 5 — Build comparable screens

**`[manual]`. Comparables are public company financials and deal data, and they are not on this surface.**

**For trading comps**, screen by all eight: **industry and business model; geography; scale; growth; margin profile; revenue quality; capital intensity; profitability.**

**For transaction comps**, also consider all six: **transaction date; control premium; deal size; buyer type; strategic fit; market cycle.**

**Calculate relevant multiples** — EV/Revenue, EV/EBITDA, EV/EBIT, P/E, ARR multiple, gross profit multiple, or industry-specific KPIs.

> **Exclude outliers only with an explicit rationale.**

**Preserved, and it is the standard that protects a comps analysis from being an argument dressed as evidence.** Screening decisions determine the answer, and an unexplained exclusion is an assumption.

**`[auto]` contributes only one thing, and it contributes it to the screen rather than the comparables**: **the subject company's own position on the screening dimensions** — its scale, growth, margin profile, capital intensity and profitability, measured rather than asserted. **A comps set is only comparable to something**, and the something should be a measured profile rather than a description.

**Note also from `quarter-end-close` and `segment-reporting`**: **ARR is a contract metric, not a ledger metric.** Where an ARR multiple is used, the ARR is `[manual]`.

---

### Step 6 — Build the football field

`[auto: computed]` for the layout; inputs vary by method. All six methods preserved:

- **DCF low/base/high or sensitivity range** — `[auto: computed]` from Steps 2–4
- **Trading comps** — `[manual]`
- **Precedent transactions** — `[manual]`
- **Broker or analyst targets, if relevant and sourced** — `[manual]`
- **Recent financing rounds, if relevant** — `[manual]`; and **note these value a specific security with specific rights**, not necessarily the whole equity
- **Other method only when defensible** — `[manual]`

> **Show enterprise value ranges and bridge to equity value.**

```
Enterprise Value
- Debt and debt-like items
+ Cash and cash-like items
- Preferred equity / minority interest / other claims
= Equity Value
/ Diluted shares
= Value per share
```

---

### Step 6b — The bridge, which is where the workspace earns its place *(Mosofin addition)*

**`[auto]` for most of it — and this is the highest-value automatic work in the skill.**

**A bridge looks like arithmetic and behaves like analysis.** Every line is a judgment about what counts as debt-like, and getting one wrong moves equity value directly, one-for-one.

| Bridge component | Mosofin | Note |
|---|---|---|
| **Bank and other borrowings** | **`[auto]`** | Straightforward. |
| **Lease liabilities** | **`[auto]` — and the one most often omitted** | See below. |
| **Cash and equivalents** | **`[auto]`** | And see the restricted-cash point. |
| **Preferred equity** | `[auto]` where on the balance sheet | |
| **Minority interest** | `[auto]` where consolidated | |
| **Debt-like items** — pension deficits, deferred consideration, unfunded obligations, factored receivables with recourse, overdue tax and payables beyond normal terms | **`[auto]` to surface candidates** | See below. |
| **Cash-like items** — surplus assets, tax refunds due, non-operating investments | `[auto]` to surface candidates | |
| **Options and warrants** | **`[manual]` — no cap table on this surface** | |
| **Diluted shares** | **`[manual]` — no cap table on this surface** | |

#### The lease liability point

**Under ASC 842 and IFRS 16, operating leases sit on the balance sheet as a lease liability. They are debt.**

Many practitioners' net debt definitions predate those standards, or were learned from templates that do. **A bridge omitting lease liabilities overstates equity value by their whole amount** — and for a retailer, a restaurant group or a logistics business that can be a very large number.

**`[auto]` reads the lease liability directly.** Report it as a distinct line rather than folding it into borrowings, so the treatment is visible and the reader can see it was considered.

**Two related consistency points, both `[manual]` to decide:** if lease liabilities are included in net debt, then **EBITDA should be pre-IFRS 16 EBITDA** (or the multiple must be applied consistently), and **the comparables must be on the same basis.** Mixing an IFRS 16 EBITDA with a net debt excluding leases, or a multiple derived from comparables on a different basis, produces an error in the same direction twice. **Flag the basis; do not resolve it silently.** See `lease-accounting-asc842-ifrs16`.

#### The debt-like sweep

`[auto]` to surface, `[manual]` to decide. **The judgment of what is debt-like is the analyst's** — but the population is readable, and a sweep of the balance sheet for candidates prevents the bridge from being built only from the lines somebody thought of:

- **Pension deficits** — see `pensions-and-postretirement-asc715`
- **Deferred and contingent consideration** from prior acquisitions
- **Overdue tax, and payables materially beyond normal terms** — effectively borrowing from creditors
- **Factored receivables with recourse**
- **Provisions with a cash cost** — restructuring, dilapidations, warranty
- **Restricted cash**, which is **not** cash-like and is routinely counted as though it were
- **Cash held in jurisdictions with repatriation costs** — the gross amount overstates its value

**Restricted cash deserves its own mention** because it errs in the opposite direction to leases: **counting restricted cash as cash-like overstates equity value.** Both errors are single-line and both are readable.

#### And the two lines Mosofin cannot supply

**Options, warrants and the diluted share count are `[manual]`.** There is no cap table on this surface — consistent with `equity-compensation-accounting`, `statement-of-equity-changes` and `sec-10q-10k-prep`.

**Which means the bridge is automatic down to equity value and manual from there to value per share.** Present it that way: the equity value line complete and measured, and the per-share lines flagged as requiring the cap table. **Value per share is usually the headline number**, and it is the one Mosofin can contribute least to.

---

### Step 7 — Deliver the valuation package

All nine elements preserved.

| Element | Verdict |
|---|---|
| **Editable DCF** | `[auto: computed]`, from a `[manual]` forecast |
| **WACC build** | `[manual]` inputs, shown component by component **with actual-versus-target evidence** |
| **Terminal value build** | `[auto: computed]`, **with TV as a percentage of EV and the cross-implied checks** |
| **Comparable company table** | `[manual]`, **with the subject's measured profile alongside** |
| **Precedent transaction table if available** | `[manual]` |
| **Sensitivity tables** | `[auto: computed]` — see `scenario-and-sensitivity-analysis`, **and use grounded ranges where the driver is measurable** |
| **Football field** | `[auto: computed]` |
| **EV-to-equity bridge** | **`[auto]` to equity value; `[manual]` per share** |
| **Source notes and unresolved data gaps** | **`[auto]` to assemble the gaps** — every `[manual]` item is a known gap |

**Two Mosofin additions to the package:**

**A Bridge Detail sheet** — every component with its balance sheet source, the debt-like sweep with each candidate's include/exclude decision and reason, and the basis note on leases and EBITDA.

**A Coverage and Provenance sheet** — the mandatory coverage sheet.

**And a labelling requirement running through the whole package**: per Step 1's seventh item, **every input carries whose judgment it is** — management, market, analyst, **or measured from the accounts.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Valuation_[EntityName]_[YYYY-MM-DD].xlsx`

Entity `display_name` on every sheet, **and the valuation date prominent.** If any read returned `mock: true`, say so in the file name and on the first sheet.

---

## Quality Bar

*(The original's own section heading, preserved. All seven items kept, with verdicts.)*

> **The valuation is not complete until:**

- **Cash flows tie to the forecast model.** `[auto: computed]` — **and, Mosofin addition, the model's history ties to the accounts.**
- **WACC and terminal value assumptions are visible and editable.** `[manual]` inputs, `[auto: computed]` structure — **no assumption buried or hardcoded.**
- **Comparables are screened, not blindly listed.** `[manual]`
- **Outliers and excluded comps have reasons.** `[manual]`
- **The football field reconciles to supporting methods.** `[auto: computed]`
- **Enterprise value bridges cleanly to equity value.** **`[auto]` — the strongest automatic contribution.**
- **Current market data is sourced or clearly labelled as placeholder or user-provided.** `[manual]`, **and market data is dated data.**

**Six Mosofin additions:**

- **The balance sheet is read at the valuation date**, not the nearest period end.
- **Lease liabilities are shown as a distinct bridge line**, with the EBITDA-basis consistency flagged.
- **Restricted cash is identified** and not counted as cash-like by default.
- **The debt-like sweep runs**, so the bridge is not built only from remembered lines.
- **Terminal value as a percentage of enterprise value is displayed**, since it is usually most of the answer.
- **Cash flow assumptions sit beside their measured history.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and every market input.** A beta, a risk-free rate or an equity risk premium persisted between engagements is stale market data presented as current, which is the specific thing the Inputs note forbids.

**What is worth persisting into the workspace-scoped skill:**

1. **The bridge component mapping** — which accounts constitute debt, lease liabilities, cash, and each debt-like item. **The highest-value item**, because it makes the bridge assemble itself and it embeds the classification decisions already taken.
2. **The classification decisions and their reasons**, so a candidate already excluded is not re-raised.
3. **The EBITDA and net debt basis** agreed for this business, since consistency across the package depends on it.
4. **Measured driver definitions**, shared with `three-statement-financial-model` and `scenario-and-sensitivity-analysis` — **they must agree or the valuation will not reconcile to the model.**
5. **The company's measured profile** on the comps screening dimensions.
6. **Prior valuations, their dates, methods and conclusions**, for continuity.
7. **Whether the cap table has been provided before, and by whom.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — a valuation is among the most commercially sensitive analyses a business commissions.

---

## Anti-patterns

- **Omitting lease liabilities from net debt.** They are debt and they are on the balance sheet.
- **Counting restricted cash as cash.** The opposite error, equally single-line.
- **Building the bridge from remembered lines.** Sweep the balance sheet.
- **Mixing an IFRS 16 EBITDA with a pre-IFRS 16 net debt**, or with comparables on the other basis.
- **Using the nearest period-end balance sheet** for a mid-period valuation date without saying so.
- **Discounting levered cash flows at WACC.**
- **Importing the historical effective tax rate** into an unlevered DCF.
- **Tying the DCF to the model and never tying the model to the accounts.**
- **A terminal assumption better than anything the business has achieved**, unremarked.
- **Not showing terminal value as a percentage of EV.** It is usually most of the answer.
- **A target capital structure far from actual**, unlabelled as an assumption.
- **Excluding an outlier without a reason.**
- **Mixing minority and control bases** on one football field.
- **Treating a financing round's post-money as common equity value.**
- **Burying assumptions in hidden tabs or hardcoded formulas.** The source's opening instruction.
- **Issuing an opinion of value.** Mosofin produces analysis; a qualified specialist opines.
