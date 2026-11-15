<!-- healthcare-revenue-cycle-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before estimating anything. This ordering is the contract. Do not
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

**Confirm scope with particular care**, because a healthcare ledger may contain PHI and reading the wrong
one is not a neutral mistake.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Check specifically whether a practice management, EHR or billing platform is connected.** If one is,
**the billing side of the bridge becomes readable** and much of this skill's `[manual]` half converts —
**and the PHI rules above become more pressing, not less.** If none is, say plainly that the billing data is
supplied by hand and label it as such.

Settle the entity scenario:

- **Single-entity** — one company file, one provider.
- **Multi-entity** — common in healthcare: **a professional corporation and a management company, multiple
  practice sites, a hospital and its physician group.** Ask which set. See the cross-entity step.

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
  - **GL AR is not subledger AR.** The GL holds a summarised balance; the billing system holds the claims.
    **The whole point of Step 3 is that they must be compared, which means neither may stand in for the
    other.**
  - **A posted contractual adjustment is not a contract term.** It is what someone recorded.
  - **A write-off is not a bad debt** until you know whether it was charity care, a denial, or a
    contractual adjustment posted to the wrong place.
  - **A customer record is not a payer**, and a customer balance is not a payer class balance, unless the
    entity set them up that way.
  - **Aged AR in the GL is not the collectability picture** — payer AR and patient AR behave completely
    differently and must not be aged together.
- **There is no billing system, no payer contract, no denial reason code and no eligibility determination
  on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and year-end,
country / region.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Billing / claims data** — charges, payments, adjustments, payer | **Required — [manual]** unless a billing platform is connected | **Ask for it aggregated by payer and period**, not patient by patient. |
| **Payer contracts** — rates, fee schedules, reimbursement terms | Recommended — **[manual]**, always | The basis of the contractual allowance. |
| **Patient AR aging** — **by payer class** | **Required — [gated]** | **The billing system's aging is the real one**; the GL's is a summary. |
| **Denials and write-offs** — reasons, recoveries | Recommended — **[manual]** for reasons, **[auto]** for amounts | Reason codes are in the billing system. |
| **Charity care policy** — eligibility rules and accounting policy | Recommended — **[manual]** | **Decides presentation**; see Step 2. |
| ~~GL mappings~~ — revenue, contra revenue, AR, cash | **Now [auto]** | From `search_accounts`. **Confirm which contra accounts are which.** |
| **Whether gross charges are recorded in the GL at all** | **Required — Mosofin addition** | Some providers post net only. **It decides whether realization is computable.** |
| **Historical realization assumptions in use** | Recommended — **[gated]** | Compare against the `[auto]` computed rate. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the period. |
| **Confirm PHI handling** | **Required — Mosofin addition** | Confirm that aggregate-level output is acceptable and that no patient detail is to be reproduced. |
| **Confirm manual evidence** | **Required** | Contracts, denial reasons and eligibility rules are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a contractual
allowance rate, a reserve percentage, or a charity care classification.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The account map, the payer class mapping, the reserve methodology and the realization basis persist; **every
rate, balance and reserve amount is re-obtained each period.**
