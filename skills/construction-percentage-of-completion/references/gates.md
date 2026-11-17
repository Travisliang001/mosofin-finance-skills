<!-- construction-percentage-of-completion · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before recognising anything. This ordering is the contract. Do
not skip a gate because a previous conversation covered it — connections, permissions, and company
files change between periods.

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

**Look for a connected project-management, job-costing or estimating platform.** It is the one thing
that would move the estimated cost at completion from `[manual]` to `[auto]`, and it would also supply
the output-method measures (surveys, milestones) that the accounting system cannot.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting exactly
  one `data_source_id`, and every contract carries its entity's `display_name`. **Construction groups
  frequently run one contract through several entities** — a main contractor and a specialist
  subsidiary — and see the cross-entity step, because the intercompany margin on such work is
  unrealised at group level.

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

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled —
  some underscored, some hyphenated.
- **The dimension tools decide whether this skill can run at all.** Classes, departments, projects and
  the customer field are how jobs are tagged. Check them first: if none is in use on cost
  transactions, per-contract costs are `[manual]` and the whole workpaper depends on supplied figures.
- **A near-substitute is not a substitute.** **Total cost of sales is not contract cost.** Allocating a
  company-wide cost total across contracts by any rule of thumb produces a percentage complete that is
  arithmetic rather than evidence — and since that percentage drives revenue, the revenue becomes
  fictional too. Do not do it.
- **Billings are not revenue.** The invoice history is `[auto]` and tempting, but under over-time
  recognition revenue is driven by progress, not by what was invoiced. Their *difference* is the WIP
  balance, which is the point of Step 8.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, country / region, and
**industry** — a construction classification supports the treatment but does not establish it.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Contracts in progress** — customer, scope, price, term | **Required — [gated]** | Customers and quoted amounts are often readable (*`search_customers`*, *`search_estimates`*); **the contract terms are [manual]**. |
| **Performance obligations per contract** | **Required — [manual]** | A judgment under the standard, not a ledger field. |
| **Total estimated costs at completion, per contract** | **Required — [manual]**, always | **The number everything depends on.** Ask for it per contract, with the date it was last revised and who revised it. |
| **Costs incurred to date** — per contract, by category | **Required — [auto] if jobs are tagged**, otherwise **[manual]** | See the check above. |
| **Billings to date** — per contract | **Required — usually [auto]** | Readable from invoice history by customer or job. |
| **Variable consideration** — variations, claims, bonuses, penalties | Recommended — **[manual]** | Including the constraint judgment. |
| **Measure of progress** — input (cost-to-cost) / output (units, milestones) | **Required — [manual]** | Output measures need site data the books do not hold. |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | |
| **Contract modifications** | If applicable — **[manual]** | With approval status; see the edge case. |
| **How jobs are tagged** — customer, class, project, department | **Required if costs are to be read** | Ask which dimension is the job code. |
| **Period being reported** | **Required** | Never default it. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | The cost estimates are the critical gap. Record which contracts have current estimates and which do not. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an estimated cost
at completion, a measure of progress, or the framework.

**On later runs**, read stored preferences first (Step 12), confirm in one line, and ask only what
changed. The job-tagging convention, the measure of progress and the contract register should persist;
**the cost estimates must be re-confirmed every period**, because a stale estimate is the single most
common cause of a POC misstatement.
