<!-- ap-invoice-processing-and-3way-match · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before processing any invoice. This ordering is the
contract. Do not skip a gate because a previous conversation covered it — connections,
permissions, and company files change between runs.

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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`. An
  exception report that silently omits an entity implies those bills were matched when they
  were never looked at.

A workspace can connect the **same platform several times** — several company files, plus
purchasing, inventory or payment platforms. Each is its own row with its own `data_source_id`
and `display_name`. **If an inventory or warehouse platform is connected, check it for
receipt data** — that is exactly what turns a 2-way match into a real 3-way match.

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call
  targeting exactly one `data_source_id`. Every matched bill, exception and KPI carries its
  entity's `display_name`. Never match one entity's bill against another entity's purchase
  order.

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
map** — built this run, held for this run, written out as the coverage sheet, **never**
written into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some underscored, some hyphenated — and this skill uses both a bill *search* and a
  single-bill *read*, which are frequently styled differently in the same catalog.
- **A near-substitute is not a substitute.** If the purchase-order tool is disabled, a vendor
  *spend* report cannot stand in: spend tells you what was billed, never what was ordered, so
  it cannot detect the thing a match exists to find — a bill for more than the order.
  Likewise, an **attachment listing is not an approval record**: seeing that a file is
  attached proves a document exists, not that anyone authorised the spend. Mark those
  `[manual]`.
- **A tolerance is a policy, not a fact.** No tool supplies the entity's price and quantity
  tolerances. They are always `[manual]` input, confirmed at Gate 3 and stored in Step 8.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each
in-scope entity.

**Derive silently** what the profile answers: base currency, fiscal calendar, country /
region, time zone, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Invoice(s)** — the population being processed | **Required** | Ask the critical question: *bills already entered in the books* (**[auto]**) or *invoices still arriving* (**[manual]** — supply the PDFs or extracted fields)? |
| **PO data** — purchase orders and line items | **Required for PO invoices — usually [auto]** | Normally pulled from the connected books. |
| **Receiving data** — GRN / receipt quantities | **Required for 3-way match — usually [manual]** | Ask where receipts are logged. Without them there is no third leg, and the match is a 2-way match however it is labelled. |
| **Vendor master** — vendor list, terms, tax IDs | Recommended — mostly **[auto]** | Terms and names pull; tax IDs and certification forms are usually **[manual]**. |
| **Chart of accounts + dimensions** — accounts, departments, projects | **Required — usually [auto]** | Accounts, classes and departments normally pull; confirm which dimension carries what. |
| **Approval matrix** — spending limits by role | Recommended — **[manual]** | The books do not record who may approve what. Ask for it, and store it in Step 8. |
| **Policy constraints** — spend policy, tax rules | Recommended — **[manual]** | |
| **Match tolerances** — allowed price and quantity variance | **Required for matching** | Never assume a tolerance. Ask for both a percentage and an absolute floor. |
| **Period in scope** | **Required** | Never default the period. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required if Gate 2 produced any [manual]** | For each gap — and receipts, approvals and bank controls will be among them — ask whether the user can supply it, and how. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the
period, the tolerances, or the entity.

**On later runs**, read stored preferences first (Step 8), confirm in one line, and ask only
what is new, changed, or contradicted. Tolerances and the approval matrix in particular
should not be re-asked every cycle.
