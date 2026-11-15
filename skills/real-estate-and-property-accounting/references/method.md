<!-- real-estate-and-property-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 0 — Read the property position before classifying anything
- Step 1 — Classify the property
- Step 2 — Initial measurement (capitalisation)
- Step 3 — Subsequent measurement
- Step 4 — Rental income (lessor side)
- Step 5 — Real estate sales
- Step 6 — Impairment
- Step 7 — Disclosures
- Step 8 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. Mosofin posts nothing.

---

## Inputs

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| Property details | Type, location, use, dates | **Required** | Acquisition dates and amounts are readable; **location and use are not** | `[auto]` in part |
| Reporting framework | US GAAP / IFRS | **Required** | Not in the books | `[manual]` |
| Purpose / use | Owner-occupied / rental / development / held for sale | **Required** | **Not stated in the books — but strongly evidenced by them.** See Step 1. | `[manual]` to conclude, `[auto]` to test |
| Acquisition / construction costs | Detailed | **Required** | **Live read**, by transaction, with vendor and date | `[auto]` |
| Construction financing | For interest capitalisation | If applicable | Interest posted to the asset is readable; **the borrowing terms are not** | `[auto]` in part |
| Subsequent measurement choice (IFRS) | Cost or fair value model | Required (IFRS) | **Not stated — but the posting pattern reveals which is being applied.** See Step 3. | `[manual]` to elect, `[auto]` to verify |
| Lease arrangements | Where leased to others | If applicable | Rent received is readable; **lease terms, escalations and incentives are not** | `[auto]` in part |
| Sale details | Buyer, price, terms, financing | If selling | Proceeds and derecognition are readable; **terms are not** | `[auto]` in part |
| Fair value data | If using fair value model | If applicable | **Not on this surface.** A valuation is an external input. | `[manual]` |

---

## Workflow

### Step 0 — Read the property position before classifying anything

*(A Mosofin addition. One batched read that determines how the rest of the run goes.)*

Pull, together: the chart of accounts filtered to property, land, accumulated depreciation and construction-in-progress; the full transaction detail on those accounts for the available history; the rental income accounts; the interest accounts; and any disposal or gain-on-sale accounts.

Then run the four **contradiction tests**. Each compares a stated or implied classification against what the ledger shows the property actually doing. All four are `[auto]` and all four are cheap.

**Test 0a — Is land being depreciated?** `[auto]`

**Land is not depreciated. Ever, under either framework.** So if there is a land account with accumulated depreciation posted against it, that is an error, it is unambiguous, and it is one read.

Two variants, and the second is more common and more damaging:

- **Explicit**: a land account with its own accumulated depreciation. Obvious once looked for.
- **Implicit**: **no land account at all.** The property was acquired and posted as a single amount to "Property" or "Buildings", the split was never made, and the whole cost — land included — is being depreciated. This overstates depreciation every year, permanently, and it never self-corrects. See Step 2.

The second variant is invisible unless you look for an absence, which is why it survives so long. Look for it.

**Test 0b — Is a fair-value-model property being depreciated?** `[auto]`

Under IAS 40's fair value model, investment property is **not depreciated**; the carrying amount moves only with fair value. So a property the client says is on the fair value model, which also carries a monthly depreciation charge, is a definitional contradiction. Either the election is not what was stated, or the depreciation should not be there.

The reverse is equally informative: **a fair-value-model property with no revaluation entry for two years is not being measured at fair value either.** The model requires remeasurement at each reporting date. Silence is not stability. See Step 3.

**Test 0c — Is a held-for-sale property still depreciating?** `[auto]`

**Depreciation stops on held-for-sale classification**, under both frameworks. If an asset has been designated held for sale and the depreciation charge continues, one of the two is wrong. One read.

**Test 0d — Is interest still being capitalised after the property started earning?** `[auto]`

**Capitalisation stops when the asset is ready for its intended use** — the original's edge case is explicit that this is *not* when it is finally rented or occupied, which makes it a judgment. But the ledger supplies a powerful piece of evidence for that judgment: **if rental income started in one month and interest capitalisation continued for months afterwards, the asset was demonstrably ready and capitalisation should have stopped at or before the point income began.**

