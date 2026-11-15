---
name: grant-accounting-nonprofit-restricted-funds
description: "Tracks grants and restricted funds in detail: classifies each award as conditional or unconditional and by its restrictions, sets up tracking by grant, recognises revenue and releases restrictions as conditions are met, checks spending against the grant budget, period and allowable costs, and prepares the reporting calendar and proposed entries. Reads expenditures tagged to each grant through a connected Mosofin workspace when the user agrees, or works from uploaded award letters and spending data. Use when the user asks about grant accounting, restricted funds, allowable costs, a grant budget against actual, releasing restricted net assets, or funder reporting. Do not use for the nonprofit statement set as a whole (use nonprofit-fund-accounting) or for a company's budget variances (use budget-vs-actual-analysis). Read-only: produces grant schedules, proposed entries and a reporting calendar, and posts nothing."
---

# Grant accounting: keeping the strings visible

Money given for a purpose is not simply income. It comes with strings: spend it on this, by then,
and report how. This skill keeps those strings visible for **each grant**: what is still
restricted, what has been released, and whether the spending was allowed.

**Works with or without Mosofin.** With Mosofin connected it reads expenditure and receipts tagged
to each grant, which is the strongest input it has. Without it, you upload the award letters and
spending data and the method is the same.

**The award letter is the authority.** Whether a grant is conditional, what it restricts, the
budget by category, the allowable cost rules and the indirect rate are in the agreement, not the
books. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never decides that a grant is conditional or unconditional.** It asks whether there is a
  barrier and a right of return.
- **Never rules a cost allowable.** It compares spending with the rules supplied and reports
  exceptions.
- **Never releases more than the award.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which organisation, which grants and which period?* | Sets the scope | **Never default the period.** |
| **C** | *Can you supply the award letters: terms, restrictions, conditions, period, reporting?* | The core input | Report spending and receipts by grant only. |
| **D** | *For each grant: is it conditional, and what are its purpose and time restrictions?* | Decides when revenue is recognised and released | List recognition and release as not computed for that grant. |
| **E** | *What is each grant's budget by category, and what are the allowable cost rules and indirect rate?* | Needed for the compliance checks | Compare spending with the award total only. |
| **F** | *How do the dimensions in the books map to grants, and when are funder reports due?* | This is how spending is read by grant | **Ask again** for the mapping. Leave the calendar empty. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report spending tagged to a grant outside its period, and spending with no grant tag.
- Check that restricted net assets equal awards received less amounts released.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Award letters** | Required | PDF |
| **Spending and receipts by grant** | Required | XLSX or CSV |
| **Grant budgets** by category | Required for budget checks | XLSX |
| Allowable cost rules and indirect rate | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Tracking **four grants** at **Riverside Community Trust** for the **year to 30 June**, tagged
> by **class**, from **your Mosofin connection** and **the award letters you uploaded**. Two are
> **conditional**. Indirect costs at **the rate in each award**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the grant, its
period and its totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the activity and classify the funding

Pull spending and receipts by grant, then classify each award:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Set up tracking, recognise and release

The tracking structure, then revenue and restrictions:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for a condition confused with a
restriction, a government grant treated as a contribution, and release beyond the award.

## Stage 5 — Compliance, entries, and present

Allowable costs and compliance, the entries as **proposals**, then the output:
[`references/method.md`](references/method.md) Steps 4–6. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist each grant's terms, its dimension
mapping and its reporting dates.

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
