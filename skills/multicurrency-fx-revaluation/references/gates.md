<!-- multicurrency-fx-revaluation · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

# Gates 0–3 — confirming scope on the Mosofin path

## Contents

- ONBOARDING — Confirm the workspace and its data sources
  - Gate 0 — Confirm the workspace
  - Gate 1 — Discover live datasources and settle the entity scenario
- PART A — Explore the confirmed sources, and personalise this run
  - Gate 2 — Discover enabled tools → build the capability map
  - Gate 3 — Profile the entity, then interview the user

# ONBOARDING — Confirm the workspace and its data sources

**Required for every skill, every run — whenever Mosofin is connected.** Gates 0 and 1
settle *which books this is about*: the workspace, and the data sources inside it.
**Part A then explores what those confirmed sources can actually do** and personalises
the run around them. Nothing is read before Gate 0 is answered.

**If the Mosofin tools are not present at all, skip this part.** There is nothing to
onboard: say so once, then run the skill manually on data the user supplies. See the
precondition check below.

Run Gates 0 → 1 → 2 → 3 in this order, before revaluing anything. This ordering is the contract. Do not
skip a gate because a previous conversation covered it — connections, permissions, and company files
change between periods.

Call the Mosofin tools by the **bare names your own tool list exposes** — `list_workspaces`,
`get_agent_datasources`, `get_datasource_tools`, `invoke_datasource_api_tool`, `get_skills`,
`get_my_skill`, `create_skill`. Do not add a `mosofin_` prefix and do not hardcode a client-side
`mcp__…` namespace; that string is composed by whichever MCP client is running.


## Gate 0 — Confirm the workspace

Call `list_workspaces` with **no arguments**.

- **One workspace** → read the workspace **name** back and **wait for an explicit yes**.
- **Two or more** (`selection_required`) → ask **in chat** whether this is single- or
  multi-workspace, then which workspace(s) **by name**, then call again with `workspace_ids=[…]`
  and `mode="single"` / `mode="multi"`.

Never auto-pick. Never print an internal numeric tenant id — name the workspace, pass the opaque
`ws_…` handle.

**Group entities frequently sit in different workspaces**, and translation needs all of them. Ask.

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Read each connected entity's home currency at Gate 3**, and use it here to settle the scenario:

- **Single entity, single currency** — **transaction FX may still apply** if it deals in other currencies.
  **Translation does not**, unless it reports in a currency other than its functional one.
- **Single entity, multiple transaction currencies** — **transaction FX and revaluation apply; translation
  does not.** This is the commonest case for this skill.
- **Multiple entities, different currencies** — **both apply**, and Step 4's translation is live. See the
  cross-entity step and the foreign currency translation work.

Refer to companies by `display_name`; never show the raw `data_source_id`.

# PART A — Explore the confirmed sources, and personalise this run

The workspace and its data sources are settled. This part finds out **what they
expose and which of it serves this request** — the tool catalogue in Gate 2, then
what is already known about this entity plus whatever still has to be asked in
Gate 3. The result is a run shaped around these books, not a generic template.

## Gate 2 — Discover enabled tools → build the capability map


*The write-tool guardrail that belongs here is in [`mosofin-protocol.md`](mosofin-protocol.md) under "Write tools — the Gate 2 guardrail". It applies in full at this gate.*


For **each in-scope datasource** (and **per company file** when several are live — pass
`data_source_id`), call `get_datasource_tools`. Bucket every tool by `effective_policy`:

| `effective_policy` | The task becomes | What you do |
|---|---|---|
| `enabled` | **[auto]** | Pull the evidence directly. |
| `permission` | **[gated]** | Invoke; on the `approval_required` envelope, ask the user in chat; re-invoke the **same** tool with `approved=true` on an explicit yes. **Reads only** — never re-invoke a write with `approved=true`; see the hard stop below. |
| `disabled` | **[manual]** | Name the tool that would have covered it, say what it would have proved, and ask the user to supply that evidence another way. |

Resolve **every task in Part B** against these buckets. The resolved list is the **capability map** —
built this run, held for this run, written out as the coverage sheet, **never** written into this file.

**Check specifically whether the reads return a currency and an original amount per transaction or
balance.** **This is the question above**, and it decides whether the revaluation population is `[auto]` or
whether the whole exercise must be performed outside the ledger.

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute:**
  - **A balance in the functional currency is not evidence it is not foreign.** Without a currency tag, a
    converted euro receivable and a domestic one look identical.
  - **A transaction-date rate recorded by the platform is not a period-end closing rate**, and it is not
    necessarily from an approved source.
  - **An account type is not a monetary / non-monetary classification.** **Deferred revenue is the case
    that catches people** — see the edge cases.
  - **A recorded FX gain is not a correct one.** It is what the platform's own revaluation produced, on its
    own rates.
- **There is no FX rate service, no hedge documentation and no functional currency determination on this
  surface.**

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) **for each in-scope entity**.

**Derive silently** what the profile answers: legal name, **home currency — the key field here** — fiscal
calendar and year-end, country.

**Ask the user** what actually changes the work:

| What to confirm | Required? | Notes |
|---|---|---|
| ~~Functional currency per entity~~ | **Now [gated]** | **The home currency is `[auto]`; the functional currency determination is `[manual]`.** They usually agree — **and when they do not, everything downstream is wrong.** |
| **Presentation currency** | **Required — [manual]** | Not a ledger field. |
| ~~Foreign-currency balances~~ | **Now [gated]** | **`[auto]` where the platform tags currency; `[manual]` otherwise.** |
| **FX rates** — closing, average, transaction-date | **Required — [manual]**, always | **Ask for the table, its source and its dates.** |
| **Account classification** — monetary vs. non-monetary | **Required — [gated]** | **Account types help; the classification is judgment.** Store it (Step 10). |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | |
| **Foreign operation financials** | If translating — **now [auto]** | Each entity's trial balance, per `data_source_id`. |
| **Hedging information** | If applicable — **[manual]** | **Hedge designation and documentation are not on this surface**. |
| **Whether the platform's own revaluation runs** | **Required — Mosofin addition** | Many platforms revalue automatically. **Know before proposing an entry**, or you will double-count. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name` **with their home currencies**, and the presentation currency. |
| **Confirm any profile contradiction** | **Required if one appears** | **Especially home currency versus asserted functional currency.** |
| **Confirm manual evidence** | **Required** | Rates, hedge documentation and the functional determination are `[manual]`. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a rate, a functional
currency, or a monetary classification.

**On later runs**, read stored preferences first (Step 10), confirm in one line, and ask only what changed.
The functional currency conclusions, the monetary classification, the rate source and the method persist;
**every rate, balance and FX amount is re-obtained.**
