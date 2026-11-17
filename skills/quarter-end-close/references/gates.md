<!-- quarter-end-close · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace before anything else
  - Gate 1 — Establish the datasource and entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Map what you can actually do
  - Gate 3 — Read the profile, then interview for what remains
  - A near-substitute is not a substitute

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.


## Gate 0 — Confirm the workspace before anything else

Nothing below runs until the workspace is confirmed.

1. Call `list_workspaces` with no arguments.
2. If the status is `confirmed`, there is one workspace. **Read its name back and wait for an explicit yes.**
3. If the status is `selection_required`, ask in chat: **"Is this a single-workspace task or a multi-workspace one?"** Never assume, never take the first row because it is first.
   - Single: ask which one by name, then `list_workspaces(workspace_ids=[<ws_...>], mode="single")`.
   - Multi: ask which ones, then `list_workspaces(workspace_ids=[<ws_...>, ...], mode="multi")`.

Refer to a workspace by **name**, or by the opaque `ws_...` handle where a machine reference is unavoidable. There is an internal numeric id behind it: never print it, never repeat it, never ask for it. If it appears in an error, name the workspace instead.

**Why this gate matters at quarter-end in particular.** Quarterly output goes *outside the building* — to a lender, to a board, to a regulator, to shareholders. A monthly close that was run against the wrong entity is an embarrassment discovered internally. A covenant certificate signed off the wrong entity's ledger is a false certification to a bank. The consequences of a mis-scoped quarter are categorically worse than a mis-scoped month, and the fix is one question asked before the first read.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every step is `[manual]`. Say so at once. A quarter-end plan can still be produced — it is a good plan — but nothing in it will have been verified against anything. Label it a plan, not a close. |
| **Exactly one company file** | The straightforward case. Confirm the `display_name` before reading. |
| **Several company files** | Ask which, **by `display_name`**. If the answer is "the group," see the consolidation note below. |
| **Connected but stale or broken** | A `reconnect_url` in any response means the connection needs the user. Stop and say so. Do not fill the gap with assumptions and do not report a partial quarter as a complete one. |

Always refer to company files by `display_name` — "Northwind Trading Ltd" — never by `data_source_id`. Pass the id between tools; do not display it.

**On consolidated quarterly reporting.** A 10-Q, a board pack and most covenant certificates are consolidated documents. The gateway gives you each connected company file separately. **Reading three ledgers is not consolidating three ledgers** — there is no elimination, no minority interest, no common-control adjustment in what comes back. If the consolidation is performed in a tool outside these books, then the consolidated figures are `[manual]` and the workspace's contribution is to the *components* only. Say which you are producing. See `consolidation-and-intercompany-eliminations` and `intercompany-reconciliation`.

---

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Map what you can actually do


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


Call `get_datasource_tools` for the chosen company file and read the **`effective_policy`** on each tool. That field decides what is possible today — not documentation, and not this file.

| `effective_policy` | Verdict | Behaviour |
|---|---|---|
| `enabled` | `[auto]` | Call it. Batch with other independent reads. |
| `permission` | `[gated]` | Expect `approval_required`. Explain what and why, get a yes, re-invoke with `approved=true`. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | `[manual]` | Not available. The step remains; the user performs it. Never quietly drop it. |

Every verdict below is a **default written before the gateway was consulted**. Where Gate 2 disagrees, **Gate 2 wins** — for this workspace, on this run — and the write-up should record the difference.

Read tool names off the response rather than typing them from memory. `UNKNOWN_TOOL` means the name is wrong; re-read the list rather than trying a near-miss.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after an approval. Dropping it on the retry is the commonest way an approved call still fails.

**Batch independent reads.** A quarter-end run needs the trial balance at four dates, the transaction detail for three months, the chart, the customer and vendor lists, and the prior-quarter balances. Almost none of these depend on each other. Issue them together. Serializing a quarter's worth of reads turns a two-minute job into a twenty-minute one and improves nothing.

### The `mock: true` flag, and why it hits this skill hardest

If a response carries `mock: true`, it is **fixture data** and not the client's books.

