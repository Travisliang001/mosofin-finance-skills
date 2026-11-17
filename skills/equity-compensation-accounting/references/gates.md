<!-- equity-compensation-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Check for a connected equity management or payroll platform.** An equity platform would supply the award
population, vesting and often the fair values — converting most of this skill's `[manual]` half. A payroll
platform supplies the payroll tax side of vesting and exercise events.

Settle the entity scenario — and here there is a structural point:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. **Awards are almost always over the *parent's* shares, while the
  employees work for — and their cost belongs to — the subsidiaries.** That mismatch is the defining
  multi-entity feature of this skill: the expense sits in one entity's books, the equity credit in
  another's. See the cross-entity step.

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
- **A near-substitute is not a substitute.** **The share count in the equity accounts is not the award
  population.** Equity accounts record *issued* shares; options and unvested RSUs are neither issued nor
  recorded there. **The outstanding award population cannot be derived from the balance sheet** — it comes
  from the cap table, and nothing else.
- **The recorded expense is not the correct expense.** It is what someone posted, usually by manual
  journal. That is exactly why the reconciliation in Step 0b is worth running.
- **There is no valuation model and no market data on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name — the issuer of the shares — base currency,
fiscal calendar and year-end, country / region.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Award details** — type, grant date, quantity, exercise / strike price, vesting terms | **Required — [manual]** | From the cap table. Ask for an award-level extract. |
| **Grant-date fair value** — per-award, or the inputs to compute it | **Required — [manual]**, always | Ask for the value, **its source and the valuation date**. |
| **Vesting conditions** — service, performance and/or market | **Required — [manual]** | The classification changes the accounting entirely; see Step 3. |
| **Reporting framework** — ASC 718 / IFRS 2 | **Required — [manual]** | Decides the attribution method options and the forfeiture treatment. |
| **Forfeiture policy** — estimate vs. account as they occur | **Required — [manual]** | A US GAAP policy choice; IFRS 2 largely settles it. |
| **Modifications / cancellations** | If applicable — **[manual]** | Repricings and accelerations are complex; flag early. |
| **Settlement type** — equity-settled vs. cash-settled | **Required — [manual]** | **Ask first**: it decides whether the award is remeasured every period. |
| **Award population data** — grants, vests, exercises, forfeitures by period | **Required for roll-forward — [manual]** | From the cap table. |
| **Where recipients work** — the functional split | Recommended — **[gated]** | Needed for Step 6's allocation; departments may be readable. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and **which entity issues the shares**. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | The cap table and every fair value are `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a fair value, a
settlement type, an attribution method, or a forfeiture rate.

**On later runs**, read stored preferences first (Step 11), confirm in one line, and ask only what changed.
The plan terms, the attribution method, the forfeiture policy and the account map persist; **the award
population, the fair values and the expense are re-obtained every period**.
