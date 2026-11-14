<!-- standard-costing-and-variance-analysis · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`), and **plant** where relevant
- **Whether quantities are exposed by the surface** — and therefore which variances were computable
- Standards source and **their effective dates**
- Periods read
- **Fixture flag** — any `mock: true`? In bold: **fixture variances are small, two-sided and cleared on schedule, so the two tests that matter both pass.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that the standard side was supplied and the actual side was read.**

**Section D — What was not done, and why**
- **The BOM and routings** — **a manufacturing system, not a ledger**
- **Standard rates and their effective dates**
- **Usage, efficiency and volume variances**, where quantities were unavailable
- **Learning curve and downtime** — operational facts
- **Production volumes**, where units are not held
- **The inventory valuation and variance capitalisation policy**
- **Recommended operational actions** — supplier, quality and capacity decisions
- **Posting.** The gateway is read-only

**Section E — Unknowns carried forward**
Bridge residual unexplained. Variance accounts not clearing. Standards showing no reset across the available history. Items whose price change has not been traced to a vendor. Capitalised adverse variance not yet assessed against NRV.

**Section F — Parameters used**
Standards applied with effective dates. Periods. Quantity source. Overhead absorption basis and planned volume. Freight and duty treatment. **A variance that cannot be reproduced cannot be investigated**, and next month's report must be comparable to this one.
