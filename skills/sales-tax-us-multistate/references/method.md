<!-- sales-tax-us-multistate · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Nexus determination
- Step 1b — The exposure join *(Mosofin addition)*
- Step 2 — Registration obligations
- Step 3 — Taxability determination
- Step 4 — Rate application
- Step 5 — Exemptions
- Step 6 — Use tax
- Step 7 — Return preparation
- Step 8 — Reconciliation
- Step 9 — Marketplace facilitator sales
- Step 10 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. **Mosofin files no return, registers with no state, and remits nothing.**

---

## Inputs

All nine preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| States/jurisdictions of activity | List | **Required** | **Derivable from ship-to addresses** — with the address caveat above | `[auto]` in part |
| **Sales by state (and locality)** | Revenue, transaction count, by period | **Required for nexus and returns** | **Live read — both the value and the count** | `[auto]` |
| **Physical presence facts** | Offices, employees, inventory, property by state | **Required for nexus** | **Not in the books.** Payroll may hint at employee states; inventory location does not appear at all. | `[manual]` |
| Product/service descriptions | What is being sold | **Required for taxability** | Item names and descriptions are readable; **they are not a taxability classification** | `[auto]` in part |
| **Current economic nexus thresholds per state** | $ and/or transaction count | **Required — user-supplied or confirmed current** | **Never from this file. Never carried forward.** | `[manual]` |
| **Current rates per jurisdiction** | State + local combined | **Required — user-supplied or confirmed current** | **Never from this file.** | `[manual]` |
| Exemption certificates on file | Resale, exempt entities | Recommended | **The certificates are documents.** The exempt *sales* are a live read — which is what makes the gap analysis work. | `[manual]` + `[auto]` |
| Marketplace sales | Sold through Amazon, eBay, etc. | Recommended | **Often traceable** — marketplace settlements look different from direct invoices | `[auto]` in part |
| Registration status per state | Where already registered | Recommended | Not in the books; **persist it** | `[manual]` |

---

## Workflow

### Step 1 — Nexus determination

**The step where the workspace contributes most, and it contributes the half that carries the money.**

Nexus is the connection that obligates a seller to collect a state's sales tax. Two types, both preserved.

#### Physical nexus — `[manual]`

Presence in the state:

- **Office, store, warehouse or other property**
- **Employees, contractors or agents**
- **Inventory stored in the state**, including third-party fulfilment such as FBA
- **Sometimes**: trade show attendance, deliveries in the entity's own vehicles

**None of this is in a general ledger.** Payroll may indicate which states employees are paid in, which is a hint and not a determination. **Inventory location — the most commonly overlooked physical-nexus trigger — is invisible**: a ledger records that inventory exists and what it cost, never where it is sitting. See the FBA edge case.

#### Economic nexus (post-*Wayfair*, 2018) — **`[auto]` for the measurement**

Exceeding a sales or transaction threshold in the state, **even without physical presence.**

- **Each state sets its own threshold** — commonly a revenue figure and/or a transaction count
- **Thresholds and measurement periods vary and change** — **confirm the current threshold for each state; do not assume a figure**

**What the workspace computes, exactly** `[auto]`:

| Measure | Note |
|---|---|
| **Sales by state, by period** | The revenue half of the test |
| **Transaction count by state, by period** | **The other half — and the one that gets forgotten.** Several states set a count threshold that a low-value, high-volume seller crosses long before the dollar threshold. Counting invoices is trivial and nobody does it. |
| **Rolling and prior-calendar-year totals** | Because measurement periods differ by state, compute both bases and let the threshold decide which applies |
| **The month each threshold was crossed** | **See below — this is the most valuable single output.** |

**For each state, document** — all three preserved:

- Physical presence facts → **physical nexus Y/N** — `[manual]`
- Sales and transaction counts against the current threshold → **economic nexus Y/N** — `[auto]` once the threshold is supplied
- **The date nexus was established**, which triggers the registration and collection obligations — **`[auto]`**

#### The trigger date, and why it is the point of the whole exercise

`[auto]`, and it deserves its own passage.

A nexus map that says "you have nexus in Ohio" is useful. A nexus map that says **"you crossed Ohio's threshold in the week ending 14 March 2024, and you have made 1,847 taxable sales into Ohio since then on which no tax was collected"** is a different document entirely — because **the trigger date determines the exposure period**, and the exposure period determines the number that matters.

The computation is exact and it is arithmetic: walk the state's sales and counts forward through time against the supplied threshold and find the crossing. **In manual practice this is rarely done properly**, because it needs the full transaction history sliced by state and month, which is tedious by hand and instant against a live ledger.

