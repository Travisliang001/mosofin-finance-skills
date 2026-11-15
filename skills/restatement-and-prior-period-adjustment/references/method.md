<!-- restatement-and-prior-period-adjustment · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 0 — Sweep for prior-period postings *(Mosofin addition)*
- Step 1 — Confirm it is an error, and not a change in estimate
- Step 2 — Quantify the error across all affected periods
- Step 3 — Assess materiality
- Step 4 — Determine the correction method
- Step 5 — Compute the corrections
- Step 6 — Prepare disclosures
- Step 7 — Address the control and governance implications
- Step 8 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal**, and in this skill that word carries more weight than usual. The gateway is read-only. **Mosofin restates nothing, concludes nothing on materiality, determines no correction method, makes no non-reliance determination, and files nothing.** It computes, it evidences, and it hands the result to the people whose decision it is.

---

## Inputs

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Description of the error** | What was misstated, and how it was discovered | **Required** | Not in the books | `[manual]` |
| **Affected periods** | Which previously-issued periods | **Required** | Not in the books; **the prior-period sweep may suggest additional ones** | `[manual]`, `[auto]` in part |
| **Quantification of the error** | Amount by period and line | **Required** | **Live read** once the error is identified — see Step 2 | `[auto]` |
| **Previously-issued financial statements** | The statements containing the error | **Required** | **Not in the books. From the documents.** The ledger's current view of a prior period is not what was issued. | `[manual]` |
| **Reporting framework** | US GAAP / IFRS | **Required** | Not in the books | `[manual]` |
| **Entity profile** | Public or private | **Required** | Not in the books | `[manual]` |
| Cause of the error | Root cause | Recommended | **Partly evidenced** — the entry's source, date and author where the surface exposes them | `[manual]`, `[auto]` in part |
| Tax effect information | For the tax impact | Recommended | Current and deferred tax balances readable; **the return position is not** | `[auto]` in part |

---

## Workflow

### Step 0 — Sweep for prior-period postings *(Mosofin addition)*

`[auto]`. One query, run before anything else, whether or not an error has already been identified.

**Read every entry posted into a previously-reported period after that period's reporting date.** For each: date posted, period affected, amount, account, source, and author where available.

Then compare the **current ledger trial balance for each closed period** against the **figures in the issued statements** for the same period. Any difference is a period whose books have moved since the statements went out.

**What comes back falls into four groups**, and they need different handling:

| Finding | What it means | Next |
|---|---|---|
| **Nothing** | The books still agree with what was issued. | Proceed to Step 1 with the error the user identified. |
| **Entries posted in the ordinary close cycle**, before the statements were finalised | Not a divergence at all — normal close activity dated into the period. | Exclude, and say you did. |
| **Entries posted after issuance that net to nil in the period** | A reclassification. May still misstate a line item even where the totals are unchanged. | Assess by line, not only by total. |
| **Entries posted after issuance that change the reported result or position** | **A correction that was made without being assessed.** The books are one thing and the filing is another. | **This is the finding.** Take it into Step 1. |

**The fourth group is the reason this step exists.** It is a restatement that has already occurred in substance: an error was found, quietly fixed in the ledger, and never assessed for materiality, never disclosed, never put to the auditors. Every comparative published since then has come from books that no longer match the filing.

**Report it as an observation with figures, dates and sources. Never as an allegation about a person.** The overwhelming majority of these are somebody trying to make the books right, doing the bookkeeping correctly and the governance not at all. That is a process finding and it is what Step 7 is for.

**And two cautions on the sweep itself.** Where the accounting system permits period locking, entries may have been posted before a lock and are not divergences — check the lock dates rather than assuming. And **the sweep finds changes, not errors**: an entry posted into a prior period may be a perfectly proper adjustment agreed with the auditors and reflected in the issued statements. Compare against the statements, not against an assumption.

---

### Step 1 — Confirm it is an error, and not a change in estimate

**`[manual]`. This is the threshold question and the ledger cannot answer it.**

All three categories preserved:

| Category | Definition | Treatment | Verdict |
|---|---|---|---|
| **Error** | A misstatement from a mathematical mistake, misapplication of GAAP or IFRS, oversight, misuse of facts **that existed**, or fraud — something that was *wrong given what was known*. | **Restatement — retrospective** | `[manual]` |
| **Change in estimate** | A revision based on **new** information or developments — updating a useful life, an allowance. | **Prospective. NOT a restatement.** | `[manual]` |
| **Change in accounting policy** (voluntary) | Applied **retrospectively**, but it is a policy change and not an error. | Retrospective, disclosed as a policy change | `[manual]` |

