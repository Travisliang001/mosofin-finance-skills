---
name: government-fund-accounting-gasb
description: "Handles accounting for state and local governments and similar public bodies under GASB or IPSAS: establishes the basis the books are kept on and whether funds are a dimension, identifies the fund structure, applies the right measurement basis to each fund type, builds the fund statements with fund balance classifications, builds the government-wide statements and the reconciliation between the two, and determines major funds. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances by fund. Use when the user asks about governmental fund accounting, modified accrual, fund balance classification, government-wide statements, major fund determination, or GASB or IPSAS reporting. Do not use for a charity (use nonprofit-fund-accounting) or for a company's statements (use financial-statement-builder). Read-only: produces the statements, reconciliations and a coverage sheet, and posts nothing."
---

# Government fund accounting: many pots, reported twice

A government does not have one set of books. It has many, **one per pot of money**, each with
rules about what it may be spent on. And it reports twice: fund by fund, and for the government as
a whole. This skill builds both views and the reconciliation between them.

**Works with or without Mosofin.** With Mosofin connected it reads balances by fund where funds
are a dimension in the books. Without it, you upload a trial balance per fund and the method is
the same.

**Two things must be settled first: the basis the books are kept on, and whether funds exist as a
dimension.** Constraints on fund balance, capital asset and debt registers, and actuarial reports
for pensions are never in the ledger. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never assumes the basis of accounting.** Nothing downstream can be read without it.
- **Never classifies fund balance without the constraint behind it.**
- **Never fabricates a pension or OPEB figure.** Those come from the actuarial report.
- **Never states a current standard from memory as settled.** They change often.

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
| **B** | *Which entity, which fiscal year, and GASB, IPSAS or another framework?* | Sets the scope | **Never default the period.** |
| **C** | *On which basis are the books kept: cash, modified accrual or full accrual?* | Everything else is read through it | **Ask again.** |
| **D** | *Which funds are in use, of which types, and how are they tagged in the books?* | The fund structure | Propose the mapping from the dimensions found, and **wait for a yes.** |
| **E** | *What constrains each fund balance: external restrictions, board commitments, assignments?* | Nothing in a ledger records it | Show fund balance in total, unclassified. |
| **F** | *Can you supply the capital asset and debt registers and the pension actuarial reports?* | Needed for the government-wide view | Build the fund statements only, and list the government-wide view as not done. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say whether a fund dimension exists. Without one, balances by fund must be supplied.
- Say which other connected files may be component units.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance by fund** | Required | XLSX or CSV |
| **Budget** by fund | Recommended | XLSX |
| **Capital asset and long-term debt registers** | Required for government-wide statements | XLSX |
| Pension and OPEB actuarial reports | Required where applicable | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing statements for **Millbrook Township** for the **year to 30 June** under **GASB**,
> from **your Mosofin connection**. Books on **modified accrual**; **six funds** tagged by
> **class**. Constraints as you listed; registers and the actuarial report **uploaded**. Shall I
> go ahead?*

On the upload path, name each file you received and say what was read from it: the fund, the
period and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the books and settle the basis and the funds

Pull the balances, establish the basis and the fund dimension, then identify the fund structure:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Measurement, fund statements and fund balance

The measurement basis per fund type, the fund statements, and fund balance classifications:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for the availability period for revenue,
nonexchange transactions, component units and internal service funds.

## Stage 5 — Government-wide view, major funds, and present

The government-wide statements, special items, major fund determination, disclosures, then the
output: [`references/method.md`](references/method.md) Steps 5–9, including Step 6b. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the framework, the basis, the fund
mapping and the constraints, with the date supplied.

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
