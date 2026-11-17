---
name: nonprofit-fund-accounting
description: "Handles accounting for a not-for-profit under ASC 958 or a local equivalent: classifies net assets by donor restriction, recognises contributions and grants, tracks and releases restrictions, accounts for endowments and in-kind gifts, allocates expenses by function, and builds the nonprofit statement set with the statement of functional expenses. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances and contribution records. Use when the user asks about nonprofit or charity accounting, net assets with and without donor restrictions, releasing restrictions, functional expense allocation, endowments, or nonprofit financial statements. Do not use for tracking one grant's budget and allowable costs (use grant-accounting-nonprofit-restricted-funds) or for a government body (use government-fund-accounting-gasb). Read-only: produces the statements, schedules and proposed entries, and posts nothing."
---

# Nonprofit accounting: who restricted what, and was it honoured

A charity's money mostly arrives with strings attached, and the accounts exist to show whether
those strings were honoured. So the statements are organised around **who restricted what**, and
expenses are shown by **function**: programmes, management, fundraising. This skill builds that
set.

**Works with or without Mosofin.** With Mosofin connected it reads contributions, expenses and net
asset balances, and checks whether the books separate restricted from unrestricted at all. Without
it, you upload the trial balance and contribution records and the method is the same.

**A donor's restriction is in the gift letter, not the ledger.** Conditions, stipulations and the
basis for splitting shared costs between functions come from you. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never decides that a gift is restricted, conditional or neither.** It asks, gift by gift where
  it matters.
- **Never invents an allocation basis for shared costs.**
- **Never releases a restriction without evidence that it was met.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–10" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which organisation and period, and which framework?* | Sets the scope | **Never default the period.** |
| **C** | *What are the programmes, and do the classes in the books represent programmes or functions?* | Decides whether the functional matrix can be read | **Ask again.** |
| **D** | *For each significant contribution: is it restricted, by purpose or by time, and is it conditional?* | Not in the ledger | Show contributions as received, and list the classification as not confirmed. |
| **E** | *How are shared costs split between programmes, management and fundraising?* | Time studies and floor area are not in the books | Show natural expenses only, with no functional split. |
| **F** | *Is there an endowment, and were there gifts in kind?* | Each has its own rules | Assume none, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report whether the chart of accounts separates net assets with and without donor restrictions.
- Report spending from restricted funds where no release was recorded.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance** at the opening and closing dates | Required | XLSX or CSV |
| **Contribution records**: donor, amount, date, restriction | Required | XLSX |
| **Expenses by natural class and by programme** | Required for the functional statement | XLSX or CSV |
| Grant agreements and the allocation basis | Recommended | PDF, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Preparing nonprofit statements for **Riverside Community Trust** for the **year to 30 June**
> under **ASC 958**, from **your Mosofin connection**. **Three programmes**, tracked as
> **classes**. Restrictions per **the gift schedule you uploaded**; shared costs split on **staff
> time**. No endowment. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the books and settle the structure

Pull the balances and activity, settle the two structural questions, then classify net assets:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Contributions, restrictions and functional expenses

Contributions and grants, tracking and release of restrictions, endowments, gifts in kind, and
functional allocation: [`references/method.md`](references/method.md) Steps 2–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for conditional gifts, pledges, restricted
funds spent before the restriction was met and underwater endowments.

## Stage 5 — Statements, disclosures, and present

The nonprofit statements and disclosures, then the output:
[`references/method.md`](references/method.md) Steps 7–9. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the framework, the programme
mapping and the allocation basis.

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
