---
name: due-diligence-quality-of-earnings
description: "Performs financial due diligence on a target: validates the base numbers, builds the bridge from reported to adjusted EBITDA with each adjustment evidenced, tests whether one-time items recur, assesses revenue quality, working capital with a normal level, net debt and debt-like items, maintenance against growth capex, and the forecast, and lists the risks. Reads the target's books through a connected Mosofin workspace when the user agrees and the target is connected, or works from the data room files the user uploads. Use when the user asks for quality of earnings, adjusted or normalised EBITDA, a working capital peg, net debt for a deal, or financial due diligence. Do not use for valuing the business (use business-valuation) or for freeing cash from working capital in your own company (use working-capital-optimization). Read-only: produces analysis for the deal team, not an audit and not investment advice."
---

# Quality of earnings: what the business really earns

Before a business is bought, sold or refinanced, someone asks whether the **reported earnings are
the real, repeatable earnings**. This skill validates the numbers, builds the bridge to **adjusted
EBITDA**, and assesses revenue quality, working capital, net debt and capex.

**Works with or without Mosofin.** With Mosofin connected to the target's books, the ledger behind
every adjustment is read. Without it, you upload the data room files and the method is the same.

**Depth depends on access to the ledger.** Without it this is a review of management's figures and
says so. Contracts, the seller's adjustments and related party arrangements come from you. **It is
analysis for the deal team, not an audit and not investment advice.** Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Not an audit, and not a recommendation to buy, sell or lend.**
- **Never accepts a management adjustment without evidence**, and treats adjustments the same way
  in both directions.
- **Never calls an item one-time that recurs.** The recurrence test is run first.
- **Never sets the working capital peg.** It shows the average, the seasonality and the methods.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–11" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which target, and is this buy-side, sell-side or refinancing?* | Sets the lens | **Ask again.** |
| **C** | *What is the cut-off date for the last twelve months, and which years are covered?* | Sets every read | **Never default it.** |
| **D** | *Do you have the ledger and trial balances, or only the statements?* | Decides how deep the work can go | Review at statement level, and say so on the first page. |
| **E** | *What adjustments has management proposed?* | The starting bridge to test | Build the bridge from the books alone. |
| **F** | *Who are the related parties, and what are the owner's arrangements?* | Essential in a private company | List owner costs and related party items as not identified. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say whether the target's books are connected, or only the acquirer's.
- Report items labelled one-time that appear in more than one year.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Financial statements**, three years plus the last twelve months | Required | XLSX or PDF |
| **Trial balances and ledger** | Required for depth | XLSX or CSV |
| **Management's adjusted EBITDA bridge** | Recommended | XLSX |
| Monthly working capital and the debt schedule | Required for those sections | XLSX |

**Read back before starting, then wait for a yes:**

> *Buy-side quality of earnings on **Harlow Fabrication** for **three years and the twelve months
> to 30 September**, from **the data room files you uploaded**, with the ledger. Management
> proposes **six adjustments**. Owner arrangements as you described. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the periods and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the evidence, set the lens and validate the base

Pull the figures, define the scope, then validate the base numbers:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Adjusted EBITDA, revenue quality and working capital

The bridge and the recurrence test, revenue quality, then working capital:
[`references/method.md`](references/method.md) Steps 3–5, including Step 3b. Check
[`references/edge-cases.md`](references/edge-cases.md) for aggressive add-backs, owner pay,
related party transactions and peg disputes.

## Stage 5 — Net debt, capex, forecast, risks, and present

Net debt and debt-like items, capex, the forecast, the risks, then the output:
[`references/method.md`](references/method.md) Steps 6–10. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the scope and the definitions
used. **Target data is not saved.**

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
