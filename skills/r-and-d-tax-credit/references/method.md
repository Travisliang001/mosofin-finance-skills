<!-- r-and-d-tax-credit · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Confirm the jurisdiction's R&D regime
- Step 2 — Assess qualifying activities (the technical test)
- Step 3 — Identify the boundaries of qualifying activity
- Step 4 — Compute qualifying expenditure
- Step 5 — Compute the benefit
- Step 6 — Documentation framework
- Step 7 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. Mosofin computes and documents; it does not file, and it does not decide that a project qualifies.

---

## Inputs

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| Jurisdiction and tax year | Country, year | **Required** | Not in the books | `[manual]` |
| Project descriptions | What was developed, with technical detail | **Required** | **Not in the books.** A project *code* may exist; a technical narrative never does. | `[manual]` |
| Cost data | Staff, contractors, materials, software, by project | **Required** | **Live read** — by project where projects are a dimension; by account and vendor regardless | `[auto]` |
| Time/effort allocation | Who worked on what, how much | **Required for staff costs** | **Not in the books.** A general ledger holds cost, not time. | `[manual]` |
| Current R&D incentive rules | Definitions, qualifying costs, rates | **Required** | Not in the books, and **never carried forward from a prior run** | `[manual]`, current-sourced |
| Entity profile | Size, profit/loss position | **Required** | Turnover, balance sheet total and the profit position are live reads; **headcount and group aggregation usually are not** | `[auto]` in part |
| Grants/subsidies received | May reduce qualifying costs | Recommended | **Live read** — grant receipts are transactions. See Step 4. | `[auto]` |
| Prior R&D claims | For continuity | Recommended | The prior credit or receivable is in the books; **the prior claim file is not** | `[auto]` in part |

---

## Workflow

### Step 1 — Confirm the jurisdiction's R&D regime

`[manual]`, entirely, and the original's insistence on this is preserved word for word in substance.

R&D incentives differ fundamentally between countries — a credit, a super-deduction, a payable cash amount; separate schemes for small and large companies. Confirm:

- The regime name and mechanism for the jurisdiction
- Whether the entity's size or status routes it to a particular scheme
- The current qualifying-cost categories and the current rate or rates
- Whether the benefit is a credit, a deduction or a payable cash amount, and how it interacts with the return

> **Do not assume — confirm current rules.**

**Nothing in this file supplies any of that**, and nothing persisted from a previous run may supply it either. A rate stored in a client profile last year is a rate from last year. Store the *methodology*; re-source the *rules*. This is the distinction Gate 3 draws and it matters most here.

`[auto]`, and the only contribution the workspace makes to this step: **the financial facts that determine scheme routing** — turnover, balance sheet total, and whether the entity is profit- or loss-making in the year. Read them and present them. The routing decision itself is the specialist's.

---

### Step 2 — Assess qualifying activities (the technical test)

**`[manual]`. All of it. Without qualification.**

This is the step that decides whether there is a claim at all, and there is nothing in an accounting system that speaks to it.

Most regimes share a conceptual core: qualifying R&D seeks an **advance in science or technology through the resolution of technical or scientific uncertainty.** For each project:

- **Was a technological or scientific advance sought?** Not merely commercially new — technically new or improved.
- **Was there technological or scientific uncertainty?** A competent professional in the field could not readily deduce the solution.
- **Was there a systematic process** of experimentation or investigation to resolve it?

**Qualifies**: developing new or improved products, processes, materials or software where the outcome was technically uncertain; experimentation; prototyping undertaken to resolve uncertainty.

**Usually does not**: routine development; cosmetic changes; market research; applying existing techniques where nothing was uncertain; work carried out after the uncertainty was resolved.

**Document the technical narrative for each qualifying project** — the advance sought, the uncertainties faced, and how they were addressed. **This narrative is what the tax authority examines.** It is written by people who did the work, or by someone who has interviewed them properly.

**What the workspace can contribute, and what it must not be mistaken for** `[auto]`:

The ledger can produce a **list of cost centres that consumed money** — projects, classes, jobs, departments. That is a useful starting inventory for the interview, because it is complete in a way that memory is not: a project nobody mentioned but which spent 140,000 is worth asking about.

