<!-- segment-reporting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Segment disclosures are consolidated disclosures, they are filed, and they identify major customers by revenue share. Getting the entity wrong produces a disclosure about a different business, with a different customer concentration, in a public document.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Everything is `[manual]`. The framework applies in full; nothing is measured. Say so. |
| **Exactly one company file** | Confirm the `display_name`. Segments are then dimensions **within** that file — see the note below. |
| **Several company files** | **Legal entities may or may not be the segments.** See below. This is the most interesting case and the easiest to get wrong. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — a segment missing from the data fails the 75% coverage test invisibly. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

### Legal entities are not segments either

**A second near-substitute, and it is seductive when several company files are connected.**

It is tempting to treat each connected company file as a segment. Sometimes that is right — many groups are organised so that each business runs in its own entity, and the CODM reviews them that way.

**But it is a coincidence of structure, not a rule.** Legal entities exist for tax, liability and historical reasons. Segments exist because of how management runs the business. A group can have:

- **one entity containing three segments** — the dimension case
- **three entities forming one segment** — a business that happens to be spread across legal vehicles
- **entities that cut across segments entirely** — a shared services company serving all of them

**Ask the CODM question first, then map it onto whatever combination of entities and dimensions answers it.** And note the practical consequence: where a segment spans several company files, its P&L requires reading all of them and **eliminating between them**, which is a consolidation and not a sum. See `consolidation-and-eliminations`.

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

**Batch independent reads.** The dimension list, the chart, revenue by customer, revenue by dimension, the balance sheet by dimension and the comparative period are independent. One message — **and read the comparative period in the same batch**, because Step 8 needs it and fetching it later doubles the work.

### The `mock: true` flag

Fixture data has **tidy dimensions with no uncoded transactions and no customer concentration.** So the completeness check passes, the reconciliation ties, and the major-customer test finds nothing — all by construction.

Label it in the file name and on Sheet 1.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

**Then do one read before the interview**, because it makes the interview far better: **pull the dimension list** — classes, locations, departments, projects, whatever the book carries — with the revenue and cost coded to each.

Now interview:

1. **Who is the CODM?** `[manual]`, and it is the first question. **It may be the CEO, a management committee, a divisional board.** The answer determines everything downstream.
2. **What reports does the CODM actually review?** `[manual]` — and this is the operative question, not "what does the org chart say."
3. **How do the CODM's reports compare to the dimensions in the book?** `[manual]` to conclude — **and this is where the dimension read earns its place**, because "here are the eight classes your ledger tracks; does the CODM see these, or something else?" is a far more productive question than an open one.
4. **What profit measure does the CODM use?** `[manual]`. See Step 4.
5. **Which of the Step 5 items does the CODM actually see?** `[manual]` — **only those need disclosing**, and disclosing more misrepresents the approach.
6. **The framework** — ASC 280 or IFRS 8. `[manual]`
7. **Intersegment pricing basis.** `[manual]` — a policy, not a posting.

**Decisions are the user's; state is the workspace's.** The ledger says how things are coded. Only management says how the business is run.
