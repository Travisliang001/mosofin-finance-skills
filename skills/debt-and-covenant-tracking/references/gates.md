<!-- debt-and-covenant-tracking · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before computing anything. This ordering is the contract. Do not
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

Settle the entity scenario — and here it is a substantive question, not a formality:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set, **and ask at what level each covenant is tested.** This is the
  decisive question. **Covenants are usually tested at the level of the borrowing group defined in the
  agreement**, which may be the whole group, a sub-group, or a single entity — and it very often does not
  match the set of connected company files. A leverage ratio computed over the wrong perimeter is wrong
  regardless of how carefully the definitions were applied. See the cross-entity step.

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
- **A near-substitute is not a substitute, and here it is the whole risk of the skill.** **Book EBITDA is
  not covenant EBITDA. Book debt is not covenant debt. Book cash is not covenant cash.** Producing a
  ratio from the readily-available book figures and calling it a covenant is the specific failure this
  skill exists to prevent.
- **The general-ledger tool is what makes the debt schedule real.** Without movement on the debt accounts
  you cannot see actual draws and repayments — only net balance changes, which conceal a draw and a
  repayment of equal size. Build from movements.
- **A balance sheet line called "Loans" is not the facility inventory.** Debt-like items are scattered:
  finance leases, shareholder loans, deferred consideration, invoice discounting. Sweep for them.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name — which is the name on the facility agreement —
base currency, fiscal calendar and **period end**, which is usually the covenant testing date.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Loan / facility agreements** — term loans, revolvers, bonds, leases-as-debt | **Required — [manual]** | The source of truth. Ask for them, or for a term sheet summary per facility. |
| **Each facility's key terms** — principal, rate, amortization, maturity, fees, covenants | **Required — [manual]** | Balances are readable; **terms are not**. |
| **Period actuals** — balance sheet and income statement | **Required for covenants — [auto]** | Pulled. These are the *inputs*, not the answer. |
| **Definitions per agreement** — particularly covenant numerators and denominators | **Required — [manual]**, and **blocking** | **Without these, no covenant is computed.** See the banner above. |
| **Forecast** — for forward covenant projection | Recommended — **[manual]** | From `rolling-forecast` or a three-statement model. |
| **Compliance certificate format** — if lender-required | Recommended — **[manual]** | |
| **Prior covenant compliance** — history | Recommended — **[manual]** | Including any waivers or amendments still in force. |
| **The covenant testing perimeter** — which entities are inside the borrowing group | **Required if multi-entity** | See Gate 1. |
| **The testing period and date** — TTM, quarterly, annual; period-end or month-end | **Required** | Never assume it matches the accounting period. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Agreements, terms and definitions are all `[manual]`. Record which facilities have definitions supplied and which do not. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a covenant
definition, a rate, a limit, or the testing perimeter.

**On later runs** — this runs quarterly for most borrowers — read stored preferences first (Step 11),
confirm in one line, and ask only what changed. The facility terms, the covenant definitions and the
testing calendar persist; **balances, ratios and headroom are always re-measured**.
