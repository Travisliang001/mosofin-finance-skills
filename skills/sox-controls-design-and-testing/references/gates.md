<!-- sox-controls-design-and-testing · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** A control conclusion is an assertion about how a specific organisation operates, and a material weakness conclusion is a public disclosure with market consequences. It also **names individuals** — SoD analysis is inherently about who did what. Producing it against the wrong entity is both wrong and a confidentiality problem.

**A note on naming people.** SoD and approval testing identify individuals by name or user id. Keep that inside the deliverable, report by **role** wherever the analysis permits, and remember that a SoD conflict is a **finding about how access is configured**, not an allegation about a person. Nearly every conflict found is somebody doing their job in a small team.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every step is `[manual]`, which is how ICFR testing has always been done. The framework applies in full. **Say that no full-population testing was available.** |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Significant locations are a scoping decision (Step 1), and each connected file is a candidate.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — a full-population test run on partial data is a full-population claim on a partial population, which is worse than a sample. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On significant locations.** Step 1 requires scoping locations and units by materiality and risk. Where several company files are connected, **each is a candidate location, and controls may operate differently in each** — a small subsidiary frequently cannot segregate duties that the parent segregates comfortably. **Test each in scope separately and report separately.** A group-level SoD conclusion drawn from the parent's data says nothing about the subsidiary where one person does everything.

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

**One capability question decides a large part of this skill: does the surface expose user attribution?**

Whether a transaction record carries **who created it, who modified it, who approved it, and when** determines whether Step 4b's SoD testing and much of Step 6b's control testing are possible at all. **Read the returned tool schemas and check.** Do not assume attribution is available, and do not assume it is absent — it varies by connector and by what the underlying system records.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** Transaction detail with attribution, the chart, the vendor and customer masters, journal entries by source, and period activity are independent. **Read the full period, not a sample** — that is the point.

### The `mock: true` flag

Fixture data has **no SoD conflicts, no unapproved transactions, no exceptions left uninvestigated, and probably a single system user.** Every control test in this skill passes.

**For a control testing skill this is uniquely dangerous**, because the output is a set of "no exceptions noted" conclusions that look exactly like real ones and would, if relied on, support an ICFR assertion. Label it in the file name, on the test results sheet, and **on every individual test conclusion.**

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. ICFR is an annual cycle with a stable framework, so by the second year almost everything structural should be known.

Interview for:

1. **Processes in scope** and the scoping rationale. `[manual]`
2. **Process descriptions and walkthroughs.** `[manual]` — how the process **actually** works.
3. **The risk assessment.** `[manual]`
4. **Existing controls**, and where their evidence lives. `[manual]` — **and specifically, for each control, whether its operation leaves a trace in the accounting system.** That single question routes every control between `[auto]` and `[manual]` testing.
5. **Materiality and scoping thresholds.** `[manual]`
6. **Systems involved**, and the ITGC position. `[manual]`
7. **The testing objective** — design, operating effectiveness, or both. `[manual]`
8. **Prior deficiencies** for follow-up. `[manual]`

**Decisions are the user's; state is the workspace's.** The ledger says what happened. Only people can say whether the control that was supposed to prevent it operated.
