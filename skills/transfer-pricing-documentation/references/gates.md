<!-- transfer-pricing-documentation · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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
   - Multi: **this is the normal case here** — ask which entities, then `list_workspaces(workspace_ids=[<ws_...>, ...], mode="multi")`.

Refer to a workspace by **name**, or by the opaque `ws_...` handle. Never print the internal numeric id, never ask for it, and if it appears in an error, name the workspace instead.

**Why this gate matters here.** Transfer pricing documentation is filed with tax authorities in multiple jurisdictions and is the basis on which a group defends its tax position. It is also **inherently multi-entity** — this is one of the few skills in the pack where the multi-workspace answer is the expected one.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace(s).

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Everything is `[manual]`, as the original assumes. The framework applies in full. |
| **One entity connected** | **Only one side of every controlled transaction is readable.** Useful, and half a picture — see below. |
| **Several entities connected** | **The good case.** Flows readable from both sides; the inventory can be built for completeness. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **An incomplete inventory is the specific failure this skill's `[auto]` half exists to prevent**, so stop. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

### The connected set is a floor, never the group

**Important, and the same logic as `related-party-disclosures-asc850`.**

The entities connected to the workspace are a **subset** of the group. A controlled transaction with an entity that is not connected is **invisible** — and that is a common situation, because groups connect their operating companies and not necessarily their IP holding company, their finance company, or a dormant entity that nonetheless charges a royalty.

**So:**

- **`[auto]` builds a complete inventory of flows *between connected entities*.**
- **It cannot establish that the inventory is complete for the group**, which is what the documentation requires.
- **Ask for the full group structure** — Input row 1 — and **reconcile the connected set against it**, listing which entities' flows could not be read.

**One-sided reading is still worth doing** and must be labelled: a flow visible in one entity's books, with the counterparty unreadable, tells you the transaction exists and what one party recorded. **It does not tell you the other party recorded the same thing** — and a mismatch between the two sides is both a reconciliation problem and a TP documentation problem, since two jurisdictions would be taxing inconsistent figures.

---

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Map what you can actually do


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


Call `get_datasource_tools` for **each** company file in scope and read the **`effective_policy`** on each tool.

| `effective_policy` | Verdict | Behaviour |
|---|---|---|
| `enabled` | `[auto]` | Call it. Batch with other independent reads. |
| `permission` | `[gated]` | Expect `approval_required`. Explain what and why, get a yes, re-invoke with `approved=true`. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | `[manual]` | Not available. The step remains; the user performs it. |

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run. Do not carry a capability map between runs.

**Policies can differ per entity.** A group may expose one subsidiary's ledger fully and another's under permission. **Record the map per entity**, because a transaction readable from one side and gated on the other is a different situation from one readable from both.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry the correct `data_source_id` on each invocation — **and note that in a multi-entity run, carrying the wrong one is an easy and silent error.**

**Batch independent reads.** Each entity's income statement, its intercompany accounts, its payroll and headcount cost, its asset base and its multi-year results are independent. **Read all entities and several years together** — TP analysis is multi-year by convention.

### The `mock: true` flag

Fixture data has **matched intercompany flows, tidy margins, and no loss-making entities.** So the completeness sweep finds a clean inventory, both sides agree, and the loss-making-tested-party test passes.

Label it in the file name and on the transaction inventory. **A TP study on fixture data is a template.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. A TP study is annual and its structure is highly stable — the functional analysis in particular changes only when the business changes.

Interview for:

1. **The full group structure** — entities, jurisdictions, ownership. `[manual]`, and it bounds the connected set.
2. **The functional analysis** — functions, assets, risks per entity. `[manual]`, and it is the heart of the study.
3. **Existing intercompany agreements.** `[manual]` — documents.
4. **Jurisdiction documentation requirements** — thresholds, deadlines, local rules. `[manual]`, **current-sourced.**
5. **Comparable data** — database access or provided comparables. `[manual]`.
6. **Prior TP documentation.** `[manual]`, and **persist the conclusions**; consistency year to year is itself defensive.

**Decisions are the user's; state is the workspace's.** And the conclusion is the specialist's.
