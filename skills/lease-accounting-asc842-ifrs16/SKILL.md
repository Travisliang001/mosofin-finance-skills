---
name: lease-accounting-asc842-ifrs16
description: "Accounts for leases under ASC 842 or IFRS 16: confirms there is a lease, sets the term and payments, takes the discount rate from the user, classifies the lease where the framework requires it, measures the right-of-use asset and lease liability, builds the amortisation schedules, and proposes the periodic entries, reassessments and disclosures. Also searches the books for recurring rent-like payments with no lease on the balance sheet. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded lease terms. Use when the user asks about lease accounting, a right-of-use asset, a lease liability, operating against finance leases, a lease amortisation schedule, a lease modification, or ASC 842 or IFRS 16. Do not use for owned assets (use fixed-asset-register-and-depreciation) or for prepaid rent alone (use prepaid-amortization-schedule). Read-only: produces the schedules and proposed entries, and posts nothing."
---

# Leases: the right to use an asset, and the debt to pay for it

Renting something for years is, in substance, buying its use on credit. Both standards put the
**right-of-use asset** and the **lease liability** on the balance sheet. This skill turns a
contract full of options and escalations into those two numbers, a schedule and the proposed
entries. A person posts them.

**Works with or without Mosofin.** With Mosofin connected it reads the lease balances and
payments, and searches for **recurring rent-like payments with no lease recorded**. Without it,
you upload the lease terms and the method is the same.

**The lease agreement and the discount rate are never in the books.** Term, payments, options,
fair value and economic life come from the agreement and from you. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never fabricates a discount rate.** It asks for the rate and how it was derived.
- **Never classifies a lease under IFRS 16**, where a lessee has one model, and never skips
  classification under ASC 842.
- **Never decides that an option is reasonably certain to be exercised.** That judgment is the
  user's, and the schedule states it.

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
| **B** | *Which company and period, and are you the lessee or the lessor?* | This workflow centres on the lessee | **Never default the period.** Treat as lessee and say so. |
| **C** | *ASC 842 or IFRS 16?* | Decides whether classification happens at all | **Ask again.** |
| **D** | *Can you supply the lease agreements: term, payments, escalations, options, start date?* | The core input | Run the search for unrecorded leases only, and say so. |
| **E** | *What discount rate applies to each lease, and how was it derived?* | It drives both balances | **Blocking.** Build the payment schedule only; measure nothing. |
| **F** | *Which expedients are elected, is there a complete lease register, and was any lease modified?* | Short-term and low-value elections remove leases from the balance sheet | Assume no expedients, and make the completeness search the priority. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the rent-like payments found with no lease behind them, with vendor and amount.
- Say that fair value and economic life are not in the books, so ASC 842 classification needs them
  supplied.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Lease agreements**, or the key terms of each | Required | PDF or XLSX |
| **Discount rate** per lease, with its derivation | Required | Type it in the chat |
| **Lease balances and payments** in the ledger | Recommended, to tie the schedule to the books | XLSX or CSV |
| Existing lease register and schedules | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Accounting for **four property leases** of **Northbrook Trading** at **30 September**, as
> **lessee** under **ASC 842**, from **the agreements you uploaded** and the ledger in **your
> Mosofin connection**. Discount rates **as you supplied**. Short-term expedient elected. Shall I
> go ahead?*

On the upload path, name each file you received and say what was read from it: the lease, its term
and its payments, or the period and totals of a listing. Flag anything unreadable straight away.

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

## Stage 3 — Read the books, search for unrecorded leases, and confirm each lease

Pull the lease accounts and payments, search for unrecognised leases, then confirm there is a
lease and from whose side: [`references/method.md`](references/method.md) Steps 0–1, including
Step 0b.

## Stage 4 — Term, rate, classification and measurement

Lease term and payments, the discount rate, classification under ASC 842, initial measurement and
the schedules: [`references/method.md`](references/method.md) Steps 2–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for option judgments, variable payments,
lease against service, and modifications against reassessments.

## Stage 5 — Entries, changes, disclosures, and present

Periodic entries as **proposals**, reassessments and modifications, expedients, disclosures, then
the output: [`references/method.md`](references/method.md) Steps 7–11. Before presenting, check it
against [`references/output.md`](references/output.md). Ask whether the user wants the workpaper
as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 12. Persist the framework, the elected
expedients and each lease's terms and rate, with the date supplied.

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
