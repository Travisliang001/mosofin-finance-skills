<!-- intangibles-and-amortization · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Check for a connected fixed-asset or intangible register module**, and for a **project-tracking or time
system**. The first would make the register `[auto]`; **the second would make the development-cost
capitalization far stronger**, since capitalizable labour needs hours by project and stage.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`.
- **Multi-entity** — ask which set. **Intangibles frequently arise on acquisition and sit in the acquirer's
  books while the business they relate to sits elsewhere**, and **internally developed software is often
  built by one group entity and used by all.** See the cross-entity step.

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
  - **The GL intangible balance is not an intangible register.** It is a total.
  - **Development spend is not capitalizable cost.** The stage determines that, and the stage is not a
    ledger field.
  - **A cost posted to an intangible account is not proof it qualified** — it is proof somebody coded it
    there. **This matters more for intangibles than for fixed assets**, because the capitalization criteria
    are judgmental rather than a simple threshold.
  - **No accumulated amortization is not proof an asset is indefinite-lived.** It may simply never have been
    amortized.
  - **A project class is not a project stage.** Tagging tells you which project; it does not tell you
    whether the work was planning, building or maintaining.
- **There is no intangible register, no useful life, no stage determination and no valuation on this
  surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, **functional currency**, fiscal calendar and
year-end, country / region.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Existing intangibles register** | Recommended — **[manual]** | **The core gap.** Without it, movements and totals still reconcile; asset-level amortization does not. |
| ~~New acquisitions or development costs~~ | **Now largely [auto]** | **Derived from debits to the intangible accounts**, and **development spend is readable by project.** Confirm rather than request. |
| **Reporting framework** — US GAAP / IFRS / local GAAP | **Required — [manual]** | **The frameworks differ materially on development costs.** Ask first. |
| **Asset class policies** — useful life, or indefinite, per class | **Required — [manual]** | The ranges in Step 2 are ranges, not a policy. |
| ~~Functional currency~~ | **Now [auto]** | From the profile. |
| ~~Chart of accounts~~ | **Now [auto]** | From `search_accounts`, including whether accumulated amortization is per class or consolidated. |
| **Capitalization policy for internally developed intangibles** — **which stages qualify** | **Required — [manual]** | **The decisive input for Step 4**, and the one the ledger cannot supply. |
| **Project stage dates**, per capitalized project | **Required if capitalizing development — [manual]** | When the application development stage began and ended. |
| **Impairment indicators**, if any | If applicable — **[manual]** | |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the period. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | The register, the lives, the policy and the stage dates are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a useful life, a
capitalization stage, or an indefinite-life conclusion.

**On later runs**, read stored preferences first (Step 13), confirm in one line, and ask only what changed.
The class policies, the capitalization policy, the account map and the project mapping persist; **the
balances, the movements and the register are re-obtained every period.**
