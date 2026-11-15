<!-- management-discussion-and-analysis · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before drafting anything. This ordering is the contract. Do not
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

**MD&A is a published document.** Confirm scope with the care that implies — **drafting a narrative about
the wrong entity's results is not a recoverable error once it circulates.**

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Settle the entity scenario, which for MD&A is **the reporting entity question**:

- **Single-entity** — one company file, and the narrative covers it.
- **Multi-entity** — ask which set, **and confirm that the MD&A covers the consolidated group**, which it
  almost always does. **An MD&A discussing consolidated results must be grounded in consolidated
  figures** — not in the parent's, and not in a sum of the subsidiaries'. See the cross-entity step.

**A disconnected group member is not a gap in a workpaper here — it means the figures underlying a
published narrative are incomplete.** Say so before drafting.

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

**Check specifically whether invoice line detail is available**, since **the price / volume / mix
decomposition depends on it entirely.** Without it, the revenue driver reverts to `[manual]`.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **A movement is not a driver.** The whole tension above.
  - **A correlation is not a cause.** Revenue rose and headcount rose; neither sentence explains the other.
  - **The ledger's prior year is not the published prior year** — see `financial-statement-builder`.
    **MD&A comparatives must match what was filed**, and unposted audit adjustments break that.
  - **Cash on hand is not liquidity.** Undrawn facilities, restricted cash and trapped subsidiary cash all
    change the answer, and none is a balance-sheet line.
  - **An estimate's balance is not its sensitivity.** Step 6 asks how the figure would move under different
    assumptions; the balance alone says nothing about that.
- **There is no forecast, no facility agreement, no market data and no management intent on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: **legal name — as it will appear in the document** — base
currency, **fiscal calendar and year-end**, country / region, industry.

**Ask the user** what actually changes the work — the original Inputs table, **minus the two the connected
books now answer**:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Financial statements, current + comparative~~ | **Now [auto]** | **But confirm the comparative matches what was filed.** |
| ~~Period-over-period variance analysis~~ | **Now [auto]** | The arithmetic; see `budget-vs-actual-analysis` for variance against plan. **The drivers are the next row.** |
| **Reporting framework and filing type** — 10-K / 10-Q, IFRS annual report, private report | **Required — [manual]** | **Decides the required sections and the legal weight.** |
| **Key business drivers** — what drove revenue, cost, margin changes | **Required — [manual]** | **The heart of the skill, and management's to supply.** |
| **Known trends and uncertainties** — forward-looking factors | **Required — [manual]**, always | **Never authored here.** |
| **Liquidity and capital data** — cash, debt, facilities, capex plans, covenant status | **Required — [gated]** | **Cash and debt `[auto]`; facilities, capex plans and covenant definitions `[manual]`.** |
| **KPIs / non-GAAP measures used** | Recommended — **[gated]** | See `kpi-dashboard-builder`; the GAAP side is `[auto]`. |
| **Prior year MD&A** | Recommended — **[manual]** | For consistency of language and of figures. |
| **Risk factors** | Recommended — **[manual]** | |
| **Who reviews and signs off**, and whether legal review applies | **Required — Mosofin addition** | Forward-looking statements need it. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and that the narrative is consolidated. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Drivers, trends, facilities and plans are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a driver, a trend, a
forward-looking statement, or a piece of guidance.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only what changed.
The structure, the non-GAAP definitions, the critical estimate list and the tie-out recipe persist; **every
figure and every narrative statement is redrafted.**
