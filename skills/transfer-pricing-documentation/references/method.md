<!-- transfer-pricing-documentation · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Map the intercompany transactions
- Step 2 — Functional analysis (functions, assets, risks)
- Step 2b — Corroborate the characterisation against the numbers *(Mosofin addition)*
- Step 3 — Select the transfer pricing method
- Step 4 — Determine the tested party and profit level indicator
- Step 5 — Benchmarking (comparables analysis)
- Step 6 — Economic analysis and conclusion
- Step 6b — The loss-making tested party test *(Mosofin addition)*
- Step 7 — Assemble the documentation (three-tiered approach)
- Step 8 — Intercompany agreements
- Step 9 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is analysis for review.** The gateway is read-only. **Mosofin files nothing, adjusts nothing, and concludes on no arm's-length position.**

---

## Inputs

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Group structure and entities** | Legal entities, jurisdictions, ownership | **Required** | **Connected entities are a floor, not the group** | `[manual]`, `[auto]` in part |
| **Intercompany transactions** | Type, parties, amounts, terms | **Required** | **`[auto]` between connected entities — and this is the completeness win** | `[auto]` |
| **Functional information** | Functions performed, assets used, risks borne | **Required** | **Not in the books.** Corroborated, not derived — see Step 2b. | `[manual]` |
| **Financial data per entity** | Segmented to the tested transactions if possible | **Required** | **`[auto]` per entity; segmentation depends on the chart's dimensions** | `[auto]` in part |
| Existing intercompany agreements | Contracts governing the transactions | Recommended | **Documents** | `[manual]` |
| **Jurisdiction documentation requirements** | Local file / master file / CbCR thresholds | **Required — confirmed current** | **Never from this file** | `[manual]` |
| Comparable data source | Database access or provided comparables | Recommended | **Not on this surface** | `[manual]` |
| Prior TP documentation | For continuity | Recommended | Not in the books; **persist the conclusions** | `[manual]` |

---

## Workflow

### Step 1 — Map the intercompany transactions

**`[auto]` between connected entities, and the foundation of everything downstream.**

Identify and categorise all related-party cross-border transactions. All five categories preserved:

| Category | Examples | Mosofin |
|---|---|---|
| **Tangible goods** | Sale and purchase of products between entities | **`[auto]`** — readable by counterparty and account |
| **Services** | Management, technical, administrative, shared services | **`[auto]`** — and **the most commonly forgotten category** |
| **Intangibles** | Licensing of IP, royalties, cost-sharing | **`[auto]` where charged**; **invisible where an entity uses group IP for free**, which is itself a TP issue |
| **Financing** | Intercompany loans, guarantees, cash pooling | **`[auto]` for loans and interest**; **guarantees leave no trace unless a fee is charged** |
| **Cost contribution arrangements** | Shared development costs | `[auto]` for the flows; `[manual]` for the arrangement |

> **For each: the parties, direction, annual amount, and governing agreement. This transaction inventory drives the whole analysis.**

`[auto]` for parties, direction and amount. **`[manual]` for the governing agreement** — and **the gap between the two is a finding**: a flow with no identifiable agreement is exactly what Step 8 exists to catch.

**Two categories deserve a specific note, because they are where completeness fails:**

**Services, especially management recharges.** These accumulate quietly. A parent absorbs a cost, recharges part of it, and the arrangement is never documented. `[auto]` finds the flow; **the analysis of whether the service was rendered, whether it benefited the recipient, and whether a mark-up is appropriate is entirely `[manual]`** — the benefit test is a functional question.

**Free use of group intangibles.** **The hardest gap, because it produces no transaction at all.** A subsidiary trading under the group brand, using group know-how, paying nothing, generates no ledger entry — and a tax authority may well assert that a royalty should have been charged. **`[auto]` cannot see this.** Ask directly: **which entities use group IP, and which of them pay for it?**

---

### Step 2 — Functional analysis (functions, assets, risks)

**`[manual]`. The core of any TP analysis, and none of it is in a ledger.**

For each entity party to a transaction, document all three:

- **Functions performed**: R&D, manufacturing, distribution, marketing, management
- **Assets used**: tangible assets, intangibles (IP, brand, know-how), capital
- **Risks borne**: market risk, credit risk, inventory risk, FX risk, R&D risk

> **The functional analysis characterises each entity** — full-fledged manufacturer versus contract manufacturer; full-risk distributor versus limited-risk distributor versus commissionaire. **The entity bearing more functions, assets and risks should earn more return. This characterisation determines which entity is the "tested party" — usually the less complex one.**

