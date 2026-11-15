<!-- business-combinations-asc805 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before recording anything. This ordering is the contract.
Do not skip a gate because a previous conversation covered it — connections, permissions, and
company files change, and after an acquisition they change a lot.

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

**This gate carries a question specific to this skill, and it changes the whole run: is the
acquiree connected as its own company file?**

- **Acquirer only connected** — the acquiree's book values, results and history are all
  **[manual]**. Ask for its trial balance and P&L at the acquisition date.
- **Both acquirer and acquiree connected** — the acquiree's pre-acquisition book values, its
  post-acquisition results, and its prior-period comparatives are **[auto]**. Establish **which
  `display_name` is which role** and state it explicitly. Confusing acquirer and acquiree in a
  purchase price allocation inverts the entire entry.

This is inherently a **multi-entity** skill even when only one file is connected, because the
accounting spans two entities by definition. Every figure must carry the `display_name` and the
role — *acquirer* or *acquiree* — it belongs to. Never blend the two before the acquisition date;
that is precisely what the acquisition entry exists to do, on one specific date.

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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability
map** — built this run, held for this run, written out as the coverage sheet, **never** written
into this file.

Rules that bite hardest here:

- **Check the acquiree's policies separately from the acquirer's.** Permissions are per company
  file, and a newly connected acquiree frequently has a different — often narrower — policy set
  than the established acquirer.
- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled
  — some underscored, some hyphenated.
- **A near-substitute is not a substitute, and here the trap is fundamental: a book value is not a
  fair value.** The entire point of a purchase price allocation is that the acquiree's carrying
  amounts are *replaced* by fair values. Reading the acquiree's balance sheet gives you the
  **left-hand column** — where things started — and nothing more. **Never present a book value as
  a fair value**, and never let an unvalued line default to its carrying amount without saying
  that is what happened.
- **There is no valuation tool, and there never will be.** Do not look for one.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for **each** entity —
acquirer and, where connected, acquiree.

**Derive silently** what the profiles answer: legal names, base currencies (a difference between
them raises a translation question), fiscal calendars and year-ends (a difference matters for the
pro-forma disclosure), countries, industries.

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profiles answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Deal terms** — parties, structure, consideration (cash, stock, contingent), date | **Required — [manual]** | The foundation of everything. Never inferred. |
| **Acquired entity's pre-acquisition balance sheet** at the acquisition date | **Required — [auto] if the acquiree is connected**, otherwise **[manual]** | See Gate 1. Confirm which `display_name` is the acquiree. |
| **Fair value valuations** of identifiable assets and liabilities | **Required — [manual]**, from a valuation specialist | The skill will not produce these. |
| **Identifiable intangibles list** with fair values | **Required — [manual]** | Same. |
| **Reporting framework** — US GAAP / IFRS | **Required** | Decides the NCI measurement choice in Step 5. Never infer from country. |
| **Contingent consideration terms** — earnouts | If applicable — **[manual]** | Including the classification analysis: liability or equity. |
| **Acquirer's existing interest** (step acquisition) | If applicable — **[manual]** | |
| **Non-controlling interest details** — if less than 100% acquired | If applicable — **[manual]** | |
| **Transaction costs** — for expense classification | Recommended — **partly [auto]** | Deal-related legal and advisory fees are often identifiable in the ledger; ask for the total so you can test it against what was posted. |
| **The acquisition date** as a precise date | **Required** | Never default it. Everything is measured on this date. |
| **Confirm roles** — which `display_name` is acquirer, which is acquiree | **Required** | |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Every fair value will be `[manual]`. Record which have been supplied and which are outstanding. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the
acquisition date, the framework, the NCI measurement choice, any fair value, or which entity is
the acquirer.

**On later runs** — this skill recurs through the measurement period and at each subsequent
reporting date — read stored preferences first (Step 11), confirm in one line, and ask only what is
new. The deal's structure does not change; the provisional amounts do.
