<!-- goodwill-and-impairment-testing · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Goodwill and Impairment Testing (Mosofin)

Tests **goodwill**, **indefinite-lived intangibles**, and **long-lived assets** for impairment under the
applicable framework. Identifies the **unit of account** (reporting unit / CGU), assesses indicators,
performs quantitative testing where required, and computes any impairment loss with disclosures.

**In plain words:** some things on the balance sheet are carried at what they cost, and the question each
year is whether they are still worth that much. If they are not, the difference is a loss that has to be
recognised now. The hard part is never the subtraction — it is working out what they are actually worth.

This skill is **framework-aware** (US GAAP **ASC 350 / 360** / IFRS **IAS 36** — with notable differences).
**Impairment involves significant valuation judgment; the skill structures the test and flags where
valuation specialists are required. It does not fabricate fair values, recoverable amounts, or cash flow
projections.**

It is **workspace-scoped**: carrying amounts, prior impairments and the performance evidence behind
triggering events come from tool calls against a company file connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

## The clean split: one side of the subtraction, not the other

Every impairment test in this skill is the same comparison:

```
Impairment = Carrying amount  −  Recoverable amount (or fair value)
```

**The workspace owns the left-hand term exactly and the right-hand term not at all.**

- **Carrying amount is `[auto]`.** Goodwill, intangibles, PP&E, accumulated depreciation and amortization —
  all readable, all precise, all tied to the financial statements.
- **Fair value, recoverable amount, value in use, cash flow projections and the discount rate are
  `[manual]`.** Always. There is **no valuation model, no market data and no forecast** on this surface —
  the same structural rule as `business-valuation`, `crypto-and-digital-asset-accounting` and
  `derivatives-and-hedging-asc815`.

**So this skill cannot conclude that anything is impaired.** What it can do is three things that are
genuinely useful:

1. **Scope the test.** **[auto]**: read the balance sheet and see whether goodwill, indefinite-lived
   intangibles or material long-lived assets exist at all, and how much. **No goodwill balance means no
   goodwill test** — a scoping conclusion in one query.
2. **Monitor the triggering events that are quantitative.** **This is the most valuable contribution, and
   it is the step that decides whether a test is needed at all.** Two of the original's eight indicators —
   **declines in operating performance or cash flows**, and **loss of key customers, contracts or markets**
   — are measurable directly from the ledger, by segment and over time. **They can be watched every month
   rather than assessed once a year**, which is exactly how a triggering event is supposed to be caught.
3. **Assemble the carrying amounts** the specialist's valuation will be compared against, and **the prior
   impairment history** that governs reversal.

**Mosofin is read-only.** It cannot record an impairment, a reversal or a write-down. Every entry below is
a *proposal*.
