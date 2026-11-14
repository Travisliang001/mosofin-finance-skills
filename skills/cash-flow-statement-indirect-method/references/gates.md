<!-- cash-flow-statement-indirect-method · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before building anything. This ordering is the contract. Do
not skip a gate because a previous conversation covered it — connections, permissions, and company
files change between periods.

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

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The statement runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every line carries its entity's `display_name`. **A consolidated
  cash flow statement is not the sum of entity statements**: intercompany transfers net to zero in
  the group but appear as real cash movements in each entity, and they must be eliminated. See the
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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map**
— built this run, held for this run, written out as the coverage sheet, **never** written into this
file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled —
  some underscored, some hyphenated.
- **The general-ledger tool is the critical one in this skill.** Without transaction-level movement
  on the fixed-asset, debt and equity accounts, capex cannot be separated from disposals and the
  financing section must be solved for rather than read. If it is disabled, say so plainly: the
  statement becomes a set of derived estimates and the supplemental detail must be supplied.
- **A near-substitute is not a substitute, and the temptation here is specific.** The platform's own
  cash flow report is a *different thing* from the statement you are building — it is a starting
  point and a cross-check. **Do not hand it over as the deliverable**, and do not assume it strips
  out acquisitions, FX and non-cash movements correctly. Rebuild, then compare.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: legal name, **functional / presentation currency**,
**fiscal calendar and year-end** (which defines the period and the comparative), country / region.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Balance Sheet — current period** | **Required — usually [auto]** | Pulled at the period-end date. |
| **Balance Sheet — prior period** (same date level) | **Required — usually [auto]** | Pulled at the comparative date. **Both must be at the same level of detail** or the changes will not map. |
| **Income Statement for the period** | **Required — usually [auto]** | Pulled. |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | Decides interest and dividend classification, restricted cash, overdrafts and leases. Never infer from country. |
| **Functional / presentation currency** | **Required — usually [auto]** | Derived; confirm only on a contradiction. |
| **Supplemental detail** — capex, debt proceeds / repayments, dividends, equity issuances, FX impact, non-cash transactions | **Required for accuracy — largely [auto]** | See the note above: the general ledger supplies most of this. Ask only for what it cannot show — chiefly acquisitions and the FX split. |
| **Method preference** — indirect (default) / direct | Optional | If direct is chosen, the indirect reconciliation is still built — see Step 8. |
| **Cash & cash equivalents definition** — what counts | Recommended — **[manual]** | Including **which accounts are restricted**, which the framework then decides how to present. |
| **Interest and dividend classification policy** (IFRS) | **Required if IFRS** | IFRS permits choices; the entity's elected policy must be applied consistently. |
| **Acquisitions or disposals of businesses in the period** | **Required if any** | **[manual]** — they distort every working-capital change and must be stripped out. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required if Gate 2 produced any [manual]** | |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the period,
the framework, the cash equivalents definition, or the entity.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only what
is new. The framework, the classification policy, the cash definition and the account mappings
should not be re-asked every period.
