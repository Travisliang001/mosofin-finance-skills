<!-- cost-accounting-job-order · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Look for connected payroll, inventory or project-management platforms.** Each closes a specific gap:
payroll supplies labour **rates**, inventory supplies **material issues** as distinct from purchases,
and project management supplies **machine hours** and cost-to-complete estimates.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting exactly
  one `data_source_id`, and every job carries its entity's `display_name`. **Overhead rates are
  entity-specific** — a rate built from one entity's pool and applied to another's jobs allocates costs
  that entity never incurred. See the cross-entity step.

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
- **The dimension tools decide whether this skill can run.** Jobs are tagged using customers, classes,
  projects or departments. Check which is in use before anything else; without a job dimension, costs
  by job are `[manual]` in full.
- **The time-tracking tool is what makes labour real.** Where it exists, hours by job are `[auto]` and
  the labour-hours allocation base is genuinely measurable. Where it does not, both direct labour and
  the base become `[manual]`.
- **A near-substitute is not a substitute.** **Total cost of sales is not job cost**, and allocating it
  across jobs by any convenient rule produces margins that are arithmetic rather than measurement.
  Likewise **a purchase is not a material issue**: buying material and consuming it on a job are
  different events, and treating the first as the second charges jobs for stock still sitting in the
  yard.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, country / region, and
**industry** — which suggests the likely allocation base (labour hours in services and field work,
machine hours in manufacturing).

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Job list** — job ID, customer, start / end dates, status | **Required — [gated]** | The dimension values are **[auto]**; **job status (open / closed) is often [manual]** and is what the stranded-WIP test needs. |
| **Direct materials** — issues to job (qty, cost, dates) | **Required — [gated]** | Purchases coded to a job are **[auto]**; true inventory *issues* need an inventory system. |
| **Direct labor** — timecards (hours, rates, job IDs) | **Required — [gated]** | **Hours [auto]** where time is tracked; **rates [manual]** without payroll. |
| **Overhead costs** — GL accounts to include in the pool | **Required — [gated]** | The accounts and balances are **[auto]**; **which accounts belong in the pool is [manual]** and is a real decision. |
| **Allocation base** — labor hours, labor dollars, machine hours, etc. | **Required — [manual]** | Labour hours and dollars are measurable; machine hours are not. |
| **Budgeted overhead and budgeted base** (for a predetermined rate) | **Required if using a predetermined rate — [gated]** | A budget held in the system is **[auto]**; otherwise **[manual]**. |
| **Revenue model** — T&M, fixed fee, POC, milestones | Recommended — **[manual]** | Determines how cost relates to revenue and whether percentage-of-completion accounting applies. |
| **Inventory / WIP policy** — capitalization rules, cutoff | Recommended — **[manual]** | |
| **How jobs are tagged** — customer, class, project, department | **Required if costs are to be read** | Ask which dimension is the job code. |
| **Period being reported** | **Required** | Never default it. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Labour rates, machine hours and the pool composition will be `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the overhead rate,
the allocation base, or which accounts sit in the pool.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what
changed. The job-tagging convention, the pool composition and the allocation base persist; **the rate
is re-derived** and **the untagged-posting test is re-run every period**.
