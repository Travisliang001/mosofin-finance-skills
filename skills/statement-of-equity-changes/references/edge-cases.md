<!-- statement-of-equity-changes · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All thirteen preserved, in order.

**Stock split**: **doesn't change total equity.** Increases share count, reduces par per share — or, for a stock dividend treated as a split, a reclassification within equity. **Retroactively adjust comparative share counts and per-share data.** `[manual]` — it is a share event, and **`[auto]` confirms only that total equity did not move**, which is the check available.

**Reverse stock split**: the opposite — fewer shares, higher par. **Retroactive adjustment to comparatives.** `[manual]`.

**Convertible preferred converted to common**: **reclassify from preferred to common + APIC. No cash.** `[auto]` to detect — a movement between two equity accounts with no cash counterpart is exactly this shape; `[manual]` for the share mechanics.

**Convertible debt converted to equity**: debt extinguished, equity issued; **the difference per the conversion accounting — book value method or fair value method.** `[auto]` to detect the debt reduction and equity increase; `[manual]` for the method, which determines whether a gain or loss arises.

**Stock-based comp with graded vesting**: expense recognised **on an accelerated basis, each tranche separately, or straight-line** — per policy. **The APIC builds accordingly.** `[manual]`. `[auto]` for one signal: **a flat monthly stock compensation charge over several years, in a company that grants regularly, is a schedule that stopped being refreshed** — the same observation `quarter-end-close` makes.

**Forfeitures of unvested awards**: **reverse previously-recognised expense** where forfeitures are accounted for as they occur — **reducing the APIC build.** `[manual]` — forfeiture events are not in the ledger.

**Cumulative effect of adopting a new standard**: **adjusts opening retained earnings in the period of adoption, shown as a separate line.** `[auto]` to detect (Test 0a's fourth legitimate category); `[manual]` to compute. **It must appear as its own line and not be folded into the opening balance**, or the comparative becomes unexplainable.

**Treasury stock methods**: **cost method (most common) versus par value method — different APIC and RE effects on reissuance.** `[manual]` for the method; `[auto]` to check it is applied consistently, since **a book that treats some reissuances one way and some the other will not reconcile** and the inconsistency is visible in the counterpart accounts.

**Quasi-reorganisation**: rare; **resets a retained earnings deficit. Special disclosure.** `[manual]`. `[auto]` to flag: a large RE movement with no income statement counterpart is either this, a prior-period adjustment, or an error — and Test 0a will surface it either way.

**Non-controlling interest in a partially-owned subsidiary**: **NCI takes its proportional share of subsidiary net income and OCI; NCI dividends reduce NCI.** **Acquisition of additional NCI shares is an equity transaction with no gain or loss** under both frameworks. `[manual]` — and that last point is important and frequently got wrong: **buying out a minority is not a purchase generating goodwill or gain; it is a transaction between owners.** See `consolidation-and-eliminations` and the business combination accounting.

**Distributions in excess of capital** (partnership): **can create a negative capital account — flag for the partner's at-risk and basis implications**, which is a tax matter. **`[auto]` to detect** — a partner capital account going negative is directly readable, and it is the sort of thing nobody notices until a tax return is prepared. `[manual]` for the consequences.

**Dividends declared but not paid at period end**: **reduce RE now, at declaration date, creating a dividend payable; the cash leaves in the period paid. The equity statement reflects declaration; the cash flow reflects payment.** **`[auto]`** — this is tie-out 8, and it is the clearest example of the three statements holding three different views of one event.

**Multiple classes of stock with different rights**: **track each class separately; allocate income per the rights** — the two-class method for participating securities in EPS. `[manual]` — **EPS allocation needs the cap table and the rights**, neither of which is on this surface.
