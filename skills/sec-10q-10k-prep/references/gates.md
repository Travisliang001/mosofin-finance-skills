<!-- sec-10q-10k-prep · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here more than anywhere in the pack.** The output of this process is **filed with a securities regulator and relied on by the public market.** Every other mis-scoped analysis produces an internal error someone can correct. A tie-out performed against the wrong entity supports a filing that is wrong in public, and the remedies for that — a non-reliance determination, an amended filing — are the most expensive corrections in this entire body of work.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The calendar, the checklists and the workflow all still work — they were always process artefacts. **No tie-out has a verified ledger side, the lock test does not run, and the comparatives are unchecked.** Say precisely that. |
| **Exactly one company file** | Confirm the `display_name`. **And confirm it is the registrant** — see below. |
| **Several company files** | **A 10-Q is consolidated. Reading several ledgers is not consolidating them.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. **Stop.** A partial tie-out on a filing is worse than none, because it will be ticked. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

### The registrant is a consolidated entity, and the gateway hands you components

**This is the single most important scoping point in the skill.**

The financial statements in a 10-Q or 10-K are those of the **registrant on a consolidated basis.** What `get_agent_datasources` returns is a set of **individual company files.** Between them sits a consolidation — eliminations, minority interests, purchase accounting, currency translation — and **none of it is in what comes back.**

So:

- **Where the consolidation is performed outside these books** — in a consolidation tool, or a spreadsheet — **the consolidated figures are `[manual]`**, and Mosofin's contribution is to the **components only.** Every tie-out then ties a component, which is useful and is not the filing.
- **Where the registrant's own file holds the consolidated result**, tie-outs work against it directly.

**Establish which, before ticking anything.** A tie-out sheet that says "agreed" against a subsidiary's trial balance, for a consolidated filing, is the kind of comfortable error that survives review. See `consolidation-and-eliminations`.

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

**A scope note.** If any tool that writes to the books appears in the listing, it is **out of scope for this skill regardless of its `effective_policy`.** Nothing in an SEC reporting process is posted by a machine.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** Trial balances at each relevant date, prior-period balances, transaction detail across the drafting window, and the chart are independent. One message.

### The `mock: true` flag

Fixture data **ties out perfectly and has never been posted into after a lock.** Every test in this skill — the tie-outs, the lock test, the comparatives check — passes by construction.

Given that this skill supports a regulatory filing, label it in the file name, on the calendar, and **at the head of the tie-out sheet.** A fixture-derived tie-out sheet must never be capable of being mistaken for a real one.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. SEC reporting is a fixed quarterly rhythm with a stable cast, so almost everything here should be known by the second run.

Interview for:

1. **Filer status** — large accelerated, accelerated, non-accelerated. `[manual]`. **It determines every deadline in Step 1 and it depends on public float, which is not in the books.** It is also re-tested annually and can change.
2. **The reporting calendar** — filing and earnings dates. `[manual]`
3. **Prior filings.** `[manual]` — documents.
4. **Significant events in the period** — M&A, debt, equity, impairments, restructurings. `[manual]` to identify; `[auto]` for some corroboration.
5. **The reviewer matrix** — accounting, FP&A, legal, IR. `[manual]`
6. **Whether XBRL applies** and who prepares it. `[manual]`. See `xbrl-tagging-checklist`.
7. **Non-GAAP measures used**, and their definitions. `[manual]` — **and persist them**, since consistency period to period is itself a requirement.

**Decisions are the user's; state is the workspace's.**
