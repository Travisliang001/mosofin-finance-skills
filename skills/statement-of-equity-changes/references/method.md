<!-- statement-of-equity-changes · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 0 — Test every equity movement for a legitimate source *(Mosofin addition)*
- Step 1 — Identify the equity components
- Step 2 — Build the roll-forward grid
- Step 3 — Movement-by-movement detail
- Step 4 — Share count roll-forward (corporations)
- Step 5 — Tie-outs
- Step 6 — Comparative period
- Step 7 — Output
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
| **Opening equity balances by component** | Prior period closing | **Required** | **Live read** — and **compare to last year's reported closing**, see Step 0 | `[auto]` |
| **Net income / (loss)** | From the income statement | **Required** | Live read | `[auto]` |
| **OCI movements** | By component | Required if OCI exists | Live read | `[auto]` |
| **Equity transactions** | Issuances, buybacks, dividends, distributions, contributions, option exercises | **Required** | **Live read at transaction level, with source** | `[auto]` |
| **Entity type** | Corporation / partnership / LLC / sole proprietor / nonprofit | **Required** | Not in the books | `[manual]` |
| **Reporting framework** | US GAAP / IFRS / Other | **Required** | Not in the books | `[manual]` |
| Share counts (if corporation) | Opening shares, issuances, buybacks by class | Recommended | **Not in the books. No cap table on this surface.** | `[manual]` |
| Non-controlling interest movements | If consolidated with NCI | If applicable | **Arises in consolidation**, generally performed outside | `[manual]` |

---

## Workflow

### Step 0 — Test every equity movement for a legitimate source *(Mosofin addition)*

**`[auto]`. The one test in this skill that is not guaranteed to pass, and therefore the only one worth much.**

It implements the original's own final quality standard — *no equity movement without a documented source* — which the original states and provides no method for.

**Read every entry hitting every equity account for the period**, with its source, date, amount and description. Then classify.

#### Test 0a — What has hit retained earnings?

**Retained earnings should move for four reasons and no others:**

1. **Net income or loss**, via the closing entries
2. **Dividends or distributions declared**
3. **Prior-period adjustments**
4. **The cumulative effect of adopting a new accounting standard**

**Anything else posted directly to retained earnings needs explaining.**

This matters because **retained earnings is the most plug-prone account in the ledger.** It is large, it is not scrutinised transaction by transaction, and a difference posted into it disappears without affecting any current-period result. An expense misposted to RE never appears in the income statement. **A balance sheet forced into balance is very often forced there through retained earnings.**

| Finding | Meaning |
|---|---|
| Only closing entries, dividends, PPAs and adoption effects | Correct. |
| **A manual journal to RE with no matching category** | **Explain it.** It may be a legitimate reclassification; it may be an error that will never surface anywhere else. |
| **A journal to RE dated mid-period** | Closing entries land at period end. A mid-period RE posting is unusual by construction. |
| **RE debited against an expense or asset account** | Almost always an error or a deliberate burial. |

**Report factually, with dates, amounts and sources. Never as an allegation** — the commonest cause is somebody clearing a difference they could not otherwise resolve.

#### Test 0b — Does opening equity agree with last year's closing?

`[auto]`, one comparison.

**Opening equity this period must equal closing equity last period** — unless there is a prior-period adjustment line, which the statement is required to show explicitly.

If they differ and no adjustment line exists, **somebody has posted into a closed period.** This is the same test `quarter-end-close`, a restatement review and the 10-Q and 10-K preparation all run, and **it surfaces here as a visible line on a primary statement** — which is why the original requires prior-period adjustments to be shown on the opening balance line rather than absorbed.

#### Test 0c — Does every other equity account's movement have a recognisable transaction type?

`[auto]`. APIC, common stock, treasury stock and AOCI each have a small set of legitimate movements, set out in Step 3. **An entry to APIC that is not an issuance, an exercise, a stock compensation charge or a treasury reissuance is a movement without a source.** Same for the others.

**AOCI deserves particular attention**: it should move only for other comprehensive income items — translation, available-for-sale securities, hedges, pension remeasurement. **A direct posting to AOCI from an operating account is a misclassification that moves a result out of profit or loss**, which is exactly the sort of thing that gets found later.

---

### Step 1 — Identify the equity components

`[manual]` for the entity type; `[auto]` to read the accounts that exist. All four entity types preserved.

**Corporation** (most complex) — all seven components:

