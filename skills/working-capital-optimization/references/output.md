<!-- working-capital-optimization · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`) — **and whether intercompany balances were eliminated**
- **Months of history read**, and observation counts per series
- **Whether item-level inventory data was available**
- **DPO denominator used** — purchases or COGS
- **Fixture flag** — any `mock: true`? In bold: **every diagnostic here measures variation, and generated data has none.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict, and the Gate 2 inventory answer.

**Section C — Steps by verdict**
Every step. **A reader should see that Steps 1–4 were measured and Steps 5–8 were not.**

**Section D — What was not done, and why**
- **Industry benchmarks** — **external data; not on this surface**
- **Agreed terms**, as distinct from recorded terms
- **Dispute status and resolution time**
- **Supplier lead times and minimum order quantities** — commercial terms
- **Demand forecast**, and therefore excess-against-forecast
- **Safety stock appropriateness** — a service-level judgment
- **Stockout rate and service level** — **the guardrail, and not in the accounting system**
- **Supplier satisfaction**
- **Every relationship and operational risk assessment**
- **Cost of capital**
- **Any change to terms, payment timing or stock policy.** The gateway is read-only

**Section E — Unknowns carried forward**
Guardrails not yet defined. Opportunities sized but not risk-assessed. Customers deteriorating generally versus individually. Slow-moving stock identified but not valued. Discounts available and still uncaptured.

**Section F — Parameters used**
Period-days convention. DPO denominator. History window. Slow-moving threshold. Segment dimensions. **A CCC that cannot be reproduced cannot be tracked**, and the entire roadmap is measured against this baseline.
