<!-- bank-fee-and-interest-analysis · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before analysing anything. This ordering is the contract.
Do not skip a gate because a previous conversation covered it — connections, permissions, and
company files change between periods.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a client-side
`mcp__…` namespace; that string is composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with
  `workspace_ids=[…]` and `mode="single"` / `mode="multi"`.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the opaque
`ws_…` handle.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Look specifically for a connected payment processor or banking platform.** It is the single
thing that would lift this skill out of its main limitation: merchant fees become directly
readable, and netted amounts become visible rather than inferred. Check every connected row.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every fee, rate and recommendation carries its entity's
  `display_name`. Multi-entity matters commercially here: **banks price on relationship totals**,
  so consolidated volumes across entities are exactly the negotiating lever — see the
  cross-entity step.

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
map** — built this run, held for this run, written out as the coverage sheet, **never** written
into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some underscored, some hyphenated.
- **A near-substitute is not a substitute.** A **P&L expense line** for bank charges is a total;
  it cannot tell you *which* fee, on *what* date, for *what* service. Unit-rate analysis and
  miscoding detection both need transaction-level detail. If the detailed ledger tool is
  disabled, the analysis collapses to a single number — say so rather than presenting a trend of
  totals as a fee analysis.
- **The transaction-count tools are as important as the fee tools here.** Deposits, transfers,
  bill payments and customer payments supply the denominators for every unit rate. Check their
  policies deliberately; without them you have costs with nothing to divide by.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: base currency (which tells you whether FX and
international fees are even likely), fiscal calendar, country / region, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Bank statements** | **Required — [manual]**, always | Ask for them. Without them the analysis covers only posted fees, and the output must say so. If the user cannot supply them, ask specifically for the bank's **account analysis statement**, which itemises fees far better than a normal statement. |
| **GL detail for bank fee, interest, and cash accounts** | **Required — usually [auto]** | Pulled from the connected books. Confirm which accounts these are, by their real names. |
| **Period** — date range | **Required** | Never default it. Ask for at least 13 months if trends are wanted, so year-on-year comparison is possible. |
| **Banking products in use** — accounts, wires, ACH, lockbox, merchant services | Recommended — **[manual]** | Tells you which of the eight fee buckets should even appear. A bucket that should exist but shows no fees is a finding. |
| **Fee schedule / contract** — the rate sheet | Recommended — **[manual]** | Without it you can measure what you *paid* per transaction but not compare it to what you were *promised*. |
| **Earnings credit rate (ECR)**, if the bank applies one | Recommended — **[manual]** | See Step 5; it materially changes the true cost. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Bank statements, the fee schedule and the product list will all be `[manual]`. Ask for each, and record what was not supplied. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the period
or the entity.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what
is new, changed, or contradicted. The account mapping, product list and fee schedule should not
be re-asked every month.
