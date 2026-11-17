<!-- revenue-recognition-asc606 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 0 — Test whether the books apply the standard at all *(Mosofin addition)*
- Step 1 — Identify the contract with a customer
- Step 2 — Identify the performance obligations
- Step 3 — Determine the transaction price
- Step 4 — Allocate the transaction price
- Step 5 — Recognise revenue when (or as) each PO is satisfied
- Step 6 — Contract assets, contract liabilities, and receivables
- Step 7 — Construct the entries
- Step 8 — Contract modifications
- Step 9 — Contract costs
- Step 10 — Disclosure-relevant data
- Step 11 — Output
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

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Reporting framework** | ASC 606 or IFRS 15 | **Required** | Not in the books | `[manual]` |
| **Customer contract / agreement** | PDF, text, or key-terms summary | **Required** | **Not in the books. The primary input.** | `[manual]` |
| **Standalone selling prices per promised good/service** | List with sources | **Required if multiple POs** | **Observable prices are a live read** — see Step 4. Estimated SSP is not. | `[auto]` in part |
| **Reporting currency** | ISO code | **Required** | Company record | `[auto]` |
| **Chart of accounts** | For posting | **Required** | Live read | `[auto]` |
| Contract modifications | Subsequent amendments | If applicable | **Not in the books**; a price change may be visible after the fact | `[manual]` |
| Existing recognised revenue, if mid-contract | Amount and through-date | If mid-contract | **Live read** — with the caution in Step 5 | `[auto]` |
| Entity's accounting policies | Practical expedients elected | Recommended | Not in the books; **persist after the first run** | `[manual]` |

---

## Workflow

### Step 0 — Test whether the books apply the standard at all *(Mosofin addition)*

`[auto]`. One batched read, run before analysing any contract, and on many sets of books it is the most important output of the engagement.

Analysing a single contract in detail is of limited use if the entity's revenue process does not implement the standard in the first place. These four tests establish whether it does.

**Test 0a — Is there a contract liability account, and does it move?**

Read the chart for deferred revenue or contract liability, and read its movement.

- **No such account, in an entity that bills in advance** — annual subscriptions, retainers, upfront licences — means **revenue is being recognised on invoice.** That is not a nuance; it is the standard not being applied. One read.
- **The account exists but never moves**, or moves only at year end in a single journal, means it is being estimated annually rather than operated.
- **It moves monthly in a clean pattern** — good. Proceed.

**Test 0b — Is there a contract asset account?**

An entity recognising revenue **over time** while billing on **milestones** must have contract assets — revenue earned ahead of the right to bill. **Over-time recognition with no contract asset anywhere means either everything bills in advance of performance, or unbilled revenue is not being recognised.** See percentage-of-completion accounting, which works the same balance from the other direction.

**Test 0c — Is revenue recognised in the same month as the invoice, every time?**

Compare invoice dates to revenue recognition dates across the population. **A perfect one-to-one match for every customer, every month, is invoice-basis recognition** — which is fine where every performance obligation is genuinely satisfied at the point of invoice, and is a material misstatement where it is not.

This test does not, on its own, tell you which. It tells you which question to ask, and it covers the whole population rather than the contracts somebody remembered.

**Test 0d — Does revenue include amounts collected for third parties?**

Step 3 is explicit: the transaction price **excludes amounts collected on behalf of third parties — sales taxes, VAT, GST.** `[auto]`: compare the revenue accounts against the tax accounts and the gross invoice values. **Revenue recorded gross of sales tax is overstated**, systematically, by the tax rate, and it distorts every margin and ratio computed from it. One comparison.

---

### Step 1 — Identify the contract with a customer

`[manual]` in substance. All five criteria preserved.

**A contract exists when:**

1. **Both parties have approved** the contract — written, oral, or implied by customary business practice
2. **Each party's rights** regarding the goods or services are identifiable
3. **Payment terms** are identifiable
4. The contract has **commercial substance**
5. **Collection of consideration is probable**

**None of the five are visible in a ledger.** A posted invoice is evidence that somebody in the business believed a contract existed. It is not the assessment.

**For each contract, document** — all six preserved: customer name; contract effective date and term; total consideration; payment terms; renewal and termination clauses; signatures or approval evidence. `[auto]` for the customer name as recorded; `[manual]` for the rest.

**Combinations.** Contracts entered into at or near the same time with the same customer **or its related parties** are combined where they were negotiated as a package, where consideration in one depends on the other, or where the goods and services form a single performance obligation. `[auto]` to surface the fact pattern — multiple contracts with one customer, contracts with customers who are also related parties, and the cross-entity case at Gate 1. `[manual]` to conclude.

