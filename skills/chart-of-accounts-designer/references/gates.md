<!-- chart-of-accounts-designer · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before designing anything. This ordering is the contract. Do
not skip a gate because a previous conversation covered it — connections, permissions, and company
files change between periods.

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

**Ask the defining question for this skill: are you designing for one entity, or harmonising across
several?**

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`. The output is one COA.
- **Multi-entity harmonisation** — ask which set. **Read each entity's chart of accounts separately**,
  every call targeting exactly one `data_source_id`, then compare them. This is a genuinely
  well-supported use case: the differences between three sibling charts are directly visible, and
  they are usually the reason group reporting is painful. See the cross-entity step.

Also establish, and it is easy to miss: **is the target system the same as the connected one?** A
migration to a different platform means the source is `[auto]` and the target's taxonomy is
`[manual]` — the account types and detail types will not map one-to-one.

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
built this run, held for this run, written out as the coverage sheet, **never** written into this
file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled —
  some underscored, some hyphenated.
- **Two tools matter most, and they do different jobs.** The **account search** gives you the chart;
  the **general ledger** gives you the *usage*. Without the second, you can restructure a COA but you
  cannot evidence which accounts are dead — and the retire list becomes an assertion. If the ledger
  tool is disabled, say the cleanup recommendations are unevidenced.
- **A near-substitute is not a substitute.** An account's **balance** is not its **usage**. A dormant
  account can carry a large balance, and a heavily-used clearing account can sit at nil. Judging
  activity from a trial balance gets both cases exactly backwards. Use transaction counts and last
  activity dates, not balances.
- **Check whether the account list includes inactive accounts.** The noise you are hunting is often
  already deactivated but still cluttering reports and import files — search with inactive included.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope
entity.

**Derive silently** what the profile answers:

- **Industry** — which drives Step 3 entirely. This is the most valuable profile field in this skill
- **Functional currency**
- Legal name, fiscal calendar, country / region — which hints at, but does not decide, the tax
  structure

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Entity industry** | **Required — usually [auto]** | Derived from the profile; **confirm it**, since the registered industry is often stale or generic. Step 3 depends on it. |
| **Entity size / stage** — startup / SMB / mid-market / enterprise | **Required — [gated]** | Transaction volumes and account counts are readable and indicate scale; the strategic stage is **[manual]**. |
| **Reporting framework** — US GAAP / IFRS / Local GAAP / Other | **Required — [manual]** | Never infer from country. |
| **Functional currency** | **Required — usually [auto]** | Derived; confirm only on a contradiction. |
| **Accounting system (target)** | **Required — [manual]** | **Ask explicitly whether it is the connected system or a different one.** It changes the whole of Sheet 2. |
| **Existing COA (if migrating)** | Required for restructuring — **usually [auto]** | Read from the connected system. Ask only for a chart that lives elsewhere. |
| **Reporting dimensions used** — class / department / location / project / custom | Recommended — usually **[auto]** | The dimensions actually in use are readable, which is better evidence than what people say they use. |
| **Multi-entity / consolidation needs** | Recommended — partly **[auto]** | The connected set gives a first draft; confirm the legal structure. |
| **Tax jurisdictions** | Recommended — partly **[auto]** | Tax codes, rates and agencies in use are readable and reveal the jurisdictions actually transacted in. Confirm the list. |
| **Specific reporting needs** — investor reporting, lender covenants, board reports, segment reporting | Optional — **[manual]** | These drive account granularity more than anything else; ask. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether this is one COA or a harmonisation. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required if Gate 2 produced any [manual]** | |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the framework,
the target system, or the industry-specific account set.

**On later runs**, read stored preferences first (Step 7), confirm in one line, and ask only what is
new. The numbering scheme, the dimension strategy and the account descriptions should not be
rebuilt; **usage is always re-measured**.