**Output a nexus map**: states with nexus, the basis, and the trigger date.

---

### Step 1b — The exposure join *(Mosofin addition)*

**`[auto]`, one join, and it is the finding that usually justifies the engagement.**

Cross the nexus map against the registration list:

| Situation | Meaning |
|---|---|
| **Nexus, registered, collecting** | Correct. Verify rates and taxability. |
| **Nexus, registered, not collecting** | A collection failure. The entity owes tax it did not charge. |
| **Nexus, NOT registered** | **Live exposure.** Back tax from the trigger date, plus interest and potentially penalties. **This is the row that matters.** |
| **No nexus, registered and collecting** | Over-collection in a state with no obligation — remittance is still required, but the position should be reviewed. |
| **Approaching the threshold** | **Not yet an obligation, and the most useful row on the sheet.** A state at 80% of threshold is a registration to plan, not a liability to discover. |

**Quantify the exposure per state**: taxable sales since the trigger date, at the applicable rate, as an **indicative** figure. It is indicative because it depends on taxability determinations that are `[manual]` — say so — but an indicative number is what tells the client whether this is a Step 2 conversation or a specialist conversation.

**And report the approaching-threshold row prominently.** Every skill in this pack finds problems after they happen; this is one of the few places where the same data prevents one.

---

### Step 2 — Registration obligations

`[manual]`, with `[auto]` inputs.

For each nexus state where the entity is not yet registered:

- **Registration is generally required before collecting tax**
- **Some states have past-liability exposure where nexus existed before registration** → consider **voluntary disclosure agreements (VDAs)** to limit the look-back
- **Flag states with potential historical exposure for specialist review**

`[auto]` supplies the two facts a VDA conversation needs: **how far back the exposure runs** (the trigger date) and **how large it is** (the indicative quantification). **`[manual]` for everything else** — a VDA is a negotiated agreement with a state revenue department, and the decision to enter one has consequences that are not accounting consequences.

**Flag early, not at the end.** Registering in a state before addressing historical exposure can forfeit the ability to negotiate a limited look-back, so the sequencing matters and it is a specialist call.

---

### Step 3 — Taxability determination

**`[manual]`, entirely and without qualification.** This is the part of US sales tax that cannot be computed.

For each product or service in each nexus state, determine taxability. All six categories preserved:

| Category | Note |
|---|---|
| **Tangible personal property** | Generally taxable, with exceptions |
| **Services** | **Taxability varies wildly by state** — many states tax few services; some tax many |
| **Software** | **SaaS taxability differs by state** — taxable in some, exempt in others, sometimes turning on the delivery method |
| **Digital goods** | State-specific rules |
| **Food, clothing, medical** | Often exempt or reduced, state-specific |
| **Shipping and handling** | Taxable in some states, not others, **sometimes depending on whether it is separately stated** |

**Build a taxability matrix**: product/service × state → taxable / exempt / reduced. **Source each determination from current state guidance — do not assume taxability; flag uncertain items for confirmation.**

**The workspace's only contribution here is the population** `[auto]`: **the complete list of items actually sold, and into which states.** That is genuinely useful — it bounds the matrix to what the entity really sells rather than to what somebody remembered, and it prevents the classic gap where a minor product line is never assessed at all.

**It is a list of things to determine, not a set of determinations.** And per the near-substitute note: **do not read taxability off the existing tax codes.** Those record a past configuration decision, which is precisely what is being tested.

---

### Step 4 — Rate application

`[manual]` for the rates. `[auto]` to validate what was applied.

For each taxable transaction:

- **Apply the correct combined rate** = state + county + city + special district
- **Most states are destination-based** (the rate at the ship-to location); some are origin-based — **confirm per state**
- **Rates change frequently and local rates are granular** — ZIP+4 or address level
- **Use current rates from the user or a current rate source; do not hardcode rates**

> **For high transaction volumes, recommend automated tax-rate determination — the entity likely uses, or should use, a tax engine. This skill validates and reconciles rather than serving as the real-time rate engine.**

**Preserved with emphasis, and it is the correct scoping for a read-only tool.** Address-level rating across thousands of jurisdictions, in real time, at the point of sale, is a job for dedicated software. Mosofin's role is to check the result.

**What checking the result looks like** `[auto]`:

- **The effective rate actually charged, by state and by period** — total tax collected over taxable sales. Compare it against the expected combined rate. A state where the effective rate is materially below expectation has transactions that were not rated.
- **Taxable sales with no tax charged at all.** The clearest possible signal — the engine was not invoked, or the transaction bypassed it.
- **Effective rates that drift over time** in a state, which is either genuine rate change or a configuration that stopped being maintained.

