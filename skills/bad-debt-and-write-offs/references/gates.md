<!-- bad-debt-and-write-offs · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before computing anything. This ordering is the contract.
Do not skip a gate because a previous conversation covered it — connections, permissions, and
company files change between periods.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a
client-side `mcp__…` namespace; that string is composed by whichever MCP client is running.


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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`. An
  allowance computed over part of a group understates the group's credit risk.

A workspace can connect the **same platform several times** — several company files. Each is its
own row with its own `data_source_id` and `display_name`.

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every loss rate, allowance and write-off carries its
  entity's `display_name`. **Loss rates are entity-specific and must not be pooled without
  saying so** — a wholesale entity and a retail one have genuinely different collection
  experience, and blending them produces a rate that describes neither.

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
- **A near-substitute is not a substitute.** A **customer balance** report gives one total per
  customer with no aging bands. Since the whole aged-receivable method assigns a *different loss
  rate to each band*, a balance report cannot drive it — using it would apply one blended rate
  to everything and quietly misstate the allowance. If the aging tool is disabled, either
  reconstruct the aging from invoice-level data (labelled as reconstructed) or mark the task
  `[manual]`.
- **Check whether the aging tool accepts a past `report_date`.** This is the specific capability
  that makes historical loss rates derivable. If it does, Step 1's loss rates are `[auto]`. If
  it does not, they are `[manual]` and must be supplied — say which applies before promising a
  historically-supported rate.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: base currency, fiscal calendar and year-end,
country / region, industry. Industry is a real input here — it sets expectations for what a
plausible loss rate looks like, though it never replaces the entity's own history.

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Reporting framework** — US GAAP (ASC 326 / CECL) / IFRS (IFRS 9 ECL) / Local GAAP / Other | **Required** | **The skill builds whichever framework is specified. It does not pick.** Never infer it from the entity's country. |
| **A/R aging at period end** — detailed by customer | **Required — usually [auto]** | Normally pulled. Confirm the as-of date. |
| **Historical loss data** — past 3–5 years of write-offs / recoveries by aging bucket | **Required for CECL/ECL; otherwise recommended — often [auto]** | See Gate 2: frequently derivable from past agings plus bad-debt account movement. Ask the user only for what the books cannot reach, and tell them which is which. |
| **Customer-specific risk information** — bankruptcy filings, dispute status, credit changes | Recommended — **[manual]** | The books do not know a customer has filed for insolvency. **Never infer it from age alone.** |
| **Forward-looking economic indicators** | Optional — **[manual]**, required if using CECL/ECL | The forecast is the user's; this skill applies it, never invents it. |
| **Existing allowance balance** — current allowance from the GL | **Required for true-up — usually [auto]** | Pulled from the allowance account. Confirm which account it is, by its real name. |
| **Chart of accounts** — accounts to post to | **Required — usually [auto]** | Confirm the allowance, bad-debt expense and recovery accounts by name. |
| **Tax jurisdiction** — for tax relief on write-offs | Recommended — **[manual]** | Drives the Step 5 tax-recovery entry, which is never claimed without confirmation. |
| **Write-off authority matrix** — who may approve a write-off, up to what value | **Required if writing anything off** | **[manual]**. A write-off without approval evidence is not a write-off, it is a loss. |
| **Period being reported** | **Required** | Never default the period. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required if Gate 2 produced any [manual]** | For each gap, ask whether the user can supply it, and how. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the
framework, the period, the loss rates, or the entity.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what
is new, changed, or contradicted. The framework, the account mapping and the authority matrix
should not be re-asked every period; the loss rates should be **re-derived**, not recalled.
