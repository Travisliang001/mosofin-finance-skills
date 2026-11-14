<!-- intercompany-reconciliation · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace
  - Gate 1 — Discover live datasources and settle the entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile the entities, then interview the user

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.

Run Gates 0 → 1 → 2 → 3 in this order, before matching anything. This ordering is the contract. Do not
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

**In this skill, multi-workspace mode is often the right answer.** Group entities are frequently split
across workspaces, and **an entity in another workspace is as unreconcilable as one that is disconnected**
unless that workspace is confirmed too. **Ask before assuming one workspace holds the group.**

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id` — **for each confirmed workspace.**

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**This gate is Step 1's input.** Record every connected company file by `display_name`. Then:

**Ask the user which of the connected entities form the group**, and — critically — **whether any group
entity is missing from the list.** A connected file that is not a group member is out of scope; **a group
member that is not connected is a pair that cannot be reconciled**, and the user needs to know that before
any work starts, not after.

**Single-entity is not a valid scenario for this skill.** If only one company file is connected, say so
plainly: **intercompany reconciliation requires at least two sides.** Offer to report the entity's IC
account balances and ageing — which is useful — but **do not call it a reconciliation.**

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Discover enabled tools → build the capability map


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


For **each in-scope datasource** — and **per company file**, passing `data_source_id` — call
`get_datasource_tools`. Bucket every tool by `effective_policy`:

| `effective_policy` | The task becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Pull the evidence directly. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and ask the user to supply that evidence another way. |

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

**Check capability per entity, and note that a pair is only as readable as its weaker side.** If entity A's
ledger is `enabled` and entity B's is `permission`-gated, **the pair is `[gated]`** — and if B's is
`disabled`, **the pair is `[manual]` however good A's access is.** Record the verdict **per pair**, not per
entity.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **One side's balance is not the pair's balance.** The whole skill exists because the two disagree.
  - **A customer or vendor record named like a group entity is not proof of an intercompany transaction** —
    it is a strong signal, and it needs confirming against the group entity list.
  - **An account named "Intercompany" is not necessarily all of the intercompany activity**, and not
    everything in it is necessarily intercompany. **Both directions need checking.**
  - **A matching amount is not a matched transaction** until the reference or the date supports it.
- **There is no FX rate service and no intercompany agreement on this surface.**

## Gate 3 — Profile the entities, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) **for each in-scope entity**.

**Derive silently** what the profile answers: **legal name — which is what the counterparty's ledger will
call it** — **functional currency**, fiscal calendar and year-end, country.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~List of group entities~~ | **Now [auto]** from Gate 1 | **Confirm which connected files are group members, and whether any member is missing.** |
| ~~Intercompany account ledger per entity~~ | **Now [auto]** | Transaction-level, both sides, same instant. |
| **Period being reconciled** | **Required** | |
| ~~Functional currency per entity~~ | **Now [auto]** | From each profile. |
| **Group reporting currency** | **Required — [manual]** | Not a ledger field. |
| **FX rates used** — per entity, per transaction date or month-end | Required if cross-currency — **[manual]**, always | **Ask for the table, its source and its dates.** Never supply a rate. |
| **Intercompany agreement / policy** — pricing methodology, payment terms | Recommended — **[manual]** | Decides several of the Step 4 causes. |
| ~~Chart of accounts, each entity~~ | **Now [auto]** | **Confirm which accounts are the IC accounts in each entity.** |
| **How each entity names the others** | **Required — Mosofin addition** | The counterparty may appear as a customer, a vendor, a class, or only in a memo. **This is the join.** |
| **Confirm scope** | **Required** | Read back group members by `display_name`, **and every pair that cannot be reconciled and why**. |
| **Confirm any profile contradiction** | **Required if one appears** | e.g. differing year-ends across the group. |
| **Confirm manual evidence** | **Required** | Rates and the agreement are `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an FX rate, a transfer
price, or a mismatch cause.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
The pair structure, the IC account map, the counterparty naming map and the known recurring causes persist;
**every balance, rate and mismatch is re-obtained each period.**