Both facts are in the same ledger. Comparing them is one query, and over-capitalisation of interest is one of the errors the original singles out.

**These four tests take one round trip.** On a portfolio that has not been reviewed in a while, they will frequently be the most valuable output of the run — and none of them requires knowing what the properties are.

---

### Step 1 — Classify the property

`[manual]` to conclude. `[auto]` to test, and the testing is substantial.

**The use determines the accounting.** All five classifications preserved:

| Classification | Definition | What the ledger shows | Verdict |
|---|---|---|---|
| **Owner-occupied (PP&E)** | Used in the entity's own operations. Account as PP&E (US GAAP / IAS 16) — cost model, depreciate. | No third-party rental income against it; occupancy costs present | `[auto]` to evidence |
| **Investment property (IAS 40 — IFRS only)** | Held to earn rentals or for capital appreciation; not for own use, not for sale in the ordinary course. Cost **or** fair value model. **US GAAP has no separate investment-property category** — such property is PP&E unless held for sale. | Third-party rental income against it | `[auto]` to evidence, `[manual]` to conclude |
| **Property held for sale** | Meets the criteria (ASC 360 / IFRS 5). **Stop depreciating**; measure at the lower of carrying amount and fair value less costs to sell. | Depreciation should have ceased — Test 0c | `[manual]` for criteria, `[auto]` for the consequence |
| **Inventory** (dealer / developer) | Held for sale in the ordinary course — a homebuilder's units. Accounted for as inventory. | Sits in inventory, moves through COGS on sale | `[auto]` to identify |
| **Property under development** | Prior to ready-for-intended-use: capitalise costs; transfer to the appropriate category when ready. | Construction-in-progress with additions and no depreciation | `[auto]` to identify, `[manual]` for readiness |

> **Confirm classification carefully — it drives all subsequent accounting. Reclassify when use changes, with framework-specific rules on remeasurement.**

**The `[auto]` evidence for classification, stated properly:**

**Rental income from third parties is the strongest single signal**, and it is decisive in one direction only. A property earning third-party rent is **not** owner-occupied. That is a genuine conclusion. It does not, on its own, establish that the property *is* investment property — under IFRS that requires it not be held for sale in the ordinary course, and under US GAAP the category does not exist at all.

So the read gives you: **a firm negative and a strong hypothesis.** Present it that way. "This property earned rent from three tenants throughout the year and is classified owner-occupied — please confirm the classification" is a good question. "This property is investment property" is not a conclusion the ledger supports.

**And the framework governs before anything else.** Under **US GAAP, do not apply IAS 40 mechanics at all.** A US GAAP entity's rental property is PP&E at cost, depreciated, unless held for sale. The commonest way to get this badly wrong is to see rental income, reach for the fair value model, and produce accounts under a standard that does not apply to the entity. Establish the framework at Gate 3 and let it gate everything here.

---

### Step 2 — Initial measurement (capitalisation)

`[auto]` for the cost build, and this is one of the strongest automatic contributions in the skill: **the acquisition transactions are individually readable**, with dates, vendors and amounts, so the cost build is reconstructed from source rather than assembled from memory.

Cost includes, all five preserved:

- **Purchase price** — `[auto]`
- **Legal fees, taxes, transfer costs** directly attributable to acquisition — `[auto]` to find; **`[manual]` to judge attributability.** This is where the interesting question lives: legal fees around a property purchase frequently cover both the acquisition and other matters, and only part is capitalisable. The ledger shows the invoice; the engagement letter says what it was for.
- **Site preparation, demolition** where required for the intended use — `[auto]` to find, `[manual]` to judge
- **Self-constructed**: direct construction costs (materials, labour), directly attributable overhead, and **capitalised interest** during construction — `[auto]` for direct costs; **`[manual]` for the overhead allocation**, which is a basis decision, not a transaction
- **Initial estimate of dismantling or restoration costs**, where an obligation exists — **`[manual]`.** A provision for an obligation that has not yet been recognised is, by definition, not in the ledger. `[auto]` for one check: whether such a provision exists at all. See `asset-retirement-obligations-asc410`.

**Capitalisation of interest** — during active construction, on qualifying expenditures, at either the specific borrowing rate or a weighted-average rate. **Stops when the asset is ready for its intended use.**

