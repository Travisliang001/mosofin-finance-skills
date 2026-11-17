<!-- fraud-detection-and-forensics · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Objectivity is paramount**: **an indicator is not proof. Many red flags have innocent explanations.
Document objectively; never accuse an individual. Presumption of innocence and due process matter.**

**Evidence preservation**: **improper handling can destroy evidence or its admissibility. Don't alter
originals; preserve metadata and chain of custody. Involve professionals early.**

**Tipping off**: **premature confrontation can lead to destroyed evidence or legal complications.
Coordinate timing with counsel.** *Mosofin note*: **a `permission` approval prompt is a form of contact.**
Agree the approver in advance.

**Legal counsel and privilege**: **investigations often proceed under legal privilege. Engage counsel early;
the analysis may need to be directed by counsel.**

**Benford's Law limits**: **applies to naturally-occurring, wide-ranging data; not to assigned numbers,
capped ranges, or small samples. A deviation is a screen, not evidence — don't over-rely.** *Mosofin note*:
because the full ledger is one call away, it is easy to run Benford's on an unsuitable population. **Report
the population and its size with every result.**

**False positives**: **aggressive screening flags many legitimate items** — a vendor sharing an address with
an employee may be a legitimate related party. **Investigate before concluding.** *Mosofin note*: **the ease
of running wide screens raises the false-positive count, not the precision.**

**Management override / collusion**: **the hardest fraud to detect — controls assume no collusion. Senior
management fraud can defeat normal controls; requires governance-level skepticism.**

**Whistleblower information**: **tips are the most common fraud detection source. Handle confidentially and
per policy; protect the whistleblower.** Note what this implies about analytics: **the most productive
detection method is not a query.**

**Small entities**: **limited segregation makes fraud easier and detection harder. Compensating controls —
owner oversight — and external review matter.**

**Regulatory / reporting obligations**: **substantiated fraud may trigger reporting obligations —
regulators, insurers, law enforcement. Flag for counsel — don't advise on the legal obligations directly.**

**Scope discipline**: **this skill assists analysis and structuring. It does not replace qualified forensic
investigators or legal counsel, and it does not render legal conclusions about guilt.**

**A test could not run and the result looks clean** — *Mosofin-specific, and the most misleading outcome
available here*. **Bank-account matching, payroll register tests and corruption indicators are all
unavailable.** Sheet 9 exists so that a clean Sheet 3 is never read as full coverage.

**A tool result is treated as preserved evidence** — *Mosofin-specific*. It has no chain of custody. It is
analysis.

**A user name on a transaction is treated as the person** — *Mosofin-specific*. Shared logins, delegated
access and system-generated entries all break that link.

**Quantifying a loss from indicators alone** — *emphasis on the original's own precondition*.
Quantification follows substantiation by investigators. A number attached to an unsubstantiated indicator
reads as an accusation.

**A red-flag list is circulated widely** — *Mosofin-specific*. It names people who have not done anything
wrong. Confirm recipients before producing it.

**Findings are carried forward to the next run** — *Mosofin-specific, and prohibited*. An unrebutted
suspicion that persists across engagements becomes a permanent mark on someone who was never told. **Persist
the method; never the results.**

**Inferring pressure or motive from the data** — *Mosofin-specific*. The workspace shows opportunity. It
shows nothing about anyone's circumstances, and guessing at them is not analysis.

**A cross-entity scheme is invisible entity by entity** — *Mosofin-specific*. Same vendor, same individual,
same invoice across two company files. Only a multi-entity comparison finds it.

**A company file is connected but not active** — *Mosofin-specific*. **In this skill the unseen entity is
where a scheme would be safest.** Say so; do not report clean.

**A result comes back with `mock: true`** — *Mosofin-specific*. **Fictional anomalies about real-sounding
names.** Stop.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's thresholds or cleared-exception rules to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask **the pre-agreed approver** in chat,
re-invoke with `approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage
sheet.
