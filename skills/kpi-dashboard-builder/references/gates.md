<!-- kpi-dashboard-builder · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before selecting metrics. This ordering is the contract. Do not
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

**This gate determines which industry metrics are possible at all.** **Check for a connected billing,
subscription, CRM, e-commerce, time-tracking or production system.** Each one converts a block of the table
above from `[manual]` to `[auto]`. **Run the selection in Step 1 against what is actually connected**, not
against what the industry set lists — otherwise the dashboard is designed around metrics nobody can
populate.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`.
- **Multi-entity** — ask which set, **and whether the dashboard is per entity, consolidated, or both.**
  See the cross-entity step; **ratios do not consolidate by addition.**

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

Resolve **every KPI in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

**Resolve the capability map before selecting the metrics**, not after. **A dashboard tile with no data
source is worse than one fewer tile.**

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **Recognised revenue is not ARR**, and **revenue decline is not churn.** The central warning above.
  - **An invoice count is not a customer count**, and **a customer record is not an active customer.**
  - **Headcount from the employee list is not FTE**, and it is not billable headcount.
  - **A closed period's figures and an open period's are not comparable** — see the real-time edge case.
  - **A class or project is not a customer cohort.**
- **There is no billing system, no CRM, no web analytics, no time system and no production data on this
  surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, **fiscal calendar** — which decides
period boundaries — country / region, **industry**, which is a starting point for Step 1.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Entity industry and business model~~ | **Now [gated]** | **Industry `[auto]` from the profile where set**; the business model is the user's. |
| ~~Source data~~ — financials | **Now [auto]** | **Operational sources remain `[manual]`** unless connected. |
| **Audience** — board / executive / departmental / investor | **Required — [manual]** | **Ask first.** It decides depth and metric count. |
| **Period and frequency** — monthly, weekly, real-time | **Required** | **[gated]**: see the real-time edge case. |
| **Targets / benchmarks** per KPI | Recommended — **[gated]** | **Budgets may be readable; benchmarks are `[manual]`.** **Never invent either.** |
| **Existing KPIs tracked** | Recommended — **[manual]** | And **how they are currently defined**, which is where drift is discovered. |
| ~~Historical data~~ | **Now [auto]** | **How many periods exist is itself a finding** — see the insufficient-history edge case. |
| **Which operational systems exist**, connected or not | **Required — Mosofin addition** | Decides whether industry metrics are possible at all. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether the dashboard is per entity or consolidated. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a SaaS model with no deferred revenue balance. |
| **Confirm manual evidence** | **Required** | Operational metrics, targets and benchmarks are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a target, a benchmark,
or a metric definition.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
The metric set, the definitions, the query recipes, the targets and the layout persist; **every value is
recomputed.**
