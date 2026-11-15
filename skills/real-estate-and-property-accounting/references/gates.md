<!-- real-estate-and-property-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Property is very commonly held in a **separate legal entity** — a propco holding the building, an opco trading from it, sometimes one special-purpose vehicle per property. That structure is the norm rather than the exception in real estate, which means a workspace with several company files is the normal case and picking the wrong one is the normal risk. Confirm first.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every step is `[manual]`. The skill still works as the original did; nothing is verified against anything. Say so. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | Ask which, **by `display_name`**. In a propco/opco structure the property is in one and the occupation is in the other — see below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**The propco/opco structure, and why it changes the answer to Step 1.**

This is the most important entity consideration in the skill, and it is easy to get backwards.

Where a property is held by one entity and occupied by a related entity that pays rent, the classification question splits:

- **In the standalone accounts of the propco**, the property earns rental income from a separate legal person. Under IFRS that is capable of being investment property under IAS 40 — the fact that the tenant is a group company does not, of itself, prevent it.
- **In the consolidated group accounts**, that rent is an intercompany transaction that eliminates. The group occupies its own building. **At group level the property is owner-occupied**, and IAS 40 does not apply to it.

So **the same building has two correct classifications at two reporting levels**, and which one is right depends on whose accounts you are preparing. Establish that before Step 1, not after.

`[auto]` where both entities are connected: read the rental income in one and the matching rent expense in the other, and confirm they agree. `[manual]` for the classification conclusion. See `consolidation-and-intercompany-eliminations` and `intercompany-reconciliation`.

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

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run, and the coverage sheet records it. Do not carry a capability map between runs.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The chart of accounts, the property and accumulated depreciation account detail, the rental income accounts, the interest accounts and the disposal accounts are all independent. One message.

### The `mock: true` flag

Fixture data will have **clean classification and consistent depreciation**, because it was generated that way. Every contradiction test in this skill — the fair-value-model property that is also depreciating, the held-for-sale asset still depreciating, land with accumulated depreciation, interest capitalising past readiness — **will pass on fixture data, and every pass will be meaningless.**

This skill is built almost entirely out of contradiction tests, so `mock: true` removes most of its value rather than some of it. Label it in the file name and on Sheet 1, and state plainly that the classification tests did not test anything.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. Property portfolios change slowly. If the workspace profile holds the framework, the measurement policy, the property list, the useful lives and the land/building allocations, **use them and say so.**

Interview for:

1. **The reporting framework.** `[manual]`, and it governs everything — see Step 1.
2. **Each property's use**, which determines classification. `[manual]` to confirm; `[auto]` to test against behaviour.
3. **The IFRS measurement election** for investment property, if applicable — cost or fair value. `[manual]`, and note it is close to irreversible.
4. **The land/building allocation** at acquisition, and its basis. `[manual]` unless it is already in the chart as separate accounts, which is itself informative.
5. **Lease terms for tenanted property** — term, escalations, rent-free periods, incentives. `[manual]`; the ledger has the cash, not the contract.

**Decisions are the user's; state is the workspace's.** The ledger says what a property earned. It does not say what the property is for.
