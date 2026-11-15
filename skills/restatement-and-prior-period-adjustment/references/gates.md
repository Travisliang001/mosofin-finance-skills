<!-- restatement-and-prior-period-adjustment · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here more than almost anywhere.** A restatement is a public act with legal weight. For a listed company it means a non-reliance determination, amended filings and likely a material weakness. **Analysis performed against the wrong entity, in a matter this consequential, is not a correctable slip.** One question, before the first read.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Quantification, benchmarks and the prior-period sweep are all `[manual]`. The framework in this skill still applies in full — it is a judgment framework, and judgment does not need a connector. Say what was not verified. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | Ask which. **And ask whether the restatement is at entity or group level** — see below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop. A partial quantification understates an error, and understating an error is how a Big R gets mistaken for an out-of-period adjustment. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**Entity versus group, which changes the materiality answer.** An error can be material to a subsidiary's own accounts and immaterial to the group's, or the reverse. Both sets of statements may have been issued. **Materiality is assessed against the statements that were issued**, so establish which statements are in scope before computing a single benchmark — the denominators differ and so does the conclusion. See `consolidation-and-eliminations`.

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

**A scope note.** If a tool that posts or amends transactions appears in the listing, it is **out of scope for this skill regardless of its `effective_policy`.** Nothing in a restatement is posted by a machine. The correction entries here go to a human, then to an auditor, then to a board.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** Trial balances at each affected period end, transaction detail across the affected periods, the current-period position, and the chart are independent. One message.

### The `mock: true` flag

Fixture data has **no history of anyone posting into a closed period**, because nobody did. The prior-period sweep — the strongest detection in this skill — returns clean by construction, and a clean sweep is precisely the result that would otherwise be reassuring.

Label it in the file name and at the head of Sheet 1. And note the sharper problem: **fixture data will also produce a restated balance sheet that balances perfectly**, which proves nothing at all (see Step 5).

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The description of the error and how it was discovered.** `[manual]` — and "how it was discovered" is not incidental; it feeds the root-cause work in Step 7 and often the fraud question.
2. **The previously-issued financial statements** for each affected period. `[manual]`, **from the documents**, not from the ledger. See the opening section.
3. **The framework** — ASC 250 or IAS 8.
4. **Public or private**, which determines whether Step 4's regulatory consequences apply at all.
5. **What was known at the time.** This is the pivot of Step 1 and it is a question about knowledge, not about numbers.
6. **Materiality benchmarks and thresholds** the entity and its auditors use.

**Decisions are the user's; state is the workspace's.** And in this skill the decisions are not only the user's — several of them belong to the auditors and the board.
