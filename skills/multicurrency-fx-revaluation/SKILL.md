---
name: multicurrency-fx-revaluation
description: "Handles foreign-currency accounting at period end: confirms each entity's functional currency, separates transaction differences from translation, revalues monetary balances at the closing rate, splits realised from unrealised gains and losses, translates foreign operations with the translation adjustment in equity, and proposes the revaluation entries and disclosures. Checks first whether the accounting system already revalues on its own, so nothing is counted twice. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded foreign-currency balances and a rate table. Use when the user asks about FX revaluation, unrealised or realised FX gains and losses, foreign-currency receivables or payables at period end, translating a foreign subsidiary, or the cumulative translation adjustment. Do not use for intercompany mismatches (use intercompany-reconciliation) or for building a general journal entry (use journal-entry-builder). Read-only: proposes entries for a person to post, and never supplies an exchange rate."
---

# FX revaluation: what foreign balances are worth at period end

Money owed in another currency changes value every day. At period end the balances still held are
restated at the closing rate, and the difference is a gain or loss. Converting a whole foreign
subsidiary into the group's currency is a separate job with a different destination. This skill
does both and proposes the entries. A person posts them.

**Works with or without Mosofin.** With Mosofin connected it reads each entity's home currency,
the foreign-currency balances where the system tags them, and the gains and losses already
recorded. Without it, you upload the balances and the method is the same.

**Two things decide whether this can be done at all.** Whether the system **tags balances by
currency**; if not, they cannot be revalued from the books. And whether the system **already
revalues on its own**; if it does, a second entry counts the difference twice. **Every rate comes
from you**, with its source and date. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal.
- **Never supplies an exchange rate**, and never reuses one from an earlier run.
- **Never proposes a revaluation entry before checking whether the system already posted one.**
- **Never revalues a non-monetary balance**, and never decides the functional currency for the
  user.

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
| **B** | *Which company or companies, and which period end?* | Sets the balances and the closing date | **Never default the period.** |
| **C** | *What are the rates: closing, average and transaction-date, with their source and dates?* | A rate is never taken from the skill | **Blocking.** List the foreign balances; compute nothing. |
| **D** | *What is each entity's functional currency, and what is the presentation currency?* | The home currency in the system usually agrees, and when it does not everything changes | Use the home currency on record and **wait for a yes.** |
| **E** | *Does your accounting system revalue automatically, and has it run for this period?* | Prevents double counting | Check the books for revaluation entries, and **ask again before proposing one.** |
| **F** | *US GAAP or IFRS? Any hedges, and which accounts are monetary?* | Decides treatment at the edges | Ask for the framework. Propose the monetary classification and wait for a yes. Assume no hedges, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and each company file **by name, with its home currency**, and wait
  for an explicit yes (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say whether balances are tagged by currency. Where they are not, say that revaluation needs the
  balances supplied.
- Flag any entity whose home currency differs from the functional currency given.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Foreign-currency balances** at the period end: account, currency, foreign amount, booked amount | Required | XLSX or CSV |
| **Rate table**: closing, average and transaction-date rates, with source and dates | Required | XLSX, CSV or pasted |
| **FX gain and loss account detail** for the period | Required to check for entries already posted | XLSX or CSV |
| **Trial balance of each foreign operation** | Required for translation | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Revaluing foreign-currency balances for **Northbrook Trading** at **30 September**, from **your
> Mosofin connection**, at the **rates you supplied from your bank, dated 30 September**.
> Functional currency **USD**; under **US GAAP**; the system **does not** revalue automatically.
> No hedges. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
currencies and the totals. Flag anything unreadable, or a rate with no date, straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and
every company file, check which read tools are enabled, and read each company profile, so
Stage 1's answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the balances and establish the ground rules

Pull the balances and recorded gains and losses in one batch, establish how the system tags
currency and whether it revalues, then confirm the functional currency:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Transaction differences and translation

Separate transaction differences from translation, account for the transaction level, then
translate foreign operations: [`references/method.md`](references/method.md) Steps 2–4, with
Steps 5–6 where hyperinflation or hedging applies. Check
[`references/edge-cases.md`](references/edge-cases.md) for monetary against non-monetary items,
intercompany balances, disposal of a foreign operation and a change of functional currency.

## Stage 5 — Propose entries, disclosures, and present

The revaluation entries as **proposals**, the disclosures, then the output:
[`references/method.md`](references/method.md) Steps 7–9. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the monetary classification, the
functional currencies and whether the system revalues. **Never a rate.**

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
