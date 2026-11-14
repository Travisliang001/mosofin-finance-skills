<!-- sox-controls-design-and-testing · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All ten preserved, in order.

**IT general controls (ITGCs)**: **access, change management and operations controls over the systems are foundational — if ITGCs are weak, automated controls and system-generated reports can't be relied upon. Scope ITGCs explicitly.** `[manual]`, entirely — **and, as the opening section says, this governs everything automated in this skill.** Mosofin reads the system; if the system's integrity is not controlled, the reads inherit that. **State the ITGC conclusion beside any reliance placed on `[auto]` testing.**

**Reliance on system-generated reports / IPE**: **information produced by the entity, used in controls, must itself be reliable. Test the completeness and accuracy of key reports, or the control over them.** **`[auto]` where the report is ledger-derived** — its completeness and accuracy can be **re-derived independently**, which is exactly what IPE testing asks for, and re-performance is the strongest method available.

**And an honest point that follows: Mosofin's own output is IPE.** A schedule this skill produces, used in a control, is information produced by the entity and is subject to the same requirement. **It does not get a free pass for having been generated automatically** — its completeness and accuracy depend on the reads behind it, which depend on the ITGCs. Record the queries and parameters so it can be re-performed.

**Management review controls (MRCs)**: **common but hard to test — the rigour of the review, the precision, and the follow-up on exceptions matter. Document the review criteria and evidence of investigation, not just a sign-off.** `[manual]` for the review; **`[auto]` for the follow-up**, per Step 6b — the strongest partial contribution available on the hardest control type.

**Segregation of duties in small entities**: **small teams often can't fully segregate duties. Identify compensating controls — owner review, for instance — and flag residual risk honestly.** `[auto]` to find the conflicts; `[manual]` for the compensating controls. **"Honestly" is the operative word**: full-population SoD testing in a four-person team will produce a long list, and the list is a fact about team size. **Report it as residual risk with compensating controls, not as a catalogue of failures**, or the analysis will be dismissed wholesale — and the two or three conflicts that genuinely matter will be dismissed with it.

**Automated controls**: **test once plus ITGC reliance — if the system and change management are controlled, an automated control that worked once is likely consistent — but only if ITGCs are effective.** `[manual]` for the reliance conclusion. **Note the tension worth naming**: this benchmark exists because testing every instance was impractical. **Where full-population testing is available, test it in full** — it is cheap, and it does not depend on the ITGC inference.

**Entity-level controls**: **tone at the top, governance and monitoring controls operate above processes and can affect the extent of process-level testing.** **`[manual]`, entirely.** Nothing about tone at the top is in a ledger, and this is the category where automation contributes least.

**Deficiency aggregation**: **individually minor deficiencies can aggregate to a significant deficiency or material weakness. Evaluate in combination, not just individually.** **`[auto]` for the arithmetic** — and it is arithmetic people reliably skip.

**Material weakness conclusion**: **major consequences — disclosure, market reaction for public companies. The evaluation must be rigorous and well-supported; involve the right governance.** **`[manual]`.** Mosofin quantifies and stops.

**Rollforward to year-end**: **controls tested at an interim date need a roll-forward to cover the remaining period to year-end.** **`[auto]` for ledger-evidenced controls — the roll-forward is the same query extended to year-end**, at no marginal cost. This is normally a second round of sample testing, and it disappears entirely for the automated subset.

**Outsourced processes (service organisations)**: **reliance on a service organisation's controls — via a SOC 1 report — and complementary user entity controls. Map these.** **`[manual]`.** A SOC 1 report is a document, and the service organisation's systems are outside the workspace entirely. `[auto]` for one thing: **whether the complementary user entity controls, the ones the entity itself must operate, actually operate** — those are on this side and several of them are ledger-evidenced.
