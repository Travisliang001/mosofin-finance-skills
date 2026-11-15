---
name: standard-costing-and-variance-analysis
description: "Analyses standard cost variances: checks whether the books run standard costing at all, whether the variance accounts clear, and whether a variance is one-sided every period, then computes price, usage, labour and overhead variances, builds the bridge from standard to actual cost, investigates root causes, and reviews the accounting treatment. Separates a stale standard from a real performance problem. Reads actual costs through a connected Mosofin workspace when the user agrees, or works from uploaded standards and actuals. Use when the user asks for variance analysis on standard costs, purchase price variance, usage or efficiency variance, labour or overhead variance, a cost bridge, or whether standards need resetting. Do not use for variance against the budget (use budget-vs-actual-analysis) or for reconciling inventory to the ledger (use inventory-to-gl-reconciliation). Read-only: produces the variances, the bridge and a coverage sheet, and posts nothing."
---

# Standard costing: is it performance, or a stale standard?

Explains the gap between what production **should have cost** and what it **did cost**. It
computes the variances, bridges standard to actual, and looks for causes. First it asks a prior
question: is the variance measuring performance, or measuring a standard nobody has updated?

**Works with or without Mosofin.** With Mosofin connected it reads the actual side exactly:
purchase prices, labour cost, overhead spend, and the history of every variance account. Without
it, you upload the actuals and the method is the same.

**Every variance has two halves, and the books hold one.** The standard, meaning the bill of
materials, routings, standard prices and rates, lives in a manufacturing system or a spreadsheet,
so you always supply it. **A variance that points the same way every period is not a performance
problem. It is a standard that needs resetting.** Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Any entry is a proposal.
- **Never invents a standard**, and never sets one from recent actuals.
- **Never forces the bridge to tie.** A residual is carried and named.
- **Never blames a person or a supplier for a variance** before the standard's age and the FX
  effect have been checked.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–5" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and which period?* | Sets every read | **Never default the period.** |
| **C** | *Can you supply the standards: bill of materials, routings, standard prices and rates, each with its effective date?* | The standard half is never in the books, and its age matters as much as its value | Run Step 0 only: the health of the variance accounts. Compute no variance. |
| **D** | *What were the production volumes, runs and scrap for the period?* | Usage and efficiency variances need quantities | Compute price and spending variances only, and list the rest as not run. |
| **E** | *Is inventory valued at standard or actual, and what is the policy for capitalising variances?* | It governs the accounting treatment | Report the variances, and list the treatment review as not run. |
| **F** | *Which overhead rates are fixed and which variable, and on what basis are they absorbed?* | Splits the overhead variance | Report overhead as one total variance. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say whether the chart of accounts has variance accounts at all. With none, the books do not run
  standard costing, and the skill says so before going further.
- Say whether the system holds quantities, or values only.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Standards**: bill of materials, routings, prices and rates, with effective dates | Required for any variance | XLSX or CSV |
| **Actual costs** for the period: purchases, labour, overhead | Required | XLSX or CSV |
| **Production data**: volumes, runs, scrap | Required for usage and efficiency variances | XLSX or CSV |
| **Variance account history**, as long as available | Recommended, for the stale-standard test | XLSX or CSV |
| Valuation policy (E), overhead basis (F) | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Analysing standard cost variances for **Northbrook Trading** for **September**, with actuals
> from **your Mosofin connection** and **standards you uploaded, last reset in January last
> year**. Production data supplied. Inventory at **standard**, variances **closed to cost of
> sales**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
item count and the totals. Flag anything unreadable straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Check the health of the standard costing system

Do variance accounts exist, do they clear, and is any variance one-sided:
[`references/method.md`](references/method.md) Step 0. This decides whether the rest applies.

## Stage 4 — Define the standards and compute the variances

Record the standards with their dates, then compute the variances:
[`references/method.md`](references/method.md) Steps 1–2. Check
[`references/edge-cases.md`](references/edge-cases.md) for no quantities in the system, a standard
reset mid-period, freight and duties, purchases and production in different periods, mix against
usage, scrap and multi-currency purchases.

## Stage 5 — Bridge, causes, treatment, and present

The bridge from standard to actual, the root causes, the accounting treatment, then the outputs:
[`references/method.md`](references/method.md) Steps 3–5, *Outputs* and *Quality checks*. Before
presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the standards with
their effective dates, the valuation policy and the overhead basis.

---

## Files

| File | Read when |
|---|---|
| [`references/mosofin-protocol.md`](references/mosofin-protocol.md) | Before the first tool call |
| [`references/gates.md`](references/gates.md) | Stage 2, Mosofin path |
| [`references/method.md`](references/method.md) | Stages 3–6 |
| [`references/edge-cases.md`](references/edge-cases.md) | Stage 4, and whenever something looks unusual |
| [`references/output.md`](references/output.md) | Before presenting |
| [`references/overview.md`](references/overview.md) | Background, or when a user asks why |
