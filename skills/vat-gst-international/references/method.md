<!-- vat-gst-international · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Determine registration obligations
- Step 2 — Determine place of supply
- Step 3 — Output VAT (VAT on sales)
- Step 4 — Reverse charge
- Step 4b — The reverse-charge net-nil detection *(Mosofin addition)*
- Step 5 — Input VAT (VAT on purchases)
- Step 5b — The partial exemption consequence test *(Mosofin addition)*
- Step 6 — Special schemes
- Step 7 — Return preparation
- Step 8 — Reconciliation
- Step 9 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. **Mosofin files no return, registers in no country, and remits nothing.**

---

## Inputs

All nine preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Countries of activity** | List | **Required** | **Derivable in part** from customer and supplier countries | `[auto]` in part |
| **Sales (outputs) by country, customer type, product** | B2B/B2C, goods/services, amounts | **Required** | **`[auto]` for amounts and country; B2B/B2C depends on whether customer status is recorded** | Split |
| **Purchases (inputs) with VAT incurred** | By country, with VAT amounts | **Required for input recovery** | **`[auto]`** | `[auto]` |
| **Business establishment facts** | Where established, fixed establishments | **Required** | **Not in the books.** A fixed establishment is a factual test about presence. | `[manual]` |
| **Current VAT/GST rates per country** | Standard, reduced, zero | **Required** | **Never from this file** | `[manual]` |
| **Current registration thresholds per country** | | **Required** | **Never from this file** | `[manual]` |
| Customer VAT/GST registration numbers | For B2B cross-border | Recommended | **`[auto]` to see which are recorded; `[manual]` to validate** | Split |
| Import/export documentation | Customs, shipping terms | Recommended | **Customs documents are not on this surface** | `[manual]` |
| Registration status per country | Where already registered | Recommended | Not in the books; **persist it** | `[manual]` |

---

## Workflow

### Step 1 — Determine registration obligations

`[manual]` for the rules; **`[auto]` for the measurement.**

**Registration is triggered by** — all three preserved:

- **Establishment** in a country — a local business generally registers
- **Exceeding a registration threshold** of local taxable turnover — **threshold varies by country; some have a nil threshold for non-established businesses**
- **Specific activities** — distance selling of goods, supplying digital services to consumers

**For each country, assess** — all three:

- **Is the entity established there?** `[manual]`
- **Does local taxable turnover exceed the current threshold?** — **confirm the current threshold; do not assume.** **`[auto]` for the turnover**, by country, per period, once countries are identifiable.
- **Do special rules force registration** — a non-established taxable person making local supplies? `[manual]`

**Document registration obligations and dates.**

**Two differences from the US analysis worth naming**, because the instinct carries over wrongly from `sales-tax-us-multistate`:

**The nil threshold changes the question.** For a non-established business, many countries impose registration from the **first** taxable supply. **So the test is not "did turnover exceed a level" but "were there any local supplies at all"** — which is a different query and a much lower bar. `[auto]` to find any supply in a country; `[manual]` for whether the nil threshold applies.

**Establishment is not a transaction.** It is a factual test about premises, people and permanence, and **nothing in a ledger determines it.** `[auto]` supplies weak circumstantial evidence — local payroll, local premises costs, local bank accounts — which is worth surfacing because a business that pays rent and salaries in a country probably has an establishment there, and may not have registered.

**`[auto]` exposure join, exactly as in the US skill**: countries with supplies, crossed against the registration list. **Countries with taxable supplies and no registration are exposure**, and **countries approaching a threshold are the preventive row.**

---

### Step 2 — Determine place of supply

**`[manual]`. The foundation of VAT, and the ledger does not contain it.**

> **The place-of-supply rules determine WHICH country's VAT applies — the foundation of VAT.** They differ for goods versus services and B2B versus B2C.

**Goods** (general):
- **Place of supply is generally where the goods are located, transported from, or transported to**
- **Domestic, intra-region (e.g. intra-EU), and import/export each have distinct treatment**

**Services** (general principles; country rules vary):
- **B2B: often where the customer is established** — reverse charge applies, see Step 4
- **B2C: often where the supplier is established**, with major exceptions — **digital services to consumers are taxed where the consumer is**
- **Special rules for land-related services, events, transport, restaurant, hire of means of transport**

> **Determine the place of supply for each transaction type. This drives which VAT registration and rate applies.**

**What the workspace contributes** `[auto]`, and it is inputs rather than answers:

- **Customer and supplier country**, where recorded
- **Whether the supply was goods or services**, where the chart or item structure distinguishes them
- **Whether the customer is B2B or B2C** — **inferable only where a customer VAT number is recorded**, which is itself the Step 4 validation point

**Three of those are partial and one is a genuine gap.** Land-related services, events and the other special rules turn on facts about **what the service was and where it was performed** — and a ledger records that a consultancy fee was charged, not that the consultancy concerned a building in Lisbon. **`[manual]`, and it is where place-of-supply errors concentrate.**

---

### Step 3 — Output VAT (VAT on sales)

`[auto]` for the amounts; **`[manual]` for the treatment.**

For supplies where the entity must charge VAT:
- **Apply the correct rate: standard, reduced, or zero-rated** — **use current rates; do not hardcode**
- **Exports of goods outside the VAT region are typically zero-rated**, with **proof of export**

> **Compute output VAT by rate category.**

`[auto]` where tax codes are exposed per line.

#### Zero-rated versus exempt

> **The zero-rated versus exempt distinction is critical:**
>
> - **Zero-rated**: taxable at 0% — **the supplier still recovers input VAT on related costs**
> - **Exempt**: outside the scope of output VAT — **but the supplier generally CANNOT recover related input VAT**
> - **This difference materially affects net VAT and is a common error**

**Preserved with full emphasis. It is the single most consequential distinction in VAT**, and edge case 1 calls it exactly that.

**The determination is `[manual]`.** Whether a supply is zero-rated or exempt is a matter of law, it varies by country, and the same supply can be treated differently in two jurisdictions.

**But the *consequence* is `[auto]`, and that is the detection** — see Step 5b. An entity making exempt supplies and recovering input VAT in full has either misclassified the supplies or failed to apply a restriction, **and both are visible without knowing which supplies are which.**

**`[auto]` for one more thing worth flagging**: **proof of export.** Zero-rating an export generally requires evidence, and **the ledger shows the zero-rated sale without showing whether the evidence exists.** Where zero-rated export sales are material, flag that the supporting documentation is a `[manual]` check — a zero-rating disallowed for want of proof becomes VAT payable by the supplier, out of margin.

---

### Step 4 — Reverse charge

`[auto]` to detect; **`[manual]` to determine.** All aspects preserved.

> **Under the reverse charge, the CUSTOMER — not the supplier — accounts for the VAT.**

- **Common for B2B cross-border services**: the supplier does not charge VAT; the customer self-accounts in their country
- **The customer records both output VAT and (usually) a matching input VAT** — often net-nil if fully recoverable, **but both sides must be reported**
- **Also applies to certain domestic supplies** — anti-fraud measures in construction, electronics, and so on, country-specific
- **For intra-EU B2B goods**: the acquisition is taxed in the destination country by the customer

> **Identify reverse-charge transactions on both the sales side** — do not charge VAT; note the customer self-accounts — **and the purchase side** — self-account for VAT on services received from abroad.

> **Validate customer VAT numbers for B2B cross-border zero-rating and reverse charge (e.g. VIES validation in the EU). An invalid customer VAT number can invalidate the treatment.**

**Validation is `[manual]`** — VIES and its equivalents are external services not on this surface. **`[auto]` for the prior question**: **which cross-border B2B customers have a VAT number recorded at all.** A zero-rated cross-border supply to a customer with no recorded VAT number is unsupported on its face, and that is a population, not a sample.

---

### Step 4b — The reverse-charge net-nil detection *(Mosofin addition)*

**`[auto]`, one query, and it is the best detection target in the skill.**

Edge case 5 describes the trap precisely:

> **Reverse charge net-nil trap**: even when reverse charge nets to nil (full recovery), **both the output and input sides must be reported. Omitting them is a reporting error even with no cash effect.**

**Why it is so reliably missed**: because it nets to nil, **nothing looks wrong.** The P&L is right. The balance sheet is right. The net VAT payable is right. **The only thing that is wrong is the return** — two boxes that should carry a number and carry zero. Nobody reconciling the accounts will ever find it, because there is nothing to find in the accounts.

**Which is exactly what makes it findable by query rather than by review.**

**Read the purchase ledger for the signature:**

| Signature | Meaning |
|---|---|
| **Supplier in another country** | The precondition |
| **Services** (or intra-EU goods acquisitions) | The scope |
| **No VAT charged on the invoice** | Consistent with the supplier correctly not charging |
| **No reverse-charge output VAT entry in the books** | **The omission** |

**Where the first three are present and the fourth is absent, the reverse charge has not been accounted for.**