None of these determine the correct rate. All of them find transactions where **something** went wrong, which is the entire population a rate review needs to look at.

---

### Step 5 — Exemptions

All three types preserved. **`[manual]` for the certificates; `[auto]` for the gap analysis, which is the valuable half.**

- **Resale**: the buyer provides a resale certificate; the sale is exempt. **Validate the certificate is current and valid for the state.**
- **Exempt entities**: government, nonprofits, certain organisations — **with valid exemption documentation.**
- **Exempt use**: manufacturing inputs, agricultural, and so on — state-specific.

**Track exemption certificates**: which customer, which state, expiration, validity.

> **Missing or expired certificates = the entity may owe the tax it did not collect.**

#### The certificate gap analysis

`[auto]` once the register is supplied — and the register only needs supplying **once**, because it persists.

**Read every sale treated as exempt**, by customer and state. Then join to the certificate register:

| Finding | Meaning |
|---|---|
| **Exempt sale, no certificate on file** | **The entity owes the tax.** The exemption is only as good as the documentation behind it. |
| **Exempt sale, certificate expired at the transaction date** | Same. Expiry dates are the commonest failure, because the sale keeps flowing after the certificate lapses. |
| **Certificate for the wrong state** | A certificate is state-specific; one from another state does not support the exemption. |
| **Certificate valid, sale exempt** | Correct. |

**This is a full-population join and it is one query.** In manual practice it is sampled, and sampling misses exactly the long-tail customer whose certificate expired three years ago and whose exempt sales have continued ever since.

**One honest limit**, consistent with `related-party-disclosures-asc850`: the join is exhaustive over *sales*, and the register is only as complete as what the client supplied. **A certificate that exists in a filing cabinet and not in the register will show as a gap** — which is a prompt to look, not a conclusion that tax is owed. Report gaps as items to resolve.

---

### Step 6 — Use tax

**`[auto]` for the population, and this is the most-ignored liability in the skill.**

Use tax is the complement to sales tax — **owed by the buyer when sales tax was not collected on a taxable purchase.**

Review the entity's own purchases. All three sources preserved:

| Source | Mosofin read | Verdict |
|---|---|---|
| **Purchases where no sales tax was charged but the item is taxable in the use state** | **Read the purchase ledger for bills with no tax line.** A complete, computable population. | `[auto]` for the population, `[manual]` for taxability |
| **Inventory items consumed internally** | Inventory withdrawn to expense rather than sold — readable where the coding distinguishes it | `[auto]` in part |
| **Fixed assets purchased from out-of-state vendors** | **Readable, and typically the largest individual items** | `[auto]` |

**Compute use tax owed.** `[auto]` for the arithmetic once taxability and rates are supplied.

**Why this matters disproportionately.** Use tax is self-assessed, nobody invoices for it, and no system prompts it — so it is simply not done in a great many businesses. It is also **exactly what a state auditor looks at first**, because it is easy to find and reliably productive: they pull the fixed asset additions and the untaxed purchase ledger, which is the same population computed here.

**Finding it first is straightforwardly better than a state finding it**, and the read is one query.

---

### Step 7 — Return preparation

`[auto]` for the figures. **`[manual]` to file.**

For each state and filing period, all seven line items preserved:

| Line | Verdict |
|---|---|
| **Gross sales** | `[auto]` |
| **Exempt sales (by reason)** | `[auto]` for the amounts; `[manual]` for the reason coding |
| **Taxable sales** | `[auto]` once taxability is determined |
| **Tax collected (by jurisdiction/rate)** | `[auto]` at whatever granularity the ledger holds — **often less granular than the return requires**; see the local-rate edge case |
| **Use tax owed** | `[auto]` for the population, `[manual]` for taxability |
| **Credits, discounts** — some states give a timely-filing discount — **and prior-period adjustments** | `[manual]` for the discount rules; `[auto]` for prior-period adjustments |
| **Net tax due** | `[auto]` |

**Filing frequency — monthly, quarterly or annual — is assigned by each state based on volume. Confirm per state.** `[manual]`. And note it **changes**: a state will move a growing seller from quarterly to monthly, and missing that notification is a straightforward late-filing penalty.

**Mosofin prepares figures. It does not file a return.** The gateway is read-only, and a tax filing is a legal act.

---

### Step 8 — Reconciliation

**`[auto]` for two of the four legs, and one of them produces the most serious finding in the skill.**

Reconcile tax collected per the billing or POS system to — all three preserved:

| Target | Verdict |
|---|---|
| **Tax payable in the GL** | **`[auto]`** — see `balance-sheet-reconciliations` |
| **Tax remitted on returns** | `[manual]` — the returns are documents |
| **Tax that should have been collected**, per the taxability matrix and rates | `[auto]` once the matrix and rates are supplied |

**Identify** — all three preserved:

- **Under-collection** — the entity owes the difference. **It cannot go back and charge past customers**, so this is funded out of margin.
- **Over-collection** — **must be refunded to customers or remitted. It cannot be kept.** `[auto]` to detect, by comparing collected against computed.
- **Timing differences** — collected in one period, remitted in the next. Normal, and must be distinguishable from the next item.

#### The collected-not-remitted test

`[auto]`, one read, and it needs stating carefully because of what it means.

**Read the sales tax payable account's movement.** In a properly running business it fills up and empties on the filing cycle — collections in, remittances out, a sawtooth.

**A sales tax payable balance that only grows is tax that was collected from customers and has not been sent to the state.**

That is not an ordinary accounting variance. **Sales tax collected is generally held as trust money** — the entity collected it as agent for the state, from the customer, and it was never the entity's money. Most states treat non-remittance far more seriously than an underpayment of the entity's own tax, and many impose **personal liability on responsible persons** for collected-and-unremitted tax, which does not disappear in an insolvency.

**Report it factually, with the balance, the growth pattern and the periods involved.** State plainly why it is treated differently from other payables. **Never as an allegation** — the overwhelming majority of cases are a business under cash pressure that intended to catch up, or a filing that was simply missed. It is precisely because the consequences are severe and the cause is usually mundane that it should be raised early and plainly.

---

### Step 9 — Marketplace facilitator sales

`[auto]` in part to separate; `[manual]` per state. All three points preserved — **and the third contains a trap.**

- **Most states now require the marketplace facilitator to collect and remit on the seller's behalf.**
- **These sales typically should NOT be included in the seller's own returns as taxable**, to avoid double taxation.
- **But they may still count toward nexus thresholds.** — **Confirm per state.**

**The trap is the third bullet and it runs opposite to intuition.** A seller whose Amazon sales are collected on by Amazon may reasonably think those sales are Amazon's problem entirely. In several states **they still count toward the seller's own economic nexus threshold** — so marketplace volume can establish nexus that then obliges the seller to register and collect on their **direct** sales into that state.

**The consequence for Step 1 is concrete: run the threshold test on total sales including marketplace volume, and the return figures on direct sales only.** Two different populations for two different purposes, from the same data. Getting this backwards understates nexus and overstates the return.

`[auto]` to trace: **marketplace settlements look different from direct invoices** — periodic net deposits from a single counterparty, often with fees netted, rather than customer-by-customer invoices. Where the ledger distinguishes them, the split is readable. Where marketplace revenue is booked as a single monthly deposit **with no state detail behind it**, the state-level split is not in the books at all and must come from the marketplace's own reports. **Say which situation applies** — it materially changes what the nexus map can claim.

---

### Step 10 — Output

An `.xlsx` workpaper. All seven of the original's sheets, plus two additions.

**Sheet 1: Nexus Map**
| State | Physical Nexus | Economic Nexus | Threshold (current) | Sales vs Threshold | Transaction Count vs Threshold | Nexus Date | Registered? | Action |

**Transaction count added as its own column** — it is a separate threshold and hiding it inside "sales vs threshold" is how it gets missed. **Threshold column carries its source and confirmation date.**

**Sheet 2: Taxability Matrix**
| Product/Service | State | Taxable/Exempt/Reduced | Rate Basis | Source | Confidence |

`[manual]` content. **Mosofin fills the Product/Service and State columns from the actual sales population and leaves the determination columns empty.**

**Sheet 3: Return Figures by State**
| State | Period | Gross Sales | Exempt | Taxable | Tax Collected | Use Tax | Adjustments | Net Due |

**Direct sales only** — marketplace-facilitated sales excluded, per Step 9, and shown separately.

**Sheet 4: Reconciliation**
Collected versus GL versus remitted versus should-have-collected. **With the collected-not-remitted test result.**

**Sheet 5: Exemption Certificate Register**
| Customer | State | Certificate Type | Expiration | Valid? | Exempt sales in period | Gap? |

**Last two columns are the Mosofin addition** — the register alone lists certificates; joined to actual exempt sales it becomes an exposure analysis.

**Sheet 6: Use Tax**
Purchases triggering use tax. `[auto]` population, `[manual]` taxability.

**Sheet 7: Open Items / Confirmations Needed**
**Rates, thresholds and taxability calls flagged for current-source confirmation.** Every `[manual]` item in the run appears here.

