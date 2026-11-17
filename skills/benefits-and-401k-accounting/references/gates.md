<!-- benefits-and-401k-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Check specifically for a connected payroll or HR platform.** It is the single thing that would
convert contribution data, PTO balances and pay rates from `[manual]` to `[auto]`, and it changes
Steps 2, 3 and 6 substantially. Do not assume the workspace is accounting-only without looking.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every cost, liability and accrual carries its entity's
  `display_name`. Benefits are usually **plan-level but employer-level for accounting**: several
  entities may participate in one retirement plan while each bears its own cost. Never pool the
  cost without saying so — see the cross-entity step and the multiemployer edge case.

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
- **A near-substitute is not a substitute.** A **P&L benefit expense line** is a total; it cannot
  distinguish the employer's contribution from the employee's withholding, and confusing those
  two doubles the expense. Nor can an employee *list* substitute for a payroll register: knowing
  who works there says nothing about what each was paid or accrued. Where the detail is
  unavailable, mark the task `[manual]`.
- **There is no actuarial tool, and there never will be.** Do not look for one and do not
  substitute anything for it.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: base currency, fiscal calendar and year-end,
country / region — which narrows but does not decide the benefit regime — and industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Benefit types offered** — retirement (DC/DB), health, insurance, PTO, other | **Required — partly [auto]** | The chart of accounts hints at what exists (*`search_accounts`*); confirm the actual list, since an unfunded benefit may have no account yet. |
| **Plan terms** — contribution formulas, match, eligibility, vesting | **Required — [manual]** | Never in the ledger. Ask for the plan document or a summary. |
| **Payroll / contribution data** — employee and employer contributions by period | **Required — [manual]** unless payroll is connected | The books show what was *posted*; the register shows what was *earned and withheld*. Ask which you have. |
| **PTO policy and balances** — accrual rates, carryover, payout-on-termination, balances | **Required for PTO — [manual]** | Balances in hours per employee are not in the accounting system. |
| **Actuarial report (if DB plan)** — obligation, plan assets, assumptions | **Required for defined benefit — [manual]**, absolutely | Without it, Step 5 produces a structure with empty cells, and that is the correct output. |
| **Reporting framework** — US GAAP / IFRS | **Required** | Determines the DB treatment entirely. Never infer from the entity's country. |
| **Vesting provisions** — for employer contributions / benefits | Recommended — **[manual]** | Drives Step 6. |
| **Period being reported** | **Required** | Never default the period. |
| **Remittance deadlines** applicable to withheld contributions | Recommended — **[manual]** | Needed to judge the unremitted-balance check in Step 2. Ask; do not assume a number of days. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Plan terms, PTO balances and any actuarial report will all be `[manual]`. Record what was not supplied. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the
framework, the period, the plan terms, or the entity.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what
is new, changed, or contradicted. Plan terms, vesting schedules and the account mapping should not
be re-asked every period.