**Preserved in full.** The characterisation drives method selection, tested party selection and the whole benchmarking exercise, and it is established by interviewing the people who do the work.

---

### Step 2b — Corroborate the characterisation against the numbers *(Mosofin addition)*

**`[auto]`, and it serves edge cases 4 and 11 directly.**

The functional analysis is a set of assertions about what each entity does. **Those assertions have financial consequences, and the consequences are readable.**

| Assertion | What the ledger can check |
|---|---|
| **"Limited-risk distributor"** | Does it carry inventory? **Inventory risk is a risk** — an entity holding significant stock is bearing it. Does it bear bad debts? **Does it show a stable, low margin, or a volatile one?** Volatility is what risk-bearing looks like in numbers. |
| **"Contract manufacturer"** | Does it own the plant, or lease it from a related party? Does it carry raw material inventory? Does it employ process engineers? |
| **"Routine service provider"** | **What is its cost mix?** A routine provider's costs are mostly staff and overhead; an entity with material R&D spend or marketing investment is doing something more. |
| **"No valuable intangibles"** | **Is there R&D spend?** Is there marketing spend building a brand? **DEMPE activities have costs**, and costs are in the ledger. See edge case 1. |
| **"Principal bearing entrepreneurial risk"** | Does its result actually vary? **A "principal" with a fixed margin is not bearing entrepreneurial risk**, whatever the agreement says. |

**What this is and is not.** It is **corroboration** — evidence that the characterisation is or is not consistent with how the money actually behaves. **It is not the functional analysis**, and it cannot establish who bears a risk contractually or who controls it.

**But it addresses the single most common TP dispute.** Edge case 4 says the risk of recharacterisation is "a common dispute" and that "substance must support the characterisation." **A tax authority examining a limited-risk entity will look at exactly these numbers.** Looking first is straightforwardly better than being shown them.

**Report contradictions as questions for the functional analysis**, with the figures, never as conclusions about the characterisation.

---

### Step 3 — Select the transfer pricing method

**`[manual]`.** All five methods preserved.

**Traditional transaction methods:**

| Method | Description | Mosofin |
|---|---|---|
| **CUP (Comparable Uncontrolled Price)** | Compares the price to a comparable third-party transaction. **Most direct when comparables exist** — commodities, loans with market rates. | **`[auto]` in one valuable case** — see below |
| **Resale Price Method** | Starts from the resale price to a third party, deducts an arm's-length gross margin. **For distributors.** | `[auto]` for the resale prices |
| **Cost Plus Method** | Adds an arm's-length mark-up to costs. **For manufacturers and service providers.** | `[auto]` for the cost base |

**Transactional profit methods:**

| Method | Description | Mosofin |
|---|---|---|
| **TNMM (Transactional Net Margin Method)** | Compares a net profit indicator of the tested party to comparables. **The most commonly used in practice.** | **`[auto]` for the tested party's side** |
| **Profit Split Method** | Splits combined profit on relative contributions. **For highly integrated operations or unique and valuable intangibles on both sides.** | `[auto]` for the combined profit; `[manual]` for the split |

> **Select and justify the method based on the functional analysis, availability of comparables and reliability. Document why other methods were less appropriate.**

**The `[auto]` contribution to CUP is worth drawing out**, because it is the one method where the workspace can supply genuine comparables rather than structure a search.

**An internal CUP is a comparable uncontrolled transaction that the group itself entered into** — the same product sold to a third party, the same service provided to an unrelated customer, a loan on market terms from an unrelated lender. **Where the group does transact with independents in the same thing, those transactions are in the ledger**, and they are frequently the most reliable comparable available: same product, same period, same market conditions.

**`[auto]` to find them**: for each controlled transaction type, look for equivalent third-party transactions in the same entity's books.

**Two caveats.** Comparability requires more than the same item — volume, terms, market and functions must be comparable, and that is `[manual]` judgment. And **an internal comparable's existence does not make CUP the most appropriate method**, which remains a `[manual]` determination. But **finding one and not using it is worse than not having one**, and a tax authority that finds an internal comparable the taxpayer ignored will ask why.

---

### Step 4 — Determine the tested party and profit level indicator

`[manual]` to select; **`[auto]` to compute.**

- **Tested party**: **usually the least complex entity** — the one without unique intangibles — **because reliable comparables are easier to find.** `[manual]`
- **Profit level indicator (PLI)** for TNMM: **operating margin, Berry ratio, mark-up on total costs, return on assets** — **chosen to fit the tested party's functional profile.** `[manual]` to choose.

