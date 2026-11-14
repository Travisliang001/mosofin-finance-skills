<!-- year-end-close · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Run the standard monthly and quarterly close
- Step 1b — Verify all twelve months are closed *(Mosofin addition)*
- Step 2 — Year-end specific procedures
- Step 3 — Statutory and regulatory filings
- Step 4 — Audit execution
- Step 5 — Closing the year and opening the new one
- Step 5b — Verify the books stayed locked *(Mosofin addition)*
- Step 5c — Verify the new year opened clean *(Mosofin addition)*
- Step 6 — Reflection and process improvement
- Step 7 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

A block with many tasks carries many verdicts. That is shown rather than averaged.

**Everything here is a proposal.** The gateway is read-only. **Mosofin posts no entry, locks no period, signs no representation letter, and files nothing.**

---

## Inputs

All nine preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Fiscal year-end date** | Date | **Required** | **`[auto]`** from the company record; confirm | `[auto]` |
| **Reporting framework** | US GAAP / IFRS / Local GAAP | **Required** | Not in the books | `[manual]` |
| **Audit type** | Full audit / Review / Compilation / None | **Required** | Not in the books | `[manual]` |
| Audit firm and timeline | Firm, dates | Recommended | Not in the books | `[manual]` |
| **Statutory filings in scope** | Tax returns, regulator filings, payroll year-end forms | **Required** | Not in the books; **persist** | `[manual]` |
| **Materiality (year-end)** | Often tighter than monthly | **Required** | **`[auto]` for the benchmarks**; the threshold is a judgment | Split |
| Major events during the year | Acquisitions, divestitures, raises, debt, restructurings | Recommended | **Not identifiable as events; their accounting traces are readable** | `[manual]`, `[auto]` in part |
| Going-concern indicators | Liquidity issues, covenant pressure | Recommended | **`[auto]` for the facts** — cash, burn, ratios, ageing | `[auto]` inputs |
| Prior year findings / management letter | Carry-forward issues | Recommended | Not in the books; **should be in the profile from last year** | `[manual]` |

---

## Workflow

### Step 1 — Run the standard monthly and quarterly close

> **Year-end is also a month-end and a quarter-end. Run those procedures fully. This skill adds year-end-specific tasks on top.**

**`[auto]` by delegation** to `month-end-close-checklist` and `quarter-end-close`. Both already scope themselves from the live chart and self-verify their entry-based tasks; there is no reason to re-derive any of it.

---

### Step 1b — Verify all twelve months are closed *(Mosofin addition)*

**`[auto]`, one query, and it is the year-end version of a test `quarter-end-close` runs across three months.**

**A year closed on top of an unclosed August produces a year-end that ties and is wrong.** For each of the twelve months, confirm:

- **The recurring entries ran** — depreciation, amortisation, prepaid releases, accruals. See `recurring-transaction-builder` and `prepaid-amortization-schedule`.
- **Accruals reversed** where they should have. See `journal-entry-review`.
- **Nothing was posted into the month after it was declared closed.**
- **The month's activity looks complete** against its neighbours — a materially lower transaction count is a month still open.

**Report by month, not in aggregate.** A single unclosed month is invisible in an annual total and obvious in a twelve-row table — and **finding it in December is far cheaper than the auditor finding it in March.**

---

### Step 2 — Year-end specific procedures

**Fifteen blocks. All preserved in full, each with its verdict.**

---

#### Audit prep

| Task | Verdict |
|---|---|
| **PBC (Provided By Client) list compilation** | **`[auto]` for the ledger-derived portion** — see Step 2a. `audit-prep-pbc-list` |
| **Lead schedules / supporting workpapers for every material BS account** | **`[auto]` to build the composition and roll-forward; `[manual]` to make it a workpaper** |
| **Confirmation letters** — cash (bank), AR (positive / negative from customers), debt (lenders), legal (attorney letters) | **`[manual]`, entirely** — see below |
| **Subsequent events documentation** | `[auto]` for the transactional sweep; **`[manual]` for completeness.** See the subsequent events review |
| **Management representation letter draft** | **`[manual]`** — management represents |
| **Schedules of estimates and judgments** | `[auto]` for the roll-forwards and rate trends; `[manual]` for the judgments |

