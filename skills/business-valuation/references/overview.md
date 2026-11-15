<!-- business-valuation · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Business Valuation (Mosofin)

Estimates the value of a business or equity interest using the standard valuation approaches —
**discounted cash flow (DCF)**, **trading comparables**, and **precedent transactions** — and
bridges **enterprise value** to **equity value**. Used for M&A, capital raises, ESOP / option
pricing, litigation, tax (estate / gift), and management decision-making.

**In plain words:** what is this business worth? There are three honest ways to answer. Work out
the cash it will throw off in future and discount that back to today (DCF). Look at what similar
public companies trade for (comps). Look at what similar businesses actually sold for (precedent
transactions). Each gives a range, none gives a number, and the skill is in reconciling them and
being explicit about what you assumed.

Valuation involves significant judgment and **the purpose drives the standard of value** (fair
market value, fair value, investment value, etc.) — different purposes use different standards and
may have specific regulatory or professional standards (**USPAP, AICPA SSVS, IVS**). This skill
structures defensible analysis and **flags where a qualified valuation specialist is required**
(especially for legal, tax, or financial-reporting use).

It is **workspace-scoped**: every subject-company figure comes from a tool call against a company
file connected to your Mosofin workspace in this conversation, or from something you supplied by
hand and that is labelled as such.

## The split that defines this skill in a Mosofin workspace

A valuation has two halves, and a connected workspace covers one of them completely and the other
not at all.

**The subject company's own financial foundation is `[auto]`** — and it is more of the work than
people expect:

- Historical financials over several years, at any as-of date
- **Capital structure** — debt, cash, equity — which feeds both the WACC weights and the equity
  bridge
- **Net debt**, itemised from the actual accounts rather than a summary line
- **Working capital and its movement**, which is a direct DCF input and is otherwise rekeyed by
  hand
- **Capex and D&A**, likewise
- The effective tax rate actually borne, as a reference point
- Minority interest and equity-method investments as carried

**Every market input is `[manual]`, and no accounting datasource will ever supply one:**

- Risk-free rate, equity risk premium, beta, size premium, country risk premium
- Peer company identities and their trading multiples
- Precedent transaction identities and their deal multiples
- Control premium and DLOM study data
- Share prices, share counts held outside the books, option and warrant terms

The original's own rule is: **"All inputs are current-sourced; do not hardcode market data — confirm
at the valuation date."** In a Mosofin workspace that rule is enforced structurally, because there
is no market datasource to hardcode from. **Never supply a market input from memory.** A
plausible-looking equity risk premium is the single easiest way to make a valuation
indefensible.

**Mosofin is read-only.** It produces analysis, not a signed valuation. For any regulated or
high-stakes purpose, a qualified specialist owns the conclusion.
