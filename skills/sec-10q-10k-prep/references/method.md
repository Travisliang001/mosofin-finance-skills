<!-- sec-10q-10k-prep · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Build the close-to-file calendar
- Step 2 — Establish tie-out discipline
- Step 2b — Check the comparatives against what was filed *(Mosofin addition)*
- Step 3 — Disclosure checklist
- Step 4 — Drafting workflow
- Step 5 — Controls and sign-offs
- Outputs
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is preparation.** The gateway is read-only. **Mosofin drafts no filing, signs no certification, tags no XBRL, and files nothing with the SEC.**

---

## Inputs

All six preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Reporting calendar** | Deadlines for filing and earnings | **Required** | **Not in the books.** Driven by filer status. | `[manual]` |
| **Trial balance and consolidation** | Reporting package | **Required** | **Trial balance is a live read. The consolidation may not be** — see Gate 1. | `[auto]` in part |
| **Prior filings** | 10-Q / 10-K, press releases | **Required** | **Not in the books — and the ledger's view of a prior period is not what was filed.** See Step 2b. | `[manual]` |
| **Significant events** | M&A, debt, equity, impairments, restructurings | **Required** | **Not identifiable as events**; their accounting consequences are readable | `[manual]`, `[auto]` in part |
| Accounting policies | Memo library | Recommended | Not in the books | `[manual]` |
| Disclosure controls | DCP / SOX evidence | Recommended | **Not in the books** — evidence of human review | `[manual]` |

---

## Workflow

### Step 1 — Build the close-to-file calendar

`[manual]` for the dates and owners. `[auto]` for one thing that matters.

All eight milestones preserved:

| Milestone | Verdict |
|---|---|
| **Day 0 close kickoff** | `[manual]` |
| **Preliminary analytics** | **`[auto]`** — period-over-period and ratio analysis are live reads, and having them ready on day 1 rather than day 6 is a genuine compression of the calendar |
| **Draft financials** | `[manual]` — the document |
| **Footnote drafting** | `[manual]` for the text; `[auto]` for the figures. See `notes-to-financial-statements` |
| **Legal review** | `[manual]` |
| **Auditor review** | `[manual]` — and **mandatory**, not substitutable |
| **XBRL prep** (if applicable) | `[manual]`. See `xbrl-tagging-checklist` |
| **Final tie-out and sign-off** | `[auto]` for the ledger side of each tie-out; `[manual]` for the sign-off |

**Assign owners and due dates.** `[manual]`, and **every milestone has a named human**, including the ones with `[auto]` inputs — an automatic input still needs someone accountable for using it.

**The calendar runs backwards from the filing deadline**, which follows from filer status. That makes filer status the first thing to establish and the easiest to assume — a company that crossed the large-accelerated threshold last year has a shorter deadline than the calendar it used before.

**`[auto]` contribution to the calendar itself**: the close-completeness checks from `month-end-close-checklist` and `quarter-end-close` establish whether Day 0 has actually happened. **A calendar that starts counting from a close that is not finished is already late** and nobody will notice for a week.

---

### Step 2 — Establish tie-out discipline

**The heart of the skill, and each of the five tie-outs has a different shape.** All five preserved.

| Tie-out | Ledger side | Document side | Verdict |
|---|---|---|---|
| **FS statements to TB** | `[auto]` — exact | **`[manual]`** — reading the draft | Split |
| **Footnotes to supporting schedules** | `[auto]` where the schedule is ledger-derived | `[manual]` | Split |
| **MD&A metrics to source data** | `[auto]` for ledger-derived metrics | `[manual]` | Split |
| **Non-GAAP measures to reconciliations** | `[auto]` for the **GAAP starting point** | `[manual]` for the adjustments | Split — see below |
| **Shares and EPS to cap table** | **Nothing. No cap table on this surface.** | `[manual]` | **`[manual]`** |

#### What "the ledger side is automatic" actually buys

It is worth being precise, because it is easy to overstate.

**Mosofin can produce, exactly and traceably, what the books say each tied figure should be** — every balance, every subtotal, every roll-forward, at the reporting date and the comparative date, with the transactions behind them. That is the reference against which the document is checked, and producing it by hand is a large part of what a tie-out costs.