- `[auto]`: the interest actually capitalised, by period — it is a posting
- `[auto]`: **the readiness evidence from Test 0d.** If income began before capitalisation ended, raise it
- `[manual]`: the rate basis, which comes from the loan agreements, not the ledger
- `[auto]`: whether capitalised interest exceeds total interest incurred in the period, which is an absolute ceiling and an easy arithmetic check

**Land and buildings separated.** **Land has an indefinite life and is not depreciated; buildings have a finite life and are.** Allocate the cost between them on relative fair values.

- `[auto]` to test whether the split was made — Test 0a's second variant. **A single-line property acquisition with no land component is a split that never happened**, and the consequence is permanent over-depreciation.
- `[manual]` for the allocation itself, which needs relative fair values and is therefore off this surface.

**The allocation basis is worth persisting.** It is established once, at acquisition, and it governs depreciation for decades. Losing it and re-estimating later produces a different number and an unexplainable restatement.

---

### Step 3 — Subsequent measurement

`[auto]` to verify what is being applied. `[manual]` to elect.

**Owner-occupied PP&E (both frameworks)**:
- Cost model: cost less accumulated depreciation and impairment — `[auto]` to compute and verify
- **IFRS also permits the revaluation model** (less common); **US GAAP is cost only** — `[manual]`
- Depreciate buildings, and components where material — **IFRS requires component depreciation; US GAAP permits it** — see the edge case
- **Land not depreciated** — `[auto]`, Test 0a
- Useful lives per the entity — `[manual]` to set, `[auto]` to check they are applied consistently. See `fixed-asset-register-and-depreciation`.

**Investment property — IFRS (IAS 40)**:
- A **policy choice applied to all investment property**: cost model **or** fair value model — `[manual]`
- **Fair value model**: revalue at each reporting date, **changes to P&L, not OCI. Not depreciated.** Requires reliable fair value measurement. — **`[manual]` for the valuation**, `[auto]` for two verifications:
  - **that no depreciation is being charged** (Test 0b), and
  - **that a revaluation actually occurred each reporting date.** A fair value model with no movement recorded for several periods is not being operated.
- **Cost model**: as PP&E, **but fair value is still disclosed in the notes** — `[manual]` for the valuation, and note that electing the cost model does **not** remove the need for a valuation; it only moves it from the face of the accounts to the notes. This is frequently misunderstood as a way to avoid getting the property valued. It is not.

> **The choice is significant and largely irreversible; flag for a considered policy decision.**

Preserved and worth emphasis. `[auto]` for one supporting fact: the fair value model puts revaluation movements **through profit or loss**, so the P&L inherits the property market's volatility. Where prior valuations exist in the books, showing what that volatility actually looked like over the available history is a genuinely useful input to a decision that is hard to reverse.

**Held for sale (both frameworks)**: lower of carrying amount and fair value less costs to sell; **depreciation stops.** `[manual]` for the measurement, `[auto]` for Test 0c.

---

### Step 4 — Rental income (lessor side)

**The richest `[auto]` territory in the skill after the contradiction tests**, because rental income is a stream of transactions with a very legible signature.

All five items preserved:

| Item | Verdict | Note |
|---|---|---|
| **Operating lease — income straight-lined over the lease term** (both frameworks) | `[auto]` to **test**, `[manual]` to compute without the lease terms | See below. The absence of straight-lining is highly detectable. |
| **Tenant incentives** — rent-free periods, lease incentives — deferred and spread to produce the straight-line effect | `[auto]` to detect the incentive, `[manual]` for the terms | A rent-free period is visible as months of zero income on a continuing tenancy |
| **Direct costs of obtaining a lease** may be capitalised and amortised | `[auto]` to find leasing commissions and legal fees, `[manual]` to judge | Frequently expensed when they should be spread |
| **Variable lease payments** per the framework | `[auto]` to identify irregular receipts, `[manual]` to treat | Turnover rents show as amounts that move with the tenant's trade |
| **Finance leases granted** (rare in real estate) — lessor recognises a receivable and interest income | `[manual]` | Classification requires the lease terms |

Coordinate with the lessor side of `lease-accounting-asc842-ifrs16`.

#### The straight-lining test