**On confirmations, per the opening section.** All four types are **third-party evidence obtained by the auditor.** The entity supplies names and balances; **the confirmation is the counterparty's reply, and it exists precisely because the entity's own records are not sufficient evidence of them.**

`[auto]` supplies the population — which banks, which customers, which lenders — **and the balances to be confirmed**, which is a real contribution to the process and is not the procedure. **Attorney letters are further out still**: legal exposure is not in any ledger, and the letter is the mechanism by which it enters the accounts at all.

---

#### Step 2a — Assemble the ledger-derived PBC *(Mosofin addition)*

**`[auto]`. The single largest time saving this skill offers.**

**Most of a first-week PBC list is ledger output.** Not judgment, not documents — extracts:

| PBC item | Verdict |
|---|---|
| Trial balance, year-end and prior year | **`[auto]`** |
| General ledger detail for the year | **`[auto]`** |
| AR ageing at year-end, with subsequent receipts | **`[auto]`** |
| AP ageing at year-end, with subsequent payments | **`[auto]`** |
| Fixed asset additions, disposals and depreciation | **`[auto]`** for the GL side |
| Roll-forwards of every reserve and provision | **`[auto]`** |
| Bank reconciliations | **`[auto]`** for the book side; **the statement is not on this surface** |
| Debt schedules and interest | **`[auto]`** for balances; terms from the agreements |
| Revenue by month, by customer, by category | **`[auto]`** |
| Journal entry listing, especially manual and period-end entries | **`[auto]`** — and see `journal-entry-review` |
| Related party transactions | **`[auto]`** for the match; see the related party disclosures |
| Payroll reconciliation to GL | **`[auto]`** for the GL side; the register is not on this surface |

**Why this matters more than it sounds.** The first two or three weeks of a fieldwork engagement are commonly spent **requesting and waiting for exactly these extracts** — and the client's finance team is producing them by hand while also trying to close. **Delivering them on day one changes the shape of the audit**, and it is a batched read.

**What it is not**: the whole PBC. **Documents, contracts, minutes, confirmations, policies and explanations are the rest**, and they are the parts that take judgment. **Present the assembled portion as the assembled portion**, with the remainder listed as outstanding and owned.

---

#### Tax provision (full year)

| Task | Verdict |
|---|---|
| **Year-end actual effective tax rate** | **`[auto]`** |
| **True-up YTD provision to actuals** | **`[auto]`** to compute |
| **Discrete items recognised** | `[manual]` |
| **Deferred tax true-up**: temporary differences, NOLs, credits | **`[manual]`** — **tax attributes are not ledger balances**, per the corporate tax return preparation |
| **Valuation allowance assessment** | **`[manual]`** — a judgment about future profitability |
| **FIN 48 / IAS 12 uncertain positions update** | `[manual]` |

Hand off to the tax provision work, and see the deferred tax roll-forward.

**The valuation allowance is worth flagging** as one of the most judgmental estimates in the accounts: it turns on whether future taxable profit will exist to use the attribute, **which is a forecast**, and `[auto]` contributes only the historical profitability that informs it.

---

#### Statutory tax returns

| Return | Verdict |
|---|---|
| **Corporate income tax returns** — federal, state/provincial, local, foreign | `[auto]` for the starting point; `[manual]` for the computation. the corporate tax return preparation |
| **Information returns: 1099 / T4A** | **`[auto]` for the payment populations**; see the 1099 and T4A preparation and vendor onboarding |
| **Withholding tax reconciliations and returns** | `[auto]` for what was withheld and remitted |
| **Sales tax / VAT / GST annual reconciliation to filings** | **`[auto]` for the control accounts**; the filings are documents. the sales tax work, the VAT and GST work |
| **Property tax returns** | `[manual]` |
| **Transfer pricing documentation update** | `[auto]` for the intercompany flows; the transfer pricing documentation |
| **R&D credit substantiation** | **`[auto]` for the cost population**; `[manual]` for qualification. the R&D tax credit work |

