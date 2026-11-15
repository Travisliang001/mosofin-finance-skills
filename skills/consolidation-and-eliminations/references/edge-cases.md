<!-- consolidation-and-eliminations · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Sub acquired mid-period**: **consolidate only from the acquisition date. Pre-acquisition results stay
out.** The acquisition-date balance sheet uses fair values. *Mosofin
note*: read the sub's P&L **from** the acquisition date, not for the whole period — the connected file
holds both, and taking the wrong range consolidates results the group never owned.

**Sub disposed mid-period**: **consolidate up to the disposal date. Recognize gain / loss on disposal.
Deconsolidate the remaining interest (if any) at fair value.**

**Step acquisition** (parent increases ownership from significant influence to control): **remeasure the
previously-held equity interest to fair value, recognize gain / loss** (US GAAP and IFRS both).

**Changes in ownership without loss of control** (e.g. parent buys more of an already-controlled sub):
**equity transaction, no gain / loss, adjust NCI and APIC.**

**Different fiscal year-ends**: if a sub's year-end differs by ≤ 3 months (US GAAP) — IFRS requires
coterminous or adjusted — **adjust for significant intervening transactions.** *Mosofin note*: directly
detectable from the entity profiles; check at Gate 3 rather than discovering it at Step 9.

**Reciprocal shareholdings** (sub owns shares in parent): treasury-stock treatment or eliminate per the
framework.

**Multi-tier groups** (parent → sub → sub-sub): **consolidate bottom-up. Sub-sub into sub, then sub into
parent. NCI computed at each level.** *Mosofin note*: the reading order matters — establish the tier
structure at Gate 1, because NCI at an intermediate level compounds and cannot be computed in one pass.

**Hyperinflationary subsidiary**: **restate the sub's financials for inflation (IAS 29) before
translation.**

**Intercompany profit in services** (not just inventory): **unrealized profit on capitalized
intercompany services** (e.g. one entity builds an asset for another) **also eliminated.**

**Deferred tax on consolidation adjustments**: eliminations and fair-value adjustments **create
temporary differences — recognize deferred tax**.

**Push-down accounting**: in some cases fair-value adjustments are pushed down to the sub's own books
(optional under US GAAP). **Affects where the adjustments live** — and therefore whether they are
already in the sub's trial balance or need adding at consolidation. Check before double-counting them.

**Functional currency reassessment**: if a sub's functional currency changes (e.g. due to changed
operations), **apply the change prospectively.**

**Goodwill in a foreign sub**: goodwill is **denominated in the sub's functional currency and
translated at the closing rate each period** (creating CTA on goodwill).

**A group member has no connected company file** — *Mosofin-specific*. Its trial balance is `[manual]`.
Name it, and never present the result as the group's consolidated financials if it is missing.

**A connected file is not part of the group** — *Mosofin-specific*. Being connected is not being in
scope. Confirm membership against the org chart; consolidating a dormant or unrelated entity is a
silent, material error.

**The wrong `data_source_id` was passed** — *Mosofin-specific, and uniquely dangerous here*. Reading
one entity while believing you read another produces a consolidation that may still balance. Label
every result with its entity as it arrives, and cross-check each entity's legal name from its profile
against the trial balance you attribute to it.

**Trial balances pulled at different dates or on different accounting methods** —
*Mosofin-specific*. The consolidation will not balance and the cause is nearly invisible. Pull all
entities identically, and state the date and method on the workpaper.

**Both sides of an intercompany balance disagree** — *Mosofin-specific opportunity*. Do not eliminate
the smaller, the larger, or the average. **Quantify the difference and investigate it in the
transactions** — the ledgers on both sides are readable. Report unresolved differences on Sheet 8
rather than forcing the elimination.

**An entity's data carries `mock: true`** — *Mosofin-specific*. Say which entity. Consolidated
statements resting partly on fixture data are not reportable.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific, and
ambiguous here*. It may mean the subsidiary was **disposed of** — which changes the consolidation scope
and requires deconsolidation accounting — or merely that a connection lapsed. **Ask which**; never
assume either.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` **for that entity** in the
coverage sheet.
