<!-- foreign-currency-translation-asc830 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**In a group whose entities sit in different workspaces, multi-workspace mode is the normal case here** —
ask rather than assuming one workspace holds the whole group.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**This is Step 1's raw material.** For each connected company file, record the `display_name` and then read
its **home currency** from the company profile. That produces the entity-and-currency map the whole skill
runs on.

**A disconnected foreign subsidiary is not a gap in a workpaper — it is a subsidiary missing from the
group.** Translation covering three of four entities is not translation; it is a partial exercise that must
be labelled as one.

Settle the entity scenario:

- **Single-entity** — one company file. **Translation may still apply** if its functional currency differs
  from the reporting currency, **and remeasurement certainly applies** if it transacts in currencies other
  than its own. Do not assume a single entity means no FX work.
- **Multi-entity** — the normal case. Ask which entities form the reporting group, and **which currency the
  group reports in**.

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

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

**Check capability per entity, not once.** In a group, one subsidiary's connection is frequently more
restricted than the parent's, and **a translated group figure is only as good as its least-readable
member.**

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **The home currency is not the functional currency** — see above.
  - **A transaction-level exchange rate is not a period-end spot rate.** Even where the platform records
    rates on multicurrency transactions, those are deal rates on deal dates from whatever source the system
    used. **A translation rate table needs an approved source, a stated date and a stated rate type.**
  - **An account type is not a monetary / nonmonetary classification.** "Other Current Asset" holds both.
  - **A balanced translated balance sheet is not a correct one** — CTA absorbed the difference.
- **There is no FX rate service on this surface.** Every rate is `[manual]`, with source and date.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) **for each in-scope entity**.

**Derive silently** what the profile answers: legal name, **home currency** — the key field here — fiscal
calendar and year-end, country / region.

**Ask the user** what actually changes the work — the original Inputs table, minus what the connected books
already answer:

| What to confirm | Required? | Notes |
|---|---|---|
| **Entity structure** — parent / subs, ownership, reporting currency | **Required — [gated]** | **The entity list is `[auto]` from Gate 1; ownership percentages and the reporting currency are `[manual]`.** |
| ~~Trial balances by entity in local currency~~ | **Now [auto]** | `get_trial_balance` per `data_source_id`. |
| **Exchange rates** — spot, average, historical, **with source and dates** | **Required — [manual]**, always | **Never supply a rate from memory.** Ask for the table, its source and its dates. |
| **Functional currency assessment** — facts and conclusions | Recommended — **[manual]** | A judgment memo. **Ask whether it agrees with each file's home currency.** |
| **Intercompany balances** — AR / AP, loans, equity | Recommended — **[auto]** to read, **[manual]** to agree | Readable per entity; the mismatch is measurable. |
| **Which currency the group reports in** | **Required — [manual]** | Determines which entities need translation at all. |
| **Long-term investment designation** on intercompany loans | **Required if intercompany loans exist — [manual]** | Decides whether FX goes to earnings or to CTA. See Step 4. |
| **Is any entity in a hyperinflationary economy?** | **Required if applicable — [manual]** | Changes the method entirely. See the edge cases. |
| **Historical rates for equity and nonmonetary items** | **Required — [manual]** | The hardest data to obtain, and the most often approximated. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name` **with their home currencies**, and the reporting currency. |
| **Confirm any profile contradiction** | **Required if one appears** | Especially **home currency vs. asserted functional currency**. |
| **Confirm manual evidence** | **Required** | Every rate, the functional currency conclusions and the historical rates are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an exchange rate, a
functional currency, or a monetary / nonmonetary classification.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what changed.
The functional currency conclusions, the account classifications, the rate *source* and the entity map
persist; **the rates, the balances and the CTA are re-obtained every period**.
