---
name: foreign-currency-translation-asc830
description: "Translates foreign subsidiaries into the reporting currency under ASC 830 or IAS 21: determines each entity's functional currency, remeasures transactions in other currencies, translates the financial statements, proves the cumulative translation adjustment independently instead of treating it as a balancing figure, handles intercompany loans, and proposes the entries and controls. Reads each entity through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances and a rate table. Use when the user asks to translate a foreign subsidiary, about the cumulative translation adjustment, functional currency, remeasurement, or ASC 830 or IAS 21. Do not use for period-end revaluation of foreign balances in one company (use multicurrency-fx-revaluation) or for the full group consolidation (use consolidation-and-eliminations). Read-only: produces the translation, the proof and proposed entries, and never supplies a rate."
---

# Currency translation: a foreign subsidiary in the group's currency

If part of a group earns and spends in one currency and the accounts are published in another, its
statements have to be **translated**. The difference that arises goes to equity as the
**cumulative translation adjustment**. This skill does the translation, **proves that adjustment
independently**, and proposes the entries. A person posts them.

**Works with or without Mosofin.** With Mosofin connected each entity's trial balance is read in
its own currency, with its home currency on record. Without it, you upload the trial balances and
the method is the same.

**The translation adjustment is a balancing figure, so a wrong rate does not fail to balance. It
lands there unseen.** That is why it is proved separately. **Every rate comes from you**,
including the historical rates for equity, which are the hardest to obtain. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never supplies a rate from memory**, and never reuses one from an earlier run.
- **Never accepts the translation adjustment because the statements balance.** It is proved.
- **Never decides the functional currency**, and never assumes it equals the home currency on
  record without asking.
- **Never approximates a historical rate without saying so.**

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
| **B** | *Which entities, and what currency does the group report in?* | Decides which entities need translating at all | **Ask again.** |
| **C** | *Which period end?* | Sets the closing rate date | **Never default the period.** |
| **D** | *What are the rates: closing, average and historical, with source and dates?* | A rate is never taken from the skill | **Blocking.** List what needs translating; compute nothing. |
| **E** | *What is each entity's functional currency, and does it agree with the currency its books are kept in?* | When they differ, remeasurement comes first | Use the home currency on record and **wait for a yes.** |
| **F** | *Are there intercompany loans, and are any designated as long-term investments? Is any entity in a hyperinflationary economy?* | Decides whether differences go to earnings or to equity, and can change the method | Treat loans as not designated, assume no hyperinflation, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and each company file **by name, with its home currency**, and wait for
  an explicit yes (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Flag any entity whose home currency differs from the functional currency given.
- Say which equity balances need a historical rate, so the user knows what to find.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance of each foreign entity**, in its own currency | Required | XLSX or CSV |
| **Rate table**: closing, average and historical, with source and dates | Required | XLSX or pasted |
| **Prior period translated balances** and the adjustment brought forward | Required for the proof | XLSX |
| Intercompany loan list with designations | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Translating **Northbrook UK** from **GBP** into **USD** at **31 December**, from **your Mosofin
> connection**, at the **rates you supplied, sourced from your bank**. Functional currency
> **GBP**, as on record. **One intercompany loan**, not designated as long-term. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the entity, its
currency, the date and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read each entity and settle the functional currency

Pull each trial balance in its own currency, then confirm the functional currency:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Remeasure, translate, and prove the adjustment

Remeasurement of transactions, translation of the statements, then the independent proof:
[`references/method.md`](references/method.md) Steps 2–3b. Check
[`references/edge-cases.md`](references/edge-cases.md) for hyperinflation, an average rate that
misstates a seasonal result, equity translated at the closing rate, and intercompany balances that
disagree before translation.

## Stage 5 — Intercompany, entries, controls, and present

Intercompany and consolidation points, the entries as **proposals**, the controls, then the
output: [`references/method.md`](references/method.md) Steps 4–6b. Before presenting, check it
against [`references/output.md`](references/output.md). Ask whether the user wants the workpaper
as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the functional currency
conclusions, the loan designations and the historical rates already agreed for equity. **Never a
current rate.**

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
