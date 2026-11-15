<!-- pensions-and-postretirement-asc715 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Settle the entity scenario — **and here the question is which entity sponsors the plan**:

- **Single-entity** — one sponsor, one plan.
- **Multi-entity** — **a group plan covering several entities is common**, and **the accounting sponsor is
  not always the entity whose employees are in it.** Ask which entity carries the obligation. See the
  cross-entity step.

**The plan itself is not a connected datasource.** Plan assets are held by a trustee or custodian, and
**their fair value comes from the actuarial report or the trustee's statement**, never from here.

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
  - **A recorded pension liability is not the funded status.** It is what was posted, possibly years ago,
    possibly from an earlier report.
  - **Employer contributions are not pension expense.** **Cash paid into the plan and the cost recognised in
    the period are different figures**, and conflating them is the classic small-entity error.
  - **Headcount is not a service cost driver you can compute with.** It is context.
  - **The AOCI balance is not the unrecognised gain or loss** until it has been agreed to the actuary's
    schedule.
- **There is no actuarial report, no plan asset valuation, no assumption set and no trustee statement on
  this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, **fiscal calendar and year-end —
which must match the actuarial measurement date**, country / region.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Actuarial valuation report** — period-end | **Required — [manual]**, always | **Everything flows from it.** Ask for the report, its measurement date and its author. |
| **Plan details** — plan type, participants, amendments | **Required — [manual]** | **Amendments create prior service cost**; they are easy to omit. |
| **Prior year rollforwards** — PBO/APBO, plan assets, AOCI components | Recommended — **[gated]** | **The AOCI and liability balances are `[auto]`; the actuarial components are not.** |
| **Payroll and headcount** — service cost drivers | Recommended — **[auto]** | **Context only**; the service cost is the actuary's. |
| **Discount rate and assumptions** — as disclosed in the report | **Required — [manual]** | **Never supplied from memory.** |
| **The framework** — ASC 715 or IAS 19 | **Required — Mosofin addition** | **They differ on the expected return / net interest treatment**; see Step 1. |
| **The measurement date** | **Required — Mosofin addition** | It must agree with the reporting date. |
| **Whether the plan is a defined benefit plan at all** | **Required — Mosofin addition** | **Defined contribution plans are not in scope**; see the edge cases. |
| **Confirm scope** | **Required** | Read back the sponsoring entity by `display_name`, the plan and the period. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a measurement date that does not match the year-end. |
| **Confirm manual evidence** | **Required** | The report and every assumption are `[manual]`. Record the report's date and author. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an assumption, a rate,
an obligation, or any actuarial component.

**On later runs**, read stored preferences first (Step 8), confirm in one line, and ask only what changed.
The plan details, the account map, the framework and the actuary persist; **every actuarial figure is
re-obtained from the current report.**