Quantify the population: how many transactions, what value, over what periods, from which suppliers.

**Two things to say when reporting it.** **The cash effect is usually nil** — where input VAT is fully recoverable, both legs cancel, and the client's instinct will be that nothing is wrong. **The reporting obligation is not nil**, and in many regimes penalties attach to under-declaration regardless of the net position.

**And where input VAT is *not* fully recoverable** — a partially exempt business, or a blocked cost — **the reverse charge is not net-nil at all.** The output leg is payable in full and only part of the input leg is recoverable, **so the omission has understated tax actually due.** `[auto]` to identify which case applies, since Step 5b already establishes whether recovery is restricted.

**This detection alone frequently justifies connecting the workspace.**

---

### Step 5 — Input VAT (VAT on purchases)

`[auto]` for the amounts; `[manual]` for recoverability.

> **Input VAT is the VAT the entity pays on its purchases, generally recoverable against output VAT.**

All four conditions preserved:

- **Recoverable only if the entity is registered and the purchases relate to taxable (including zero-rated) supplies** — `[manual]`
- **Not recoverable to the extent purchases relate to exempt supplies** — partial exemption — `[manual]` method, **`[auto]` detection**
- **Blocked input VAT**: some countries block recovery on specific costs — **entertainment, certain vehicles** — country-specific. `[auto]` for the population, `[manual]` for the rule
- **Requires valid VAT invoices** — **`[manual]`.** The ledger records that VAT was posted; **it does not establish that a compliant VAT invoice exists**, and recovery without one can be denied.

> **Compute recoverable input VAT, separating blocked and exempt-related (irrecoverable) portions.**

**The blocked-cost sweep is `[auto]` and shares its population with `tax-return-prep-corporate`'s disallowables sweep** — entertainment, hospitality, certain motor costs. **Input VAT recovered on entertainment is one of the most common VAT errors** and it is one read of the same accounts.

---

### Step 5b — The partial exemption consequence test *(Mosofin addition)*

**`[auto]`, and it detects a material error without needing to know which supplies are exempt.**

The logic is simple and it runs backwards from the consequence:

1. **Does the entity make exempt supplies?** `[auto]` where the tax codes distinguish exempt from zero-rated — **and where they do not, that itself is the finding**, because the two require different treatment and a chart that cannot tell them apart cannot support the restriction.
2. **Is input VAT being recovered in full?** `[auto]` — compare input VAT posted to input VAT recovered on the returns.
3. **If both are true, one of two things is wrong**: the supplies are not actually exempt (they may be zero-rated, which does preserve recovery), **or a partial exemption restriction has never been applied.**

**Both are material.** A business making exempt supplies and recovering all its input VAT is over-recovering, cumulatively, for as long as it has been doing so — and it is the kind of error that accrues quietly and is assessed with interest.

> **Partial exemption**: an entity making both taxable and exempt supplies **can only recover input VAT on the taxable portion.** Apply the country's partial-exemption method — standard turnover-based or a special method. **This is complex — flag for careful calculation.**

`[auto]` for the turnover-based apportionment arithmetic, which is mechanical once the split of supplies is determined; `[manual]` for the method and the determination.

---

### Step 6 — Special schemes

`[manual]` for eligibility; `[auto]` for one relevant fact each.

**EU One-Stop-Shop (OSS) / Import One-Stop-Shop (IOSS)**:
- **OSS**: report B2C supplies across EU member states in a single return, instead of registering in each
- **IOSS**: for imported low-value goods to EU consumers
- **Determine eligibility and whether the entity uses these**

`[auto]`: **B2C supplies by member state**, which is what an OSS return reports and what determines whether OSS is worth using rather than registering locally.

**Other regimes** — **cash accounting schemes, flat-rate schemes, margin schemes** (second-hand goods, travel) — **country and eligibility specific. Apply if relevant.**

`[auto]` for one check worth running: **is the scheme in use actually being operated?** A cash accounting scheme means VAT is accounted on payment rather than invoice — **and a book accounting on invoice while claiming cash accounting is misdeclaring in both directions.** The posting basis is visible.

---

### Step 7 — Return preparation

`[auto]` for the figures; **`[manual]` to file.**

For each country, registration and period — all six elements preserved:

| Element | Verdict |
|---|---|
| **Output VAT by rate** | `[auto]` where tax codes are exposed |
| **Input VAT (recoverable)** | `[auto]` for posted; **`[manual]` for the recoverable determination** |
| **Reverse-charge VAT (both output and input sides)** | **`[auto]` to compute; see Step 4b for whether it was accounted at all** |
| **Net VAT payable or refundable** | `[auto]` |
| **EC Sales Lists / recapitulative statements** for intra-EU B2B; **Intrastat** for goods movements above thresholds | `[auto]` for the data **where customer VAT numbers and commodity detail are recorded**; `[manual]` for the thresholds |
| **SAF-T, e-invoicing or real-time reporting** where applicable — **growing globally** | **`[manual]`** |

> **Filing frequency varies by country and size — monthly, quarterly, annual.**

`[manual]`, and it **changes**: a growing business gets moved to monthly filing, and missing the change is a straightforward late-filing penalty. Same point as `sales-tax-us-multistate`.

**The last row deserves emphasis.** **E-invoicing and real-time reporting mandates are spreading quickly**, and they are not a variation on a return — they are a different obligation with a different infrastructure, often requiring transactions to be cleared with the tax authority **before or as they are issued.** **A business that discovers one late has a systems problem, not a filing problem.** Flag the entity's obligations early; see edge case 9.

---

### Step 8 — Reconciliation

**`[auto]` for three of the four legs.** All four preserved.

| Reconciliation | Verdict |
|---|---|
| **Output VAT per the billing system to VAT payable in the GL** | **`[auto]`** |
| **Input VAT per purchase records to VAT recoverable in the GL** | **`[auto]`** |
| **VAT control account to the returns filed** | **`[manual]` for the returns side** — the returns are filed documents. See `balance-sheet-reconciliations`. |
| **VAT on the return to the VAT in the financial records** | Same |

> **Identify discrepancies, timing differences and errors. The VAT control account should reconcile to amounts due or refundable.**

**Note which legs are which.** The first two tie one part of the ledger to another and will generally agree — informative, and not external verification. **The legs that reach outside are the ones involving the filed returns**, and those need the returns.

#### The collected-not-remitted test

`[auto]`, and it carries the same weight as its US counterpart.

**Read the VAT control account's movement.** In a properly running business it fills and empties on the filing cycle.

**A control account balance that only grows is VAT collected from customers and not paid over.**

**In most VAT regimes this is more clearly trust money than US sales tax**: the business charged VAT as a collector on the state's behalf, has been reimbursed for its input VAT, and holds the net. Non-payment is treated seriously, penalties and interest accrue, and **in a number of jurisdictions directors can be made personally liable.**

**Report it factually** — the balance, the growth pattern, the periods — **and say plainly why it is treated differently from an ordinary payable. Never as an allegation.** The usual cause is a business under cash pressure intending to catch up, and raising it early is the whole value of raising it.

---

### Step 9 — Output

An `.xlsx` workpaper. All eight of the original's sheets, plus two additions.

**Sheet 1: Registration Analysis**
| Country | Established? | Turnover vs Threshold (current) | Registration Required? | Date | Registered? | Scheme (OSS/etc.) |

**Add an "Any local supplies?" column** — for nil-threshold countries the question is presence of supply, not level. **Threshold column carries its source and confirmation date.**

**Sheet 2: Place of Supply & Treatment**
| Transaction Type | Goods/Services | B2B/B2C | Place of Supply | VAT Treatment | Rate Category |

**`[manual]` determinations.** Mosofin populates the transaction types and the readable attributes and **leaves Place of Supply and VAT Treatment for the preparer.**

**Sheet 3: Output VAT**
By rate category, **with zero-rated and exempt clearly separated.** **If the chart cannot separate them, that is stated at the top of the sheet** — it is a prerequisite for Step 5b.

**Sheet 4: Reverse Charge**
Sales-side and purchase-side items. **With the Step 4b omission population**, and whether the net position is nil or not.

**Sheet 5: Input VAT**
Recoverable, blocked, and exempt-related (irrecoverable) portions. **With the blocked-cost sweep.**

**Sheet 6: Return Figures by Country**
Return-ready net VAT, plus EC Sales List and Intrastat data where relevant.

**Sheet 7: Reconciliation**
VAT control account versus returns versus GL. **With the collected-not-remitted test, and each leg marked internal or external.**

**Sheet 8: Open Items / Confirmations Needed**
**Rates, thresholds and treatment calls flagged for current-source confirmation.** Every `[manual]` item appears here.

**Sheet 9: Detections** *(Mosofin addition)*
| Detection | Country | Population | Value | Periods | Cash effect | Reporting effect | Action |
|---|---|---|---|---|---|---|---|

