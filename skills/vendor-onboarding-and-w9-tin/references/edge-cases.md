<!-- vendor-onboarding-and-w9-tin · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All ten preserved, in order.

**Vendor refuses to provide a tax form** (US): **the entity may need to apply backup withholding on payments. Flag.** `[manual]` for the withholding; **`[auto]` to identify the population** — vendors paid with no form on file, ranked by amount, which is Step 0b.

**Sole proprietor using SSN versus EIN**: **both are valid TINs for 1099 purposes — capture whichever is on the form.** `[manual]`. **Do not "correct" one to the other.**

**LLC tax classification**: **a US LLC can be taxed as disregarded, partnership, S-corp or C-corp. The W-9 must specify. C-corp / S-corp = generally not 1099-reportable; others are. Capture the classification; do not assume.** `[manual]`. **`[auto]` for one audit**: LLC vendors in the master **with no tax classification recorded** — because "LLC" alone does not determine reportability, and a master full of unclassified LLCs is a year-end problem waiting.

**Vendor changes legal name or TIN mid-relationship**: **treat as a new vendor record, link to the old via a "successor of" field. Do not just edit the old record — it breaks the audit trail.** `[manual]`. **`[auto]` to detect** where change history exists — a name or TIN change on an existing record is exactly the edit this edge case forbids, and finding it retrospectively is worth doing.

**Multiple remit-to addresses for one vendor**: **capture as separate remit-to children of the same vendor parent. Different bank details per remit-to.** `[manual]`. **Note the interaction with Step 0d**: legitimate remit-to children will look like duplicates on a name match. **Distinguish them, or the duplicate report will be dismissed as noise.**

**Vendor is in a sanctioned country or under sanctions**: **hard stop. Do not onboard. Escalate to legal and compliance.** **`[manual]` — and Mosofin cannot determine this, because it cannot screen.** The hard stop is preserved at full strength; **what Mosofin contributes is the country field and nothing more.**

**Vendor's name on bank account differs from legal name** — a DBA on the account: **require explanation. Common but worth verifying with the vendor directly through a known channel.** `[manual]` — **and "through a known channel" is the same discipline as Step 5's third point.**

**Vendor is also a customer** — intercompany or reciprocal: **cross-link the records.** **`[auto]` to detect — Step 0e.**

**One-time payee** — a one-off honorarium, prize or refund: **minimum capture (name, address, TIN if required for tax reporting); full onboarding not always warranted, per the user's policy.** `[manual]`. **`[auto]` for the risk**: a "one-time" payee who has now been paid eleven times. **The policy exemption was for a single payment**, and recurring use of it is how vendors end up permanently undocumented.

**Vendor in a jurisdiction with no formal tax ID**: **capture passport or national ID per the user's policy; flag for compliance review.** `[manual]` — **and per the data note, this is identity documentation and should be handled accordingly**, not transcribed into a general working file.
