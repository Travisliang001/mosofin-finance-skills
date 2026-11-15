---
name: statement-of-equity-changes
description: "Builds the statement of changes in equity: tests every movement in an equity account for a legitimate source, identifies the components for the entity type, rolls each one forward from opening to closing balance, details each movement, rolls forward the share counts from the cap table the user supplies, ties out to the balance sheet and income statement, and adds the comparative period. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances and equity ledger detail. Use when the user asks for a statement of changes in equity or stockholders' equity, a retained earnings roll-forward, an equity roll-forward, or why equity moved. Do not use for the full statement set (use financial-statement-builder) or for the year-end closing entries (use closing-entries-and-trial-balance). Read-only: produces the statement, its tie-outs and a coverage sheet, and posts nothing."
---

# Statement of changes in equity: every movement, explained

Rolls **every equity component** forward from its opening balance to its closing balance: net
income, other comprehensive income, contributions, distributions and share transactions. First it
checks that each movement has a legitimate source. A person reviews and issues the statement.

**Works with or without Mosofin.** With Mosofin connected the amounts are read from the equity
accounts, movement by movement. Without it, you upload the trial balances and the equity ledger
detail and the method is the same.

**The amounts are in the books. The shares are not.** Share counts by class come from the cap
table, which you supply. And most of the tie-outs hold by construction, so the real test is the
source of each movement, not whether the totals agree. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never invents a share count.** With no cap table, the share roll-forward is listed as not
  done.
- **Never lets an unexplained entry to equity pass as a normal movement.** It is listed with its
  amount and asked about.
- **Never treats a tie-out that holds by construction as evidence.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, which period, and which comparative?* | Sets the opening and closing dates | **Never default the period.** |
| **C** | *What type of entity: corporation, partnership, LLC, sole proprietor or nonprofit? Which framework?* | Decides the components | **Ask again.** |
| **D** | *What are the share counts by class, opening and each movement?* | The cap table is never in the books | Build the amounts only, and list the share roll-forward as not done. |
| **E** | *What explains any unusual movement in equity this period?* | A direct entry to equity needs a reason | List each one as unexplained, with its amount. |
| **F** | *Is treasury stock at cost or par, and what were the dividend dates and per-share amounts?* | Both change the detail shown | Show treasury stock as recorded, and dividends in total only. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the movements in equity that have no obvious source before the interview, so the user can
  explain them.
- Confirm the equity accounts by name and which component each belongs to.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance** at the opening and closing dates | Required | XLSX or CSV |
| **Ledger detail for every equity account** for the period | Required | XLSX or CSV |
| **Cap table** with movements | Required for the share roll-forward | XLSX |
| Net income and other comprehensive income for the period | Required for the tie-out | XLSX or PDF |

**Read back before starting, then wait for a yes:**

> *Building the statement of changes in equity for **Northbrook Trading**, a **corporation** under
> **US GAAP**, for the **year to 31 December** with the prior year as comparative, from **your
> Mosofin connection** and **the cap table you uploaded**. Treasury stock at **cost**. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the dates, the
accounts and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Test each movement, then identify the components

Every movement in equity tested for a legitimate source, then the components for this entity type:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Build the roll-forward and the movement detail

The roll-forward grid, the detail of each movement, and the share counts:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for stock splits, conversions, share-based
payment, a new accounting standard, and distributions in excess of capital.

## Stage 5 — Tie out, add the comparative, and present

The tie-outs, the comparative period, then the output:
[`references/method.md`](references/method.md) Steps 5–7. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the entity type, the
component mapping and the treasury stock method.

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