**The information returns block has a preventive angle worth using**: vendor onboarding's Step 0b identifies **actively-paid vendors with no tax form on file**, ranked by amount. **Running that in November rather than January is the difference between requesting a form and filing without one.**

---

#### Payroll year-end

| Task | Verdict |
|---|---|
| **W-2 / T4 / equivalent annual employee tax forms** | **`[manual]`** — the payroll register produces them |
| **W-3 / T4 Summary / transmittal** | `[manual]` |
| **Year-end payroll reconciliation** | **`[auto]` for the GL side**; `payroll-reconciliation` |
| **Reconcile YTD payroll to GL** | **`[auto]` for the GL side; the register is the other half and is not on this surface** |
| **Reconcile YTD withholding to remittances and forms** | `[auto]` for remittances; forms are documents |
| **401(k) / pension contribution year-end** | `[auto]` for amounts; the benefits accounting |
| **Stock-based comp settled at year-end** | **`[manual]` — no cap table on this surface**; the equity compensation accounting |

**The recurring absence across the payroll quartet applies here in full**: `payroll-clearing-reconciliation`, `payroll-journal-entry-builder`, `payroll-reconciliation` and the payroll tax filings all note that **the payroll register is the missing half.** At year-end the reconciliation of GL to register is a required procedure and **only one side of it is readable.**

---

#### Estimates and reserves (full review)

**Ten preserved.** `[auto]` for every roll-forward and rate trend; `[manual]` for every judgment.

| Estimate | Verdict | Cross-reference |
|---|---|---|
| **Allowance for doubtful accounts — fresh look** | `[auto]` roll-forward and rate; `[manual]` judgment | `bad-debt-and-write-offs` |
| **Inventory reserve — fresh look** | Same | `inventory-obsolescence-and-reserve`, `inventory-to-gl-reconciliation` |
| **Warranty reserve** | Same | |
| **Litigation accruals** — legal letter coordination | **`[manual]`** | Attorney letters |
| **Restructuring reserves** | `[auto]` roll-forward; `[manual]` judgment | the restructuring accounting |
| **Asset retirement obligations** | `[manual]` | `asset-retirement-obligations-asc410` |
| **Self-insurance reserves** | `[manual]` — actuarial |
| **Deferred compensation** | `[auto]` for balances; `[manual]` for the arrangement |
| **Pension / OPEB** — actuarial reports | **`[manual]`** | the pension accounting |
| **Stock-based comp forfeiture rate** | **`[manual]` — no cap table** | the equity compensation accounting |

**"Fresh look" is the operative phrase in the first two**, and `quarter-end-close`'s test applies with more force at year-end: **a reserve rate identical to four decimal places for eight quarters is not being reviewed.** `[auto]` shows the rate series; the fresh look is a person's.

---

#### Impairment testing

| Test | Verdict |
|---|---|
| **Goodwill annual impairment test** — **typically required at fiscal year-end at minimum** | **`[manual]`** — needs fair values. the goodwill impairment test |
| **Long-lived assets impairment review** — triggering events | `[auto]` for **some** indicators; `[manual]` for the test |
| **Intangible assets impairment review** | Same. the intangibles register |
| **Investments other than trading securities** | `[manual]` — valuations |

**The goodwill test is annual and mandatory**, which makes it a year-end procedure rather than a triggered one — **and it is entirely dependent on valuations that are not on this surface.** Consistent with the business combination accounting, a valuation and property accounting. Plan for it early; it needs an external input with a lead time.

---

#### Going-concern assessment

**`[manual]` for the assessment; `[auto]` for the facts.** All four preserved:

- **12-month look-forward from issuance of the financial statements**
- **Substantial doubt? Manageable?**
- **Plans to address**
- **Disclosure consideration**

`[auto]`: cash and its trend, operating burn or generation, working capital and current ratio at each period end, total debt, receivables concentration.

**`[manual]`, and not derivable**: **debt maturity dates** — in the loan agreements, not the balance sheet; undrawn facility headroom; funding plans; letters of support.

