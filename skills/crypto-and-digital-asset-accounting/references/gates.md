<!-- crypto-and-digital-asset-accounting · gates.md · read for: Stage 2 — confirming scope and capabilities on the Mosofin path. Edit here, not in SKILL.md. -->

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

Run Gates 0 → 1 → 2 → 3 in this order, before recognising anything. This ordering is the contract. Do not
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

## Gate 1 — Discover live datasources and settle the entity scenario

Call `get_agent_datasources` with the confirmed `workspace_id`.

- `connected: true` → **in scope**.
- `connected: false` → **excluded, and named as excluded**. Surface any `reconnect_url`.

**Check every connected row for a crypto exchange, custodian or wallet-tracking platform.** If one is
connected, holdings and on-chain transactions may become `[auto]` and this skill changes shape entirely.
If none is, say so — the holdings are supplied, and everything downstream inherits that.

Settle the entity scenario:

- **Single-entity** — ask which company by `display_name`; the workflow runs against that one
  `data_source_id`.
- **Multi-entity** — ask which set. The workflow runs **once per entity**, every call targeting exactly
  one `data_source_id`, and every holding carries its entity's `display_name`. **Which legal entity owns
  a wallet is a question the chain cannot answer** — an address has no legal owner recorded on it. See
  the cross-entity step.

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

Rules that bite hardest here:

- **Read the real tool name from the catalog, never from memory.** Names are not uniformly styled — some
  underscored, some hyphenated.
- **A near-substitute is not a substitute, and here it is severe.** **A carrying value is not a holding.**
  The balance sheet shows what was recorded, not what is in the wallet — and the entire risk in this
  area is that those two diverge, through theft, key loss, an unrecorded transfer, or a custodian
  failure. **Never present a recorded balance as evidence of existence.** Existence needs the wallet.
- **Cash movement to an exchange is not a purchase.** It is a transfer of fiat. What was bought, at what
  price, in what quantity, happened off-ledger.
- **There is no price feed and no chain explorer.** Do not look for one; do not substitute anything.

## Gate 3 — Profile the entity, then interview the user

Call the platform's company-profile tool (on QuickBooks, `get_company_info`) for each in-scope entity.

**Derive silently** what the profile answers: legal name, base currency — which is the currency every
crypto position must ultimately be expressed in — fiscal calendar, country / region, industry.

**Ask the user** what actually changes the work — the original Inputs table, minus what the profile
answered:

| What to confirm | Required? | Notes |
|---|---|---|
| **Digital assets held / transacted** — type, quantities, dates | **Required — [manual]** unless an exchange is connected | The holdings themselves. Ask for a wallet or exchange export with balances **as at the reporting date**. |
| **Reporting framework** — US GAAP / IFRS | **Required — [manual]** | Determines the entire measurement model. |
| **Purpose of holding** — investment / payment / inventory (broker-dealer) / NFT-specific | **Required — [manual]** | Drives classification, and under IFRS decides between IAS 38 and IAS 2. |
| **Cost basis** — acquisition cost per lot | **Required — [gated]** | The **fiat outflow is often [auto]**; **the per-lot quantity split is [manual]**. |
| **Market data** — fair values at relevant dates from a principal market | **Required — [manual]**, always | Ask for the value, **the venue it came from, and the timestamp**. |
| **Transactions** — purchases, sales, transfers, rewards, payments | **Required — [gated]** | Fiat legs **[auto]**; crypto legs **[manual]**. |
| **Custody arrangements** — self-custody, exchange, custodian | Recommended — **[manual]** | Material to whether the entity even has an asset — see Step 5. |
| **Internal controls** — wallet keys, access, transaction approval | Recommended — **[manual]** | |
| **Cost basis method** on disposals — specific identification, FIFO, other | **Required if any disposals** | Confirm what the framework and the entity's policy permit. |
| **Confirmation of the current standard** as at the reporting date | **Required** | Never assert it from memory. |
| **Confirm scope** | **Required** | Read back in-scope and excluded company files by `display_name`, and which entity owns which wallet. |
| **Confirm any profile contradiction** | **Required if one appears** | |
| **Confirm manual evidence** | **Required** | Holdings, prices and custody will all be `[manual]`. Record what was supplied and as at when. |

Ask as **one short batch**. Propose defaults where reasonable — but **never** default a fair value, a
classification, the framework, or the current state of a standard.

**On later runs**, read stored preferences first (Step 9), confirm in one line, and ask only what changed.
The classification, the measurement model and the account map persist; **holdings, prices and the standard
confirmation are re-obtained every period**.