**All four PLIs are `[auto]` to compute**, exactly, for every connected entity, for every available year:

| PLI | Computation |
|---|---|
| **Operating margin** | Operating profit ÷ revenue |
| **Berry ratio** | Gross profit ÷ operating expenses |
| **Mark-up on total costs** | Operating profit ÷ total costs |
| **Return on assets** | Operating profit ÷ operating assets |

**Compute all four and present them**, even though only one will be used. The choice is `[manual]` and functional, **but seeing the tested party's profile across all four is informative** — a Berry ratio and an operating margin that tell different stories usually indicate that the cost base includes pass-through items, which affects both the PLI choice and the comparability adjustments in Step 6.

**And compute them multi-year.** TP analysis conventionally uses a multi-year average precisely because single years are noisy, and the ledger holds the history.

**One caution on segmentation.** The PLI should ideally be computed **for the tested transaction**, not for the whole entity. `[auto]` can do this **only where the chart distinguishes the relevant business** — the same dimension question as `segment-reporting`. **Where it cannot, the entity-level PLI is a proxy and must be labelled one**, since an entity with both controlled and uncontrolled business has a blended margin that describes neither.

---

### Step 5 — Benchmarking (comparables analysis)

**`[manual]`, and the original already draws the line correctly.**

> **Search for comparable independent companies or transactions via databases — flag if the user needs database access; this skill structures the search and analysis rather than accessing proprietary databases.**

**Preserved exactly. Comparables come from commercial databases and they are not on this surface.** Mosofin structures the analysis, computes the tested party's side, and stops.

All six screening criteria preserved: **industry, function, size, independence, data availability, loss-making exclusions.** `[manual]`.

The remaining steps:

- **Compute the PLI for each comparable** — `[manual]`, from the database data
- **Build the arm's-length range**, commonly the interquartile range — **`[auto]` arithmetic once the comparables exist**
- **Compare the tested party's result to the range** — **`[auto]`**

> **If the tested party's result falls within the range → supports arm's length. If outside → a TP adjustment may be needed, to the median or an appropriate point.**

**A note on the loss-making exclusion**, because it connects to edge case 7: comparables that lose money are commonly screened out, **while the tested party's own losses are the thing under examination.** That asymmetry is standard practice and it is worth understanding — a range built from profitable comparables, applied to a loss-making tested party, will produce an adjustment. **Which is the point**, and it is why edge case 7 matters so much.

---

### Step 6 — Economic analysis and conclusion

`[auto]` for the comparison; **`[manual]` for the conclusion.**

- **Compare the actual intercompany results to the arm's-length range** — `[auto]`
- **If within range**: document the conclusion that pricing is arm's length — `[manual]`
- **If outside**: **quantify the adjustment needed and flag the exposure** — `[auto]` to quantify — **and any year-end true-up the group should make**
- **Consider comparability adjustments** — working capital, accounting differences — **to improve reliability.** `[auto]` for working capital adjustments, which are arithmetic; `[manual]` for accounting differences.

**The working capital adjustment is genuinely automatable and often skipped.** It normalises for differences in receivable, payable and inventory levels between the tested party and the comparables — and **both sides of it need days computations**, which is the same measurement `three-statement-financial-model` and `scenario-and-sensitivity-analysis` make. The tested party's side is `[auto]`; the comparables' side comes with the database data.

---

### Step 6b — The loss-making tested party test *(Mosofin addition)*

**`[auto]`, one query per entity, and it is the single highest-yield risk indicator in the skill.**

Edge case 7 says it plainly: **tax authorities scrutinise entities that consistently lose money, and a limited-risk entity making losses is a red flag requiring strong support.**

**That is directly computable.** For every connected entity, read the result for every available year, and set it against the entity's characterisation.

| Pattern | Meaning |
|---|---|
| **Limited-risk entity, profitable, stable margin** | Consistent with its characterisation. |
| **Limited-risk entity, one loss year** | Explicable — a downturn, an exceptional item. Document the reason. |
| **Limited-risk entity, losses in consecutive years** | **The red flag.** A limited-risk entity is characterised as bearing little risk and therefore earning a modest but reliable return. **Consistent losses are evidence that it is bearing risk after all** — which supports recharacterisation as a full-risk entity, with a very different expected return. |
| **"Principal" with a flat, low margin** | The inverse problem. An entity taking entrepreneurial risk should show variable returns. |

**Why this is worth running before anything else**: it identifies which entity's position is exposed, and it is exactly the analysis the tax authority will perform first. **It costs one read per entity and it reframes the whole study** — a group with a persistently loss-making limited-risk subsidiary has a specific problem to defend, and knowing that before writing the local file changes what the local file needs to say.

