<!-- government-fund-accounting-gasb · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Modified vs. full accrual is the dominant complexity**: **applying the wrong basis to a fund is the most
common error. Governmental funds = modified accrual = no capital assets / long-term debt; proprietary and
fiduciary = full accrual = these on the BS. Always confirm fund type first.** *Mosofin note*: **the platform
holds one basis and will produce a plausible statement on the wrong one without complaint.**

**"Available" period for revenue recognition (modified accrual)**: **revenue must be measurable AND
available — typically within 60 days of period-end for GASB — to be recognized. Property tax, sales tax and
similar revenues require this assessment.** *Mosofin note*: **post-year-end collections are readable**, so
the test can be measured once the period is confirmed.

**Fund balance classifications are constraint-based**: **based on the strength of the limitation — external
> formal action by the governing body > intent > unassigned. Don't conflate.**

**Major fund determination**: **governmental and enterprise funds are presented individually if "major"
(meeting size thresholds), otherwise aggregated. Determine annually.** *Mosofin note*: **it is arithmetic —
compute it and show the working**, and never carry last year's determination forward.

**Pensions and OPEB**: **require actuarial valuation; the net pension / OPEB liability is often the largest
line on the government-wide statement. Don't fabricate; coordinate with actuary.**

**Nonexchange transactions** (taxes, grants): **specific GASB guidance on when to recognize — eligibility
criteria, time requirements, purpose restrictions. Different from commercial revenue.**

**Component units**: **legally separate entities for which the primary government is financially
accountable — blended or discretely presented depending on relationship. Specific guidance.** *Mosofin
note*: **other connected company files are candidates**, and the distinction is `[manual]`.

**Reconciliations between perspectives**: **differences between fund balance and net position have specific
common reconciling items — capital assets, long-term debt, deferred items, internal service fund
eliminations. Build a clear bridge.**

**Internal Service Funds**: **typically consolidated into governmental activities in the government-wide
statements** — eliminations needed. **Proprietary at fund level, governmental at government-wide level.**

**Standards change frequently**: **GASB issues new standards regularly — lease accounting GASB 87,
subscription IT GASB 96, and others. Confirm current standards.** *Mosofin note*: **record the date on which
currency was confirmed**, since a stored framework note ages.

**IPSAS vs. national public-sector framework**: **confirm which applies; some national frameworks differ
from IPSAS.**

**No fund dimension exists in the ledger** — *Mosofin-specific, and a stop condition*. **Fund-level reporting
cannot be produced.** Say so; do not aggregate everything into a General Fund.

**A class is treated as a fund without testing** — *Mosofin-specific*. **Run the self-balancing test.** A
dimension that does not balance is a cost tag.

**The platform's report is presented as a fund statement** — *Mosofin-specific, and the central trap*. **State
which basis produced it**, and list the conversions still required.

**Retained earnings is labelled fund balance** — *Mosofin-specific*. The platform's equity labels are
commercial. **Net position and fund balance are different things, on different bases.**

**A commercial cash flow statement is relabelled as proprietary** — *Mosofin-specific*. **GASB uses four
categories, not three.** Rebuild it.

**Interfund transfers do not net to zero** — *Mosofin-specific*. An unmatched entry misstates two funds and
the elimination. One query.

**Fiduciary funds are consolidated into the government-wide statements** — *Mosofin-specific, and wrong*.
They are excluded. The error is easy to make when each fund is a separate connected file.

**A result comes back with `mock: true`** — *Mosofin-specific*. **These statements are public documents,
frequently audited and filed with a state authority.**

**A stored fund balance or pension liability is reused** — *Mosofin-specific*. All state. **Persist the fund
structure and the classification decisions; rebuild the numbers.**

**A stored preference names a fund file that is no longer connected** — *Mosofin-specific*. **A missing fund
is a missing part of the reporting entity.** Flag it and stop.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
