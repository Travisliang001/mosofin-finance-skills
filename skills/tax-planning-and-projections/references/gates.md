<!-- tax-planning-and-projections · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** Tax attaches to a **specific taxpayer**. A projection built on the wrong entity's results produces a liability figure for a person or company that does not owe it — and, worse, a set-aside plan that leaves the real taxpayer short.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The base, the payments and the cash position are all `[manual]`. The framework applies in full. Say so. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Ask which entity is the taxpayer** — and see the owner-managed note below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — **an understated base produces an understated set-aside, and the consequence is a missed payment.** |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On owner-managed businesses**, which is the case this skill most often serves.

Lever 5 in Step 5 — **salary versus dividend versus retained profit** — spans **two taxpayers**: the company and the owner. The company's results are in the workspace; **the owner's personal position generally is not.** So:

- `[auto]` for the corporate side
- **`[manual]` for the personal side** — other income, filing status, allowances already used, residence
- **`[manual]` for the combined analysis**, which is the only analysis that answers the question

**Modelling the corporate layer alone and presenting it as an extraction conclusion is the characteristic error here**, and it reliably points the wrong way, because the combined burden is what the owner actually pays. See `personal-tax-return-prep`, which makes the same point from the other side: the workspace holds business books, not a person's tax position.

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

**Batch independent reads.** Year-to-date results by account, the tax payable and tax expense accounts, the cash and reserve accounts, the prior year's tax charge, and payment history are independent. One message.

### The `mock: true` flag

Fixture data has **a plausible profit, a tax account that behaves, and cash that covers everything.** So the base is fictitious, the payments-made check passes, and the affordability test passes.

**The affordability test is the one that matters most to a real client**, and fixture data guarantees it. Label it in the file name and on the projection summary.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything. Tax planning recurs annually with a stable structure.

Interview for:

1. **Taxpayer type and jurisdiction.** `[manual]`
2. **Current rates, brackets, allowances and rules.** `[manual]`, **current-sourced, never carried forward.**
3. **The forward half of the income projection.** `[manual]` — see Step 1.
4. **The book-to-tax adjustments** expected for the year. `[manual]`
5. **Personal circumstances**, for an individual or an owner-manager. `[manual]`
6. **Decisions under consideration.** `[manual]`
7. **The jurisdiction's safe-harbour rule** for estimates. `[manual]`

**Decisions are the user's; state is the workspace's.** And here, more than anywhere: **the decision is also the professional's.**