**Probability of collection.** Under both standards collection must be **probable** for a contract to exist. If it is not, **defer recognition until cash is collected or the threshold is met.** Both use the word "probable," though IFRS is sometimes applied at a lower threshold in practice — **confirm with the user** rather than assuming they are identical in application.

`[auto]` supporting evidence, and it is genuinely useful: **the customer's payment history.** A customer who has never paid, or who is far outside normal terms, is evidence bearing on whether collection is probable — computed from settled invoices, with the caveats set out in the receivables ageing. It informs a judgment; it does not make one. And note the direction: **this test matters most for new contracts with existing slow payers**, which is precisely where the collectibility criterion bites and where nobody usually looks.

---

### Step 2 — Identify the performance obligations

**`[manual]`. This is contract analysis and the ledger has nothing to say about it.**

A performance obligation is a promise to transfer a **distinct** good or service, or a **series** of distinct goods or services that are substantially the same.

**A good or service is distinct if both:**

1. **The customer can benefit from it on its own** or with other readily available resources — *capable of being distinct*
2. **The promise is separately identifiable** from other promises in the contract — *distinct in the context of the contract*

**Both limbs. Failing the second while passing the first is the commonest error**, because the first is intuitive and the second is not: a good the customer could in principle use alone may still be so integrated with the rest of the contract that it is not separately identifiable within it.

**Common bundling questions** — all four preserved:

- Software licence + implementation + post-go-live support → distinct or bundled?
- Equipment + installation → distinct or bundled?
- Software + cloud hosting → distinct or bundled, especially for SaaS?
- A service contract with multiple service types

**A series of distinct services that are substantially the same** — daily cleaning, a monthly subscription — is a **single performance obligation with over-time recognition.**

**Immaterial promises** — trivial promotional items — may be ignored, **but document the assessment.**

**Customer options for additional goods or services**: assess whether the option confers a **material right** — a discount on future purchases the customer would not otherwise have received. **If so, the option is a separate performance obligation** and part of the transaction price is allocated to it. This is easy to miss and it moves revenue out of the current period.

**Output a numbered list of POs with the distinct-test reasoning for each.**

`[auto]` and the only contribution available here: **the invoice line descriptions**, as a starting inventory of what the business thinks it sold. **Invoice lines are a billing structure, not a performance obligation analysis** — they are built for the customer's purchase order, and a single line frequently contains several obligations while several lines frequently contain one. Use them as a checklist against the contract, never as the answer.

---

### Step 3 — Determine the transaction price

`[manual]` for the estimate; `[auto]` for two checks.

The transaction price is the consideration the entity **expects to be entitled to**. It **excludes amounts collected on behalf of third parties** — sales taxes, VAT — which Test 0d checks.

**Consider** — all five preserved:

| Type | Note | Verdict |
|---|---|---|
| **Fixed consideration** | The stated contract amount | `[manual]` from the contract |
| **Variable consideration** | Discounts, rebates, refunds, performance bonuses, penalties, contingent consideration | `[manual]` to estimate; `[auto]` for history — see below |
| **Significant financing component** | Where payment timing gives a significant financing benefit, typically more than a year before or after delivery. Adjust using a discount rate. | `[manual]` for the rate; `[auto]` to flag the timing gap |
| **Non-cash consideration** | Measured at fair value | `[manual]` — no valuations on this surface |
| **Consideration payable to the customer** | Generally **reduces** the transaction price, unless it is payment for a distinct good or service from the customer | **`[auto]` to detect** — see below |

**Variable consideration estimation** — both methods preserved:

- **Expected value**: the probability-weighted sum of possible amounts. For **many similar contracts.**
- **Most likely amount**: the single most likely outcome. For **binary or limited outcomes.**

**Apply the constraint**: include variable consideration **only to the extent it is highly probable that a significant revenue reversal will not occur** when the uncertainty resolves.

**Document**: the sources of variable consideration; the estimation method chosen and why; the constraint analysis, showing how much was included and how much excluded.

**Two `[auto]` contributions worth having:**

**Historical outturn on variable consideration.** Where the entity has run similar arrangements before, **the ledger holds what actually happened** — the rebates actually granted, the bonuses actually earned, the penalties actually suffered. That is direct evidence for an expected-value estimate and it is far better than an unaided guess. It does not make the estimate; it informs it, and it gives the constraint analysis something concrete to reason from.

