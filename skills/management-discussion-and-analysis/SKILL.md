---
name: management-discussion-and-analysis
description: "Drafts the management discussion and analysis: the overview, results of operations with every variance computed from the books, non-GAAP measures where used, liquidity and capital resources, critical accounting estimates, and a section for known trends that management writes, then checks that every figure agrees with the statements. Flags every forward-looking statement for sign-off. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded statements. Use when the user asks to draft or review MD&A, a management commentary, an explanation of results for a report or filing, or a liquidity discussion. Do not use for variance against the budget (use budget-vs-actual-analysis), a KPI dashboard (use kpi-dashboard-builder) or the notes (use notes-to-financial-statements). Read-only: produces a draft for management and legal review, and publishes nothing."
---

# MD&A: why the numbers moved, in management's voice

The statements say what happened. The **MD&A** says why, what it means, and what management
expects. This skill drafts it from the entity's actual figures, without boilerplate, and **flags
every forward-looking statement** for sign-off. It is a draft for management: the narrative is
theirs and carries legal weight.

**Works with or without Mosofin.** With Mosofin connected every figure and variance is computed
from the books and agreed to the statements. Without it, you upload the statements and the method
is the same.

**The arithmetic of a variance is not its explanation.** That revenue fell six percent can be
read. Why it fell, and what is expected next, are management's to supply. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never authors a forward-looking statement.** The section for trends is drafted as questions
  for management.
- **Never invents the reason for a variance.** With no driver given, the variance is stated and
  the reason is marked as needed.
- **Never defines a non-GAAP measure**, and never shows one without its reconciliation.
- **Never uses a comparative that has not been checked against what was issued.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–10" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and what kind of report: 10-K, 10-Q, an IFRS annual report or a private report?* | Decides the sections and the legal weight | **Never default the period.** |
| **C** | *What drove the changes in revenue, cost and margin?* | The heart of the document | Draft the variances with each reason marked as needed from management. |
| **D** | *What are the known trends and uncertainties?* | Never authored here | Leave the section as questions for management. |
| **E** | *What are the facilities, capex plans and covenant status?* | Cash and debt are in the books; plans and terms are not | Draft liquidity from balances only, and say so. |
| **F** | *Which non-GAAP measures are used, who signs off, and does legal review apply?* | Forward-looking wording needs sign-off | Use GAAP measures only, and leave the sign-off open. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Confirm the comparative figures against what was previously issued.
- Say that the narrative is on consolidated figures, and name the company files behind it.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Financial statements**, current and comparative | Required | XLSX or PDF |
| **Prior MD&A** | Recommended, for consistency | PDF |
| Drivers, trends, facilities and plans | Required for a complete draft | Type it in the chat |
| Non-GAAP definitions and reconciliations | Required if used | XLSX |

**Read back before starting, then wait for a yes:**

> *Drafting MD&A for **Northbrook Holdings** for the **year to 31 December**, for the **10-K**,
> from **your Mosofin connection**. Drivers as you described; trends section **left for
> management**; liquidity with **the facility terms you supplied**. Sign-off by **the CFO and
> counsel**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the figures and set the structure

Pull the statements and variances, then establish the structure:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Draft the sections

The overview, results of operations, non-GAAP measures, liquidity, critical estimates and known
trends: [`references/method.md`](references/method.md) Steps 2–7. Check
[`references/edge-cases.md`](references/edge-cases.md) for a loss-making period, going-concern
doubt, a material weakness, an acquisition, a restatement and a seasonal business.

## Stage 5 — Check consistency and grounding, and present

Every figure agreed to the statements and every forward-looking statement flagged, then the
output: [`references/method.md`](references/method.md) Steps 8–9. Before presenting, check it
against [`references/output.md`](references/output.md). Ask whether the user wants the draft as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the structure, the non-GAAP
definitions and the sign-off list.

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
