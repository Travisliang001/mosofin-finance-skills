<!-- sox-controls-design-and-testing · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Scope the control environment
- Step 2 — Understand the process (walkthroughs)
- Step 3 — Identify risks (what could go wrong)
- Step 4 — Design / identify controls (the RACM)
- Step 4b — Segregation of duties, tested across the population *(Mosofin addition)*
- Step 5 — Assess control design
- Step 6 — Build test plans (operating effectiveness)
- Step 6b — Which controls can be tested at full population *(Mosofin addition)*
- Step 7 — Execute testing and document results
- Step 8 — Evaluate deficiencies
- Step 9 — Remediation
- Step 10 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is evidence for a human conclusion.** The gateway is read-only. **Mosofin concludes on no deficiency, rates no severity, and certifies nothing.**

---

## Inputs

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Processes in scope** | Revenue, procurement, payroll, close, etc. | **Required** | Not in the books; **the chart shows which processes generate material activity** | `[manual]`, `[auto]` in part |
| **Process descriptions / walkthroughs** | How each process actually works | **Required** | **Not in the books.** A process is people and systems, not postings. | `[manual]` |
| **Risk assessment** | What could go wrong | **Required** | Not in the books | `[manual]` |
| Existing controls | Controls currently in place | Recommended | **Not in the books** — but **whether each leaves a ledger trace is the key routing question** | `[manual]` |
| **Materiality / scoping** | Significant accounts and locations | **Required for scoping** | **Account balances and activity are live reads**; the thresholds are not | `[auto]` in part |
| Systems involved | ERP, sub-systems, IT environment | Recommended | Not in the books | `[manual]` |
| **Testing objective** | Design / operating effectiveness / both | **Required** | Not in the books | `[manual]` |
| Prior deficiencies | For follow-up | Recommended | Not in the books; **persist them** | `[manual]` |

---

## Workflow

### Step 1 — Scope the control environment

`[manual]` for the thresholds and the rationale; **`[auto]` for the quantitative inputs**, which is a genuine saving on an annually repeated exercise.

Determine what is in scope by risk and materiality. All five dimensions preserved:

| Dimension | Mosofin contribution | Verdict |
|---|---|---|
| **Significant accounts and disclosures** (by materiality and risk) | **`[auto]`** — every account balance, its activity volume, its volatility and its trend. **Rank the chart by size and by movement**, which is most of the quantitative side of scoping. | `[auto]` inputs, `[manual]` conclusion |
| **Relevant assertions** for each — **existence, completeness, valuation, rights/obligations, presentation** | Not in the books | `[manual]` |
| **Significant processes** feeding those accounts | `[auto]` in part — **which transaction types actually populate each significant account** is readable, and it maps accounts to processes empirically rather than from an org chart | `[auto]` in part |
| **Significant locations / units** | **`[auto]`** where each is a connected file or a dimension — relative size is directly measurable | `[auto]` inputs |
| **IT systems supporting the processes (ITGCs — foundational)** | **Not in the books at all** | `[manual]` |

> **Scoping focuses effort on what matters to the financial statements. Document the scoping rationale.**

**Two `[auto]` observations worth adding to the scoping discussion:**

- **Accounts that grew materially since last year's scoping** — a scope built once and rolled forward misses the account that has tripled.
- **Accounts populated largely by manual journal entries** rather than by transactional processes. High manual-journal volume is a risk indicator in its own right, and it is a fact about the data. See `journal-entry-review`.

**And the ITGC point from the opening section belongs here operationally**: ITGCs are foundational, they are entirely `[manual]`, and **their effectiveness is a precondition for relying on the automated testing later in this skill.** Scope them first.

---

### Step 2 — Understand the process (walkthroughs)

**`[manual]`.** A walkthrough is a conversation and an observation. Nothing in a ledger describes how work is done.

Document for each in-scope process:

- **The flow from transaction initiation to recording** in the financials
- **Who does what, in which system**
- **Where data enters, transforms and posts**
- **The points where errors or fraud could occur** — the "what could go wrong," WCGW

> **A walkthrough traces one transaction through the whole process to confirm understanding.** Document via narratives and flowcharts.