This matters more here than in almost any other skill in the pack, and for a specific reason. **The quarterly diagnostics in this file are all patterns across time.** Q4 versus Q1–Q3 posting volume. Reserve rates that never move. Prior quarters that were reopened. Estimate methodology drift over eight quarters.

Fixture data has no history worth the name. It is generated smooth. Its quarters are uniform, its reserve rates are stable because nobody varied them, its prior periods were never reopened because nobody ever posted into them. **Every single time-series diagnostic below will come back clean on mock data, and every one of those clean results is meaningless.**

So: label fixture-derived output in the file name and on the first sheet, and be explicit that the pattern tests did not run against anything real. A clean quarterly diagnostic on fixture data is not a mild caveat. It is the absence of a test.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. If the workspace carries a client profile — the fiscal year end, the reporting framework, the covenant package, who signs what — **use it and say you are using it.** A quarterly cadence means these questions come round four times a year; asking them fresh each time is how a tool stops being used.

Interview only for what is genuinely open. For this skill, that is:

1. **Which quarter, and on what fiscal calendar?** A quarter is not three calendar months in every company. Read the fiscal year end from the company record, then confirm.
2. **Which reporting obligations are actually in scope this quarter?** 10-Q, board pack, lender certificate, internal management report — the answer drives everything in Step 3, and the four have almost nothing in common.
3. **Materiality for the interim period.** The original notes it is often tighter than monthly. See the note in Step 2 on the two denominators.
4. **Is an auditor performing an interim review?** Step 4 exists or does not exist on this answer.
5. **Are segments tracked as a dimension inside the book, or outside it?** Answerable in part from the chart — read the class/location/department dimensions first, then confirm. It decides whether Step 2's segment task is `[auto]` or `[manual]`.
6. **What do the covenants actually say?** Not the ratio names — the **definitions**. This is the single most important interview question in the skill and the next section explains why.

**Decisions are the user's; state is the workspace's.** The ledger can tell you EBITDA as the chart computes it. Only the credit agreement says what EBITDA means to the bank.

---

## A near-substitute is not a substitute

Three of these, and each one produces a confident wrong number rather than an obvious gap. Confident wrong numbers are the dangerous kind.

**1. Ledger EBITDA is not covenant EBITDA.**

This is the most dangerous near-substitute in the skill, because the output of the mistake is a compliance certificate.

A credit agreement's EBITDA is a bespoke, negotiated definition. It typically adds back things the ledger does not group together — non-recurring items, restructuring costs, stock compensation, management fees, specified one-offs listed by name in the agreement — and it frequently annualizes or pro-formas acquisitions. Two agreements at the same company will define it differently. **The ledger's operating result plus depreciation and amortization is not that number.** It is close enough to look right and different enough to change the answer.

So: computing the ratio is `[auto]`. Establishing the **inputs** to the ratio is `[manual]` and is read out of the credit agreement, once, and then recorded so it does not have to be read again. Reporting "compliant" from a ledger-derived EBITDA the agreement would not recognise is worse than reporting nothing.

**2. Deferred revenue is not RPO, and recognised revenue is not ARR.**

Both are in Step 2's KPI block and both are outside the ledger by construction.

**Remaining performance obligations** are the committed amounts *not yet recognised* — and they include amounts **not yet billed**. Deferred revenue captures only what has been billed and not recognised. The unbilled committed portion is in the contracts and nowhere else. Reporting the deferred revenue balance as RPO understates it, systematically, and by an amount that grows with the length of the contracts.

**ARR** is a contract metric — what customers are committed to pay on an annualised basis. Recognised revenue is what was earned in a period, which is a different thing that happens to be measured in the same units. Multiplying a month's revenue by twelve is not ARR; it is a month's revenue multiplied by twelve.

**3. Book cash is not a bank statement.**

Step 6 asks that YTD cash reconcile to YTD bank statement activity. **Bank statements are not on this surface.** The ledger's bank account and the ledger's cash movements are the same data twice, so tying one to the other proves nothing. This absence is consistent across the pack — see `bank-reconciliation`, `merchant-and-payment-processor-rec`, `payroll-clearing-reconciliation`. The test is real and it stays in the checklist as `[manual]`.
