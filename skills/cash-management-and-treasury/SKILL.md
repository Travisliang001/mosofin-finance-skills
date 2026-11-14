---
name: cash-management-and-treasury
description: "Reviews how a business holds and moves its cash and designs the treasury set-up: a map of every cash account with its balance and activity, the bank account structure, a liquidity policy, a short-term investment policy, payment controls, FX and borrowing facility management, KPIs and governance. Finds dormant accounts, idle balances and concentration with one bank. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded account balances and movements. Use when the user asks about treasury or cash management, too many bank accounts, cash pooling or concentration, where to hold surplus cash, a liquidity or investment policy, payment controls, or wire-fraud prevention. Do not use for a weekly cash forecast (use cash-flow-forecast-13-week), for bank charges (use bank-fee-and-interest-analysis) or for loan covenants (use debt-and-covenant-tracking). Read-only: produces the map, the policies and a coverage sheet, and moves no money."
---

# Treasury: how cash is held, moved and protected

Most businesses collect bank accounts over time: one per entity, one per currency, one for a
project that ended years ago. This skill maps **where the cash is**, then designs how many
accounts are needed, how much to keep in each, what to do with the surplus, and **who may move
it**. It designs; your team and your bank act.

**Works with or without Mosofin.** With Mosofin connected the cash map is a read: every cash
account, its balance and its real activity. Without it, you upload the balances and movements and
the method is the same.

**The books show the accounts, not the banking.** The bank's name, each account's purpose, the
signatories, the facilities and any restriction on moving cash are never in an accounting system.
Controls are **designed** here, never tested. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never moves money, opens or closes an account, or changes anything in any system.**
- **Never presents a designed control as a tested one.**
- **Never names an investment product, a bank or a rate as a recommendation.** It sets the policy
  criteria; the choice is the user's.
- **Never counts cash that cannot be moved as available.** Trapped cash is shown apart.

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
| **B** | *Which legal entities, countries and currencies are in scope, and is any missing from what I can see?* | An entity with no connected file still holds cash | **Ask again.** A missing entity is listed as a gap in the map. |
| **C** | *For each bank account: which bank, what is it for, and who can sign?* | None of this is in the books | Map by account name only, and list bank, purpose and signatories as missing. |
| **D** | *Is any cash trapped or restricted, and can cash move between entities?* | It changes every liquidity figure, and decides whether pooling is possible | **Ask again** with more than one entity. Otherwise assume none, and say so. |
| **E** | *What is your risk appetite: the most you will hold with one bank, what you may invest in, how much FX exposure?* | Policy limits are the user's decision | Draft the policies with the limits left open. |
| **F** | *Which policies and facilities exist today, and what must liquidity cover: debt service, capex?* | Extend what exists; do not replace it unseen | Design from scratch, and **say that no existing policy was supplied.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and **every company file by name**, and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- List the cash accounts found and ask the user to map each to its bank and purpose (C).
- Point out any account with a balance and no recent activity.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Cash account list** with balances, by entity and currency | Required | XLSX or CSV |
| **Movements per account**, 12 months | Required for the activity and liquidity view | XLSX or CSV |
| Bank, purpose and signatories per account (C) | Required for the structure design | XLSX, or type it in the chat |
| Existing policies and facility terms (F) | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Reviewing treasury for **Northbrook Trading** and **Northbrook UK**, from **your Mosofin
> connection**: **eleven cash accounts**, in USD and GBP. You mapped nine to their banks; two are
> unidentified. No cash is restricted, and cash **can** move between the two. No existing policy.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
account count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and
every company file, check which read tools are enabled, and read each company profile, so
Stage 1's answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the accounts and map the cash landscape

Pull every cash account with its balance and movements in one batch, then build the map:
[`references/method.md`](references/method.md) Steps 0–1. The map is the foundation for
everything after it.

## Stage 4 — Design the structure and the policies

Bank account structure, liquidity policy, short-term investment policy, payment controls, FX and
facility management: [`references/method.md`](references/method.md) Steps 2–7. Check
[`references/edge-cases.md`](references/edge-cases.md) for trapped cash, tax on pooling, bank
concentration, payment fraud and dormant accounts that still hold a balance.

## Stage 5 — KPIs, governance, and present

Treasury KPIs and reporting, documentation and governance, then the output:
[`references/method.md`](references/method.md) Steps 8–10. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file, or the policy as a document, before creating either.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the account map and the agreed
policy limits. Balances are read again every run.

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
