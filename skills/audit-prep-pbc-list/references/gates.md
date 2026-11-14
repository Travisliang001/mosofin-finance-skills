<!-- audit-prep-pbc-list · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before building any list. This ordering is the contract.
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

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the
opaque `ws_…` handle.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. This matters more here than almost
  anywhere: an audit-readiness assessment that silently omits an entity tells the client they
  are ready when a whole component has not been looked at. Surface any `reconnect_url`.

A workspace can connect the **same platform several times** — several company files, plus
payment or payroll platforms. Each is its own row with its own `data_source_id` and
`display_name`.

**The audit scope is what decides the entity scenario here.** Ask directly: is the audit of a
single legal entity, or of a **group** (consolidated financial statements covering several
entities)?

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity / group audit** — ask which set. The workflow runs **once per entity**, every
  call targeting exactly one `data_source_id`, and every PBC item, readiness score and owner
  carries its entity's `display_name`. A **group audit** then adds consolidation support and
  component coordination — see the edge case.

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

| `effective_policy` | The PBC item becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Produce the schedule directly from the books. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and assign the item to a named human owner. |

Resolve **every PBC item in Part B** against these buckets. The resolved list is the
**capability map** — and in this skill it is unusually valuable, because *it is the readiness
assessment*. Which schedules the workspace can produce, and which it cannot, is exactly what
Step 4 is asking. It is built this run, held for this run, written out as the coverage sheet,
and **never** written into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some underscored, some hyphenated — and the payables and receivables aging reports
  frequently carry *different* policies in the same catalog. Check each one.
- **A near-substitute is not a substitute — and an auditor will notice.** A vendor *balance*
  report handed over as an "A/P aging" has no due-date buckets; a summary total handed over as
  a "subledger-to-GL reconciliation" reconciles nothing. Substituting produces exactly the
  rework the tie-out standard exists to prevent. Mark the item `[manual]` and name the export
  needed.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers, and do not ask about it:

- Legal name and address — which the audit report will carry
- **Fiscal calendar and year-end** — which sets the audit period and the subsequent-events
  window
- Base currency
- **Industry** — which drives Step 1's tailoring. This is the single most useful profile field
  here: it is what tells you not to request inventory support from a services firm

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Financial statements / TB for the audit period** — the numbers being audited | **Required — usually [auto]** | Normally pulled. Confirm the period and whether the figures are final or still moving. |
| **Type of engagement** — audit / review / compilation | **Required** | These demand very different levels of support. An audit seeks evidence; a **review** applies analytics and enquiry; a **compilation** does neither. Never assume "audit". |
| **Entity profile** — industry, size, complexity, public / private | **Required — partly [auto]** | Industry pulls; complexity, ownership and public status are **[manual]**. |
| **Auditor's PBC request, if received** | Recommended — **[manual]** | If it exists, **their list governs**. Map to it rather than building a parallel one. |
| **Prior year audit** — prior PBC list, adjustments, management letter | Recommended — **[manual]** | Prior audit adjustments may be visible as journal entries (**[auto]**), but the management letter is a document. |
| **Available support** — reconciliations and schedules already prepared | Recommended — **[manual]** | Ask what exists outside the books, so you do not re-request it. |
| **Key personnel / owners** — who owns each area | Recommended — **[manual]** | Every `[manual]` item needs a named human, or it will not get done. |
| **Materiality**, if the auditor has communicated it | Recommended | Drives Step 1 prioritization. Never invent a figure. |
| **Fieldwork start date** | **Required for the timeline** | Step 5 sequences backwards from it. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether this is a single or group audit. |
| **Confirm any profile contradiction** | **Required if one appears** | E.g. the profile's year-end does not match the stated audit period. |
| **Confirm manual evidence** | **Required** | For each `[manual]` item — and there will be many — ask who owns it and where it lives. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the audit
period, the engagement type, the materiality, or the entity.

**On later runs** — and audit prep is annual, so "later" means next year — read stored
preferences first (Step 9), confirm in one line, and ask only what is new, changed, or
contradicted. Last year's PBC list, owners and area map should be the starting point, not a
blank page.
