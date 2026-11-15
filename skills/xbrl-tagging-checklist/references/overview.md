<!-- xbrl-tagging-checklist · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# XBRL Tagging Checklist (iXBRL) — Mosofin Seed

Provides a disciplined approach to XBRL tagging, review and validation for SEC filings, including governance around extensions and common error prevention.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## Be direct: this is the narrowest fit in the pack

**XBRL tagging operates on two artefacts, and Mosofin can read neither.**

| Artefact | What it is | Mosofin |
|---|---|---|
| **The filing document** | An iXBRL document — financial statements, notes and MD&A, with tags embedded | **Cannot read it.** Same boundary as `sec-10q-10k-prep`. |
| **The taxonomy** | The US GAAP taxonomy for the relevant year — thousands of elements with their balance types, period types, data types and calculation relationships | **Cannot read it.** An external published artefact. |

**So Steps 1, 2, 3 and 5 — tag selection, extensions governance, dimensional tagging and validation — are `[manual]` in substance.** Mosofin does not select an element, does not decide whether an extension is warranted, does not tag, and does not run EDGAR validation.

**Saying that plainly is more useful than manufacturing a contribution**, and it is consistent with how a valuation and `scenario-and-sensitivity-analysis` are treated here.

### What it can do, and it is genuinely useful

**Step 4 is the exception, and it is the step where tagging errors actually cause harm.**

Its four checks are about whether the tagged data is **internally consistent and agrees with the underlying figures**. The underlying figures come from the accounts — **and Mosofin holds that side exactly.**

> **The tagged document must agree with the ledger. Mosofin supplies the ledger side, computed and traceable.**

That is the same structure as `sec-10q-10k-prep`'s tie-outs: **document-to-ledger, automatic on one side, and the comparison performed by a person.**

**And one contribution the original does not mention**: **the expected calculation relationships are derivable from the chart itself.** A roll-forward's arithmetic — opening plus movements equals closing — and a subtotal's composition are structural facts about the accounts, and they are precisely what an XBRL **calculation linkbase** expresses. `[auto]` can produce the expected set and hand it to the tagger as a specification rather than leaving it to be reconstructed from the document. See Step 4b.

### Three near-substitutes

**1. A tag is not a number.** Tagging maps a value to a concept. **Whether the value is right was settled before tagging began**, by `financial-statement-builder` and the close. **An XBRL review is not a second chance to check the financials**, and treating it as one confuses two separate quality gates.

**2. Valid XBRL is not correct XBRL.** EDGAR validation checks that the instance is well-formed and internally consistent against the taxonomy's rules. **It does not check that the right element was chosen, or that the figure is right.** A filing can pass validation cleanly and be tagged with a concept that means something else entirely — which is the whole reason Steps 1 and 2 exist and why an independent reviewer signs off in Step 5.

**3. Mosofin's own figures are information produced by the entity.** Per `sox-controls-design-and-testing`'s IPE point: a schedule Mosofin produces, used as the authoritative reference for a tie-out, **is subject to the same reliability requirements as any other internally-produced report.** Record the queries and parameters so it can be re-performed.

---

## Related skills

| Skill | Relationship |
|---|---|
| `sec-10q-10k-prep` | The filing this tags, the tie-out discipline, and the numbers-lock problem applied to XBRL. |
| `financial-statement-builder` | Produces the figures being tagged — and settles their correctness before tagging begins. |
| `notes-to-financial-statements` | Note detail tagging, where most extensions and most errors arise. |
| `segment-reporting` | Segment dimensions, and the same ledger-native-or-not binary. |
| `statement-of-equity-changes` | Equity roll-forwards, which are calculation relationships. |
| `restatement-and-prior-period-adjustment` | Restated comparatives, which must be the ones tagged. |
| `sox-controls-design-and-testing` | Why a Mosofin-produced reference schedule is information produced by the entity. |
| `consolidation-and-eliminations` | Why the registrant's figures are consolidated and the gateway returns components. |
| `quarter-end-close` / `year-end-close` | The close that produces the figures, and the calendar the tagging sits on. |