**Consideration payable to the customer.** This is a real detection. `[auto]`: **look for payments made *to* a customer** — a name appearing in both the customer and vendor lists, credits and rebates posted to expense rather than against revenue, marketing or listing fees paid to a party who is also a customer. Under the standard these generally **reduce revenue**, and when they are sitting in operating expenses instead, **revenue is overstated and margin is misstated in both directions at once.** One read of two lists, and it also picks up the related-party pattern in the related party disclosures.

---

### Step 4 — Allocate the transaction price

`[auto]` for the arithmetic. **`[manual]` for the inputs — except the top of the hierarchy, which is a genuine recovery.**

Allocate to each PO on **relative standalone selling prices.**

#### The SSP hierarchy, and which level the ledger can supply

| Level | Method | Verdict |
|---|---|---|
| **1. Observable price** — where the entity **sells the good or service separately** to similar customers in similar circumstances | **`[auto]`** — see below | |
| **2. Estimated SSP** — adjusted market assessment approach | `[manual]` | |
| **2. Estimated SSP** — expected cost plus margin | `[auto]` in part for the cost; `[manual]` for the margin | |
| **2. Estimated SSP** — residual approach, **only where specific conditions are met**, typically where the price is highly variable or uncertain | `[manual]` | |

**Level 1 is a live read, and the original treats it as a user input.**

"Observable price when the entity sells the good or service separately to similar customers in similar circumstances" is a description of **the sales ledger.** If the entity does sell the item standalone, those transactions are in the books, with their customers, dates and prices. So:

- `[auto]`: **find standalone sales of the same item** — invoices containing that item and nothing else
- `[auto]`: **their price distribution**, with the count, the range and the central tendency
- `[auto]`: **whether the price is stable or highly variable**, which is itself the test that determines whether the residual approach is even available

That is a real and material contribution: the top of the SSP hierarchy, evidenced from the entity's own transactions, rather than asserted.

**Three caveats that must travel with it.** *"Similar customers in similar circumstances"* is judgment, and the ledger does not classify circumstances. **A price given inside a bundle is not a standalone price** — filter to invoices where the item was genuinely sold alone. And a handful of standalone sales is a thin population; report the count so the user can weigh it.

**For each PO:**

```
PO allocation = Transaction price x (SSP of this PO / Sum of all POs' SSPs)
```

`[auto]`.

**Discounts.** A contract discount is **generally allocated proportionally to all POs** on their SSPs. **Exception**: where there is observable evidence the discount relates only to specific POs, allocate it to those. `[manual]` for the evidence.

**Variable consideration** is **typically allocated to the PO or POs it relates to** — entirely, where it relates to one; on SSPs where it relates to several. `[manual]` to determine the relationship.

**Output a clear allocation table** showing each PO with its SSP, its percentage of total SSP, and its allocated transaction price. `[auto]`, and **verify the allocations sum to the transaction price** — a rounding residue left unallocated will not tie later.

---

### Step 5 — Recognise revenue when (or as) each PO is satisfied

`[manual]` for the determination. `[auto]` for the schedule once determined.

**Over time if any of the three criteria is met** — all three preserved:

1. **The customer simultaneously receives and consumes the benefits** as the entity performs — routine cleaning, subscription services
2. **The entity's performance creates or enhances an asset the customer controls** as it is created — construction on the customer's land
3. **The entity's performance does not create an asset with alternative use to the entity, AND the entity has an enforceable right to payment for performance to date** — custom-built equipment with progress billing rights

**Otherwise: point in time** — recognise when control transfers.

**For over-time recognition, choose a measure of progress:**

- **Output methods**: units delivered, milestones achieved, value-to-date
- **Input methods**: cost-to-cost, labour hours, machine hours, time elapsed

**Apply consistently. Document the method.** `[auto]` for cost-to-cost and time-elapsed where the underlying data is in the books; `[manual]` for output measures, which generally are not. See percentage-of-completion accounting for the cost-to-cost mechanics and its warnings about inefficient costs and uninstalled materials.

**For point-in-time recognition, identify the indicators of control transfer** — all five preserved:

- The entity has a **present right to payment**
- The customer has **legal title**
- The customer has **physical possession**
- The customer has the **risks and rewards** of ownership
- The customer has **accepted** the asset

`[auto]` for shipment and invoice dates where the surface holds them; `[manual]` for title, risk and acceptance, which are contractual.

**While a judgment is still open** — distinct or not, over time or at a point in time — build the
schedule under each answer, show the difference in revenue and in the contract balances, and ask which
applies. Never pick one silently.