**It is a list of spending, not a list of research.** A project code called `PLATFORM-REWRITE-2024` tells you a budget existed. It does not tell you whether anything about it was technically uncertain, and the temptation to read qualification off a project name is precisely the over-claiming the next step warns against.

---

### Step 3 — Identify the boundaries of qualifying activity

`[manual]` for the boundary. `[auto]` for one useful piece of evidence.

Within a project, **only the work addressing technological uncertainty qualifies.** Identify:

- The **start** of qualifying activity — when the uncertainty and the experimentation began
- The **end** — when the uncertainty was resolved or the advance achieved
- **Qualifying versus non-qualifying sub-activities** within the project

> **This boundary determination is critical and commonly over-claimed. Be disciplined.**

Preserved with emphasis, because the original names it as the most common error and the most common audit trigger, and a live cost feed makes over-claiming easier rather than harder: it is trivially simple to total a whole project and call it qualifying expenditure.

**The one `[auto]` contribution: the project's spend profile over time.**

Read the project's costs by month for its whole life. Then set that curve against the technical narrative's claimed boundary. The pattern is informative:

- Spend that **tails off sharply** around the claimed end of uncertainty is consistent with the narrative.
- Spend that **continues unchanged for many months after** the uncertainty is said to have been resolved suggests either that the boundary is drawn too late — the later spend being routine build-out, not research — or that the narrative's end date is wrong.
- Spend that **starts well before** the claimed start of qualifying activity raises the reverse question.

This is **a question to ask, not a conclusion to draw.** Development spend does not stop when uncertainty is resolved; there is a great deal of ordinary work after the hard part is over, and that is exactly why the boundary exists. The curve tells you where to look. The technical narrative, and the people who wrote it, tell you the answer.

---

### Step 4 — Compute qualifying expenditure

**The heart of the workspace's contribution, and the verdicts vary sharply by category.**

Per the jurisdiction's qualifying-cost categories — **confirm current rules** — commonly including some of the following. All six are preserved:

| Category | Mosofin source | Verdict |
|---|---|---|
| **Staff costs** — salaries and employer costs of employees engaged in qualifying R&D, apportioned by qualifying time | Total payroll cost is readable. **Payroll by employee is often not** — many books carry a summarised journal from a payroll provider. **Time by project is never readable.** | `[auto]` for the pool at best; **`[manual]` for the apportionment** |
| **Contractors / externally provided workers**, often at a restricted percentage | **Vendor bills. Directly readable, by vendor, by project where coded.** | `[auto]` |
| **Subcontracted R&D**, often restricted, with rules on who may claim | Readable as spend; **the entitlement rules are not** | `[auto]` for the cost, `[manual]` for the treatment |
| **Consumables and materials** consumed or transformed in the R&D | Readable where coded to a consumables account or a project | `[auto]` |
| **Software, cloud and data costs**, where the regime allows | **Highly readable** — recurring charges from identifiable providers | `[auto]` |
| **Utilities** related to R&D, in some regimes | Readable as total cost; **the R&D apportionment is not** | `[auto]` for the pool, `[manual]` for the split |

For each project and category the original requires three actions:

- **Gather the cost** — `[auto]` where the category is coded
- **Apportion to qualifying activity** — `[manual]`, and the original is right that staff time especially **needs a defensible basis**: time records, or structured estimates tied to demonstrable project involvement
- **Apply the regime's category restrictions and caps** — `[auto]` arithmetic, once the rules are supplied

#### Staff costs: the largest category and the least visible

This asymmetry deserves its own paragraph because it is where claims are won and lost.

In most R&D claims, **staff costs are the biggest single number.** They are also the number the accounting system knows least about.

**A general ledger holds cost. It does not hold time.** Even where payroll is posted in detail — which is not the norm; see `payroll-journal-entry-builder` and `payroll-reconciliation` — it records that an employee was paid, not what they worked on. The apportionment that turns a payroll cost into a qualifying cost comes from timesheets, from project management systems, or from structured estimates. All three are outside these books.

So **Sheet 4, Staff Time Apportionment, is `[manual]` end to end**, and the workspace's contribution is limited to:

- The **payroll cost pool**, so the apportionment has a correct denominator — `[auto]`
- **Employer costs alongside salary**, so they are not omitted, since most regimes allow them — `[auto]`
- Where payroll *is* posted by department or project, the existing allocation as a **starting point** — `[auto]`, with the caveat that a departmental allocation was made for management reporting and was not made to a tax definition of qualifying activity. It is a hypothesis, not an apportionment.

**Do not manufacture an apportionment percentage.** The original calls pure guesses weak; a guess generated by a tool is not stronger for having been generated by a tool, and it is more dangerous because it arrives looking computed.

#### The completeness contribution, which is where this skill genuinely pays

`[auto]`, and it is worth more than any single category above.

A claim assembled from what the finance team and the engineers remember is **incomplete in one direction and over-inclusive in the other.** A live ledger fixes the first problem properly:

- **Read the full vendor ledger for the year** and surface candidates that look like R&D spend regardless of whether anyone mentioned them — cloud and compute providers, test laboratories, prototype fabricators, specialist engineering contractors, data providers, certification bodies.
- **Read every project or class dimension that consumed cost**, including the ones absent from the claim discussion.
- **Read the software and subscription spend in full.** It is recurring, identifiable, frequently allowable, and routinely forgotten because nobody thinks of a monthly bill as project cost.

Under-claiming is invisible. Nobody audits a claim for the costs it left out, and the client simply receives less than they were entitled to, permanently, with no signal that anything went wrong. **A complete population is the one contribution here that is unambiguously good for the client and requires no judgment to produce.**

The opposite direction needs the same discipline in reverse: a complete population also shows what is being claimed that perhaps should not be. Present the whole population and mark what is in and what is out — never quietly filter.

#### Grants and subsidies

`[auto]` to find, `[manual]` to apply. **This is a strong automatic contribution and it is easy to miss by hand.**

The original notes that grants may reduce qualifying costs, may disqualify a project, or may route it to an entirely different scheme, depending on the jurisdiction — and its edge case says **identify all funding.**

**Grant income is a transaction.** It arrives in the bank, it is posted to a grant income account or to deferred income, and it is readable. So:

- Read for **grant and subsidy receipts** in the period and in prior periods where the project spans years — `[auto]`
- Read for **deferred grant income** on the balance sheet, which is the sign of a grant received for costs not yet incurred — `[auto]`
- Match grant receipts to projects where the coding permits — `[auto]`; ask where it does not

**A missed grant does not make a claim slightly wrong. It can invalidate the treatment of a whole project**, because in several regimes grant-funded work is excluded from the main scheme entirely. Finding one late — after filing — is materially worse than finding it now. This check is one query and it should run on every claim without being asked for. See `grant-accounting-nonprofit-restricted-funds` for the accounting side.

---

### Step 5 — Compute the benefit

`[auto]` for the arithmetic. `[manual]` for the mechanism and the rate, **confirmed currently, every year.**

Apply the jurisdiction's mechanism:

- **Credit** = qualifying expenditure x credit rate, **or**
- **Enhanced deduction** = qualifying expenditure x uplift percentage, reducing taxable income, **or**
- **Payable cash credit** for loss-making entities, where the regime allows losses to be surrendered for cash

**Show how the benefit interacts with the corporate tax computation** — whether it reduces tax, generates a refund, or creates a carryforward. Hand off to `tax-return-prep-corporate`, and see `corporate-tax-provision-asc740` for the accounting consequence, since a credit recognised in the accounts is a provision matter as well as a return matter.

`[auto]` and relevant to the third mechanism: **whether the entity is loss-making, and the size of the loss**, are live reads. For a startup, the payable cash credit is frequently the whole point of the exercise — it is cash rather than a deferred benefit — and the eligibility test usually turns on the loss position. Read it; do not ask for it.

---

### Step 6 — Documentation framework

The support file a claim needs. All four elements preserved.

| Element | Verdict | Note |
|---|---|---|
| **Technical narratives** per project — advance, uncertainty, resolution | `[manual]` | The qualitative support. Written by the people who did the work. This is what gets examined. |
| **Cost analysis** per project and category, with the apportionment basis | `[auto]` to assemble, `[manual]` for the apportionment basis | The quantitative support. **Stamp it with when it was assembled** — see below. |
| **Project records** referenced — design documents, test results, version control, meeting notes | `[manual]` | Demonstrates the systematic process. None of it is in an accounting system. |
| **Methodology note** — how qualifying activities and costs were identified and apportioned | `[auto]` in part | The cost-identification method is describable precisely, because it was a query. **Say so, including the filters used.** The activity-identification method is the user's to describe. |

