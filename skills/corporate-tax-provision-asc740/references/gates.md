<!-- corporate-tax-provision-asc740 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Tax is jurisdictional, and jurisdiction usually follows legal entity.** So the connected entity list
maps closely onto the tax jurisdictions in play — ask the user to confirm **which jurisdiction each
entity is taxed in**, since that is the fact that determines its rate.

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The provision runs **once per entity and jurisdiction**, every call
  targeting exactly one `data_source_id`, and every figure carries its entity's `display_name`.
  **Deferred tax balances belong to the entity that will pay or save the tax**, and **rates differ by
  jurisdiction**, so nothing may be pooled before the per-entity computation is complete. See the
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
- **A near-substitute is not a substitute, and here it is a category error.** **Book values are not tax
  values.** The ledger gives book depreciation, book accruals, book carrying amounts — the *other half*
  of every temporary difference lives in the tax computation and is `[manual]`. Never present a book
  balance as a temporary difference; a temporary difference is the *gap* between two bases, and the
  workspace holds only one of them.
- **Check whether the P&L can be filtered by class, department or entity.** That determines whether
  pre-tax income can be split by jurisdiction automatically or must be supplied.
- **There is no tax-rate tool.** Do not look for one.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, **country / region** — which *suggests* the
tax jurisdiction but does not establish it, since an entity can be taxed elsewhere — base currency, and
**fiscal year end**, which defines the provision period.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Pre-tax book income** — by entity / jurisdiction | **Required — [auto] in total, [gated] by jurisdiction** | Pulled. Ask how jurisdictions map to entities or dimensions. |
| **Statutory tax rate(s)** — per jurisdiction, current year | **Required — [manual]**, always | **User-supplied or current-sourced.** Ask for each rate **with its source and the year it applies to**. Never supply one from memory. |
| **Enacted future rate(s)** for deferred measurement | **Required — [manual]** | May differ from the current rate; see Step 5 and the rate-change edge case. |
| **Permanent differences** | **Required — [gated]** | Candidates detectable by account; **the determination is [manual]**. |
| **Temporary differences** | **Required — [gated]** | Book side **[auto]**; **tax basis [manual]**. |
| **Opening deferred tax balances** — prior period DTA/DTL detail | **Required — [auto] in total, [manual] by component** | The account balance is readable; the component detail behind it usually is not. |
| **Tax attributes** — NOLs, credits, carryforwards with expiration | Recommended — **[manual]** | From the tax returns, not the books. |
| **Valuation allowance assessment inputs** — evidence of future taxable income | Recommended — **[gated]** | **Cumulative loss history is [auto]**; forecasts and tax-planning strategies are **[manual]**. |
| **Uncertain tax positions** — positions and assessments | Recommended — **[manual]** | |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | The DTA treatment differs materially — see Step 6. |
| **Multi-jurisdiction detail** | If applicable | Which entity is taxed where, and any tax holidays or incentives. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, with each one's jurisdiction. |
| **Confirm any profile contradiction** | **Required if one appears** | E.g. the entity is incorporated in one country and taxed in another. |
| **Confirm manual evidence** | **Required** | Every rate, every tax basis, every NOL. Record which are supplied and which are outstanding. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a tax rate, a tax
basis, the framework, or the jurisdiction.

**On later runs** — this is annual, with interim provisions between — read stored preferences first
(Step 12), confirm in one line, and ask only what changed. The jurisdiction map, the temporary-difference
schedule structure and the account map persist; **every rate must be re-confirmed**, because rates change
and a stale rate silently misstates every deferred balance.
