<!-- crypto-and-digital-asset-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Standards changed recently and continue to evolve**: ASU 2023-08 (US GAAP) introduced fair-value
measurement for in-scope crypto, replacing the cost-less-impairment-no-reversal model. **Confirm the
current rules; older guidance is no longer applicable for in-scope assets.** *Mosofin note*: **never state
the current position from memory.** Record the confirmation date on Sheet 2.

**Scope of fair-value treatment**: ASU 2023-08 has specific criteria — **fungible, on a public blockchain,
not an issuer's own** — **not all crypto is in scope. NFTs typically aren't; some less-standard tokens
aren't.**

**IFRS lacks crypto-specific standards**: applying IAS 38 or IAS 2 **requires judgment.** Most operating
entities holding crypto for investment use IAS 38 cost or revaluation; traders and broker-dealers may use
IAS 2.

**Stablecoin classification**: **not automatically cash.** Depends on the right to redeem and counterparty
risk. May be a receivable, a cash equivalent (rarely, and only if very specific criteria are met), or
other crypto.

**Counterparty / custody risk**: post-FTX, **more rigorous assessment of whether assets on an exchange are
the entity's assets or a claim against the exchange. Material to recognition.**

**Fork events, airdrops**: receipt of new tokens — **typically recognized as other income at fair value
when received and the entity has the right.** Easy to miss entirely, because no cash moves and nothing
appears in the ledger.

**Stolen / lost crypto**: **write off (recognize the loss); insurance recovery if any. Significant control
concern.** *Mosofin note*: **the books cannot detect this** — the carrying value sits unchanged while the
asset is gone. Only the wallet shows it, which is why existence testing matters more here than almost
anywhere.

**Cost basis method on sales**: **specific identification is most common and accurate; other methods may
be permitted but document the policy.**

**Tax treatment is separate and complex**: crypto tax — including character (capital, ordinary) and
recognition events — is **jurisdiction-specific and often differs from book. Flag for a tax specialist; do
not advise on crypto tax in this skill** (see the corporate tax return preparation and personal tax return preparation
for the surrounding concepts, and flag specialist needs).

**Smart contract / DeFi activity**: lending, providing liquidity, yield farming — **each has specific
recognition issues; emerging guidance; specialist required.**

**Volatility and price source**: **principal market identification and Level 1 / 2 / 3 classification
matter for fair value reliability.** *Mosofin note*: because prices move so fast, **a price without a
timestamp and a venue is not evidence.** Record both for every value.

**Internal controls are paramount**: **a wallet compromise is a total loss.** Robust key management,
segregation and monitoring are essential — coordinate with `sox-controls-design-and-testing`.

**A carrying value presented as evidence of existence** — *Mosofin-specific, and the gravest error
available here*. The ledger records what someone entered. Theft, key loss and unrecorded transfers all
leave the carrying value untouched. **Existence requires the wallet or custodian statement.**

**Cash to an exchange treated as a purchase** — *Mosofin-specific*. The fiat leg is a transfer; what was
bought, in what quantity, at what price, happened off-ledger.

**A price supplied without a venue or timestamp** — *Mosofin-specific*. In this asset class that is not a
minor omission; the same asset can differ materially between venues and across hours.

**US GAAP impairment needs a price series, not a closing price** — *Mosofin-specific practical trap*. The
legacy model impairs to the **lowest** price at **any** point in the period. A single period-end quote
cannot support it.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
holdings are therefore unexamined. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data cannot support a carrying
value in an area where existence is already the hardest assertion.

**A stored price or holding is reused** — *Mosofin-specific*. Both are state, and in this asset class
they are stale within hours. Persist the price *source*, never the price.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's classification to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
