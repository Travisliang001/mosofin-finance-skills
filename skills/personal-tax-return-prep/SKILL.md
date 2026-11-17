---
name: personal-tax-return-prep
description: "Organises and computes an individual income tax return: reads the business-sourced figures for an owner where they are in the books, gathers and categorises income, applies deductions, reliefs and credits the user confirms, computes taxable income, tax and the balance due or refund, and produces a document checklist. Reads only the entities the taxpayer has an interest in through a connected Mosofin workspace when the user agrees, or works from uploaded documents. Use when the user asks to prepare or organise a personal tax return, compute an individual's tax, or build a checklist of documents for one. Do not use for a company's return (use tax-return-prep-corporate) or for a projection (use tax-planning-and-projections). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing. Handles one person's tax data and saves none of it."
---

# Personal tax return: one person's year, brought together

Everything a person earned in a year, from every source, brought together; then what the law lets
them subtract; then the tax on what remains, less what was already paid. This skill organises it,
computes it, and lists the documents needed.

**Works with or without Mosofin.** With Mosofin connected it reads only the business-sourced
figures, such as an owner's salary and dividends, from entities the taxpayer has an interest in.
Without it, you supply the documents and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** **This is one individual's tax
position.** It is shown only to the person named, and none of it is saved. Background:
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
- **Never reads an entity the taxpayer has no stated interest in.**
- **Never saves personal tax data**, and never asks for a full tax identification number.
- **Cross-border residency is flagged for a specialist, not worked through.**

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
| **B** | *Who is the taxpayer, in which jurisdiction, and for which tax year?* | The personal year may differ from the business year | **Ask again.** |
| **C** | *What are the current rates, thresholds and rules, with their source and year?* | Never built in, never carried forward | **Blocking.** Assemble the figures from the books, and compute no tax. |
| **D** | *What is the filing status: single, married, dependants, residency?* | Changes the computation | **Ask again.** |
| **E** | *Which connected entities does the taxpayer have an interest in, and in what capacity?* | Scopes what may be read | Read nothing from the books. |
| **F** | *What income documents, deductions and tax already paid are there?* | Personal documents are not in any books | List them on the checklist as outstanding. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Read back the taxpayer, the year and the entities in scope before any read.
- Confirm who may see the output.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Income documents** for the year | Required | PDF |
| **Rates and allowances** with source and year | Required | Type it in the chat, or PDF |
| **Prior year return** | Recommended | PDF |
| Deduction and credit evidence | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing the **2025 personal return** for **the owner you named**, resident in **the
> jurisdiction you named**, filing **jointly**. Salary and dividends from **Northbrook Trading**
> through **your Mosofin connection**; other income from **the documents you uploaded**. Output to
> **the taxpayer only**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the document type
and the year. Do not repeat tax numbers, account numbers or other personal identifiers back. Flag anything unreadable straight away.

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

## Stage 3 — Read the business figures and set the framework

The business-sourced figures, then the framework for this jurisdiction and year:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Income, deductions and taxable income

Income by category, income-specific and personal deductions, then taxable income:
[`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for foreign income, self-employment,
capital gains and rental property.

## Stage 5 — Tax, credits, balance due, and present

The tax, credits, the balance due or refund, the document checklist, then the output:
[`references/method.md`](references/method.md) Steps 6–10. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the structure of the checklist
only. **No personal figure, document or identifier is saved.**

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