> **Misclassifying a change in estimate as an error, or the reverse, is itself wrong. Confirm the item is genuinely an error before proceeding. Document the basis.**

Preserved with emphasis, and here is why no amount of live data helps:

**The distinction turns on what was known at the time, not on what the numbers were.** An allowance that proved too low is a change in estimate if the information arrived later, and an error if the information was on the file and was overlooked. **The amounts are identical in both cases.** The ledger shows an adjustment; it does not show whether the facts behind it existed and were available a year ago.

That is a question about knowledge, and knowledge is not a field. Ask, document, and be able to defend the answer — because the treatments diverge completely from this point and an auditor will test this determination first.

**One `[auto]` contribution, and it is evidentiary rather than conclusive:** where the surface exposes an entry's **source, posting date and author**, that context supports the enquiry. An adjustment posted by the same person who prepared the original, two days after a query from the auditors, is a different conversation from one arising in a routine review. **It is context for a human judgment, never a substitute for it.**

---

### Step 2 — Quantify the error across all affected periods

**`[auto]`, and this is the largest block of automatic work in the skill.** Once the error is defined, its effect is arithmetic on live data.

All five elements preserved:

| Element | Verdict |
|---|---|
| The misstatement amount in **each affected period** — income statement and balance sheet | `[auto]` |
| The **cumulative effect on retained earnings** as of the beginning of the earliest period presented | `[auto]` |
| Effects on **each affected line item, subtotal and per-share amount** | `[auto]` for line items and subtotals; **`[manual]` for per-share** — share counts are not on this surface |
| The **income tax effect** of the correction | `[auto]` for the gross effect and the current tax balances; **`[manual]` for the return position and any amended return.** See the tax provision work |
| Effects that **reverse over time versus permanent** | `[auto]` to model; `[manual]` to conclude |

> **Both the "rollover" (income-statement) and "iron curtain" (balance-sheet) views of the error matter for the materiality assessment.**

Preserved, and **both are `[auto]`** — which matters, because in manual practice one of the two frequently gets skipped and it is generally the one that would have given the awkward answer.

- **Rollover** looks at the error originating in each period: how much did *this year's* income statement get wrong?
- **Iron curtain** looks at the accumulated error sitting on the balance sheet at the period end: how wrong is the balance sheet *now*, including errors that originated earlier?

They give different numbers, and an error can be immaterial under one and material under the other. Computing both is arithmetic, so **compute both, present both, and never present only the smaller one.**

**On per-share amounts, which are a genuine gap.** Weighted average shares outstanding are not in a general ledger — there is no cap table on this surface, consistently with the equity compensation accounting, `financial-statement-builder` and an IPO readiness review. Per-share effects are a **required** disclosure under Step 6 for entities that report EPS, so the share counts must be supplied. Ask for them early; the disclosure cannot be completed without them.

---

### Step 3 — Assess materiality

Materiality determines the correction method. Evaluate **quantitatively AND qualitatively** — a **SAB 99-style analysis** for US public companies, analogous judgment otherwise.

**This is the step where the split has to be drawn most carefully**, because more of it is computable than the usual reflex suggests — and the conclusion is still not Mosofin's to reach.

**Quantitative** — `[auto]`, in full.

The size of the error against the relevant benchmarks — net income, revenue, equity, total assets — **in each affected period, under both rollover and iron-curtain methods.** Every benchmark is a live read; every ratio is arithmetic. Present the full matrix: benchmark × period × method. In manual practice this table is usually partial, and it is partial in a direction.

**Qualitative** — and here the original lists seven factors. **Four of them are partly computable, which is a better result than "qualitative means manual" would suggest.** All seven preserved:

| Qualitative factor | Verdict | What Mosofin can actually do |
|---|---|---|
| **Does it change a loss to a profit, or the reverse?** | **`[auto]`** | Pure arithmetic: reported result versus corrected result, checking for a sign change. **This factor is the classic example of a small error being material, and it is fully computable.** |
| **Does it affect compliance with debt covenants or regulatory requirements?** | **`[auto]` given the definitions** | Recompute each covenant on corrected figures and compare to the threshold. **The covenant definitions come from the credit agreement, not the ledger** — see `quarter-end-close` and `debt-and-covenant-tracking`. Given them, this is arithmetic, and a correction that breaches a covenant is material almost regardless of size. |
| **Does it affect a trend, a segment, or a key metric?** | **`[auto]` in part** | Restate the trend and show it beside the reported one. Segment effects are `[auto]` where segments are a dimension in the book, `[manual]` where they are not. Which metrics matter is `[manual]`. |
| **Does it mask a change in earnings?** | **`[auto]` in part** | Compute the earnings trajectory with and without the error. Whether the difference constitutes masking is judgment. |
| **Does it affect management compensation?** | `[manual]` | Compensation plans and their triggers are not in a general ledger. |
| **Does it arise from fraud or an illegal act?** | `[manual]` | See `fraud-detection-and-forensics`, and note the heightened obligations. |
| **Would it influence a reasonable user's decision?** | `[manual]` | **This is the actual test.** The six factors above are indicators of it; this one is the question they are all evidence for, and it is a judgment about people. |

