<!-- related-party-disclosures-asc850 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Related-Party Disclosures (ASC 850 / IAS 24) — Mosofin Seed

Identifies related parties, catalogues related-party transactions and balances, and prepares complete and accurate disclosures.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The shape of this skill, stated once

A related-party disclosure has two halves, and a live ledger is useless for one of them and unusually good at the other.

**Half one — who is a related party.** Entities under common control, significant shareholders, key management personnel, close family members, directors and their businesses.

**None of this is in an accounting system.** There is no field for "director." There is no cap table, no register of members, no list of who is married to whom. This absence is consistent across the pack, `financial-statement-builder`, an IPO readiness review, `quarter-end-close`. The universe comes from the org chart, the cap table, the statutory registers and the board minutes, and it is `[manual]` in full.

**Half two — completeness.** Given a list of names, has anything been transacted with any of them, anywhere in the books, that has not been picked up?

**This is where the workspace changes the work materially.** The original's Step 2 asks for a scan. A connected ledger does not scan — it reads **the entire population**: every vendor, every customer, every transaction. Two of the four completeness procedures stop being sampling exercises and become exhaustive matches, at no extra cost.

### A near-substitute is not a substitute

And now the limit, which has to sit immediately next to that claim because the claim is seductive.

> **A name match is not a completeness procedure.**

The match is exhaustive over **transactions**. The thing being searched for is **relationships**. Those are different populations, and only the first one is in the ledger.

Matching a director named Okonkwo against the vendor master reliably finds "Okonkwo Consulting Ltd." It does **not** find:

- the director's spouse's company, trading under a different surname
- a company named after a street, a pet, or a Latin word
- an entity where the director's interest is held through a nominee or a trust
- a supplier who is a related party because of a relationship nobody mentioned

**So the absence of a match is not evidence of absence.** A completeness procedure that returns nothing has told you that nothing matched the names you already had — which is a statement about your input list, not about the client's affairs.

This is the same distinction `internal-audit-workpaper` draws about full-population testing: testing every transaction is genuinely stronger than sampling, **and it still cannot prove completeness**, because completeness is a claim about what is missing. Present the match as what it is: strong evidence in one direction, none at all in the other.

---

## Related skills

| Skill | Relationship |
|---|---|
| `intercompany-reconciliation` | Reading both sides of a transaction between connected entities — and the disclosure risk when only one side recorded it. |
| `consolidation-and-eliminations` | Where intercompany trading recorded as third-party trading becomes an elimination problem too. |
| `notes-to-financial-statements` | The destination for Sheet 4. |
| `quarter-end-close` | Where Step 5's quarterly refresh belongs as a recurring task. |
| `fraud-detection-and-forensics` | Undisclosed related parties are a standard fraud pattern; the detections in Step 2 overlap. |
| `internal-audit-workpaper` | Why full-population testing is stronger than sampling and still cannot prove completeness. |
| `journal-entry-review` | Related-party entries posted by journal rather than through the sales or purchase ledger. |
| `recurring-transaction-builder` | Detects a recurring counterparty matching a connected entity — the same flag from the other direction. |
