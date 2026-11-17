<!-- esg-sustainability-reporting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace
  - Gate 1 — Discover live datasources and settle the entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile the entity, then interview the user

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.

Run Gates 0 → 1 → 2 → 3 in this order, before computing anything. This ordering is the contract. Do not
skip a gate because a previous conversation covered it — connections, permissions, and company files
change between periods.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a client-side
`mcp__…` namespace; that string is composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with `workspace_ids=[…]`
  and `mode="single"` / `mode="multi"`.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the opaque
`ws_…` handle.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Check for a connected sustainability, carbon-accounting, HR or utility platform.** Any of these would
convert a large part of this skill's `[manual]` half — a carbon platform holds the factors and the physical
data; an HR system holds the social metrics. Their absence is itself worth stating in the coverage sheet.

**Then treat the connected list as a boundary question, because that is what it is here.** Ask:

- **Single-entity** — one company file, one reporting boundary.
- **Multi-entity** — which set. And then the ESG-specific question: **is the reporting boundary the same
  as the financial consolidation boundary?** Often it is not. Groups report ESG for sites they operate but
  do not own, or exclude entities they consolidate. See the cross-entity step.

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Discover enabled tools → build the capability map


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


For **each in-scope datasource** (and **per company file** when several are live — pass
`data_source_id`), call `get_datasource_tools`. Bucket every tool by `effective_policy`:

| `effective_policy` | The task becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Pull the evidence directly. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and ask the user to supply that evidence another way. |

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute.** This is the skill where that rule does the most work:
  - **Utility spend is not energy consumption.** Currency is not kWh.
  - **Fuel spend is not litres**, and litres are what the factor needs.
  - **Vendor count is not supply-chain coverage.**
  - **Employee count is not a workforce diversity metric.**
  - **A spend-based estimate is not a measurement.** It is the lowest-quality tier in every recognised
    data-quality hierarchy, and it must be labelled as such wherever it is reported.
- **There is no emission factor, no physical quantity and no social datum on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency — which matters, since spend-based
factors are currency-specific — fiscal calendar, country / region, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **ESG reporting goal** — stakeholder needs, compliance vs. voluntary | **Required — [manual]** | **Ask first.** A regulatory disclosure and a website page have completely different evidence bars. |
| **Current metrics** — what is tracked today | **Required — [manual]** | The honest starting point; most entities track less than they think. |
| **Organizational boundaries** — entities and sites included | **Required — [gated]** | The **entities** are partly readable from Gate 1; the **sites** are not. |
| **Activity data sources** — utility bills, travel, procurement, HR | Recommended — **[gated]** | Procurement and travel are **[auto]** as *spend*; utilities and HR are `[manual]` as *quantities*. |
| **Prior disclosures** — ESG report / website metrics | Recommended — **[manual]** | Needed for consistency, and because a previously published figure constrains you. |
| **Framework, if any** | Recommended — **[manual]** | Decides the metric catalog's shape and what is mandatory. |
| **Emission factor source** | **Required if reporting emissions — [manual]** | Ask for **source, version and year**. Never supply one. |
| **Consolidation approach** — equity share vs. operational / financial control | **Required if multi-entity — [manual]** | Determines whose emissions count as yours. |
| **Assurance intent** — is this going to be assured, and to what level | Recommended — **[manual]** | Changes the control design in Step 3 substantially. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and **whether the ESG boundary matches**. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Every factor and every physical quantity is `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an emission factor,
a boundary, a consolidation approach, or a physical quantity.

**On later runs**, read stored preferences first (Step 5), confirm in one line, and ask only what changed.
The metric catalog, the boundary, the category mapping and the control design persist; **the activity data,
the factors and the resulting metrics are re-obtained every period**.
