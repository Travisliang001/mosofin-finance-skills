<!-- vendor-onboarding-and-w9-tin · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** The output contains **vendor bank details and tax identifiers**. Producing it in the context of the wrong client is a data incident, not a reconciliation error.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Onboarding works exactly as the original describes, from uploads. **The master audit, the duplicate check and the bank-change detection do not run.** Say so. |
| **Exactly one company file** | Confirm the `display_name`. |
| **Several company files** | **Groups frequently share suppliers and keep separate vendor masters.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — **a partial master produces a clean duplicate check.** |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On shared suppliers across a group.** Where several entities are connected, **the same supplier commonly exists in several vendor masters with different records** — different tax IDs captured, different bank details, one with a form on file and one without.

`[auto]` to match across masters, and it produces two useful things: **a group-level view of the supplier**, and **inconsistencies between the records** that suggest which one is out of date. **A bank detail present in one entity's master and different in another's is worth resolving before either pays.**

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

**Two capability questions matter here, and vendor banking data is commonly restricted:**

1. **Does the surface expose vendor bank details at all?** Frequently it does not, or only partially — and **that is a sensible restriction rather than a gap.** Where it does not, the duplicate check runs on name, tax ID and address, and the bank-change detection does not run.
2. **Does it expose master-data change history** — what changed, when, by whom? Step 0c depends entirely on it.

**Expect `permission` rather than `enabled` on vendor banking**, and when explaining the approval request, say specifically what is being read and why — the purpose is duplicate detection and change monitoring, not extraction.

**A scope note**: if a tool that creates or edits a vendor record appears in the listing, it is **out of scope regardless of `effective_policy`.** This skill produces a record for a human to enter.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The vendor master, payment history by vendor, master-data change history, the customer list and the chart are independent. **Read the whole master**, not a sample.

### The `mock: true` flag

Fixture data has **a clean vendor master with no duplicates, complete fields, and no bank-detail changes.** Every audit in Step 0 returns clean.

**And "no duplicates found" and "no bank changes detected" are this skill's headline outputs**, which makes fixture data uniquely misleading here. Label it in the file name and **at the head of the audit sheet**, not in a footnote.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **The payer's jurisdiction.** `[manual]` — it determines every validation rule.
2. **The entity's onboarding policy** — which documents are required, form expiry conventions, one-time-payee thresholds. `[manual]`, **and persist it**; Sheet 4 is built from it.
3. **The screening arrangements** — who runs sanctions and PEP checks, on what service. `[manual]`.
4. **Whether the accounting system records master-data changes**, and who has access to edit vendors.
5. **Withholding rules** applicable in the payer's jurisdiction. `[manual]`.

**Decisions are the user's; state is the workspace's.**
