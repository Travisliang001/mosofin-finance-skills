<!-- sec-10q-10k-prep · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# SEC 10-Q / 10-K Preparation — Mosofin Seed

Builds an external reporting process for SEC filings, focused on completeness, tie-outs, disclosure readiness, and a controlled drafting and review workflow.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The structural fact that shapes this skill

> **For an SEC filer, the authoritative financial statements are the ones in the filing document. Not the ones in the accounting system.**

That sounds obvious and its consequences are not.

In every other skill in this pack, the financial statements *are* what the ledger produces. Here they are a **separate artefact** — a document assembled in Word or a dedicated reporting tool, tagged for XBRL, filed on EDGAR, and signed. The ledger is its **source**, not its embodiment.

Three consequences run through everything below:

**1. A tie-out is document-to-ledger, not ledger-to-ledger.** Mosofin can supply, exactly, what the books say. **It cannot read the draft 10-Q.** So every tie-out in Step 2 is automatic on one side and manual on the other, and a "tie-out" that reads the ledger twice has verified nothing about the filing. This is the same trap as `financial-statement-builder`'s balancing balance sheet, in a setting where the stakes are considerably higher.

**2. The document can drift from the ledger while it is being drafted.** Step 4 says *lock numbers before final drafting* — which is a control, and controls can fail. **Whether the ledger actually stayed still during the drafting window is testable**, and it is one query. See Step 4b.

**3. What was filed last time is not what the ledger now says about last time.** If anyone has posted into a closed period since the last filing, this quarter's comparatives will not match the comparatives already on file. For a private company that is untidy. **For a filer it is a disclosure event.** See `restatement-and-prior-period-adjustment`, which runs the same test as its primary detection.

### What Mosofin cannot verify, stated before anything else

**The most scrutinised number in the filing is one this skill cannot check.**

Step 2's fifth tie-out is *shares and EPS to the cap table*. **There is no cap table on this surface.** Share counts, weighted average shares, options and their dilutive effect, warrants, convertibles — none of it is in a general ledger. This absence is consistent across the pack (the equity compensation accounting, `financial-statement-builder`, an IPO readiness review, `quarter-end-close`, `restatement-and-prior-period-adjustment`), but it lands hardest here, because **EPS is the number the market reads first.**

Say so on the tie-out sheet rather than leaving an unticked box that looks like an oversight. It is not an oversight; it is a boundary.

**Also entirely off this surface**: legal review, auditor review, the DCP certifications, the reviewer matrix, filer status, and every deadline that follows from it.

---

## Related skills

| Skill | Relationship |
|---|---|
| `quarter-end-close` | The close beneath the 10-Q — and the source of the preliminary analytics and estimates review. |
| `year-end-close` | Q4 and the 10-K. There is no fourth 10-Q. |
| `month-end-close-checklist` | Whether Day 0 has actually happened. |
| `financial-statement-builder` | The statements the filing document carries — and why a balancing balance sheet proves only arithmetic. |
| `notes-to-financial-statements` | Footnote figures and their supporting schedules. |
| `management-discussion-and-analysis` | The MD&A tie-out, and the rule against forward-looking statements. |
| `restatement-and-prior-period-adjustment` | Where Step 2b's comparatives difference goes when it is material. |
| `sox-controls-design-and-testing` | DCP and ICFR evidence. |
| `internal-audit-workpaper` | Why a population read is not a control test. |
| `segment-reporting` | The segment note and its reconciliation to the consolidated total. |
| `related-party-disclosures-asc850` | The related-party disclosure and the limits of a name match. |
| `subsequent-events-asc855` | Type 1 and Type 2 classification through to the filing date. |
| `xbrl-tagging-checklist` | Tagging the filed document. |
| `consolidation-and-eliminations` | Why the registrant is a consolidated entity and the gateway hands you components. |