**Build the recognition schedule:**

| Period | PO | Method | Progress % (if over time) | Cumulative Revenue | Period Revenue |

`[auto]` once the method and inputs exist.

#### A caution on "existing recognised revenue"

The Inputs table marks this `[auto]`, and it is — the ledger will tell you exactly what has been recognised to date. **It will not tell you whether that was right.**

Where this skill is applied mid-contract, there are two different questions and they must not be conflated:

- **What has been recognised?** `[auto]`, exact.
- **What should have been recognised?** The output of this analysis.

**Where they differ, that is a finding, not an opening balance.** Do not anchor the schedule to what is already in the books and roll forward from there — that silently adopts whatever was done before. Compute the correct cumulative position, compare it to the actual, and put the difference in front of someone. If it is material and relates to a prior reported period, see a restatement review.

---

### Step 6 — Contract assets, contract liabilities, and receivables

**`[auto]` in full**, once the recognition schedule exists. All three definitions preserved:

| Balance | Definition | Verdict |
|---|---|---|
| **Receivable (AR)** | An **unconditional** right to consideration. Booked when the invoice is issued, or when there is a right to payment regardless of further performance. | `[auto]` |
| **Contract asset** | The entity has performed but the right to consideration is **conditional on further performance** — not merely on the passage of time. Common in long-term projects with milestone billing. | `[auto]` |
| **Contract liability (deferred revenue)** | Consideration received, or an unconditional right to it, **before** transferring the goods or services. | `[auto]` |

At each reporting date:

```
Cumulative billings vs. Cumulative revenue earned

Billings > Revenue earned  -> Contract Liability (deferred revenue)
Billings < Revenue earned  -> Contract Asset (unbilled), or AR if an invoice has been issued
```

**The distinction between a contract asset and a receivable is the one most often collapsed**, and it is not cosmetic: a receivable is conditional only on time passing, a contract asset is conditional on doing more work. They carry different credit risk and, under IFRS, different impairment considerations. percentage-of-completion accounting makes the same point.

**And carry across that skill's presentation rule** `[auto]` to check: **do not net contract assets against contract liabilities across different contracts.** The position is determined per contract and presented separately. A single net figure hides both.

---

### Step 7 — Construct the entries

`[auto]` to draft. **`[manual]` to post.** Hand off to `journal-entry-builder`. All five preserved.

**Initial booking when the invoice is issued, cash received later:**
```
DR  Accounts Receivable                             $invoice amount inclusive of tax
    CR  Contract Liability / Deferred Revenue          $invoice amount excl. tax
    CR  Output Tax / VAT / GST Payable                 $tax
```

**Note what this entry does and does not do**: it creates a receivable and a **liability**. It does not create revenue. This is the entry Test 0a looks for, and its absence is the signature of invoice-basis recognition.

**Periodic revenue recognition:**
```
DR  Contract Liability / Deferred Revenue           $period revenue
    CR  Revenue                                       $period revenue
```

**Over-time revenue recognised but not yet billed:**
```
DR  Contract Asset (Unbilled AR)                    $earned not billed
    CR  Revenue                                       $earned not billed
```

**When the unbilled amount becomes billable:**
```
DR  Accounts Receivable                             $billed
    CR  Contract Asset                                $earned previously
    CR  Output Tax Payable                            $tax
    CR  Revenue                                       $any additional earned with billing
```

**Variable consideration true-ups.** At each reporting date, **re-estimate.** Differences flow through revenue — **catch-up for already-completed POs; prospective for those in progress.**
```
DR/CR  Revenue                                      $change in estimate
    CR/DR  Contract Liability / Refund Liability       $change
```

---

### Step 8 — Contract modifications

`[manual]` to assess. `[auto]` to compute once assessed. All three treatments preserved.

| Treatment | When | Effect |
|---|---|---|
| **A separate contract** | The modification adds **distinct** goods or services **at their standalone selling price** | Account for separately; **no change to the original contract** |
| **Termination of the existing contract and a new one** | The remaining goods or services **are distinct** from those already delivered | The **unrecognised portion plus the modification fee** is reallocated to the remaining POs |
| **Continuation of the existing contract** | The remaining goods or services are **not distinct** | **Cumulative catch-up adjustment** to revenue, on the updated transaction price and progress |

> **Document the modification, the assessment, and the resulting accounting.**

**Note that both conditions matter for the first treatment** — distinct **and** at SSP. A modification adding distinct services at a discount is not a separate contract, and treating it as one is a common error that leaves the discount unallocated.

