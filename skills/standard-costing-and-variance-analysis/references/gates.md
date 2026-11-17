<!-- standard-costing-and-variance-analysis · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Standards are plant- and product-specific. A variance computed against another entity's actual costs is a comparison between one factory's standards and another factory's spending, which will produce large, confident, meaningless numbers.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Both halves are `[manual]`. The framework applies in full. Say what was not measured. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Ask which — and note that plants are frequently separate entities.** Variances are computed per plant. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — a partial actual understates a variance in an unpredictable direction. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On multi-plant groups.** The original's own output calls for a variance report **by product, line and plant.** Where plants sit in separate company files, **compute and report each separately** — standards differ by plant, and so do the operational explanations. A group-level PPV is an average that describes no factory.

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

**One capability question decides half this skill: does the surface expose quantities?**

Per the third near-substitute: price and spending variances need values; **usage, efficiency and volume variances need units.** Read the returned schemas and establish whether purchase and production transactions carry quantity as well as value. **Do not assume either way** — it varies by connector, and it frequently varies by transaction type within one connector.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The chart, the variance account history, purchase transactions by item and vendor, labour and overhead accounts, and inventory movements are independent. **Read a long history** — the stale-standard test needs it.

### The `mock: true` flag

Fixture data has **variances that behave**: small, two-sided, and cleared to COGS on schedule. So the stale-standard test finds nothing and the uncleared-variance test finds nothing.

Both of those are the tests that matter. Label it in the file name and on the variance report.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The BOM and routings.** `[manual]` — **not in the books.**
2. **Standard rates** — material prices, labour rates, overhead rates — **with their effective dates.** `[manual]`, and **the dates are as important as the rates**, per Step 0.
3. **Production volumes, runs and scrap.** `[manual]` unless the system holds units.
4. **The inventory valuation policy** — standard versus actual, and the **variance capitalisation policy.** `[manual]`, and it governs Step 5.
5. **Which overhead rates are fixed and which variable**, and the basis of absorption. `[manual]`

**Decisions are the user's; state is the workspace's.** The ledger says what was spent. Only the standard says what should have been.