`[auto]`, and it is the single most valuable finding available in this step. Straight-lining of operating lease income is required under **both** frameworks, and it is one of the most commonly skipped adjustments in small and mid-sized property books, because the cash is simple and the adjustment is not.

**Two signatures, either of which is sufficient to raise it:**

**1. Income exactly equals cash, month by month, on a lease that is not flat.** If a tenancy has a rent-free period or a step-up, straight-lined income and cash received **must** differ in the early periods. If they are identical every month, the income is being recognised as received, which is not straight-lining.

The rent-free period is the clearest case: **months of zero rental income on a continuing tenancy, followed by full rent.** Under straight-lining those months carry income anyway, funded by a receivable. Zero income in a rent-free period is the error made visible.

**2. There is no deferred rent balance.** Straight-lining necessarily creates one — an asset where income has been recognised ahead of cash, a liability where cash has run ahead of income. **A portfolio with escalating leases and no deferred rent account anywhere on the balance sheet is a portfolio that is not straight-lining anything.** One read of the chart.

The second test is the stronger one because it needs no lease terms at all — only the observation that the balance which straight-lining inevitably produces does not exist.

**What the ledger cannot supply:** the lease term, the escalation schedule, the incentive terms. Those are in the leases. So Mosofin detects the absence of straight-lining reliably and computes the correct figure only once the terms are provided. Say which half you have.

---

### Step 5 — Real estate sales

`[auto]` for the arithmetic and the derecognition check. `[manual]` for control and the terms.

A sale of real estate falls under revenue recognition for non-financial-asset sales when the buyer obtains control — see `revenue-recognition-asc606`. All five items preserved:

- **Determine when control transfers** — usually closing or legal completion. `[manual]`; a completion date is a legal fact, not a posting. `[auto]` for the posting date, which is evidence of it and not the same thing.
- **Recognise the sale at the transaction price.** `[auto]`
- **Derecognise the property; gain or loss = consideration − carrying amount.** `[auto]`, and see the critical check below.
- **If financing is provided to the buyer on off-market terms, separate the financing component.** `[manual]` — the terms are in the contract. `[auto]` for the signal: sale proceeds received in instalments over time rather than at completion.
- **Sale-and-leaseback has specific rules**: the seller-lessee assesses whether a sale occurred under 606 first. If yes, recognise a sale with adjustments for off-market terms and the leaseback. If no, **treat it as financing.** `[manual]`, and see the edge case.

**The check that matters most** `[auto]`: **did the asset actually come off the books?**

Sale proceeds arriving with no corresponding derecognition of the property overstates the gain by the entire carrying amount of the asset — which, for real estate, is an enormous number. The two halves of a disposal are posted separately and it is entirely possible for the cash to be recorded and the asset to be forgotten. Read the disposal accounts against the property register and confirm that every property whose proceeds appear has also had its cost and accumulated depreciation removed.

The mirror check is worth running too: **a property removed from the books with no proceeds recorded.**

---

### Step 6 — Impairment

All three cases preserved.

| Case | Treatment | Verdict |
|---|---|---|
| Owner-occupied / PP&E | Long-lived asset impairment triggers | `[auto]` for **some** indicators, `[manual]` for the test |
| Investment property under the IFRS cost model | Tested similarly | Same |
| Investment property under the **fair value model** | **No separate impairment test** — fair value changes are captured continuously | `[auto]` to confirm the model, `[manual]` for the valuation |

**Testing itself is `[manual]`** — it requires recoverable amounts, which means valuations or cash flow projections, and neither is on this surface.

**Indicators are partly readable** `[auto]`: a property whose rental income has fallen materially; a property standing vacant, which shows as income ceasing while occupancy costs continue; a development whose costs have run well beyond the original spend profile. Present these as **indicators prompting a test**, never as a conclusion about value, and be clear that a ledger-based indicator scan is not a complete indicator review — market and regulatory indicators are not in it.

**And the development-specific case from the edge cases** `[auto]` in part: if expected net realisable value or recoverable amount falls below capitalised cost during construction, write it down. The capitalised cost is readable; the expected realisable value is not.

---

### Step 7 — Disclosures

For `notes-to-financial-statements`. All six items preserved:

