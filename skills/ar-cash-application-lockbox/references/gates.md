<!-- ar-cash-application-lockbox · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before matching anything. This ordering is the contract.
Do not skip a gate because a previous conversation covered it — connections, permissions, and
company files change between runs.

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
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

Two things to look for specifically here:

- **A connected payment processor or banking platform changes this skill materially.** It is
  the difference between reviewing recorded receipts and actually seeing the money arrive.
  Check every connected row, not just the accounting one.
- A workspace can connect the **same platform several times** — several company files, several
  processor accounts. Each is its own row with its own `data_source_id` and `display_name`.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting
  exactly one `data_source_id`, and every receipt, match and unapplied item carries its
  entity's `display_name`. **Never apply one entity's receipt to another entity's invoice** —
  that is not a match, it is an intercompany transaction in disguise.

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
map** — built this run, held for this run, written out as the coverage sheet, **never** written
into this file.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly
  styled — some underscored, some hyphenated.
- **A near-substitute is not a substitute.** A **customer balance** report tells you what a
  customer owes in total; it cannot tell you *which invoice* a payment settled, so it cannot
  drive cash application. Likewise a **deposit** record in the books is not a **bank
  statement**: it shows what someone entered, not what the bank actually received. Where the
  invoice- or payment-level tool is disabled, mark the task `[manual]` and ask for an export.
- **The customer-payment search and the deposit search answer different questions.** Payments
  are what was received against invoices; deposits are how those receipts were banked, often in
  batches. You need both for Step 5, and confusing them produces a tie-out that ties to itself.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`).

**Derive silently** what the profile answers: base currency, fiscal calendar, country / region,
time zone. The time zone matters here — a receipt's "day" for a daily tie-out depends on it.

**Ask the user** what actually changes the work — the original Inputs table, minus what the
profile answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Bank deposit data** — lockbox / ACH / wire report | **Required — usually [manual]** | Ask for the file, or confirm a banking datasource is connected. Without it, the Step 5 tie-out cannot be done and must be reported as not done. |
| **Open A/R invoices** | **Required — usually [auto]** | Normally pulled from the connected books. |
| **Remittance advice** — email / EDI / PDF | Recommended — **[manual]** | The single biggest driver of match quality. Ask whether remittances exist and where. |
| **Customer master** — mapping of payer identifiers | Recommended — partly **[auto]** | Customer records pull; the **payer-alias map** (the name the bank shows versus the customer in the books) is usually **[manual]** and is worth storing at Step 6. |
| **Deduction policy** — allowable write-offs and approvals | Recommended — **[manual]** | Sets the threshold below which a short-pay is written off rather than chased. Never invent one. |
| **Period / date range in scope** | **Required** | Never default the period. |
| **Unapplied cash account** | **Required if used** | Confirm which account holds unapplied cash, by its real name. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required if Gate 2 produced any [manual]** | For each gap — bank data and remittances will be among them — ask whether the user can supply it, and how. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default the
period, the deduction threshold, or the entity.

**On later runs**, read stored preferences first (Step 6), confirm in one line, and ask only
what is new, changed, or contradicted. The payer-alias map and the deduction policy in
particular should not be re-asked every day.
