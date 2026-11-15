---
name: tax-return-prep-corporate
description: "Prepares the corporate income tax computation and its workpapers: starts from book profit and tests that it agrees with the accounts, adds back disallowable costs and sweeps the ledger for ones nobody listed, deducts items taxed differently, computes tax depreciation or capital allowances, applies loss relief and credits, and works out the tax, payments and supporting schedules. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded trial balance. Use when the user asks to prepare a corporate tax computation, convert book income to taxable income, find disallowable expenses, or build tax return workpapers. Do not use for the tax charge in the accounts (use corporate-tax-provision-asc740) or for an individual (use personal-tax-return-prep). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# Corporate tax computation: from book profit to taxable profit

Converts **book profit into taxable profit**: adds back what the tax rules disallow, deducts what
they treat differently, replaces book depreciation with the tax version, applies losses and
credits, and computes the tax. It builds the workpapers a return is prepared from.

**Works with or without Mosofin.** With Mosofin connected the starting profit is read and the
ledger is swept for disallowable costs nobody listed. Without it, you upload the trial balance and
the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** Loss carryforwards, allowance pools and
elections are tax attributes from prior returns, not ledger balances. Background:
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
- **Never decides that a cost is deductible.** It lists candidates and applies the schedule the
  user supplies.
- **Never takes a loss carryforward or an allowance pool from the ledger.** They come from the
  prior return.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–11" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which entity, jurisdiction and tax year?* | Sets every rule that applies | **Ask again.** |
| **C** | *What are the current rates, thresholds and rules, with their source and year?* | Never built in, never carried forward | **Blocking.** Assemble the figures from the books, and compute no tax. |
| **D** | *Which categories are disallowed in this jurisdiction, and to what extent?* | Drives the add-backs | List the candidate accounts, and add back nothing. |
| **E** | *What are the allowance pools, losses brought forward and credits, from the prior return?* | Tax attributes are not in the books | Compute taxable profit before reliefs, and say so. |
| **F** | *Are there group or related party matters?* | Group relief and pricing adjustments | Treat the entity as standalone, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Test that the profit read agrees with the accounts being filed.
- Report entertainment, fines, donations and similar accounts as candidates for add-back.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance and accounts** for the year | Required | XLSX or PDF |
| **Rates and rules** with source and year | Required | Type it in the chat, or PDF |
| **Prior year return** | Required for attributes | PDF |
| Fixed asset additions and disposals | Required for tax depreciation | XLSX |

**Read back before starting, then wait for a yes:**

> *Preparing the **2025 corporate tax computation** for **Northbrook Trading**, in **the
> jurisdiction you named**, from **your Mosofin connection** and **the prior return you
> uploaded**. Disallowables per **your schedule**; rates from **the source you gave**. Standalone
> entity. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the year and the
totals. Flag anything unreadable straight away.

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

## Stage 3 — Establish and test the starting point

Book profit, tested against the accounts: [`references/method.md`](references/method.md) Steps
1–1b.

## Stage 4 — Adjust to taxable profit

Add-backs, the sweep for unlisted disallowables, items taxed differently, tax depreciation, and
adjusted profit: [`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for interest limits, loss restrictions and
capital against revenue.

## Stage 5 — Reliefs, tax, schedules, and present

Loss relief, the tax, credits, payments, the supporting schedules, then the output:
[`references/method.md`](references/method.md) Steps 6–11. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the account-to-category
mapping for add-backs. **No rate and no attribute balance is saved.**

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