| Component | Note |
|---|---|
| **Common stock** (par value × shares) | **The par calculation needs share counts** — `[manual]` |
| **Preferred stock**, if any, **by series** | Each series tracked separately |
| **Additional paid-in capital (APIC)** | The excess over par, and where stock compensation accumulates |
| **Retained earnings / (accumulated deficit)** | Test 0a's subject |
| **Treasury stock** (contra-equity) | Reduces equity; carried at cost under the cost method |
| **Accumulated other comprehensive income / (loss) (AOCI)** | Not retained earnings — see Step 3 |
| **Non-controlling interest**, if consolidated | See Gate 1 |

**Partnership / LLC**:
- **Partners' / Members' capital**, by partner or member where reported individually
- Often combined: **contributed capital + accumulated earnings − distributions**

**Sole proprietor**:
- **Owner's capital**
- **Owner's draws**, closed into capital at year end

**Nonprofit (ASC 958)**:
- **Net assets without donor restrictions**
- **Net assets with donor restrictions**
- See nonprofit fund accounting — and note that the NFP statement of activities carries the *release from restrictions* line that moves between these two classes.

`[auto]` to read which equity accounts actually exist in the chart, **which is a useful cross-check on the stated entity type**: a chart with APIC and treasury stock is not a sole proprietorship, and a chart with partners' capital accounts is not a corporation. Where the stated type and the chart disagree, ask.

---

### Step 2 — Build the roll-forward grid

**`[auto]`.** The statement is a matrix — **components as columns, movements as rows.**

```
                          Common  Preferred  APIC   Retained  Treasury  AOCI    NCI    Total
                          Stock   Stock             Earnings  Stock
Opening balance            ...      ...       ...     ...       ...      ...     ...    ...
+ Net income                                          NI                                NI
+ Other comprehensive
    income                                                              OCI            OCI
+ Issuance of common
    stock                  par                APIC                                     proceeds
+ Stock-based comp                            SBC                                      SBC
+ Exercise of options      par                APIC                                     proceeds
- Repurchase of stock                                          (cost)                  (cost)
- Dividends declared                                  (div)                            (div)
+ Contributions
- Distributions
+/- Other                  ...     ...        ...     ...       ...      ...     ...    ...
Closing balance            ...      ...       ...     ...       ...      ...     ...    ...
```

**Every cell in this grid is `[auto]` except the split between par and APIC on issuances and exercises**, which needs the share count and the par value — `[manual]`. The **total** proceeds are readable; the **allocation** between the two columns is not.

**And note the "+/− Other" row.** In a manual statement this row absorbs whatever did not fit. **Test 0c exists so that it does not** — every item landing there should be named, and a populated "Other" row with no explanation is the equity statement's equivalent of a plug.

---

### Step 3 — Movement-by-movement detail

All movements preserved, each with its verdict.

**Net income** — adds to **retained earnings**. `[auto]`

**Other comprehensive income** — adds to **AOCI, not retained earnings.** Each OCI component (**CTA, available-for-sale securities, hedges, pension**) may be shown separately or combined. `[auto]` for the amounts; `[manual]` for presentation choice. See `foreign-currency-translation-asc830` for CTA — and carry its warning: **CTA is a plug, so a wrong translation rate does not fail to balance; it lands in CTA.**

**Dividends declared** (corporation) — **reduce retained earnings.** All three types preserved:

| Type | Treatment | Verdict |
|---|---|---|
| **Cash dividends** | Reduce RE; **create a dividend payable until paid** | `[auto]` |
| **Stock dividends** | Reduce RE; **increase common stock + APIC. No cash.** | `[auto]` for amounts, `[manual]` for the par split |
| **Property dividends** | Reduce RE **at the fair value of the property distributed** | `[manual]` — a fair value |

**Distributions** (partnership / LLC / sole proprietor) — reduce partner, member or owner capital. `[auto]`

**Stock issuances**:
- **Common stock at par** → Common Stock account
- **Excess over par** → APIC
- **Issuance costs** → **reduce APIC** under US GAAP, or expense — varies

`[auto]` for the total; `[manual]` for the par split. **`[auto]` for one check**: issuance costs expensed rather than netted against APIC is a presentation error visible in the cost accounts around the issuance date.

**Stock-based compensation** — **increases APIC as the expense is recognised over the vesting period**; the offsetting debit is compensation expense on the income statement. `[auto]` for what was posted; **`[manual]` for whether it is right**, which needs grant, vesting and forfeiture data.

**Option / warrant exercises**:
- **Cash received + par** → Common Stock
- **Excess** → APIC
- **Related APIC from prior stock compensation expense moves with the exercise**

`[auto]` for cash received; `[manual]` for the rest.

