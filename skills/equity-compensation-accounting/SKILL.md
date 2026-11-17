---
name: equity-compensation-accounting
description: "Accounts for share-based compensation under ASC 718 or IFRS 2: classifies each award as equity-settled or cash-settled, takes the grant-date fair value the user supplies, analyses the vesting conditions, sets the recognition pattern, handles forfeitures, builds the expense schedule and proposed entries, and prepares the award roll-forward and disclosures. Compares the expense recorded in the books with the schedule. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded cap table and award data. Use when the user asks about stock compensation expense, options, RSUs, an ESPP, vesting schedules, forfeitures, a modification or repricing, or ASC 718 or IFRS 2. Do not use for the statement of equity (use statement-of-equity-changes) or for the payroll entry (use payroll-journal-entry-builder). Read-only: produces the schedule and proposed entries, and never values an award."
---

# Share-based pay: how much it cost, and when

Paying people in shares or options is still pay. The accounting asks **how much**, since no money
changed hands, and **when**, since the employee must stay to earn it. The answer: value the award
on the grant date and spread it over the vesting period. This skill builds that schedule and
proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads the expense and equity already
recorded and compares them with the schedule. Without it, you upload the award data and the method
is the same.

**The cap table and every fair value come from you.** Award terms, grant dates, vesting conditions
and valuations are never in the accounting system. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never values an award or picks a valuation input.** It asks for the value, its source and its
  date.
- **Never decides whether a performance condition is probable.**
- **Never picks the forfeiture policy**, and never changes it between periods without saying so.

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
| **B** | *Which company and period, and ASC 718 or IFRS 2?* | Decides attribution and forfeiture treatment | **Never default the period.** |
| **C** | *What are the awards: type, grant date, quantity, strike price, vesting terms, and equity- or cash-settled?* | From the cap table | **Blocking.** Report the expense recorded, and build no schedule. |
| **D** | *What is the grant-date fair value of each award, and where does it come from?* | Never computed here | **Blocking** for that award. |
| **E** | *What are the vesting conditions: service, performance or market? What is the forfeiture policy?* | They change the accounting entirely | Treat as service-only with forfeitures as they occur, and **say that you assumed it.** |
| **F** | *Were any awards modified, cancelled or exercised in the period?* | Repricings and accelerations are complex | Assume none, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report how the expense recorded has moved over time. A flat charge through periods of granting
  and vesting is a schedule nobody refreshed.
- Confirm which entity issues the shares.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Award data from the cap table**: grants, vests, exercises, forfeitures | Required | XLSX |
| **Fair values** per award, with source and date | Required | XLSX or PDF |
| **Ledger detail** for stock compensation expense and equity | Recommended, for the comparison | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Accounting for share-based pay at **Northbrook Holdings** for **Q3** under **ASC 718**, from
> **the cap table export you uploaded** and the ledger in **your Mosofin connection**. **Options
> and RSUs**, equity-settled, service vesting over **four years**; values from **your latest
> independent valuation**; forfeitures **as they occur**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the award count,
the dates and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read what was recorded and classify the awards

Pull the recorded expense and equity, reconcile what was recorded, then classify each award:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Value, vesting, recognition and forfeitures

The grant-date fair value supplied, vesting conditions, the recognition pattern and forfeitures:
[`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for market and performance conditions,
graded vesting, modifications and private company valuations.

## Stage 5 — Schedule, entries, roll-forward, and present

The expense schedule and entries as **proposals**, exercises and settlements, the roll-forward and
disclosures, then the output: [`references/method.md`](references/method.md) Steps 6–10. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the framework, the forfeiture
policy and the attribution method. Award data is supplied again each period.

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
