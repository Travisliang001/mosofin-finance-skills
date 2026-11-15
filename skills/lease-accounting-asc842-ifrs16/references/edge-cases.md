<!-- lease-accounting-asc842-ifrs16 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Operating-lease ROU amortization (ASC 842)**: **the ROU asset amortization is a balancing figure so total
lease expense is straight-line — not independent straight-line depreciation. A common mechanical error.**
*Mosofin note*: **now detectable** — read the monthly expense and check it is level.

**IFRS 16 vs. ASC 842 expense pattern**: **IFRS 16 produces front-loaded total expense (depreciation +
interest) for all leases; ASC 842 operating leases produce level expense. This affects the P&L and is a key
conversion difference**.

**"Reasonably certain" option judgments**: **whether renewals, terminations or purchase options are
reasonably certain drives the term and measurement — significant judgment; document the basis.**

**Discount rate sensitivity**: **the IBR materially affects the liability; small rate differences compound.
Use a defensible rate.**

**Variable lease payments**: **index or rate-based are included at the initial index or rate — and reassessed
on change; usage or sales-based are expensed as incurred, not capitalized. Don't capitalize true variable
payments.** *Mosofin note*: **the ledger does not distinguish them**; only the contract does.

**Lease vs. service**: **if the customer doesn't control an identified asset, it's a service, not a lease.
Assess before capitalizing.**

**Modifications vs. reassessments**: **different triggers and mechanics; a modification changes the
contract, a reassessment reflects changed circumstances under the existing contract. Apply the right one.**

**Short-term and low-value elections**: **reduce burden but must be applied consistently; a lease with a
purchase option isn't short-term.** *Mosofin note*: **a multi-year "short-term" population is readable** and
worth questioning.

**Sale-leaseback, sublease, lessor accounting**: **each has distinct rules; this workflow centers on lessee
operating / finance — flag these for the specific guidance.**

**Impairment of ROU assets**: **ROU assets are subject to impairment** (the goodwill impairment test
principles for long-lived assets).

**Transition**: **adopting the standards involved transition methods and expedients; for already-adopted
entities, ensure consistency with the transition approach taken.**

**Rent expense with no ROU asset** — *Mosofin-specific, and the highest-value finding*. **Unrecognised
leases**, or an exemption claim worth confirming.

**Recurring equal payments to a vendor** — *Mosofin-specific*. **The signature of a lease** — and also of
subscriptions, insurance instalments and loan repayments. **A candidate, not a conclusion.**

**The schedule does not tie to the ledger** — *Mosofin-specific*. Lease schedules are maintained outside and
posted by journal, so drift is common and silent.

**Total operating lease expense is not level** — *Mosofin-specific*. **The plug mechanic has gone wrong.**

**A payment amount changed mid-term** — *Mosofin-specific*. An escalation, a reassessment trigger, or an
unremeasured modification. The ledger shows it; the contract explains it.

**Classification asserted under IFRS 16** — *Mosofin-specific*. **Lessees do not classify under IFRS 16.**
A framework error, raised before measurement.

**A foreign-currency lease with the ROU retranslated** — *Mosofin-specific*. **The liability is monetary and
retranslates; the ROU asset is non-monetary and does not.**

**Lease liabilities ignored in covenant calculations** — *Mosofin-specific*. They are debt under many
definitions, and recognition alone can cause a breach.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
leases are therefore unexamined — **including the completeness search.**

**A result comes back with `mock: true`** — *Mosofin-specific*. Lease liabilities flow into leverage and
covenant measures.

**A stored schedule or rate is reused** — *Mosofin-specific*. Both are state. Persist the methodology and
the account map; rebuild the schedule.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's IBR or cleared-payment list to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
