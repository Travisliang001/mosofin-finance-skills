<!-- transfer-pricing-documentation · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Transfer Pricing Documentation — Mosofin Seed

Prepares and reviews transfer pricing documentation for cross-border related-party transactions — establishing that intercompany prices are at arm's length. Covers the functional analysis, method selection, benchmarking framework, and the three-tiered documentation structure under the OECD framework as adopted, with local variations.

**Framework-aware** — OECD Transfer Pricing Guidelines as the international baseline, local country rules vary — and it **does not hardcode jurisdiction thresholds, safe harbours or penalty rules.**

> **Transfer pricing is high-stakes and jurisdiction-specific; this skill builds the analysis and documentation structure and flags where qualified TP specialist review and local-rule confirmation are required.**

**Preserved without weakening.** This is the fifth source in the pack to state the no-hardcoding discipline itself, and the specialist-review requirement here is not a formality — TP disputes are among the largest tax exposures a group carries.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The split, which is unusually clean

| Layer | Where it lives | Verdict |
|---|---|---|
| **The transaction inventory** — what flowed between which entities, by type and amount | **Both ledgers, where both entities are connected** | **`[auto]`** |
| **The tested party's own result** — its PLI, over multiple years | **Its ledger** | **`[auto]`** |
| **The functional analysis** — functions performed, assets used, risks borne | **How the business actually operates.** Not a financial fact. | **`[manual]`** |
| **The comparables** — independent companies, their financials, the arm's-length range | **Commercial databases** | **`[manual]`** |
| **Local rules, thresholds, deadlines, safe harbours** | **Current official sources** | **`[manual]`** |

**One side of the arm's-length comparison is automatic and the other is not.** The tested party's margin is exact and free; the range it must sit inside comes from outside entirely.

### The strongest contribution is completeness, not arithmetic

Step 1 says the transaction inventory *"drives the whole analysis"*, and it is right. **It is also the step most often incomplete**, because in practice it is assembled by asking people what the intercompany transactions are.

**People forget categories.** The management recharge that started three years ago and was never papered. The guarantee the parent gave. The IP licence running on a one-page agreement from 2019. The interest on a loan nobody thinks of as a loan because it is called a current account. **Each of those is a controlled transaction requiring analysis, and none of them come to mind when somebody is asked "what do we charge each other?"**

**Reading both ledgers for every flow with a connected counterparty finds them all.** That is a genuine and material improvement in the foundation of the analysis, and everything downstream inherits it.

### Substance leaves a financial trace

The functional analysis is `[manual]` — functions, assets and risks are facts about how work is done, and no ledger records them.

**But the source's own edge cases 4 and 11 are about characterisation being contradicted by reality**, and reality has a cost structure:

> **An entity characterised as a limited-risk distributor that employs two hundred people including an R&D team is characterised wrongly, and its cost profile says so.**

`[auto]` can read **headcount cost, functional cost mix, asset base and inventory ownership by entity.** None of that *is* the functional analysis. **All of it corroborates or contradicts one**, and a contradiction is exactly what a tax authority looks for. See Step 2b.

### Three near-substitutes

**1. An intercompany balance is not a transaction inventory.** The balance is a net figure covering many flows of different types. **TP needs the gross flows, by category, by direction** — a net receivable of 400,000 might be 3m of goods one way and 2.6m of services the other, and those are two separate controlled transactions requiring two separate analyses. See `intercompany-reconciliation`.

**2. A contract is not conduct.** The source says it twice — Step 8 and edge case 11 — and it is the principle tax authorities apply: **where the agreement and the actual behaviour diverge, they follow the behaviour.** The ledger shows the behaviour. That makes it evidence about the *weakest* part of most TP positions.

**3. The tested party's margin is not the arm's-length range.** Knowing an entity earned a 3.2% operating margin says nothing about whether that is arm's length. **The range requires comparables, and comparables are not on this surface.**

---

## Related skills

| Skill | Relationship |
|---|---|
| `intercompany-reconciliation` | Reading both sides of a flow, explicitly out of scope for elimination but the source of the inventory. |
| `consolidation-and-eliminations` | Elimination, explicitly out of scope. |
| `related-party-disclosures-asc850` | Identifying related parties, and evidencing arm's length from comparable third-party terms. |
| `tax-return-prep-corporate` | Thin capitalisation, interest limitation, and TP adjustments in the computation. |
| `tax-planning-and-projections` | Where cross-border structuring is flagged for specialists. |
| `vat-gst-international` | The customs and VAT interaction with TP adjustments. |
| `segment-reporting` | The same dimension question behind segmenting a tested party's results. |
| `r-and-d-tax-credit` | R&D spend by entity, which also evidences DEMPE activity. |
| `three-statement-financial-model` / `scenario-and-sensitivity-analysis` | The working capital days used in comparability adjustments. |
