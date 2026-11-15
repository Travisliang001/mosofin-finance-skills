<!-- vat-gst-international · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

**Why this gate matters here.** VAT registration attaches to a **legal entity in a country**, and a group may hold several registrations across several entities. **A return prepared from the wrong entity's ledger is filed with a tax authority** under a registration number that does not correspond to the transactions in it.

---

## Gate 1 — Establish the datasource and entity scenario

Call `get_agent_datasources` for the confirmed workspace.

| Scenario | What it means here |
|---|---|
| **No datasource connected** | Everything is `[manual]`. The framework applies in full. Say so. |
| **Exactly one company file** | Confirm the `display_name`. **One entity may hold several country registrations** — see below. |
| **Several company files** | **Registrations are per entity per country.** Never combine. |
| **Connected but stale or broken** | A `reconnect_url` means the connection needs the user. Stop — **missing purchases understate input VAT recovery, which costs the client money silently.** |

Refer to company files by `display_name`. Pass `data_source_id` between tools; never display it.

**One entity, several registrations.** Unlike most skills here, the unit of analysis is **entity × country**, not entity. A single company file may support VAT returns in four countries, and **each needs its own output VAT, input VAT and control account position.**

`[auto]` **only where the chart or a dimension distinguishes them.** Many books carry one VAT account pair and rely on tax codes to separate jurisdictions; some carry a full set per country. **Establish which at Gate 3**, because a single-country return extracted from a blended account is not a return.

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

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this run.

**This is the capability version of the rule the source already lives by.** Do not carry a capability map between runs any more than you would carry last year's threshold.

**Two capability questions decide a lot here**: does the surface expose **tax codes per transaction line**, and does it expose **customer and supplier country**? Without the first, output VAT cannot be split by rate category; without the second, the cross-border analysis is guesswork.

Read tool names off the response. `UNKNOWN_TOOL` means re-read the list.

**Every call is stateless.** Carry `data_source_id` on each invocation, including the retry after approval.

**Batch independent reads.** The chart, the VAT accounts, sales and purchase transaction detail with tax codes, the customer and supplier masters, and turnover by country are independent. One message.

### The `mock: true` flag

Fixture data has **a VAT control account that empties on schedule, no foreign-supplier services, and no exempt supplies.** So all three of the headline detections return clean.

Label it in the file name and on the reconciliation sheet.

---

## Gate 3 — Read the profile, then interview for what remains

Call `get_my_skill` and `get_skills` before asking anything.

Interview for:

1. **Countries of activity** and **registration status** per country, with dates. `[manual]` — **persist it**; it is the join that makes the analysis an exposure assessment.
2. **Current rates and thresholds** per country. `[manual]`, current-sourced, **never carried forward.**
3. **Business establishment facts** — where established, fixed establishments. `[manual]`, and **it drives Step 1.**
4. **How the chart separates countries** — one VAT account pair or several. See Gate 1.
5. **Which supplies are zero-rated and which exempt.** `[manual]` — **the most consequential determination in the skill.**
6. **Partial exemption method**, if applicable.
7. **Special schemes in use** — OSS, IOSS, cash accounting, flat rate, margin.
8. **E-invoicing and real-time reporting obligations** per country.

**Decisions are the user's; state is the workspace's.**
