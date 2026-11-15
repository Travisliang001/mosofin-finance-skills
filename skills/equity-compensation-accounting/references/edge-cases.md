<!-- equity-compensation-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Market conditions**: **factored into grant-date fair value; expense recognized even if the condition is
never met**, as long as service is rendered. **Counterintuitive but required — don't reverse for an unmet
market condition.**

**Performance conditions**: **recognize based on probability of achievement; true up as probability
changes; reverse if it becomes improbable. Different from market conditions.**

**Cash-settled awards**: **liability classification with remeasurement each period — expense is volatile as
the share price moves. Don't treat as equity-settled.** *Mosofin note*: the presence of a liability rather
than an equity credit in the accounts is a readable cross-check on the classification.

**Graded vesting attribution**: **the accelerated method front-loads expense and is required under IFRS 2;
US GAAP permits straight-line for service awards. The choice materially changes period expense.**

**Modifications / repricing**: **incremental fair value (before vs. after) is additional expense; can be
significant. Flag for careful treatment.** Two valuations at the modification date are needed.

**Private company valuations**: **illiquid shares need a defensible valuation** (often a **409A**-type
valuation in the US context). **Flag valuation-specialist involvement; don't fabricate a fair value.**
*Mosofin note*: and do not reuse a stale one — record the valuation date against each grant.

**ESPP with look-back**: **the look-back feature makes the fair value more complex than a simple discount.
Apply the appropriate model.**

**Early exercise / non-standard terms**: **change the expense pattern; analyze the specific terms.**

**Tax effects**: **book expense and the tax deduction differ in timing and often amount** — the deduction
is frequently based on **intrinsic value at exercise or vest**, not grant-date fair value. **Excess tax
benefits / deficiencies flow through the provision** (US GAAP). Coordinate with
the tax provision work.

**Forfeiture policy consistency**: **apply the chosen policy consistently; switching requires care.**

**Awards to non-employees**: **historically different, now largely aligned with employee awards under
ASC 718 (post-ASU 2018-07) — confirm treatment.**

**Recorded expense differs from the schedule** — *Mosofin-specific, and common*. SBC is posted by manual
journal from a schedule kept elsewhere; nobody reconciles a non-cash expense. Run the Step 0b comparison.

**The share count in the equity accounts read as the award population** — *Mosofin-specific*. Options and
unvested RSUs are not issued shares and appear nowhere on the balance sheet. Only the cap table has them.

**RSU vesting missed entirely** — *Mosofin-specific*. Unlike an option exercise, RSU vesting brings in **no
cash**, so there is no bank movement to prompt anyone. It is the event most often unrecorded.

**Exercise cash with no equity entry** — *Mosofin-specific*. Money arrived; the shares were issued; if the
equity accounts do not move, the entry was missed.

**A stale valuation applied to a later grant** — *Mosofin-specific discipline*. Private valuations are
periodic and dated. Record the valuation date per grant and flag any grant priced off an out-of-date one.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose SBC
is therefore unexamined. In a group this matters, because the expense may sit in exactly that entity.

**A result comes back with `mock: true`** — *Mosofin-specific*. SBC flows into published results, the tax
provision and the cash flow statement; a fixture-based figure propagates into all three.

**A stored fair value or award list is reused** — *Mosofin-specific*. Both are state. Persist the valuation
*source* and the plan design; re-obtain the awards and the values.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply the issuer's policy to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
