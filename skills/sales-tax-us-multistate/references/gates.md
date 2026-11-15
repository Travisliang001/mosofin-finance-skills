<!-- sales-tax-us-multistate · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Nexus attaches to a **legal entity**, and thresholds are measured per entity per state. A group with three selling entities has three separate nexus analyses, and **an entity below the threshold on its own does not acquire nexus because a sister company is above it.** Mixing two entities' sales into one threshold test produces nexus conclusions that are wrong in both directions at once.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Sales by state, transaction counts, exempt sales and the use-tax population are all `[manual]`. The framework still applies; nothing is measured. Say so. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | **Run the nexus analysis per entity, never combined.** See above. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **Do not run a partial nexus analysis** — missing sales understate a threshold test, and the failure mode is concluding there is no obligation where there is one. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

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

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run.

**This is the capability version of the rule this skill already lives by.** Do not carry a capability map between runs any more than you would carry last year's nexus threshold.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** Invoice detail with addresses, the customer list, the sales tax payable accounts, the purchase ledger, the chart and any tax-code configuration are independent. **Read the full multi-year invoice history in one go** — threshold measurement periods are rolling or prior-calendar-year, so a single current period is not enough.

### The `mock: true` flag

Fixture data has **invented addresses that map to no real distribution of states**, and a tax payable account that behaves. So the nexus map is meaningless, the trigger dates are meaningless, and the collected-not-remitted test passes by construction.

Label it in the file name and on Sheet 1. **A nexus analysis on fixture data is not a weak analysis; it is not an analysis.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **Physical presence facts** by state — offices, employees, contractors, inventory, property. `[manual]`, and see Step 1: **inventory in a third-party warehouse is the one people forget.**
2. **Registration status per state**, and the registration dates. `[manual]` — **persist this; it is the join that turns sales data into an exposure list.**
3. **Current economic nexus thresholds** per state. `[manual]`, current-sourced, **never carried forward.**
4. **Current rates.** `[manual]`, current-sourced. **Or, better, confirmation of which tax engine the entity uses** — see Step 4.
5. **Product and service descriptions**, in enough detail for taxability. `[manual]`
6. **Taxability determinations**, with sources. `[manual]`
7. **Exemption certificates on file.** `[manual]` to supply; **persist the register.**
8. **Marketplace channels** used. `[manual]` to identify; `[auto]` in part to trace.
9. **Filing frequency assigned by each state.** `[manual]` — the state assigns it.

**Decisions are the user's; state is the workspace's.** The ledger says what was sold and where it went. Only the states say what is owed.
