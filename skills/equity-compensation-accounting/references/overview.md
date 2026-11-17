<!-- equity-compensation-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Equity Compensation Accounting (Mosofin)

Accounts for **share-based / stock-based compensation** — options, RSUs, RSAs, ESPPs and similar awards —
under **ASC 718** (US GAAP) / **IFRS 2**. Determines grant-date fair value, recognizes expense over the
service / vesting period, handles forfeitures and modifications, and produces the entries and disclosures.

**In plain words:** when you pay people in shares or options rather than cash, that is still pay, and it
still costs the business something. The accounting question is *how much* — because nobody handed over any
money — and *when*, since the employee has to stay to earn it. The answer is: value the award on the day
it is granted, then spread that value across the years they have to work for it.

This skill is **framework-aware** (ASC 718 / IFRS 2). **Fair-value inputs** — volatility, expected term,
risk-free rate — **and the entity's valuation are inputs**; the skill applies the recognition mechanics
correctly and **flags where a valuation specialist is needed** (complex or illiquid awards).

It is **workspace-scoped**: recorded expense, APIC movements and exercise proceeds come from tool calls
against a company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

## What is outside the ledger here

**The cap table is the source of truth, and it is not an accounting datasource.** Grants, quantities,
strike prices, vesting schedules, exercises, forfeitures and the award population all live in an equity
management system or a spreadsheet. So:

- **The award population and its terms** — `[manual]`
- **Every grant-date fair value**, and every input to it — `[manual]`. There is no market data here, the
  same structural rule as in a business valuation, `crypto-and-digital-asset-accounting` and
  `derivatives-and-hedging-asc815`
- **The vesting conditions and the probability assessment** for performance conditions — `[manual]`

**What the workspace does contribute is a set of checks on whether the accounting actually happened
correctly:**

1. **The expense reconciliation.** The schedule says the period's charge should be X; **the ledger says
   what was actually posted.** Comparing them is one read, and a difference means either the schedule is
   stale or an entry was missed — both common, since SBC is usually a manual journal.
2. **The APIC roll-forward.** Equity-settled expense credits additional paid-in capital, and that
   movement is readable — which feeds `statement-of-equity-changes` directly.
3. **Exercise proceeds through cash.** When options are exercised, **money comes in**. Cash received with
   no corresponding equity entry, or an equity entry with no cash, is a completeness signal.
4. **Functional allocation.** Where the entity uses departments or classes, the split of SBC across R&D,
   sales and G&A is readable — and checkable against where the recipients actually work.

**Mosofin is read-only.** It cannot grant, vest, exercise or settle anything. Every entry below is a
*proposal*.
