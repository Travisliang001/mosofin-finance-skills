<!-- rolling-forecast · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** A rolling forecast is a **persistent artefact** that accumulates value over many refreshes — prior forecasts, an accuracy record, an agreed driver set. Attaching that history to the wrong entity does not just produce one wrong file; it contaminates the series, and the accuracy tracker is only as good as the continuity of what it is tracking.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Actuals are `[manual]` — supplied by export. The forecast still works exactly as the original did, but **the roll is no longer automatic and the seasonality derivation does not run.** Say so. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | Ask which. **A group rolling forecast is a consolidation question** — see below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **Do not roll forward on partial actuals.** A month locked with incomplete data is worse than a month not locked. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On group forecasts.** Reading three ledgers is not consolidating three ledgers — there is no elimination in what comes back. Intercompany revenue and cost will be double-counted in any naive sum, and in a forecast that error compounds forward across the whole horizon. Either forecast each entity separately and label each, or take the consolidated actuals from wherever the consolidation is actually performed.

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

**Batch independent reads.** Monthly actuals across several years, the chart, the payroll accounts, the current-period close status and any budget loaded in the book are independent. **Read the full multi-year history in one go** — seasonality needs it, and fetching a year at a time is the commonest way this skill becomes slow.

### The `mock: true` flag

Fixture data has **smooth, seasonless history and no forecast track record.** So:

- the derived seasonality will be flat, and flat seasonality is not seasonality
- the hockey-stick test will find nothing, because generated actuals track generated plans
- the accuracy tracker has nothing to score

**Every time-series contribution in this skill needs real history**, and fixture data does not have any. Label it in the file name and on Sheet 1.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. **This skill depends on persistence more than any other in the pack** — an accuracy tracker cannot exist on run one — so the profile is not a convenience here, it is the mechanism.

Interview for:

1. **The horizon and granularity**, if not already agreed. `[manual]`
2. **Updated drivers and assumptions.** `[manual]` — this is Step 3 and it is the substance.
3. **Pipeline and bookings.** `[manual]` — CRM data, not ledger data.
4. **The headcount plan** — hires, attrition, timing. `[manual]`
5. **Known future events** — contracts, launches, price changes. `[manual]`
6. **The FX assumption**, where relevant. `[manual]`, and **never supplied by this file or carried forward from a prior run.**

**Decisions are the user's; state is the workspace's.** The ledger says what happened. Only the client says what will.
