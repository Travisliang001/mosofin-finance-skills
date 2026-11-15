---
name: ipo-readiness-accounting
description: "Builds an IPO readiness roadmap for the finance function: measures how long the close actually takes and how much of it rests on manual journals, assesses gaps against public-company requirements, plans close acceleration, lists the accounting policy memos needed, and sets out equity and earnings-per-share readiness, internal control readiness and the reporting process. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded close calendars and statements. Use when the user asks about getting finance ready for an IPO, a public-company readiness assessment, shortening the close, or which years need audits before listing. Do not use for preparing a filing (use sec-10q-10k-prep) or for testing controls (use sox-controls-design-and-testing). Read-only: produces the roadmap and a gap list, and is not legal or securities advice."
---

# IPO readiness: getting finance ready to be public

A public company closes faster, documents more, controls more tightly and reports to a calendar.
This skill builds the **roadmap** from where the finance function is today: gaps against
public-company requirements, a plan to speed up the close, the policy memos needed, and readiness
for equity, controls and reporting.

**Works with or without Mosofin.** With Mosofin connected it **measures** what is usually only
asserted: how long the close takes, how much is posted by manual journal, and whether closed
periods were reopened. Without it, you upload the close calendar and the method is the same.

**Most readiness sits outside the books.** The cap table, contracts, the control assessment, the
intended registrant and which years must be audited come from you and your advisers. **This is a
finance roadmap, not legal or securities advice.** Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Not legal, securities or listing advice.** Requirements are confirmed with counsel and the
  auditors.
- **Never asserts close speed.** It measures it from posting dates.
- **Never states a filing requirement from memory as settled.**
- **Never assesses a group structure that is about to change without saying so.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–8" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, what is the target timeline, and which entity will be the registrant?* | Sets the sequence | **Ask again.** |
| **C** | *Is a reorganisation planned before the IPO?* | The structure being assessed may change | Assess the current structure, and **say that you assumed it stays.** |
| **D** | *Which years must be audited, and what is their status?* | Usually the binding constraint | List audit status as not supplied. |
| **E** | *What is the equity history: cap table, grants, valuations?* | The whole equity section rests on it | List equity and earnings-per-share readiness as not assessed. |
| **F** | *What is the state of the control environment, and which systems are in use?* | Sets the control workstream | List the control assessment as not supplied. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the measured close timeline for the last twelve months, and the share of entries that are
  manual journals.
- Report periods reopened after close.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Close calendar and task list** | Required | XLSX |
| **Financial statements** for the years to be presented | Required | PDF or XLSX |
| **Cap table and grant history** | Required for the equity section | XLSX |
| Control assessment and systems list | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Assessing IPO readiness for **Northbrook Holdings**, targeting **a listing in 18 months**,
> registrant **the current parent**, no reorganisation planned, from **your Mosofin connection**.
> **Two of three years audited.** Cap table uploaded. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the periods covered
and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the books and measure the close

Pull the posting history, then measure what is usually asserted:
[`references/method.md`](references/method.md) Steps 0–0b.

## Stage 4 — Gaps, close plan and policy memos

Gaps against public-company requirements, the close acceleration plan, and the policy memo
library: [`references/method.md`](references/method.md) Steps 1–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for a fast close bought at the cost of
accuracy, a close carried by manual journals, and reopened periods.

## Stage 5 — Equity, controls, reporting, and present

Equity and earnings-per-share readiness, control readiness, the reporting process, then the
output: [`references/method.md`](references/method.md) Steps 4–7. Before presenting, check it
against [`references/output.md`](references/output.md). Ask whether the user wants the roadmap as
an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the timeline, the registrant and
the workstream owners.

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