| Disclosure | Verdict |
|---|---|
| Property by class — carrying amounts, depreciation, additions, disposals | `[auto]` — this is a roll-forward and every component is a live read |
| Useful lives and depreciation methods | `[auto]` to observe what is applied, `[manual]` to state the policy |
| **IFRS investment property**: classification, measurement model, fair values (**disclosed even under the cost model**), rental income, direct operating expenses | `[auto]` for rental income and operating expenses; **`[manual]` for fair values** |
| Capitalised interest | `[auto]` |
| **Restrictions on title, pledges as security** | **`[manual]`.** A mortgage or charge over a property is a legal instrument. The loan is in the books; **the security it is granted over is not.** |
| Commitments — capital expenditure, lease commitments | `[manual]` — a commitment is a contract not yet transacted, and the ledger records transactions |

**The pledge disclosure deserves a note**, because it is a required disclosure that is easy to miss and impossible to derive. The ledger shows a property and shows a loan. **Nothing in it says the one is charged against the other.** That connection exists only in the mortgage deed, and it must be asked for.

---

### Step 8 — Output

An `.xlsx` property workbook. All nine of the original's sheets, plus two additions.

**Sheet 1: Property Register**
Each property: classification, location, dates, costs, current measurement. `[auto]` for costs and dates; `[manual]` for location and classification. **Add a Source column** distinguishing ledger-read from user-supplied.

**Sheet 2: Classification & Use**
Owner-occupied / investment / held for sale / under development, with the rationale. `[manual]` for the conclusion — **and add an Observed Behaviour column** carrying the `[auto]` evidence: rental income earned, whether depreciation is being charged, whether interest is capitalising. The rationale and the evidence sit side by side, and where they disagree the sheet shows it.

**Sheet 3: Initial Cost Build**
Acquisition and construction cost components, with the capitalised-interest computation. `[auto]` — reconstructed from individual transactions, each traceable.

**Sheet 4: Land/Building Split & Depreciation**
Allocation, useful lives, depreciation schedule. `[manual]` for the allocation; `[auto]` for the depreciation arithmetic. **If no split exists, this sheet says so at the top** rather than presenting a building-only schedule that quietly includes the land.

**Sheet 5: Fair Value Workbook** (IFRS fair value model, if elected)
Valuation method, key inputs, period changes through P&L. **`[manual]` for the valuation** — Mosofin records what was provided and by whom, and does not value anything.

**Sheet 6: Rental Income Schedule**
Per lease: straight-line, incentives. `[auto]` for cash received per tenant; `[manual]` for the terms; **`[auto]` for the straight-lining test result**, which belongs here prominently.

**Sheet 7: Sales & Disposals**
For sales: the 606 application, gain or loss, financing components. `[auto]` for the arithmetic and **for the derecognition check.**

**Sheet 8: Impairment Assessments**
Triggers and tests. `[auto]` for readable indicators, marked as incomplete; `[manual]` for the tests.

**Sheet 9: Disclosures**
Disclosure-ready data, with the pledge and commitment items flagged as requiring input.

**Sheet 10: Ledger Contradictions** *(Mosofin addition)*
The output of Step 0 — what the books said without being asked:

| Test | Property | Evidence | Amount | Periods | Recommended action |
|---|---|---|---|---|---|

Land depreciating, or no land account at all. Fair-value-model property being depreciated, or not revalued. Held-for-sale property still depreciating. Interest capitalising after income began. Missing deferred rent. Proceeds with no derecognition.