**Treasury stock**:
- **Repurchase**: reduce equity — debit Treasury Stock, a contra account, **at cost under the cost method**
- **Reissuance**: reduce Treasury Stock; **the difference goes to APIC or RE per the method**

`[auto]` for amounts; `[manual]` for the method — see the edge case.

**Capital contributions** — increase the relevant capital account. `[auto]`

**Prior-period adjustments / restatements** — **adjust opening retained earnings**, shown as **a separate line affecting the opening balance.** `[auto]` to detect (Test 0b); `[manual]` to conclude.

**Changes in non-controlling interest** — NCI's share of subsidiary net income and OCI, NCI dividends, acquisition or disposal of NCI. `[manual]` — see Gate 1.

---

### Step 4 — Share count roll-forward (corporations)

**`[manual]`, in full. There is no cap table on this surface.**

```
                                Shares
Opening shares outstanding       ...
+ Shares issued                  ...
+ Options/warrants exercised     ...
+ Stock dividend shares          ...
- Shares repurchased (treasury)  ...
Closing shares outstanding       ...
```

> **Distinguish issued versus outstanding — issued − treasury = outstanding. Track by class: common, preferred series.**

**Preserved in full and Mosofin cannot populate any of it.** Not the opening count, not any movement, not the class split.

**Present the empty schedule with a clear note** — *"requires cap table; not derivable from the general ledger"* — rather than omitting the step. It is a required part of the statement, tie-out 7 depends on it, and per-share disclosures elsewhere in the accounts depend on it too.

**The issued-versus-outstanding distinction is worth flagging to whoever completes it**, because it is the routine error: treasury shares remain **issued** and are not **outstanding**, and using the wrong one misstates every per-share figure in the accounts.

---

### Step 5 — Tie-outs

All eight preserved — **with the classification from the top of this file, because six of them are guaranteed.**

| # | Tie-out | Verdict | What it demonstrates |
|---|---|---|---|
| 1 | **Each component: opening + movements = closing** | `[auto]` | **Arithmetic.** Guaranteed. |
| 2 | **Total closing equity = balance sheet equity section** | `[auto]` | **Same accounts.** Guaranteed. |
| 3 | **Net income = income statement net income** | `[auto]` | **Guaranteed once closing entries are posted** — and **worth running before they are**, where the statement is being prepared pre-close, because then it is a real check. |
| 4 | **OCI = statement of comprehensive income** | `[auto]` | Same. |
| 5 | **Closing retained earnings = balance sheet RE** | `[auto]` | Same account. |
| 6 | **Closing AOCI = balance sheet AOCI** | `[auto]` | Same account. |
| 7 | **Closing share counts = shares disclosed on the BS / notes** | **`[manual]`** | **The only tie-out reaching outside the ledger — and the only one Mosofin cannot perform.** |
| 8 | **Dividends declared = dividends in the financing section of cash flow, adjusted for declared-but-unpaid** | **`[auto]`, and it has real content** | See below |

**Run all eight.** Guaranteed ties still catch a genuine class of error — a component omitted from the statement, a movement posted to the wrong column, a comparative pulled from the wrong period. **But label which are guaranteed**, so a reader does not treat six automatic ticks as six independent confirmations.

#### Tie-out 8 is the one with substance

`[auto]`, and it is genuinely three-way:

```
Dividends declared (equity statement, at declaration)
  less  Increase in dividend payable
  =     Dividends paid (cash flow, financing)
```

**The equity statement reflects declaration; the cash flow reflects payment; the dividend payable holds the difference.** Three separate places in the accounts, and they must be mutually consistent — which is not guaranteed, because a dividend declared in one period and paid in the next touches all three at different times.

`[auto]` computes all three legs and the reconciliation. **A break here means either a dividend declared and never recorded as payable, or a payment made against no declaration** — and both are real errors. See `cash-flow-statement-indirect-method`.

---

### Step 6 — Comparative period

**`[auto]`.**

> **Present the prior period's roll-forward as well** — typically two or three years of movement for annual filings.

Read both periods in the same batch. **And run Test 0b across each boundary**, not only the current one: a three-year statement has two opening-balance transitions, and a prior-period posting can sit at either.

**Where comparatives have been restated** — after a stock split, a reverse split, or a prior-period adjustment — **the restated figures must be used consistently across all periods presented.** `[auto]` to check the presented comparative against what was previously reported, which is the 10-Q and 10-K preparation's comparatives test applied to this statement.

---

### Step 7 — Output

An `.xlsx` workpaper. All five of the original's sheets, plus two additions.

**Sheet 1: Statement of Changes in Equity**
The full matrix, current and comparative periods. `[auto]` for the amounts; **par/APIC splits marked as requiring share data.**

