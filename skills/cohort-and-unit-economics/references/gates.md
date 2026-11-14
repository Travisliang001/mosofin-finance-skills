<!-- cohort-and-unit-economics · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before computing anything. This ordering is the contract. Do
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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`. In cohort
  analysis an excluded entity does not just shrink the sample — if that entity holds a particular
  customer type, it biases every retention curve.

**Look for a connected billing, subscription or commerce platform.** It would supply plan tiers, sign-up
dates distinct from first invoice, and sometimes acquisition channel — converting several `[manual]`
inputs to `[auto]`.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set, **and ask whether customers are shared**. The analysis runs
  **once per entity**, every call targeting exactly one `data_source_id`, and every cohort carries its
  entity's `display_name`. **A customer billed by two group entities is one customer, not two** — see
  the cross-entity step, because getting this wrong double-counts acquisitions and halves apparent
  lifetime value.

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
built this run, held for this run, written out as the coverage sheet, **never** written into this
file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled —
  some underscored, some hyphenated.
- **The customer-level revenue tool is the one this skill lives on.** Without revenue by customer by
  period, there is no cohort triangle — only aggregate trends, which is what cohort analysis exists to
  see past. If it is disabled, say so; do not substitute total revenue and call it a cohort analysis.
- **A near-substitute is not a substitute.** **Total revenue by month is not cohort revenue by month.**
  A flat total can conceal severe churn offset by new acquisition — that concealment is precisely the
  problem cohorts solve. Never build retention from aggregate revenue.
- **Check how far back the history goes.** Cohort analysis needs depth: a workspace connected eighteen
  months ago cannot show a three-year retention curve. State the earliest cohort available and treat
  anything before it as unobservable, not as zero.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, country / region, and
**industry** — which suggests the likely business model but does not decide it.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Customer-level data** — acquisition date, revenue by period, status | **Required — usually [auto]** | Derived: acquisition date from first invoice, revenue by month from customer sales, status from recent activity. **Confirm the acquisition definition** — see Step 1. |
| **Acquisition cost data** — S&M spend by period, customers acquired | **Required for CAC — [gated]** | Spend is **[auto]** from the P&L; **which accounts count as acquisition cost is [manual]** and materially changes CAC. |
| **Cost-to-serve / gross margin per customer** | **Required for LTV — [gated]** | Company-level gross margin is **[auto]**; per-customer variation is **[manual]**. |
| **Business model** — subscription / transactional / marketplace / hybrid | **Required — [manual]** | Changes what retention even means. Ask; do not infer from industry. |
| **Period granularity** — monthly / quarterly cohorts | **Required** | Monthly is standard; quarterly for smaller volumes. |
| **Discount rate** (for discounted LTV) | Optional — **[manual]** | Needed if LTV feeds a valuation. |
| **Segmentation** — by plan, channel, geography | Optional — **mixed** | Plan / item and geography are often **[auto]**; **channel is [manual]** unless a marketing or commerce platform is connected. |
| **Which accounts constitute sales & marketing spend** | **Required for CAC** | Fully-loaded or paid-only — see Step 5. Ask which, and which accounts. |
| **Analysis window** | **Required** | Never default it. Confirm against the earliest cohort actually available. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether customers are shared across entities. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Channel and per-customer cost-to-serve will be `[manual]`. Record what was not supplied. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the business
model, the acquisition definition, the S&M account set, or the discount rate.

**On later runs**, read stored preferences first (Step 11), confirm in one line, and ask only what
changed. The cohort definition, the S&M account set and the margin basis should not be re-asked; **the
cohorts themselves are always rebuilt** from current data.