`[auto]` for the signal: **a change in the billing amount or cadence for an existing customer** is where a modification has probably occurred. The ledger sees the consequence; the modification document says which of the three treatments applies.

---

### Step 9 — Contract costs

Both categories under ASC 340-40 / IFRS 15 preserved — **and this is a strong `[auto]` detection.**

| Category | Treatment | Verdict |
|---|---|---|
| **Incremental costs of obtaining a contract** — sales commissions paid only on a win | **Capitalise if recoverable**, amortise over the period of benefit. **Practical expedient** available where the amortisation period would be one year or less. | `[auto]` to detect; `[manual]` for the policy |
| **Costs to fulfil a contract**, where not covered by another standard | Capitalise where they relate directly to a contract, generate or enhance resources used to satisfy POs, and are expected to be recovered. Amortise as the POs are satisfied. | `[auto]` in part |

**Build the capitalised cost schedule and the amortisation schedule.** `[auto]` once the policy is set.

#### The commission test

`[auto]`, one read, and it finds a genuine and common failure.

**An entity with multi-year customer contracts, paying sales commissions on contract wins, expensing all of them immediately, with no contract cost asset on the balance sheet, is either:**

- properly applying the **one-year practical expedient** — which is a legitimate election, or
- **not applying ASC 340-40 at all.**

The two look identical in the accounts and are entirely different in substance. The test: **read the commission expense and the contract terms.** Where contracts run for three years and commissions are expensed on day one with no expedient documented, the costs of obtaining those contracts are being recognised in the wrong period — and the effect is largest for a growing business, which is when it matters most.

**Ask which it is.** The answer belongs in the profile, because it is a policy election that must be applied consistently.

---

### Step 10 — Disclosure-relevant data

All four areas preserved.

| Disclosure | Verdict |
|---|---|
| **Revenue disaggregation** — by product line, geography, customer type, timing of recognition; **the entity decides which** | **`[auto]` where those are dimensions in the book; `[manual]` where they are not.** Read the dimension list rather than assuming — the same binary as segments in `quarter-end-close`. |
| **Contract balances** — opening and closing AR, contract assets, contract liabilities | **`[auto]`** — a roll-forward, every component readable |
| **Significant judgments** — transaction price, allocation, timing | `[manual]` |
| **Remaining performance obligations** — the transaction price allocated to unsatisfied POs, and the expected timing | **`[manual]`.** See the near-substitute note: **RPO is not the deferred revenue balance**, because it includes committed amounts not yet billed. |

Feed into the notes to the financial statements.

---

### Step 11 — Output

An `.xlsx` workpaper. All ten of the original's sheets, plus two additions.

**Sheet 1: Contract Summary** — customer, contract number, dates, total transaction price, numbered POs, recognition method per PO, key judgments.

**Sheet 2: Five-Step Analysis** — each step documented with the entity's reasoning. **`[manual]` content in an `[auto]` structure**; Mosofin does not fill in the judgments.

**Sheet 3: SSP and Allocation**
| PO | SSP | Source (observable / estimated method) | % of total | Allocated TP |

**Add an Observations count column** where the SSP came from observable standalone sales — a price supported by three transactions is not a price supported by three hundred, and the reader needs to see which.

**Sheet 4: Recognition Schedule** — period, PO, method, progress %, cumulative and period revenue, across all periods of the contract. `[auto]`.

**Sheet 5: Contract Balances Roll-Forward** — by period: AR opening / billings / receipts / closing; Contract Asset opening / additions / billing transfers / closing; Contract Liability opening / receipts / revenue / closing. **`[auto]`, in full.**

**Sheet 6: GL Postings** — each period's entries. Marked **PROPOSED — NOT POSTED.**

**Sheet 7: Variable Consideration / Constraint Analysis** — with the historical outturn from Step 3 where available.

**Sheet 8: Modifications** — the analysis and its accounting impact.

**Sheet 9: Contract Costs** — capitalised costs and amortisation, **with the commission test result from Step 9.**

**Sheet 10: Disclosure Inputs** — with **RPO marked as requiring unbilled commitment data.**

**Sheet 11: Standard Application Tests** *(Mosofin addition)* — the Step 0 results:

| Test | Finding | Evidence | Population | Recommended action |
|---|---|---|---|---|

Contract liability present and moving. Contract asset present where over-time recognition exists. Invoice-date versus recognition-date match rate. Revenue gross of sales tax. Consideration payable to customers sitting in expense. Commission treatment.

