<!-- related-party-disclosures-asc850 · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here, and it matters unusually much.** This skill compiles a document about **named individuals** — who they are, what they own, what they have transacted, on what terms. It is the most personally sensitive output in the pack. Producing it against the wrong entity does not just give a wrong answer; it assembles a dossier of one client's directors' business interests and hands it to a conversation about a different client.

**A privacy note that applies throughout this skill.** Compile only what the disclosure requires. Do not assemble a broader picture of an individual than the standard asks for, do not carry names between workspaces, and do not send any of it anywhere. The output is a working paper for a set of financial statements, not a background check.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every completeness procedure is `[manual]`. The skill still works as the original did. Say so — and say specifically that the vendor and customer match was not run, because that is the procedure a reader will assume happened. |
| **Exactly one company file** | Confirm the `display_name` before reading. |
| **Several company files** | **This is not merely a scoping question here — it is a source of related parties.** See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop; an incomplete match presented as complete is worse than no match. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

### The connected company files *are* related parties

`[auto]`, and it is the one part of Step 1 the workspace can genuinely populate.

If a workspace holds several company files, those entities are, in the ordinary case, **under common control** — that is generally why they are in one workspace. Step 1's first category therefore arrives partly pre-populated, without an interview:

- **The entities themselves** — each `display_name` is a candidate related party of every other.
- **Transactions between them** are readable **from both sides**, in one batched read, which is a stronger position than a related-party review usually enjoys. See `intercompany-reconciliation`.
- **A transaction recorded by one and not the other** is both a reconciliation difference and a disclosure risk: one entity is disclosing a related-party transaction that the counterparty's books do not show.

**Two cautions.** Being in one workspace is *evidence* of common control, not proof of it — a consultant may hold unrelated clients in one workspace, and the user should confirm rather than have it assumed. And **an entity under common control that is not connected to the workspace is invisible**, which is the ordinary case for a founder's other business. The connected set is a floor on the universe, never a ceiling.

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

**Batch independent reads.** The vendor master, the customer master, the chart of accounts, the loan and director's-account detail, and the transaction ledger are independent of one another. One message. Where several company files are in scope, read all of them together.

### The `mock: true` flag

Fixture data has **no related parties**, because nobody generated any. The vendor and customer masters contain invented names that match nothing, the match returns clean, and the clean result means nothing whatsoever.

This skill is unusually vulnerable to that, because **its headline output is a negative finding** — "we ran the completeness match and found nothing further." On fixture data that sentence is true and worthless, and it reads exactly like the valuable version. Label it in the file name and at the head of the completeness sheet.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

The related-party universe is expensive to assemble and stable between periods. **If the profile carries it, use it and say so — and then ask what has changed**, which is a much better question than asking for the whole list again. Step 5's control is precisely this: a periodic refresh, not a periodic rebuild.

Interview for:

1. **The org chart and ownership structure.** `[manual]`
2. **Key personnel** — officers, directors, significant shareholders. `[manual]`
3. **Close family members**, to the extent the framework requires. `[manual]`, and see the privacy note — collect the minimum the standard asks for.
4. **Which framework** — ASC 850 or IAS 24. They differ, notably on the scope of key management personnel and close family. `[manual]`
5. **What has changed since the last refresh**: board joiners and leavers, new subsidiaries, share transfers.

**Decisions are the user's; state is the workspace's.** The ledger says who was transacted with. Only the client says who is related.
