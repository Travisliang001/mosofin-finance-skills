<!-- revenue-recognition-asc606 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Revenue is the top line. A recognition analysis performed against the wrong entity produces the single most visible wrong number a set of accounts can contain — and it also contains named customers and their contract terms, which is commercially sensitive on its own.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Steps 1 to 4 are unaffected — they were always contract analysis. **Step 0's tests, the balance roll-forwards, and observable SSP do not run.** Say which. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | Ask which. **And note the contract-combination question below.** |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**Contract combination across entities.** Step 1 requires combining contracts entered into at or near the same time **with the same customer or its related parties** where they were negotiated as a package. Where several company files are connected, **the same customer may hold contracts with more than one of them** — and that is exactly the fact pattern the combination rule exists for.

`[auto]`: read the customer lists across connected files and surface customers appearing in more than one. `[manual]` to conclude, because whether contracts were negotiated as a package is not visible in either ledger. **A tool that combines automatically has decided a judgment; a tool that never looks has missed the fact pattern entirely.** Look, and ask.

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

**Batch independent reads.** The chart, the revenue accounts, the deferred revenue and contract asset accounts, the invoice detail, the customer list, the commission expense accounts and the sales-tax accounts are all independent. One message.

### The `mock: true` flag

Fixture data will show **deferred revenue that unwinds perfectly on a straight line** — because that is how it was generated. Every test in Step 0 asks whether the books are actually applying the standard, and generated books apply it flawlessly by construction.

Label it in the file name and on Sheet 1. A clean Step 0 on fixture data is not reassurance; it is the absence of a test.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. Revenue policy is stable and the interview is long, so this matters.

Interview for:

1. **The framework** — ASC 606 or IFRS 15. `[manual]`
2. **The contract itself**, or a summary of its key terms. `[manual]` — **this is the primary input and there is no substitute for it.**
3. **Standalone selling prices**, with sources. `[manual]` where estimated; **`[auto]` where observable** — see Step 4.
4. **Practical expedients elected** — the portfolio approach, the right-to-invoice expedient, the one-year commission expedient, the significant-financing expedient. `[manual]`, and **these are policy elections that must be applied consistently**, so they belong in the profile after the first run.
5. **Existing recognised revenue**, where mid-contract. **`[auto]` from the ledger — but read the caution in Step 5**: what has been recognised is not necessarily what should have been.

**Decisions are the user's; state is the workspace's.** The ledger says what was invoiced. Only the contract says what was promised.
