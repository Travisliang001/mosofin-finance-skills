<!-- statement-of-equity-changes · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Equity is entity-specific in the most literal sense — it records who owns this particular legal person and what they have put in and taken out. It is also the statement most likely to name individuals (partners, members, owners) and to disclose distributions to them.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every movement is `[manual]`. The framework applies in full. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Ask which — and establish whether this is a consolidated statement**, which changes everything about NCI. See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On non-controlling interest.** The NCI column exists **only in a consolidated statement**, and consolidation is generally performed outside these books. Reading several company files gives you several standalone equity sections; **it does not give you NCI**, which arises from the consolidation of a partially-owned subsidiary and requires the ownership percentages, the elimination entries and the subsidiary's results attributed proportionally.

So: **`[auto]` for each entity's own equity; `[manual]` for the NCI column and for anything consolidated.** See `consolidation-and-eliminations`. Where the registrant's own file holds the consolidated result, NCI may be readable as an account — check rather than assume.

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

**Batch independent reads.** The chart, every equity account's full transaction detail, the income statement, the dividend payable account and the prior period's closing balances are independent. **Read the comparative period in the same batch** — Step 6 needs it.

### The `mock: true` flag

Fixture data has **clean equity movements from recognisable sources and no direct postings to retained earnings.** So Step 0's source test — the one test in this skill that is not guaranteed to pass — passes.

Label it in the file name and on the tie-out sheet.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **Entity type** — corporation, partnership, LLC, sole proprietor, nonprofit. `[manual]`, and it determines the entire component structure in Step 1.
2. **Reporting framework.** `[manual]`
3. **Share counts by class**, opening and every movement. `[manual]` — **the cap table.**
4. **The nature of any unusual equity movements**, which Step 0 will have surfaced.
5. **Treasury stock method** — cost or par value. `[manual]`, and it changes the reissuance accounting.
6. **Dividend declaration and payment dates**, and per-share amounts. `[manual]` for per-share; `[auto]` for the amounts and the payable movement.

**Decisions are the user's; state is the workspace's.**
