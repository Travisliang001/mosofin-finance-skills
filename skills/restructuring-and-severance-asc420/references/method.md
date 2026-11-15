<!-- restructuring-and-severance-asc420 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Identify cost types and recognition rules
- Step 2 — Build the accrual model
- Step 3 — Roll forward the reserve
- Step 3b — Challenge the reserve *(Mosofin addition)*
- Step 4 — Journal entries
- Step 5 — Disclosures and controls
- Outputs
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. Mosofin posts nothing and recognises nothing.

---

## Inputs

All six preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Restructuring plan** | Approved plan date, scope, departments | **Required** | **Not in the books.** A board paper. | `[manual]` |
| **Employee list impacted** | Names/IDs, terms, notice dates, amounts | **Required** | **Not in the books.** HR data. **And see the confidentiality note** — prefer cost type and headcount over names. | `[manual]` |
| **Contracts to terminate** | Lease and vendor contracts, penalties | Required if applicable | The *payments* under them are readable; **the termination penalties are in the contracts** | `[auto]` in part |
| **Communications evidence** | Board approval, announcements | Recommended | **Not in the books — and it is the recognition trigger.** | `[manual]` |
| **Payments schedule** | Expected payment dates | Recommended | **Expected** dates are not in the books; **actual** payments are | `[manual]`, `[auto]` after the fact |
| **Prior reserves** | Rollforward, if ongoing | Recommended | **Live read, in full** — every line of Step 3 | `[auto]` |

---

## Workflow

### Step 1 — Identify cost types and recognition rules

`[manual]` for the rules. All three categories and all three hinges preserved.

**Typical categories:**

| Category | Note | Verdict |
|---|---|---|
| **One-time termination benefits (severance)** | The main event in most restructurings. Recognition depends on the future-service question — Step 2. | `[manual]` |
| **Contract termination costs** | Penalties and settlements for ending contracts early. | `[manual]` for the terms, `[auto]` for the payments once made |
| **Costs to exit a facility** (certain direct costs) | **Narrower than people expect** — and see the lease note below. | `[manual]` |

**Recognition hinges on:**

- **Commitment to the plan and communication.** `[manual]`, and evidenced. See the near-substitute note: a board approval alone is not communication.
- **Whether employees must provide future service.** `[manual]`, and it is the crux — Step 2.
- **Whether a contract is terminated or ceases to be used.** `[manual]`, and see immediately below.

#### A flag on facility exit costs and leases

The original says a contract termination cost is recognised when the contract is terminated **or no longer used**, "depending on guidance." That parenthesis is carrying real weight and it is worth unpacking, because it is the most likely place for this skill to apply a superseded model.

The old **cease-to-be-used** approach — setting up an exit liability for an operating lease on the date you stop occupying the space — **was substantially changed by the current lease standards.** Under ASC 842 and IFRS 16 an operating lease sits on the balance sheet as a right-of-use asset and a lease liability already, so vacating the premises is generally an **impairment assessment of the ROU asset**, and an early exit is generally a **lease modification or termination**, rather than a separate exit provision.

**Confirm which model applies before building a cease-use liability**, and route the lease element to `lease-accounting-asc842-ifrs16`. Setting up a 420-style exit reserve on top of an ROU asset that is still on the balance sheet **double-counts the same economic obligation** — and it is exactly the sort of thing that survives because both entries look individually reasonable.

`[auto]` for the supporting read: **is there an ROU asset for this facility on the balance sheet?** If there is, the exit is a lease question first. One read of the chart.

---

### Step 2 — Build the accrual model

**`[manual]` in substance.** This is the step that has to be built from HR and legal inputs, and no amount of ledger access changes that.

**For each impacted employee (or group):**

- **Determine the severance amount per agreement** — contractual, statutory, and any enhancement. `[manual]`
- **Determine the recognition timing:**
  - **If no future service is required**: accrue **when communicated and probable.** `[manual]`
  - **If future service is required**: accrue **over the service period.** `[manual]`

**For contract termination**: recognise **when the contract is terminated or ceases to be used** (per the applicable guidance — see the flag above) **and the obligation is probable and estimable.** `[manual]`

#### Why the future-service question is the crux

The two treatments produce very different results from the same facts, and the difference lands in the period where it is most visible.

- **No future service** — the employee leaves at announcement, or is told to go and paid in lieu. The whole cost hits **immediately**, in the period of communication.
- **Future service required** — the employee must work a transition period to earn the benefit. The cost **spreads across that period**.

Get this wrong in the first direction and you have understated the current period and created a reserve that will not unwind as expected. Get it wrong in the second and you have taken a charge early, which conveniently makes the following periods look better.

**It turns on the terms of the arrangement, and the terms are not in the ledger.** Ask, and document the answer per group rather than per plan — a single restructuring commonly has both kinds in it.

#### The `[auto]` check, which runs later and is worth setting up now

`[auto]`, once payments begin: **does the payment pattern match the recognition basis?**