> **Contemporaneous documentation is far stronger than reconstructed. Flag where records are thin.**

Preserved, and it is the sentence this whole skill turns on. Two rules follow from it, and they are the Mosofin additions to this step:

**1. Date-stamp the assembly.** Every cost schedule carries the date it was produced and the period it covers. A schedule produced during the year, from records maintained at the time, is a different evidential object from one produced two years later from the same ledger — and only the stamp distinguishes them, because they look identical.

**2. State the extraction method precisely.** "Costs coded to project X in the general ledger, extracted [date], filtered to accounts A, B and C" is an honest and reproducible description of a reconstruction. It lets a reviewer — or an inspector — see exactly what was done and repeat it. It is also, quietly, much better evidence than an unexplained total, because it is verifiable.

The methodology note is the one place where being a tool is an advantage rather than a caveat: **a query can be described exactly, and a person's recollection cannot.**

---

### Step 7 — Output

A documentation pack and a workpaper. All preserved, with two additions.

**Document: R&D Claim Report**
Technical narratives and methodology, with the claim summary. Largely `[manual]` content in an `[auto]` structure.

**Workpaper (.xlsx):**

**Sheet 1: Claim Summary**
Qualifying expenditure by project and category, the benefit, and the interaction with the return. `[auto]` for the totals; every rate applied is labelled with its source and the date it was confirmed.

**Sheet 2: Project Qualification Assessment**
| Project | Advance Sought | Uncertainty | Systematic Process | Qualifies? | Boundary (start/end) |

**`[manual]` in every column.** Mosofin may pre-populate the project identifiers from the dimension list, because that is a completeness aid — **and must leave every assessment column empty.** A qualification column filled in by a tool is the most dangerous cell in this workpaper.

**Sheet 3: Cost Analysis**
| Project | Cost Category | Gross Cost | Qualifying % / Apportionment Basis | Restriction/Cap | Qualifying Amount |

`[auto]` for **Gross Cost**; `[manual]` for **Qualifying %**; `[auto]` for the arithmetic once both exist. Add a **Source** column — ledger-read or user-supplied — and an **Assembled on** stamp.

**Sheet 4: Staff Time Apportionment**
By person, project, and qualifying-time basis. **`[manual]`.** The workspace supplies the cost pool and nothing else. If payroll arrives as a summarised journal, say so here — it explains why the sheet starts empty.

**Sheet 5: Benefit Computation**
Mechanism applied, rate, resulting credit, relief or cash. `[auto]` arithmetic; the mechanism and rate carry their source and confirmation date.

**Sheet 6: Documentation Index**
Supporting records per project. `[manual]` — the records are outside. `[auto]` for one column: whether ledger evidence exists for each claimed cost line, which is a genuine part of the index even though it is the smaller part.

**Sheet 7: Open Items / Specialist Review**
Rules confirmed and rules still needed; over-claim risks; items for R&D-specialist sign-off. **Every `[manual]` item in this run appears here.**

**Sheet 8: Cost Population Completeness** *(Mosofin addition)*
The output of the completeness sweep — everything the ledger surfaced, whether or not it made it into the claim:

| Candidate cost | Vendor / account | Project | Amount | In claim? | Reason if excluded |
|---|---|---|---|---|---|

Plus the grant sweep. **This sheet protects the client in both directions** — it is the evidence that the population was complete, and it is the record of what was deliberately left out and why, which is exactly the question an inspector asks.

**Sheet 9: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet. Contents below.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

File naming: `R&D_Claim_[YYYY]_[EntityName]`

The entity `display_name` goes in the file name and on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All ten preserved, each with its verdict.

