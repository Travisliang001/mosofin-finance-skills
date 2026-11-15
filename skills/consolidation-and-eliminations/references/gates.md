<!-- consolidation-and-eliminations · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace
  - Gate 1 — Discover live datasources and settle the entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile each entity, then interview the user

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.

Run Gates 0 → 1 → 2 → 3 in this order, before consolidating anything. This ordering is the contract.
Do not skip a gate because a previous conversation covered it — connections, permissions, and company
files change between periods, and in a group they change often.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a client-side
`mcp__…` namespace; that string is composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with `workspace_ids=[…]`
  and `mode="single"` / `mode="multi"`. A group's entities may legitimately span workspaces.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the opaque
`ws_…` handle.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

**This gate is the heart of this skill.** The connected list is the candidate consolidation group, and
reconciling it against the *legal* group structure is the first substantive act of the
consolidation:

- `connected: true` → **available to consolidate**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.
- **An entity in the legal group with no connected company file is a gap, not an omission.** Ask the
  user for its trial balance and mark it `[manual]`. **Never produce consolidated statements that
  silently exclude a group member** — the result is not the group's financials.
- **A connected company file that is not in the consolidation group** — a dormant entity, an
  associate, a client's file — must be **excluded deliberately**, not consolidated because it happened
  to be connected. Confirm the list against the org chart.

Ask the user to **confirm the group membership by `display_name`**, and record the role of each:
parent, consolidated subsidiary, equity-method associate, or out of scope.

This skill is **inherently multi-entity**. Every call targets exactly one `data_source_id`, and every
figure carries its entity's `display_name` until the moment it is deliberately combined.

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Discover enabled tools → build the capability map


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


For **each in-scope entity** — pass `data_source_id` every time — call `get_datasource_tools`. Bucket
every tool by `effective_policy`:

| `effective_policy` | The task becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Pull the evidence directly. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and ask the user to supply that evidence another way. |

Resolve **every task in Part B** against these buckets, **per entity**. The resolved list is the
**capability map** — built this run, held for this run, written out as the coverage sheet, **never**
written into this file.

Rules that bite hardest here:

- **Capability is per company file, and in a group it varies a lot.** A newly acquired subsidiary
  often has narrower permissions than the parent. **One entity's trial balance being `[manual]` makes
  the whole consolidation partly manual** — say which entities are evidenced and which are supplied.
- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled, and
  a group may span platforms with different naming.
- **A near-substitute is not a substitute.** A **balance sheet and P&L** are not a **trial balance**:
  consolidation needs account-level detail on both sides to sum entities line by line and to locate
  the intercompany accounts. Reports are pre-classified and will not sum correctly across entities
  with different chart structures.
- **Pull every entity at the same date and on the same accounting method.** This is easy to get wrong
  and produces a consolidation that will not balance for reasons nobody can find later.

## Gate 3 — Profile each entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) **for every in-scope
entity**.

**Derive silently** what the profiles answer — and this is genuinely useful here:

- **Each entity's legal name and country**
- **Each entity's base currency** — which gives the **functional currency candidates** for Step 3
  and immediately tells you whether translation is needed at all
- **Each entity's fiscal year end** — differences matter (see the edge case)

**Ask the user** what actually changes the work — the original Inputs table, minus what the profiles
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Trial balance for each entity** | **Required — [auto] per connected entity**, **[manual]** for any unconnected group member | Pull all at the same date and accounting method. |
| **Group structure / ownership percentages** | **Required — [manual]** | Not in the books. Drives NCI entirely. Ask for the org chart with percentages and the parent of each entity. |
| **Functional currency per entity** | **Required — [gated]** | Base currency is **[auto]**; **functional currency is a judgment** about the primary economic environment and may differ. Confirm. |
| **Group presentation currency** | **Required — [manual]** | |
| **FX rates** — closing, average, and historical | **Required if multi-currency — [manual]**, always | No accounting datasource supplies rates. Ask for each rate with its source and date. |
| **Intercompany balances and transactions** | **Required — [auto] where both sides are connected**, otherwise **[manual]** | See `intercompany-reconciliation`. **Measure the mismatch before eliminating.** |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | Drives the NCI measurement option and several treatments. |
| **Acquisition details** — fair value adjustments, goodwill | Required if applicable — **[manual]** | |
| **Prior period consolidated balances** | Recommended — **[manual]** | For continuity and the NCI roll-forward opening. |
| **Consolidation date and period** | **Required** | Never default. Applied identically to every entity read. |
| **Confirm group membership and each entity's role** | **Required** | Parent / consolidated / equity-method / out of scope, by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | E.g. differing fiscal year ends. |
| **Confirm manual evidence** | **Required** | Ownership, rates and acquisition values will all be `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default ownership
percentages, FX rates, the framework, the presentation currency, or the group membership.

**On later runs** — consolidation is monthly or quarterly — read stored preferences first (Step 11),
confirm in one line, and ask only what changed. The group structure, ownership percentages and
account mappings should not be re-asked; **the rates always are**, and the trial balances are always
re-read.
