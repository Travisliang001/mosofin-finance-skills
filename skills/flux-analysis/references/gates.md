<!-- flux-analysis · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace
  - Gate 1 — Discover live datasources and settle the entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile the entity, then interview the user

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1 settle
*which books this is about*: the workspace, and the data sources inside it. **Part A then explores
what those confirmed sources can actually do** and personalises the run around them. Nothing is
read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** Say so once, then run the skill
manually on data the user supplies.

Run Gates 0 → 1 → 2 → 3 in this order, before analysing anything. Do not skip a gate because a
previous conversation covered it: connections, permissions and company files change between
periods.

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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The flux runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every movement carries its entity's `display_name`. A
  consolidated flux is only as good as the eliminations behind it: if the user wants one, say
  that intercompany movements must net out and check that they do.

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they expose and which
of it serves this request** — the tool catalogue in Gate 2, then what is already known about this
entity plus whatever still has to be asked in Gate 3.

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

- **Read the real tool name from the catalog, never from memory.**
- **A near-substitute is not a substitute.** A trial balance gives balances but not the
  statement grouping; a summary P&L gives totals but not the postings behind a movement. If the
  ledger tool is disabled, the flux can flag movements but not explain them: say so, and mark
  every explanation "asked".
- **The comparison periods must come from the same tool and basis.** Two reads on different
  accounting methods (cash and accrual) make a false flux in every account.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: base currency, fiscal calendar (which decides what
"same month last year" means), accounting method.

**Ask the user** what actually changes the work — Stage 1's table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Period and comparison basis** | **Required** | Never default the period. |
| **Thresholds** | Recommended | Default to 10% and 1% of revenue (income statement) or of total assets (balance sheet), stated as defaults. |
| **Account owners** | Recommended — **[manual]** | Without them every question goes to the controller. |
| **Known events** | Optional — **[manual]** | Price changes, campaigns, one-offs: evidence the books do not hold. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the period
or the entity.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what
is new, changed, or contradicted. Thresholds and owners should not be re-asked every month.