**Sheet 11: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Real_Estate_[YYYY]_[EntityName].xlsx`

The entity `display_name` goes in the file name and on every sheet — which matters more here than usual, given how often each property sits in its own entity. If any read returned `mock: true`, say so in the file name and on Sheet 1.

**And the register reconciliation, which the original leaves implicit:** run it in **both directions**, as `fixed-asset-register-and-depreciation` and `intangibles-and-amortization` do. Register to GL catches properties in the register with no balance. **GL to register catches property costs in the ledger that are on no register at all** — the more common and more dangerous direction, because an unregistered property is depreciating on nobody's schedule. With five properties this is a five-row exercise, so there is no excuse for sampling it.

---

## Output Quality Standards

All ten preserved, with verdicts.

- **Classification correctly applied per framework** — owner-occupied / investment / held for sale / inventory / under development. `[manual]` to conclude, **`[auto]` to test against observed behaviour.**
- **US GAAP versus IFRS investment property treatment correctly distinguished.** `[manual]`, and established before anything else is done.
- **Initial cost capitalisation appropriate**, including the land/building split and capitalised interest. `[auto]` for the cost build and both tests; `[manual]` for the allocation basis and attributability.
- **Subsequent measurement applied per the entity's policy choice, consistently and disclosed.** `[auto]` to verify the policy is actually being operated — **including that a fair-value-model property is being revalued and not depreciated.**
- **Rental income straight-lined with incentives.** `[auto]` to test for its absence; `[manual]` to compute without the lease terms.
- **Real estate sales applied under ASC 606 / IFRS 15.** `[manual]` for control; **`[auto]` for the derecognition check.**
- **Impairment assessed for cost-model properties.** `[auto]` for readable indicators, **flagged as an incomplete indicator review**; `[manual]` for the test.
- **Transfers between classifications handled per framework.** `[manual]` to treat; `[auto]` to detect from a change in income pattern.
- **Disclosures appropriate to the framework and the choices made.** `[auto]` for the roll-forward and income figures; **`[manual]` for fair values, pledges and commitments.**
- **File naming consistent.** `[auto]`

**Three Mosofin additions:**

- **Every property is reviewed individually.** The portfolio is small enough that sampling has no justification, and the per-property materiality makes it indefensible.
- **The register reconciles in both directions**, and the GL-to-register direction is run first.
- **Every figure is attributed** — ledger-read, user-supplied, or valuation-derived. A fair value carries the valuer and the date.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map. Gate 2 reads it every run.

**What is worth persisting after the first run** — and property is exceptionally good for this, because portfolios change slowly:

1. **The property list**, with each property's classification and the reasoning that supported it.
2. **The framework and the measurement election**, which are close to permanent.
3. **The land/building allocation per property, and its basis.** This is the highest-value item to persist. It is established once at acquisition, it governs depreciation for decades, and re-deriving it later produces a different answer that nobody can reconcile to the original.
4. **Useful lives and any component breakdown.**
5. **The account structure** — which accounts hold property, land, accumulated depreciation, construction in progress, rental income, deferred rent.
6. **Lease terms per tenancy**, once obtained, so the straight-lining computation does not need re-interviewing each period. These are expensive to gather and stable for years.
7. **Pledges and charges over property**, once established — a required disclosure that is invisible in the ledger and therefore lost every time unless written down.
8. **Prior valuations with their dates and valuers**, for the trend and for the volatility question.
9. **Contradictions found and resolved**, so they are re-tested first next period.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — property addresses and valuations are commercially sensitive.

**The evolved version should open with the contradiction tests and a list of what changed since last time.** For a stable portfolio, that is a very short and very useful report.

---

## Anti-patterns

- **Reading classification off the account name.** "Investment Property" is a label somebody typed; classification follows use.
- **Applying IAS 40 under US GAAP** because the ledger shows rental income. The category does not exist there.
- **Depreciating land** — or, more commonly, **never splitting it out**, so it depreciates invisibly inside the building.
- **Depreciating a fair-value-model property.** The two are mutually exclusive by definition.
- **Leaving a fair-value-model property unrevalued.** Silence is not stability; the model requires remeasurement each reporting date.
- **Continuing depreciation on a held-for-sale asset.**
- **Capitalising interest past readiness.** Rental income starting is strong evidence the asset was ready.
- **Recognising rent as received** where leases escalate or carry rent-free periods. No deferred rent balance means no straight-lining.
- **Assuming the cost model avoids needing a valuation.** It moves it to the notes; it does not remove it.
- **Recording sale proceeds without derecognising the asset.** The gain is overstated by the whole carrying amount.
- **Missing a sale-leaseback.** A disposal followed by rent to the buyer is the signature; getting it wrong books a gain that should not exist.
- **Sampling a five-property portfolio.** Read every one.
- **Treating a ledger indicator scan as a complete impairment review.** Market and regulatory indicators are not in the books.
- **Answering the classification question without establishing standalone versus consolidated.** The same building has two correct answers.
- **Saying "posted".** The gateway reads.
