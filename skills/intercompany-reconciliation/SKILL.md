---
name: intercompany-reconciliation
description: "Reconciles intercompany balances between companies in the same group: builds the entity matrix, matches transactions on both sides, reconciles each pair, names the cause of every mismatch, handles currency differences, and proposes settlements and elimination entries. Lists any pair it could not reconcile because only one side was available. Reads each entity's ledger through a connected Mosofin workspace when the user agrees, or works from uploaded intercompany ledgers. Use when the user asks to reconcile intercompany accounts, find an intercompany mismatch, match intercompany receivables and payables, reconcile an intercompany loan, prepare elimination entries, or plan an intercompany settlement. Do not use for reconciling a balance sheet account to its support (use balance-sheet-reconciliations) or for a bank account (use bank-reconciliation). Read-only: produces the reconciliation, proposed entries and a coverage sheet, and posts nothing."
---

# Intercompany reconciliation: both sides of every pair

When companies in one group trade with each other, each transaction should appear twice: once in
each set of books, equal and opposite. This skill reads **both sides of every entity pair**,
matches them, explains each difference, and proposes **settlements and elimination entries**. A
person posts them.

**Works with or without Mosofin.** With Mosofin connected it reads every connected entity's ledger
in one batch, at the same moment, so there is no version skew between the sides. Without it, you
upload a ledger per entity and the method is the same.

**A pair needs both sides.** One entity's view of a balance is not the balance; it is the number
in question. Where a group member is not available, the pair is listed as **not reconciled**, with
the missing entity named. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** It cannot force a match by
  adjusting one side, and every entry is a proposal.
- **Never presents a single-sided figure as a reconciliation.**
- **Never supplies an FX rate, a transfer price or the cause of a mismatch.** Rates come from the
  user with their source and date; a cause is stated only where the evidence shows it.

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
| **B** | *Which companies are in the group, and is any member missing from what I can see?* | Decides which pairs can be reconciled at all | **Ask again.** A missing member turns its pairs into not reconciled. |
| **C** | *Which period?* | Sets every read and every cut-off | **Never default the period.** |
| **D** | *Which accounts are the intercompany accounts in each company, and how does each company name the others?* | The counterparty may be a customer, a vendor, a class or only a memo. This is the join | Propose the accounts and names found, and **wait for a yes.** |
| **E** | *What is the group reporting currency, and which FX rates apply? Give the table, its source and its dates.* | Separates a real difference from a rate difference | Reconcile cross-currency pairs in the transaction currency only, and say translation was not done. |
| **F** | *Is there an intercompany agreement: pricing method and payment terms?* | Several mismatch causes can only be judged against it | List those causes as not assessed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and **every group member by name**, and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Name every pair that cannot be reconciled, and why, before starting.
- Take each entity's functional currency and year-end from its company profile. Differing
  year-ends are confirmed with the user, never assumed away.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Intercompany ledger for each company**: date, reference, amount, currency and counterparty per transaction | Required, for **both** sides of every pair | XLSX or CSV |
| Intercompany account list for each company (D) | Required | Type it in the chat, or a chart of accounts export |
| FX rate table with source and dates (E) | Required for cross-currency pairs | XLSX, CSV or pasted |
| Intercompany agreement or policy (F) | Recommended | PDF or pasted |

**Read back before starting, then wait for a yes:**

> *Reconciling intercompany balances for **September** across **Northbrook Trading, Northbrook
> Logistics and Northbrook UK**, from **your Mosofin connection**. Reporting currency **USD**, rates
> from **the table you supplied**. **Northbrook Asia is not connected**, so its three pairs will be
> listed as not reconciled. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the company, the
period, the row count and the totals. Flag anything unreadable, or a pair with only one side,
straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and every
company file, check which read tools are enabled **per company**, and read each company profile,
so Stage 1's answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read both sides and build the entity matrix

Pull every entity's intercompany ledger in one batch, then lay out who owes whom:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Match, reconcile each pair, and explain the differences

Match transaction by transaction, reconcile the balance for each pair, identify the cause of each
mismatch, then handle currency: [`references/method.md`](references/method.md) Steps 2–5. An
unmatched item is a status, never forced. Check
[`references/edge-cases.md`](references/edge-cases.md) for intercompany loans, three-party flows,
withholding tax, intercompany dividends, differing year-ends and mismatches that persist.

## Stage 5 — Propose settlements and eliminations, and present

Settlement proposal, elimination entries as **proposals**, then the output and coverage sheet:
[`references/method.md`](references/method.md) Steps 6–8. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the pair structure, the
intercompany account map, the counterparty naming map and the known recurring causes. Every
balance, rate and mismatch is read again each period.

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
