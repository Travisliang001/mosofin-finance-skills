---
name: insurance-accounting-overview
description: "Maps the accounting close for an insurance business: settles whether the entity is a carrier, a managing general agent or a broker, then lays out the schedules and controls for premium and unearned premium, claims and loss reserves, reinsurance, acquisition costs and commissions, and investment income, with the close deliverables. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded close schedules. Use when the user asks how to close the books of an insurer, broker or agent, about unearned premium, loss reserves, reinsurance recoverables, deferred acquisition costs, or an insurance close checklist. Do not use for a company's own insurance prepayments (use prepaid-amortization-schedule) or for the general close (use month-end-close-checklist). Read-only: produces the close map, schedules tied to the ledger and a coverage sheet, and never estimates a reserve."
---

# Insurance close: money now, a promise about later

Insurance takes money now for a promise about later, so almost every number is an estimate about
events not yet finished. **Premium** is spread over the period it covers, **claims** are provided
for before their cost is known, and part of the risk is passed to reinsurers. This skill maps how
the close works and what evidence each part needs.

**Works with or without Mosofin.** With Mosofin connected it reads the premium, claims,
reinsurance and commission accounts and ties each schedule to the ledger. Without it, you upload
the close schedules and the method is the same.

**The business model decides everything.** A carrier, an agent and a broker have different books.
Policy and claims data live in their own systems, and **loss reserves come from the actuary, never
from here**. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never estimates a loss reserve or incurred-but-not-reported claims.** Those are actuarial.
- **Never assumes the business model.** It asks first.
- **Never treats a reserve balance as evidence that the reserve is adequate.**
- **Never recomputes unearned premium from the ledger alone.** It needs the policy data.

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
| **B** | *Which entity and period, and is it a carrier, a managing general agent or a broker?* | Decides everything below | **Ask again.** |
| **C** | *Is the entity regulated, and under which regime?* | Decides whether client money rules apply | List regulatory items as not assessed. |
| **D** | *Can you supply the premium and claims data from the policy and claims systems?* | Not in the accounting system | Tie the ledger to last period's schedules only, and say so. |
| **E** | *What reinsurance is in place: treaties, cessions, recoverables?* | Contracts | Show reinsurance balances as recorded, with no test against terms. |
| **F** | *Who is the actuary and how often is the valuation done? Do you have last close's schedules?* | Reserves and the opening positions | List reserves as recorded, not assessed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report whether the accounts found match the business model stated, such as reserve accounts in a
  broker's books.
- Read back the business model for each company file.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Premium and policy data** for the period | Required for a carrier or agent | XLSX or CSV |
| **Claims data** and the actuary's reserve report | Required for a carrier | XLSX and PDF |
| **Reinsurance terms** | Recommended | PDF |
| **Prior close schedules** | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Mapping the close for **Harbour Mutual**, a **carrier**, for **September**, from **your Mosofin
> connection** and **the policy and claims extracts you uploaded**. Regulated; reserves from **the
> actuary's quarterly report**. One quota share treaty. Shall I go ahead?*

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

## Stage 3 — Read the accounts and settle the model

Pull the insurance accounts, then settle the business model and what the accounts show:
[`references/method.md`](references/method.md) Steps 0–0b.

## Stage 4 — Work through the five areas

Premium and unearned premium, claims and loss reserves, reinsurance, acquisition costs and
commissions, and investment income: [`references/method.md`](references/method.md) sections 1–5.
Check [`references/edge-cases.md`](references/edge-cases.md) for losses shown net of reinsurance
only, a recoverable treated as cash, and commissions.

## Stage 5 — Close deliverables, and present

The close deliverables, then the output: [`references/method.md`](references/method.md) Steps 6–7.
Before presenting, check it against [`references/output.md`](references/output.md). Ask whether
the user wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the business model, the regime and
the account mapping.

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