**`[auto]` for one supporting element, and it is genuinely useful**: **trace the selected transaction through the ledger.** A walkthrough follows one item end to end, and the accounting leg of that journey — the document, its postings, its subsequent settlement, its links — is directly readable. **Pulling the complete transaction trail before the walkthrough meeting makes the meeting shorter and the narrative more accurate**, because the participants are describing something concrete rather than remembering a general practice.

**It does not replace the walkthrough.** The parts that matter most — who reviewed it, what they looked at, what happens when it fails — are precisely the parts the trail does not contain.

---

### Step 3 — Identify risks (what could go wrong)

**`[manual]`.**

For each process and relevant assertion, identify the risks of material misstatement:

- **What could go wrong such that the account or assertion is misstated?**
- e.g. **revenue completeness**: *"shipments occur but aren't invoiced or recorded"*
- e.g. **AP existence**: *"payments made for goods not received"*

**Map each WCGW to the account(s) and assertion(s) it threatens.**

**Both of the original's examples are worth dwelling on, because they illustrate the boundary of this skill precisely.**

Take **"shipments occur but aren't invoiced."** Can a ledger detect this? **Partly, and only from one side.** If shipments are recorded in the system, unshipped-but-uninvoiced items are findable. **If the shipment never entered any system at all, nothing in the ledger knows it happened** — which is the whole difficulty of completeness, and why completeness is the assertion least amenable to data analysis. `internal-audit-workpaper` makes the same point: a full-population ledger test still cannot prove completeness, because completeness is a claim about what is missing.

**"Payments made for goods not received"** is more tractable — it is the three-way match, and both sides are typically in the system. See `three-way-match`.

**So: risks are identified by people, and the ledger can tell you afterwards which ones it would be capable of detecting.** That is worth recording in the RACM, because it determines the test approach.

---

### Step 4 — Design / identify controls (the RACM)

`[manual]` to design; `[auto]` for the SoD analysis and the coverage arithmetic.

For each risk, identify the control(s) addressing it. Build the **Risk and Control Matrix**:

| Process | Risk (WCGW) | Account/Assertion | Control | Control Type | Frequency | Owner | Key? |

**Characterise each control** — all four preserved:

- **Preventive vs. detective**
- **Manual vs. automated** (IT-dependent)
- **Frequency** — per transaction, daily, monthly, quarterly
- **Key vs. non-key** — key controls are those that, alone or with others, **adequately address a material risk**; these get tested

**Type** — all six preserved: **authorisation, reconciliation, review, segregation of duties, physical, IT general or application control.**

**Mosofin addition to the RACM: a ninth column — "Ledger-evidenced?"** For each control, does its operation leave a trace in the accounting data? **That single column routes every control between full-population `[auto]` testing and sampled `[manual]` testing**, and filling it in at design time saves the question being asked again at Step 6.

**Coverage check** `[auto]` for the arithmetic:

> **Every significant risk should have at least one effective control; every key control should map to a real risk. Identify gaps — risks without controls — and redundancies.**

This is a completeness join across the matrix and it is mechanical: risks with no control, controls with no risk, key controls that duplicate one another. **Do it as a query rather than by eye**, because a RACM with 200 rows is exactly where an uncovered risk hides.

---

### Step 4b — Segregation of duties, tested across the population *(Mosofin addition)*

**The strongest `[auto]` in the skill — where the surface exposes user attribution.**

> **Segregation of duties**: ensure incompatible duties — **authorising payments + recording + custody of cash** — are separated. **Flag SoD conflicts.**

**SoD is fundamentally a question about who did what**, and where the accounting system records the actor on each transaction, that question is directly answerable **across every transaction in the period** rather than across a sample.

**Conflicts worth testing** `[auto]`:

| Conflict | Why it matters |
|---|---|
| **Same user created the vendor and approved a bill to it** | The classic fictitious-vendor exposure. See `fraud-detection-and-forensics`. |
| **Same user entered and approved the same transaction** | Self-approval — the most common conflict and the easiest to find. |
| **Same user posted a journal and reviewed it** | See `journal-entry-review`. |
| **Same user handles cash receipts and customer credits** | Lapping exposure. |
| **Same user modifies a master record and transacts against it** | Bank detail changes are the highest-value case. |
| **A single user id appears on every stage of a process** | Not a specific conflict; a structural one. |

