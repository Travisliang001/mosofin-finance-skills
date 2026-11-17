<!-- inventory-costing-fifo-lifo-wavg · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before costing anything. This ordering is the contract. Do not
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

**Check for a connected inventory, warehouse or ERP platform.** A dedicated inventory system may **expose
layers directly and support methods the accounting platform does not** — which would convert the largest
`[gated]` element here. **Where only an accounting platform is live, say so**, because it determines whether
layers are read or reconstructed.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`.
- **Multi-entity** — ask which set. **Inventory held by one entity and sold by another is common**, and
  **intercompany mark-up in stock is the classic consolidation adjustment.** See the cross-entity step.

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

**Check specifically whether item-level and line-level detail is available.** A platform that exposes
invoice and bill **headers** but not **lines** cannot support layer reconstruction — **the whole method
collapses to `[manual]`**, and that must be established early rather than discovered halfway through.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **The platform's inventory value is not the reported inventory value** unless the methods agree.
  - **An average cost field is not a weighted-average computation** you can rely on without knowing whether
    it is periodic or moving.
  - **Quantity on hand is not the physical quantity.** It is the recorded quantity; **only a count proves
    existence** — see `inventory-to-gl-reconciliation`.
  - **A recent selling price is not NRV.** NRV is selling price **less costs to complete and sell**, and
    those costs are `[manual]`.
  - **Purchase price on a bill is not full inventory cost** — freight, duties and conversion costs belong in
    it too, and they are often posted elsewhere.
- **There is no layer stack, no replacement cost, no standard cost variance report and no physical count on
  this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and year-end,
country / region.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Inventory transactions~~ — purchases and sales | **Now [gated]** | **`[auto]` where line-level detail is exposed**; otherwise `[manual]`. |
| **Method** — FIFO / LIFO / weighted-average / specific ID | **Required — [manual]** | **And separately: which method does the platform apply?** See Step 0b. |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | **Decides LIFO eligibility and the NRV / LCM rules.** |
| **System type** — periodic / perpetual | **Required — [gated]** | **Partly readable**: whether COGS posts per sale. |
| **Opening inventory** — quantity and cost, or opening layers | **Required — [gated]** | **The balance is `[auto]`; the opening layers are `[manual]`** unless reconstructable. |
| **NRV / market data** — selling price, costs to complete and sell | Recommended — **[gated]** | **Selling prices `[auto]` from recent sales**; **costs to complete and sell `[manual]`.** |
| **Cost components** — purchase price, freight-in, duties, conversion costs | **Required — [gated]** | Readable where separately posted; **allocation is `[manual]`.** |
| ~~Item / SKU detail~~ | **Now [auto]** where an items module is used | Confirm pooling. |
| **Whether standard costing is in use** | **Required — Mosofin addition** | It changes everything downstream; see the edge cases. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the period. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. LIFO asserted under IFRS. |
| **Confirm manual evidence** | **Required** | NRV inputs, opening layers and cost allocations are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a costing method, an
NRV, or a cost allocation.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
The method, the framework, the pooling, the cost components and the NRV basis persist; **every quantity,
cost and layer is re-obtained each period.**
