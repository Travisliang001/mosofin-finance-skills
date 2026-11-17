<!-- tax-return-prep-corporate · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Establish the starting point
- Step 1b — Test that the starting point is actually final *(Mosofin addition)*
- Step 2 — Add back disallowable / non-deductible items
- Step 2b — Sweep for the disallowables nobody remembered *(Mosofin addition)*
- Step 3 — Deduct items taxed differently or not taxable
- Step 4 — Tax depreciation / capital allowances
- Step 5 — Compute adjusted taxable income before reliefs
- Step 6 — Apply loss relief
- Step 7 — Compute the tax
- Step 8 — Apply tax credits and reliefs
- Step 9 — Compute payments, instalments and balance due
- Step 10 — Assemble supporting schedules
- Step 11 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a computation for review.** The gateway is read-only. **Mosofin files nothing and signs nothing.**

---

## Inputs

All ten preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Final financial statements / TB** | For the tax year | **Required** | **Live read — and test that it is final.** See Step 1b. | `[auto]` |
| **Jurisdiction(s) and tax year** | Country/state, year-end | **Required** | Fiscal year end readable; jurisdiction is not | `[manual]` |
| **Current tax rate(s) and rules** | User-supplied or current-sourced | **Required** | **Never from this file.** | `[manual]` |
| **Fixed asset additions/disposals** | For tax depreciation | **Required** | **Live read** — additions and disposals in the period | `[auto]` |
| **Book depreciation/amortisation** | To add back | **Required** | **Live read, exact** — the largest single add-back | `[auto]` |
| **Schedule of disallowable / non-deductible items** | Per jurisdiction | **Required** | **The population is readable; the disallowance is not.** See Step 2b. | Split |
| Loss carryforwards/carrybacks | With years and limitations | Recommended | **Tax attributes, not ledger balances** | `[manual]` |
| Tax credits available | R&D, investment, foreign tax | Recommended | Candidate spend readable; entitlement not | `[auto]` in part |
| Prior year return | Continuity, attributes, elections | Recommended | **A document** | `[manual]` |
| Group / related party info | Group relief, transfer pricing | If applicable | **`[auto]` where entities are connected**; relationships and relief rules are not | Split |

---

## Workflow

### Step 1 — Establish the starting point

**`[auto]`, and it is the one figure everything else adjusts.**

> **Begin with pre-tax accounting profit or loss from the final financial statements for the tax year.** The computation converts this book figure into taxable income via adjustments.
>
> **Confirm the tax year, jurisdiction(s), filing entity, and the current rules and rates that apply — do not assume; confirm for the year.**

`[auto]` for the profit figure, exact, with every account behind it traceable. `[manual]` for everything in the second paragraph.

---

### Step 1b — Test that the starting point is actually final *(Mosofin addition)*

`[auto]`, one query, and it matters more here than in the skills that run the same test.

The input says **"final"** financial statements. A computation built on a trial balance that subsequently moves produces a return that does not tie to the accounts — and **for a filed return, a moved starting point is an amended return**, not a re-run.

Check:

- **Is the year closed**, with all close entries posted? See `year-end-close` and `month-end-close-checklist`.
- **Has anything been posted into the year since it was closed?** The same test `quarter-end-close`, `restatement-and-prior-period-adjustment` and `sec-10q-10k-prep` all run.
- **Do the accounts used match the statements as signed?** Where the statutory accounts are a separate document, **the return generally starts from the figure in those accounts**, not from whatever the ledger says today.

**If the year is still moving, say so before computing.** The computation is cheap to re-run; the return is not.

**And re-run this check immediately before filing**, exactly as `subsequent-events-asc855` re-runs its sweep before issuance. The gap between preparing a computation and filing it is frequently weeks, and it is a window in which the audit adjustments arrive.

---

### Step 2 — Add back disallowable / non-deductible items

**`[auto]` for the population; `[manual]` for the disallowance.** All seven categories preserved.

> **Items expensed in the books but not deductible for tax — jurisdiction-specific; confirm each.**