#### Why full-population SoD testing is materially better

Manual SoD testing normally takes one of two forms, and both are weak.

**Reviewing the permissions matrix** tells you what people *could* do. It is a design assessment, it is often out of date, and it says nothing about whether anyone actually did.

**Sampling transactions** tells you about the sample. **A conflict that occurred four times in twelve thousand transactions will almost certainly not appear in a sample of forty** — and four self-approved payments is exactly the finding that matters.

**Reading every transaction finds all four.** That is not a faster version of the manual test; it is a different and stronger test.

#### Three things this test cannot do

- **It needs attribution.** Where the surface does not expose who created or approved a record, none of it runs. **Check at Gate 2.**
- **A shared login destroys it.** If several people use one account — common in small teams — the data shows one actor and the analysis is meaningless. **Ask**, because the ledger cannot tell you, and it will silently produce a clean result.
- **It finds conflicts, not intent.** Report the conflict, the count and the amounts. **A conflict in a four-person finance team is a structural fact about the team's size**, not a suspicion about a person — see the edge case on small entities, and say so in the write-up.

---

### Step 5 — Assess control design

**`[manual]`.**

> **Before testing operation, assess whether the control is designed effectively — if it operated as designed, would it prevent or detect the misstatement?**
>
> - **A poorly designed control can't be effective no matter how well it operates**
> - **Identify design deficiencies** — control missing, or design inadequate to address the risk

**Design assessment is a reasoning exercise about a hypothetical**: *would this control, working properly, catch the thing it is aimed at?* There is nothing to read, because the question is not about what happened.

**One `[auto]` contribution that is genuinely a design input**: **the precision of a threshold.** A control described as "the controller reviews all journals over 50,000" has a design property that is measurable — **what proportion of journal value falls below 50,000?** If 94% of the journal value in the period sits under the threshold, the control's design covers 6% of the risk, and that is a design observation supported by a number.

**The same applies to any threshold-based control**: approval limits, review triggers, exception thresholds. **The threshold's coverage is arithmetic, and coverage is a design question.** This is one of the few places where data speaks directly to design rather than operation.

---

### Step 6 — Build test plans (operating effectiveness)

`[auto]` for the sampling arithmetic; **`[manual]` for the method** — with a large exception in Step 6b.

For each key control, design a test. All four elements preserved:

**Test method** — **inquiry, observation, inspection of evidence, re-performance.**

> **Re-performance and inspection are stronger than inquiry alone.**

Preserved and important. The four methods form a hierarchy of strength, and the same hierarchy appears in `internal-audit-workpaper`.

| Method | What it is | Verdict |
|---|---|---|
| **Inquiry** | Asking someone whether the control operates | `[manual]` — **and never sufficient on its own** |
| **Observation** | Watching the control operate | `[manual]` |
| **Inspection of evidence** | Examining the artefact the control produced | `[manual]` where the artefact is a document; **`[auto]` where it is a ledger record** |
| **Re-performance** | Doing the control again and comparing | **`[auto]` where the control is a computation or comparison over ledger data** |

**Re-performance is the strongest method and it is the one a connected ledger is best at.** A reconciliation control can be re-performed exactly. A completeness check can be re-run. A threshold review's population can be reconstructed.

**Sample size** — **based on control frequency and risk; more frequent controls need larger samples.** `[auto]` to compute from the frequency and risk inputs — **and moot for controls tested at full population, see Step 6b.**

**Attributes tested** — **what evidences the control operated**: sign-off, reconciliation completed and reviewed, **exception followed up.** `[manual]` to define. **Note the third attribute** — it is the one that separates a real review from a signature, and Step 6b can test it.

**Period** — **controls must operate throughout the reporting period.** `[auto]` to verify coverage across the whole period rather than a window, which is another place sampling normally compromises.

---

### Step 6b — Which controls can be tested at full population *(Mosofin addition)*

**`[auto]`. The practical heart of the conversion.**

**Not every control. A specific and identifiable set.** Populate the RACM's "Ledger-evidenced?" column using this list.