If severance was accrued in full at communication — the no-future-service treatment — **but the employees remained on payroll for six months afterwards**, then future service looks very much as though it was required, and the recognition was probably wrong. The ledger holds both facts: the date the accrual was raised, and the months in which those people were still being paid ordinary wages.

**This is a genuine test of a judgment**, made from data, and it is one query. It does not settle the question — a garden-leave arrangement can look identical — but it is exactly the sort of challenge an auditor will raise, and it is better raised internally first.

---

### Step 3 — Roll forward the reserve

**`[auto]`, in full.** Every line is a live read.

```
Beginning liability
+ Additions (new accruals)
- Cash payments
+/- Adjustments (revisions)
= Ending liability
```

| Line | Source | Verdict |
|---|---|---|
| Beginning liability | Account balance at the prior period end | `[auto]` |
| Additions | Credits to the liability, with their expense counterpart | `[auto]` |
| Cash payments | Debits with a cash counterpart | `[auto]` |
| Adjustments / revisions | Debits or credits with an expense counterpart — **releases** | `[auto]` |
| Ending liability | Account balance at the period end | `[auto]` |

Each line ties to identifiable transactions rather than to a summary movement, so an unexplained line is immediately traceable to the entries that caused it.

---

### Step 3b — Challenge the reserve *(Mosofin addition)*

**The highest-value automatic work in this skill.** Four tests, all `[auto]`, all one query, and each of them finds something that occurs regularly in real books.

**Test A — Is the reserve stale?**

Read the liability's movement by period. **A restructuring reserve with no payments and no releases for several consecutive periods is a problem in one of two directions:**

- there is still an unsettled obligation that nobody is settling, or
- **the obligation has gone and the release was never made.**

Under both ASC 420 and IAS 37, **a provision that is no longer required must be released.** A reserve that simply sits there is not a neutral act — it is a liability the entity does not have, and it is the classic shape of the concern regulators describe as reserve smoothing: a balance available to absorb a future bad quarter.

**Report the age, the amount, and the periods of inactivity. As an observation, with figures. Never as an allegation about intent.** The commonest cause by far is that the restructuring finished and nobody went back to the account.

**Test B — Where were releases credited?**

When a reserve is released, the credit should go back to **the same line the charge came from** — the restructuring line — so that the reversal is as visible as the original.

`[auto]`: read the counterpart account on every release. **A restructuring reserve released against ordinary operating expenses** makes an unrelated cost line look better and makes the reversal invisible. That may be a coding error and it may not; either way it is a finding, and it is one read of an account code.

**Test C — Is severance being paid twice?**

**The double-count, and it is common.** Severance is accrued, creating a liability. Then the payments are processed through the normal payroll run and land in **wages expense** instead of being debited against the liability.

Result: the cost is recognised twice — once in the accrual and once in payroll — and the reserve stays fully intact, which will then also trip Test A.

`[auto]`: read the payroll and wages accounts for the periods after the accrual for termination-related payments, and read the liability for corresponding debits. **If the wages line moved and the liability did not, the accrual is not being used.** See `payroll-journal-entry-builder` and `payroll-reconciliation`.

**Test D — Are additions still arriving after the plan should have finished?**

Step 5 discloses an **expected completion date**. `[auto]`: read for additions to the reserve after it.

Two possible explanations and both need saying: the plan has extended in scope — in which case it is arguably a **new plan needing its own commitment, communication and recognition analysis** — or unrelated costs are being swept into a convenient existing reserve. The second is a presentation problem, because a cost in the restructuring line is a cost most readers will treat as non-recurring.

---

### Step 4 — Journal entries

`[auto]` to draft and to verify. **`[manual]` to post.** Both preserved.

**Accrue severance:**
```
DR  Restructuring Expense              XXX
    CR  Restructuring Liability            XXX
```

**Pay severance:**
```
DR  Restructuring Liability            XXX
    CR  Cash                               XXX
```

**Note what the second entry says, because Test C is the case where it is not what actually happens.** The payment debits the **liability**, not an expense. If a payment run debits wages instead, the cost has been recognised a second time.

Two entries the original does not draft, and both are needed in practice — added here:

**Release an unneeded provision** (the entry Test A finds missing):
```
DR  Restructuring Liability            XXX
    CR  Restructuring Expense              XXX
Memo: Release of provision no longer required — [plan] — [period]
```
**Credited back to the restructuring line**, per Test B, so the reversal appears where the charge did.

**Accrue where future service is required** — recognised across the service period rather than in one entry, per Step 2. Hand off to `recurring-transaction-builder` for the schedule and `journal-entry-builder` for the format.

---

### Step 5 — Disclosures and controls

**Disclose** — all three preserved:

| Disclosure | Verdict |
|---|---|
| **Nature of the restructuring** | `[manual]` |
| **Expected completion date** | `[manual]` — **and Test D checks the reserve against it** |
| **Rollforward of the liability** | **`[auto]`** — Step 3, complete and traceable |

Feed into `notes-to-financial-statements`.

**Controls** — all three preserved:

| Control | Verdict | Note |
|---|---|---|
| **Approved plan evidence** | `[manual]` | A document. |
| **HR/legal support for amounts** | `[manual]` | Individual entitlements come from agreements and statute. |
| **Review of changes in estimates** | `[manual]` to conclude, **`[auto]` to trigger** | Test A and Test D are exactly this review, run from data. **A revision is a change in estimate — prospective, not a restatement.** See `restatement-and-prior-period-adjustment` for the distinction, which matters and is often got wrong. |

---

## Outputs

All four of the original's outputs preserved, plus two Mosofin additions. Delivered as an `.xlsx` workpaper.

**Sheet 1: Accrual Model by Employee / Cost Type**
`[manual]`. **Present by cost type and headcount group wherever the accounting permits**, rather than by name — see the confidentiality note. Where names are genuinely required, say why on the sheet.

Columns: cost type, group, headcount, amount, recognition basis (immediate / over service period), service period if any, communication date, evidence reference.

**Sheet 2: Reserve Rollforward**
`[auto]`, all five lines, each traceable to its transactions. By plan where there is more than one — **two restructurings in one account is a rollforward nobody can use.**

**Sheet 3: JE Package**
The accrual, payment, and release entries. Marked **PROPOSED — NOT POSTED.**

**Sheet 4: Disclosure-Ready Summary**
Nature, expected completion, rollforward. Marked **DRAFT.**

**Sheet 5: Reserve Challenge** *(Mosofin addition)*
The four tests from Step 3b:

| Test | Plan | Finding | Amount | Periods | Recommended action |
|---|---|---|---|---|---|

Staleness, release destination, severance double-count, post-completion additions.

**Sheet 6: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Restructuring_[YYYY]_[EntityName].xlsx`

Entity `display_name` in the file name and on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 2.

---

## Output Quality Standards

*(A Mosofin addition — the original has no Output Quality Standards section.)*

- **The recognition trigger is evidenced, not asserted** — commitment *and* communication, with the document referenced and dated.
- **The future-service question is answered per group, not per plan**, and documented.
- **The severance model reconciles to the accrual entry**, and both are traceable.
- **The rollforward ties**, with every line traceable to its transactions, **and separately per plan** where more than one exists.
- **The lease element is routed to the lease standard** before any cease-use liability is set up.
- **The reserve is challenged every period** — staleness, release destination, double-count, post-completion additions — and the results are reported whether or not they are comfortable.
- **Releases are credited back to the restructuring line.**
- **Payments debit the liability, not wages.**
- **Statutory and discretionary elements are shown separately.**
- **Impairments, pension curtailments and acquisition-related restructurings are kept out of the provision.**
- **Names are used only where the accounting requires them**, and the working paper is built by cost type and headcount where it can be.
- **Every figure is attributed** — ledger-read or user-supplied.
- **Nothing is presented as posted.**
- **File naming consistent.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — and **any discount rate.**

**What is worth persisting into the workspace-scoped skill:**

1. **The plan register**: each restructuring, its approval and communication dates, its expected completion date, and **which account holds its reserve.** Without this, Test D has no date to test against and the rollforward cannot be split by plan.
2. **The recognition basis agreed per group**, and the reasoning — because the auditor will ask again next year.
3. **The account structure**: restructuring expense, restructuring liability, and which payroll accounts the severance payments run through. Test C needs the last of these.
4. **Whether the facility element was treated under the lease standard**, and the conclusion reached.
5. **Findings already raised and resolved**, with their explanations, so the same stale balance is not re-reported every quarter after the client has explained it.
6. **The completion status of each plan**, so a finished plan's reserve gets released rather than forgotten.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and **do not persist the employee list at all** once the accrual is settled. It has served its purpose and it is the most sensitive thing in the engagement.

**The evolved version's recurring job is Step 3b**, run every quarter: is this reserve still needed, is it still being used properly, and has anything new been swept into it?

---

## Anti-patterns

- **Accruing on board approval alone.** Recognition needs communication; a minute is not a communication.
- **Answering the future-service question once for a whole plan.** One restructuring commonly contains both treatments.
- **Building a cease-use liability on top of an ROU asset.** The lease standards changed this; check before double-counting the same obligation.
- **Letting a finished plan's reserve sit.** A provision no longer required must be released — and a reserve that sits is a balance available to smooth a bad quarter.
- **Releasing a reserve into ordinary operating costs.** The reversal belongs where the charge was.
- **Paying severance through wages while the accrual stands.** The cost is then recognised twice and the reserve never unwinds.
- **Sweeping later costs into an existing reserve.** A restructuring line reads as non-recurring; that is exactly why it attracts things.
- **Merging statutory redundancy with a discretionary enhancement.** Different obligations, potentially different dates.
- **Putting acquisition restructuring costs into the purchase price allocation.** They are post-combination expenses.
- **Calling an impairment a restructuring provision.** Different standard, different disclosure.
- **Treating a revised estimate as an error.** It is prospective.
- **Naming individuals in a working paper that does not need names.**
- **Aggregating a group restructuring into one liability** across entities.
- **Saying "posted" or "recognised".** The gateway reads; a person recognises.
