---
name: intangibles-and-amortization
description: "Maintains intangible assets and their amortisation: checks that amortisation is being charged at all, identifies the asset classes, sets useful lives and methods from the user's policy, tests which internal development costs qualify for capitalisation, scans for costs expensed that should be capitalised and the reverse, computes amortisation, and proposes the entry, the roll-forward and the disclosure inputs. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded register and ledger detail. Use when the user asks about intangible assets, amortisation, capitalised software or development costs, patents, customer lists, useful lives, or impairment indicators for intangibles. Do not use for tangible assets (use fixed-asset-register-and-depreciation) or for prepaid expenses (use prepaid-amortization-schedule). Read-only: produces the register, schedules and proposed entries, and posts nothing."
---

# Intangibles: what has no physical form, and how long it lasts

Some of what a business owns has no physical form: a customer list, a patent, software written
in-house. Its cost goes on the balance sheet and is written off over its life. This skill keeps
the **register**, computes **amortisation**, tests what may be capitalised, and proposes the
entry. A person posts it.

**Works with or without Mosofin.** With Mosofin connected it reads the balances, additions and
disposals and the amortisation charged, and checks first that a charge exists at all. Without it,
you upload the register and the ledger detail and the method is the same.

**The register, the useful lives and the capitalisation policy are yours.** Without an asset-level
register, totals still reconcile but amortisation by asset does not. Which development stages
qualify is a policy decision under the framework you name. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never picks a useful life.** The standard ranges are ranges, not a policy.
- **Never capitalises a development cost without the policy and the project stage dates.**
- **Never concludes on impairment.** It lists the readable indicators and leaves the test to the
  user.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–13" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period?* | Sets every read | **Never default the period.** |
| **C** | *US GAAP, IFRS or local GAAP?* | The frameworks differ materially on development costs | **Ask again.** |
| **D** | *Do you have an intangibles register, by asset?* | Without it only totals can be reconciled | Reconcile movements and totals only, and say asset-level amortisation was not checked. |
| **E** | *What is the useful life or indefinite status for each class, and the amortisation method?* | The policy decides the charge | Report the charge in the books against the balances, and compute nothing new. |
| **F** | *What is the capitalisation policy for internal development, and what are the stage dates of each project?* | The decisive input for development costs | List development spend by project, and capitalise nothing. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report whether an amortisation charge is being posted, and whether it has changed while the
  balances have.
- Confirm which accounts hold intangibles and whether accumulated amortisation is by class or in
  one account.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Intangibles register**: asset, cost, date, life, method | Recommended. The core gap when missing | XLSX |
| **Ledger detail** for the intangible and accumulated amortisation accounts | Required | XLSX or CSV |
| **Development spend by project**, with stage dates | Required if capitalising development | XLSX |
| Asset class policy and capitalisation policy | Required | PDF, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Reviewing intangibles for **Northbrook Trading** for the **year to September**, under **US
> GAAP**, from **your Mosofin connection** and **the register you uploaded**. Software over **5
> years** straight-line, customer lists over **8**. Development capitalised from **application
> stage** only, with stage dates supplied. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
asset count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the balances and check that amortisation runs

Pull the accounts and movements, check the amortisation charge exists, then identify the classes:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Lives, methods, capitalisation and the charge

Useful lives, the method, capitalisation of internal development, the two-way scan, then the
amortisation: [`references/method.md`](references/method.md) Steps 2–5, including Step 4b. Check
[`references/edge-cases.md`](references/edge-cases.md) for cloud arrangements, website costs,
research that does not qualify and renewed contracts.

## Stage 5 — Entry, impairment indicators, roll-forward, and present

The entry as a **proposal**, impairment indicators, life reassessment, disposals, the roll-forward
and disclosure inputs, then the output: [`references/method.md`](references/method.md) Steps 6–12.
Before presenting, check it against [`references/output.md`](references/output.md). Ask whether
the user wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 13. Persist the class policies, the
capitalisation policy and the account mapping.

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
