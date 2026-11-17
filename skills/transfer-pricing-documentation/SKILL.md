---
name: transfer-pricing-documentation
description: "Supports transfer pricing documentation for a group: maps the intercompany transactions from the books, records the functional analysis the user supplies and checks it against where costs and people actually sit, sets out method selection and the tested party, lays out benchmarking against comparables the user provides, flags a loss-making tested party, and assembles the documentation and the list of intercompany agreements. Reads intercompany flows through a connected Mosofin workspace when the user agrees, or works from uploaded data. Use when the user asks about transfer pricing documentation, a local file or master file, intercompany pricing support, or a benchmarking study outline. Do not use for matching intercompany balances (use intercompany-reconciliation) or for consolidation (use consolidation-and-eliminations). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# Transfer pricing: showing that group prices are arm's length

When companies in a group trade with each other, tax authorities ask whether the price is what
independent parties would have agreed. The answer is a **documented study**. This skill maps the
transactions from the books, records your functional analysis, and assembles the documentation.

**Works with or without Mosofin.** With Mosofin connected the intercompany flows are read, and the
characterisation of each entity is checked against where costs actually sit. Without it, you
upload the data and the method is the same.

**The analysis and the comparables are yours.** Functions, assets and risks, intercompany
agreements, local documentation rules and comparable data are not in the books. **The output is a
draft for a qualified transfer pricing professional, not advice.** Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system, and files nothing.** Every entry and
  every figure is a proposal.
- **Produces computations and illustrations, not tax advice.** A qualified tax professional
  reviews before anything is filed or acted on.
- **Never supplies comparable data, a range or a local rule.** Each comes from the user, with its
  source.
- **Never selects the method or concludes that a price is arm's length.**
- **Never changes an intercompany price or proposes a year-end adjustment as settled.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–9" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which group, which year, and which entities and jurisdictions?* | Bounds the study | **Ask again.** |
| **C** | *What are the documentation requirements in each jurisdiction, with source?* | Thresholds and deadlines are never built in | List the transactions, and say the requirements were not supplied. |
| **D** | *What does each entity do: its functions, assets and risks?* | The heart of the study | Show where costs and people sit, and ask. |
| **E** | *Which intercompany agreements exist?* | Documents, not ledger entries | List transactions with no agreement on file. |
| **F** | *Do you have comparable data and last year's documentation?* | Benchmarking and consistency | Outline the benchmarking only, with no range. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and **every group entity by name, with its jurisdiction**, and wait for
  an explicit yes (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Report intercompany flows by type and by pair of entities.
- Flag a tested party that made a loss in the year.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Group structure** | Required | PDF |
| **Intercompany transactions** by type and pair | Required | XLSX or CSV |
| **Intercompany agreements** | Required | PDF |
| Comparable data and prior documentation | Recommended | XLSX or PDF |

**Read back before starting, then wait for a yes:**

> *Preparing 2025 transfer pricing documentation for **Northbrook Trading and Northbrook UK**,
> from **your Mosofin connection**. **Two transaction types**: management fees and goods.
> Functional analysis as you described; comparables from **the set you uploaded**. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the entities, the
year and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Map the transactions and record the functional analysis

The intercompany transactions, the functional analysis and its corroboration:
[`references/method.md`](references/method.md) Steps 1–2b.

## Stage 4 — Method, tested party, benchmarking and analysis

Method selection, the tested party, benchmarking and the economic analysis:
[`references/method.md`](references/method.md) Steps 3–6b. Check
[`references/edge-cases.md`](references/edge-cases.md) for valuable intangibles, intercompany
financing, limited-risk characterisation and year-end true-ups.

## Stage 5 — Assemble the documentation, and present

The documentation, the agreements, then the output: [`references/method.md`](references/method.md)
Steps 7–9. Before presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the draft as an Excel
file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the group structure,
the functional characterisation and last year's conclusions.

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