**And the rule that runs through the MD&A and `quarter-end-close`: never author a forward-looking statement.** A going-concern conclusion is a management assertion with legal weight and audit consequences. **Present the liquidity facts; management assesses and signs.**

---

#### Statement of cash flows (annual)

`[auto]`. All three preserved: **full year with prior year comparative; direct or indirect method — typically indirect for US GAAP and most IFRS; reconciliation of operating activities.**

Built from balance sheet movements and net income, all live. See `cash-flow-statement-indirect-method`.

---

#### Disclosures preparation

`[auto]` for the figures; **`[manual]` for the narrative and for completeness.** All seven preserved:

| Disclosure | Verdict |
|---|---|
| **Full notes to financial statements** | `[auto]` figures, `[manual]` text. the notes to the financial statements |
| **Significant accounting policies** | `[manual]` |
| **Segment information** | **`[auto]` if segments are a dimension**; segment reporting |
| **Related party transactions** | `[auto]` for the match, `[manual]` for the universe. the related party disclosures |
| **Commitments and contingencies** | **`[manual]` — not transactions** |
| **Subsequent events through report date** | `[auto]` sweep, `[manual]` completeness. the subsequent events review |
| **Risk factors** | `[manual]` |

**The pattern is consistent across all seven and worth naming at the end of the pack**: **the amounts are readable and the completeness is not.** A ledger tells you the size of everything disclosed; it can never tell you that something disclosable was omitted, because omission leaves no trace. **That is what the checklist and the reviewer are for.**

---

#### Statement of equity changes

`[auto]` for the dollar roll-forward of every component — common stock, APIC, retained earnings, AOCI, treasury. **`[manual]` for share counts.** See the statement of changes in equity, and its point that **six of its eight tie-outs are guaranteed by construction** — the substantive test is the source test on every equity movement.

---

#### Consolidation (multi-entity)

| Task | Verdict |
|---|---|
| **Full consolidation procedures** | `[manual]` where performed outside. the consolidation |
| **Currency translation through year-end** | `[auto]` mechanics — **and CTA is a plug**, so prove it independently. the foreign currency translation work |
| **Intercompany eliminations** | **`[auto]` where both sides are connected.** `intercompany-reconciliation` |
| **Minority interest / non-controlling interest** | `[manual]` — arises in consolidation |

---

#### Fixed assets year-end

| Task | Verdict |
|---|---|
| **Full FA register review** | `[auto]` for the GL side; **the register is outside.** Run the reconciliation **in both directions.** `fixed-asset-register-and-depreciation` |
| **Physical asset count** — typically annual | **`[manual]`. Only counting says what is there.** |
| **Disposal review** | `[auto]` for disposals posted; **`[auto]` for assets still depreciating that the count could not find** |
| **Impairment screen** | `[auto]` for indicators; `[manual]` for the test |
| **Useful life review** where circumstances changed | `[manual]` |

**The count deserves the same treatment as a petty cash count's**: the register says what should exist; **the count is the only evidence of what does.** And the `[auto]` complement is genuinely useful — **assets on the register that the count did not find** is a list the count produces and the ledger cannot.

---

#### Lease year-end

All five preserved. `[auto]` for the GL side; **the lease schedule is outside.**

- **ROU asset and lease liability roll-forward** — `[auto]` for the balances
- **Modifications during the year** — `[manual]`
- **Impairment / abandonment review** — `[manual]`
- **Reassessment of lease term / discount rate where required** — `[manual]`
- Hand off to the lease accounting

**And the standing detection from that skill**: **rent expense with no ROU asset means unrecognised leases** — recurring equal payments to a landlord are the signature, and year-end is when it should be swept for.

---

#### Revenue year-end

| Task | Verdict |
|---|---|
| **Full ASC 606 / IFRS 15 review** | `[manual]` for the five-step analysis; **`[auto]` for the Step 0 tests** in the revenue recognition review — is the standard being applied at all? |
| **Backlog / RPO disclosure** | **`[manual]` — RPO includes unbilled commitments and is not the deferred revenue balance** |
| **Contract balance roll-forwards** | **`[auto]`** |
| **Disaggregation by required dimensions** | `[auto]` where the dimensions exist |

---

