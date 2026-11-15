<!-- business-valuation · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Purpose drives standard of value**: fair market value (tax), fair value (financial reporting under
ASC 820 / IFRS 13), statutory fair value (e.g. appraisal rights) — **these are different standards
with different implications. Apply the right one.**

**Early-stage / unprofitable businesses**: DCF on negative or volatile cash flows is unreliable;
revenue multiples, comparable-company analysis, or alternative methods (**venture capital method**,
**real options** for certain situations) may be more relevant. Flag. *Mosofin note*: a short or
volatile ledger history is directly visible — say so rather than extrapolating from two quarters.

**Privately-held with no comps**: peer selection is judgment-heavy; **use the best available with
adjustment. Document the basis.**

**Synergies (strategic buyer)**: belong in **investment value** to a specific buyer, **not in fair
market value.** Don't include them in standalone valuations unless the purpose explicitly is
investment value.

**Control premium / DLOM stacking**: **applying both can over-adjust**; apply only what is
appropriate to the level of value being concluded.

**WACC sensitivity is huge**: small input changes (50 bp on WACC, 50 bp on growth) can move DCF value
substantially. **Always show sensitivity; don't present DCF point estimates without ranges.**

**Market data must be current at the valuation date**: risk-free rates, equity risk premia, betas,
peer multiples — **at the valuation date, not today's market.** *Mosofin note*: this is why no
market value is ever persisted at Step 12.

**Terminal value dominance**: TV is often **60–80% of DCF value** — the assumptions there matter
more than the explicit forecast. **Don't bury TV; rigorously justify it.**

**Tax (estate / gift), litigation, financial reporting**: require **qualified valuation specialists
adhering to professional standards** (USPAP, AICPA SSVS, IVS). **Don't substitute generic valuation
work where these are required — flag.**

**Cross-border valuations**: country risk, currency, tax differences. **The currency of valuation
must be defined.** *Mosofin note*: check it against the entity's base currency from the profile and
reconcile explicitly.

**Audit, fairness opinion, ESOP**: each has specific procedural and documentation expectations beyond
technical valuation work.

**A market input was supplied from memory** — *Mosofin-specific, and the gravest failure available
here*. There is no market datasource. Every rate, premium and multiple must carry an external source
and a date, or be listed as outstanding. **A plausible number with no source makes the whole
valuation indefensible.**

**Book equity was used as market equity in the WACC weights** — *Mosofin-specific*. The balance
sheet gives book values. WACC weights are conventionally market-based, and for a private company the
equity value is what you are solving for — which makes this circular. Say how it was resolved
(target structure, iteration, or peer-average structure) rather than silently using book.

**A summary line was used as net debt** — *Mosofin-specific*. Itemise. Finance leases, shareholder
loans and deferred consideration frequently sit outside an account named "debt", and restricted cash
frequently sits inside one named "cash".

**The share count came from the equity accounts** — *Mosofin-specific*. Those are issued shares, not
diluted. Options, warrants, convertibles and RSUs are not in the accounting system.

**Reported EBITDA was used unadjusted** — *Mosofin-specific*. It is readable, which makes it
tempting. Applying a market multiple to unnormalised earnings mixes a clean numerator with a dirty
denominator; say which you used and coordinate with `due-diligence-quality-of-earnings`.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
which part of the foundation is therefore unevidenced. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. A valuation may be relied on in a
transaction, a tax filing or litigation. Fixture data cannot support it.

**A stored peer set or WACC input is being reused** — *Mosofin-specific*. The peer *identities* may
persist; their *multiples and betas* must not. Re-source every market value at the new valuation
date.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply one entity's peer set or net-debt definition to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
