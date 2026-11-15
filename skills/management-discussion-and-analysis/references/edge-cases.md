<!-- management-discussion-and-analysis · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Loss-making period**: **discuss the losses candidly, the path to profitability, and liquidity sufficiency.
Don't bury bad news.**

**Going-concern doubt**: **MD&A must address it directly — conditions, management's plans, and the
assessment. Coordinate with the going-concern note. Heavy legal review.** *Mosofin note*: **the conditions
are partly measurable** — cash trend, burn, covenant headroom — **the plans and the assessment are
management's**, and this is the section where that boundary matters most.

**Material weakness in internal controls**: **disclose in Item 9A (controls), and MD&A may reference.
Coordinate with `sox-controls-design-and-testing`.**

**Significant acquisition during the period**: **explain the impact on results — organic vs. acquired growth
— the financing, and integration. Pro-forma context helps.** *Mosofin note*: **the acquisition's ledger
traces are readable**; the organic / acquired split needs the acquired entity's contribution identified.

**Restatement**: **MD&A discusses the restated figures; explain the nature and impact**
(`restatement-and-prior-period-adjustment`).

**Highly seasonal business**: **explain seasonality so a single period isn't misread. Provide
trailing-twelve-month or full-year context.** *Mosofin note*: **seasonality is measurable** from monthly
history rather than asserted.

**Foreign-currency-heavy results**: **separate organic performance from FX translation effects
(constant-currency analysis).**

**Non-GAAP measure that excludes recurring costs**: **SEC scrutinizes adjustments that remove normal
operating expenses. Flag for review.** *Mosofin note*: **recurrence is countable** — test every adjustment
across prior periods.

**Forward-looking guidance**: **if the entity issues guidance, ensure it's clearly forward-looking with
appropriate caveats. Claude drafts based on management's stated expectations — it doesn't generate guidance
independently.**

**Private company report**: **MD&A may be less formal and not legally required, but still benefits from the
same structure and grounding.**

**A driver asserted without evidence, presented as analysis** — *Mosofin-specific*. Fine to include;
**classify it as management-asserted** so the grounding claim stays honest.

**The comparative does not match the filed prior year** — *Mosofin-specific*. Unposted audit adjustments.
**A visible inconsistency in a published document.**

**"One-time" items that recur** — *Mosofin-specific, and countable*. Test before characterising.

**Cash on hand presented as liquidity** — *Mosofin-specific*. **Restricted, trapped and committed cash are
all on the balance sheet and none of it is available.**

**A forward-looking statement with no management source** — *Mosofin-specific, and prohibited*. **It does
not go in the draft.**

**Group revenue including intercompany** — *Mosofin-specific*. Eliminate before discussing.

**Reported growth that is entirely currency** — *Mosofin-specific*. **Constant-currency analysis is the
honest presentation.**

**A disconnected group member** — *Mosofin-specific*. **The figures underlying a published narrative are
incomplete.** Say so before drafting.

**A result comes back with `mock: true`** — *Mosofin-specific*. **A published, and for filers legal,
document.** Stop.

**A prior period's narrative reused** — *Mosofin-specific*. **That is boilerplate**, which this skill exists
to avoid. Redraft.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
describe one entity's critical estimates as another's.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
