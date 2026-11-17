---
name: related-party-disclosures-asc850
description: "Prepares related party disclosures under ASC 850 or IAS 24: takes the list of related parties from the user, runs completeness procedures against the vendor, customer and employee records, compiles every transaction and balance with each related party from the books, drafts the disclosures, and sets out the controls. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded ledgers and a related party list. Use when the user asks for related party disclosures, a list of related party transactions, a related party completeness check, or balances with directors, shareholders or affiliates. Do not use for intercompany matching (use intercompany-reconciliation) or for the notes as a whole (use notes-to-financial-statements). Read-only: produces the schedules and draft disclosure, collects only what the standard requires, and posts nothing."
---

# Related parties: who they are, and what passed between you

A related party disclosure has two halves. **Who is a related party**: owners, directors, key
management, their close family and their businesses. And **what passed between you**: transactions
and balances. This skill compiles the second from the books, once you have supplied the first.

**Works with or without Mosofin.** With Mosofin connected every transaction and balance with a
named party is read, and names are matched against the vendor, customer and employee records.
Without it, you upload the ledgers and the method is the same.

**The books cannot tell you who is related.** Ownership, board membership and family ties are not
ledger fields. A name match is a lead, not a finding. And this skill collects only the personal
detail the standard asks for. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never decides that someone is a related party.** It shows the lead and asks.
- **Never collects personal information beyond what the standard requires**, and saves no family
  detail.
- **Never judges whether a transaction was at arm's length.**
- **Never treats no transactions as no disclosure.** A relationship can need disclosing on its
  own.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–5" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and ASC 850 or IAS 24?* | The two differ on key management and close family | **Never default the period.** |
| **C** | *Who are the related parties: owners, directors, officers, affiliates, and the family members the framework requires?* | This is the universe, and it is never in the books | **Ask again.** Run name-matching leads only, and say so. |
| **D** | *What changed since last time: board joiners and leavers, new subsidiaries, share transfers?* | A party can be related for part of the year | Assume no change, and **say that you assumed it.** |
| **E** | *Are there guarantees, or transactions at no charge?* | Neither leaves a normal trace in the ledger | List both as not confirmed. |
| **F** | *Who may see the output?* | It names individuals | **Ask again.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report name and address matches between the related party list and the vendor, customer and
  employee records as leads.
- Read the saved profile for the list of entities, and ask what changed.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Related party list** | Required | XLSX, or type it in the chat |
| **Vendor and customer transaction detail** for the period | Required | XLSX or CSV |
| **Period-end receivable and payable balances** by party | Required | XLSX or CSV |
| Prior year disclosure | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing related party disclosures for **Northbrook Trading** for the **year to 31 December**
> under **ASC 850**, from **your Mosofin connection**, against **the list of eleven parties you
> supplied**. One director joined in **June**. Output to **you and the CFO only**. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
party count and the totals. Flag anything unreadable straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Define the related party universe

The list of related parties under the framework: [`references/method.md`](references/method.md)
Step 1.

## Stage 4 — Test completeness and compile transactions

Completeness procedures, then every transaction and balance by party:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for a party related for part of the year,
common control without ownership, a transaction at no charge and a guarantee.

## Stage 5 — Draft disclosures, controls, and present

The draft disclosures and the controls, then the outputs:
[`references/method.md`](references/method.md) Steps 4–5 and *Outputs*. Before presenting, check
the coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether
the user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the list of related
entities and the framework. **No personal or family detail is saved.**

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