**Sheet 12: Coverage and Provenance** *(Mosofin addition)* — the mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `RevRec_[Customer]_[ContractNumber]_[YYYY-MM-DD].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All twelve preserved.

- **The five-step analysis is complete and documented per contract.** `[manual]` content.
- **Performance obligations identified with the distinct-test reasoning** — **both limbs.** `[manual]`
- **SSP source disclosed for each PO.** `[auto]` where observable, **with the observation count**; `[manual]` where estimated.
- **Allocation arithmetic verified**, and the allocations sum to the transaction price. `[auto]`
- **Recognition method supported by the criteria met** — the specific criterion, named. `[manual]`
- **Variable consideration: estimation method, constraint application and reassessment cadence documented.** `[manual]`, with `[auto]` historical outturn as evidence.
- **All entries balance.** `[auto]`
- **Contract-balance roll-forwards tie.** `[auto]`, **and contract assets are not netted against contract liabilities across contracts.**
- **Modifications, costs to obtain and fulfil, and refund liabilities addressed where present.** `[auto]` to detect; `[manual]` to treat.
- **Framework consistency** — under ASC 606, no IFRS 15-only expedients, and vice versa. `[manual]`
- **File naming consistent.** `[auto]`
- **No assumption substituted for entity judgment — the entity owns the call; this skill documents and applies it.** **`[manual]`, and it is the standard that governs all the others.**

**Four Mosofin additions:**

- **Step 0 runs before any contract analysis.** A perfect analysis of one contract is worth little in books that recognise on invoice.
- **What was recognised and what should have been are reported separately**, never merged into an opening balance.
- **Revenue is tested for third-party amounts** — sales tax in revenue is one comparison and a systematic overstatement.
- **Every figure is attributed** — ledger-read, contract-derived, or estimated.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — and **any SSP.** Standalone selling prices move with the entity's pricing, and an SSP persisted for two years will silently misallocate every new contract.

**What is worth persisting into the workspace-scoped skill:**

1. **The framework and every practical expedient elected**, since consistency is itself a quality standard and an auditor will test it.
2. **The performance obligation library** — this entity's recurring PO patterns and the distinct-test reasoning already agreed. Most businesses sell a handful of contract shapes repeatedly, and re-deriving the analysis for each new contract of a known shape is the largest avoidable cost in this skill.
3. **The SSP *methodology* per PO type** — which level of the hierarchy, and how derived. **The method, not the price.**
4. **The account structure**: revenue, deferred revenue, contract assets, contract costs, refund liabilities.
5. **Whether disaggregation dimensions exist in the book**, which flips Step 10 between `[auto]` and `[manual]`.
6. **The commission policy** and whether the one-year expedient is elected.
7. **Historical variable-consideration outturn**, which is the evidence base for future estimates and improves with every period.
8. **Step 0 findings and their resolutions**, so the tests re-run against a known baseline.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — customer names, contract terms and pricing are commercially sensitive.

**The evolved version's interview should be about what is different in this contract**, against a library of shapes already analysed — not about the five steps from scratch.

---

## Anti-patterns

- **Building the schedule from invoice dates.** That is a billing schedule. The standard exists because the two differ.
- **Reporting deferred revenue as RPO.** RPO includes unbilled commitments.
- **Skipping Step 0.** A meticulous analysis of one contract, in books that recognise on invoice, changes nothing.
- **Anchoring to what has already been recognised.** Compute what should have been, then compare.
- **Applying only the first limb of the distinct test.** Separately identifiable *within the contract* is the limb that does the work.
- **Reading performance obligations off invoice lines.** Invoice lines are built for a purchase order.
- **Leaving sales tax in revenue.** One comparison; a systematic overstatement.
- **Leaving consideration payable to a customer in operating expenses.** It generally reduces revenue.
- **Expensing commissions on multi-year contracts** without establishing whether the expedient applies.
- **Netting contract assets against contract liabilities** across different contracts.
- **Calling a contract asset a receivable.** One is conditional on time; the other on doing more work.
- **Recording an agent arrangement gross.** Thin, stable margin against a single matching supplier cost is the signature — ask.
- **Treating a discounted modification as a separate contract.** Distinct *and* at SSP; both.
- **Persisting an SSP.** Persist how it is derived.
- **Letting FX movement into the revenue line.**
- **Recognising on renewal probability.** Only what was delivered.
- **Substituting an assumption for the entity's judgment.** The entity owns the call; this skill documents and applies it.
- **Saying "posted".** The gateway reads.
