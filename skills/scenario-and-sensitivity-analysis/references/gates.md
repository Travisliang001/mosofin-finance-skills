<!-- scenario-and-sensitivity-analysis · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** The output of this skill is a statement about **how much risk a specific business carries**, frequently prepared for a board, a lender or an investor. Volatility measured from the wrong entity's history produces ranges that are precisely wrong — plausible-looking, specific, and about somebody else.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | **The analysis still runs in full** — every technique is computation. **The ranges revert to user-supplied, which is what the original assumed.** Say so explicitly: the tornado ranks by model coefficient, not by observed risk. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | Ask which. **A group model needs consolidated history**; summing ledgers is not consolidating them. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. The analysis can proceed on supplied ranges — **label them as supplied.** |

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
| `disabled` | `[manual]` | Not available. The step remains; the user supplies the ranges. |

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run. Do not carry a capability map between runs.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** **Read the longest available monthly history in one go** — volatility, correlation and percentile estimates all degrade sharply with fewer observations, and fetching a year at a time is both slow and insufficient.

### The `mock: true` flag

**This skill is the most thoroughly defeated by fixture data of any in the pack**, because its entire contribution is a measurement of variability.

Generated ledgers are **smooth**. Their margins do not move, their growth does not wobble, their costs do not spike. So:

- observed volatility will be near zero, producing **absurdly narrow ranges**
- the tornado will rank drivers by model coefficient after all, having appeared to do otherwise
- correlations will be artifacts of the generator
- percentiles of a smooth series are meaningless

**A scenario analysis whose ranges came from fixture data is worse than one with honest guesses**, because it carries the authority of measurement without the substance. Label it in the file name, on Sheet 1, and **on the ranges themselves.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The underlying model or plan.** `[manual]` — and establish **whether Mosofin has its structure or only its outputs**, because that determines whether scenarios can be computed here or must be run by the user.
2. **The output metric or metrics of interest.** `[manual]`, and see the edge case — the choice changes the ranking.
3. **The drivers to vary.** `[manual]` to choose; `[auto: read]` to measure.
4. **Ranges.** `[auto: read]` to propose from history; **`[manual]` to accept, adjust or override** — and overriding is legitimate and often right.
5. **Scenario definitions**, if discrete. `[manual]` — coherent stories are authored, not computed.
6. **Probability weights**, if used. `[manual]`
7. **Constraints and thresholds** — covenant levels, minimum cash, breakeven. `[manual]` for covenant definitions (**from the credit agreement**); `[auto: read]` for current position against them.

**Decisions are the user's; state is the workspace's.**
