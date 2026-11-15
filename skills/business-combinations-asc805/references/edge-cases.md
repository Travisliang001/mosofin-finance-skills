<!-- business-combinations-asc805 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Asset acquisition vs. business combination**: the screen materially changes the accounting.
**Misclassification is consequential — confirm the assessment.** Transaction costs alone flip from
expensed to capitalized.

**Reverse acquisitions**: the legal acquirer can be the accounting acquiree (e.g. a SPAC merger).
**Apply control-based acquirer identification, not legal form.** *Mosofin note*: this is precisely
where naming the roles at Gate 1 matters — the connected file that "looks like" the buyer may be the
accounting acquiree.

**Contingent consideration remeasurement**: post-acquisition changes in the fair value of
liability-classified contingent consideration hit P&L — **can be volatile and unintuitive (a good
acquisition outcome triggering earnouts increases the liability and the expense).** Expect to
explain this to management more than once.

**In-process R&D (IPR&D)**: capitalized as an indefinite-lived intangible at acquisition; amortized
once completed (over its useful life); **written off if abandoned.** Tested for impairment as
indefinite-lived until completion.

**Bargain purchase**: **recheck all measurements before recognizing a bargain purchase gain** —
bargain purchases are unusual, and a negative result is usually a missed liability.

**Step acquisition (control gained from a smaller stake)**: remeasure the previously-held interest
to fair value with a gain / loss; **this gain / loss can be significant and is non-cash.**

**Acquired deferred tax assets**: recognize per the framework; subsequent changes in the valuation
allowance generally **don't adjust goodwill** (US GAAP — except during the measurement period).

**Pre-existing relationships** between acquirer and acquiree (settlement of pre-existing contracts
at acquisition): **accounted for separately, not as part of consideration.** *Mosofin note*: where
both entities are connected, prior trading between them is directly visible — check for it, because
an existing supply relationship is easy to overlook and changes the consideration figure.

**Replacement of share-based payment awards**: split between consideration (pre-combination service)
and post-combination compensation expense — **careful allocation.**

**Multiple components**: if the deal has separate components beyond the business combination itself
(e.g. a related supply arrangement at off-market terms), **separate them and account for each.**

**Common control transactions**: outside the scope of ASC 805 / IFRS 3 in many cases; **carryover
basis or other treatment applies. Flag.** *Mosofin note*: a workspace holding several company files
under one owner is a strong hint that a transaction between two of them may be common control — ask
rather than defaulting to acquisition accounting.

**Valuations are specialist work**: fair values of intangibles, contingent consideration, and complex
financial instruments require valuation specialists. **Don't fabricate.**

**A book value was carried through as a fair value** — *Mosofin-specific, and the sharpest risk when
the acquiree is connected*. Reading the acquiree's balance sheet makes it easy to fill Sheet 3's
fair value column with the book column. **State, per line, whether fair value equals book value by
conclusion or by default.**

**Transaction costs were capitalized** — *Mosofin-specific and directly detectable*. Identify
deal-related professional fees in the acquirer's ledger and report where they were posted.

**The acquiree's file is merged into the acquirer's during integration** — *Mosofin-specific*. The
post-acquisition revenue and earnings disclosure then becomes `[manual]`, because the separate
results are no longer distinguishable. Capture them **before** integration.

**The acquiree's fiscal year-end differs from the acquirer's** — *Mosofin-specific*. The pro-forma
comparable period is not simply the prior year; say which periods were used and why.

**The acquiree's base currency differs** — *Mosofin-specific*. Book values must be translated at the
acquisition-date rate before allocation; see `foreign-currency-translation-asc830`.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
which side of the allocation is therefore unevidenced. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. A purchase price allocation is
audited and sits on the balance sheet for years. Fixture data cannot support it.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply one deal's structure to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
