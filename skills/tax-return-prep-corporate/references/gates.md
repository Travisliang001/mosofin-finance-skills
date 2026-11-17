<!-- tax-return-prep-corporate · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** A corporate tax return is filed by **one legal entity** for **one tax year**. It is signed, it carries penalties, and it is not casually amended. Building it on the wrong entity's results is not a correctable slip.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every figure is `[manual]`. The computation framework applies in full. |
| **Exactly one company file** | Confirm the `display_name` — **and confirm it is the filing entity.** |
| **Several company files** | **Group filing changes the question entirely.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — **an incomplete starting point produces a wrong return.** |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On groups, which the edge cases flag twice.**

Whether the return is filed **entity by entity** or on a **consolidated / group basis** is a jurisdictional and structural fact, and it determines what the starting point even is:

- **Separate filing**: each entity's own pre-tax profit is the starting point. `[auto]` per entity. **Group relief** — the surrender of losses between group companies — is then a `[manual]` overlay requiring the other entities' positions.
- **Group or consolidated filing**: the starting point is a **consolidated** figure, and consolidation generally happens outside these books. **Reading several ledgers is not consolidating them** — there are no eliminations in what comes back.

**Establish which before reading anything**, and note the second reason it matters: **intra-group transactions are transfer pricing matters** regardless of how the return is filed. See the transfer pricing documentation and `consolidation-and-eliminations`.

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

**Batch independent reads.** The final trial balance, the full expense ledger, depreciation and amortisation accounts, asset additions and disposals, interest expense, the tax accounts and payment history are independent. One message.

### The `mock: true` flag

Fixture data has **a clean final trial balance, tidy depreciation, and no awkward expense categories.** So the completeness sweep in Step 2b finds nothing and the finality check in Step 1b passes.

Label it in the file name and on the computation summary. **A tax computation on fixture data is an arithmetic demonstration, not a return.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. A corporate return is annual, with a structure that changes rarely.

Interview for:

1. **Jurisdiction(s), tax year and filing entity.** `[manual]`
2. **Current rates and rules.** `[manual]`, current-sourced, **never carried forward.**
3. **The disallowable schedule for this jurisdiction.** `[manual]` — **which categories are disallowed, and to what extent.**
4. **Capital allowance pools, rates and elections.** `[manual]`
5. **Loss carryforwards and carrybacks, by type and year, with restrictions.** `[manual]` — **tax attributes, not ledger balances.**
6. **Credits available.** `[manual]`
7. **The prior year return** — for continuity, attributes and elections. `[manual]`
8. **Group and related party information.** `[manual]`

**Decisions are the user's; state is the workspace's.** And filing is the qualified preparer's.
