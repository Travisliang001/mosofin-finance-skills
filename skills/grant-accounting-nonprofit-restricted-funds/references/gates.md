<!-- grant-accounting-nonprofit-restricted-funds · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before recognising anything. This ordering is the contract. Do not
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

**Check for a connected grant management or donor CRM platform.** If one is live, **the grant register, the
agreement terms and the reporting calendar may become `[auto]`**, which converts this skill's largest manual
component. Most accounting connections do not include one.

Settle the entity scenario:

- **Single-entity** — one company file holding all funds and programs, distinguished by a dimension.
- **Multi-entity** — ask which set. **Nonprofits commonly have affiliated entities, a supporting foundation,
  or a fiscal sponsorship arrangement.** See the cross-entity step, which matters here because **a grant
  restricted in one entity's hands does not become unrestricted by being transferred to another.**

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
  - **Contribution revenue recorded is not contribution revenue properly recognised.** If the grant was
    conditional, the entry was premature — and it looks identical.
  - **A class or program is not a grant.** Several grants often fund one program, and one grant often spans
    several programs. **Ask how this entity's dimensions map to grants** before treating a class total as a
    grant total.
  - **Spend tagged to a grant is not allowable spend.** Allowability is a rule in the agreement.
  - **Cash received is not revenue**, and **revenue is not release from restriction.** Three different
    events, frequently conflated, and this skill has to keep them apart.
- **There is no grant agreement, no allowable cost rule and no indirect cost rate on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, **fiscal year end** — which for
nonprofits is frequently not December — country / region.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Grant agreements** — terms, restrictions, conditions, reporting | **Required — [manual]** | **The core input.** Ask for the award letters, not a summary. |
| ~~Chart of accounts and fund structure~~ | **Now [auto]** | Accounts and the class / program / fund dimensions. **Confirm how dimensions map to grants.** |
| **Budget and allowable cost rules** — grant budget by category | **Required — [gated]** | **The budget may be readable**; the allowability rules are `[manual]`. |
| ~~Expenditures tagged to grant / program~~ | **Now [auto]** | The strongest input this skill has. |
| ~~Cash receipts by grant~~ | **Now [auto]** | Deposits by grant or funder. |
| **Conditional or unconditional**, per grant | **Required — [manual]** | **Ask explicitly: is there a barrier and a right of return?** The answer decides when revenue exists at all. |
| **Purpose and time restrictions**, per grant | **Required — [manual]** | Needed to compute release. |
| **Indirect cost rate**, if any | If applicable — **[manual]** | Negotiated rate or de minimis; not in the ledger. |
| **Reporting deadlines** per funder | Recommended — **[manual]** | Drives the calendar output. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the grants covered. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a grant period that does not fit the fiscal year. |
| **Confirm manual evidence** | **Required** | Agreements, conditions and cost rules are `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a restriction, a
condition, an allowability rule, or an indirect cost rate.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The grant terms, the dimension mapping, the classification decisions and the release basis persist; **the
spend, the balances and the release amounts are re-obtained every period.**
