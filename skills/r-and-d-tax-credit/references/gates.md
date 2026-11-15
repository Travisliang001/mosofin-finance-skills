<!-- r-and-d-tax-credit · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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
3. If the status is `selection_required`, ask in chat: **"Is this a single-workspace task or a multi-workspace one?"**
   - Single: ask which one by name, then `list_workspaces(workspace_ids=[<ws_...>], mode="single")`.
   - Multi: ask which ones, then `list_workspaces(workspace_ids=[<ws_...>, ...], mode="multi")`.

Refer to a workspace by **name**, or by the opaque `ws_...` handle. Never print the internal numeric id, never ask for it, and if it appears in an error, name the workspace instead.

**Why this gate matters here.** An R&D claim is a filing to a tax authority with penalty exposure attached. Group structures are common in R&D-intensive businesses — a trading company, an IP-holding company, a development company — and **which entity incurred the cost determines which entity may claim it**, under rules that are intricate and unforgiving. Reading costs from the wrong company file does not produce a slightly wrong claim; it produces a claim by an entity that did not incur the expenditure. Confirm first.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | The cost population is `[manual]` and must be supplied. The technical assessment was `[manual]` anyway, so the whole skill runs as the original did. Say so plainly. |
| **Exactly one company file** | The straightforward case. Confirm the `display_name`. |
| **Several company files** | Ask which, **by `display_name`** — and ask which entity is making the claim, which may not be the same one. See below. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop. An incomplete cost population understates a claim, which costs the client money and is not discovered by anything downstream. |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**On group structures, which are the norm in this area.** Two questions have to be separated and the original's edge case on group rules is the reason:

- **Which entity incurred the cost?** Readable, per connected file. `[auto]`
- **Which entity is entitled to claim it?** Not readable. Depends on the jurisdiction's rules on subcontracting within a group, on which company employed the staff, on who bore the risk, and on who owned the resulting IP. `[manual]`, and frequently the single most consequential judgment in a group claim.

Where R&D staff are employed by one company and recharged to another, **both legs are visible if both companies are connected, and neither leg on its own tells you who may claim.** Read both, present both, label both, and route the entitlement question to a specialist. See `intercompany-reconciliation` and the transfer pricing documentation — an R&D recharge between connected entities is a transfer pricing matter as well as a claim matter.

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
| `disabled` | `[manual]` | Not available. The step remains; the user supplies the data. |

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run, and the coverage sheet records it.

**This is the capability version of the rule this skill already lives by.** Do not carry a capability map between runs any more than you would carry last year's credit rate.

Read tool names off the response rather than typing them from memory. `UNKNOWN_TOOL` means re-read the list, not try a near-miss.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The chart of accounts, the vendor ledger for the year, the project or class dimension list, the payroll accounts and the grant income accounts are all independent. One message.

### The `mock: true` flag

If a response carries `mock: true`, it is **fixture data.**

The consequence here is specific: **a claim quantum computed on fixture data is a number with no relationship to anything.** Unlike a reconciliation, where fixture data at least demonstrates the arithmetic works, an R&D cost population is *entirely* about which real transactions belong in it. A fixture population tests nothing at all.

Label it in the file name, on the claim summary, and on every cost schedule. And do not produce a technical narrative alongside fixture costs even as an illustration — a narrative and a quantum sitting on the same page read as a claim, whatever the caveat says.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` **before asking anything.**

R&D claims are annual and repetitive. If the workspace profile carries the jurisdiction, the regime, the scheme the entity falls into, the project structure and the apportionment methodology agreed last year, **use them and say so.** But — and this is the discipline the original insists on — **use last year's methodology, and re-confirm this year's rules.** They are different things. The methodology is how the client works; the rules are what the law says, and the law changes.

Interview for:

1. **Jurisdiction and tax year.** `[manual]`
2. **The current regime, mechanism, scheme routing and rates.** `[manual]`, current-sourced, never carried forward. See Step 1.
3. **Project descriptions with technical detail.** `[manual]` — and this is the heart of the claim.
4. **Time and effort allocation.** `[manual]`. See Step 4, where this is discussed at length, because it is the largest cost category and the least visible.
5. **Entity size and status** — SME or large, profitable or loss-making. Partly readable; see below.
6. **Whether projects, classes or departments are dimensions in the book.** Answerable from the chart. **This one question determines whether half this skill is `[auto]` or `[manual]`**, so ask it early and answer it from the data rather than from memory.

**On entity size, which routes the whole claim in many jurisdictions:** turnover and balance sheet total are `[auto]`, straight off the accounts. Headcount is usually not — payroll frequently arrives as a summarised journal with no employee count in it. And the definitions are the hard part: most regimes aggregate **linked and partner enterprises**, so a company that is small on its own may be large once its group and its investors are counted. **The group is not in the company file.** Read what is readable, state it, and route the size determination to the specialist. Getting it wrong routes the entire claim to the wrong scheme at the wrong rate.

**Decisions are the user's; state is the workspace's.** The ledger says what was spent. It does not say whether it was research.