| Category | Mosofin | Verdict |
|---|---|---|
| **Book depreciation and amortisation** — replaced by tax depreciation, Step 4 | **`[auto]`, exact.** The largest add-back in most computations and a direct read. | `[auto]` |
| **Certain fines and penalties** | `[auto]` where coded to a recognisable account; **also findable in the detail of general expense accounts** | `[auto]` to find, `[manual]` to judge |
| **Non-business entertainment** (jurisdiction-specific) | `[auto]` where coded | Split |
| **Certain provisions and accruals not yet allowable** | **`[auto]`** — provision account movements are directly readable, and *movement* is what matters, since it is generally the increase that is disallowed | Split |
| **Disallowed interest** — thin-capitalisation or interest limitation rules | **`[auto]` for interest expense and for the limitation base** — commonly a percentage of EBITDA, which is computable | `[auto]` for inputs, `[manual]` for the rule |
| **Impairments not yet allowable** | `[auto]` — impairment charges are identifiable | Split |
| **Other jurisdiction-specific add-backs** | `[manual]` — by definition | `[manual]` |

**The interest limitation deserves a note**, because both of its inputs are readable: the interest expense and, where the cap is EBITDA-based, the EBITDA. `[auto]` computes the cap and the excess **once the percentage is supplied** — and **disallowed interest frequently carries forward**, which makes it a tax attribute to track (see edge case 2 and Step 6's discipline).

---

### Step 2b — Sweep for the disallowables nobody remembered *(Mosofin addition)*

**`[auto]`, and it addresses the real risk in Step 2, which is completeness rather than arithmetic.**

**An add-back missed is tax underpaid**, with interest and potentially penalties, discovered on enquiry rather than by anybody internally. And the way add-backs get missed is not that somebody computes one wrongly — **it is that a category never comes up**, because the schedule was copied from last year and the business has changed.

So: **read the full expense ledger for the year** and surface accounts and transactions whose description or coding suggests a commonly disallowed category:

- **fines, penalties, late-payment charges, parking, regulatory penalties**
- **entertaining, hospitality, client events, gifts**
- **donations** — often relieved separately rather than deducted as an expense
- **legal and professional fees**, which frequently mix deductible and capital or disallowable elements
- **provisions and their movements**
- **impairments and write-offs**
- **payments to related parties** — see `related-party-disclosures-asc850` and transfer pricing
- **items capitalised that may be deductible, and expensed items that may be capital** — the distinction in edge case 4

**Present the population with amounts, ranked, as candidates for the preparer's judgment.** It is a completeness aid, not a determination — the same shape as the cost sweep in `r-and-d-tax-credit`, and with the same justification: **the ledger is complete about transactions and a memory is not.**

**And note it runs in both directions.** The same sweep surfaces items that were added back and perhaps need not have been — an over-cautious schedule carried forward for years is also a cost, and nobody ever audits a return for the deduction it failed to take.

---

### Step 3 — Deduct items taxed differently or not taxable

`[manual]` for the treatment; `[auto]` for several populations. All five preserved.

| Item | Mosofin | Verdict |
|---|---|---|
| **Income recognised for book but not taxable**, or taxed elsewhere | `[auto]` to identify candidate income accounts | Split |
| **Dividends with participation exemption / dividends-received deduction** (jurisdiction-specific) | **`[auto]`** — dividend income received is directly readable | Split |
| **Deductions allowable for tax beyond the book expense** — enhanced deductions, e.g. certain R&D super-deductions | `[auto]` for the underlying spend; `[manual]` for the enhancement. See `r-and-d-tax-credit` | Split |
| **Reversals of prior-year add-backs now allowable** | **`[manual]`** — depends on the **prior year's computation**, which is a document | `[manual]` |
| **Gains and income deferred for tax** | `[auto]` for the gain; `[manual]` for the deferral | Split |

**The fourth row is worth flagging as a routine failure point.** Reversals of prior-year add-backs — a provision disallowed last year and paid this year, for instance — are **deductions the entity is entitled to and frequently forgets**, because they require reading last year's computation rather than this year's ledger. **Nothing in the current year's accounts prompts them.** This is exactly what the seed-to-evolved section exists to fix: persist the add-backs, and next year's reversals surface automatically.

---

### Step 4 — Tax depreciation / capital allowances

**`[manual]` for the schedule; `[auto]` for its inputs and for the add-back it replaces.**

> **Book depreciation is added back; tax depreciation (capital allowances) is deducted instead, using the jurisdiction's tax rules.**

All four elements preserved:

- **Asset pools/classes and their rates** — jurisdiction-specific. `[manual]`
- **First-year, bonus or accelerated allowances, or expensing**, if available — **confirm current rules.** `[manual]`
- **Balancing charges and allowances on disposals.** `[manual]` for the rules; **`[auto]` for the disposals themselves**, with proceeds and book values
- **Special rules for specific asset types** — vehicles, buildings, intangibles. `[manual]`

> **Build a tax depreciation schedule separate from the book fixed-asset register** (`fixed-asset-register-and-depreciation`). **The two diverge and create the depreciation temporary difference seen in the provision.**

**Preserved and important.** They are two different registers with two different lives and two different methods, maintained in parallel for the life of every asset.

**What the workspace supplies** `[auto]`: **additions and disposals in the period**, with dates, amounts, descriptions and counterparties — which is precisely the input the pool movements need. **The book depreciation charge**, exactly, for the add-back. **And the book carrying values on disposal**, which the balancing computation needs alongside proceeds.

**What it does not**: the pools, the rates, the elections, the prior pool balances. **The tax written-down values are tax attributes and live in the prior year's computation**, not in the accounts — the second near-substitute again.

---

### Step 5 — Compute adjusted taxable income before reliefs

**`[auto]` arithmetic**, once the adjustments exist.

```
Pre-tax accounting profit
+ Disallowable items / book depreciation add-back
- Items not taxable / additional tax deductions
- Tax depreciation / capital allowances
= Adjusted profit / (loss) for the period (before loss relief)
```

> **Separate income by category or schedule if the jurisdiction taxes different income types differently** — trading income, investment income, capital gains, rental, and so on.

`[auto]` for the separation **where the chart distinguishes those income types**, which it usually does at least partially; `[manual]` for the mapping to the jurisdiction's schedules. **This separation matters for Step 6**, because losses generally offset only the same type.

---

### Step 6 — Apply loss relief

**`[manual]`, and the reason is the second near-substitute: losses are tax attributes, not ledger balances.**

All four elements preserved:

- **Current-year loss**: carryback where permitted, or carryforward
- **Brought-forward losses**: offset against current taxable income **subject to restrictions** — some jurisdictions cap the percentage of profits that losses may offset
- **Track loss type** — trading versus capital and so on — because **losses can often only offset the same type**
- **Group relief / loss surrender** between group companies, where applicable and permitted

> **Maintain a loss memorandum: opening losses, used, arising, expiring, closing — by type and year.**

**The memorandum is the artefact and it lives outside the accounts.** `[auto]` supplies exactly one line of it — the **current-year loss arising**, from Step 5. Everything else — opening balances by type and year, prior utilisation, expiry dates, restriction history — comes from the prior year's memorandum.

**Three points worth making explicit:**

**Losses expire.** A memorandum tracking year of origin is not bookkeeping tidiness; in jurisdictions with expiry, **a loss not used in time is lost permanently**, and the memorandum is the only thing that shows it approaching.

**Ownership changes can forfeit losses** — edge case 3. This is a fact about share ownership, and **there is no cap table on this surface** (consistent with `equity-compensation-accounting`, `statement-of-equity-changes` and others). It must be asked.

**The deferred tax asset is not the loss.** A DTA is the loss measured at a rate and reduced for recoverability. **Reading it backwards to derive the attribute gives the wrong number.** See `income-tax-deferred-tax-rollforward`.

---

### Step 7 — Compute the tax

`[auto]` arithmetic; **`[manual]` for every parameter.**

```
Taxable income (after loss relief)
x Applicable tax rate(s)        <- confirm current rate(s); some jurisdictions have bands / marginal relief
= Tax before credits
```

> **Apply any special rate rules — small-company rates, bands, surcharges — for the jurisdiction and year. Confirm current parameters.**

**Bands and marginal relief make this less trivial than it looks**, and it is the same cliff structure `tax-planning-and-projections` maps: **a band boundary can create an effective marginal rate well above the headline rate.** `[auto]` computes it correctly given the parameters, and **showing where the entity sits relative to a band boundary is worth doing** — it is a planning fact discovered during compliance work, and it is free.

---

### Step 8 — Apply tax credits and reliefs

`[auto]` for candidate identification and arithmetic; **`[manual]` for entitlement.** All four preserved.

| Credit | Mosofin | Verdict |
|---|---|---|
| **R&D tax credits** | **`[auto]` to identify candidate spend** — see `r-and-d-tax-credit`, which does this properly | Split |
| **Foreign tax credits** — for tax paid abroad on foreign income, **subject to limitations** | `[auto]` for foreign tax suffered where recorded; **`[manual]` for the limitation**, which is intricate | Split |
| **Investment and other statutory credits** | `[auto]` for candidate spend; `[manual]` for entitlement | Split |
| **Withholding tax credits** | **`[auto]`** where withholding suffered is recorded — and **it frequently is not**, being netted into income; ask | Split |

```
Tax before credits
- Tax credits
= Net tax payable
```

**Withholding is the one most often lost.** Where a customer or a foreign payer withholds tax and the entity records only the net receipt, **the withholding is invisible in the ledger and the credit goes unclaimed.** `[auto]` can flag the possibility — foreign customers, receipts that do not match invoices — but the certificates are outside. **Ask directly.**

---

### Step 9 — Compute payments, instalments and balance due

**`[auto]` for three of the four.** All four preserved.

| Element | Verdict |
|---|---|
| **Estimated / instalment payments already made during the year** | **`[auto]`** — a live read, and see below |
| **Payment-on-account requirements** | `[manual]` — jurisdictional |
| **Balance due or refund** | `[auto]` arithmetic |
| **Payment deadlines and instalment schedule** — **confirm** | `[manual]` |

**The payments-made read is the same check as in `tax-planning-and-projections`**, and it is worth running here too, at a point when it can still be acted on: **a scheduled instalment with no corresponding payment in the ledger is a missed instalment on which interest is already running.**

---

### Step 10 — Assemble supporting schedules

> **A return needs workpapers behind every figure.**

All eight preserved:

| Schedule | Verdict |
|---|---|
| **Book-to-tax reconciliation** | `[auto]` for the book side of every line; `[manual]` for the rationale |
| **Capital allowances / tax depreciation schedule** | `[manual]`, with `[auto]` movements |
| **Loss memorandum** | `[manual]`, with `[auto]` current-year arising |
| **Disallowable items detail** | **`[auto]` for the detail behind each add-back** — every transaction, traceable |
| **Credits computations** | Split |
| **Related party / transfer pricing summary**, if applicable | `[auto]` where entities are connected; `[manual]` for the analysis. See the transfer pricing documentation |
| **Reconciliation of the computation to the financial statements** | **`[auto]`** — both ends readable |
| **Return-to-provision reconciliation** — tie back to `corporate-tax-provision-asc740` | **`[auto]` for the provision side**; `[manual]` for the analysis |

**Two of these deserve emphasis.**

**The disallowable items detail is where the connection pays off in review.** Every add-back can be supported by the actual transactions behind it — dates, counterparties, amounts, descriptions — rather than a total carried from a schedule. **That is exactly what an enquiry asks for**, and assembling it after the fact, years later, is the expensive version.

**The return-to-provision reconciliation is the loop back to the provision skill**, and the third near-substitute governs it: **the difference is expected.** `[auto]` computes both sides and the difference; the analysis of *why* — a rate change, an adjustment identified during the computation, a claim not anticipated — is `[manual]`, and **the true-up feeds back to `corporate-tax-provision-asc740`.**

---

### Step 11 — Output

An `.xlsx` tax computation workpaper. All eight of the original's sheets, plus two additions.

**Sheet 1: Tax Computation Summary**
Pre-tax profit → taxable income → tax → credits → net payable. **Header carries the basis, the finality status of the starting point, every parameter's source and confirmation date, and the fixture flag.**

**Sheet 2: Book-to-Tax Reconciliation**
**Every adjustment itemised with rationale and jurisdiction basis.** `[auto]` for the amounts; `[manual]` for the rationale. **Add a Source column** — ledger-read or user-supplied.

**Sheet 3: Capital Allowances / Tax Depreciation**
By pool and asset: additions, disposals, allowances, balancing items. **`[manual]` schedule with `[auto]` movements**, and **prior pool balances marked as coming from the prior return.**

**Sheet 4: Loss Memorandum**
By type and year, opening to closing. **`[manual]`, with the current-year arising figure supplied.** **Expiry dates shown**, with anything expiring within two years highlighted.

**Sheet 5: Credits**
R&D, foreign tax and other computations.

**Sheet 6: Payments & Balance Due**
Instalments, balance, deadlines. **With the payments-made check**, and any missed instalment at the top.

**Sheet 7: Reconciliations**
Computation to financial statements; **return-to-provision tie-back, with the difference presented as an expected true-up rather than a variance.**

**Sheet 8: Open Items / Confirmations**
**Rates, allowance rules and jurisdiction-specific calls flagged for current-source confirmation and local-preparer review.** Every `[manual]` item appears here.

**Sheet 9: Disallowable Candidates Sweep** *(Mosofin addition)*
The Step 2b population:

| Account | Transactions | Amount | Suggested category | In computation? | Preparer's determination |
|---|---|---|---|---|---|

**Both directions** — candidates not yet added back, and add-backs that may not be required.

**Sheet 10: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Tax_Computation_[YYYY]_[EntityName].xlsx`

Entity `display_name` on every sheet. **Every sheet carries the local-preparer-review statement.** If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All ten preserved.

- **Computation flows clearly from book profit to taxable income to tax payable.** `[auto]` arithmetic.
- **Every book-to-tax adjustment itemised with rationale.** `[auto]` for amounts and **the transactions behind them**; `[manual]` for rationale.
- **Tax depreciation / capital allowances on a separate, reconciled schedule.** `[manual]` schedule, `[auto]` movements.
- **Loss memorandum complete by type and year, with restrictions applied.** `[manual]` — **tax attributes, with expiry visible.**
- **Credits computed and applied.** Split.
- **Payments, instalments and balance due with deadlines.** `[auto]` for payments made — **including any that were not.**
- **Reconciliation to financial statements and return-to-provision tie-back.** `[auto]`, **with the difference framed as an expected true-up.**
- **No hardcoded rates, allowances or rules — all confirmed for jurisdiction and year.** `[manual]`, and **nothing persisted supplies one.**
- **Complex and cross-border positions flagged for specialist and local-preparer review.** `[manual]`.
- **File naming consistent.** `[auto]`

**Five Mosofin additions:**

- **The starting point is tested for finality**, before computing and again before filing.
- **The disallowable population is swept**, in both directions, because completeness is the risk.
- **Every add-back carries its underlying transactions**, which is what an enquiry asks for.
- **Tax attributes are never inferred from accounting balances.**
- **Prior-year add-backs are carried forward** so their reversals are not forgotten.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and every rate, allowance and restriction.**

**What is worth persisting into the workspace-scoped skill** — and this skill benefits more than most, because **a tax computation is largely a continuation of the previous one:**

1. **The disallowable schedule as determined for this entity** — which accounts, which categories, what proportion. **The determinations, re-confirmed annually, not the rates.**
2. **The prior year's add-backs**, so **Step 3's reversals surface automatically** instead of being forgotten. This is the single most valuable item, because nothing in the current year's ledger prompts them.
3. **The capital allowance pools and their written-down values**, carried from the prior computation — **the attribute that is not in the accounts.**
4. **The loss memorandum**, by type and year, with expiry dates.
5. **Elections made and elections available, with their deadlines.** **The highest-consequence thing to persist**, since a missed election is unrecoverable and invisible.
6. **The account-to-computation mapping**, so the book side assembles itself.
7. **Whether withholding is recorded gross or net**, and where the certificates live.
8. **The return-to-provision history**, so a recurring true-up pattern is visible.
9. **Which local preparer reviews, and what they need.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — a tax computation is among the most confidential documents a company has.

**Store the determinations and the attributes; re-confirm the rules.** The attributes carry forward by design; the rules do not.

---

## Anti-patterns

- **Computing on a trial balance that is still moving.** A moved starting point after filing is an amended return.
- **Copying last year's disallowable schedule** without sweeping for what has changed.
- **Reading a deferred tax asset backwards to get the loss carryforward.** Different measurement, different number.
- **Treating the return-to-provision difference as an error.** It is an expected true-up.
- **Forgetting reversals of prior-year add-backs.** Nothing in this year's ledger prompts them.
- **Deriving tax written-down values from the book register.** Two registers, two lives, two methods.
- **Missing withholding recorded net.** The credit goes unclaimed and the ledger never mentions it.
- **Losing a loss to expiry** because the memorandum tracks totals rather than years.
- **Missing an election deadline.** Unrecoverable and invisible.
- **Presenting an add-back as a total** rather than with the transactions behind it. An enquiry asks for the transactions.
- **Sweeping only for missed add-backs.** Over-cautious add-backs cost money too.
- **Assuming losses survive an ownership change.**
- **Attempting a cross-border or Pillar Two position without a specialist.**
- **Carrying a rate forward.** The original forbids it; so does this file.
- **Saying "filed".** Mosofin computes; a qualified preparer reviews and files.
