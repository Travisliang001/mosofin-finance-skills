<!-- contingencies-and-litigation-asc450 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before assessing anything. This ordering is the contract. Do not
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

Confirming carefully matters here for an unusual reason: **litigation information is sensitive and
often privileged.** Reading one entity's legal spend while believing you are in another's is a
confidentiality problem, not just a data error.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The completeness sweep runs **once per entity**, every call
  targeting exactly one `data_source_id`, and every matter carries the entity it sits in. **A
  contingency attaches to a specific legal entity** — that is the whole point of separate legal
  entities — so **never present a group contingency without saying which entity bears it**. See the
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
- **A near-substitute is not a substitute, and here the substitution would be a genuine harm.** **Legal
  spend is not a probability assessment.** A large bill from a litigation firm tells you a matter
  exists; it tells you nothing about whether the entity will lose or how much. **Never infer a
  probability, a range, or an outcome from the fee pattern.** Use it for completeness only.
- **The vendor and ledger tools carry the completeness signal.** If they are disabled, the
  completeness sweep cannot be performed — say so, rather than reporting a clean sweep that never ran.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name — which is the name that appears in
proceedings — base currency, fiscal calendar, country / region, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Contingency list** — matter name, type, status, counsel | **Required — [manual]** | Not in the ledger. This is the population; the completeness sweep tests it, it does not replace it. |
| **Management assessment** — probability and estimate / range | **Required — [manual]**, always | **Mosofin will not supply this.** Ask per matter, and record who gave it and when. |
| **Legal letters** — outside counsel responses | Recommended — **[manual]** | Often the only defensible support for the assessment. |
| **Prior period disclosures** — prior footnotes and accruals | Recommended — **[gated]** | Prior *accruals* are readable from the ledger; **prior footnote language is [manual]**. |
| **Insurance coverage** — policies, deductibles, limits | Recommended — **[manual]** | Recoveries *received* are readable; the policy terms are not. |
| **Reporting framework** — US GAAP or IFRS | **Required** | **[manual]**, and it matters more here than the original's US-GAAP framing implies — see the edge case on IAS 37 thresholds. |
| **Which vendors are law firms / legal counsel** | **Required for the completeness sweep** | Ask the user to identify them, or confirm the ones the spend pattern suggests. |
| **Reporting period** | **Required** | Never default it. |
| **Whether any matter is privileged or restricted** | **Required** | Some matters must not be written into a shared workpaper. Ask before producing one. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Every probability and every estimate is `[manual]`. Record which matters have a current counsel assessment and which do not. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a probability, an
estimate, a range, or the framework.

**On later runs**, read stored preferences first (Step 6), confirm in one line, and ask only what
changed. The counsel vendor list and the matter register persist; **every probability and estimate must
be re-confirmed each period** — a stale assessment is the classic contingency failure.
