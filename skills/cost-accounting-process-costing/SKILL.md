---
name: cost-accounting-process-costing
description: "Costs continuous production by department or process: maps the production flow, builds the physical units schedule, computes equivalent units under weighted average or FIFO, the cost per equivalent unit, and the cost assigned to completed units and to work in progress, then reconciles the cost roll-forward to the ledger. Reads departmental costs through a connected Mosofin workspace when the user agrees, or works from uploaded production and cost data. Use when the user asks for process costing, equivalent units, cost per unit in continuous production, a production cost report, or work in progress valuation by department. Do not use for costing discrete jobs (use cost-accounting-job-order) or for standard cost variances (use standard-costing-and-variance-analysis). Read-only: produces the production cost report and proposed entries, and posts nothing."
---

# Process costing: cost per unit in a continuous flow

When thousands of identical units flow through production, the cost of one cannot be tracked. So a
department's cost for the period is divided by the units that effort was equivalent to.
Half-finished units count in part: these are **equivalent units**. This skill builds the
**production cost report** by department.

**Works with or without Mosofin.** With Mosofin connected the costs added by department are read
from the books and the result is reconciled to the work in progress account. Without it, you
upload the cost and production data and the method is the same.

**Costs are in the books. Units are not.** Units started, completed and in progress, and how
complete they are, come from production, counted by people. Every unit and every percentage is
yours to supply. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never infers units or completion from a work in progress balance.**
- **Never picks weighted average or FIFO**, and never changes it between periods without saying
  so.
- **Never lets the model agree with itself and not with the ledger.** The roll-forward is tied to
  the books.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–8" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period?* | Sets every read | **Never default the period.** |
| **C** | *What are the departments or processes, in order, and how are they tagged in the books?* | Costs are split by that tag | **Ask again.** |
| **D** | *What are the units: opening work in progress, started, completed, closing, and how complete?* | Production data, never in the books | **Blocking.** Report cost by department only; compute no unit cost. |
| **E** | *Weighted average or FIFO, and where are materials added: at the start, part way, or evenly?* | Changes the equivalent units | **Ask again.** |
| **F** | *What spoilage or yield is normal?* | Needed to tie units in to units out | Report any unit difference as unexplained. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report costs posted to work in progress with no department tag, and any manual journal into it.
- Record who supplied the unit counts and when the count was taken.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Costs added by department**: materials, labour, overhead | Required | XLSX or CSV |
| **Production report**: units and completion by department | Required | XLSX |
| **Work in progress account detail** for the period | Required for the reconciliation | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Process costing for **Northbrook Trading** for **September**, across **Mixing, Filling and
> Packing**, tagged by **department**, from **your Mosofin connection**. **Weighted average**,
> materials added **at the start**. Units from **the production report you uploaded, counted on 30
> September**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
departments and the totals. Flag anything unreadable straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the costs and map the flow

Pull costs by department and the work in progress account, then map the production flow:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Units, equivalent units and cost per unit

The physical units schedule, equivalent units and the cost per equivalent unit:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for units in and out that disagree, a
method change, materials timing, and transfers between departments above cost.

## Stage 5 — Assign costs, reconcile, and present

Costs assigned to output, the roll-forward reconciled to the ledger, the postings as
**proposals**, then the outputs: [`references/method.md`](references/method.md) Steps 5–7 and
*Outputs*. Before presenting, check it against [`references/output.md`](references/output.md). Ask
whether the user wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the production flow, the department
tag, the method and the point at which materials are added.

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
| [`references/tools-and-glossary.md`](references/tools-and-glossary.md) | When you need a tool name or a term |
