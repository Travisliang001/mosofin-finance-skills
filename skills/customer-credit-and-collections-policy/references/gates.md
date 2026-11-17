<!-- customer-credit-and-collections-policy · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before designing anything. This ordering is the contract. Do not
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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`. A segmentation
  built on part of the customer base will produce a policy sized for the wrong business.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set, **and ask whether one policy will govern all of them**. That is the
  decisive question: a group can run one credit policy across every entity, or each entity can run its
  own, and the segmentation looks quite different depending on which. **A customer trading with three
  entities is one credit relationship** — see the cross-entity step.

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
- **The invoice and payment tools together are what make segmentation real.** Without both, payment
  behaviour cannot be measured and Step 1 collapses to segmenting by revenue alone — which is the
  common, and much weaker, approach. Say so if that is what happened.
- **A near-substitute is not a substitute.** **An aging is a snapshot, not behaviour.** A customer who is
  current today may habitually pay at day 55 and simply be between invoices. Segmentation by "currently
  overdue" produces a policy that chases the unlucky rather than the slow.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, country / region, and
**industry** — which sets expectations for normal payment terms in that trade.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected
books already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Customer list + A/R aging** | **Required — usually [auto]** | **Do not ask for an export; read it.** Confirm the as-of date. |
| **Current credit terms** — Net 30/45/60, discounts | **Required — usually [auto]** | The terms catalogue and per-customer terms pull. **Ask which terms are *policy* versus which have simply accreted.** |
| **Payment history** — days-to-pay, write-offs | Recommended — **[auto]** | Read it. It is the core of segmentation. |
| **Customer financials** — credit reports, statements | Recommended — **[manual]** | See `credit-limit-and-customer-risk`; policy design rarely needs them. |
| **Sales / CS escalation rules** — roles and ownership | Recommended — **[manual]** | Who owns the relationship, who can authorise an exception. |
| **Write-off policy** — approval limits | Recommended — **[manual]** | |
| **Whether order hold is technically possible** | **Required for Step 2** | A hold rule nobody can enforce is not a policy. Ask how orders are actually stopped. |
| **The problem being solved** | **Required** | DSO, bad debt, disputes, or simply the absence of any policy. It changes what the model optimises for. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether one policy governs all. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Roles, approval limits and escalation paths will all be `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the approval limits,
the escalation ladder, or the terms.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The policy, the segments and the reason codes persist; **the segmentation and the KPI baseline are always
re-measured**, because that is how you tell whether the policy is working.
