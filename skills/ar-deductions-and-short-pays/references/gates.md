<!-- ar-deductions-and-short-pays · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace
  - Gate 1 — Discover live datasources and settle the entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile the entity, then interview the user

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1 settle
*which books this is about*: the workspace, and the data sources inside it. **Part A then explores
what those confirmed sources can actually do** and personalises the run around them. Nothing is
read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** Say so once, then run the skill
manually on data the user supplies.

Run Gates 0 → 1 → 2 → 3 in this order, before analysing anything. Do not skip a gate because a
previous conversation covered it: connections, permissions and company files change between
periods.

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

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The log is built **once per entity**, every call targeting
  exactly one `data_source_id`, and every deduction carries its entity's `display_name`. A
  customer that buys from two entities has two sets of deductions; never net one against the
  other.

**Look for a connected CRM, EDI or retailer portal.** Retail customers often post the reason and
backup for a deduction in their own portal; if one is connected, it is the best source for the
customer's side of the claim.

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they expose and which
of it serves this request** — the tool catalogue in Gate 2, then what is already known about this
entity plus whatever still has to be asked in Gate 3.

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

- **Read the real tool name from the catalog, never from memory.**
- **A near-substitute is not a substitute.** An aging summary gives balances by customer, not
  the invoice and payment behind each deduction. Without invoice-level reads the log can list
  partly paid customers but not the deductions themselves: say so.
- **The backup is never in the books.** Proofs of delivery, carrier reports and agreements are
  **[manual]** on every path. Without them each item is "needs backup".

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, industry (retail
customers deduct far more often, and by reason code).

**Ask the user** what actually changes the work — Stage 1's table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **As-at date** | **Required** | Never default it. |
| **Where deductions are kept** | **Required** | A log, a separate account, or open invoice balances. |
| **Write-off policy** | Recommended — **[manual]** | Without it, no write-offs are proposed. |
| **Backup** | **Required — [manual]**, always | Proofs of delivery, carrier reports, agreements, contracts. |
| **Dispute window and customer rules** | Optional — **[manual]** | Default: over 90 days is at risk. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the date
or the entity.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what
is new, changed, or contradicted. The reason-code map and policy should not be re-asked every
month.
