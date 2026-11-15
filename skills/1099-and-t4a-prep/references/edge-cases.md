<!-- 1099-and-t4a-prep · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Vendor refuses to provide a tax form**: in jurisdictions that require it, the entity may
need to apply backup withholding on future payments, or withhold prior payments out of
remaining balances. Flag it.

**Vendor changed name / TIN mid-year**: use the latest valid combination at year-end if both
apply to the same payment relationship, but flag for review — sometimes two separate vendor
records are needed. In the books this often shows up as two vendor rows, not one; check for
duplicates before assuming one changed.

**Vendor was on file as non-corp but is actually incorporated**: re-classify and re-determine
reportability. A corrected return for prior years may be needed.

**Mixed-type payments to one vendor**: e.g. one contractor receives a $5,000 service fee plus
$2,000 reimbursing expenses they paid on your behalf. Reimbursements documented as expense
reports with receipts are typically not reportable; service fees are. Allocate carefully.

**Payments made via a third-party processor** (PayPal, a card processor): the processor often
files its own 1099-K, and you should not also report those payments on a 1099-NEC — the
vendor would be reported twice. Confirm per current rules. In a workspace where a payment
processor is *also* connected as a datasource, you can see both sides — say clearly which
payments came from which platform, and do not double-count a payment that appears in both.

**Below threshold but voluntarily reported**: allowed; just include it and note that it was
voluntary.

**Cross-border vendors**: the home-country form (1099) may not apply; a non-resident
withholding return may apply instead (1042-S in the US, NR4 in Canada, etc.). Confirm the
jurisdiction and the form type with the user.

**Foreign currency payments**: convert per the jurisdiction's rule — a specific date's rate
or an annual average. Record which rule and which rates were used.

**Refunds / credits received from vendors**: net them against payments to that vendor in the
same year (*`search_vendor_credits`*). Do not show a negative on the return unless the
jurisdiction permits it.

**Corrected returns** (a prior year needs amending): produce it per the jurisdiction's
corrected-return process — e.g. a US Form 1099 with the "CORRECTED" box ticked.

**Multiple entities filing under one EIN**: aggregate properly — the tax authority sees a
single filer. This is the one case where a multi-entity run genuinely **consolidates** rather
than compares, and thresholds apply to the aggregate, not per company file. Confirm the
shared tax ID with the user explicitly before aggregating; getting this backwards produces
either duplicate returns or missing ones.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and
say what is therefore missing from the return. If a `reconnect_url` is offered, surface it.
Do not silently produce a return that looks complete.

**The tool that lists vendor payments is `disabled` in this workspace** — *Mosofin-specific*.
Do not substitute a vendor *balance* report: a balance shows what is still owed, while an
information return needs what was actually paid. Mark the task `[manual]`, name the tool,
and ask the user for a payment export.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data can demonstrate
the workpaper's shape but cannot support a filing. Say so at the top of the deliverable and
do not describe the return as filing-ready.

**The same vendor appears in several connected company files** — *Mosofin-specific*. Report
per filer unless the entities share one tax ID. Show the vendor once per entity, labelled,
plus an aggregate line clearly marked as informational only.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*.
Flag it to the user. Never apply it to a different entity, and never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke the
same tool with `approved=true` (**reads only — never for a write**) after an explicit yes, and record in the coverage sheet that
the task was `[gated]` rather than `[auto]`.
