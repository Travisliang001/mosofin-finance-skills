<!-- working-capital-optimization · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** The output names customers who pay slowly and suppliers whose terms could be renegotiated. **It is commercially sensitive about third parties**, and it recommends actions that affect real relationships.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The whole diagnostic becomes `[manual]` from exports. **The skill still works and loses most of its advantage.** Say so. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Working capital is managed where the cash is.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — **a short history destroys the seasonality analysis**, which is the thing that stops period-end snapshots misleading. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On group working capital.** Intercompany receivables and payables inflate both sides and **are not working capital in any meaningful sense** — the group does not fund itself. **Compute per entity on third-party balances, and eliminate intercompany before any group view.** See `intercompany-reconciliation`; the eliminations themselves are consolidation work.

**And note a real trap**: a shared services entity that pays on behalf of the group will show enormous DPO and negligible DSO, which is an artefact of the structure rather than a working capital achievement. **Read the structure before reading the ratios.**

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

**One capability question shapes Step 3 entirely: does the surface expose inventory at item level, with quantities and movement dates?** Many accounting systems hold inventory only as a value; **SKU-level turns, ABC analysis and slow-mover identification need item detail**, which often lives in a warehouse or inventory system instead. **Check, and say which.**

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** **Read the longest available monthly history in one go**, plus invoice-level detail with issue and payment dates, bill-level detail with terms and payment dates, and the item ledger if exposed. Fetching a year at a time defeats the seasonality work.

### The `mock: true` flag

Fixture data is **smooth**: stable days, no seasonality, no slow payers, no early payments, no window dressing. **Every diagnostic in this skill measures variation, and generated data has none.**

Label it in the file name and on the executive summary. **The opportunity figures will be small and meaningless**, which is a less obvious failure than a large meaningless one.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. **Do the diagnostic read first** — it makes the interview far better, because the conversation becomes *"your DSO is 52 days, of which 9 are invoicing delay"* rather than *"how are collections?"*

Interview for:

1. **Customer payment terms** — standard and exceptions. `[manual]`; **`[auto]` to compare against actual behaviour.**
2. **Supplier payment terms** — standard and exceptions. Same.
3. **Industry benchmarks.** `[manual]` — **external data, not on this surface.**
4. **Cost of capital**, for valuing the unlock. `[manual]`.
5. **Service-level commitments and guardrails.** `[manual]` — Step 7.
6. **Which relationships are strategically untouchable.** `[manual]`, **and ask before recommending anything about a supplier.**

**Decisions are the user's; state is the workspace's.**
