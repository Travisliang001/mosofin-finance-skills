<!-- inventory-obsolescence-and-reserve · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before reserving anything. This ordering is the contract. Do not
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

**Check for a connected inventory, warehouse or ERP platform.** One would supply **lot dates, locations and
condition codes** — which converts aging from a proxy to a fact, and may carry damage and expiry flags this
skill otherwise cannot see.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`.
- **Multi-entity** — ask which set. **Stock held in one entity and sold by another** means the movement
  history and the holding are in different files. See the cross-entity step.

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

**Check whether line-level sales detail is available.** Movement by SKU is the core input; **without invoice
line detail there is no movement analysis**, and the skill degrades to whatever listing the user supplies.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **No movement is not obsolescence.** See above.
  - **Last purchase date is not lot age.**
  - **A recent selling price is not NRV** — costs to complete and sell must come off.
  - **Quantity on hand is not physical quantity**, and **nothing here can see condition.** A pallet of
    water-damaged stock reads exactly like good stock.
  - **A reserve balance is not an adequate reserve.** It is what was posted.
- **There is no demand forecast, no lot condition and no physical inspection on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and year-end,
country / region, industry — **which matters, since obsolescence risk differs enormously between, say,
fashion and fasteners.**

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Inventory listing~~ — SKU, qty, cost, location, lot / date | **Now largely [auto]** | **Lot and date only where the platform tracks them**; otherwise the aging basis is a proxy. |
| ~~Inventory movement~~ — usage / sales by SKU over time | **Now [auto]** | **The core input, and a query.** |
| ~~Selling prices~~ — current selling price by SKU / channel | **Now [auto]** | Realised prices from recent sales. |
| **Forecast and demand** — S&OP forecast | Recommended — **[manual]**, always | **Not in a ledger.** Without it, excess is measured against history rather than plan. |
| **Write-off policy** — approval thresholds | Recommended — **[manual]** | |
| **Costing method** — FIFO / LIFO / WAVG / standard | **Required — [gated]** | **The platform's method may differ from the reported one.** |
| **Aging bucket definition and reserve rates** | **Required — [gated]** | **Propose derived rates; the policy is the user's.** |
| **Known damaged, expired or quarantined stock** | **Required — [manual]** | **Invisible here.** Ask explicitly. |
| **Special-handling categories** — seasonal, end-of-life, customer-specific | Recommended — **[manual]** | **Prevents false positives** in the no-move list. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the period. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Forecast, condition and policy are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a reserve percentage,
an obsolescence conclusion, or a physical condition.

**On later runs**, read stored preferences first (Step 8), confirm in one line, and ask only what changed.
The bucket definitions, the derived rates, the special-handling categories and the account map persist;
**every quantity, movement figure and reserve amount is re-obtained each period.**
