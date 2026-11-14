<!-- credit-limit-and-customer-risk · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before assessing anything. This ordering is the contract. Do not
skip a gate because a previous conversation covered it — connections, permissions, and company files
change between reviews.

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

Settle the entity scenario — and it matters unusually much here:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. **A customer trading with several group entities represents one
  credit exposure, not several.** Each entity may see a modest, well-behaved balance while the group's
  total exposure to that customer is large and its concentration risk real. **Run the history per entity,
  then aggregate deliberately** — see the cross-entity step. This is the single most valuable thing a
  multi-entity workspace adds to a credit decision.

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
- **A near-substitute is not a substitute, and here it would be a serious error.** **Your financial
  statements are not your customer's.** Nothing readable in this workspace can produce their current
  ratio, their leverage or their cash flow. Never compute a "customer ratio" from your own data.
- **The invoice and payment tools are what make the payment history real.** Without both, days-to-pay
  cannot be measured and the strongest available evidence is lost. If either is disabled, say the
  payment-history analysis could not be performed.
- **There is no credit bureau tool.** Do not look for one and do not substitute anything for one.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers about **your** entity: base currency — which tells you
whether a customer's trading currency creates exposure — fiscal calendar, country, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected
books already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Customer name and legal entity** | **Required — partly [auto]** | The customer record and its registered details pull; **the legal entity actually contracting is [manual]** and often differs from the trading name. |
| **Customer's jurisdiction** | **Required — [gated]** | The address on the customer record is **[auto]**; where they are legally incorporated is **[manual]**. |
| **Requested trading terms** — net days, expected monthly volume, currency | **Required — [manual]** for the request; **[auto]** for current terms and historic volume | |
| **Customer's financials** | Recommended — **[manual]**, always | Their balance sheet and P&L. Not in your workspace. |
| **Trade references** — from other suppliers | Recommended — **[manual]** | |
| **Credit bureau report** | Recommended — **[manual]** | |
| **Internal trading history** — prior payment record | If returning customer — **[auto]** | **Do not ask for this; read it.** It is the richest input available and it is already here. |
| **Customer's industry** | Recommended — **[gated]** | Sometimes on the customer record; otherwise supplied. |
| **Entity's risk appetite / credit policy** | Recommended — **[manual]** | Tier ceilings, concentration limits, approval authority. |
| **Insurance / credit insurance availability** | Optional — **[manual]** | Insurer limits are an independent read on the same customer. |
| **Current credit limit**, if one is set | **Required for a review** | **[gated]**: sometimes on the customer record, otherwise supplied. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether the customer trades with more than one. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | The customer's financials, bureau report and references will all be `[manual]`. Record which were supplied. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a credit limit, a
tier, or a risk appetite.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what
changed. The tier ceilings, the concentration policy and the review cadence persist; **the payment
history and exposure are always re-read**, since they are the point.
