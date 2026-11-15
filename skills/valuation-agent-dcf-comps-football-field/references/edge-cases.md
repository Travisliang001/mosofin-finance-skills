<!-- valuation-agent-dcf-comps-football-field · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section.)*

**The valuation date is not a period end.** The bridge needs a balance sheet at the date. **Say what basis was used** — nearest close, or a computed position — because the bridge's apparent precision depends on it.

**Levered cash flows discounted at WACC.** Double-counts the financing benefit and overvalues. Step 2's conversion instruction exists for this; **check which the model produces** rather than assuming.

**Lease liabilities in net debt but IFRS 16 EBITDA in the multiple.** The error compounds. **Pick a basis, state it, and apply it to the comparables too.**

**Restricted cash treated as cash.** Overstates equity value. `[auto]` to identify where the balance sheet distinguishes it; **ask where it does not.**

**A terminal value that is 85% of enterprise value.** Not wrong, and it means the explicit forecast is nearly decorative. **Say so, and make the sensitivity on terminal assumptions the headline.**

**Terminal growth above long-run economic growth.** Implies the business eventually becomes the whole economy. `[manual]` — and it needs the "clear rationale" the source requires.

**A target capital structure far from the actual.** A claim about recapitalisation, which changes WACC materially. **`[auto]` shows the actual**; the target is an assumption and should be labelled one.

**Comparables on a different accounting basis.** Different frameworks, different lease treatment, different capitalisation policies. **A multiple is only transferable if the metrics are comparable**, and this is where cross-border comps sets quietly fail.

**A recent financing round used as a valuation point.** It priced a specific security with specific rights — liquidation preference, anti-dilution, participation. **The headline post-money is not the common equity value**, and treating it as one overstates. `[manual]` — and it needs the cap table.

**Negative EBITDA or negative cash flows.** Multiples break; the DCF becomes almost entirely terminal value. **Flag that the method is doing very little work** rather than presenting a range with false precision.

**Purpose is financial reporting or tax.** A qualified valuation specialist is required. **This skill's output is working analysis feeding that process**, not the valuation.

**Minority versus control basis.** Trading comps generally reflect minority stakes; transaction comps include a control premium. **Mixing them on one football field without stating the basis compares two different things.** `[manual]`.
