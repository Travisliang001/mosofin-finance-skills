<!-- vendor-onboarding-and-w9-tin · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Vendor Onboarding and Tax-Form Validation — Mosofin Seed

Onboards new vendors with full data capture, validates tax forms, screens against sanctions lists, and audits the vendor master for completeness. **Designed to prevent payment-fraud and tax-reporting issues downstream.**

**Jurisdiction-agnostic.** It accepts any tax form for any country — W-9 / W-8 (US), TD1 / T4A info (Canada), VAT registration certificates (EU / UK), CR / TRN (GCC), PAN / GSTIN (India), and others. **The validation rules depend on the user's stated jurisdiction and the form's stated type.**

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## Two halves, and the workspace only touches one

**Onboarding a new vendor is document work.** A W-9, a W-8BEN-E, a VAT certificate, a bank letter — **none of these are in an accounting system**, and extracting and validating them is `[manual]`, or done from uploads exactly as the original describes.

**Auditing the vendor master is ledger work**, and the original treats it almost as an afterthought — a paragraph at the end of Step 8:

> **For batch audit mode: scan the user's existing vendor master and produce a list of vendors with missing fields, expired forms, or inconsistencies.**

**That paragraph is the half a connected workspace transforms**, and it is promoted to a first-class step below (Step 0). Reading every vendor record, every payment, and every master-data change is one batched query, and it produces findings that a per-vendor onboarding process structurally cannot.

### The audit that matters is not the one people run

The obvious audit asks: **which vendor records are incomplete?** It produces a long list dominated by dormant records nobody will ever pay again, and it gets ignored.

**The useful audit asks: which incomplete records are being paid?**

> **A dormant vendor with no tax form is housekeeping. An active vendor paid heavily all year with no tax form is a reporting problem, and possibly a backup withholding problem.**

`[auto]` joins the vendor master to payment activity and **ranks by money, not by record count.** That single change turns an ignored list into a short list somebody acts on. See Step 0b.

### And the detection that matters most

Step 5 is emphatic about bank-detail changes, and it is right to be:

> **Compare against any prior bank details on file — any change requires reverification through a known contact, not the contact who submitted the change.**

**That instruction exists because of payment-redirection fraud**: a convincing email, apparently from a known supplier, asking for bank details to be updated. The details change, the next payment goes to the fraudster, and it is discovered when the real supplier chases.

**Where the system records master-data changes, `[auto]` finds the signature**: **a bank detail change, followed by a payment within days.** That is one query, it runs across the whole master, and it is the highest-value detection in this skill. See Step 0c.

### A near-substitute is not a substitute

**1. A vendor record is not a validated vendor.** A populated tax-ID field means somebody typed something. It does not mean a form was received, signed, dated, or checked. **The ledger holds the data, not the document** — so master-data completeness and documentation completeness are different questions, and only the first is readable.

**2. A TIN that passes format validation is not a verified TIN.** The original is precise about this and it is preserved: format checks confirm shape. **Matching the TIN to the name requires a lookup service, and Mosofin cannot run one.**

**3. Mosofin cannot screen, and therefore clears nobody.** No sanctions list, no PEP list, no OFAC. **The absence of a hit in Mosofin's output means no screening was performed** — not that the vendor is clear. This is stated again in Step 4 because it is the most dangerous possible misreading of this skill's output.

### A note on the data this skill handles

Vendor onboarding captures **bank account details, tax identifiers, and sometimes dates of birth or national identity documents** (W-8BEN, and edge case 10). That is sensitive personal and financial data about third parties.

**Mosofin reads what is already recorded. It does not enter, transmit, or reproduce banking or identity details anywhere outside the deliverable**, it does not carry them between workspaces, and where an analysis can be done on a masked or partial identifier — matching on the last four digits to find duplicates, for instance — **it should be.**

---

## Related skills

| Skill | Relationship |
|---|---|
| `invoice-data-extractor` | Invoice processing, explicitly out of scope. |
| `duplicate-invoice-detection` | Why duplicate vendor records defeat duplicate-invoice controls. |
| `three-way-match` | Exception 9, and the master-data change control it tests. |
| `sox-controls-design-and-testing` | Master data change control as a ledger-evidenced control, and the SoD reading of who changed and who paid. |
| `fraud-detection-and-forensics` | Payment redirection, and vendor/employee coincidences. |
| `vendor-statement-reconciliation` | What breaks when one supplier sits under two records. |
| `related-party-disclosures-asc850` | Vendor/customer overlaps and connected-entity matches. |
| `working-capital-optimization` | Terms as recorded versus terms as operated. |
| `accounts-payable-automation` | Where a validated vendor record is consumed downstream. |
