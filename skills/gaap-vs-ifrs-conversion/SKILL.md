---
name: gaap-vs-ifrs-conversion
description: "Converts financial statements between US GAAP and IFRS or a local GAAP: scopes the conversion, identifies the differences area by area for this business, classifies each, quantifies the adjustments with their deferred tax, applies first-time adoption rules where relevant, builds the reconciliation between the two frameworks, and restates the statements and policies. Reads the source statements through a connected Mosofin workspace when the user agrees, or works from uploaded statements and policies. Use when the user asks to convert accounts between US GAAP and IFRS, list GAAP differences for their business, prepare a reconciliation between frameworks, or plan first-time adoption of IFRS. Do not use for translating currencies (use foreign-currency-translation-asc830) or for group consolidation (use consolidation-and-eliminations). Read-only: produces the adjustments, the reconciliation and restated statements, and posts nothing."
---

# GAAP to IFRS: one business, two rulebooks

The same business and the same transactions, under two rulebooks that disagree about **when to
recognise things and what to measure them at**. Converting means finding every place they disagree
for this business, sizing each difference, and showing how one set of accounts becomes the other.
This skill builds that reconciliation.

**Works with or without Mosofin.** With Mosofin connected the source statements and balances are
read, which shows which areas are large enough to matter. Without it, you upload the statements
and the method is the same.

**The books do not declare a framework, and a balance is not a policy.** How each item is
accounted for today comes from you, area by area. Differences that turn on judgment are set out,
not decided. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never infers an accounting policy from a balance.**
- **Never states a standard's requirement from memory as settled.** The user confirms the standard
  in force at the reporting date.
- **Never drops the deferred tax on an adjustment.**
- **Never decides an elective exemption for the user.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–9" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and from which framework to which?* | Direction matters | **Ask again.** Never default either. |
| **C** | *Why convert: group reporting, a listing, or first-time adoption? Will dual reporting continue?* | Decides whether first-time adoption rules apply, and the deliverable | **Ask again.** |
| **D** | *How are the key items accounted for today: revenue, leases, inventory, development costs, fixed assets, financial instruments?* | The core input | List the areas by size, and ask about each. |
| **E** | *Can you supply the schedules for the affected areas?* | Adjustments are computed from them | Identify the difference, and list its amount as not quantified. |
| **F** | *What is materiality, and the transition date if this is first-time adoption?* | Sets the effort and the opening balance sheet | Quantify every difference found. **Never supply a threshold.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report any balance that contradicts the framework stated, such as a revaluation surplus in books
  said to be US GAAP.
- Read back each company file with its current framework.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Source financial statements** and trial balance | Required | XLSX or PDF |
| **Accounting policies** in use | Required | PDF, or type it in the chat |
| **Schedules** for the affected areas | Required to quantify | XLSX |

**Read back before starting, then wait for a yes:**

> *Converting **Northbrook Trading** from **US GAAP to IFRS** for the **year to 31 December**, for
> **group reporting**, ongoing each year, from **your Mosofin connection** and **the policies you
> uploaded**. Inventory is on **FIFO**; development costs are **expensed**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the statements and scope the conversion

Pull the source statements, then scope the conversion:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Identify, classify and quantify the differences

Differences by area, their classification, and the adjustments:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for LIFO inventory, development costs,
impairment reversals, the revaluation model and deferred tax on every adjustment.

## Stage 5 — First-time adoption, reconciliation, and present

First-time adoption where it applies, the reconciliation, the restated statements and policies,
then the output: [`references/method.md`](references/method.md) Steps 5–8. Before presenting,
check it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the two frameworks, the policies
confirmed and the differences that apply to this business.

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