- **Jurisdiction's specific regime and mechanism confirmed.** `[manual]`, current-sourced this year.
- **Each project assessed against the advance / uncertainty / systematic-process test.** `[manual]`. **Never pre-filled by Mosofin.**
- **Qualifying boundaries within projects identified — no whole-project over-claiming.** `[manual]` to determine; `[auto]` for the spend-profile evidence.
- **Qualifying costs computed by category with defensible apportionment and restrictions applied.** `[auto]` for the costs; `[manual]` for the apportionment; `[auto]` for the restriction arithmetic.
- **Grants and subsidies accounted for.** `[auto]` to find — run it every time, unasked.
- **Benefit computed per the current mechanism and rate, with the tax-return interaction shown.** `[auto]` arithmetic, `[manual]` inputs.
- **Technical narratives and cost support assembled.** `[manual]` and `[auto]` respectively — **and the split is stated, not blurred.**
- **No hardcoded rates, definitions or cost rules — all current-sourced.** `[manual]`. The original's own standard, and it now covers capabilities as well as rates.
- **Over-claim risks and material claims flagged for R&D-specialist review.** `[auto]` to flag; `[manual]` to review.
- **File naming consistent.** `[auto]`

**Three Mosofin additions:**

- **Every cost figure is attributed** — ledger-read or user-supplied — and every rate carries its source and confirmation date.
- **Every assembled schedule is date-stamped and its extraction method described.** A reconstruction is presented as a reconstruction.
- **The cost population is complete before it is filtered.** Sheet 8 shows what was found; the claim shows what was taken; the difference is explained.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed**, and this skill's author already argued the point:

- **Rates, definitions and qualifying-cost rules.** The original says so three times. It is right.
- **The capability map.** The same argument, one layer out. Gate 2 reads it fresh.

Neither belongs in a document that outlives the thing it describes.

**What is worth persisting after the first claim:**

1. **The project structure and dimension mapping** — which projects, which classes, which accounts constitute R&D spend in this book. Rebuilding it every year is the largest avoidable cost in an annual claim.
2. **The apportionment methodology and its basis**, with who agreed it. Consistency year to year is itself evidence of rigour; inconsistency is a question.
3. **The cost-category mapping**: which accounts feed which qualifying category in this chart.
4. **The vendor list that constitutes R&D spend** — the cloud providers, labs and contractors. Next year's completeness sweep starts from a known list rather than a blank page.
5. **Grant history**, since grants often span years and a grant received in year one affects year two.
6. **The prior claim's quantum and treatment**, for continuity and for the year-on-year comparison a reviewer will make.
7. **Whether payroll is posted in detail or as a summarised journal** — it determines how much of Sheet 4 can ever be automated.
8. **Which projects were assessed as non-qualifying, and why.** Re-litigating a settled "no" every year wastes the client's time and risks a different answer for no reason.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and here that includes project names and technical subject matter, which are commercially sensitive in a way an account code is not.

**Never persist a rate.** Persist where to find the rate.

**The evolved version's interview should be about this year's projects and nothing else.** Everything structural should already be known, so that the conversation is spent where it is worth spending: on what was actually uncertain this year.

---

## Anti-patterns

- **Pre-filling the qualification columns.** Sheet 2 is human. A tool marking a project as qualifying is the worst single thing this skill could do.
- **Reading qualification off a project name.** `PLATFORM-REWRITE` is a budget line, not a technical uncertainty.
- **Claiming the whole project** because the total is one click away. Only the uncertain part qualifies.
- **Manufacturing an apportionment percentage.** A guess is not improved by being computed.
- **Treating a departmental payroll allocation as a qualifying-time apportionment.** It was made for management reporting, against a different definition, for a different purpose.
- **Presenting a reconstruction as contemporaneous.** Date-stamp the assembly and describe the extraction.
- **Skipping the grant sweep** because nobody mentioned a grant. It is one query and a missed grant can invalidate a project's treatment.
- **Filtering the population before showing it.** Complete first, then explain the exclusions.
- **Carrying last year's rate forward.** The original forbids it and it is right.
- **Carrying last year's capability map forward.** Same error, different subject.
- **Assuming the entity claiming is the entity that paid.** In a group, it frequently is not.
- **Determining SME status from one company file.** Linked and partner enterprises aggregate, and they are not in the book.
- **Producing a quantum without flagging specialist review** on a material claim.
- **Saying "filed".** The gateway reads.
