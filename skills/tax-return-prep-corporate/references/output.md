<!-- tax-return-prep-corporate · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`) — **the filing entity**
- **Separate or group filing basis**
- Jurisdiction(s) and tax year
- **Finality status of the starting point**, and the date it was last tested
- **Every rate, allowance rate and restriction used, with source and date confirmed**
- **Fixture flag** — any `mock: true`? In bold.

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that the starting point was read and every adjustment was determined.**

**Section D — What was not done, and why**
- **Every rate, allowance, pool rate and restriction** — current-sourced
- **The disallowance determinations** — jurisdiction-specific judgment
- **Capital allowance pools, prior written-down values, elections** — **tax attributes, in the prior return**
- **The loss memorandum's opening position, types, and expiry**
- **Ownership changes** affecting loss availability — **no cap table on this surface**
- **Reversals of prior-year add-backs**, where the prior computation was unavailable
- **Withholding tax suffered**, where recorded net
- **Foreign tax credit limitations, treaty positions, Pillar Two**
- **Elections and claims, and their deadlines**
- **The transfer pricing analysis**
- **Review by a qualified local tax preparer — required**
- **Filing and signing.** The gateway is read-only

**Section E — Unknowns carried forward**
Sweep candidates not yet determined. Losses approaching expiry. Elections whose deadlines are approaching. Missed instalments. Return-to-provision difference not yet explained. Withholding certificates outstanding.

**Section F — Parameters used**
Every rate and restriction with source and date. Starting point and its finality. Accounts swept. Pools and rates applied. **A computation that cannot be reproduced cannot be defended on enquiry**, and enquiries come years later.