| Control | What the ledger evidences | Test |
|---|---|---|
| **Approval above a threshold**, where the system records an approver | The approver, on every transaction | **Every transaction over the threshold**, checked for an approver, and for an approver other than the preparer |
| **Segregation of duties** | Who did what | Step 4b, full population |
| **Reconciliation performed** | Whether the reconciling entries exist | **Whether the reconciliation produced entries in every period it should have** — a period with none is a period where it may not have run |
| **Recurring entries ran** | Their presence or absence | Every period. See `recurring-transaction-builder` |
| **Period close / no posting to closed periods** | Postings after the close date | Every entry. |
| **Duplicate payment prevention** | Duplicate vendor, amount, date, reference | Every payment. See `three-way-match` |
| **Master data change control** | Changes to vendor and customer records, where recorded | Every change |
| **Exception follow-up** | Whether flagged exceptions were subsequently corrected | See below — **this is the interesting one** |

#### Testing exception follow-up, which the original identifies as the hard part

The management-review edge case says it exactly: *the rigour of the review, the precision, and the follow-up on exceptions matter. Document the review criteria and evidence of investigation, **not just a sign-off**.*

**`[auto]` can test the follow-up even when it cannot test the review.**

If a control is supposed to identify exceptions and ensure they are investigated and resolved, then **exceptions that persist uncorrected in the ledger are evidence that the follow-up did not happen** — regardless of whether the review was signed.

Concretely: unreconciled items still outstanding months later; flagged variances never adjusted; aged items in a suspense or clearing account that nobody cleared; the same exception recurring period after period.

**This is genuine control-operation evidence, obtained from outcome data**, and it is one of the few places where the outcome legitimately speaks to the operation — because the control's defined output *is* a corrected ledger. **A signed review over a population of uncorrected exceptions is a control that did not operate effectively**, whatever the signature says.

Say it carefully and factually. **It is evidence of an ineffective control, not of a dishonest reviewer**, and the usual cause is a review performed under time pressure against an unrealistic population.

#### And what stays sampled and manual

**Everything whose evidence is a human act recorded outside the accounting system.** Review meetings. Judgment applied to an estimate. Physical controls. Authorisations by email. Anything in a workflow tool the gateway does not reach. Observation of a process.

**That is most management review controls, and it is the majority of the entity-level controls.** No amount of ledger access changes it.

---

### Step 7 — Execute testing and document results

Split, per Step 6b. All four steps preserved.

- **Select the sample** — `[auto]` where the population is being tested in full (no sample required — record that); `[manual]` otherwise
- **Examine evidence that the control operated for each item** — `[auto]` for ledger-evidenced controls; `[manual]` otherwise
- **Document the test, the evidence and the result** (pass / exception) — `[auto]` to produce the schedule; `[manual]` to conclude
- **For exceptions, determine whether it's an isolated instance or a control failure** — **`[manual]`, and it is a judgment**

**Document in test workpapers: control, test performed, sample, results, conclusion.**

**The isolated-versus-failure judgment deserves a note**, because it is where automated testing can mislead in a specific way. **Full-population testing finds more exceptions than sampling does** — that is what it is for. A control tested at full population may show eleven exceptions where a sample of forty showed none, and **eleven exceptions out of twelve thousand is not necessarily a worse control than zero out of forty.** It is a better-measured one.

**So report the exception rate with its denominator, always**, and resist the instinct to treat a newly-visible exception count as a deterioration. The control did not get worse; the test got better. That distinction needs stating explicitly in the first year of full-population testing, or the results will be misread.

---

### Step 8 — Evaluate deficiencies

**`[manual]` for every conclusion. `[auto]` for the quantification.** All three severity levels preserved.

| Level | Definition |
|---|---|
| **Deficiency** | A control **doesn't allow management or employees to prevent or detect misstatements timely** |
| **Significant deficiency** | A deficiency, or combination, **important enough to merit attention by those responsible for oversight** |
| **Material weakness** | A deficiency, or combination, such that there is **a reasonable possibility a material misstatement won't be prevented or detected timely** |

**Evaluate based on** — all three preserved:

