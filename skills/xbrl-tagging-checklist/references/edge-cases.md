<!-- xbrl-tagging-checklist · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section.)*

**Taxonomy version changes.** The US GAAP taxonomy is updated annually; **elements are deprecated, added and re-specified.** A tag map carried forward unchanged will eventually reference deprecated elements. **`[manual]` — and it is why the taxonomy version is a required input.**

**A component-level reference against a consolidated filing.** Every figure disagrees, and the disagreement looks like a tagging error. **Establish the basis at Gate 1.**

**Comparatives tagged from a stale figure.** The prior period's figures may have been restated — see `restatement-and-prior-period-adjustment` — in which case **the comparative tagged must be the restated one**, not what was originally filed. `[auto]` to detect the difference; `[manual]` to conclude.

**A perfectly valid instance with a wrong element.** Validation cannot see it. **This is what the independent reviewer is for**, and it is the reason Step 5's sign-off is substantive.

**Extension proliferation.** A filing where a large share of concepts are extensions is not comparable to anything. **Passes validation; defeats the purpose.** `[manual]` — count them, and compare to the prior filing.

**An unanchored extension.** Opaque to every consumer. Anchoring is the minimum mitigation.

**Sign double-inversion.** Balance type and presentation negation both invert; applied together they cancel or compound. **`[auto]` supplies the ledger's sign as ground truth.**

**Share and per-share figures.** Not monetary, and **not derivable from this surface.** The EPS consistency check is `[manual]` and depends on the cash table — flag it rather than leaving it blank.

**Dimensions that do not reconcile.** Where the dimensional analysis was built outside the accounts, it will not reconcile by construction. **A difference is then a real finding**; where dimensions are ledger-native, a difference is a tagging error. **Say which.**

**Detail tagging of notes.** Note tagging is substantially more granular than statement tagging and is where most extensions and most errors arise. **The reference schedule should cover note figures too**, not just the primary statements.

**A late change to the financials.** If a figure changes after tagging, **the instance and the document diverge silently.** This is the numbers-lock problem from `sec-10q-10k-prep`, applied to XBRL — **and `[auto]` can re-run the reference schedule at no cost immediately before filing**, which is the check that catches it.

**A filing that is not consolidated.** Rare, and worth confirming rather than assuming, since it changes the entire reference basis.
