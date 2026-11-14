<!-- budget-builder · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before building anything. This ordering is the contract.
Do not skip a gate because a previous conversation covered it — connections, permissions, and
company files change between periods.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a client-side
`mcp__…` namespace; that string is composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with
  `workspace_ids=[…]` and `mode="single"` / `mode="multi"`.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the opaque
`ws_…` handle.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`. A budget
  built on a partial group understates both the revenue and the cost base.

A workspace can connect the **same platform several times** — several company files, plus
payments or payroll platforms. Each is its own row with its own `data_source_id` and
`display_name`.

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every driver, line and assumption carries its entity's
  `display_name`. **Budget each entity in its own functional currency and consolidate at budgeted
  FX rates** — this is the original's own edge case, and it is the default behaviour here, not an
  exception.

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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability
map** — built this run, held for this run, written out as the coverage sheet, **never** written
into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some underscored, some hyphenated.
- **Check specifically whether a budget-reading tool is listed and enabled.** If it is, read the
  existing budget before building anything — replacing an approved budget the user forgot to
  mention is a genuine and avoidable harm. If it is not, ask whether a budget already exists.
- **A near-substitute is not a substitute.** An **annual** P&L cannot supply seasonality; only a
  **monthly** breakdown can. If the report tool will not break down by month, say the seasonal
  shape is unevidenced and ask the user for the pattern, rather than dividing by twelve and
  presenting it as a monthly budget.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers, and do not ask about it:

- **Functional currency** — the base currency the books are kept in
- **Fiscal calendar and year-end** — which defines the budget year's start and end months. Getting
  this wrong shifts every seasonal assumption by however many months the year-end differs
- Country / region, time zone
- **Industry** — which suggests which of the Step 2 revenue models fits

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Budget period** — fiscal year, monthly / quarterly granularity | **Required** | Never default it. Confirm against the profile's year-end. |
| **Prior year actuals** — by month, by line | **Required for incremental / driver methods — usually [auto]** | Normally pulled. Ask for at least 24–36 months if seasonality matters. |
| **Budgeting method** — incremental / zero-based / driver-based | **Required** | Often a hybrid; ask per area, not once. |
| **Revenue drivers** — units, price, customers, churn, pipeline | **Required — [manual]** | Historical *outcomes* are readable; the *plan* is not. Show the history, then ask what changes. |
| **Headcount plan** — existing + planned hires by role, timing, comp | **Required for most entities — [manual]** | The employee list may pull; compensation and hiring plans do not. |
| **Known commitments** — contracts, leases, committed spend | Recommended — **[manual]** | **[auto]** as a proxy: recurring vendor spend shows what is contractually sticky. |
| **Strategic initiatives** — new products, markets, projects with budgets | Recommended — **[manual]** | |
| **Inflation / escalation assumptions** | Recommended — **[manual]** | **Do not assume a rate.** Ask, or leave the line flat and say so. |
| **Approval structure** — who owns which budget lines | Recommended — **[manual]** | Each department line needs an owner who will defend it. |
| **Strategic targets** — growth, margin, profitability, cash burn | Recommended — **[manual]** | Needed for Step 8. |
| **Does a budget already exist?** | **Required** | Ask, and check the system. Extending beats replacing. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Drivers, hiring plan and targets will all be `[manual]`. Record what was not supplied. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the period,
the drivers, the inflation rate, the tax rate, the payroll loading rate, or the entity.

**On later runs** — budgeting is annual, so "later" means next year — read stored preferences
first (Step 10), confirm in one line, and ask only what is new, changed, or contradicted. Last
year's driver structure, department map and assumption register should be the starting point.
