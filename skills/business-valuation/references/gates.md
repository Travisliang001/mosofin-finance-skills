<!-- business-valuation · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before valuing anything. This ordering is the contract. Do
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

**Ask directly what is being valued**, because it decides the entity scenario and it is genuinely
ambiguous in a multi-file workspace:

- **One legal entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **A group** — ask which set. **A group valuation is not the sum of its entities' valuations.**
  Intercompany trading must be eliminated, shared costs must be allocated consistently, and the
  group's capital structure is not the sum of the parts. Run the financial foundation **once per
  entity**, every call targeting exactly one `data_source_id`, label every figure with its
  `display_name`, then consolidate deliberately — see `consolidation-and-eliminations` and the
  cross-entity step below.

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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map**
— built this run, held for this run, written out as the coverage sheet, **never** written into this
file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled —
  some underscored, some hyphenated.
- **A near-substitute is not a substitute.** A **summary balance sheet line** labelled "loans" is
  not a net debt schedule: the bridge needs each debt-like item identified — finance leases,
  shareholder loans, deferred consideration, unfunded obligations — and a single line hides them.
  If the detailed ledger is unavailable, the bridge is `[gated]` and must be built from a supplied
  schedule.
- **There is no market-data tool, and there never will be.** Do not look for one, do not substitute
  anything for one, and do not supply a rate from memory.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: legal name, **base currency** (which must match or be
reconciled to the currency of the valuation), fiscal calendar and year-end, country / region, and
**industry** — which is the starting point for peer selection even though the peers themselves are
`[manual]`.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Target business** — description, industry, stage, size | **Required — partly [auto]** | Industry and size derive; stage and strategic description are **[manual]**. |
| **Purpose of valuation** — M&A / financial reporting / tax / litigation / management | **Required — [manual]** | **Ask first.** It drives the standard of value and whether a specialist is mandatory. |
| **Standard of value** — fair market value / fair value / investment value | **Required — [manual]** | Follows from purpose; confirm explicitly rather than inferring. |
| **Valuation date** | **Required — [manual]** | Every company figure is read as at this date, and every market input must be sourced as at it. Never default to today. |
| **Historical financials** — multi-year | **Required — usually [auto]** | Pulled. Confirm how many years. |
| **Adjusted / normalized EBITDA** — from `due-diligence-quality-of-earnings` if available | **Required for multiples — [gated]** | Reported EBITDA is **[auto]**; the normalising adjustments are **[manual]**. Never apply a multiple to unadjusted EBITDA without saying so. |
| **Forecast / projections** — for DCF | **Required for DCF — [manual]** | From `three-statement-financial-model` or `rolling-forecast`. History informs it; it is not history. |
| **Comparable companies** — trading or transaction comps | Recommended — **[manual]** | Peer identities and their multiples, sourced as at the valuation date. |
| **Discount rate inputs** — risk-free rate, equity risk premium, beta, size premium, country risk, debt cost | **Required for DCF — [manual]**, always | **Current data at the valuation date.** Ask for each with its source and date. |
| **Capital structure** — debt, equity, cash | **Required for WACC and bridge — largely [auto]** | Book values pull; **market values of equity and any off-balance-sheet debt are [manual]**. |
| **Diluted share count and dilutive instruments** — options, warrants, convertibles, RSUs | **Required for per-share value — [manual]** | A cap table is not in the accounting system. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether this is an entity or group valuation. |
| **Confirm any profile contradiction** | **Required if one appears** | E.g. the base currency differs from the valuation currency. |
| **Confirm manual evidence** | **Required** | Every market input will be `[manual]`. Record which have been supplied with sources and which are outstanding. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the valuation
date, the purpose, the standard of value, any market input, or the entity.

**On later runs**, read stored preferences first (Step 12), confirm in one line, and ask only what
is new. The peer set and the WACC *structure* persist; **the market values behind them do not** and
must be re-sourced at each new valuation date.