**Sheet 8: Exposure Summary** *(Mosofin addition)*
The Step 1b join, ranked by amount:

| State | Nexus basis | Trigger date | Registered? | Sales since trigger | Indicative exposure | Approaching threshold? | Action |
|---|---|---|---|---|---|---|---|

**Including the approaching-threshold states**, which are the only preventive rows in the document.

**Sheet 9: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet — **including which address field was used**, per the near-substitute note.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Sales_Tax_Multistate_[Period]_[EntityName].xlsx`

Entity `display_name` in the file name and on every sheet — nexus is per entity. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All ten preserved.

- **Nexus determined per state with basis and trigger date.** `[auto]` for economic nexus and the trigger date; `[manual]` for physical presence.
- **No hardcoded thresholds, rates or taxability rules — all user-supplied or current-sourced, with sources noted.** `[manual]`. **Nothing persisted supplies one either.**
- **Taxability matrix with source and confidence per determination.** `[manual]`; `[auto]` for the population it must cover.
- **Return figures reconcile to collected and to GL.** `[auto]` for both legs available.
- **Marketplace-facilitated sales separated from direct sales** — **and still counted toward thresholds where the state requires.** `[auto]` in part.
- **Use tax reviewed on the entity's purchases.** **`[auto]` for the population** — the same population a state auditor pulls first.
- **Exemption certificates tracked with validity.** `[manual]` register; **`[auto]` full-population gap join.**
- **Uncertain items flagged for current-source confirmation, not assumed.** `[manual]`, Sheet 7.
- **File naming consistent.** `[auto]`
- **Recommendation to use or validate a tax engine for high-volume real-time rating.** **Mosofin validates and reconciles; it is not a rate engine.**

**Four Mosofin additions:**

- **The address field used is stated.** Billing versus ship-to changes the whole state analysis.
- **Transaction count is tested as a separate threshold**, not folded into the revenue test.
- **The exposure join runs every time**, including the approaching-threshold rows.
- **The collected-not-remitted test runs every time**, and is reported plainly.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and any rate, threshold or taxability rule.** The original says so and it is the whole discipline of the skill.

**What is worth persisting into the workspace-scoped skill:**

1. **The registration list with dates.** This is the join that turns sales data into an exposure analysis, and without it Step 1b cannot run at all.
2. **Physical presence facts**, including **where inventory sits** — the fact the ledger will never supply and the one that most often creates unexpected nexus.
3. **The exemption certificate register.** Supplied once, joined every period thereafter. High effort to gather, and it makes the gap analysis automatic from then on.
4. **The taxability matrix, with sources and dates** — **as a record of what was determined and when, explicitly to be re-confirmed**, not to be reused unexamined. Store the determination *and* its age, so a stale one is visible.
5. **Which address field the book holds**, and whether ship-to detail exists.
6. **Marketplace channels** and whether their state-level detail is available.
7. **Filing frequencies per state**, and the date each was last confirmed.
8. **Trigger dates already established**, which do not change and are expensive to recompute.
9. **Findings and their resolutions** — certificate gaps closed, exposures addressed, VDAs entered.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed.**

**Store the sources and their dates, never the values.** That is the difference between a skill that gets faster and one that gets wrong.

**The evolved version's monthly job is short and valuable**: which states moved closer to a threshold, which crossed one, whether the payable account is emptying on schedule, and which certificates expired this month.

---

## Anti-patterns

- **Computing state-by-state sales from billing addresses** in destination-sourced states. Say which field was used.
- **Testing only the revenue threshold.** The transaction count is a separate test and low-value high-volume sellers cross it first.
- **Reading taxability off existing tax codes.** Those are a past configuration decision — the thing being tested.
- **Excluding marketplace sales from the nexus test.** They may still count toward the threshold even when the facilitator collects.
- **Including marketplace sales in the return as taxable.** Double taxation.
- **Combining entities in one threshold test.** Nexus is per legal entity.
- **Sampling the exemption certificate file.** The join is exhaustive and free; sampling misses the long-tail expiry.
- **Skipping use tax.** It is the first thing a state auditor pulls.
- **Treating a growing sales tax payable as an ordinary accrual.** Collected tax is trust money and is treated differently.
- **Registering before assessing historical exposure.** Sequencing affects what a VDA can achieve.
- **Assuming filing frequency is stable.** States move growing sellers to monthly.
- **Preparing a home-rule local return from state-level tax codes.** The granularity is not there.
- **Carrying a threshold or rate forward from a prior run.** The original forbids it; so does this file.
- **Acting as a rate engine.** Validate and reconcile; recommend proper software for real-time rating.
- **Saying "filed" or "remitted".** The gateway reads.