**Mosofin cannot read the draft.** Somebody compares the document against the reference and initials it. That comparison **is** the tie-out.

**So the honest framing: Mosofin builds the tie-out schedule; a person performs the tie-out.** That division should appear on the sheet, so a reviewer knows which column was computed and which was checked.

#### Non-GAAP measures deserve their own note

`[auto]` for the starting point; `[manual]` for the rest — and there is a compliance dimension.

Under **Regulation G** a non-GAAP measure must be reconciled to **the most directly comparable GAAP measure**, and that GAAP measure is a live read. So the top line of every non-GAAP reconciliation is verifiable automatically.

**The adjustments are the exposure.** Each add-back should be traceable to something identifiable in the books — a restructuring charge, an impairment, a specific expense line. `[auto]` to test whether it is: **an adjustment that cannot be traced to a ledger amount is an adjustment nobody can support**, and that is precisely what draws SEC comment.

**Two further checks worth running** `[auto]`:

- **Consistency with the prior period.** A measure defined one way last quarter and another way this quarter, without disclosure of the change, is a problem. Compare the adjustment categories period to period.
- **Recurring "non-recurring" items.** An add-back that appears in eight consecutive quarters is not non-recurring, whatever it is labelled. This is a well-worn area of regulatory comment, and it is arithmetic over the persisted history.

#### And the EPS gap, restated because it matters

**Shares outstanding, weighted average shares, and the dilutive effect of options, warrants and convertibles are not on this surface.** The entire fifth tie-out is `[manual]`, sourced from the cap table and the equity administration system.

Put it on the sheet as **"not verifiable from the ledger — cap table required"**, not as an empty cell.

---

### Step 2b — Check the comparatives against what was filed *(Mosofin addition)*

**`[auto]`, one comparison, and for a filer it can be a disclosure event.**

Read the ledger's current figures for the **prior period** and compare them to the figures **as filed** in the corresponding prior filing.

They should be identical. Where they are not, **somebody has posted into a period that has already been reported to the market**, and this quarter's comparative column will not match the comparative column already on file.

| Finding | Meaning |
|---|---|
| **Identical** | Good. The comparatives will agree. |
| **Differs, immaterial** | Still needs explaining, and still needs a decision about which figure the filing carries. |
| **Differs, material** | **A restatement question**, with all that follows for a filer — non-reliance, amended filings, ICFR implications. |

**Route it to `restatement-and-prior-period-adjustment`**, which treats this as its primary detection and works through the materiality and correction-method analysis properly. **Do not resolve it here** and do not silently adopt whichever figure is more convenient.

**Run this every quarter.** It costs one comparison, and the alternative is discovering the divergence when a reader notices that two filings disagree.

---

### Step 3 — Disclosure checklist

`[manual]` for the drafting; `[auto]` for the figures and for several completeness triggers. All six areas preserved.

| Area | Verdict | Note |
|---|---|---|
| **Significant accounting policy changes** | `[manual]` | `[auto]` for one signal: a transition adjustment posted to opening equity |
| **Revenue, leases, debt, equity** | `[auto]` for the balances and roll-forwards; `[manual]` for the narrative | See `revenue-recognition-asc606`, `lease-accounting-asc842-ifrs16`, `debt-and-covenant-tracking` |
| **Commitments and contingencies** | **`[manual]`** | **Not transactions.** A guarantee, a purchase commitment, a pending claim — none appear in a ledger until they crystallise |
| **Subsequent events** | **`[manual]` for completeness**; `[auto]` for the transactional sweep | See `subsequent-events-asc855` and the treatment in `quarter-end-close`: the ledger sweep finds transactions, and most Type 2 events are not transactions |
| **Related parties** | `[auto]` for the full-population match; `[manual]` for the universe | See `related-party-disclosures-asc850` — and its warning that a name match cannot establish completeness |
| **Segment reporting** | **`[auto]` if segments are a dimension in the book; `[manual]` if not** | Read the dimension list. See `segment-reporting` |

**The pattern across these six is consistent and worth naming**: **the amounts are readable and the completeness is not.** A ledger will tell you the size of every disclosed item; it will never tell you that something disclosable was omitted, because omission leaves no trace. That is what the checklist is for, and why it stays a checklist with human owners.

