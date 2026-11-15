<!-- notes-to-financial-statements · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before drafting anything. This ordering is the contract. Do not
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

**These notes will be published.** Confirm scope with that in mind.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Settle the entity scenario, which for notes is **the reporting entity question**:

- **Single-entity** — the notes accompany that entity's statements.
- **Multi-entity** — **the notes almost always accompany consolidated statements**, so the disclosures must
  be consolidated too. **A related-party note built from one entity's records will miss the group's
  intercompany relationships entirely.** See the cross-entity step.

**The connected list is also the starting point for the related-party note** — see Step 5.

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

Resolve **every note in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **A balance is not a policy**, and **a pattern is not a policy either** — it is a basis for a question.
  - **A transaction after year-end is not a subsequent event** until someone judges it material and
    classifies it. **It is a candidate.**
  - **A vendor sharing a name with a director is not a related party transaction** — it is a match to
    investigate.
  - **The ledger's prior year is not the published prior year.** Comparative notes must agree to what was
    filed; see `financial-statement-builder`.
  - **A roll-forward built from the ledger is not the disclosed roll-forward** until it ties to the
    statement face.
- **There is no policy manual, no legal file, no contract and no valuation on this surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: **legal name — as it appears in the notes** — **functional and
presentation currency**, **fiscal calendar and year-end**, country / region, industry.

**Ask the user** what actually changes the work — the original Inputs table, **minus the parts the connected
books now answer**:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Financial statements~~ | **Now [auto]** | From `financial-statement-builder` or read directly. |
| **Reporting framework** | **Required — [manual]** | **Decides the entire checklist.** |
| ~~Entity profile~~ — public/private, industry, size, jurisdiction | **Now largely [auto]** | **Public or private is `[manual]`**, and it changes the disclosure volume enormously. |
| **Supporting schedules** — debt, lease, FA register | **Required for detail notes — [gated]** | **Balances `[auto]`; the schedules `[manual]`** — see the linked skills. |
| **Accounting policies in use** | **Required — [manual]** | **Not in the data.** Inferable in places, confirmable always. |
| **Significant judgments and estimates** | **Required — [gated]** | **Scopeable from the balance sheet**; the judgment is `[manual]`. |
| **Related party information** | Recommended — **[gated]** | **Name matching is `[auto]`; the relationships are `[manual]`.** |
| **Commitments and contingencies** | Recommended — **[manual]** | **Legal review territory.** |
| **Subsequent events** | Recommended — **[gated]** | **Candidates `[auto]`; the assessment `[manual]`.** |
| **Prior year notes** | Recommended — **[manual]** | For consistency, and to check comparatives against what was filed. |
| **The issuance date** | **Required — Mosofin addition** | **Defines the subsequent events window.** Without it, the candidate population has no end. |
| **Who performs legal review** | **Required if contingencies exist — Mosofin addition** | |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and whether consolidated. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Policies, contingencies and legal positions are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a policy, a
contingency assessment, or a materiality judgment on a subsequent event.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only what changed.
The checklist, the policy statements, the note structure and the tie-out map persist; **every figure is
recomputed and every note redrafted.**
