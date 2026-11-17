<!-- government-fund-accounting-gasb · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before building anything. This ordering is the contract. Do not
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

**Check what kind of platform is connected.** A **specialized public-sector ERP** would supply funds, dual
basis and budgetary control natively, and most of this skill's `[gated]` verdicts would become `[auto]`.
**A commercial accounting platform will not** — and that is the case the structural note above addresses.
**Say which you are working with**, because it changes what every downstream figure means.

Settle the entity scenario, which in the public sector means the **reporting entity**:

- **Single company file** — one file holding all funds, distinguished by a dimension.
- **Multiple company files** — often **one file per fund or per component unit**, which is a legitimate and
  common structure. Ask which files make up the **primary government** and which, if any, are **component
  units**. See the cross-entity step.

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
- **A near-substitute is not a substitute**, and this skill has more of them than most:
  - **A class or department is not a fund.** See above.
  - **The platform's accounting-method setting is not the measurement focus.** "Accrual" in a commercial
    system is not GASB full accrual with an economic resources focus, and it is certainly not modified
    accrual.
  - **Retained earnings is not fund balance**, and **equity is not net position.** The labels the platform
    uses are commercial ones.
  - **A transfer between classes is not necessarily an interfund transfer** — it may be an allocation. But
    it is the right place to look.
  - **Revenue recorded is not revenue recognized under modified accrual** until the **availability** test
    has been applied.
- **There is no actuarial valuation, no capital asset register and no bond schedule on this surface** — see
  `fixed-asset-register-and-depreciation` and `debt-and-covenant-tracking` for the same gaps.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, **fiscal year end** — which for
governments is frequently 30 June rather than 31 December — country / region.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Entity type and jurisdiction** | **Required — [manual]** | State / local government, agency, district. |
| **Reporting framework** — GASB / IPSAS / other | **Required — [manual]** | **Ask first.** |
| **Fund structure** — funds in use, their types and purposes | **Required — [gated]** | **Propose from the dimension list; confirm the mapping.** |
| ~~Trial balances by fund~~ | **[auto] if a fund dimension exists**, otherwise **[manual]** | The pivotal question. |
| **Which basis the books are kept on** | **Required — [manual]**, and **Mosofin-specific** | See the structural note. Nothing downstream is interpretable without it. |
| **Budget data** | Recommended — **[gated]** | Some platforms hold budgets; the **budgetary basis** is `[manual]`. |
| **Revenue sources** — tax types, grants, fees, transfers | **Required — [gated]** | Accounts are `[auto]`; **the nonexchange classification is `[manual]`.** |
| **Long-term assets and debt** — capital assets, bonded debt, pensions, OPEB | **Required for government-wide — [gated]** | **Balances readable *if* on the books**; the registers and schedules are `[manual]`. |
| **Pension / OPEB actuarial reports** | If applicable — **[manual]**, always | **Never fabricate.** Often the largest line on the statement. |
| **Period** — fiscal year | **Required** | |
| **Fund balance constraints** — external restrictions, board commitments, assignments | **Required — [manual]** | **Nothing in a ledger records a governing-body resolution.** |
| **Component units**, and whether blended or discretely presented | If applicable — **[gated]** | Other connected files are candidates. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the funds covered. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a fiscal year end that disagrees with the period requested. |
| **Confirm manual evidence** | **Required** | The actuarial reports, the constraints and the registers are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a fund type, a
measurement basis, a fund balance classification, or a pension liability.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only what changed.
The fund structure and mapping, the basis-of-books answer, the classification decisions and the
reconciliation template persist; **the balances are re-obtained every period.**
