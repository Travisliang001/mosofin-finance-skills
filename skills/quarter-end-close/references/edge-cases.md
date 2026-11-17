<!-- quarter-end-close · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All ten preserved, in order, each with the verdict and whatever the workspace adds.

**Quarter ends mid-week**: the cutoff is still the last calendar day; close work happens on the following business days. `[auto]` — and use it: read for transactions **dated** within the quarter but **entered** after it, which is the exact population that a mid-week quarter end creates. A few are proper (accruals). A pattern of them, particularly revenue, is a cutoff problem. See `revenue-cutoff-testing`.

**Mid-quarter material event** (acquisition, divestiture, major financing, restatement): may require additional disclosures or pro-forma data. `[manual]` to identify — none of these announce themselves in a ledger as what they are. `[auto]` for one weak signal: an unusually large single transaction, or a new account appearing in the chart mid-quarter, is worth asking about.

**Significant change in estimate** (an upward revision of a contingent liability, say): catch-up adjustment in the current quarter; consider disclosure as a change in estimate. `[auto]` to detect via the rate trend on Sheet 3, `[manual]` to judge. **Prospective, not retrospective** — a change in estimate is not an error and must not be handled as one. See a restatement review for the distinction, which matters enormously and is frequently got wrong.

**Auditor identifies a control deficiency during interim review**: document, propose remediation, and consider whether it rises to a material weakness requiring disclosure. `[manual]` throughout. See `sox-controls-design-and-testing`.

**First or last quarter of a fiscal year**: Q1 has a fresh budget; Q4 transitions into year-end procedures. **Use `year-end-close` for Q4, not this skill.** `[auto]` to determine which quarter it is from the fiscal calendar — and this matters, because the answer routes to a different skill. Check the fiscal year end before assuming a calendar one.

**Acquired entity in the current quarter**: integration, opening balance fair-value accounting, first reporting this quarter. `[manual]` — the purchase price allocation needs valuations that are not on this surface. Hand off to the business combination accounting. `[auto]` for one thing: whether the acquired entity is a separately connected company file, which determines whether its numbers can be read at all.

**Discontinued operations**: separate presentation on the P&L; specific tests for held-for-sale classification. `[manual]` for the classification decision. `[auto]` for the presentation **if** the discontinued component is a dimension in the book; if it is not, separating it is a manual exercise and will not tie without care.

**Adoption of a new accounting standard mid-year**: normally applied from the start of the fiscal year, though the quarterly reporting may show the transition impact. `[manual]`. `[auto]` for one supporting read: whether a transition adjustment was actually posted to opening equity, and for how much.

**Foreign-currency reporting**: the cumulative translation adjustment is updated at each period end; the cash flow statement uses period-average rates for activity. `[auto]` for the mechanics — and carry across the warning from the foreign currency translation work: **CTA is a plug, so a wrong rate does not fail to balance. It lands in CTA.** Prove CTA independently rather than trusting that the statements balanced. See also `multicurrency-fx-revaluation`.

**Restatement triggered by quarterly close findings**: assess materiality; if material, restate the prior periods. `[manual]` for the decision — it is a judgment with legal and market consequences. `[auto]` for the quantification, and Step 5's reopened-period test is frequently how this gets discovered in the first place. Hand off to a restatement review.