---

### Step 4 — Drafting workflow

`[manual]` for the workflow. **`[auto]` for one control test that the original implies and does not test.**

All three preserved:

- **Lock numbers before final drafting.** `[manual]` to impose; **`[auto]` to verify** — Step 4b.
- **Version control for drafts.** `[manual]` — the drafts are documents.
- **Reviewer matrix** — accounting, FP&A, legal, IR. `[manual]`

#### Step 4b — Test whether the numbers stayed locked *(Mosofin addition)*

**`[auto]`, one query, and it tests the control rather than assuming it.**

*Lock numbers before final drafting* is a control. Like every control, it can fail — and its failure is silent, because the ledger does not announce that it has moved.

**Read for any entry posted into the reporting period after the lock date.** For each: date posted, amount, account, source, and author where the surface exposes it.

| Finding | Consequence |
|---|---|
| **Nothing posted after the lock** | The control held. The draft still agrees with the books. |
| **Entries posted, netting to nil in the period** | A reclassification. **Totals unchanged, but a line item in the draft may now be wrong** — check by line, not by total. |
| **Entries posted that change reported figures** | **The draft no longer agrees with the ledger.** Every tie-out performed before the posting is stale, and the affected ones must be re-performed. |

**Why this is worth running on every filing.** The drafting window is exactly when a late adjustment is most likely — the auditors raise a point, a reconciliation resolves, an accrual is refined — and it is also exactly when the document has stopped being regenerated from the system. **The failure mode is a filed document that disagrees with the books it came from**, and nobody discovers it until someone reconciles the two, which may be a quarter later.

Report it factually with dates and amounts. **As with `restatement-and-prior-period-adjustment`: the overwhelming majority of these are somebody doing correct accounting during a window when the document had already been frozen. That is a process finding, not misconduct.**

---

### Step 5 — Controls and sign-offs

**All three preserved. All three `[manual]`, and none should be dressed otherwise.**

| Item | Verdict | Note |
|---|---|---|
| **DCP certifications** | `[manual]` | Officers certifying, personally, with statutory consequences. Not a machine's act in any sense. |
| **SOX controls evidence** | `[manual]` | See `sox-controls-design-and-testing`. A control test examines whether a control *operated*, which is generally evidence of human action. |
| **Final read-through for consistency** | `[manual]` | Reading the whole document for internal consistency — a number in the MD&A that contradicts the same number in a footnote. |

**One narrow `[auto]` contribution, described accurately**: for controls whose operation leaves a trace in the ledger, the trace is readable — whether entries above a threshold carry an approver where the system records one, whether expected reconciliations produced entries, whether anything was posted into a closed period (Step 4b).

That is **population evidence about some controls, and it is not a control test.** `internal-audit-workpaper` works through the distinction properly and it holds here.

**On the final read-through**: `[auto]` can compare **figures** appearing in more than one place *where both are ledger-derived*. It cannot read the document, so it cannot perform the read-through. The consistency risk in a filing is largely between **prose and figures** — a narrative saying "revenue grew modestly" beside a table showing 31% — and prose is exactly what is not on this surface. See `management-discussion-and-analysis`.

---

## Outputs

All five of the original's outputs preserved, plus two Mosofin additions. Delivered as an `.xlsx` workpaper.

**Sheet 1: Reporting Calendar with Owners**
| Milestone | Owner | Due | Status | Verdict | Dependency |

**Every milestone has a named human**, including automatic ones. **Filer status and the deadline it drives are stated at the head.**

**Sheet 2: Tie-Out Checklist**
| Tie-out | Ledger reference (computed) | Document figure | Agreed? | By whom | Date | Basis |

**Mosofin fills the "Ledger reference" column and leaves the rest.** Header states plainly: **Mosofin builds the schedule; a person performs the tie-out.** The EPS row carries **"not verifiable from the ledger — cap table required."**

**Sheet 3: Disclosure Checklist**
The six areas, each with owner and status. **Amounts pre-populated where ledger-derived; completeness marked as the owner's responsibility.**

**Sheet 4: Drafting / Review Workflow SOP**
Version control, reviewer matrix, lock date. `[manual]`.

