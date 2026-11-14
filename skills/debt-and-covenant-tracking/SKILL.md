---
name: debt-and-covenant-tracking
description: "Tracks borrowings and loan covenants: the schedule of facilities and balances, amortisation checked against what was actually repaid, a sweep for debt-like items missing from the list, each covenant computed on the agreement's own definitions with its headroom, a forward projection, the maturity profile, and the compliance report. Computes no covenant until the agreement's definitions are supplied, and labels book figures as book figures. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded statements and loan terms. Use when the user asks to track debt or loan covenants, check covenant compliance or headroom, build a debt or amortisation schedule, prepare a compliance certificate, review the maturity profile, or assess a possible breach. Do not use for a weekly cash forecast (use cash-flow-forecast-13-week) or for interest accruals alone (use accruals-and-deferrals). Read-only: produces the schedules, the covenant position and a coverage sheet, and posts nothing."
---

# Debt and covenants: what you owe, and how much room is left

A loan comes with promises: keep debt below a multiple of profit, keep interest cover above a
level, report on time. Break one and the loan can fall due at once. This skill tracks **what is
owed**, works out **where the business stands against each promise**, and shows the headroom. A
person signs the compliance certificate.

**Works with or without Mosofin.** With Mosofin connected it reads every debt account, the
principal repaid and the interest charged, and the book figures behind each ratio. Without it, you
upload them and the method is the same.

**The loan agreement is the source of truth, and it is never in the books.** "EBITDA", "Debt" and
"Cash" are defined terms in an agreement, with addbacks, exclusions and caps. A ratio from book
figures can show comfortable headroom while the covenant is in breach. So **no covenant is
computed until the agreement's definitions are supplied.** Until then the skill gives the book
components, labelled as inputs. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system**, and never contacts a lender.
- **Never presents a book ratio as a compliance position.**
- **Never assumes the test period matches the accounting period**, and never invents a rate, a
  term or a definition.
- **Never certifies compliance.** It prepares the computation; an authorised person signs.

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
| **B** | *Which facilities do you have, and what are the terms of each: principal, rate, repayment, maturity, fees?* | Balances are in the books; terms are not | Build the schedule from the debt accounts found, and list the terms as missing. |
| **C** | *How does each agreement define its covenants: the exact numerator and denominator, addbacks and caps?* | Without these a covenant ratio is wrong | **Blocking.** Compute no covenant. Give the book components, labelled as inputs. |
| **D** | *What is the test date and the test period: trailing twelve months, quarterly or annual?* | It often differs from the accounting period | **Never assume it.** Ask again. |
| **E** | *Which companies are inside the borrowing group?* | The covenant is tested on that perimeter | Required with several company files. Treat a single company as the whole group, and say so. |
| **F** | *Do you have a forecast, the lender's certificate format, and any waivers or amendments in force?* | Needed for the forward view and the report | Report the current position only, with no projection. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- List the debt accounts found in the chart of accounts and **confirm them against the facilities
  named in B.**
- Say which facilities have definitions supplied and which do not, before starting.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Loan agreements**, or a term sheet summary for each facility | Required | PDF, or type the terms in the chat |
| **Covenant definitions** for each agreement (C) | **Required for any covenant.** Without them only book components are given | PDF or pasted |
| **Balance sheet and income statement** for the test period | Required | XLSX, CSV or PDF |
| **Ledger detail for the debt and interest accounts** | Required to check amortisation against actual repayments | XLSX or CSV |
| Forecast, certificate format, waivers (F) | Recommended | XLSX or PDF |

**Read back before starting, then wait for a yes:**

> *Tracking debt and covenants for **Northbrook Trading** at **30 September**, tested on the
> **trailing twelve months**, from **your Mosofin connection**. Two facilities: the **term loan**,
> with definitions supplied, and the **revolver**, with none, so its covenants will not be
> computed. No forecast supplied. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the facility or
the period, and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, settle the testing perimeter, check which read tools are enabled, and read the
company profile. On the upload path, go straight to Stage 3.

## Stage 3 — Read the debt position and build the schedules

Pull the debt and interest accounts in one batch, sweep for debt-like items missing from the
facility list, then build the debt schedule and the amortisation schedules:
[`references/method.md`](references/method.md) Steps 0–2, including Step 0b.

## Stage 4 — Catalogue, define and compute the covenants

List the covenants, record each definition exactly as the agreement states it, then compute the
ratios and the headroom: [`references/method.md`](references/method.md) Steps 3–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for pro-forma adjustments, cure rights,
cross-default, leases counted as debt, foreign currency debt and reporting deadlines.

## Stage 5 — Project, report, and present

Forward projection where a forecast was supplied, the maturity profile, the compliance report,
breach handling if it applies, then the output:
[`references/method.md`](references/method.md) Steps 6–10. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the facility terms and the
covenant definitions, each keyed to its own facility. Every balance and ratio is computed again
each period.

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
