<!-- intangibles-and-amortization · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Internal-use software with cloud / SaaS arrangements**: **under recent guidance (ASC 350-40 updates), some
implementation costs in cloud computing arrangements are capitalizable as prepaid (not intangibles).
Distinguish carefully.** *Mosofin note*: **cloud and hosting spend is readable**, which makes the question
concrete rather than theoretical.

**Website development costs**: **similar framework to internal-use software. Phases: planning (expense),
application / infrastructure (capitalize), graphics / content (depends), operating (expense).**

**R&D costs that don't qualify for capitalization**: **expense as R&D, even if there's a future economic
benefit anticipated. Most R&D is expensed.**

**In-process R&D acquired in a business combination**: **capitalized at fair value with indefinite life
until the project is completed** — then amortize over the resulting intangible's life — **or abandoned**,
then impair. *Mosofin note*: **IPR&D is indefinite-lived, so Step 0b will surface it as unamortized** —
which is correct, not an error.

**Renewed customer contracts**: **if the customer relationship is renewable without significant cost, useful
life can extend across renewals. Document the basis.**

**Combined / integrated intangibles**: **if an intangible is so integrated with another that it can't
reasonably be separated, may need to combine for amortization. Document.**

**Trade name with finite legal life but indefinite economic life**: **typically classified as indefinite if
renewal is expected. Otherwise finite over legal life.** *Mosofin note*: **renewal fees appearing in the
ledger support the expectation**; their absence undermines it.

**Foreign-currency intangibles**: **held at historical cost in functional currency at the acquisition rate.
No FX revaluation; amortization runs in functional currency.**

**Intangibles acquired below market**: **if acquired below fair value, the difference may indicate
measurement issues. Carefully assess.**

**Patents under appeal / litigation**: **continue amortizing per current useful life unless materially
impaired by an adverse ruling.**

**Negative goodwill**: **handled in the business combination accounting, not here.**

**Brand acquired through marketing spend over years**: **typically not recognized as an intangible because
measurement is not reliable. Acquired brands are recognized; built brands are not.** *Mosofin check*:
**marketing spend sitting in an intangible account is a straightforward error**, and Step 4b's scan finds
it.

**Cost carried with no amortization and no impairment test** — *Mosofin-specific, and the cheapest finding
here*. Either indefinite-lived with a **mandatory annual test nobody is doing**, or amortization that never
started.

**A capitalization appears in the GL but not in the register** — *Mosofin-specific, and the most damaging*.
**That intangible will never be amortized.**

**A register asset has no cost in the GL** — *Mosofin-specific*. A phantom.

**Development spend continues after the stated go-live date** — *Mosofin-specific*. Either the ready-for-use
date is wrong or post-implementation costs are being capitalized. **Report the profile; do not adjudicate
the stage.**

**Capitalized costs that look like training, maintenance or data conversion** — *Mosofin-specific*. All
expense-stage activities. Step 4b surfaces them as candidates.

**Cost removed on disposal without the accumulated amortization** — *Mosofin-specific*, or the reverse. Both
leave the balance sheet wrong.

**The implied amortization rate is far from the policy life** — *Mosofin-specific*. Wrong lives, missing
assets, or a stale recurring journal.

**Goodwill sitting among the intangible accounts** — *Mosofin-specific*. **Route it to
the goodwill impairment test; it is never amortized here.**

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
intangibles are therefore unexamined.

**A result comes back with `mock: true`** — *Mosofin-specific*. **Capitalizing development costs moves
expense off the income statement**, so a fixture-based figure misstates reported profit directly.

**A stored register or net book value is reused** — *Mosofin-specific*. Both are state. Persist the policies
and the mapping; re-obtain the register and the balances.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's capitalization policy or lives to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
