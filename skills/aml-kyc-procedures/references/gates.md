<!-- aml-kyc-procedures · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before any customer work. This ordering is the
contract. Do not skip a gate because a previous conversation covered it.

Call the Mosofin tools by the **bare names your own tool list exposes** —
`list_workspaces`, `get_agent_datasources`, `get_datasource_tools`,
`invoke_datasource_api_tool`, `get_skills`, `get_my_skill`, `create_skill`. Do not add a
`mosofin_` prefix and do not hardcode a client-side `mcp__…` namespace; that string is
composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with
  `workspace_ids=[…]` and `mode="single"` / `mode="multi"`.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the
opaque `ws_…` handle.

Compliance work carries a specific hazard here: reading one entity's customer data while
believing you are in another's is a data-protection incident, not just a mistake. Confirm
deliberately.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. In AML this matters more than
  elsewhere: a customer population drawn from three of four connected systems is an
  *incomplete* population, and monitoring coverage gaps are themselves a regulatory finding.
  Surface any `reconnect_url`.

A workspace can connect the **same platform several times** — several company files, plus
payment processors. Each is its own row with its own `data_source_id` and `display_name`.
Obliged-entity status is usually **per legal entity**, so the entity question decides whose
regulatory obligations are in play.

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, and every risk
  rating, alert, and escalation carries its entity's `display_name`. Two entities' customer
  activity is never merged into one profile without that label — a customer who looks
  ordinary at each entity separately may look very different in aggregate, and that
  observation must be made explicitly rather than by accident.

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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability
map** — built this run, held for this run, written out as the coverage sheet, **never**
written into this file.

Rules that bite hardest in this skill:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some underscored, some hyphenated.
- **A near-substitute is not a substitute — and in AML this is a compliance failure, not an
  inconvenience.** A customer *balance* report is not a customer *activity* report: a balance
  shows what is owed, while monitoring needs every movement, including the ones that netted
  to zero — which is exactly what layering looks like. If the transaction-detail tool is
  disabled, monitoring is `[manual]`. Say so; do not monitor from balances.
- **No tool in any accounting datasource performs screening.** See the banner above.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each
in-scope entity.

**Derive silently** what the profile answers:

- The entity's own legal name, address, and country — which narrows, but does **not** decide,
  the applicable regime
- Industry, which is itself a **product/service risk** input (a money-services business,
  a casino, and a bookshop do not carry the same inherent risk)
- Fiscal calendar, base currency, time zone

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Jurisdiction(s) and regulatory regime** — where the entity operates and is regulated | **Required** | Never infer from the profile's country. Multi-jurisdiction entities carry several regimes at once. |
| **Entity type and products** — what financial services / products are offered | **Required** | Drives whether the entity is an obliged entity at all, and its product-risk profile. |
| **Customer information** — identity, ownership, activity | **Required** | Activity is usually **[auto]**; identity and ownership are **[manual]**. Say which is which when asking. |
| **Existing AML policy** — current procedures, if any | Recommended — **[manual]** | Ask for it; building a second, conflicting framework is worse than extending the first. |
| **Risk appetite / regulatory expectations** — tolerance, regulator guidance | Recommended | Shapes the risk-rating thresholds. |
| **Transaction data** — for monitoring | If monitoring — usually **[auto]** | Normally pulled from the connected books; ask what sits outside them (cash takings, another bank, a platform not connected). |
| **Screening tools available** — sanctions / PEP / adverse-media sources | Recommended — **[manual]**, always | Ask **which tool the entity actually uses**, because Mosofin cannot do this. If the answer is "none", that is itself a finding for Sheet 7. |
| **Period for monitoring** | **Required if monitoring** | Never default the period. |
| **Responsible officer (MLRO / BSA officer)** by name and role | **Required** | Every escalation is routed to a person, not a mailbox. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | For each `[manual]` gap — and there will be several — ask whether the user can supply it, and how. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the
jurisdiction, the period, the entity, or any regulatory threshold.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only
what changed. The interview shrinks; the gates never do.
