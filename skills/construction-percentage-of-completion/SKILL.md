---
name: construction-percentage-of-completion
description: "Accounts for long-term construction and similar contracts recognised over time under ASC 606 or IFRS 15: confirms the over-time criteria, identifies the performance obligations, sets the transaction price, applies the measure of progress, computes cumulative revenue, cost and margin, applies changes in estimate, provides for loss contracts, and tracks contract assets and liabilities against billings. Reads costs and billings by job through a connected Mosofin workspace when the user agrees, or works from uploaded contract schedules. Use when the user asks about percentage of completion, cost-to-cost, over- and under-billings, work in progress on contracts, a loss-making contract, or revenue on a long-term project. Do not use for costing jobs without revenue recognition (use cost-accounting-job-order) or for revenue contracts in general (use revenue-recognition-asc606). Read-only: produces the contract schedule and proposed entries, and never estimates cost to complete."
---

# Percentage of completion: how done are you?

A project that takes two years cannot wait until the end to record revenue. Revenue is recognised
**as the work gets done**. The hard part is deciding how done it is, and the answer rests on one
number: the **total estimated cost at completion**. This skill builds the contract schedule from
it and proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads costs to date and billings by
contract, where jobs are tagged. Without it, you upload the contract schedules and the method is
the same.

**The estimate to complete is never in the books.** It comes from the project team, per contract.
So do the contract price, the variations and whether a claim has been approved. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never estimates the cost to complete.** A contract with no current estimate is listed as not
  computed.
- **Never recognises a variation or claim that has not been approved** without the user's judgment
  on it.
- **Never defers a loss.** A loss-making contract is provided for in full when it is known.
- **Never nets contract assets against contract liabilities across contracts.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–12" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and US GAAP or IFRS?* | Sets the scope | **Never default the period.** |
| **C** | *Which contracts are in progress: customer, scope, price, term? How are jobs tagged in the books?* | This is how costs and billings are read by contract | **Ask again** for the tagging. |
| **D** | *What is the total estimated cost at completion for each contract, and when was it last updated?* | The number everything depends on | **Blocking** for that contract. |
| **E** | *Which measure of progress applies: cost-to-cost, units or milestones?* | Output measures need site data | Use cost-to-cost, and **say that you assumed it.** |
| **F** | *Are there variations, claims, bonuses or penalties, and are they approved?* | Variable consideration is constrained | Use the original contract price only, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report costs with no job tag, which cannot be attributed to a contract.
- Say which contracts have a current estimate and which do not.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Contract list**: price, term, status | Required | XLSX |
| **Estimated cost at completion** per contract, with date | Required | XLSX |
| **Costs to date and billings to date** per contract | Required | XLSX or CSV |
| Variations and claims with approval status | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Accounting for **five contracts in progress** at **Northbrook Construction** for **September**
> under **ASC 606**, tagged by **project**, from **your Mosofin connection**. Cost-to-cost;
> estimates at completion **updated this month by the project managers**. One unapproved
> variation, left out. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the contract, the
period and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read costs and billings, and confirm over-time recognition

Pull costs and billings by contract, confirm the over-time criteria, then the performance
obligations: [`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Price, progress and cumulative results

The transaction price, the measure of progress, cumulative revenue, cost and margin, and changes
in estimate: [`references/method.md`](references/method.md) Steps 3–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for wasted costs, uninstalled materials,
claims and disputes, and cost-plus contracts.

## Stage 5 — Loss contracts, contract balances, and present

Loss provisions, contract assets and liabilities, modifications and disclosures, with entries as
**proposals**, then the output: [`references/method.md`](references/method.md) Steps 7–11. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 12. Persist the job tagging, the measure of
progress and the contract list. Estimates are supplied again every period.

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