> **Conclude on materiality to each affected period. This is judgmental and must involve management, auditors, and (public companies) governance.**

**This sentence is the boundary of the skill and it is preserved without qualification.**

**Mosofin computes every indicator and concludes nothing.** The distinction is not procedural pedantry. Materiality is a judgment the framework deliberately assigns to particular people, and for a public company the conclusion has regulatory consequences that follow automatically from it. A tool that fills in the conclusion column has not saved anyone time — it has produced a document that looks like a governance decision and is not one, which is worse than an empty column.

So: **Sheet 3 has a Conclusion column and Mosofin leaves it blank.** The indicators beside it are complete, computed, and both-methods. The judgment is signed by someone.

---

### Step 4 — Determine the correction method

`[auto]` to model the consequences of each path. **`[manual]` to choose one.**

All three methods preserved, with the two sub-cases intact.

**Material to prior periods → Restatement ("Big R")**
- Restate the previously-issued statements, retrospectively — `[auto]` to compute
- Correct each affected prior period presented — `[auto]`
- **Adjust the opening balance of retained earnings** for the earliest period presented, for the cumulative effect of periods before that — `[auto]`
- **For US public companies**: typically a **non-reliance determination** on the prior statements (an Item 4.02-type disclosure), amended filings, and ICFR implications — **likely a material weakness** — **`[manual]`, all of it, with legal and regulatory advisors**

**Immaterial to prior periods, correcting in the current period — two sub-cases:**

- If the cumulative correction would be **material to the current period** if recorded now → **still restate the immaterial prior periods ("Little r")**, to avoid a material current-period hit. `[auto]` to detect that this is the case; `[manual]` to conclude.
- If immaterial to **all** periods → an **out-of-period adjustment** in the current period, no restatement, **with consideration of disclosure.** `[auto]` to compute; `[manual]` to conclude.

> **Document the determination and its basis.**

**The Little r case deserves the emphasis the original's edge case gives it, because it is genuinely counter-intuitive and commonly got wrong.** Each prior period's error was immaterial. Nobody would restate any of them individually. But correcting the accumulated total in the current period would produce a material hit to *this* period — so the answer is to restate the immaterial prior periods after all.

The test is arithmetic and it is `[auto]`: **accumulate the error across all prior periods, compare that total against the current period's benchmarks, and report whether it clears them.** In manual practice this comparison is frequently not made — each year is looked at, found small, and dismissed — which is exactly how a Little r case gets mishandled into an out-of-period adjustment.

**And the aggregation point from the edge cases belongs here too** `[auto]`: **where several errors exist, assess them aggregated as well as individually.** Several immaterial errors can aggregate to material, and a tool should do this arithmetic because people reliably do not.

---

### Step 5 — Compute the corrections

`[auto]` to compute. `[manual]` to post — and in this skill, `[manual]` to post *after an auditor has been involved*.

All five preserved:

- **Build the correction entries** — `[auto]` to draft; hand off to `journal-entry-builder`
- **For restatement**: restate each affected prior-period statement; adjust opening retained earnings for pre-presented-period effects — `[auto]`
- **For an out-of-period adjustment**: record the catch-up in the current period — `[auto]` to draft
- **Include the tax effect** — `[auto]` for the computation, `[manual]` for the return consequences
- **Ensure the corrected statements balance and tie across** (`financial-statement-builder`) — `[auto]`, **with the caveat below**

#### The tie-out proves less than it appears to

Carrying forward the caution from `financial-statement-builder`, because it applies with full force here:

**A restated balance sheet built from a corrected ledger will balance.** It will balance whether the correction is right or wrong, complete or partial, correctly classified or not — because double entry makes it balance. The tie-out demonstrates that the entries were entered as entries. **It is not evidence that the restatement is correct**, and on a document this consequential a green tick in the wrong place is actively dangerous.

The tests that mean something are the ones that reach outside the arithmetic:

- Does the **cumulative effect on opening retained earnings** equal the sum of the per-period effects for periods before the earliest presented? `[auto]`, and it is a genuine cross-check because the two are computed independently.
- Do the **restated comparatives** tie to what will be presented in the next period's statements? `[auto]`, and see the edge case on carrying comparatives forward.
- Does the **restated figure for each affected line** reconcile to the issued figure plus the identified error, line by line? `[auto]`, and this is the one that catches an error that was quantified in total but misallocated across lines.

---

### Step 6 — Prepare disclosures

`[auto]` to assemble the figures. **`[manual]` to draft, approve and issue.**

Restatement disclosure under ASC 250 / IAS 8. All four elements preserved:

| Element | Verdict |
|---|---|
| **The nature of the error** | `[manual]` — a description, and a carefully-worded one |
| **The effect on each affected line item and per-share amount, for each period presented** | `[auto]` for line items; **`[manual]` for per-share** (no share counts on this surface) |
| **The cumulative effect on retained earnings (or other equity) at the beginning of the earliest period** | `[auto]` |
| **That previously-issued statements have been restated** | `[manual]` — a statement made by the entity |

Coordinate with `notes-to-financial-statements`.

**For public companies, additional regulatory disclosures apply — flag for legal and regulatory advisors.** `[manual]`, and flagged **at the start of the engagement rather than at the end**, because the regulatory timetable for a non-reliance determination can begin running from the moment the conclusion is reached.

---

### Step 7 — Address the control and governance implications

**All four preserved, and all four are `[manual]` in their essentials.** This step is where a tool must be most careful not to appear to have done the work.

| Item | Verdict | Note |
|---|---|---|
| **A material error usually indicates a control deficiency — assess whether it is a material weakness** | `[manual]` | See `sox-controls-design-and-testing`. A control assessment is about whether a control operated, which is generally evidence of human action. |
| **Determine the root cause and remediation** | `[manual]`, `[auto]` in part | The entry's source, date and author give context. **Root cause is why it happened**, and that is established by talking to people. |
| **Governance (audit committee or board) involvement is required for material restatements** | `[manual]` | A meeting. |
| **For public companies, consider clawback and compensation-recovery rules where applicable — flag for legal** | `[manual]` | Compensation arrangements are not in the ledger, and the rules are legal ones. |

**The `[auto]` contribution here is narrow and genuine:** where Step 0's sweep found prior-period postings, **the pattern across them is itself control evidence.** One entry into a closed period is an incident. **Fourteen entries into closed periods across three years, from four different people, is a control that does not exist** — nothing is preventing posting into reported periods, and nobody is reviewing what does.

That is a population observation about what the data shows, presented with counts and dates. **It is not a control test** — see `internal-audit-workpaper` — and it is not a conclusion about a material weakness. It is a fact that the people making that conclusion will want in front of them.

---

### Step 8 — Output

An `.xlsx` workpaper. All eight of the original's sheets, plus two additions.

**Sheet 1: Error Assessment**
Description, error versus estimate versus policy determination, cause, affected periods. **`[manual]` for the determination** — the column exists and Mosofin does not fill it. Header carries the fixture flag and the reads timestamp.

**Sheet 2: Quantification**
Effect by period and line, **under both rollover and iron curtain**, tax effect, cumulative retained earnings effect. `[auto]`. **Per-share row marked as requiring share counts.**

**Sheet 3: Materiality Analysis**
Quantitative benchmarks and qualitative factors, per period — **SAB 99-style** where applicable.

**The layout matters here.** Every indicator is computed and filled. **The Conclusion column is blank and labelled "management / auditors / governance."** A reader must be able to see instantly which cells are arithmetic and which are judgment — and that the judgment has not been pre-empted.

**Sheet 4: Correction Method Determination**
Big R / Little r / out-of-period, with rationale. `[auto]` for the **Little r test** — the accumulated error against current-period benchmarks — and for the aggregation of multiple errors. `[manual]` for the determination.

**Sheet 5: Correction Entries**
The entries and the restated figures. Marked **PROPOSED — NOT POSTED — AUDITOR INVOLVEMENT REQUIRED.**

**Sheet 6: Restated Statements**
Corrected statements, tied out — **with the tie-out caveat from Step 5 printed on the sheet**, so nobody reads a balancing balance sheet as a verified one.

**Sheet 7: Disclosure Draft**
Nature and effect. Marked **DRAFT**.

**Sheet 8: Control / Governance / Regulatory**
Deficiency assessment, remediation, items for auditors, governance and legal. Every row has a named human owner.

**Sheet 9: Prior-Period Posting Sweep** *(Mosofin addition)*
The output of Step 0:

| Entry date | Period affected | Account | Amount | Source | Author | Group | Assessed? |
|---|---|---|---|---|---|---|---|

Plus the per-period comparison of current ledger against issued statements. **This sheet frequently starts the engagement rather than concluding it.**

**Sheet 10: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Restatement_[YYYY]_[EntityName].xlsx`

Entity `display_name` in the file name and on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All ten preserved, with verdicts.

- **Item confirmed as an error (versus an estimate change or policy change) with a documented basis.** `[manual]`
- **Error quantified across all affected periods, rollover and iron curtain, with the tax effect.** `[auto]` — **both methods, always both.**
- **Materiality assessed quantitatively and qualitatively (SAB 99-style), concluded per period.** `[auto]` for the indicators; **`[manual]` for the conclusion, which involves management, auditors and governance.**
- **Correction method determined and justified.** `[auto]` for the Little r test and the aggregation; `[manual]` to determine.
- **Corrections computed; restated statements balance and tie across.** `[auto]` — **and the tie-out caveat is printed on the sheet**, because balancing is not correctness.
- **Opening retained earnings adjusted for the pre-presented-period cumulative effect.** `[auto]`, cross-checked against the sum of per-period effects.
- **Disclosure drafted — nature and per-line effect.** `[auto]` for the figures; `[manual]` for the wording and the per-share amounts.
- **Control deficiency / material weakness assessed; root cause and remediation.** `[manual]`, with the sweep pattern as supporting evidence.
- **Auditor, governance and (public-company) legal/regulatory involvement flagged as mandatory.** `[auto]` to flag; **and flagged at the start, not the end.**
- **File naming consistent.** `[auto]`

**Four Mosofin additions:**

- **The prior-period sweep is run every time**, whether or not an error has been identified — because it can find one nobody reported.
- **The issued statements are obtained from the documents.** The ledger's current view of a prior period is not what was reported, and treating it as such repeats the error being corrected.
- **The materiality Conclusion column is left blank by Mosofin.** Indicators computed; judgment reserved.
- **Every proposed entry is marked as requiring auditor involvement**, not merely review.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — and **any materiality threshold.** Thresholds are entity-specific, auditor-agreed and revisited annually. Persist where the threshold comes from, never the number.

**What is worth persisting into the workspace-scoped skill:**

1. **The period lock dates and the close calendar**, so the sweep can distinguish ordinary close activity from posting into a reported period. Without this the sweep produces noise.
2. **The issued-statement baseline per period** — which document, its date, its key figures. This is what makes next year's sweep a comparison rather than an investigation.
3. **The benchmarks and thresholds** agreed with the auditors, and where they came from.
4. **Covenant definitions**, shared with `quarter-end-close` and `debt-and-covenant-tracking` — expensive to obtain, stable, and needed for one of the qualitative factors.
5. **Share counts by period**, for the per-share disclosure.
6. **Prior-period postings already assessed and cleared**, with the reason — so they are not re-raised every quarter.
7. **Any restatement already made**, with its comparatives, so the carry-forward check in the edge cases has something to check against.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and a prior restatement is among the most sensitive facts a client has.

**The evolved version's routine job is the sweep**, run every period, answering one question cheaply: *has anything in a reported period changed since we reported it?* Most periods the answer is no, and the no is worth having.

---

## Anti-patterns

- **Reading a prior-period trial balance and calling it "what we reported."** If anyone posted into that period, it is not. Get the statements.
- **Skipping the sweep because an error was already identified.** There may be others, already corrected, already undisclosed.
- **Filling in the materiality conclusion.** Compute every indicator; conclude nothing. The framework assigns that judgment to named people.
- **Presenting only the rollover view**, or only the iron curtain. Both, always, and never only the smaller.
- **Dismissing several small errors one at a time.** Aggregate them; that is what the standard asks.
- **Missing the Little r case** by looking at each prior year, finding it immaterial, and taking the hit in the current period.
- **Treating a balancing restated balance sheet as a verified one.** Double entry guarantees the balance.
- **Calling something an error because the outcome was wrong.** What mattered was what was known.
- **Calling something an estimate change because that is the easier treatment.** The determination is testable and an auditor will test it first.
- **Reporting a prior-period posting as misconduct.** Nearly always it is correct bookkeeping and absent governance. Report the pattern with figures.
- **Producing a complete-looking pack that implies the work is done.** On audited statements it cannot start without the auditor.
- **Flagging the regulatory consequences at the end.** Timetables start when the conclusion is reached.
- **Restating and then not carrying the corrected comparatives forward.** That creates a second inconsistency on top of the first.
- **Saying "restated" or "filed".** The gateway reads.
