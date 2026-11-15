---
name: benefits-and-401k-accounting
description: "Accounts for employee benefits: sorts them into defined contribution plans, compensated absences, short-term benefits such as health cover, and defined benefit plans, then computes the cost and the liability for each, handles vesting and forfeitures, and reconciles what was withheld to what was remitted. Checks for employee contributions still sitting in the employer's books. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded payroll and plan data. Use when the user asks about 401(k) or retirement plan accounting, employer match, accrued vacation or PTO, a health benefit accrual, or unremitted contributions. Do not use for the payroll entry itself (use payroll-journal-entry-builder), payroll tie-outs (use payroll-reconciliation) or a defined benefit valuation in depth (use pensions-and-postretirement-asc715). Read-only: produces the schedules and proposed entries, and remits nothing."
---

# Employee benefits: what you owe beyond pay

Pay is not the only thing owed to employees. There are **retirement contributions**, health cover,
and **holiday built up and not yet taken**. Each is a cost already incurred, and often a
liability. This skill computes each one and proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads the benefit expense and
liability accounts, and checks whether **amounts withheld from employees were passed on**. Without
it, you upload the payroll and plan data and the method is the same.

**Plan terms and balances are not in the books.** The match formula, eligibility, vesting, holiday
balances in hours and any actuarial report come from you or from payroll. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never values a defined benefit obligation.** Without an actuarial report, that part is listed
  as not done.
- **Never assumes a match formula, an accrual rate or a vesting schedule.**
- **Never remits or moves a contribution.** An unremitted balance is reported with its age.

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
| **B** | *Which company and period, and US GAAP or IFRS?* | The framework decides the defined benefit treatment | **Never default the period.** |
| **C** | *Which benefits are offered: retirement, health, insurance, paid time off, others?* | Sets what is in scope | Use what the chart of accounts suggests, and confirm. |
| **D** | *What are the plan terms: contribution formula, match, eligibility, vesting?* | Never in the ledger | Report what was expensed, and compute nothing. |
| **E** | *What are the paid-time-off policy and the balances per employee?* | Hours and rates come from payroll or HR | List the accrual as not computed. |
| **F** | *Is there a defined benefit plan with an actuarial report, and what are the remittance deadlines?* | Needed for that plan, and to judge unremitted balances | Treat as none, and report unremitted balances by age only. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report employee contributions withheld and not yet remitted, with their age.
- Say whether payroll is connected, or only the accounting entries.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Payroll and contribution data** by period | Required | XLSX or CSV |
| **Plan documents** or a summary of terms | Required | PDF |
| **Paid-time-off balances** by employee | Required for that accrual | XLSX |
| Actuarial report | Required for a defined benefit plan | PDF |

**Read back before starting, then wait for a yes:**

> *Accounting for benefits at **Northbrook Trading** for **September** under **US GAAP**, from
> **your Mosofin connection** and **the payroll data you uploaded**. A **401(k) with a 4% match**,
> vesting over **three years**; paid time off **paid out on leaving**. No defined benefit plan.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
employee count and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the accounts and sort the benefits

Pull the benefit accounts, then categorise the benefits:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Compute each benefit

Defined contribution plans, compensated absences, short-term benefits, defined benefit plans and
vesting: [`references/method.md`](references/method.md) Steps 2–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for use-it-or-lose-it policies,
self-insured health plans, remittance deadlines and multiemployer plans.

## Stage 5 — Reconcile, disclose, and present

The reconciliation and disclosures, with entries as **proposals**, then the output:
[`references/method.md`](references/method.md) Steps 7–8. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the plan terms, the paid-time-off
policy and the account mapping.

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
