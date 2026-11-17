---
name: pensions-and-postretirement-asc715
description: "Turns an actuarial report for a defined benefit pension or other postretirement plan into the accounting under ASC 715 or IAS 19: identifies the plan and its components, rolls the obligation and plan assets forward, determines funded status and the net periodic cost, and proposes the journal entries and disclosures. Compares what the books recorded with what the report says. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded actuarial report. Use when the user asks about defined benefit pension accounting, funded status, net periodic benefit cost, actuarial gains and losses, or pension disclosures. Do not use for defined contribution plans such as a 401(k) (use benefits-and-401k-accounting). Read-only: produces the roll-forwards and proposed entries from the actuary's figures, and never supplies an assumption."
---

# Defined benefit pensions: from the actuary's report to the books

A defined benefit plan promises people an income after they retire. What that promise is worth
today depends on assumptions about lifespans, pay and returns, which is why an **actuary** works
it out. The accounting job is turning the actuary's answer into the books correctly. This skill
does that and proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads the pension liability, the
amounts in other comprehensive income and the contributions paid, and compares them with the
report. Without it, you upload the report and the method is the same.

**Everything flows from the actuarial report.** The obligation, the plan assets, the discount rate
and every other assumption come from it, never from the books and never from memory. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never supplies a discount rate or any actuarial assumption.**
- **Never computes the obligation.** With no report, nothing is measured.
- **Never treats a defined contribution plan as a defined benefit plan.** The plan type is
  confirmed first.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–8" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, which plan, and which period end?* | Sets the scope | **Never default the period.** |
| **C** | *Is this a defined benefit plan, and ASC 715 or IAS 19?* | The two differ on expected return and net interest | **Ask again.** A defined contribution plan is out of scope. |
| **D** | *Can you supply the actuarial valuation report, and what is its measurement date?* | Everything flows from it | **Blocking.** Report the balances in the books only. |
| **E** | *Were there plan amendments, curtailments or settlements?* | Amendments create prior service cost and are easy to miss | Assume none, and **say that you assumed it.** |
| **F** | *Do you have last year's roll-forwards?* | The opening position | Open from the balances in the books, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report whether any pension entry was posted in the period, and whether the recorded liability
  equals the funded status in the report.
- Check that the measurement date agrees with the reporting date.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Actuarial valuation report** at the period end | Required | PDF |
| **Prior year roll-forwards** | Recommended | XLSX |
| **Ledger detail** for the pension liability, other comprehensive income and contributions | Recommended | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Accounting for the **staff pension plan** of **Northbrook Trading** at **31 December** under
> **ASC 715**, from **the actuary's report dated 20 January, measured at 31 December**, and the
> ledger in **your Mosofin connection**. No amendments in the year. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the report's date,
author and key figures. Flag anything unreadable straight away.

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

## Stage 3 — Read the books and compare with the report

Pull the pension balances, compare what was recorded with the report, then identify the plan and
its components: [`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Roll forward, funded status and cost

The obligation and plan asset roll-forwards, funded status, and the net periodic cost:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for a multi-employer plan, no pension entry
posted at all, and contributions that differ from the report.

## Stage 5 — Entries, disclosures, and present

The entries as **proposals**, the disclosures, then the output:
[`references/method.md`](references/method.md) Steps 5–7. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the plan type, the framework and
the account mapping. Every figure comes from the next report.

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
