<!-- subsequent-events-asc855 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** A subsequent events conclusion adjusts issued financial statements or adds a disclosure to them. It also, characteristically, concerns **named customers who have failed to pay and named counterparties in dispute** — commercially sensitive information about third parties.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every procedure is `[manual]`, as the original assumed. Say that the transactional sweep did not run — **which matters, because it is the Type 1 half.** |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **An event at one entity can be a subsequent event for another.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — **a partial sweep produces a clean log, which is the most misleading possible output here.** |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On group events.** A subsequent event affecting a subsidiary is generally a subsequent event for the group, and the reverse is often true too. **Where several files are connected, sweep all in scope** — an insolvency of a customer who trades with two group entities is one event with two effects, and finding it in one ledger should prompt the check in the other.

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

**Batch independent reads.** The post-period transaction detail, the receivables position at the balance sheet date, the inventory position, the payables, and the provisions are independent. **Read the balance sheet date position and the post-period activity together** — the sweep works by comparing them.

### The `mock: true` flag

Fixture data has **no post-period insolvencies, no write-offs of pre-period receivables, and no credit notes against pre-period invoices.** The sweep returns nothing.

**And "nothing found" is this skill's headline output**, which makes fixture data uniquely misleading here — a clean subsequent events log is exactly what a real clean review produces. Label it in the file name and **at the head of the log**, not in a footnote.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The balance sheet date.** `[manual]` to confirm; `[auto]` from the fiscal calendar.
2. **The issuance or availability date, and which definition applies.** `[manual]` — see Step 1; it determines the window and the two definitions give different windows.
3. **Post-period activity** — board minutes, legal updates, major transactions. `[manual]` for the first two; **`[auto]` for the third.**
4. **Significant estimates** — reserves, impairments, contingencies. `[manual]` to identify; `[auto]` for the balances, **and these are the estimates the sweep tests.**
5. **Management's known events.** `[manual]`, **and this is the Type 2 half.** Ask specifically and by category — see Step 2's checklist — rather than open-endedly, because "has anything happened?" reliably produces "no."

**Decisions are the user's; state is the workspace's.**