- **Likelihood** — reasonable possibility of misstatement — `[manual]`
- **Magnitude** — could the potential misstatement be material? — **`[auto]` to quantify the exposed population**; `[manual]` to conclude
- **Compensating controls** — does another control mitigate? — `[manual]`

> **Aggregate related deficiencies. The conclusion — especially a material weakness — has significant reporting consequences for public companies.**

**`[auto]` for the aggregation arithmetic**, the same discipline a restatement applies to materiality: **individually minor items are dismissed one at a time, and the combination is never computed.** Compute it.

**And the boundary, which is identical to the one in the restatement skill: Mosofin computes the magnitude and concludes nothing.**

Severity rating is a judgment the framework assigns to management and the auditors, and a material weakness conclusion carries disclosure consequences that follow automatically from it. **A tool that fills in the severity column has produced something that looks like a governance decision and is not one.** Leave it blank, with the exposure quantified beside it.

---

### Step 9 — Remediation

`[manual]` for the plan; **`[auto]` for the re-test**, which is where this becomes recurring value.

For each deficiency, all four preserved:

- **Root cause** — `[manual]`, established by talking to people
- **Remediation action** — redesign the control, add a control, fix SoD, improve evidence — `[manual]`
- **Owner and timeline** — `[manual]`
- **Re-testing plan** to confirm the remediated control **operates effectively over a sufficient period** — **`[auto]` for ledger-evidenced controls**

**The re-test is where the connected workspace pays off repeatedly.** A remediated control must be shown to operate over a sufficient period before the deficiency can be closed — which normally means a second round of sample testing, scheduled, staffed and performed months later.

**For a ledger-evidenced control, the re-test is the same query run again.** It can run monthly at no marginal cost, which means remediation can be **monitored continuously** rather than assessed once at year end. A SoD conflict remediated in March can be confirmed clean every month through December, and the evidence for closing the deficiency is a continuous record rather than a sample.

**That is a genuinely better remediation process**, not merely a cheaper one.

---

### Step 10 — Output

An `.xlsx` control package. All eight of the original's sheets, plus two additions.

**Sheet 1: Scoping**
Significant accounts, assertions, processes, locations, systems, with rationale. **`[auto]` quantitative inputs; `[manual]` thresholds.** Add the growth flag and manual-journal-volume observations.

**Sheet 2: Risk and Control Matrix (RACM)**
The full matrix — **with the added "Ledger-evidenced?" column**, and the coverage check run as a query.

**Sheet 3: Process Documentation**
Narratives and walkthrough references. `[manual]`, with transaction trails attached where they support the narrative.

**Sheet 4: Design Assessment**
Design conclusion per key control; design gaps. **Threshold coverage percentages where the control is threshold-based.**

**Sheet 5: Test Plans**
Method, sample size, attributes, period per key control. **Full-population tests marked as such, with "no sample — population tested" in the sample column** rather than a number.

**Sheet 6: Test Results**
Execution, evidence, exceptions, conclusions. **Exception rate with its denominator on every row.** Header carries the first-year caution: a higher exception count from full-population testing is better measurement, not deterioration.

**Sheet 7: Deficiency Evaluation**
Each deficiency, severity, aggregation, conclusion. **Magnitude quantified by Mosofin; the severity column left blank for management and the auditors.** Aggregation computed.

**Sheet 8: Remediation Tracker**
Root cause, action, owner, timeline, re-test status. **Ledger-evidenced controls carry a continuous re-test record rather than a single date.**

**Sheet 9: Full-Population Test Detail** *(Mosofin addition)*
| Control | Population | Tested | Exceptions | Rate | Attribution available? | Notes |
|---|---|---|---|---|---|---|

Every full-population test, with the SoD conflict detail. **Where attribution was unavailable or a shared login is in use, that is recorded here** — it is the reason a test did not run, and it must not look like a clean result.

**Sheet 10: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `SOX_ICFR_[YYYY]_[EntityName].xlsx`

Entity `display_name` on every sheet — controls operate per location. If any read returned `mock: true`, say so in the file name and **on every test conclusion.**

---

## Output Quality Standards

All eleven preserved.

