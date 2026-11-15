<!-- goodwill-and-impairment-testing · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before testing anything. This ordering is the contract. Do not
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

**Gate 1 matters structurally here, because goodwill usually arises from acquiring a business — and that
business is often a separate company file.** **A reporting unit or CGU may map to an entire connected
entity**, which makes the connected list a candidate unit-of-account structure. Ask.

Settle the entity scenario:

- **Single-entity** — one company file; the unit of account sits inside it, identified by segment.
- **Multi-entity** — **the common case where goodwill exists**. Ask which entities, and **whether the
  reporting units or CGUs correspond to entities, to segments within them, or to neither.** See the
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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute**, and this skill has one that is unusually tempting:
  - **A class, department or location is not a CGU.** **A CGU is the smallest group of assets generating
    largely independent cash inflows** — a definitional test about cash independence. **How someone
    configured segment tracking in the accounting system is a reporting convenience.** The two often
    coincide, and coinciding is not the same as being defined by. **Use the dimensions as a starting
    proposal; confirm the unit of account with the user.**
  - **Carrying amount is not book value in the loose sense** — for a CGU it includes allocated goodwill and
    excludes items not part of the unit. Assembling it needs the allocation, which is `[manual]`.
  - **A decline in segment profit is not impairment.** It is an indicator that a test is required.
  - **Net book value is not fair value.** Ever.
- **There is no valuation, no forecast, no discount rate and no market capitalization on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar and **year-end** —
which is when the annual test falls — country / region.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Asset / unit being tested** — goodwill / indefinite-lived intangible / long-lived asset | **Required — [gated]** | **What exists is `[auto]`**; what is being tested is the user's call. |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | **Ask first.** The mechanics diverge completely from Step 4 onward. |
| **Unit of account** — reporting units (US GAAP) / CGUs or groups (IFRS) | **Required — [gated]** | Propose from the segment dimensions; **confirm against the definitional test.** |
| ~~Carrying amount~~ | **Now [auto]**, except the allocation | Balances are readable; **goodwill allocated to each unit is `[manual]`.** |
| **Cash flow projections** | **Required for quantitative test — [manual]** | **Never fabricate.** Ask for the budget and who approved it. |
| **Discount rate (WACC)** — pre-tax (IFRS) or post-tax (often US GAAP) | **Required — [manual]** | **Ask which basis**, and check it matches the cash flow basis. |
| **Comparable market data** | Recommended — **[manual]** | For the market approach. |
| **Triggering events**, if interim test | If applicable — **[gated]** | **Two of eight are `[auto]`**; see Step 2. |
| **Prior impairment history** | Recommended — **now [auto]** | Readable from the impairment accounts; **governs IFRS reversal.** |
| **Goodwill allocation to units**, and its basis | **Required if testing goodwill — [manual]** | **The allocation drives the outcome**; see the edge cases. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and the units being tested. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. an annual test date that does not match the year-end. |
| **Confirm manual evidence** | **Required** | Every valuation input is `[manual]`. Record what was supplied, **its source, and its date**. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a fair value, a
discount rate, a growth rate, or a cash flow projection.

**On later runs**, read stored preferences first (Step 12), confirm in one line, and ask only what changed.
The unit-of-account definitions, the goodwill allocation basis, the framework and the test date persist;
**every valuation input and every carrying amount is re-obtained each time.**
