<!-- ipo-readiness-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**IPO readiness work is confidential and market-sensitive.** Confirm scope carefully, and note that
**an intention to go public is itself non-public information.**

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Treat this list as the start of the systems inventory** the original asks for as an input. What is
connected — accounting, payroll, billing, expense, equity — **tells you part of the landscape**, and **what
is conspicuously absent is often the finding**: no billing system behind a subscription revenue model, no
equity platform behind an option-heavy cap table.

Settle the entity scenario, which for an IPO is **the registrant question**:

- **Single-entity** — one company file. Ask **whether that entity is the intended registrant.**
- **Multi-entity** — ask which set, **and which entity will be the registrant**, and **whether the group
  structure is final.** **Pre-IPO reorganisations are common**, and a readiness assessment of a structure
  that is about to change has limited value. See the cross-entity step.

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
- **A near-substitute is not a substitute:**
  - **A fast close is not a controlled close.** Speed and ICFR are different requirements, and optimising
    only for speed makes the second harder.
  - **Clean-looking financials are not audited financials.** **PCAOB-standard audit is a different bar**
    from a private-company review, and the workspace cannot tell you which was performed.
  - **The absence of restatements in the ledger is not the absence of errors.**
  - **A user field on a transaction is not segregation of duties evidence.** Shared logins, delegated
    access and system entries all break that link — the same caveat as
    `fraud-detection-and-forensics`.
- **There is no cap table, no valuation, no contract, no control documentation and no audit opinion on this
  surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: **legal name — the prospective registrant's** — base currency,
**fiscal calendar and year-end**, country / region, industry.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Current close process** — timeline, owners, pain points | **Required — [gated]** | **The timeline is measurable**; owners and pain points are `[manual]`. |
| ~~Historical financials~~ — years available | **Now [auto]** | **Audit status remains `[manual]`** and is the part that matters. |
| **Revenue model and contracts** — ASC 606 impacts | **Required — [manual]** | Contracts are not on this surface. |
| **Equity history** — cap table, option grants, valuations | **Required — [manual]**, always | **The whole equity workstream depends on it.** |
| **Systems landscape** — ERP, billing, payroll, FP&A | Recommended — **[gated]** | Partly readable from Gate 1. |
| **Control environment** — SOX readiness assessment | Recommended — **[manual]** | |
| **Target timeline** and **intended registrant** | **Required — Mosofin addition** | Determines sequencing and which entity is assessed. |
| **Whether a pre-IPO reorganisation is planned** | **Required — Mosofin addition** | Assessing a structure about to change wastes the work. |
| **Which years must be audited**, and their current status | **Required — Mosofin addition** | The binding constraint on almost every IPO timetable. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the registrant. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a year-end that does not suit a public reporting calendar. |
| **Confirm manual evidence** | **Required** | The cap table, contracts, audit status and control documentation are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an audit status, an
EPS figure, or a control conclusion.

**On later runs**, read stored preferences first (Step 8), confirm in one line, and ask only what changed.
The roadmap, the workstream owners, the memo index and the close calendar persist; **every measurement is
re-taken**, since the whole point is to track movement.