- **Scoping driven by materiality and risk, documented.** `[auto]` inputs, `[manual]` conclusion.
- **Processes understood via walkthroughs; WCGW identified per assertion.** `[manual]`
- **RACM maps every significant risk to a control; key controls designated; SoD assessed.** `[auto]` for the coverage join and **full-population SoD**.
- **Coverage gaps and redundancies identified.** `[auto]`
- **Design assessed before operating-effectiveness testing.** `[manual]`, with threshold coverage as a measured design input.
- **Test plans appropriate to control frequency and risk** — method, sample, period. `[auto]` for sampling arithmetic; **full-population tests marked as needing no sample.**
- **Test results documented with evidence; exceptions evaluated.** `[auto]` for ledger-evidenced controls; **exception rates always with denominators.**
- **Deficiencies evaluated for likelihood and magnitude, aggregated, and severity-rated.** `[auto]` for magnitude and aggregation; **`[manual]` for severity, which Mosofin leaves blank.**
- **Remediation tracked with re-testing.** **`[auto]` continuous re-test for the automated subset.**
- **ITGC and IPE reliance addressed.** `[manual]` for ITGCs — **and the ITGC conclusion governs reliance on every automated test here.**
- **File naming consistent.** `[auto]`

**Five Mosofin additions:**

- **Every control carries a "ledger-evidenced?" determination**, made at design time.
- **Where full population is available, no sample is taken**, and the sheet says so.
- **Attribution availability is recorded** — a test that could not run must never resemble a test that passed.
- **Mosofin's own outputs are treated as IPE**, with queries and parameters recorded so they can be re-performed.
- **The severity column is left for management and the auditors.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and the ITGC conclusion**, which is re-assessed every year and governs everything.

**What is worth persisting into the workspace-scoped skill:**

1. **The RACM**, including the ledger-evidenced determination per control. **This is the single highest-value artefact** — expensive to build, stable between years, and it turns each subsequent year into a re-test rather than a rebuild.
2. **The scoping thresholds and rationale**, so scope changes are visible as changes.
3. **The SoD conflict definitions** for this entity, and **conflicts already accepted with their compensating controls** — so the same structural conflicts in a small team are not re-raised as new findings every year.
4. **Whether attribution is available**, and whether logins are shared.
5. **The full-population test queries and their parameters** — this is what makes them re-performable, and it is required because the outputs are IPE.
6. **Prior deficiencies, their remediation and the re-test record.**
7. **Threshold coverage percentages**, so a threshold that has been eroded by inflation becomes visible.
8. **Exception baselines per control**, so a genuine change in rate is distinguishable from the first year's better measurement.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and SoD data names individuals, which makes this a confidentiality rule and not a tidiness one.

**The evolved version runs the ledger-evidenced controls continuously** — monthly, at no marginal cost — so that year-end is a review of a continuous record rather than a testing exercise. That is the largest structural change this conversion offers, and it only exists once the RACM is persisted.

---

## Anti-patterns

- **Presenting a population read as a control test.** The data shows outcomes; a control test asks whether the control operated.
- **Concluding a control operated because nothing went wrong.** Nothing may have needed catching.
- **Concluding a control failed because something went wrong.** A control can operate and still miss an item.
- **Reading the permissions matrix instead of the transactions.** Could-do is not did.
- **Running SoD analysis over shared logins.** It returns clean and means nothing. Ask first.
- **Treating a sign-off as evidence of a review.** Test the follow-up.
- **Reporting a first-year exception count as deterioration.** The test got better, not the control worse.
- **Reporting exceptions without denominators.**
- **Filling in the severity column.** Quantify the magnitude; leave the rating.
- **Dismissing deficiencies one at a time.** Aggregate them.
- **Relying on automated test evidence without an ITGC conclusion.** The reads inherit the system's integrity.
- **Treating Mosofin's own schedules as exempt from IPE requirements.**
- **Cataloguing every SoD conflict in a four-person team as a failure.** It is residual risk with compensating controls.
- **Sampling a control that can be tested in full.**
- **Letting a "no attribution available" result look like "no exceptions noted."**
- **Saying "certified" or "concluded".** Mosofin evidences; people conclude.
