<!-- revenue-recognition-asc606 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All seventeen preserved, in order.

**Customer pays upfront for a multi-year SaaS subscription**: recognise **ratably over the service period.** The upfront cash creates a large deferred revenue balance. **Watch for a significant financing component** — where the prepayment period exceeds a year, discounting may be required under IFRS 15; ASC 606 permits a practical expedient where the period is one year or less. `[auto]` to flag the timing gap; `[manual]` for the rate.

**Customer paid more than they consumed at year end, with or without auto-renewal**: **recognise revenue only for services actually delivered through year end, regardless of renewal probability.** `[auto]` to compute. Renewal probability is irrelevant to the current period and it is a common place for optimism to leak in.

**Free trial periods**: typically **no revenue during the trial** unless the customer is contractually committed. Where trial-to-paid conversion is highly probable, consideration may need allocating across the full period. `[manual]`.

**Implementation fees on a SaaS contract**: assess whether implementation is **distinct** from the ongoing service. **Often it is not** — in which case recognise it as part of the subscription over the term. Where clearly distinct (the customer could use a third party), it is a separate PO recognised on delivery. `[manual]`, and one of the most consequential judgments in software revenue.

**Setup fees with no separate performance**: typically a **customer option to renew** — recognise ratably over the **expected customer life**, which may exceed the initial contract term. `[manual]`; `[auto]` in part for churn history, which informs expected life.

**Right to invoice expedient**: where consideration **directly corresponds to the value transferred to date** — billable hours at a rate — recognise at the amount billable. Simpler than measuring progress separately. `[manual]` to elect; **and note this is the one case where invoice equals revenue legitimately**, which is exactly why Test 0c is a question rather than a conclusion.

**Refund liabilities for expected returns**: estimate refunds and book a **Refund Liability instead of revenue**; book an **asset for the expected returned inventory at cost.** `[auto]` for returns history; `[manual]` for the estimate. **The asset side is frequently forgotten**, which overstates the cost of the return.

**Customer acceptance clauses**: where acceptance is a **formality** with no real risk of rejection, recognise at delivery. Where **substantive**, defer until granted. `[manual]`.

**Principal versus agent**: determine whether the entity **controls** the good or service before transfer (**principal — gross**) or merely arranges it (**agent — net**). **Apply the control indicators carefully — this is a frequent area of restatement.** `[manual]` to conclude. **`[auto]` for a genuine signal**: a revenue stream with a persistently thin and very stable gross margin, paired with a near-matching cost from a single supplier that moves in lockstep, is the arithmetic signature of an agent arrangement recorded gross. It is a question to raise, never a conclusion — some businesses genuinely run on thin margins — but getting this wrong misstates the top line by the entire gross amount while leaving profit unchanged, which is why it restates so often.

**Bill-and-hold arrangements**: revenue may be recognised before physical delivery **only if specific criteria are met** — the reason is substantive, the product is separately identified, it is ready for physical transfer, and the entity cannot use it or direct it to another customer. `[manual]`. **All four, not most of them.**

**Licences of IP**:
- **Right-to-use** (functional IP — software, completed media): **point in time**, at grant
- **Right-to-access** (symbolic IP — brands, franchises with ongoing entity activity): **over time**
- Distinguish on **whether the entity's ongoing activities significantly affect the IP.** `[manual]`.

**Royalties (sales- or usage-based)**: recognised **as the subsequent sales or usage occurs** — with the specific rule that royalties on IP are recognised at the **later** of the underlying sale/usage **or** the performance obligation being satisfied. `[auto]` to compute from reported sales data where it is in the books; `[manual]` where royalty reports come from the licensee.

**Warranties**:
- **Assurance-type** (the product works as promised): **accrue as a cost — not a separate PO**
- **Service-type** (services beyond assurance): **a separate PO**

`[manual]` to classify. **The distinction is whether the customer could buy it separately**, and misclassifying a service-type warranty as assurance recognises its revenue too early.

**Multi-year contracts with material variable pricing**: **re-estimate at each reporting date.** Catch-up for revenue already earned; prospective for the rest. `[auto]` to compute the true-up; `[manual]` for the estimate.

**Contract loss provisions**:
- **ASC 606 has no specific loss-contract guidance** — other standards may apply (ASC 605-35 for construction)
- **IFRS 15 refers to IAS 37** where a contract becomes onerous

`[manual]`. See percentage-of-completion accounting, which is emphatic that **the entire expected loss is recognised immediately and never spread**, and the restructuring accounting for the IAS 37 onerous-contract model.

**Cancellable contracts** (the customer may cancel without penalty): assess whether a contract truly exists; **in many cases the contract term is limited to the non-cancellable period.** `[manual]`, and it materially shortens RPO and the amortisation period for contract costs — which is exactly why it gets overlooked.

**Multi-currency contracts**: recognise revenue in the functional currency **at the spot rate when revenue is recognised**, or at the contract date where that is the entity's policy. **FX gains and losses on remeasuring receivables and contract assets are separate** from revenue. `[auto]` for the mechanics; see `multicurrency-fx-revaluation`. **Do not let FX movement flow through the revenue line** — it is a different caption and blending them corrupts the top line.
