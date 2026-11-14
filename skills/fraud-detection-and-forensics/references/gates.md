<!-- fraud-detection-and-forensics · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before analyzing anything. This ordering is the contract. Do not
skip a gate because a previous conversation covered it — connections, permissions, and company files
change between periods.

**And in this skill, run Step 1 — the engagement-type question — before Step 0's data pull.** If a specific
allegation exists, the correct first action is to involve counsel and preserve evidence, **not to start
querying**. Ask before you read.

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

**Confirm scope with particular care here.** Running fraud analytics against the wrong company file means
producing a list of suspicious-looking items about an organization nobody asked you to examine.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**An excluded entity matters differently here.** In most skills it is a gap in a workpaper. In fraud
analytics, **the entity you cannot see is exactly where a scheme would be safest** — say so plainly rather
than reporting clean results for the entities you could read.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`.
- **Multi-entity** — ask which set. **Cross-entity schemes are a real category** — a vendor paid by two
  group companies, an employee of one entity approving payments in another. See the cross-entity step.

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

**A gated tool deserves a moment's thought in this skill.** Approval prompts go to a person. **If that
person is within the scope of a concern, asking them for approval is a form of tipping off.** Where an
allegation exists, agree with the engagement owner *in advance* who approves data access.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **An indicator is not evidence, and evidence is not proof.** This is the whole discipline.
  - **A tool result is not a preserved record.** No chain of custody.
  - **Vendor and employee bank details are not on this surface** — so the strongest fictitious-vendor and
    ghost-employee tests **cannot be run here.** Say so; do not substitute a weaker test and imply it
    covered the same ground.
  - **Payroll register detail is not on this surface** — so tests depending on tax and benefit deductions
    are `[manual]`.
  - **A user name on a transaction is not the person who did it.** Shared logins are common.
- **There is no bank statement, no payroll register, no email, no document image and no external
  verification on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency, fiscal calendar, country / region,
industry.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| **Objective** — risk assessment / analytical detection / investigation support | **Required — [manual]** | **Ask first, before any data pull.** See Step 1. |
| ~~Data / records~~ | **Now largely [auto]** | Transactions, GL, vendor and employee masters. **Bank and payroll detail remain out of reach.** |
| **Area of concern**, if known | Recommended — **[manual]** | Focuses the tests; its absence widens them. |
| **Entity context** — industry, size, control environment | **Required — [gated]** | Size and industry are partly readable; **the control environment is not.** |
| **Specific allegations / indicators** | If applicable — **[manual]** | **If one exists, stop and escalate before analyzing.** |
| **Relevant policies** — authorization limits, procedures | Recommended — **[manual]** | **The authorization threshold is needed for the just-under-threshold test**; ask for it explicitly. |
| **Period** — date range | **Required** | |
| **Who is authorized to see the output**, and who approves data access | **Required — Mosofin addition** | Because the output names people, and approval prompts can tip off. |
| **Whether counsel is engaged** | **Required for investigation support** | The analysis may need to be directed by counsel under privilege. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm manual evidence** | **Required** | Policies, allegations and control context are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default an authorization
threshold, and **never** assume the objective is analytical detection when an allegation may exist.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
**Note the unusually strict persistence rule in Step 9: no findings, no names, no flagged items are ever
stored.**
