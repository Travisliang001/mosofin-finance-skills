<!-- personal-tax-return-prep · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace and the taxpayer
  - Gate 1 — Discover live datasources and settle the scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile the entity, then interview the taxpayer

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.

Run Gates 0 → 1 → 2 → 3 in this order. **Where no business is connected, Gates 1 and 2 will establish that
quickly and the skill proceeds entirely on supplied documents** — which is a normal and complete outcome.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a client-side
`mcp__…` namespace; that string is composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace and the taxpayer

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with `workspace_ids=[…]`
  and `mode="single"` / `mode="multi"`.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the opaque
`ws_…` handle.

**And confirm the taxpayer — a Mosofin addition specific to this skill.** **Whose return is this, and what
is their relationship to the connected business?** Owner, director, partner, employee, or none. **Do not
read owner-specific figures without establishing that the person asking is entitled to them.**

## Gate 1 — Discover live datasources and settle the scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Settle which of two situations applies:**

- **No business connection relevant to this taxpayer** — **the workflow runs entirely on supplied
  documents.** **This is a complete and normal outcome**; say so and proceed.
- **The taxpayer owns or draws from one or more connected entities** — **those entities supply specific
  inputs**, listed below. **Ask which entities, and in what capacity.**

**Where several entities are connected, only those the taxpayer has an interest in are in scope for this
return.** Reading the others would be compiling data about a person's business associates for their personal
tax file.

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Discover enabled tools → build the capability map


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


For **each in-scope datasource** (and **per company file** — pass `data_source_id`), call
`get_datasource_tools`. Bucket every tool by `effective_policy`:

| `effective_policy` | The task becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Pull the evidence directly. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and ask the user to supply that evidence another way. |

Resolve **every business-sourced figure** against these buckets. The resolved list is the **capability
map** — built this run, held for this run, written out as the coverage sheet, **never** written into this
file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **Accounting profit is not taxable business income.** The business computation has its own adjustments —
    see `tax-return-prep-corporate`.
  - **A distribution recorded in the accounts is not necessarily taxable in the year it was recorded.**
    Timing depends on declaration, payment and jurisdiction.
  - **A drawings balance is not income**, and in some jurisdictions **an overdrawn owner's account has tax
    consequences of its own** — see the edge cases.
  - **Salary in the business's payroll is not the taxpayer's total employment income.** They may have other
    employers.
- **There is no personal income statement, no brokerage record, no rate table and no allowance on this
  surface.**

## Gate 3 — Profile the entity, then interview the taxpayer

Where a business is in scope, call the platform's company-profile tool (on QuickBooks, `get_company_info`)
for each in-scope entity. **Derive** the legal name, currency, **fiscal year end — which may not match the
personal tax year**, and country.

**Ask the taxpayer or their adviser** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Jurisdiction and tax year** | **Required — [manual]** | **The personal tax year may differ from the business year end.** |
| **Filing status / personal circumstances** — single, married, dependents, residency | **Required — [manual]** | |
| **Income documents** — employment, self-employment, investment, rental, pension, capital gains, other | **Required — [gated]** | **Business-sourced items may be `[auto]`; everything else is supplied.** |
| **Current rates, brackets, allowances** | **Required — [manual]**, always | **Ask for the values, their source and their year.** |
| **Deductions / reliefs** | **Required — [manual]** | Jurisdiction-specific. |
| **Tax credits** | Recommended — **[manual]** | |
| **Taxes already paid** — withholding, estimated payments | **Required — [gated]** | **Owner salary withholding may be `[auto]`**; personal payments are not. |
| **Prior year return** | Recommended — **[manual]** | For carryforwards and continuity. |
| **Residency / domicile details** | If applicable — **[manual]** | **Cross-border: flag for specialist.** |
| **Which connected entities the taxpayer has an interest in**, and in what capacity | **Required — Mosofin addition** | Scopes what may be read. |
| **Confirm scope** | **Required** | Read back the taxpayer, the tax year, and the entities in scope by `display_name`. |
| **Confirm manual evidence** | **Required** | Every personal document, rate and allowance is `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a rate, a band, an
allowance, a residency conclusion, or a filing status.

**On later runs**, read stored preferences first — **and note that Step 11 stores almost nothing** for this
skill.