#### Restatement / prior-period adjustment review

> **Errors discovered during year-end? Material? Hand off to a restatement review.**

**`[auto]` to detect, and this is where that skill's primary test belongs**: **compare the prior year's figures as they stand in the ledger today against the prior year's issued statements.** A difference means somebody posted into a reported period. **`[manual]` for the materiality conclusion and the correction method.**

---

### Step 3 — Statutory and regulatory filings

All four categories preserved. **`[manual]` to file, throughout.**

**For SEC filers:**
- **10-K drafting** — `[auto]` for the statements; `[manual]` for the document. the 10-Q and 10-K preparation
- **Item 9A (Controls and Procedures)** — **full ICFR testing and reporting if an accelerated filer.** `[manual]`; `sox-controls-design-and-testing`
- **Exhibits and certifications** — `[manual]`
- **Proxy statement coordination** — `[manual]`

**For private entities with statutory filing requirements:**
- **Corporate annual report / accounts filing** — Companies House in the UK, equivalents across the EU and Commonwealth
- **Director's reports**
- **Strategic / Business reports**

`[auto]` for the financial content; `[manual]` for the narrative and the filing.

**For nonprofits:**
- **Form 990 (US)** — nonprofit fund accounting
- **Charity commission filings (UK)**
- **Equivalents in other jurisdictions**

**For regulated industries:**
- **Industry-specific regulator filings** — banking, insurance, broker-dealer, utility. `[manual]`

**Deadlines are the thing to track**, and they differ per filing and per jurisdiction — Sheet 8 exists for it. **Persist them**; they recur annually and unchanged.

---

### Step 4 — Audit execution

**`[manual]` throughout, with one `[auto]` contribution.** All seven preserved.

| Item | Verdict |
|---|---|
| **PBC delivery on schedule** | **`[auto]` for the ledger-derived portion** — Step 2a |
| **Auditor walkthroughs and inquiries** | `[manual]` |
| **Substantive testing support** | **`[auto]` in large part** — most substantive requests are "show me the detail behind this", which is a query |
| **Confirmations management** | `[manual]` |
| **Auditor's adjusting entries — review, accept or push back, post** | **`[manual]`**, and see below |
| **Audit findings and recommendations** | `[manual]` |
| **Final management representation letter** | `[manual]` |
| **Audit report sign-off** | `[manual]` |

**On the auditor's adjusting entries**, per the third near-substitute: **review, accept or push back is a negotiation.** `[auto]` can quantify a proposed adjustment's effect on every affected balance and on the comparatives — **which is genuinely useful input to the decision.** **The decision is the entity's and its auditor's**, and Mosofin accepts nothing on anyone's behalf.

**And note that unadjusted differences accumulate**: an adjustment declined as immaterial this year sits on a schedule and is considered again next year, in aggregate. **That is the same arithmetic a restatement review insists on** — individually minor items assessed in combination — and `[auto]` should do it.

---

### Step 5 — Closing the year and opening the new one

`[auto]` to draft and verify; **`[manual]` to post and lock.**

- **Final adjusting entries posted** — `[manual]`
- **Closing entries** — `[auto]` to draft; `closing-entries-and-trial-balance`:
  - **Close revenue accounts to Income Summary / Retained Earnings**
  - **Close expense accounts to Income Summary / Retained Earnings**
  - **Net income to Retained Earnings**
  - **Dividends / distributions to Retained Earnings**
- **Books locked for the closed year** — **`[manual]`**
- **New fiscal year opened with zero P&L balances and rolled-forward BS** — `[manual]` to open; **`[auto]` to verify**

---

### Step 5b — Verify the books stayed locked *(Mosofin addition)*

**`[auto]`, and at year-end it matters more than anywhere.**

**A lock is a control and controls fail.** Read for any entry posted into the closed year **after the lock date** — with its date, amount, account, source and author.

**Why year-end is the worst place for this to happen**: the year's figures are **audited, filed, and become the comparative in every subsequent report.** A post-lock entry means the audited statements and the ledger have diverged — and every comparative drawn from the ledger thereafter disagrees with what was filed.

