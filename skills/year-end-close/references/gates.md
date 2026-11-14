<!-- year-end-close · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace before anything else
  - Gate 1 — Establish the datasource and entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Map what you can actually do
  - Gate 3 — Read the profile, then interview for what remains

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.


## Gate 0 — Confirm the workspace before anything else

1. Call `list_workspaces` with no arguments.
2. If the status is `confirmed`, there is one workspace. **Read its name back and wait for an explicit yes.**
3. If the status is `selection_required`, ask: **"Is this a single-workspace task or a multi-workspace one?"**
   - Single: ask which one by name, then `list_workspaces(workspace_ids=[<ws_...>], mode="single")`.
   - Multi: ask which ones, then `list_workspaces(workspace_ids=[<ws_...>, ...], mode="multi")`.

Refer to a workspace by **name**, or by the opaque `ws_...` handle. Never print the internal numeric id, never ask for it, and if it appears in an error, name the workspace instead.

**Why this gate matters here, at the end of the cycle.** The year-end figures are **audited, filed, and become the comparative for every subsequent period.** An error at any other point in the year is corrected in the next month. **An error here is corrected by restating.**

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The plan, the calendar and the checklists all work as the original describes. **No PBC is pre-assembled, no lead schedule is built, and none of the close-completeness tests run.** Say precisely that. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Step 2's consolidation block is the reason.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **Stop.** A partial year-end is not a year-end. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On consolidation, which year-end forces.** Step 2 has a dedicated block: full consolidation, currency translation, intercompany eliminations, non-controlling interest. **Reading several ledgers is not consolidating them** — there are no eliminations in what comes back, and NCI arises only in the consolidation.

`[auto]` for each entity's own position and, where both sides of an intercompany relationship are connected, **for reading both sides together** — which is the strength `intercompany-reconciliation` describes. `[manual]` for the consolidation itself where it happens outside these books. **Establish which before promising consolidated figures.**

---

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Map what you can actually do


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


Call `get_datasource_tools` for the chosen company file and read the **`effective_policy`** on each tool.

| `effective_policy` | Verdict | Behaviour |
|---|---|---|
| `enabled` | `[auto]` | Call it. Batch with other independent reads. |
| `permission` | `[gated]` | Expect `approval_required`. Explain what and why, get a yes, re-invoke with `approved=true`. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | `[manual]` | Not available. The step remains; the user performs it. |

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run, and the coverage sheet records the difference.

**A scope note.** If a tool that posts entries or locks a period appears in the listing, it is **out of scope regardless of `effective_policy`.** Closing entries, adjusting entries and the period lock are all posted by a person.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** Trial balances at each month end, the full year's transaction detail, prior-year balances, ageings, the chart and the new year's opening position are independent. **A year-end run is the largest read in the pack — issue it as one batch**, not thirteen.

### The `mock: true` flag

Fixture data has **twelve tidy closed months, clean closing entries, a locked year nobody posted into, and a new year opening at exactly the right balances.** So every completeness test in this skill passes.

**And this is the run whose output goes to an auditor.** Label it in the file name, on the calendar, and at the head of the PBC — **a pre-assembled PBC built from fixture data would be handed to an audit team as though it were the client's records.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. **Year-end is annual and its structure is highly stable** — the framework, the audit firm, the statutory filings and the estimate methodologies change rarely, and Step 6 exists to capture them.

Interview for:

1. **The fiscal year-end date and the reporting framework.** `[manual]` to confirm; `[auto]` to read the fiscal calendar.
2. **Audit type** — full audit, review, compilation, or none. `[manual]`, **and it determines whether Steps 2a and 4 apply at all.**
3. **Audit firm and timeline.** `[manual]` — and it sets the calendar backwards.
4. **Statutory filings in scope.** `[manual]`; **persist the list.**
5. **Year-end materiality**, often tighter than monthly. `[manual]`.
6. **Major events during the year** — acquisitions, divestitures, equity raises, debt issuances, restructurings. `[manual]` to identify; **`[auto]` for their accounting traces.**
7. **Going-concern indicators.** `[manual]` to assess; `[auto]` for the liquidity facts.
8. **Prior year auditor's findings and management letter.** `[manual]` — **and this is Step 6's carry-forward, which should already be in the profile if last year's run persisted properly.**

**Decisions are the user's; state is the workspace's.**
