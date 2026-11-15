---
name: consolidation-and-eliminations
description: "Consolidates the trial balances of a group into group financial statements: sets the consolidation scope, aligns framework and currency, translates foreign entities at rates the user supplies, builds the consolidation workpaper, proposes intercompany eliminations, computes non-controlling interest and equity-method investments, and ties the consolidated statements out. Lists any group member whose books it could not read. Reads each entity through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances. Use when the user asks to consolidate entities, prepare group or consolidated accounts, eliminate intercompany balances, compute non-controlling interest, or build a consolidation workpaper. Do not use for matching intercompany balances pair by pair (use intercompany-reconciliation) or for a single company's statements (use financial-statement-builder). Read-only: produces the workpaper, proposed eliminations and a coverage sheet, and posts nothing."
---

# Consolidation: the group as one business

A group presents itself as though it were one business. That means adding up all the entities,
then removing everything they did with **each other**: a group cannot sell to itself or owe itself
money. This skill builds the **consolidation workpaper**, proposes the eliminations and produces
the group statements. A person reviews and adopts them.

**Works with or without Mosofin.** With Mosofin connected every connected entity's trial balance
is read at the same date, and intercompany balances are measured on both sides. Without it, you
upload a trial balance per entity and the method is the same.

**The group structure and every exchange rate come from you.** Ownership percentages, fair value
adjustments and goodwill are not in any entity's books, and no accounting system supplies rates.
Adding ledgers together is not consolidating them. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never presents summed ledgers as a consolidation.** An entity it could not read is named as
  missing.
- **Never supplies an exchange rate or an ownership percentage.**
- **Never forces an elimination.** An intercompany difference is carried and shown, not absorbed.
- **Never decides functional currency or control for the user.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–11" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which entities are in the group, who owns what percentage, and which is the parent?* | Drives scope and non-controlling interest | **Ask again.** Nothing can be consolidated without it. |
| **C** | *What consolidation date and period, and US GAAP or IFRS?* | Applied identically to every entity | **Never default either.** |
| **D** | *What is the presentation currency, and what are the closing, average and historical rates, with source and dates?* | No accounting system supplies rates | Consolidate same-currency entities only, and list the rest as not translated. |
| **E** | *Were there acquisitions: fair value adjustments, goodwill? Any equity-method investments?* | Not in any entity's books | Assume none, and **say that you assumed it.** |
| **F** | *Do you have the prior period's consolidated balances?* | Needed for continuity and the opening non-controlling interest | Start the roll-forward from this period, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and **every group member by name, with its role**, and wait for an
  explicit yes (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Name every group member that is not connected. Its figures must be uploaded, or the
  consolidation is partial and says so.
- Flag differing year-ends or accounting methods across the entities before anything is added up.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance for each entity** at the same date | Required | XLSX or CSV |
| **Group structure** with ownership percentages | Required | PDF, or type it in the chat |
| **Rate table** with source and dates | Required for more than one currency | XLSX or pasted |
| **Intercompany balances and transactions** per entity | Required for eliminations | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Consolidating **Northbrook Trading (parent), Northbrook Logistics (100%) and Northbrook UK
> (80%)** at **31 December** under **US GAAP**, from **your Mosofin connection**. Presentation
> currency **USD**, rates from **the table you supplied**. No acquisitions in the year. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the entity, the
date, the account count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read every entity and set the scope

Pull each trial balance at the same date, then settle which entities are consolidated and how:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Align, translate, build the workpaper and eliminate

Align framework and currency basis, translate, build the workpaper, then the eliminations as
**proposals**: [`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for an entity acquired or sold mid-period,
changes in ownership, different year-ends, multi-tier groups and intercompany profit.

## Stage 5 — Non-controlling interest, statements, tie-outs, and present

Non-controlling interest, equity-method investments, the consolidated statements and the tie-outs,
then the output: [`references/method.md`](references/method.md) Steps 6–10. Before presenting,
check it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the group structure, each entity's
role and the elimination rules. Every balance and rate is obtained again each period.

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
