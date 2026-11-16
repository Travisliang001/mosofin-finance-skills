---
name: flux-analysis
description: "Flux analysis of the income statement and balance sheet: compares each account with the prior month and the same month last year, flags movements that pass both a percentage and an amount threshold, sorts each into a driver (volume, price, mix, timing, one-time, or error), and drafts the explanation and the follow-up for each account's owner. Treats an account that drops to nil as a possible missing posting, not a saving, and proves the cash movement from the balance sheet changes. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded statements. Use when the user asks for a flux, fluctuation or variance analysis, month-over-month or year-over-year review, or explanations of account movements for the close or a review. Do not use for comparison against a budget (use budget-vs-actual-analysis). Read-only: produces the flux schedule, explanations, proposed entries and a coverage sheet, and posts nothing."
---

# Flux analysis: which accounts moved, and why

A flux (fluctuation) analysis compares this period's balances with a prior period and explains
every movement big enough to matter. This skill finds those movements with **two thresholds that
must both trip**, sorts each into a **driver**, and drafts the explanation and the question for
the account's owner. A person signs off each explanation.

**Works with or without Mosofin.** With Mosofin connected it reads the income statement and
balance sheet for each period, and drills into the ledger for the accounts that move. Without it,
you upload the statements and the method is the same.

**A movement is not an explanation.** "Marketing is up 53%" restates the number. An explanation
names the driver and the evidence: a campaign, a price change, an entry posted late, a missing
accrual. Where no evidence explains a movement, the skill says so and asks; it never invents a
reason. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** It posts no entry and sends no
  question. Every entry and every owner request is a proposal.
- **Both thresholds must trip** before a movement is flagged, and the thresholds are stated on
  the face of the output.
- **Never invents an explanation.** Each one cites its evidence or is marked "unexplained: asked".

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Collect the basics in **one short batch**. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and which period?* | Sets every read | **Never default the period.** |
| **C** | *Compare with what: the prior month, the same month last year, or both?* | Decides the comparison columns | Both, where the data covers them. |
| **D** | *What thresholds? A percentage and an amount, for the income statement and the balance sheet* | Decides what gets flagged | 10% and 1% of revenue for the income statement; 10% and 1% of total assets for the balance sheet. **Say that the default was used.** |
| **E** | *Who owns which accounts?* | Who each question goes to | One question list to the controller. |
| **F** | *Anything you already know happened? A price change, a campaign, a one-off* | Explanations with evidence the books do not hold | Explain from the books only. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Confirm the periods and the comparison basis (C) before reading.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Income statement by account** for the period and each comparison period, or a monthly trend report | Required | XLSX or CSV |
| **Balance sheet by account** at the same dates | Recommended. Without it the cash proof and balance sheet flux are not run, and the output says so | XLSX or CSV |
| Ledger detail or journal list for the period | Recommended. It turns a movement into an explanation | XLSX or CSV |
| Owner list (E) and known events (F) | Optional | Any, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Flux for **Acme Supply** for **March 2026**, against **February 2026** and **March 2025**,
> from **your Mosofin connection**. Flagging a movement over **15% and 5,000** on the income
> statement and **15% and 25,000** on the balance sheet. Questions go to the account owners you
> listed. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the periods it
covers, the row count and the totals. Flag anything unreadable, or covering the wrong period,
straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile. On the upload
path, go straight to Stage 3.

## Stage 3 — Build the comparison

Read both statements for every period in one batch and line the accounts up side by side:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Flag, drill in and explain

Apply both thresholds, then drill into each flagged account and assign its driver:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for nil balances, reclassifications and
sign changes.

## Stage 5 — Prove cash, propose entries, and present

Prove the cash movement from the balance sheet changes, propose entries for errors and missing
postings, and draft the owner questions: [`references/method.md`](references/method.md) Steps 5–6
and *Outputs*. Before presenting, check it against [`references/output.md`](references/output.md).
Ask whether the user wants the schedule as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the thresholds, the owner list and
the account groupings.

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