**Run it at the lock, and run it again before the accounts are issued.** Route anything found to a restatement review, which treats exactly this as its primary detection.

---

### Step 5c — Verify the new year opened clean *(Mosofin addition)*

**`[auto]`, one query, and it catches an error that otherwise surfaces months later.**

Read the new year's **opening trial balance**:

| Check | What a failure means |
|---|---|
| **Every P&L account opens at zero** | **A P&L account with an opening balance means the closing entries did not complete.** The new year's results are overstated from day one, and nobody notices until a variance analysis looks odd. |
| **Every balance sheet account opens at last year's closing balance** | A mismatch means either the roll-forward failed or something moved after the close. |
| **Retained earnings opening = prior closing + net income − distributions** | The closing entries' arithmetic, verified independently. |

**All three are exact, and all three are routinely assumed.** A partially-completed close is a silent error with a long tail — **and it takes one read to rule out.**

---

### Step 6 — Reflection and process improvement

**All four preserved — and this step is the lifecycle, already present in the original.**

- **Carry-forward issues for next year**
- **Auditor management letter responses**
- **Process improvements identified**
- **Updated close calendars and templates**

**It is worth ending on this**, because it is what the seed-to-evolved section of every skill in this pack has been describing: **capture what was learned so next year starts further forward.** The source's own final step asks for updated calendars, updated templates and carried-forward issues — **which is precisely what `create_skill` persistence exists to hold.**

`[auto]` contributes the measurable part: **how long each phase actually took**, which tasks slipped, how many auditor adjustments arose and where, which accounts generated the most queries. **Next year's calendar should be built from this year's actuals rather than from last year's plan** — the same discipline `rolling-forecast` applies to forecasting.

---

### Step 7 — Output

An `.xlsx` workpaper. All ten of the original's sheets, plus two additions.

**Sheet 1: Year-End Calendar**
Detailed timeline from late November or December through audit completion. **Add a Verdict column** and **build the durations from last year's actuals** where the profile holds them.

**Sheet 2: PBC List**
Audit-firm-aligned schedule of supporting documents. **`[auto]` items marked as assembled and attached; everything else listed with an owner and a date.** `audit-prep-pbc-list`.

**Sheet 3: Lead Schedules Index**
Master list of supporting workpapers per balance sheet account. **`[auto]` for the completeness check**: every account above materiality has a schedule — which is the source's own second quality standard, made testable.

**Sheet 4: Tax Provision Workpaper**
Current and deferred provision, ETR walk, deferred tax roll. `[auto]` for the ETR and the current position; `[manual]` for deferred attributes.

**Sheet 5: Estimates and Judgments Memo**
Each significant estimate with **methodology, inputs, change in estimate, sensitivity.** **Add the rate series and quarters-unchanged**, per the fresh-look point.

**Sheet 6: Going Concern Assessment**
`[auto]` facts; `[manual]` conclusion. **Never authored by Mosofin.**

**Sheet 7: Subsequent Events Log**
**With a Source column** — ledger sweep or enquiry — and the completeness note. the subsequent events review.

**Sheet 8: Statutory Filings Tracker**
| Filing | Due Date | Jurisdiction | Owner | Status | Filed Date |

**Every row has a named human.** Deadlines persisted from last year.

**Sheet 9: Final Tie-Out and Books Locked**
**With the Step 5b and 5c results**: post-lock entries, and the new year's opening verification.

**Sheet 10: Carry-Forward Items**
For the new year. **This sheet is next year's Gate 3 input** — see Step 6.

**Sheet 11: Close Completeness Tests** *(Mosofin addition)*
| Test | Result | Detail | Action |
|---|---|---|---|

Twelve months verified closed. Post-lock entries. New year opening. Prior-year comparatives against issued statements. Accounts above materiality without a lead schedule.

