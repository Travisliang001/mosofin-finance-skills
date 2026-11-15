---
name: payroll-tax-filings
description: "Supports payroll tax deposits and returns: identifies the filing obligations the user confirms, the deposit schedule assigned for the year, computes the amounts due from the payroll register on rates the user supplies, reconciles deposits made to the liability, and prepares the figures for periodic returns and year-end wage statements. Reads the payroll liability accounts through a connected Mosofin workspace when the user agrees, or works from uploaded payroll registers. Use when the user asks about payroll tax deposits, reconciling payroll tax liabilities to payments, quarterly payroll returns, or year-end wage statement totals. Do not use for the payroll journal entry (use payroll-journal-entry-builder) or for tying the register to the ledger (use payroll-reconciliation). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing. Works on totals where it can and saves no employee data."
---

# Payroll tax filings: what was withheld, deposited and reported

Payroll taxes are withheld from pay, added to by the employer, deposited on a schedule and
reported on returns. The three figures must agree: **withheld, deposited, reported**. This skill
computes the amounts due, reconciles deposits to the liability, and prepares the return figures.

**Works with or without Mosofin.** With Mosofin connected the payroll liability accounts and
payments are read. Without it, you upload the registers and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** The payroll register is usually outside
the books, and so is the deposit schedule assigned for the year. **Even where a provider files for
you, the employer remains liable**, so the reconciliation still matters. Background:
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
- **Never deposits, files or signs anything.**
- **Never shows employee-level pay where a total will do**, and saves no employee data.
- **Never assumes the deposit schedule.** It can change each year.

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
| **B** | *Which employer, which employment jurisdictions, and which period?* | The country on record is only a pointer | **Ask again.** |
| **C** | *What are the current rates, wage bases and deposit rules, with source and year?* | Never built in | **Blocking.** Reconcile deposits to the liability recorded, and compute nothing. |
| **D** | *What deposit schedule were you assigned for this year?* | It decides the due dates | List due dates as not determined. |
| **E** | *Can you supply the payroll registers, and does a provider file and remit for you?* | The register is the missing half | Work from the ledger alone, and say that the register was not seen. |
| **F** | *Is this a periodic return, year-end, or both?* | Year-end adds wage statements | Prepare the periodic figures only. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report payroll tax liabilities with no payment against them, by age.
- Confirm who may see the output.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Payroll registers** for the period | Required | XLSX or CSV |
| **Rates and deposit rules** with source | Required | PDF |
| **Deposit confirmations** | Required for the reconciliation | PDF or CSV |
| Prior filings | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing **Q3 payroll tax** figures for **Northbrook Trading**, employing in **one
> jurisdiction**, from **your Mosofin connection** and **the registers you uploaded**. **Semi-
> weekly** deposit schedule for 2026. Filed by **your payroll provider**; rates from **the source
> you gave**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals, with no employee detail. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the liabilities and identify the obligations

Pull the liability accounts and payments, then the filing obligations and deposit requirements:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Compute and reconcile

The amounts due, then deposits against the liability:
[`references/method.md`](references/method.md) Steps 3–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for a deposit schedule change, wage-base
ceilings, employees in several jurisdictions and a third-party provider.

## Stage 5 — Returns, year-end, calendar, and present

The periodic returns, year-end filings and wage statements, the remittance calendar, then the
output: [`references/method.md`](references/method.md) Steps 5–8. Before presenting, check it
against [`references/output.md`](references/output.md). Ask whether the user wants the workpaper
as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the jurisdictions and the account
mapping. **No rate, schedule or employee data is saved.**

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
