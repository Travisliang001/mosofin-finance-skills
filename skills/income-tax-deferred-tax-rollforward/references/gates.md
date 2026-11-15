<!-- income-tax-deferred-tax-rollforward · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Settle the entity scenario — and here it is inseparable from the tax question:

- **Single-entity** — one company file, and usually one taxpayer.
- **Multi-entity** — ask which set, **and then ask the question the ledger cannot answer: which entities
  are in which tax group, and in which jurisdictions?** **Deferred tax is computed per taxpayer per
  jurisdiction**, and legal entities, tax consolidation groups and reporting entities frequently do not
  coincide. See the cross-entity step.

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
  - **Book basis is not tax basis**, and the difference between them is the entire subject.
  - **The recorded deferred tax balance is not the correct one.** It is what was posted, usually by an
    annual journal from a workpaper maintained elsewhere — which is exactly why the footing check is worth
    running.
  - **Accumulated book depreciation is not tax depreciation.** See
    `fixed-asset-register-and-depreciation`: the tax schedule is not on this surface.
  - **A statutory rate is not an enacted rate for the reversal period**, and the rate to use is the one
    enacted at the reporting date for the period the difference reverses.
  - **Pre-tax book income is not taxable income.** The cumulative-loss test uses the evidence available;
    say which measure you used.
- **There is no tax return, no tax basis, no tax depreciation schedule, no enacted rate table and no NOL
  register on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, **fiscal calendar and year-end**,
country / region — **a pointer to the likely jurisdiction, not a statement of it.**

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Trial balance~~, and **book-to-tax adjustments** | **TB now [auto]**; **adjustments `[manual]`** | The adjustments are the tax analysis, not a ledger output. |
| **Tax returns / taxable income schedules** — prior and current year | Recommended — **[manual]** | The source of tax basis. |
| **Fixed asset schedules** — book vs. tax depreciation | Often required — **[gated]** | **Book side `[auto]`; the tax schedule is `[manual]`.** |
| **NOL / credit carryforwards** — by jurisdiction **+ expiry** | Often required — **[manual]** | **Expiry dates matter as much as amounts.** |
| **Tax rates** — enacted rates by jurisdiction | **Required — [manual]**, always | **Never supply a rate from memory.** Ask for the rate, the jurisdiction and the enactment date. |
| **Prior deferred tax workpapers** | Recommended — **[manual]** | The opening balances to prove against the ledger. |
| **Valuation allowance evidence** — forecasts, reversals, history | Recommended — **[gated]** | **The loss history is `[auto]`**; the forecast is not. |
| **Which entities are in which tax group and jurisdiction** | **Required if multi-entity — [manual]** | The ledger does not know. |
| **Whether the reversal periods are known** | Recommended — **[manual]** | Needed to pick the right enacted rate. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, the period, and the taxpayer(s). |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. a tax year that does not match the fiscal year. |
| **Confirm manual evidence** | **Required** | Tax basis, rates and NOLs are `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a tax rate, a tax
basis, a reversal pattern, or a valuation allowance conclusion.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
The difference inventory, the account map, the jurisdiction map and the reversal patterns persist; **every
balance, rate and allowance amount is re-obtained each period.**