**Sheet 2: Movement Detail**
**Each movement explained with its source** — journal reference, income statement line, transaction. **`[auto]`, and this sheet is the evidence for the last quality standard**, which is otherwise an aspiration. Every row carries its source document and date.

**Sheet 3: Share Count Roll-Forward**
By class. **`[manual]` — presented as an empty schedule with the note "requires cap table; not derivable from the general ledger."** Never omitted.

**Sheet 4: Tie-Outs**
The eight validations — **each marked as *guaranteed by construction* or *independent*.** Tie-out 7 marked as not performable. Tie-out 8 shown as the three-way reconciliation.

**Sheet 5: Dividends / Distributions Detail**
Declaration dates, payment dates, per-share amounts. `[auto]` for dates and amounts; `[manual]` for per-share.

**Sheet 6: Equity Movement Source Test** *(Mosofin addition)*
The Step 0 results:

| Account | Entry date | Amount | Source | Recognised category? | Explanation |
|---|---|---|---|---|---|

Direct postings to retained earnings. Opening-balance breaks. Unrecognised movements in APIC, AOCI and treasury stock. Anything that would otherwise land in "Other."

**Sheet 7: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Statement_of_Equity_[YYYY-MM]_[EntityName].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 4.

---

## Output Quality Standards

All nine preserved.

- **Every component rolls forward: opening + movements = closing.** `[auto]` — **guaranteed; label it as such.**
- **Total closing equity = balance sheet equity section.** `[auto]` — guaranteed.
- **Net income and OCI tie to their statements.** `[auto]` — guaranteed post-close.
- **Share counts roll forward by class.** **`[manual]` — no cap table on this surface.**
- **Dividends and distributions tie to cash flow, adjusted for timing.** **`[auto]`, and genuinely independent** — the three-way reconciliation in tie-out 8.
- **Comparative period included.** `[auto]`, with the boundary test run at each transition.
- **Prior-period adjustments shown on the opening balance line.** `[auto]` to detect the break; **shown as a line, never absorbed.**
- **File naming consistent.** `[auto]`
- **No equity movement without a documented source.** **`[auto]` — Step 0, and the only substantive test in the skill.** Sheet 6 is its evidence.

**Four Mosofin additions:**

- **Guaranteed tie-outs are labelled as guaranteed**, so six automatic ticks are not read as six confirmations.
- **Every movement carries its source document**, which is what makes the last standard testable.
- **Retained earnings is tested against its four legitimate movement types.**
- **The share schedule is presented empty with its reason**, never omitted.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh.

**What is worth persisting into the workspace-scoped skill:**

1. **The account-to-component mapping** — which chart accounts constitute common stock, APIC, AOCI, treasury and so on. Established once; every subsequent statement builds itself.
2. **The entity type, framework and treasury method.**
3. **Par values by class**, which do not change, and which are half of what the par/APIC split needs.
4. **The share roll-forward as supplied**, so next period starts from a known opening count rather than re-requesting the whole history. **The cap table remains authoritative** — this is a convenience copy, and it must be reconciled to the cap table each period rather than trusted.
5. **The prior period's closing balances as reported**, so Test 0b has a baseline that does not depend on re-reading old accounts.
6. **Explanations already given for unusual movements**, so the same journal is not re-queried every quarter.
7. **The dividend declaration and payment pattern**, for tie-out 8.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — partner capital balances and distribution histories are personal financial information.

**The evolved version's job is the source test and the deltas**: what moved in equity this period, did each movement have a legitimate source, and does the opening balance still agree with what was reported.

---

## Anti-patterns

- **Presenting six guaranteed tie-outs as six confirmations.** Label which are arithmetic.
- **Treating the balance sheet equity section as independent evidence.** Same accounts.
- **Skipping the source test** because the roll-forward already ties. The roll-forward always ties.
- **Leaving a direct posting to retained earnings unexplained.** RE moves for four reasons.
- **Absorbing a prior-period adjustment into the opening balance.** It is a required separate line.
- **Populating an "Other" row without naming what is in it.**
- **Omitting the share schedule** because it cannot be filled. Present it empty with its reason.
- **Confusing issued with outstanding.** Treasury shares stay issued.
- **Putting OCI into retained earnings.** It goes to AOCI.
- **Treating a buy-out of minority shares as a purchase.** It is an equity transaction; no gain or loss.
- **Missing a negative partner capital account.** It is readable and it has tax consequences.
- **Applying two treasury stock methods in one book.**
- **Assuming the ledger's par/APIC split is right.** It depends on share counts nobody in the ledger knows.
- **Saying "posted".** The gateway reads.
