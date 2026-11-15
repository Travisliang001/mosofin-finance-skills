<!-- 1099-and-t4a-prep · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before any vendor work. This ordering is the
contract. Do not skip a gate because a previous conversation covered it — connections,
permissions, and company files change between runs.

Call the Mosofin tools by the **bare names your own tool list exposes** —
`list_workspaces`, `get_agent_datasources`, `get_datasource_tools`,
`invoke_datasource_api_tool`, `get_skills`, `get_my_skill`, `create_skill`. Do not add a
`mosofin_` prefix and do not hardcode a client-side `mcp__…` namespace; that string is
composed by whichever MCP client is running and differs between clients.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → the tool auto-confirms it. Read the workspace **name** back to the
  user and **wait for an explicit yes** before doing anything else.
- **Two or more** (`selection_required`) → ask **in chat**: "Is this a single-workspace or
  a multi-workspace job?" Then ask which workspace(s) **by name**, and call
  `list_workspaces` again with `workspace_ids=[…]` and `mode="single"` or `mode="multi"`.

Never auto-pick a workspace. Never print an internal numeric tenant id — refer to a
workspace by its human name, and pass the opaque `ws_…` handle between tools.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- Rows with `connected: true` are **in scope**.
- Rows with `connected: false` are **excluded — and you must name them as excluded** to
  the user ("*Northwood Demo Books* is connected but not active, so nothing in this return
  comes from it"). Silently ignoring a dead connection makes the return look more complete
  than it is. If the envelope offers a `reconnect_url`, surface it.

A workspace can connect the **same platform several times** — three QuickBooks company
files for three franchise locations, plus two payment-processor accounts. Each is its own
row with its own `data_source_id` and `display_name`. Information returns are filed **per
filer**, so the entity question is not cosmetic here — it decides how many returns exist.

When more than one entity is live, ask the user which scenario applies:

- **Single-entity** — ask which company by `display_name`. The whole workflow runs against
  that one `data_source_id`, and produces one filer's set of returns.
- **Multi-entity** — ask which set (all three locations? two of them?). The workflow runs
  **once per entity**, every call targeting exactly one `data_source_id`, and a combination
  step follows (see "Both entity scenarios" in Part B). Every intermediate and final result
  is **labelled with its datasource and `display_name`**. Two entities' payment totals are
  never added into one figure without that label — for information returns that would be a
  filing error, not just untidy presentation.

Refer to companies by `display_name`. Never show the raw `data_source_id` to the user —
pass it between tools.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Discover enabled tools → build the capability map


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


For **each in-scope datasource** (and, when several company files are live, **per company
file** — pass `data_source_id`), call `get_datasource_tools`. Bucket every returned tool by
its `effective_policy`:

| `effective_policy` | The task becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Pull the evidence directly. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and ask the user to supply that evidence another way. |

Then resolve **every task in Part B** against these buckets. That resolved list is the
**capability map**. It is built this run, held for this run, written out as the coverage
sheet — and **never** written into this file. Policies differ per workspace *and* per
company file, and change between periods.

Two rules that matter for this skill specifically:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some are underscored, some hyphenated. Always take the exact string from the
  Gate 2 listing.
- **A near-substitute is not a substitute.** If the tool that lists vendor payments in
  detail is disabled, a summary balance report answers a *different question* — it shows
  what you still owe a vendor, not what you actually paid them during the year, and an
  information return needs the second. Mark the task `[manual]` and say so plainly.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each
in-scope entity.

**Derive silently** everything the profile answers, and do not ask about it:

- Legal name and address of the payer (the filer) — this feeds the payer block of every form
- Fiscal calendar and year-end
- Country / region, which narrows but does **not** decide the reporting jurisdiction
- Base currency, which tells you whether a currency-conversion step is even needed
- Time zone
- Industry, which hints at likely form types (a construction company suggests UK CIS or
  Canadian T5018 may be in play)

**Ask the user** only what actually changes the work. This is where the original Inputs
table lives, minus what the profile already answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Reporting jurisdiction** — which country's information-return regime applies | **Required** | Never default this from the profile's country. A US-registered company can have UK CIS obligations. |
| **Tax / reporting year** — the year being reported | **Required** | Never default the period. Ask for exact start and end dates. |
| **Form types in scope** — e.g. 1099-NEC, 1099-MISC, T4A, T5018, CIS | **Required** | Ask which forms the user believes apply; do not infer. |
| **Reporting thresholds for that jurisdiction and year** — the dollar/pound amount above which a vendor must be reported | **Required — user supplies** | Do **not** apply a remembered figure. Thresholds change. If the user does not know, tell them to confirm with the tax authority or a tax adviser; this skill will not bake one in. |
| **Vendor tax forms on file** — W-9 / W-8 / CIS registration / equivalent | **Required — likely [manual]** | The signed certification form itself is a document, not ledger data. Ask how the user can supply it (a folder, an export, a spreadsheet). |
| **Vendor master** — names, tax IDs, entity types, addresses | **Required — usually [auto]** | Normally pulled from the connected books; ask only for what the books do not hold. |
| **Payment ledger for the year** — every payment to every vendor | **Required — usually [auto]** | Normally pulled; ask for anything paid outside the connected books (a separate bank, a personal card). |
| **Filing channel** — paper, e-file, or a filing vendor's system | Recommended | Affects formatting and due dates. |
| **Currency-conversion rule** | Required only if payments were made in more than one currency | Payment-date rate or annual average — the jurisdiction decides; the user tells you which. |
| **Confirm scope** | **Required** | Read back which company files are in scope and which are excluded, by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | E.g. the profile's fiscal year-end does not match the reporting year the user named. |
| **Confirm manual evidence** | **Required if Gate 2 produced any [manual]** | For each gap, ask whether the user can supply it, and how. |

Ask these as **one short batch**, not one question at a time. Propose sensible defaults
where reasonable — but **never** default the reporting year, the jurisdiction, the
thresholds, or the entity.

**On later runs**, read the stored preferences first (see the evolution step at the end of
Part B), confirm them in a single line, and ask only what is new, changed, or contradicted.
The interview shrinks. The gates never do.
