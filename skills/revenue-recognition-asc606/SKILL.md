---
name: revenue-recognition-asc606
description: "Applies the five-step revenue recognition model of ASC 606 and IFRS 15 to a customer contract: tests first whether the books apply the standard at all, then identifies the contract and its performance obligations, sets and allocates the transaction price, recognises revenue over time or at a point in time, and builds the schedule, the contract asset and liability balances, the proposed entries and the disclosure data. Reads billing and recognised revenue through a connected Mosofin workspace when the user agrees, or works from an uploaded contract and billing history. Use when the user asks how to recognise revenue on a contract, about deferred revenue, performance obligations, standalone selling prices, variable consideration, contract modifications, or ASC 606 or IFRS 15. Do not use for raising an invoice (use customer-invoicing) or for period-end deferrals in general (use accruals-and-deferrals). Read-only: produces the analysis, the schedule and proposed entries, and posts nothing."
---

# Revenue recognition: an invoice is not revenue

Applies the **five-step model** to a customer contract: the contract, the performance obligations,
the price, its allocation, and recognition as each obligation is met. It produces the analysis,
the **recognition schedule** and the proposed entries. A person reviews the judgments and posts.

**Works with or without Mosofin.** With Mosofin connected it reads what was billed and what was
recognised, and tests whether revenue in the books simply follows the invoices. Without it, you
upload the contract and the billing history and the method is the same.

**The contract is the primary input, and it is never in the books.** A general ledger is organised
around invoices, and an invoice is not revenue. The terms, the obligations and the standalone
selling prices come from you. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never treats billed as earned.** Recognition follows the obligations, not the invoice dates.
- **Never picks the framework, an expedient or a standalone selling price.** An estimated price
  states its method and source.
- **Never concludes on a judgment for the user**: principal or agent, distinct or not, over time
  or point in time. It sets out the indicators and asks.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–11" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, which contract, and which period?* | Sets the unit of account | **Ask again.** The analysis is contract by contract. |
| **C** | *ASC 606 or IFRS 15?* | The two differ at the edges | **Ask again.** Never infer it from the country. |
| **D** | *Can you supply the contract, or its key terms: deliverables, price, term, payment, renewal, termination?* | There is no substitute for it | Run Step 0 only, the test of how the books recognise revenue, and say so. |
| **E** | *What are the standalone selling prices, and where do they come from?* | Allocation depends on them | Use observable prices from the books where they exist, and ask about the rest. |
| **F** | *Which practical expedients are elected, and was the contract modified?* | Both change the schedule | Assume none, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report what Step 0 shows before the interview: does recognised revenue move with invoicing, or
  with delivery?
- Mid-contract, read what has been recognised so far. It is evidence of what was done, not of what
  should have been.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **The contract**, or a summary of its key terms | Required | PDF or pasted |
| **Invoices and payments** on the contract to date | Required | XLSX or CSV |
| **Revenue and deferred revenue ledger detail** for the customer | Recommended, for the mid-contract position | XLSX or CSV |
| Standalone selling prices with sources | Required for more than one obligation | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Analysing the **three-year software and implementation contract** with **Harlow Fabrication**
> for **Northbrook Trading**, under **ASC 606**, from **the contract you uploaded** and billing in
> **your Mosofin connection**. Standalone prices from **your price list**. No expedients; no
> modifications. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the contract's
parties, term and price, or the period and totals of a listing. Flag anything unreadable straight
away.

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

## Stage 3 — Test the books, then identify the contract and its obligations

Whether the books apply the standard at all, then the contract and its performance obligations:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Price, allocate and recognise

The transaction price, its allocation, and recognition as each obligation is satisfied:
[`references/method.md`](references/method.md) Steps 3–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for upfront payments, implementation and
setup fees, free trials, acceptance clauses, principal against agent, licences and royalties.

## Stage 5 — Balances, entries, modifications, and present

Contract assets and liabilities, the entries as **proposals**, modifications, contract costs and
disclosure data, then the output: [`references/method.md`](references/method.md) Steps 6–11.
Before presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the framework, the
elected expedients and the standalone selling price method. Each contract is analysed afresh.

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
