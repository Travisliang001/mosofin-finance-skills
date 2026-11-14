---
name: audit-prep-pbc-list
description: "Prepares a business for its audit: scopes the audit areas, builds the PBC (prepared-by-client) list by financial statement area, states what makes each item audit-ready, scores readiness and gaps, and sets up a tracker with owners and dates working back from fieldwork. Produces the schedules the books can supply and lists the documents only people can, such as bank statements, contracts and minutes. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded trial balance and the auditor's request list. Use when the user asks to prepare for an audit or review, build or manage a PBC list, check audit readiness, or track auditor requests. Do not use for running the close (use month-end-close-checklist) or for reconciling balance sheet accounts (use balance-sheet-reconciliations). Read-only: produces the list, the schedules and a coverage sheet, and posts nothing."
---

# Audit preparation: the PBC list, ready before fieldwork

Before an audit the auditors ask for a long list of schedules and evidence: the **PBC list**,
"prepared by client". This skill builds that list by financial statement area, works out which
items can be produced now and which cannot, and gives each an **owner and a date**. The audit
procedures are the auditor's; this prepares the client's side.

**Works with or without Mosofin.** With Mosofin connected it produces many of the schedules
directly: the trial balance, ageing, ledger extracts, roll-forwards. Without it, you upload the
trial balance and the method is the same.

**Schedules are in the books. Documents are not.** Bank statements, signed contracts, board
minutes, loan agreements and count sheets are never in an accounting system. Expect a list that is
about half schedules the skill can produce and half documents a named person must find. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system**, and sends nothing to the auditor.
- **Never assumes the engagement is an audit.** An audit, a review and a compilation need very
  different support.
- **Never invents materiality**, and never marks an item ready without its evidence.
- **Where the auditor has sent a list, that list governs.** The skill maps to it and does not
  build a parallel one.

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
| **B** | *Is this an audit, a review or a compilation, and for which company and period?* | Sets the level of support needed | **Ask again.** Never assume an audit, and never default the period. |
| **C** | *When does fieldwork start, and are the figures final or still moving?* | The timeline is built backwards from that date | Build the list with no dates, and say so. |
| **D** | *Has the auditor sent a request list? Do you have last year's list, adjustments and management letter?* | Their list governs, and last year's issues come back | Build a standard list by area, and say it is not the auditor's. |
| **E** | *Who owns each area, and what support is already prepared outside the books?* | Every document item needs a named person | Leave the owner column open, and say so in the summary. |
| **F** | *Has the auditor told you materiality?* | It sets the priority of each area | Rank areas by balance size only. **Never supply a figure.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Check that the books cover the whole audit period, and that the year-end in the company profile
  matches the period given.
- With several company files, ask whether this is a single audit or a group audit.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance** at the period end, and the prior year | Required | XLSX or CSV |
| **Auditor's request list**, if received | Recommended. It governs when it exists | PDF or XLSX |
| Prior-year list, audit adjustments and management letter | Recommended | PDF or XLSX |
| Engagement type and period (B), fieldwork date (C), owners (E) | Required for B and C | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Preparing the **audit** of **Northbrook Trading** for the **year to 31 December**, from **your
> Mosofin connection**. Fieldwork starts **9 February**. Working from **the auditor's list you
> uploaded**, 84 items. No materiality given. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
account count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the balances and scope the areas

Pull the trial balance and the supporting reads in one batch, then scope and rank the audit areas:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Build the list and assess readiness

Build the list by area, state what makes each item audit-ready, then score readiness and gaps:
[`references/method.md`](references/method.md) Steps 2–4. Every schedule produced records where it
came from. Check [`references/edge-cases.md`](references/edge-cases.md) for a first-time audit, a
tight deadline, a weak monthly close, confirmations, related parties and a group audit.

## Stage 5 — Tracker, judgmental areas, and present

The tracker and timeline, preparation for estimates and judgments, expected adjustments and
prior-year items, then the output: [`references/method.md`](references/method.md) Steps 5–8.
Before presenting, check it against [`references/output.md`](references/output.md). Ask whether
the user wants the tracker as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the list structure, the owners and
the mapping to the auditor's numbering. Every balance and status is read again next time.

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
