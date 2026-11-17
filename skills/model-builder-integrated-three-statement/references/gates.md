<!-- model-builder-integrated-three-statement · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before pulling historicals. This ordering is the contract. Do not
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

**A model outlives the conversation that built it.** Record the workspace and entity in the model itself, so
whoever opens it in six months knows what it was built from.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Settle the entity scenario — **and settle it before pulling anything**, because it defines the model:

- **Single-entity model** — one company file. The historicals are that entity's.
- **Consolidated model** — **the historicals must be consolidated**, with intercompany eliminated. **Not the
  parent's, and not a sum of the entities'.** See the cross-entity step.

**A disconnected group member means the historical foundation is incomplete.** For a fundraising or board
model, say so before building — **the model will be relied on.**

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
  - **A historical ratio is not a forecast assumption.** It is the starting point for a conversation about
    one.
  - **A trend is not a driver.** Revenue rising 8% a year is an observation; **what actually drives it —
    customers, price, volume — is the model's subject.**
  - **The books' history is not necessarily the published history.** See `financial-statement-builder`;
    unposted audit adjustments matter to a model that will be shown to investors.
  - **Cash in the ledger is not cash in the bank.** See `bank-reconciliation`.
- **There is no forecast, no assumption support, no debt schedule and no cap table on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: **legal name**, **base currency** — the model's currency —
**fiscal calendar and year-end** — the model's period structure — country, industry.

**Ask the user** what actually changes the work — the original Inputs table, **minus the four the connected
books now answer**:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Historical P&L~~ | **Now [auto]** | For every period the model needs. |
| ~~Historical balance sheet~~ | **Now [auto]** | Including the opening position. |
| ~~Historical cash flow or cash movement support~~ | **Now [auto]** where the platform provides it | Otherwise derivable from balance movements. |
| **Forecast assumptions** — growth, margin, working capital, capex, debt, tax, payroll, operating drivers | **Required — [manual]**, always | **Never generated.** Presented alongside their historical values. |
| **Forecast horizon and period cadence** — monthly / quarterly / annual | **Required — [manual]** | |
| ~~Chart of accounts or mapping~~ | **Now [auto]** | **Confirm the account-to-line mapping**, which is the part judgment enters. |
| **Debt, leases, equity, and fixed asset schedules** | Required if applicable — **[gated]** | **Balances `[auto]`; the schedules are `[manual]`** — see `debt-and-covenant-tracking`, `lease-accounting-asc842-ifrs16`, `fixed-asset-register-and-depreciation`. |
| ~~Opening model date and currency~~ | **Now [auto]** | **Confirm the opening date** against the last closed period. |
| **What the model is for** | **Required — Mosofin addition** | Fundraising, board, lender, internal. It sets the standard of evidence and how assumptions should be justified. |
| **Whether the historicals must match published statements** | **Required — Mosofin addition** | If an audit exists, the model's history should agree with it. |
| **Confirm scope** | **Required** | Read back the entity by `display_name`, the historical periods, and whether consolidated. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a monthly model for an entity whose books close quarterly. |
| **Confirm manual evidence** | **Required** | Assumptions and schedules are `[manual]`. |

Ask as **one short batch** — **and ask for assumptions after presenting the historical drivers**, not
before. Propose defaults where reasonable — but **never** default a growth rate, a margin, a working capital
assumption, or any other forward input.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The architecture, the mapping, the driver definitions and the check set persist; **the historicals and the
driver values are re-obtained, and the assumptions are re-confirmed.**
