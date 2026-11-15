<!-- cost-accounting-process-costing · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before costing anything. This ordering is the contract. Do not
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

**Check every connected row for a manufacturing, MES, ERP-production or inventory platform.** This is
the highest-value check in the gate for this skill: such a system holds units, batch progress and
completion percentages — the entire `[manual]` half. Without one, this skill runs on supplied
quantities.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting exactly
  one `data_source_id`, and every department and cost pool carries its entity's `display_name`. **A
  process that spans entities** — one company's department transferring part-finished goods to another's
  — is an intercompany transfer, not a departmental one, and the margin on it is unrealised at group
  level. See the cross-entity step.

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
- **The dimension tools carry the departments.** Whether cost can be split by process at all depends on
  whether departments or classes are used on production postings. Check first.
- **A near-substitute is not a substitute, and here the temptation is specific.** **A dollar balance is
  not a unit count.** WIP of $180,000 tells you nothing about how many units are in process or how far
  through they are — and dividing a WIP balance by a standard cost to *infer* units is circular, since
  that standard cost is what the exercise is meant to produce. **Never derive equivalent units from
  money.**
- **An item quantity on hand is not work in process.** Inventory item counts, where available, describe
  finished or raw stock, not part-processed batches.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, country / region, and
**industry** — a process-manufacturing classification supports the method choice but does not decide it.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Departments / processes** — ordered list (Dept A → Dept B → …) | **Required — [gated]** | The dimension values are **[auto]**; **the production sequence is [manual]**, and the order matters because cost flows downstream. |
| **Beginning WIP** — units, % completion, costs (DM, conversion) | **Required — units and % [manual]; costs [auto]** | The cost carried is in the WIP account; the units and completion are not. |
| **Units started / completed** — units in / out by department | **Required — [manual]** | Production data. |
| **Ending WIP** — units, % completion | **Required — [manual]** | |
| **Costs added** — direct materials, labor, overhead by department | **Required — usually [auto]** | Readable by department where postings carry the dimension. |
| **Method** — weighted-average or FIFO | **Required — [manual]** | Changes the equivalent-unit computation entirely. Confirm; consistency period to period matters more than the choice. |
| **Where materials are added** — start, mid-process, or evenly | **Required — [manual]** | Drives the material equivalent-unit percentage. |
| **How departments are tagged** — department, class, location | **Required if costs are to be split** | Ask which dimension is the process. |
| **Normal spoilage / yield expectations** | Recommended — **[manual]** | Needed for the units tie-out; see the quality checks. |
| **Period being reported** | **Required** | Never default it. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Every unit and every percentage is `[manual]`. Record who supplied them and when the count was taken. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a completion
percentage, a unit count, the method, or the material addition point.

**On later runs**, read stored preferences first (Step 8), confirm in one line, and ask only what
changed. The department sequence, the method, the material addition points and the account map persist;
**every unit count and completion percentage is supplied afresh each period**.