Reverse charge not accounted. Input VAT recovered in full against exempt supplies. Blocked costs recovered. Control account not clearing. Zero-rated cross-border supplies to customers with no VAT number recorded. Countries with supplies and no registration. Countries approaching a threshold.

**The Cash effect and Reporting effect columns are separate on purpose** — the reverse-charge finding frequently has nil cash effect and a real reporting one, and collapsing them into a single materiality column hides it.

**Sheet 10: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `VAT_GST_[Country]_[Period]_[EntityName].xlsx`

Entity `display_name` and **country** on every sheet — registrations are per entity per country. If any read returned `mock: true`, say so in the file name and on Sheet 7.

---

## Output Quality Standards

All eleven preserved.

- **Registration obligations assessed per country with current thresholds (not assumed).** `[auto]` for turnover; `[manual]` for thresholds — **and nil-threshold countries tested on presence of supply.**
- **Place of supply correctly determined per transaction type.** `[manual]`
- **Zero-rated versus exempt correctly distinguished.** `[manual]` to determine; **`[auto]` to detect the consequence of getting it wrong.**
- **Reverse charge identified on both sales and purchase sides, both legs reported.** **`[auto]` — including where neither leg was.**
- **Input VAT recovery adjusted for blocked and exempt-related portions.** `[auto]` for the populations; `[manual]` for the rules.
- **Special schemes applied where relevant.** `[manual]`, **with a check that a claimed scheme is actually being operated.**
- **Returns reconcile to GL and to the VAT control account.** `[auto]` for the internal legs; **`[manual]` for the returns.**
- **No hardcoded rates, thresholds or country rules — all current-sourced with sources noted.** `[manual]`, **and nothing persisted supplies one.**
- **Customer VAT numbers validated for cross-border B2B.** `[manual]` to validate; `[auto]` to find the missing ones.
- **File naming consistent.** `[auto]`
- **Uncertain treatments flagged for confirmation.** `[manual]`, Sheet 8.

**Five Mosofin additions:**

- **Cash effect and reporting effect are reported separately**, since the headline detection has nil cash effect.
- **The reverse-charge omission sweep runs every period.**
- **Input VAT recovery is tested against the existence of exempt supplies.**
- **The control account is tested for clearing**, and trust-money treatment explained where it is not.
- **Bad debt relief is swept for**, because it is unclaimed relief in the client's favour.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and every rate, threshold and country rule.**

**What is worth persisting into the workspace-scoped skill:**

1. **Registration status and dates per country.** The join that makes the analysis an exposure assessment.
2. **How the chart maps to countries and rate categories**, including whether exempt and zero-rated are distinguishable — a prerequisite for Step 5b.
3. **The zero-rated / exempt determinations** for this business's supplies, **with sources and dates, explicitly to be re-confirmed.**
4. **The partial exemption method and its recovery rate**, with the year it was agreed.
5. **Blocked cost categories** applicable in each country.
6. **Suppliers whose invoices attract reverse charge**, so the Step 4b sweep starts from a known list.
7. **Schemes in use** — OSS, IOSS, cash accounting, margin — and the basis they require.
8. **Filing frequencies and e-invoicing obligations per country**, with the date each was last confirmed.
9. **Findings and their resolutions**, so a reverse-charge population already corrected is not re-raised.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed.**

**Store the determinations and where they came from; re-confirm the rules.**

---

## Anti-patterns

- **Ignoring the reverse charge because it nets to nil.** The cash is right and the return is wrong.
- **Assuming reverse charge is always net-nil.** For a partially exempt business it is not.
- **Recovering input VAT in full while making exempt supplies.**
- **Treating exempt as zero-rated.** One preserves recovery; the other blocks it.
- **Reading treatment off tax codes.** They record a past configuration decision.
- **Applying a turnover threshold in a nil-threshold country.** The test is any local supply.
- **Recovering input VAT on entertainment** where it is blocked.
- **Zero-rating a cross-border B2B supply with no customer VAT number recorded.**
- **Zero-rating an export without proof of export.** Disallowed, it becomes VAT out of margin.
- **Treating a growing VAT control balance as an ordinary payable.** It is generally trust money.
- **Reconciling the ledger to itself** and calling it a return reconciliation.
- **Missing bad debt relief.** Unclaimed relief in the client's favour.
- **Discovering an e-invoicing mandate at period end.** It is a systems obligation.
- **Combining entities or countries in one return.** Registration is per entity per country.
- **Carrying a rate or threshold forward.** The source forbids it; so does this file.
- **Saying "filed" or "remitted".** The gateway reads.