Report the years, the amounts and the characterisation. **`[manual]` for whether the losses are defensible** — genuine start-up losses, a market downturn affecting everyone, an exceptional item — and that defence is what the documentation must carry.

---

### Step 7 — Assemble the documentation (three-tiered approach)

`[manual]` for the requirements; `[auto]` for substantial parts of the content. All three tiers preserved, under the **OECD BEPS Action 13** framework as adopted locally.

**Master File** — **high-level overview of the global group**: organisational structure, business description, intangibles, intercompany financing, financial and tax positions.

`[manual]` for the narrative; **`[auto]` for the financing and financial positions** where entities are connected.

**Local File** — **detailed transactional analysis for the specific entity or jurisdiction**: the local entity's controlled transactions, functional analysis, method, benchmarking, and conclusion.

**`[auto]` for the controlled transactions** (Step 1) and **the entity's financial data**; `[manual]` for the rest.

**Country-by-Country Report (CbCR)** — for large groups above the revenue threshold — **a jurisdiction-by-jurisdiction summary of revenue, profit, tax, employees and assets.**

**`[auto]` in part, with a hard limit.** Revenue, profit, tax paid and assets are readable **for connected entities**; employee numbers usually are not, and **entities outside the workspace contribute nothing.** Since **CbCR is a group-wide report by definition**, a partial read is a partial report — useful as a starting position, never as the filing.

> **Confirm which tiers apply based on the group's size and each jurisdiction's rules — thresholds and requirements vary and change. Confirm current.**

**`[auto]` for the group's consolidated revenue** where the consolidation is available, which is the figure the CbCR threshold turns on — **and it is worth checking, because a growing group crosses that threshold once and the obligation appears without warning.**

---

### Step 8 — Intercompany agreements

**`[manual]` to read the agreements; `[auto]` to read the conduct — and the comparison is the point.**

> **Ensure the legal agreements support the TP positions:**
> - **Agreements exist and reflect the actual conduct — substance must match form**
> - **Terms align with the functional analysis and method**
> - **Flag where conduct and contracts diverge — tax authorities follow substance**

**This is where the ledger is unusually useful, because conduct is exactly what it records.**

`[auto]` checks against a supplied agreement:

| Agreement term | Ledger check |
|---|---|
| **A charge exists at all** | **Is there a flow?** An agreement providing for a management fee, with no fee ever charged, is form without conduct. |
| **The stated mark-up** | Compute the actual realised mark-up on the actual cost base. **Does it match the agreement?** |
| **The charging frequency** | Monthly per the agreement, one journal at year end in practice, is a divergence. |
| **The cost base** | What was actually included, against what the agreement specifies. |
| **Payment terms** | Charged and never settled is a financing transaction as well as a service one. |
| **A flow with no agreement at all** | **The commonest finding**, and the one Step 1 surfaces. |

**And the reverse, which is the more dangerous direction**: **an agreement that exists and is not being followed is worse than no agreement**, because it documents that the parties intended something different from what they did. Tax authorities follow conduct — and the agreement is then evidence against the position rather than for it.

---

### Step 9 — Output

The documentation and a workpaper. All preserved, plus two additions.

**Document: Transfer Pricing Report** (per entity/jurisdiction)
Structured local file content: executive summary, group overview, functional analysis, method selection, benchmarking, conclusion. `[manual]` for the substance.

**Workpaper (.xlsx):**

**Sheet 1: Transaction Inventory**
All intercompany transactions by type, parties, amount, agreement. **`[auto]` for flows between connected entities.** **Add a "Both sides read?" column** and **an "Agreement identified?" column** — the two gaps that matter.

**Sheet 2: Functional Analysis Matrix**
Functions / assets / risks by entity, with characterisation. **`[manual]` — Mosofin does not populate the characterisation.** **Add the Step 2b corroboration alongside**, as a separate block clearly marked as evidence rather than analysis.

**Sheet 3: Method Selection**
Method chosen, tested party, PLI, justification, rejected alternatives. **With any internal CUP candidates found in Step 3.**

**Sheet 4: Benchmarking**
Comparables, screening, PLI computation, arm's-length range. **`[manual]` — comparables are not on this surface**, and the sheet says so where they have not been supplied.

**Sheet 5: Economic Analysis**
Tested party result versus range; adjustment if any. **All four PLIs shown, multi-year.**

