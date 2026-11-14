<!-- working-capital-optimization · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All twelve preserved, in order.

**Damage from over-stretching AP**: **stretching beyond terms without agreement seems "free" but isn't — preferred-customer status, terms, and ultimately supply itself can suffer. The "savings" can reverse into COD demands and supply disruption. The biggest mistake in working capital programs.** `[manual]`. **And the asymmetry at the top of this file exists because of this edge case**: the saving is computable and the reversal is not.

**Lost sales from inventory cuts**: **stockout cost is often invisible in financials but real — lost orders, customer switching, expedite costs. Don't optimise inventory in isolation from service.** `[manual]`. **"Invisible in financials" means invisible to Mosofin**, which is precisely why the guardrail must be entered by hand.

**Concentration risk in AR**: **a few large customers stretching can mask a broader payment trend. Look at the distribution, not just the average DSO.** **`[auto]`** — DSO by customer, with concentration, is exact. **A mean DSO is a poor summary of a skewed distribution**, and this is a case where the automated version is straightforwardly better than the manual one.

**Seasonality**: **working capital is highly seasonal in many businesses — retail builds inventory pre-peak, collects post-peak. Trend analysis must account for seasonality; period-end snapshots mislead.** **`[auto]`** — Step 1b, from the monthly series.

**Growth versus working capital**: **growing businesses consume working capital. Don't interpret growing WC investment as inefficiency if it's funding growth.** **`[auto]`** — Step 1b separates volume from deterioration arithmetically.

**One-time versus sustainable improvement**: **pushing collection hard in one period generates a one-time unlock but isn't repeatable; the sustainable improvement is process change. Distinguish.** **`[auto]`** — the intra-period pattern shows which.

**Factoring and supply chain financing have real cost**: **not free cash; the discount or fee is a financing cost. Use selectively.** `[manual]`. **`[auto]` for one honest comparison**: the implied annualised rate against the client's cost of capital, so the lever is evaluated as the financing it is.

**Industry benchmarks vary widely**: **capital-light services have very different profiles from heavy manufacturing or distribution. Compare to relevant peers.** `[manual]` — **benchmarks are not on this surface**, and a generic benchmark is worse than none.

**Inventory write-downs from liquidation**: **liquidating obsolete inventory frees cash but takes a P&L hit. Often net-positive — cash now beats book value held forever, plus stopped carrying costs — but recognise the trade-off.** `[auto]` for the carrying value and the age; `[manual]` for the realisable value. **Note that the provisioning question may already exist independently of the cash one**, as an inventory obsolescence reserve.

**Customer payment terms as competitive weapons**: **in some markets, generous terms are a sales weapon; tightening them may cost market share. Calibrate versus industry.** `[manual]` — **a commercial judgment with no ledger proxy.**

**Supplier financial stress**: **a supplier in trouble may need faster payment, not slower, to ensure continuity. Working capital optimisation must adapt to the relationship and the situation.** `[manual]`, **and it is the clearest possible counter-example to a purely arithmetic approach**: the optimal action for a fragile sole-source supplier may be to pay them sooner, at a direct cost to the metric this skill is trying to improve.

**Tax and reporting effects**: **large changes near period-end can look like window dressing — and inventory write-downs and AR allowances have P&L effects. Coordinate with reporting periods.** **`[auto]` to detect the pattern** — Step 1b — and `[manual]` to judge. **A working capital programme whose gains appear only at period ends will attract exactly this question**, from auditors and from acquirers in a quality-of-earnings review.
