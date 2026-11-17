<!-- valuation-agent-dcf-comps-football-field · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** A valuation goes to buyers, investors, boards and sometimes auditors. **A net debt figure read from the wrong entity produces a specific, confident, wrong equity value** — and it is the kind of error that survives review, because the bridge looks like arithmetic rather than analysis.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Everything is `[manual]`, as the original assumes. **The bridge, the tie-back and the historical evidence all become supplied inputs.** Say so. |
| **Exactly one company file** | Confirm the `display_name` — **and confirm it is the valuation subject.** |
| **Several company files** | **What is being valued: an entity, or the group?** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **A missing debt-like item is exactly the failure mode the automatic half exists to prevent**, so stop. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On what is being valued.** A DCF of a group's consolidated cash flows must bridge to a **consolidated** net debt, and consolidation generally happens outside these books. **Summing several entities' debt and cash is not consolidated net debt** — intercompany loans would be counted as both an asset and a liability of the same group, when they eliminate entirely. Getting that wrong can move the bridge substantially in either direction. See `consolidation-and-eliminations` and `intercompany-reconciliation`.

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

**Batch independent reads.** The balance sheet at the valuation date, the debt and lease accounts, cash, the chart, and the multi-year income statement and cash flow history are independent. **Read the balance sheet at the valuation date specifically**, not at the last period end — see Step 1.

### The `mock: true` flag

Fixture data has **a tidy balance sheet with no unusual debt-like items and no lease liabilities.** So the bridge comes out clean and the omission this skill exists to catch does not exist to be caught.

Label it in the file name and on the bridge. **A valuation on fixture data is an arithmetic demonstration.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The forecast model.** `[manual]` — and **establish whether Mosofin has its outputs or its structure.**
2. **The valuation date.** `[manual]` — and it controls everything; see Step 1.
3. **The purpose and audience.** `[manual]`, **and it sets whether a qualified specialist is required.**
4. **WACC inputs.** `[manual]` — market data.
5. **The comparable and transaction universes.** `[manual]`.
6. **Options, warrants and diluted share count.** `[manual]` — **no cap table on this surface.**
7. **The client's net debt definition**, if they have one — because Step 6b's finding depends on knowing what they think it includes.

**Decisions are the user's; state is the workspace's.** And the opinion of value is the specialist's.
