---
name: chart-of-accounts-designer
description: "Designs or restructures a chart of accounts: measures how each existing account is actually used, sets the structure and numbering, builds the account list by section with descriptions and intended use, adds industry and tax accounts, handles multi-entity needs, and maps every old account to its new one. Fits the account types of the accounting system the user names. Reads the existing chart through a connected Mosofin workspace when the user agrees, or works from an uploaded chart. Use when the user asks to design, clean up, simplify or restructure a chart of accounts, renumber accounts, merge duplicate accounts, or set up accounts for a new company or system. Do not use for coding individual transactions (use gl-coding-assistant) or for building a journal entry (use journal-entry-builder). Read-only: produces the proposed chart, the mapping and a coverage sheet, and changes no account."
---

# Chart of accounts: the buckets every transaction goes into

The chart of accounts is the set of buckets every transaction is sorted into. Too many, or
overlapping ones, and every month-end becomes an argument about where things go. This skill
designs a new chart or cleans up an old one, with **numbering, descriptions and intended use**,
and maps each old account to its new one. A person makes the changes in the accounting system.

**Works with or without Mosofin.** With Mosofin connected the existing chart is read in full, and
so is **how each account is actually used**: which are busy, which are dormant, which duplicate
each other. Without it, you upload the chart and the method is the same.

**The target system is whatever you name.** It may be the connected system or a different one,
and its account types and numbering rules shape the design. The reporting framework and the
reports you need are yours to state. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never creates, renames, merges or deactivates an account in any system.** The chart and the
  mapping are proposals.
- **Never infers the reporting framework from the country.**
- **Never proposes removing an account that still holds a balance** without saying where the
  balance goes.
- **Never mistakes a balance for usage.** An account is judged by its activity.

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
| **B** | *Is this a new chart, or a restructure of the existing one? For which company?* | A restructure needs a mapping from old to new | **Ask again.** |
| **C** | *Which accounting system will the chart live in: the connected one, or another?* | Account types and numbering rules differ by system | **Ask again.** Never assume it is the connected system. |
| **D** | *Which reporting framework: US GAAP, IFRS or local GAAP?* | Decides the sections and some required accounts | **Ask again.** Never infer it from the country. |
| **E** | *What industry and size is the business, and which dimensions do you report by: class, department, location, project?* | Industry adds accounts; dimensions replace many sub-accounts | Use the industry in the company profile, and **confirm it.** |
| **F** | *Which reports must the chart serve: investors, lenders, the board, segments? Any multi-entity needs?* | Reporting needs drive how fine the accounts are | Design for standard statements only, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Make sure inactive accounts are included in the read. Left out, they hide history.
- With several company files, ask whether this is one chart or a harmonisation across them.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Existing chart of accounts**: number, name, type, active status | Required for a restructure | XLSX or CSV |
| **Trial balance, or activity by account**, 12 months or more | Recommended. Without it usage cannot be measured | XLSX or CSV |
| Target system (C), framework (D), industry and dimensions (E), reporting needs (F) | C and D required | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Restructuring the chart of accounts for **Northbrook Trading**, from **your Mosofin
> connection**, to stay in **the connected system**, under **US GAAP**. A **services** business
> reporting by **department**. The chart must serve the **lender's covenant reporting**. Shall I
> go ahead?*

On the upload path, name each file you received and say what was read from it: the account count
and the period of activity. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the chart and measure usage

Pull the chart, the dimensions and the tax codes in one batch, then measure how each account is
used: [`references/method.md`](references/method.md) Steps 0–0b.

## Stage 4 — Set the structure and build the account list

Structure and numbering, the account list by section, then industry and tax accounts:
[`references/method.md`](references/method.md) Steps 1–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for accumulated noise, number conflicts
with the target system, one account used for different purposes, sub-account sprawl and dormant
accounts that still hold a balance.

## Stage 5 — Multi-entity, mapping, and present

Multi-entity considerations, then the output with the old-to-new mapping:
[`references/method.md`](references/method.md) Steps 5–6. Before presenting, check it against the
quality standards and design principles in [`references/output.md`](references/output.md). Ask
whether the user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the structure, the numbering
convention and the design decisions. Usage is measured again every run.

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
