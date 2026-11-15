<!-- due-diligence-quality-of-earnings · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before analysing anything. This ordering is the contract. Do not
skip a gate because a previous conversation covered it — connections, permissions, and company files
change, and in a deal they change often.

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

Confirming carefully matters especially here: **deal information is confidential**, often under an NDA,
and frequently not known to the target's own staff. Reading the wrong entity is a confidentiality
incident.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Then ask the decisive question: which connected company file, if any, is the target?**

- **The target is connected** (sell-side, exit prep, refinancing, or post-close) → the analysis runs
  against that `data_source_id`, and most of Part B is `[auto]`.
- **The target is not connected** (typical buy-side) → **every target figure is `[manual]`**, supplied from
  the data room. The skill still structures the whole analysis; it simply reads nothing. **Never
  substitute the acquirer's own data.**

**Also settle the deal perimeter.** A target may be one entity, several, or a carve-out — a division that
has never had its own financial statements. **Carve-outs are the hardest case**: the standalone figures do
not exist and must be constructed, and shared costs must be allocated. See the cross-entity step.

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
- **The general-ledger tool is what gives QofE its depth.** Summary reports show the reported numbers; the
  **ledger shows the transactions behind them**, which is where one-off items, related-party flows and
  recognition timing actually live. Without it this is a ratio review, not a QofE — say so.
- **Check how far back the history goes.** QofE needs three years plus LTM. A connector added eighteen
  months ago cannot evidence year one, and the recurring-"one-time" test needs multiple years to work at
  all.
- **A near-substitute is not a substitute.** **Reported EBITDA is not adjusted EBITDA**, and a monthly P&L
  is not a working capital analysis. Both are starting points.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for the target, where it is
connected.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and year-end —
which defines what "LTM" means — country / region, and **industry**, which frames every benchmark.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Side / type of engagement** — buy-side / sell-side / refinancing | **Required — [manual]** | **Ask first.** It sets the emphasis, and with Gate 1 it determines the data position. |
| **Target's financial statements** — multi-year (3 years + TTM / LTM) | **Required — [auto] if the target is connected**, otherwise **[manual]** | |
| **Trial balances, GL, supporting schedules** | **Required for depth — same split** | Without the GL this is a ratio review. |
| **Management EBITDA / adjusted EBITDA bridge** — the seller's adjustments | Recommended — **[manual]** | **Ask for it early on buy-side**; the whole of Step 3 is a critique of it. |
| **Industry context** — for benchmarking | Recommended — **partly [auto]** | Industry from the profile; benchmarks **[manual]**. |
| **Customer / vendor concentration data** | Recommended — **[auto] if connected** | Contract terms remain **[manual]**. |
| **Working capital detail** — AR / AP / inventory by month | **Required for WC analysis — [auto] if connected** | Normally the most laborious input. |
| **Debt and debt-like items** — detailed | **Required for net debt — [gated]** | Balances **[auto]**; off-balance-sheet and contingent items **[manual]**. |
| **Forecast** — management projections | Recommended — **[manual]** | |
| **Known related parties and owner arrangements** | **Required for private-company QofE** | **[manual]** to identify; **[auto]** to quantify once named. |
| **The LTM cut-off date** | **Required** | Never default it. |
| **Confirm scope** | **Required** | Read back **which company file is the target**, the deal perimeter, and any excluded files. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | On buy-side, essentially everything. Record what was supplied and its source. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an adjustment, the
working capital target methodology, the net debt definition, or the LTM date.

**On later runs** — a deal runs for months, with several iterations — read stored preferences first
(Step 11), confirm in one line, and ask only what changed. The adjustment framework, the net debt
definition and the WC methodology persist; **every figure is re-measured**.
