<!-- quickbooks-ar-aging-collections · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace before anything else
  - Gate 1 — Establish the datasource and entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Map what you can actually do
  - Gate 3 — Read the profile, then interview for what remains
  - Safety and operating boundaries

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.


## Gate 0 — Confirm the workspace before anything else

Before the company-information call, before any report, before anything.

1. Call `list_workspaces` with no arguments.
2. If the status is `confirmed`, there is one workspace. **Read its name back and wait for an explicit yes.**
3. If the status is `selection_required`, ask in chat: **"Is this a single-workspace task or a multi-workspace one?"**
   - Single: ask which one by name, then `list_workspaces(workspace_ids=[<ws_...>], mode="single")`.
   - Multi: ask which ones, then `list_workspaces(workspace_ids=[<ws_...>, ...], mode="multi")`.

Refer to a workspace by **name**, or by the opaque `ws_...` handle where a machine reference is unavoidable. Never print the internal numeric id, never ask for it, and if it surfaces inside an error message, name the workspace instead.

**Why a collections skill needs this gate more than most.** The output of this skill is a list of named customers, their balances, and how overdue they are — and then draft letters addressed to them. It is customer-identifying commercial data. Producing it against the wrong entity is not a reconciliation error; it is showing one client another client's debtors. One question prevents it.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Every read below is unavailable. Fall back to the original's export path — ask for an A/R Aging Detail with customer, invoice number, invoice date, due date and open balance — and label the entire output as user-supplied. |
| **Exactly one QuickBooks company file** | The original's assumed case. Confirm the `display_name` before reading. |
| **Several company files** | Ask which, **by `display_name`**. "All of them" means several agings, each labelled, **never merged into one total.** |
| **A connected file that is not QuickBooks** | This skill is written against the QuickBooks surface. Another accounting system may expose an equivalent aging; check `get_datasource_tools` and, if the shape differs materially, use `ar-aging-and-collections` rather than forcing this one. |
| **Connected but stale or broken** | A `reconnect_url` in a response means the connection needs the user's attention. Stop and say so. Do not present a partial aging as a complete one — in collections, a missing invoice is a customer nobody chases. |

Refer to company files by `display_name` throughout. Pass `data_source_id` between tools; never display it.

**On multiple entities.** A group with three trading companies often has customers who buy from two of them. The same customer name will appear in two agings with two balances, and those balances are **not** additive from the customer's point of view unless the entities invoice as one. Do not combine them into a single "total exposure" figure without saying exactly what you have done and on whose authority. If a genuine group exposure view is wanted, that is a consolidation question — see `consolidation-and-intercompany-eliminations`.

---

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Map what you can actually do


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


Call `get_datasource_tools` for the chosen company file. **Read the `effective_policy` on each returned tool.** That field, and not this document, not the bundled reference, and not memory, decides what is possible today.

| `effective_policy` | Verdict | Behaviour |
|---|---|---|
| `enabled` | `[auto]` | Call it. Batch it with other independent reads. |
| `permission` | `[gated]` | The call raises `approval_required`. Explain what you want and why, get a yes, re-invoke with `approved=true`. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | `[manual]` | Not available. The step remains; the user supplies the data by export. |

The original's advice — *"Match tools by capability and description, not by generated hash, because installed MCP names can change"* — was directionally right and is now made exact: **match on what `get_datasource_tools` returns, every run.** Do not type a tool name from memory and do not infer one from a report title. An `UNKNOWN_TOOL` envelope means the name is wrong; re-read the list rather than trying a near-miss.

**Every call is stateless.** Carry `data_source_id` on each `invoke_datasource_api_tool` call, including the retry after an approval. Dropping it on the retry is the commonest way an approved call still fails.

**Batch independent reads.** The company information, the A/R Aging Detail and the A/R Aging Summary do not depend on one another. Issue them in one message. Three serial round trips to build one aging is three times the wait for no gain.

### Re-derive the basis constraint rather than asserting it

The original states flatly that the aging capability is accrual-basis only. Treat that as a **hypothesis to check at Gate 2**, not a fact to repeat:

- Read the aging tools' parameters as returned. If a basis parameter exists, the constraint has changed and the original text is stale.
- If no basis parameter exists, the constraint holds **for this connector today**, and the original's handling is correct: **if the user explicitly asks for a cash-basis A/R aging, do not call the aging tools.** Explain that this connector cannot provide it and ask whether accrual basis is acceptable.

Record what you found in the coverage sheet. That is how the next run gets a better answer than this one.

**Why this matters beyond pedantry:** a cash-basis A/R aging is very close to a contradiction — under a strict cash basis there are no receivables — but QuickBooks will produce something under that label, and what it produces is not what an accrual aging means. Silently serving an accrual aging to someone who asked for cash basis, or vice versa, produces a number nobody can reconcile to anything.

### The `mock: true` flag

If a response carries `mock: true`, it is **fixture data**, not the client's books.

The consequence here is unusually concrete: **the customer names are not real customers.** Everything downstream — the priority queue, the concentration analysis, the draft letters — is addressed to invented people. A draft reminder generated from fixture data must never be handed to anyone as ready to review, because reviewing it will not reveal that the recipient does not exist. Label it in the file name, on the provenance sheet, and on every draft.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` **before asking the user anything.**

This gate matters more in this skill than in any other in the pack, because the original's interview list is long and every item on it is stable:

- dispute status and credit holds
- strategic customer tier
- brand voice and approved reminder wording
- late-fee rules and escalation policy
- credit sales figure and measurement period for DSO
- payment terms where they are needed for a draft

**None of these change between runs.** If the workspace profile carries them, use them and say you are using them. Asking a credit controller for their escalation policy every Monday is how a tool gets abandoned by the person it was built for.

**Decisions are the user's; state is the workspace's.** The ledger says who owes what. Only the user says who gets chased hard.

---

## Safety and operating boundaries

All seven of the original's boundaries are preserved, unweakened, with the gateway's own guarantees noted alongside.

- **Treat every QuickBooks operation in this workflow as read-only.** Under Mosofin this is not merely a rule the skill follows — **the gateway is read-only.** There is no write path. That is a stronger guarantee than a policy, and it should be stated to the user as such when they ask whether this is safe to run.
- **Never create or update customers, invoices, terms, reminders, or settings.**
- **Never call a send-reminder, email, payment, write-off, or other mutation tool.** If such a tool appears in `get_datasource_tools`, it is out of scope for this skill regardless of its `effective_policy`.
- **Produce correspondence as drafts only, and say that it has not been sent.**
- **Never invent late fees, service suspension, legal escalation, or payment promises.** A drafted threat that the client's policy does not authorise is a commercial and possibly legal problem, and it is the single worst thing this skill could produce.
- **If the user asks to send a reminder, finish the analysis and explain that sending requires a separate confirmation-controlled workflow outside this skill.** Do not offer to do it another way.
- **The basis constraint** — see Gate 2, where it is re-derived rather than assumed.

**One Mosofin addition:** the output of this skill is customer-identifying data about a third party. Keep it inside the deliverable. Do not send it anywhere, do not put customer names or balances into a URL or a query string, and do not carry customer lists between workspaces.
