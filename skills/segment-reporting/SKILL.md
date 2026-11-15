---
name: segment-reporting
description: "Prepares operating segment disclosures under ASC 280 or IFRS 8: identifies operating segments from what the chief operating decision maker actually reviews, applies the aggregation criteria and the quantitative thresholds, settles the measure of segment profit, assembles the segment data, reconciles it to the consolidated totals, and adds the entity-wide disclosures and comparatives. Reads segment dimensions through a connected Mosofin workspace when the user agrees, or works from uploaded segment data. Use when the user asks for segment reporting, reportable segments, the ten percent tests, a segment note, or a reconciliation of segments to the consolidated figures. Do not use for a management dashboard (use kpi-dashboard-builder) or for the notes as a whole (use notes-to-financial-statements). Read-only: produces the segment schedules, the reconciliation and a coverage sheet, and concludes on no judgment."
---

# Segment reporting: the business as management sees it

Segment disclosure shows the business the way its **chief operating decision maker** sees it. This
skill identifies the operating segments, tests which are **reportable**, assembles their figures,
and **reconciles them to the consolidated totals**. Management makes the judgments.

**Works with or without Mosofin.** With Mosofin connected it reads the dimensions in the books,
such as class, department or location, and assembles figures by them. Without it, you upload the
segment data and the method is the same.

**One question decides everything: are the segments a dimension inside the accounting system, or
do they live outside it?** And what counts as a segment is set by what the decision maker reviews,
not by the chart of accounts. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never defines segments from the dimensions in the books alone.** They follow what the decision
  maker reviews.
- **Never discloses more than the decision maker actually sees.**
- **Never forces the reconciliation to agree.** A difference is shown and named.
- **Never decides aggregation or the profit measure for the user.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–9" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and ASC 280 or IFRS 8?* | Sets the scope | **Never default the period.** |
| **C** | *Who is the chief operating decision maker, and which reports do they actually review?* | This defines the segments | **Ask again.** Nothing follows without it. |
| **D** | *How do those reports map to the dimensions in the books?* | Decides whether figures can be read or must be supplied | Show the dimensions found, and ask. |
| **E** | *Which profit measure does the decision maker use, and which other items do they see?* | Only those are disclosed | Assemble revenue by segment only, and say so. |
| **F** | *How are sales between segments priced?* | A policy, not a posting | Show intersegment amounts as recorded, and list the basis as not supplied. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the dimensions in use and how much revenue and cost carries no dimension at all.
- With several company files, say whether segments cross entities.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Segment figures**: revenue, profit measure, assets by segment | Required | XLSX |
| **Consolidated statements** for the period | Required for the reconciliation | XLSX or PDF |
| **The reports the decision maker reviews** | Recommended | PDF |
| Prior year segment note | Recommended, for comparatives | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing segment disclosures for **Northbrook Trading** for the **year to 31 December** under
> **ASC 280**, from **your Mosofin connection**. The decision maker is **the CEO**, who reviews
> results by **three divisions**, which match the **class** dimension. Profit measure: **operating
> profit before central costs**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
segments and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Identify the operating segments

The operating segments under the management approach, then aggregation:
[`references/method.md`](references/method.md) Steps 1–2.

## Stage 4 — Test, measure and assemble

The quantitative thresholds, the measure of segment profit, then the segment data:
[`references/method.md`](references/method.md) Steps 3–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for a single segment, a matrix
organisation, a measure that differs from GAAP, and a change in segment structure.

## Stage 5 — Reconcile, add entity-wide disclosures, and present

The reconciliations, the entity-wide disclosures, comparatives and consistency, then the output:
[`references/method.md`](references/method.md) Steps 6–9. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the segment
definitions, the dimension mapping and the profit measure.

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
