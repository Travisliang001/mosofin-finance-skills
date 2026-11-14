<!-- cash-management-and-treasury · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before designing anything. This ordering is the contract. Do
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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**This gate does double duty in this skill.** The connected datasource list is itself the **first
draft of the entity structure** the design rests on — it tells you how many company files exist and
what each is called. Confirm it against the user's understanding of the legal structure, because the
two are often not the same: a legal entity with no connected file is invisible here, and its cash is
missing from the map.

**Treasury is inherently a multi-entity discipline** — pooling, concentration and in-house banking
only exist because there are several entities. So:

- **Single-entity** — ask which company by `display_name`. Steps 1, 3, 4, 5, 6 and 8 all apply;
  Step 2's pooling structures largely do not.
- **Multi-entity** — ask which set. The landscape map runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every account and balance carries its entity's `display_name`.
  **Ask the decisive follow-up: can cash actually move between these entities?** See the cross-entity
  step; a pooling design proposed where funds are legally trapped is worse than no design.

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
- **A near-substitute is not a substitute — and here the substitution is a control failure, not just
  a data gap.** No accounting tool reports who may sign on an account, who holds online access, or
  whether a payment passed dual approval. **An absence of evidence of fraud is not evidence of
  control.** Mark every control in Step 5 `[manual]` unless the user supplies the evidence, and say
  so on the face of the output.
- **A balance without its bank is not a counterparty exposure.** Step 8's concentration KPI needs to
  know *which bank* holds each balance, and the chart of accounts does not. Group by bank only once
  the user has mapped accounts to banks.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: legal name, **base currency**, country / region — which
together begin the entity-structure map — fiscal calendar, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Entity structure** — legal entities, jurisdictions, currencies | **Required — partly [auto]** | Connected files and their profiles give a first draft. **Ask what is missing** — entities with no connected file hold cash you cannot see. |
| **Current bank accounts** — by entity, currency, purpose, balance | **Required — balances [auto], the rest [manual]** | Accounts and balances pull. **Bank name, account purpose, and signatories do not.** Ask the user to map each account to its bank. |
| **Cash inflows / outflows** — volumes, currencies, predictability | **Required — usually [auto]** | Derivable from actual movement per account. |
| **Banking relationships** — banks, products, fees | Recommended — **[manual]** | Fees *posted* are readable (see `bank-fee-and-interest-analysis`); the relationship and rate card are not. |
| **Existing policies** — investment, FX, signatory, payment | Recommended — **[manual]** | Ask before designing. Replacing a policy nobody mentioned is worse than extending it. |
| **Liquidity needs** — working capital, debt service, capex commitments | **Required — [gated]** | Working capital is derivable; debt service and capex commitments are **[manual]**. |
| **Risk appetite** — counterparty, investment, FX | **Required — [manual]** | Including the deposit-insurance limit or comfort threshold per bank. |
| **Available facilities** — revolvers, lines of credit | Recommended — **[manual]** | Limits, undrawn availability, covenants. |
| **Trapped cash** — regulatory or contractual restrictions | **Required if any** | **[manual]**, and it changes every liquidity figure. Ask explicitly. |
| **Can cash move between entities?** | **Required if multi-entity** | Decides whether pooling is even possible. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Bank identities, signatories, access, facilities and policies will all be `[manual]`. Record what was not supplied. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the minimum
cash balance, the risk appetite, the counterparty limits, or the entity.

**On later runs**, read stored preferences first (Step 11), confirm in one line, and ask only what
changed. The account-to-bank map, the policy thresholds and the authority matrix should not be
re-asked; **balances and volumes are always re-read**.
