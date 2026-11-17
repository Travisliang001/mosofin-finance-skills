<!-- internal-audit-workpaper · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before planning fieldwork. This ordering is the contract. Do not
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

**An excluded entity is a scope limitation**, in the precise audit sense of the edge cases — **not a
footnote.** It restricts access to evidence and it therefore limits the conclusion. **Document it as a scope
limitation and state its effect**, exactly as the standard requires.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`.
- **Multi-entity** — ask which set, **and whether the audit covers the group or one entity.** An audit of
  "the procurement process" across a group is a different engagement from one covering a single company.
  See the cross-entity step.

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

**In this skill the capability map is an audit planning document.** It says which procedures can be
performed from the workspace, which need a person, and — where a tool is `disabled` — **which evidence is
unavailable, which is a scope limitation to be documented rather than worked around.**

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **Recorded is not correct, and recorded is not complete.** The ledger is one side of the evidence.
  - **An analytical procedure is not a test of controls.** Finding no anomalies does not mean the control
    operated; see `sox-controls-design-and-testing`.
  - **A query result is not a conclusion.** The auditor concludes.
  - **A system record is not an approval.** Unless approval is captured as a field, the evidence of
    authorisation is elsewhere.
- **There is no confirmation capability, no physical observation and no interview on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and year-end,
country / region, industry.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Audit subject / area** — the process, function or area | **Required — [manual]** | |
| **Audit objectives** — what the audit aims to assess | **Required — [manual]** | **Ask first.** Everything links back to these. |
| **Audit type** — operational / financial / compliance / IT | **Required — [manual]** | Changes the procedures and the reporting; see the edge cases. |
| **Risk assessment / why this audit** | Recommended — **[manual]** | The drivers that justify the focus. |
| **Process information** — how the area operates | **Required — [manual]** | **Not in a ledger.** Walkthroughs and process documentation. |
| **Relevant criteria** — policies, regulations, standards | **Required — [manual]** | **The "should be" half of every finding.** Without criteria there are no findings, only observations. |
| **Prior audit results** | Recommended — **[manual]** | **Repeat findings rate higher**; see Step 6. |
| ~~Data / evidence available~~ | **Now largely [auto]** | Transactions and records in the connected file. **State which fields exist before designing tests around them.** |
| **Whether completeness is in scope** | **Required — Mosofin addition** | If so, an external reference point is needed. |
| **Independence position** | **Required — Mosofin addition** | Who is performing the audit, and whether they operated the area. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, **and any excluded entity as a scope limitation**. |
| **Confirm manual evidence** | **Required** | Criteria, process information and prior results are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the criteria, a risk
rating, or a root cause.

**On later runs**, read stored preferences first (Step 11), confirm in one line, and ask only what changed.
The program, the criteria references, the test definitions and the rating scale persist; **every population,
result and finding is re-obtained each engagement.**
