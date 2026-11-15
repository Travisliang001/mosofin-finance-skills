---
name: r-and-d-tax-credit
description: "Supports an R&D tax credit or relief claim: confirms the regime the user states for their jurisdiction, sets out the tests for qualifying activity project by project, draws the boundaries of qualifying cost, computes qualifying expenditure from the books where projects are tracked, computes the benefit on the user's rates, and builds the documentation a claim needs. Reads project and payroll costs through a connected Mosofin workspace when the user agrees, or works from uploaded cost data. Use when the user asks about an R&D tax credit, qualifying research expenditure, what R&D costs can be claimed, or documentation for an R&D claim. Do not use for capitalising development costs in the accounts (use intangibles-and-amortization). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# R&D tax credit: what qualifies, and what it cost

R&D incentives reward work that seeks a real technical advance. A claim has two parts: **which
activities qualify**, a technical judgment project by project, and **what they cost**. This skill
sets out the first for you to decide, computes the second, and builds the documentation.

**Works with or without Mosofin.** With Mosofin connected costs are read by project where projects
are tracked in the books. Without it, you upload the cost data and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** Whether a project qualifies, and how
staff time splits between projects, are never in the books. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system, and files nothing.** Every entry and
  every figure is a proposal.
- **Produces computations and illustrations, not tax advice.** A qualified tax professional
  reviews before anything is filed or acted on.
- **Never supplies a rate, threshold, bracket or rule.** Each comes from the user, with its source
  and its year, and is never carried over from an earlier run.
- **Never decides that an activity qualifies.** It sets out the tests and records the user's
  answer.
- **Never estimates staff time on R&D.** The apportionment comes from the user, with its basis.
- **Never includes a cost on the wrong side of the boundary to enlarge a claim.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–7" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which entity, jurisdiction and tax year?* | Each regime has its own rules | **Ask again.** |
| **C** | *Which regime and scheme apply, and what are the rates, with source and year?* | Never built in | **Blocking.** Assemble costs by project, and compute no benefit. |
| **D** | *What are the projects, with enough technical detail to test them?* | The heart of the claim | List the projects found in the books as candidates only. |
| **E** | *How was staff time split between projects, and on what basis?* | The largest cost and the least visible | Leave staff cost out, and say so. |
| **F** | *Is the company an SME or large, and were there grants or subcontractors?* | Changes the scheme and the boundaries | Ask again for size. Assume no grants, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say whether projects, classes or departments are tracked in the books. That decides how much can
  be read.
- Report costs with no project tag.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Project descriptions** | Required | PDF or text |
| **Costs by project**: staff, materials, subcontractors | Required | XLSX or CSV |
| **Time allocation** by person and project | Required for staff cost | XLSX |
| Regime rules and rates with source | Required | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing the **2025 R&D claim** for **Northbrook Trading**, in **the jurisdiction and scheme
> you named**, with costs by **project** from **your Mosofin connection**. **Three projects**,
> which you judged to qualify. Staff time from **timesheets**. No grants. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the project, the
period and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Confirm the regime

The regime, scheme and rates as supplied: [`references/method.md`](references/method.md) Step 1.

## Stage 4 — Qualifying activity and qualifying cost

The activity tests, the cost boundaries, then qualifying expenditure:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for software development, grants,
subcontractors and staff time.

## Stage 5 — Benefit, documentation, and present

The benefit, the documentation framework, then the output:
[`references/method.md`](references/method.md) Steps 5–7. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the project list and
how costs are tagged. **No rate is saved.**

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
