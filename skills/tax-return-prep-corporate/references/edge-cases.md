<!-- tax-return-prep-corporate · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All eleven preserved, in order.

**Multi-jurisdiction filing**: **separate computations per jurisdiction; the entity may file in several. Foreign income, foreign tax credits and treaty positions add complexity — flag for specialist.** `[manual]`. `[auto]` for one fact that establishes the question exists: **whether the books show foreign income, foreign currency transactions or foreign withholding.**

**Interest deductibility limitations**: **many jurisdictions cap interest deductions — a percentage-of-EBITDA limitation, for instance. Disallowed interest may carry forward. Confirm current rules.** **`[auto]` for both inputs** — interest expense and EBITDA — `[manual]` for the percentage. **And the carryforward makes disallowed interest a tax attribute**, tracked alongside losses.

**Loss restriction rules**: **carried-forward losses may be capped — only able to offset a percentage of profits above an allowance — and ownership changes can forfeit losses. Confirm.** `[manual]`. **Ownership changes are not in the ledger** — no cap table on this surface — and this is a case where a change the accountant did not hear about can invalidate a large attribute.

**Capital versus revenue distinction**: **gains and expenses may be capital — different treatment and rate — versus revenue. Misclassification changes the tax materially.** `[manual]` to judge; **`[auto]` to surface the candidates** — Step 2b sweeps for expensed items that may be capital and capitalised items that may be deductible, which is exactly this boundary. **Legal and professional fees are the usual battleground.**

**Group taxation**: **consolidated or group filing, group relief, and intra-group transactions have special rules. Transfer pricing applies to related-party dealings.** `[manual]`; `[auto]` where entities are connected. See Gate 1.

**Transfer pricing adjustments**: **related-party transactions must be at arm's length; adjustments may be needed for the computation.** `[manual]`. **`[auto]` to surface the transactions** where both parties are connected — and note from `related-party-disclosures-asc850` that arm's length can be **partly evidenced** by comparing terms given to related and unrelated parties for the same thing.

**Tax depreciation versus book**: **these almost always differ, creating the largest temporary difference. Keep the schedules separate and reconcile.** `[auto]` for the book side; `[manual]` for the tax side. **Two registers, in parallel, for the life of every asset.**

**Anti-avoidance / minimum tax regimes**: **alternative minimum taxes, global minimum tax (Pillar Two), and general anti-avoidance rules may apply. Flag for specialist.** `[manual]`, entirely. **Pillar Two in particular is a group-level regime with its own data requirements** that a single entity's ledger does not contain.

**Elections and claims with deadlines**: **many reliefs require a formal election or claim by a deadline. Track and flag.** `[manual]`. **This is the highest-consequence `[manual]` in the skill**: a relief the entity was entitled to, missed because a deadline passed, is simply gone — and nothing in the accounts will ever mention it. **Persist the elections list**; see the lifecycle section.

**Return-to-provision differences**: **the filed return will differ from the estimated provision; reconcile and feed the true-up back to `corporate-tax-provision-asc740`.** **`[auto]` for both sides.** **Expected, not an error** — the third near-substitute.

**Complex or high-value returns**: **this skill organises the computation but is not a substitute for a qualified local tax preparer. Always recommend professional review for filing, especially across jurisdictions or with complex positions.** **`[manual]`, and it goes on every sheet.**
