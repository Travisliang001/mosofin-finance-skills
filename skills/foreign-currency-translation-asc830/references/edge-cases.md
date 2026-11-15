<!-- foreign-currency-translation-asc830 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain,
including the hyperinflation topic promised in the original's description but absent from its body, and
from the workspace model.

**Hyperinflationary economies** — *promised in the original's description, not covered in its workflow, so
carried in here*. Under **IAS 29** the subsidiary's statements are **restated for inflation using a general
price index before translation**, then translated at the **closing rate** — including the income statement,
not the average rate. **US GAAP (ASC 830) takes a different route entirely**: the functional currency of an
entity in a highly inflationary economy is **deemed to be the reporting currency**, so the entity is
**remeasured** rather than translated, with differences in **earnings** rather than CTA. **The two
frameworks diverge sharply, and the identification of an economy as hyperinflationary is `[manual]`.** Never
translate a hyperinflationary entity by the normal method.

**Home currency and functional currency disagree** — *and the Mosofin surface makes this visible*. Raise it
before proceeding; every rate applied downstream depends on it.

**The average rate misstates a seasonal result** — earnings concentrated in months when the rate was far
from average. Use a weighted average or translate monthly, and say which.

**Equity translated at closing rather than historical** — a classic error that lands entirely in CTA and is
undetectable without the Step 3b proof.

**Deferred revenue or prepayments classified as monetary** — they are **nonmonetary**. A common
misclassification because they sit among current assets and liabilities.

**An intercompany loan's designation is never documented** — settlement or net investment decides whether
the FX difference hits profit. **Ask; do not infer from the account name.**

**Intercompany balances disagree before translation** — a genuine reconciliation break. **Fix it first.**
Translating a broken balance produces a difference nobody can attribute.

**CTA has never moved despite years of rate movement** — *Mosofin-specific*. Translation is probably not
happening at all; the group may be consolidated at a single rate.

**The translated balance sheet balances, so it is assumed correct** — *Mosofin-specific, and the central
trap*. **CTA absorbed the error.** Only the independent proof detects it.

**A rate is used with no source or date** — treat exactly as an unsupported figure. **Every rate carries a
source, a type, a date and an approver.**

**A rate is applied in the wrong direction** — multiplying where you should divide. It balances. It lands in
CTA. The Step 3b proof catches it; nothing else will.

**An account is not classified and silently defaults to a rate** — *Mosofin-specific completeness check*.
Every account in every trial balance must be classified explicitly.

**A subsidiary is disconnected** — *Mosofin-specific*, **and a stop condition here**. Its absence does not
produce an out-of-balance; CTA absorbs it. Say which entities were translated and which were not.

**A result comes back with `mock: true` for one entity** — *Mosofin-specific*. The group balance sheet will
balance perfectly and mean nothing. Report it per entity.

**Consolidating first and translating the total** — wrong whenever entities have different functional
currencies. **Translate each entity, then consolidate.**

**Eliminating intercompany before translating** — removes the very differences that reveal a wrong rate.
**Translate first, then eliminate.**

**A partly owned foreign subsidiary** — **CTA is split between the group and the non-controlling interest**
in proportion to net assets. Easy to forget, and it misstates both equity lines.

**A chain of foreign subsidiaries** — translation happens at each level, through each intermediate
functional currency. Do not shortcut straight to the group currency.

**A stored rate is reused** — *Mosofin-specific*. Rates are state. **Persist the source and the policy;
never the rates.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it and stop.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet, **naming the
entity**.
