<!-- quarter-end-close · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

Sheet 10 of every output. Not optional, and not abbreviated because the quarter went smoothly.

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- Date and time of the reads
- Quarter and fiscal calendar used, **and whether the fiscal year end was read or assumed**
- **Fixture flag** — did any response carry `mock: true`? If so, in bold, with the Gate 2 caution restated: **the time-series diagnostics did not test anything.** Fixture data is generated smooth and will pass every pattern test in this skill.

**Section B — Capability map as observed today**
Each tool used: its name as returned by `get_datasource_tools`, its `effective_policy`, and the resulting verdict. Note every case where the observed policy differed from this file's default — those differences are what the evolved version should absorb.

**Section C — Steps by verdict**
Every task in Step 2's eleven groups, plus Steps 1 and 3 through 6, with the verdict **as it actually applied here**. Count them. A reader should see immediately how much of the quarter was automatic and how much was not.

**Section D — What was not done, and why**
The `[manual]` list with reasons. For a quarter-end this will typically include:

- The EAETR — **a forecast rate; no ledger contains next year's expected income**
- Covenant definitions — **in the credit agreement, not the chart of accounts**
- The bank statement leg of Step 6 — **bank statements are not on this surface**
- Type 2 subsequent events — **not transactions; found by asking, not by reading**
- The going-concern assessment — **forward-looking; management's to make and to sign**
- Litigation accruals, earn-out revaluation, stock compensation — **legal judgment, valuation, and cap table respectively, none of which are on this surface**
- Control testing and sub-certifications — **evidence of human action, and humans signing**
- ARR, MRR, bookings, backlog and RPO — **contract metrics, not ledger metrics**
- Every filing, certificate and signature in Step 3

**Section E — Unknowns carried forward**
Variances quantified but not explained. Subsequent events flagged by the ledger sweep but not yet categorised. Covenant definitions still not obtained. Estimates whose rate has not moved and whose review has not been evidenced. These are next quarter's opening work list.

**Section F — Parameters used**
Interim materiality and the denominators it was assessed against. Covenant definitions as applied. The fiscal calendar. Segment dimension, if any. Which months of the quarter were verified as closed. Anyone re-running next quarter needs these to get a comparable answer — and comparability across quarters is most of the point of quarterly reporting.