**Sheet 6: Documentation Compliance**
Which tiers apply, thresholds, deadlines per jurisdiction. **`[manual]`, current-sourced — with deadlines prominent**, per edge case 9.

**Sheet 7: Open Items / Specialist Review**
Local-rule confirmations and items needing TP-specialist sign-off. **Every `[manual]` item appears here.**

**Sheet 8: Risk Indicators** *(Mosofin addition)*
| Entity | Characterisation | Result by year | Loss years | Cost profile flags | Conduct/contract divergences | Priority |
|---|---|---|---|---|---|---|

Step 6b's loss test, Step 2b's corroboration, and Step 8's divergences in one place — **the sheet a specialist should read first.**

**Sheet 9: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet, **including which entities were readable.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

File naming: `Transfer_Pricing_[Jurisdiction]_[YYYY]_[EntityName]`

If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All eleven preserved.

- **Complete intercompany transaction inventory.** **`[auto]` between connected entities** — **and the connected set is stated as a floor, not asserted as complete.**
- **Functional analysis supporting entity characterisation.** `[manual]`, **with `[auto]` corroboration presented separately.**
- **Most-appropriate method selected and justified, alternatives addressed.** `[manual]`, **with internal CUP candidates surfaced.**
- **Tested party and PLI chosen consistently with the functional profile.** `[manual]` to choose; **`[auto]` to compute, all four, multi-year.**
- **Benchmarking establishes a defensible arm's-length range.** **`[manual]` — comparables are not on this surface.**
- **Economic analysis compares results to the range and quantifies any adjustment.** `[auto]`
- **Documentation tiers determined against current thresholds.** `[manual]`, current-sourced.
- **Intercompany agreements checked against actual conduct.** **`[auto]` for conduct** — the strongest structural contribution.
- **No hardcoded thresholds, safe harbours or penalty rules — all current-sourced.** `[manual]`, **and nothing persisted supplies one.**
- **Complex areas — intangibles, restructurings, financing — flagged for TP-specialist review.** `[manual]`.
- **File naming consistent.** `[auto]`

**Five Mosofin additions:**

- **The connected entity set is reconciled against the group structure**, with unreadable entities listed.
- **Flows are read from both sides where possible**, and one-sided readings are labelled.
- **Loss-making entities are tested against their characterisation** before the study is written.
- **Conduct is compared to agreements**, since tax authorities follow conduct.
- **Free use of group intangibles is asked about**, because it produces no transaction to find.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and every threshold, safe harbour and deadline.**

**What is worth persisting into the workspace-scoped skill:**

1. **The group structure**, with which entities are connected and which are not — **the reconciliation that makes the inventory's completeness assessable.**
2. **The functional analysis and characterisations**, with their support. **Expensive to establish, stable until the business changes, and re-used every year.**
3. **The transaction inventory by category**, so a new flow type appearing is visible as a change.
4. **The method, tested party and PLI selected**, with justification — **consistency year to year is itself defensive**, and an unexplained method change invites questions.
5. **Intercompany agreements and their key terms**, so Step 8's conduct check runs automatically.
6. **The benchmarking study and its refresh date** — studies are typically refreshed on a cycle, and knowing when it is due matters.
7. **Prior conclusions and any adjustments made.**
8. **Documentation deadlines per jurisdiction**, given penalty protection turns on them.
9. **Internal comparables previously identified.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — a TP study is among the most sensitive documents a group holds, and it describes exactly where profit sits.

---

## Anti-patterns

- **Building the transaction inventory from memory.** People forget management recharges, guarantees and old licences.
- **Treating an intercompany balance as the transaction inventory.** The balance nets flows that need separate analysis.
- **Asserting the inventory is complete** when only some entities are connected.
- **Deriving the functional analysis from the numbers.** They corroborate; they do not establish.
- **Ignoring a cost profile that contradicts the characterisation.** The tax authority will not ignore it.
- **Writing the local file before checking whether the tested party is loss-making.**
- **Using an entity-level PLI for a transaction** without labelling it a proxy.
- **A single-year PLI.** TP is multi-year by convention because single years are noisy.
- **Ignoring an internal comparable.** Being shown one you did not use is worse than not having one.
- **Presenting a margin as arm's length** without a range. One side is not a comparison.
- **An agreement that exists and is not followed.** Worse than none — it documents a different intention.
- **An interest-free intercompany balance** treated as not being a financing transaction.
- **A true-up to the median every year**, unexamined.
- **Adjusting TP without considering customs and VAT.**
- **Missing a documentation deadline.** Penalty protection frequently turns on it.
- **Concluding on arm's length.** That is the specialist's.
