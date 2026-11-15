---
name: corporate-tax-provision-asc740
description: "Computes the income tax provision for the financial statements under ASC 740 or IAS 12: starts from pre-tax book income, identifies permanent and temporary differences, computes current and deferred tax at rates the user supplies, sets out the valuation allowance evidence and uncertain positions, allocates tax between components, and builds the effective tax rate reconciliation with tie-outs. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded trial balance. Use when the user asks for the tax provision, current and deferred tax expense, an effective tax rate reconciliation, a valuation allowance assessment, or ASC 740. Do not use for the tax return (use tax-return-prep-corporate) or for the deferred tax schedule alone (use income-tax-deferred-tax-rollforward). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# Tax provision: the tax charge in the accounts

The tax charge in the accounts is not the amount paid to the tax authority. Accounting and tax
rules disagree about **when** things count, so the accounts carry **current tax** and **deferred
tax**. This skill computes both and reconciles the effective rate.

**Works with or without Mosofin.** With Mosofin connected pre-tax income, the book side of each
difference and the loss history are read. Without it, you upload the trial balance and the method
is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** Tax basis, loss carryforwards and
uncertain positions come from the tax returns and from you. Background:
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
- **Never concludes on a valuation allowance or an uncertain tax position.** It sets out the
  evidence.
- **Never takes a tax basis from the ledger.**

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
| **B** | *Which entity, period and framework: US GAAP or IFRS?* | Deferred tax asset treatment differs | **Ask again.** Never default the period. |
| **C** | *What are the statutory rates, and the enacted future rates, per jurisdiction, with source?* | Never built in | **Blocking.** Identify the differences, and compute no tax. |
| **D** | *Which differences are permanent, and what is the tax basis of each temporary difference?* | The books show candidates only | List the candidates as not determined. |
| **E** | *What are the opening deferred tax balances by component, and the loss and credit carryforwards with expiry?* | From prior workpapers and returns | Open from the balance in the books in total, and say so. |
| **F** | *Are there uncertain tax positions, and what supports future taxable income?* | Judgments for management | List both as not assessed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Read back each company file with its jurisdiction.
- Report the cumulative loss history, which is evidence for the valuation allowance.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance** for the period | Required | XLSX or CSV |
| **Rates** per jurisdiction with source | Required | Type it in the chat |
| **Prior period provision workpapers** | Required for opening balances | XLSX |
| Tax returns and attribute schedules | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Computing the **2025 tax provision** for **Northbrook Trading** under **US GAAP**, from **your
> Mosofin connection** and **last year's workpapers**. Rates from **the source you gave**.
> Differences as you classified; no uncertain positions. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the books and start from pre-tax income

Pull the evidence, then pre-tax book income: [`references/method.md`](references/method.md) Steps
0–1.

## Stage 4 — Differences, current tax and deferred tax

Permanent and temporary differences, current tax, then deferred tax:
[`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for an enacted rate change, cumulative
losses and the return-to-provision true-up.

## Stage 5 — Allowance, positions, rate reconciliation, and present

The valuation allowance evidence, uncertain positions, allocation, the rate reconciliation and
tie-out, then the output: [`references/method.md`](references/method.md) Steps 6–11. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 12. Persist the classification of each
difference and the account mapping. **No rate is saved.**

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
