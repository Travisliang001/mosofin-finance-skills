<!-- derivatives-and-hedging-asc815 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before recording anything. This ordering is the contract. Do not
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

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting exactly
  one `data_source_id`, and every instrument carries its entity's `display_name`. **Which entity is the
  counterparty to the derivative, and which entity holds the hedged item, must be the same entity for
  hedge accounting** — a group treasury holding the swap while a subsidiary holds the debt is a common and
  consequential structure. See the cross-entity step.

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
- **A near-substitute is not a substitute.** **A recorded derivative balance is not a valuation.** It is
  last period's mark, or whatever someone entered. Fair value at this reporting date comes from the
  counterparty or an independent model — never from the ledger.
- **Nothing in the ledger identifies an embedded derivative.** An embedded derivative lives inside an
  ordinary-looking contract — a supply agreement with a price linked to a commodity index, a convertible
  loan, a lease with an unusual escalation. **Only reading the contracts finds them.** The absence of one
  in the accounts is not evidence there is none.
- **There is no market-data tool.** Do not look for one and do not substitute anything.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name — the counterparty on the ISDA — base currency,
which determines what counts as an FX exposure at all, fiscal calendar and reporting dates.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Derivative contracts** — ISDA / confirmations, terms, notional, dates | **Required — [manual]** | The instruments themselves. Ask for confirmations or a treasury schedule. |
| **Hedged items** — debt schedule, forecasted transactions, net investments | **Required — [gated]** | Debt and net investments are largely **[auto]** (see `debt-and-covenant-tracking`); **forecasted transactions are [manual]**. |
| **Valuations** — counterparty mark-to-market + methodology | **Required — [manual]**, always | Ask for the value, **the source, the date and the methodology**. |
| **Risk management policy** — objectives and approved instruments | Recommended — **[manual]** | Also the basis for the designation's stated objective. |
| **Prior period hedge memo** — designations and status | Recommended — **[manual]** | Essential for the documentation-timing check. |
| **Discount curves / FX rates** — market data source | Recommended — **[manual]** | |
| **Whether hedge accounting is being applied at all** | **Required** | It is elective. Many entities hold derivatives and take all fair value changes to P&L, which is simpler and entirely legitimate. Establish this first — it removes most of the work if the answer is no. |
| **Designation dates per relationship** | **Required if hedge accounting applies** | For the timing check. |
| **Reporting date** | **Required** | Never default it. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and which entity holds each instrument and each hedged item. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Contracts, valuations, curves and documentation are all `[manual]`. Record which relationships have current documentation and which do not. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a fair value, a
designation, an effectiveness conclusion, or the framework.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The instrument inventory's fixed terms, the designations and the effectiveness method persist;
**valuations, effectiveness results and OCI balances are re-obtained every period**.
