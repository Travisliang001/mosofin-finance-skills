<!-- segment-reporting · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`) — **all files read, where a segment spans entities**
- Framework: ASC 280 or IFRS 8
- **CODM as identified, and by whom**
- **Whether segments are a ledger dimension, and which dimension**
- **Whether the balance sheet is dimensioned** — it determines the asset test
- Geographic attribution basis used
- Period and comparative period
- **Fixture flag** — any `mock: true`? In bold.

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Steps 1, 2 and 4 were human.**

**Section D — What was not done, and why**
- **CODM identification** — **a person or committee; not a field in any ledger**
- **What the CODM actually reviews** — their reports, not the chart
- **The aggregation judgment**
- **The profit measure definition**
- **Which Step 5 items the CODM sees**
- **Intersegment pricing basis** — a policy
- **Long-lived assets by country** — **an asset register records cost, not location**
- **Product grouping**, where revenue is coded only to accounts
- **Common control between customers**, for the 10% aggregation
- **Disclosure.** The gateway is read-only

**Section E — Unknowns carried forward**
Uncoded transactions unresolved. Dimensions whose relationship to the CODM's view is unconfirmed. Segments failing tests but of continuing significance. Restatement practicability undetermined. Customers approaching the 10% threshold.

**Section F — Parameters used**
Dimension used for segments. Profit measure and its definition. Denominators for each test. Attribution basis. Periods read. **Segment disclosures must be comparable period to period**, and comparability depends on these staying stable or the change being disclosed.
