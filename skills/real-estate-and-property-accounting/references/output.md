<!-- real-estate-and-property-accounting · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`), and **whether this is a propco, an opco, or a combined entity**
- Reporting level: **standalone or consolidated** — because it changes the classification answer
- Date and time of the reads; period covered
- Reporting framework, **and how it was established**
- **Fixture flag** — any `mock: true`? In bold, with the warning that the contradiction tests pass by construction on generated data.

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict. Note divergences from this file's defaults.

**Section C — Steps by verdict**
Every step with the verdict as it actually applied.

**Section D — What was not done, and why**
Typically:

- **Fair value measurement** — **no valuation on this surface**, under either the fair value model or the cost model's note disclosure
- **The land/building allocation basis** — relative fair values, from outside
- **Lease terms, escalations and incentives** — in the leases, not the ledger
- **Impairment testing** — recoverable amounts, not readable
- **Held-for-sale criteria** — management intent and marketing activity
- **Restrictions on title and pledges** — legal instruments; the loan is in the books, the charge is not
- **Capital and lease commitments** — contracts not yet transacted
- **Dismantling and restoration estimates**
- **Posting.** The gateway is read-only

**Section E — Unknowns carried forward**
Contradictions raised but not yet explained. Properties whose classification is unconfirmed. Leases whose terms are still needed for straight-lining. Impairment indicators flagged but not tested.

**Section F — Parameters used**
Framework. Measurement election per property. Useful lives. Land/building allocations and their basis. Accounts included in the property sweep. Anyone re-running next year needs these, and for property they govern the numbers for decades rather than months.