**Sheet 12: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `YearEndClose_[FY-end]_[EntityName].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name, on the calendar, and **at the head of the PBC.**

---

## Output Quality Standards

All ten preserved.

- **Audit PBC complete and dated before auditor arrival.** **`[auto]` for the ledger-derived portion, assembled in advance**; `[manual]` for the rest, with owners.
- **All material accounts have a lead schedule.** **`[auto]` to test** — read the trial balance, apply materiality, check coverage. **A completeness test on the audit prep itself.**
- **Estimates documented with methodology and inputs.** `[auto]` for roll-forwards and rate series; `[manual]` for the documentation.
- **Tax provision tied to current and deferred positions.** `[auto]` current; `[manual]` deferred.
- **Statutory filings tracked with owners and dates.** `[auto]` to track; `[manual]` to file.
- **Going-concern assessment present and documented.** `[auto]` facts; **`[manual]` conclusion, never authored here.**
- **Books closed and locked with sign-off.** `[manual]` to lock; **`[auto]` to verify it held.**
- **New year opened cleanly.** **`[auto]` — Step 5c, and it is exact.**
- **File naming consistent.** `[auto]`
- **Carry-forward items captured for next year.** **`[manual]` to identify; persisted, so next year begins with them.**

**Five Mosofin additions:**

- **All twelve months are verified closed**, individually, not in aggregate.
- **The ledger-derived PBC is assembled before the auditor asks.**
- **The lock is verified**, at the lock and again before issuance.
- **The new year's opening balances are verified**, P&L at zero and balance sheet rolled.
- **Next year's calendar is built from this year's actual durations.**

---

## Seed to evolved: what happens on the first real run

**Step 6 is this section, written by the original author**, and it is a good note to end the pack on: **the source already asks for carry-forward issues, updated calendars and updated templates.** The lifecycle is not something the conversion imposed; it is something the original wanted and had no mechanism for.

**What must never be frozen into a seed:** a capability snapshot. Capabilities change, policies tighten and loosen, and **a seed that hardcodes today's map is wrong the first time anything changes and wrong silently.** Gate 2 reads it fresh, every run, every year.

**What is worth persisting into the workspace-scoped skill:**

1. **The close calendar with actual durations**, so next year's plan is built from what happened rather than what was hoped.
2. **The PBC list as the auditor actually requests it**, split into ledger-derived and other — **the second year's PBC is assembled on day one.**
3. **The lead schedule index**, mapping accounts to schedules.
4. **Estimate methodologies and their rate history**, so "fresh look" has a baseline.
5. **Statutory filings, deadlines and owners** — annual and unchanging.
6. **The audit adjustments raised**, adjusted and unadjusted, since unadjusted differences aggregate across years.
7. **The management letter points and their remediation status.**
8. **Carry-forward items** — Sheet 10, which becomes next year's Gate 3 input.
9. **Anything the coverage sheet recorded as a divergence from this file's defaults.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — the seed goes to the next engagement and must arrive carrying no client's materiality, no client's auditor, and no client's accounts.

**The second year-end should be materially easier than the first**, and the measure of whether this skill worked is whether it is.

---

## Anti-patterns

- **Closing December and calling the year closed.** Twelve months, each verified.
- **Assuming the lock held.** It is one query, and a post-lock entry means the ledger and the audited accounts have diverged.
- **Assuming the new year opened clean.** A P&L account with an opening balance is a silent error with a long tail.
- **Presenting a ledger extract as a lead schedule.** The tie to evidence and the analysis are what make it a workpaper.
- **Treating a pre-assembled PBC as a complete PBC.** Documents, contracts, minutes and confirmations are the rest.
- **Substituting the client's own records for a confirmation.** The point of a confirmation is that it comes from somebody else.
- **Substituting the register for a count.**
- **Authoring a going-concern conclusion.**
- **Accepting an auditor's adjustment on the client's behalf.**
- **Dismissing unadjusted differences one year at a time.** They aggregate.
- **Reading a stable reserve rate as a completed fresh look.**
- **Leaving the goodwill impairment test late.** It needs a valuation with a lead time, and it is mandatory annually.
- **Reporting a clean sweep from fixture data to an audit team.**
- **Building next year's calendar from last year's plan** rather than this year's actuals.
- **Discarding the carry-forward sheet.** It is next year's starting position, and Step 6 exists to produce it.
- **Saying "closed", "locked", "filed" or "audited".** The gateway reads; people close, lock, file and audit.
