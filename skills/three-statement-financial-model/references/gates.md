<!-- three-statement-financial-model · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace before anything else
  - Gate 1 — Establish the datasource and entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Map what you can actually do
  - Gate 3 — Read the profile, then interview for what remains

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.


## Gate 0 — Confirm the workspace before anything else

1. Call `list_workspaces` with no arguments.
2. If the status is `confirmed`, there is one workspace. **Read its name back and wait for an explicit yes.**
3. If the status is `selection_required`, ask: **"Is this a single-workspace task or a multi-workspace one?"**
   - Single: ask which one by name, then `list_workspaces(workspace_ids=[<ws_...>], mode="single")`.
   - Multi: ask which ones, then `list_workspaces(workspace_ids=[<ws_...>, ...], mode="multi")`.

Refer to a workspace by **name**, or by the opaque `ws_...` handle. Never print the internal numeric id, never ask for it, and if it appears in an error, name the workspace instead.

**Why this gate matters here.** A three-statement model is frequently built **for fundraising or a transaction** — it goes to investors, lenders and diligence teams. A model whose historical base came from the wrong entity is a document that misrepresents a business to people relying on it.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The model can still be built — it always could. **The historical base and every measured driver become `[manual]`.** Say so; it materially weakens the assumptions. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **A consolidated model is not a summed model.** See below and the edge case. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **A wrong opening balance sheet propagates through every forecast period**, so stop rather than proceed on partial data. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On multi-entity models.** The edge case says it: **build entity-level models, then consolidate, keeping eliminations explicit.** Reading three ledgers gives three sets of statements; **it does not give a consolidated base**, because there are no eliminations in what comes back. Intercompany revenue and cost double-count, intercompany balances gross up the balance sheet, **and in a model that error propagates forward across the whole horizon and compounds.**

---

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Map what you can actually do


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


Call `get_datasource_tools` for the chosen company file and read the **`effective_policy`** on each tool.

| `effective_policy` | Verdict | Behaviour |
|---|---|---|
| `enabled` | `[auto]` | Call it. Batch with other independent reads. |
| `permission` | `[gated]` | Expect `approval_required`. Explain what and why, get a yes, re-invoke with `approved=true`. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | `[manual]` | Not available. The step remains; the user performs it. |

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run. Do not carry a capability map between runs.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The historical income statements, balance sheets, receivables, payables, inventory, fixed assets, debt and equity accounts are independent. **Read the longest available history in one go** — the measured drivers need it, and a one-year base gives a range of one.

### The `mock: true` flag

Fixture data produces **a smooth historical base with stable working capital days and no volatility.** So every measured driver comes back tidy, the ranges are narrow, and the model inherits a history that never happened.

**A model built on a fixture base is a template, not a model.** Label it in the file name, on the cover tab, and on the assumptions tab beside every measured driver.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

**Do the historical read before the interview**, because it changes what needs asking: with the measured drivers in hand, the conversation becomes *"your DSO has run between 38 and 52 days over three years, averaging 44 — what should the model assume?"* rather than *"what DSO should we use?"*

Interview for:

1. **The forecast horizon and granularity.** `[manual]`
2. **Operating drivers** — revenue build, margin, opex. `[manual]` to set, **`[auto]` to evidence.**
3. **The capex plan.** `[manual]` — a plan is not in the ledger.
4. **New borrowings, repayment schedules and rates.** `[manual]` — **in the loan agreements.**
5. **Planned equity transactions.** `[manual]`
6. **The tax approach** — effective rate or detailed. `[manual]`
7. **The circularity approach.** `[manual]` — see Step 6.
8. **What the model is for** — fundraising, diligence, internal planning. `[manual]`, and it sets the rigour bar.

**Decisions are the user's; state is the workspace's.**
