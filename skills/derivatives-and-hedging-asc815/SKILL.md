---
name: derivatives-and-hedging-asc815
description: "Supports accounting for derivatives and hedges under ASC 815 or IFRS 9: inventories the instruments, checks whether hedge accounting was elected and documented at inception, records the fair values the user supplies, sets out effectiveness testing, proposes the journal entries, and prepares disclosures and controls. Runs checks on the books for settlements with no recorded instrument and for amounts left in other comprehensive income. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded contracts and valuations. Use when the user asks about derivative accounting, an interest rate swap, a forward or option, hedge accounting, hedge documentation, effectiveness testing, or ASC 815. Do not use for period-end revaluation of foreign balances (use multicurrency-fx-revaluation) or for loan covenants (use debt-and-covenant-tracking). Read-only: produces schedules and proposed entries, and never values an instrument."
---

# Derivatives and hedging: the instrument, the designation, the value

A derivative goes on the balance sheet at fair value. **Hedge accounting** is an election that
changes where the gains and losses go, and it only applies if the hedge was designated and
documented at the start. This skill inventories the instruments, checks the designation, records
the values you supply and proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads the derivative balances,
settlements and amounts in other comprehensive income, and checks them against each other. Without
it, you upload the contracts and valuations and the method is the same.

**The contracts, the valuations and the hedge documentation are never in the books.** A recorded
balance is not a current valuation, and hedge accounting is never assumed. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never values a derivative**, and never takes a recorded balance as a current value.
- **Never assumes hedge accounting applies.** It is elective and needs documentation dated at
  inception.
- **Never concludes that a hedge is effective.** It sets out the test and the inputs.

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
| **B** | *Which company and reporting date?* | Sets the valuation date | **Never default it.** |
| **C** | *What derivatives are held: type, notional, dates, counterparty?* | The instruments themselves | List what the books suggest as leads, and ask. |
| **D** | *Is hedge accounting applied, and what are the designation date and documentation for each relationship?* | Without both, changes in value go to earnings | Treat every derivative as not designated, and say so. |
| **E** | *What is each instrument's fair value at the reporting date, from whom and by what method?* | Never computed here | **Blocking** for that instrument. |
| **F** | *What are the hedged items, and is any forecast transaction no longer expected?* | Decides what stays in other comprehensive income | Report amounts in other comprehensive income as not assessed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report settlements with no recorded instrument, and amounts sitting in other comprehensive
  income with no live hedge.
- Say which entity holds each instrument and each hedged item.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Derivative confirmations** or a summary of terms | Required | PDF or XLSX |
| **Valuations** at the reporting date, with source and method | Required | PDF |
| **Hedge documentation** and the prior period memo | Required if hedge accounting applies | PDF |
| **Ledger detail** for derivative and related accounts | Recommended | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Accounting for **one interest rate swap** at **Northbrook Trading** at **31 December** under
> **ASC 815**, from **the confirmation and bank valuation you uploaded** and the ledger in **your
> Mosofin connection**. Designated as a **cash flow hedge of the term loan**, documented **at
> inception**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the instrument, its
terms and its value. Flag anything unreadable straight away.

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

## Stage 3 — Read the books, run the checks and inventory the instruments

Pull the balances, run the three checks, then inventory the instruments and their scope:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Designation, value and effectiveness

Hedge designation and documentation, the fair values supplied, and effectiveness testing:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for documentation dated after inception, an
embedded derivative, and a counterparty's mark as the only valuation.

## Stage 5 — Entries, disclosures, controls, and present

The entries as **proposals**, the disclosures and controls, then the outputs:
[`references/method.md`](references/method.md) Steps 5–6 and *Outputs*. Before presenting, check
it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the instrument inventory and each
designation with its date. Values are supplied again every period.

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
