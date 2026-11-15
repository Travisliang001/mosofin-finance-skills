<!-- nonprofit-fund-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before classifying anything. This ordering is the contract. Do not
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

**Check for a connected donor CRM or grant management platform.** One would supply **donor stipulations,
conditions, pledge schedules and restriction terms** — converting the largest manual component here. Most
accounting connections do not include one.

Settle the entity scenario:

- **Single-entity** — one company file.
- **Multi-entity** — common in the sector: **an operating charity with a separate trading subsidiary**, **a
  supporting foundation holding endowment**, **affiliated chapters**. Ask which set. See the cross-entity
  step, which matters here because **a restriction travels with the money.**

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

**Check specifically that the reads return a dimension per transaction** — class, department or location.
**The functional matrix depends on it entirely.**

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **A program class is not a functional classification.** The central warning above.
  - **A restricted balance is not a restriction.** The account shows an amount; **only the donor's
    stipulation says what it is for.**
  - **Board-designated is not donor-restricted**, and **both may sit in the same account.** See the edge
    cases — the difference is who can undo it.
  - **A grant is not necessarily a contribution.** Many are exchange transactions.
  - **A donor record is not a donor stipulation.**
- **There is no donor agreement, no endowment deed, no fair value and no allocation study on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, **fiscal calendar and year-end** —
frequently not December for charities — country / region.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Organization profile** — mission, programs, sources of funding | **Required — [manual]** | Shapes the functional split. |
| **Reporting framework** — ASC 958 / local NFP framework | **Required — [manual]** | |
| **Period** | **Required** | |
| **Contribution data** — donor, amount, restrictions, date, conditions | **Required — [gated]** | **Amounts and dates `[auto]`; restrictions and conditions `[manual]`.** |
| **Grant agreements** — conditional vs. unconditional, restrictions, terms | Recommended — **[manual]** | See `grant-accounting-nonprofit-restricted-funds`. |
| ~~Net asset balances by class at opening~~ | **Now [gated]** | **`[auto]` if the chart separates classes; otherwise `[manual]`.** |
| ~~Expenses by natural and functional classification~~ | **Now [gated]** | **Natural `[auto]`; functional `[auto]` only if tracked as a dimension.** |
| **Investment income**, including endowment activity | Recommended — **[gated]** | Income `[auto]`; the restriction on it is `[manual]`. |
| **In-kind contributions** | If applicable — **[manual]** | Only in the ledger if already recorded. |
| **How shared costs are allocated between functions** | **Required for the matrix — [manual]** | Time studies, square footage. **Not in the ledger.** |
| **Whether classes represent programs or functions** | **Required — Mosofin addition** | **Decides whether the functional matrix is possible.** |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the period. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. no restricted net asset account in a charity with restricted funding. |
| **Confirm manual evidence** | **Required** | Stipulations, conditions and allocation bases are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a restriction, a
condition, an allocation basis, or a functional split.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only what changed.
The account map, the dimension mapping, the allocation methodology and the classification decisions persist;
**every balance and every release is re-obtained.**
