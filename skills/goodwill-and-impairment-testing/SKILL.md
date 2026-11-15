---
name: goodwill-and-impairment-testing
description: "Tests goodwill, indefinite-lived intangibles and long-lived assets for impairment under US GAAP or IFRS: scopes what must be tested from the balance sheet, identifies the unit of account, screens for triggering events, sets out the qualitative assessment, runs the quantitative test on the cash flows and discount rate the user supplies, and proposes the impairment entry and disclosures. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded carrying amounts and projections. Use when the user asks about a goodwill impairment test, triggering events, recoverable amount, value in use, or whether an asset is impaired. Do not use for the purchase accounting that created the goodwill (use business-combinations-asc805) or for inventory write-downs (use inventory-obsolescence-and-reserve). Read-only: produces the test and a proposed entry, concludes on no impairment, and supplies no cash flow or discount rate."
---

# Impairment testing: is the asset still worth its carrying amount?

An asset cannot be carried at more than it is worth. Goodwill is tested every year; other assets
when something suggests a problem. This skill scopes **what must be tested**, screens for
triggers, and runs the test on the projections and rate you supply.

**Works with or without Mosofin.** With Mosofin connected the carrying amounts, the impairment
history and two of the trigger indicators are read. Without it, you upload the carrying amounts
and the method is the same.

**The test rests on a forecast and a discount rate, and both are yours.** So is the allocation of
goodwill to units. The two frameworks work differently, so the framework is asked first.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never fabricates cash flows or a discount rate.**
- **Never concludes that an asset is or is not impaired.** It shows the comparison and the
  sensitivity.
- **Never reverses an impairment under US GAAP**, and never reverses goodwill impairment under
  either framework.
- **Never allocates goodwill to units for the user.**

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
| **B** | *Which entity and test date, and US GAAP or IFRS?* | The mechanics diverge | **Ask again.** |
| **C** | *What is being tested, and what is the unit of account?* | Reporting units or cash-generating units | Propose from the dimensions in the books, and **wait for a yes.** |
| **D** | *How is goodwill allocated to units, and on what basis?* | Not in the ledger | **Blocking** for the goodwill test. |
| **E** | *What are the cash flow projections and the discount rate, and is the rate pre-tax or post-tax?* | Never supplied here | **Blocking** for the quantitative test. Run the trigger screen only. |
| **F** | *Have there been triggering events?* | Most are outside the books | Report the two readable indicators, and list the rest as not assessed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report what the balance sheet says must be tested, before the interview.
- Report prior impairments, which limit any reversal.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Carrying amounts** by unit | Required | XLSX |
| **Cash flow projections** | Required for the quantitative test | XLSX |
| **Discount rate** with its derivation | Required | PDF or XLSX |
| Market data for the market approach | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Testing goodwill for **Northbrook Trading** at **31 December** under **US GAAP**, across **two
> reporting units**, with goodwill allocated **as you supplied**, from **your Mosofin connection**
> and **the projections and post-tax rate you uploaded**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the unit, the date
and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the books and scope the test

Pull the balances, scope from the balance sheet, then the asset and the framework:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Triggers, qualitative assessment and the test

Triggering events, the optional qualitative assessment, then the quantitative tests:
[`references/method.md`](references/method.md) Steps 2–7. Check
[`references/edge-cases.md`](references/edge-cases.md) for goodwill allocation, sensitivity to the
rate and growth, and market value below book value.

## Stage 5 — Reversal, entry, disclosures, and present

Reversal where the framework allows, the entry as a **proposal**, disclosures, then the output:
[`references/method.md`](references/method.md) Steps 8–11. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 12. Persist the framework, the units and the
goodwill allocation.

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
