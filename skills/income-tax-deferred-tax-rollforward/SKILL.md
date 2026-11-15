---
name: income-tax-deferred-tax-rollforward
description: "Builds and maintains the deferred tax schedule under ASC 740 or IAS 12: the inventory of temporary differences between book and tax basis, deferred tax assets and liabilities by jurisdiction at the enacted rates the user supplies, the roll-forward from opening to closing, the valuation allowance evidence, the tie to the total provision, and the proposed entries and disclosures. Reads book balances through a connected Mosofin workspace when the user agrees, or works from an uploaded trial balance and tax schedules. Use when the user asks for a deferred tax roll-forward, deferred tax assets and liabilities, temporary differences, or to tie deferred tax to the provision. Do not use for the whole provision (use corporate-tax-provision-asc740) or for the tax return (use tax-return-prep-corporate). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# Deferred tax: the future tax already on the balance sheet

The accounts and the tax return count the same things at different times. Until those gaps unwind,
the future tax they represent sits on the balance sheet: an **asset** if it will save tax later, a
**liability** if it will cost tax later. This skill builds that schedule and rolls it forward.

**Works with or without Mosofin.** With Mosofin connected the book side of every difference is
read. Without it, you upload the trial balance and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** The tax basis, the tax depreciation
schedule and loss carryforwards with their expiry come from the returns. Background:
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
- **Never puts a permanent difference in the schedule.**
- **Never concludes on the valuation allowance.** It sets out the evidence.

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
| **B** | *Which entity, period and tax jurisdiction?* | Sets the scope | **Never default the period.** |
| **C** | *What are the enacted rates by jurisdiction, with source, and when is each difference expected to reverse?* | Deferred tax uses the rate for the reversal period | **Blocking.** Build the inventory, and compute no balance. |
| **D** | *What is the tax basis of each item: fixed assets, accruals, reserves?* | The book side is read; the tax side is not | List the item with its tax basis outstanding. |
| **E** | *What are the loss and credit carryforwards, with expiry dates?* | Expiry matters as much as amount | Leave them out, and say so. |
| **F** | *Do you have last period's deferred tax workpapers?* | The opening balances | Open from the ledger balance in total. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Prove the opening balances against the ledger.
- With several entities, ask which tax group and jurisdiction each belongs to.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance** for the period | Required | XLSX or CSV |
| **Tax basis schedules**, including tax depreciation | Required | XLSX |
| **Prior deferred tax workpapers** | Required for opening balances | XLSX |
| Enacted rates with source | Required | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Rolling forward deferred tax for **Northbrook Trading** for **2025**, from **your Mosofin
> connection** and **the tax depreciation schedule you uploaded**. Enacted rate from **the source
> you gave**. Losses brought forward per **the prior return**, expiring as listed. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the books and build the inventory

Pull the book balances, then the inventory of temporary differences:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Compute and roll forward

Deferred tax assets and liabilities, then the roll-forward:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for a rate that is not the enacted rate for
the reversal period, and a rate change.

## Stage 5 — Allowance, tie-out, entries, and present

The valuation allowance evidence, the tie to the provision, entries as **proposals**, disclosures,
then the output: [`references/method.md`](references/method.md) Steps 4–8. Before presenting,
check it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the inventory of differences and
the account mapping. **No rate is saved.**

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
