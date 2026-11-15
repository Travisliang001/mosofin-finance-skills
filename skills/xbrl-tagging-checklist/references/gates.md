<!-- xbrl-tagging-checklist · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** The tagged data is filed on EDGAR and consumed by machines — analysts' models, screening tools, regulators' systems. **A wrong figure in XBRL propagates further and faster than the same figure in the human-readable document**, because nobody reads it before it is used.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every step is `[manual]`, as the original assumes. **The reference figures must come from the filing's own supporting schedules.** Say so. |
| **Exactly one company file** | Confirm the `display_name` — **and confirm it is the registrant.** |
| **Several company files** | **The filing is consolidated.** See below — this is the same trap as `sec-10q-10k-prep`. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop; a partial reference set produces false tie-out differences. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**The consolidated-registrant point, restated because it is the likeliest error.** XBRL tags the **registrant's consolidated financial statements.** What the gateway returns is individual company files. **Where the consolidation is performed outside these books, the reference figures Mosofin can supply are component-level and are not what is tagged.** A component-level reference will disagree with every tagged consolidated figure, and the disagreement will look like a tagging error. **Establish the basis first.** See `consolidation-and-eliminations`.

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

**Batch independent reads.** The trial balance at both period ends, the roll-forward components, the dimension lists and the comparative period are independent. **Read the comparative period in the same batch** — XBRL tags both, and a comparative tagged from a stale figure is a common error.

### The `mock: true` flag

Fixture data supplies **reference figures that correspond to nothing being filed.** A tie-out against them is a tie-out against fiction.

Label it in the file name and at the head of the reference schedule. **And note the specific hazard here**: a reference schedule looks authoritative by design, and its whole purpose is to be trusted by a tagger who will not question it.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. XBRL tagging is a quarterly cycle with a highly stable tag map.

Interview for:

1. **The filing draft.** `[manual]` — Mosofin cannot read it.
2. **The taxonomy version** — the US GAAP taxonomy year in use. `[manual]`, **and it changes annually.**
3. **The prior filing's tag map.** `[manual]` — **and persist it**; it is the single most valuable artefact in this skill.
4. **Validation tool output**, where available. `[manual]`.
5. **Who performs the independent review.** `[manual]` — Step 5.

**Decisions are the user's; state is the workspace's.**
