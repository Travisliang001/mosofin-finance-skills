<!-- model-auditor-financial-model-review · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before tying anything out. This ordering is the contract. Do not
skip a gate because a previous conversation covered it — connections, permissions, and company files
change between periods.

**Steps 3, 4 and 5 can proceed without the gates** — they are spreadsheet inspection. **Step 2 cannot.**

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

**Confirm that the workspace holds the entity the model is about.** **A tie-out against the wrong company
file produces confident FAIL flags on a model that is correct**, which wastes everyone's time and damages
the reviewer's credibility.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Settle the entity scenario against **what the model represents**:

- **Single-entity model** — one company file, and the tie-out runs against it.
- **Consolidated model** — **the model's historicals are consolidated figures**, so **the tie-out needs
  consolidated source**, not the parent's and not a sum of entities. See the cross-entity step.

**Ask what the model covers before tying anything out.** **A consolidated model tied to a single entity's
books will fail on every line**, and the reviewer will spend an hour discovering why.

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

Resolve **every tie-out target in Step 2** against these buckets. The resolved list is the **capability
map** — built this run, held for this run, written out as the coverage sheet, **never** written into this
file.

**Where a read is unavailable, the corresponding tie-out reverts to OPEN** — the original's own status —
**and OPEN items are what a HOLD is made of.** Establish the map before promising a complete tie-out.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **A tied historical figure does not make the model correct.** The history being right says nothing
    about the forecast, the formulas or the logic.
  - **The current books are not necessarily what the model was built from** — and **not necessarily what
    was published either.** Three versions of the past can all be in play.
  - **A trial balance is not a financial statement.** A model line labelled "Revenue" may aggregate several
    accounts; **confirm the mapping before flagging a FAIL.**
  - **Cash in the ledger is not cash in the bank.** See `bank-reconciliation`.
- **There is no model, no formula, no cap table and no assumption support on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, **base currency** — which must match the model's —
**fiscal calendar and year-end**, which must match the model's period structure.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Financial model** | **Required — [manual]** | Not in the workspace. |
| ~~Source files~~ — historical financials, TB, forecasts, debt schedules, cap table, assumptions | **Mixed** | **Financials and TB now `[auto]`**; **cap table, debt schedules and assumption support remain `[manual]`.** |
| **Intended use** — board, lender, investor, M&A, client, internal | **Required — [manual]** | **Ask first.** It sets the bar: a lender model and an internal plan warrant different severity thresholds. |
| **Materiality threshold** | Recommended — **[manual]** | **Needed for the IMMATERIAL DIFF flag.** Without it, every penny difference is a FAIL. |
| **Review scope** — full model / selected tabs / specific issue | **Required — [manual]** | |
| **Known problem areas** | Recommended — **[manual]** | |
| **What the model represents** — which entity, or the consolidated group | **Required — Mosofin addition** | **Before any tie-out.** |
| **The model's as-at date and source vintage** | **Required — Mosofin addition** | When were its actuals extracted? It predicts what the tie-out will find. |
| **The model's account mapping**, if line labels differ from the chart | Recommended — **[gated]** | Prevents false FAILs. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the periods tied. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a model on a December year-end for a June-year-end entity. |
| **Confirm manual evidence** | **Required** | The model, the cap table and the assumption support are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a materiality
threshold or a mapping between model lines and accounts.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The line-to-account mapping, the materiality basis and the checklist persist; **every tie-out is
re-performed.**
