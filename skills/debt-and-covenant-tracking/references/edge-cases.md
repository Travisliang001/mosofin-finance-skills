<!-- debt-and-covenant-tracking · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**"EBITDA" per agreement vs. book EBITDA**: agreement EBITDA is **virtually always different** — specific
addbacks, exclusions, and caps on certain addbacks. **Compute per the agreement, not book — the most
common covenant computation error.** *Mosofin note*: and the easiest one to make here, because book EBITDA
is one read away. **Show the bridge from book to covenant EBITDA, adjustment by adjustment.**

**Pro-forma adjustments**: agreements often allow them — for an acquisition, treating its EBITDA as if
owned for the full TTM period. **Track and apply per the agreement.**

**Cure rights**: some agreements allow curing a breach via an equity contribution (an **"EBITDA cure"**).
Specific mechanics; **track the available cures** — they are usually limited in number and in frequency.

**Cross-default**: **a breach of one facility can trigger default on others. Map the cross-default web.**

**Material adverse change (MAC)**: a **qualitative event of default** — judgment-heavy and rare to invoke,
but it exists. Be aware.

**Reporting deadlines**: **missing a reporting deadline — financials, certificates — can itself be a
default. The compliance calendar matters.** It is the most avoidable default there is.

**Floating-rate exposure**: **rate increases compress interest coverage. Project at current and stressed
rates.** *Mosofin note*: the **effective rate actually borne** is computable from interest against average
balance, which is a better base for stress testing than the headline margin.

**Capitalized leases / new lease standards as debt**: covenants drafted before **ASC 842 / IFRS 16** may
not contemplate operating lease liabilities now on the balance sheet. **Read carefully — some definitions
exclude these; others include.** *Mosofin note*: the lease liability is directly readable, and including
or excluding it can move a leverage ratio by a full turn. This is the single highest-impact definitional
question in most modern agreements.

**Refinancing timeline**: refinancing **12–18 months ahead of maturity is typical; waiting too long risks
distressed terms.** The maturity profile drives planning.

**Subordinated / mezzanine / second-lien debt**: **priority and intercreditor terms matter; covenants may
differ across tranches** — and the tighter tranche binds first.

**Foreign currency debt**: **revaluation affects ratios; some agreements account for FX in definitions,
some don't. Read carefully.** A currency move can breach a leverage covenant with no change in the
business at all.

**Going concern interaction**: **covenant uncertainty within 12 months can trigger a going-concern
assessment**, which the notes to the financial statements must reflect. A projected breach is not only a lender
issue; it is a financial-statement issue.

**A covenant computed from book figures** — *the central Mosofin-specific hazard*. Do not do it. Where
definitions are unavailable, present the book components labelled as such and state that the covenant was
not computed.

**A debt-like item missing from the facility inventory** — *Mosofin-specific*. Finance leases, shareholder
loans, deferred consideration and overdrafts are all readable and are all frequently inside a covenant
Debt definition. Sweep for them at Step 0b.

**A revolver drawn and repaid within the period** — *Mosofin-specific*. Net balance movement shows nothing;
the ledger shows both legs. Interest was incurred and the peak balance may matter for a covenant tested on
average or maximum debt.

**The effective rate differs from the stated rate** — *Mosofin-specific*. Fees charged as interest, a
ratcheted margin, or a facility that is not what the inventory says. Worth investigating.

**Confirmed breach, but debt still classified long-term** — *Mosofin-specific and directly detectable*.
The balance sheet is misstated. Flag it.

**A company file is connected but not active** — *Mosofin-specific*. If it is inside the covenant
perimeter, the ratio cannot be computed. Name it and stop rather than computing over a partial perimeter.

**A result comes back with `mock: true`** — *Mosofin-specific*. A compliance certificate is signed by an
officer and relied on by a lender. Fixture data cannot support it.

**A stored covenant definition belongs to a different facility** — *Mosofin-specific*. Facilities define
the same-sounding ratio differently. Key every definition to its facility.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*, and here it may
mean **the borrowing perimeter has changed**. Ask; do not assume it is a connection lapse.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
