<!-- restructuring-and-severance-asc420 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Beyond the usual: the working paper contains a redundancy list. Producing it in the context of the wrong client is a confidentiality incident, not a reconciliation error.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The accrual model still works in full — it was always built from HR and legal inputs. **The rollforward, the recognition check and the staleness test do not run.** Say which. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | Ask which — **and note that a restructuring frequently spans entities.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**Restructurings cross entity lines routinely.** A group closes a site; the employees are on one entity's payroll, the lease sits in another, and the plan was approved by the parent. **The obligation is recognised by the entity that has it**, which is not always the entity that announced the plan. Where several files are connected, read each and label each figure with its entity. Do not aggregate a group restructuring into one column and present it as one liability. See `consolidation-and-eliminations`.

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

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run. Do not carry a capability map between runs.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The restructuring liability account detail, the restructuring expense account, the payroll and wages accounts, the chart, and the lease and facility accounts are independent. One message.

### The `mock: true` flag

Fixture data has **no stale reserves and no double-counted severance**, because nobody generated any. Every diagnostic in this skill is a test for a *lingering* or *misdirected* balance, and fixture balances neither linger nor wander.

Label it in the file name and on the rollforward sheet.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The plan**: approval date, scope, departments, expected completion date. `[manual]`
2. **The communication**: what was said, to whom, when, and how it is evidenced. `[manual]` — **this is the recognition trigger and it must be evidenced, not asserted.**
3. **The impacted population**: headcount and cost by group; names only where genuinely required. `[manual]`
4. **Severance terms**: contractual, statutory, and any enhanced offer. `[manual]`
5. **Whether future service is required** of any group, and over what period. `[manual]` — the crux of Step 2.
6. **Contracts to terminate**, with penalties. `[manual]`
7. **Framework**: ASC 420 or IAS 37. `[manual]` — they are close but not identical, and the recognition triggers differ in wording.

**Decisions are the user's; state is the workspace's.**
