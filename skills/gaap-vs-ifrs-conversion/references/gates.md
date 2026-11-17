<!-- gaap-vs-ifrs-conversion · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before converting anything. This ordering is the contract. Do not
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

Settle the entity scenario — and here the reason for conversion decides it:

- **Single-entity** — one company file converted from one framework to another.
- **Multi-entity** — **the common case, because the commonest reason for conversion is group reporting
  alignment**: subsidiaries on local GAAP feeding a parent that reports under IFRS. Ask which entities, and
  **which framework each one currently reports under** — they may differ from each other. See the
  cross-entity step.

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
- **A near-substitute is not a substitute:**
  - **A balance is not a policy.** The whole skill turns on this.
  - **An account's absence is not proof a policy was not applied** — but it is a strong scoping signal, and
    it should be reported as a signal.
  - **The platform's reports are not framework statements.** See `financial-statement-builder`; presentation
    differences are a whole category here.
  - **An inventory balance does not reveal its costing method.** Note, though, that **many accounting
    platforms support only one costing method**, which — if the entity uses the platform's own inventory
    module — may itself answer the LIFO question. **Confirm with the user rather than inferring.**
- **There is no accounting policy manual, no lease register, no fixed-asset register and no valuation on
  this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and year-end,
country / region — **and note that the country is a strong hint at the source framework, not a statement of
it.**

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Source financial statements~~ | **Now [auto]** | Trial balance, balance sheet and P&L from the connected file. |
| **Source framework and target framework** — From → To | **Required — [manual]** | **The books do not declare a framework.** Ask, then check for contradictions. |
| **Detailed accounting policies** — how key items are currently accounted for | **Required — [manual]** | **The core input.** Ask area by area, guided by the `[auto]` scoping. |
| **Supporting schedules** — leases, inventory, PP&E, R&D, financial instruments | **Required for affected areas — [manual]** | Ask only for the areas scoping showed are live. |
| **Reason for conversion** — group reporting / listing / first-time adoption | **Required — [manual]** | Decides whether IFRS 1 applies and whether this is one-off or ongoing. |
| **Materiality** | Recommended — **[gated]** | Balance sizes are `[auto]`; the threshold is the user's. |
| **Transition date**, if first-time adoption | If applicable — **[manual]** | For IFRS 1. |
| **Whether dual reporting will be ongoing** | **Required — Mosofin addition** | Changes the deliverable from a conversion to a process. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, **each with its current framework**. |
| **Confirm any profile or account contradiction** | **Required if one appears** | e.g. a revaluation surplus in books said to be US GAAP. |
| **Confirm manual evidence** | **Required** | Every policy and schedule is `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch** — **and ask it after the scoping read**, so you are asking about the three areas
that apply rather than all ten. Propose defaults where reasonable — but **never** default a framework, a
policy, or a costing method.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
The applicable difference areas, the policy positions, the classification of each difference and the
adjustment methodology persist; **the balances and the adjustment amounts are re-obtained every period**.