**Sheet 5: Risk List and Mitigation Plan**
`[manual]` for the risks; `[auto]` for the ones the ledger surfaces — see Sheet 6.

**Sheet 6: Ledger Control Tests** *(Mosofin addition)*
| Test | Finding | Evidence | Amount | Periods | Action |
|---|---|---|---|---|---|

The comparatives check (Step 2b). The numbers-lock test (Step 4b). Non-GAAP adjustments not traceable to the ledger. Recurring "non-recurring" items. Non-GAAP definitions inconsistent with the prior period.

**Sheet 7: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `SEC_Filing_Prep_[YYYY-Q#]_[EntityName].xlsx`

Registrant `display_name` in the file name and on every sheet, **and a statement of whether the figures are consolidated or component-level.** If any read returned `mock: true`, say so in the file name and at the head of Sheet 2.

---

## Output Quality Standards

*(A Mosofin addition — the original has no Output Quality Standards section.)*

- **Filer status established and the calendar built backwards from the resulting deadline.**
- **Every calendar milestone has a named owner**, including those with automatic inputs.
- **Consolidated versus component basis is stated** on every sheet carrying figures.
- **Every tie-out shows which side was computed and who performed the comparison.**
- **The EPS and shares tie-out is marked as requiring the cap table**, not left blank.
- **Non-GAAP measures reconcile to the most directly comparable GAAP measure**, with every adjustment traceable to a ledger amount or explained.
- **Non-GAAP definitions are consistent with the prior period**, or the change is disclosed.
- **"Non-recurring" items recurring across periods are flagged.**
- **The comparatives are checked against what was actually filed**, every quarter.
- **The numbers-lock control is tested, not assumed** — and affected tie-outs re-performed where it failed.
- **Disclosure completeness is owned by a person**, since omission leaves no ledger trace.
- **Auditor review is recorded as mandatory and not substitutable.**
- **Nothing is presented as drafted, certified, tagged or filed by Mosofin.**
- **File naming consistent.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and filer status**, which is re-tested annually and drives every deadline.

**What is worth persisting into the workspace-scoped skill:**

1. **The calendar template with owners**, which is stable quarter to quarter and expensive to rebuild.
2. **The tie-out schedule definitions** — which ledger figures support which filing line. This is the largest single saving: established once, computed automatically every quarter thereafter.
3. **Non-GAAP definitions and their adjustment categories**, which must be consistent period to period and which the recurring-item test needs a history for.
4. **The filed figures for each period**, so Step 2b's comparison has a baseline that does not require re-reading old filings.
5. **The lock date convention** and the drafting window.
6. **Whether segments, and which dimensions carry them.**
7. **Where the consolidation is performed**, and whether the registrant's file holds the consolidated result.
8. **Findings and resolutions**, so a post-lock posting pattern already explained is not re-raised identically.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed.**

**The evolved version's quarterly job is short and specific**: has anything moved in a reported period, did the numbers stay locked, do the non-GAAP definitions still match last quarter, and here is the tie-out schedule ready to be checked.

---

## Anti-patterns

- **Ticking a tie-out that read the ledger twice.** The document is the other side, and Mosofin cannot read it.
- **Tying out a component and presenting it as the consolidated filing.** It agrees perfectly and proves nothing about the registrant.
- **Leaving the EPS tie-out blank.** Mark it as requiring the cap table; a blank reads as an oversight.
- **Assuming the numbers stayed locked.** Test it. The drafting window is when late adjustments arrive.
- **Adopting whichever prior-period figure is convenient** when the ledger and the last filing disagree.
- **Presenting a non-GAAP adjustment that cannot be traced to a ledger amount.**
- **Labelling an eight-quarter item "non-recurring."**
- **Redefining a non-GAAP measure without disclosing the change.**
- **Treating a ledger subsequent-events sweep as complete.** Most Type 2 events are not transactions.
- **Treating a population read as a control test.**
- **Building the calendar to last year's deadline** after a filer-status change.
- **Counting Day 0 from a close that is not finished.**
- **Using `quarter-end-close` for Q4.** There is no fourth 10-Q.
- **Saying "filed", "certified" or "tagged".** The gateway reads.
