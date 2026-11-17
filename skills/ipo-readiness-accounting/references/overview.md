<!-- ipo-readiness-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# IPO Readiness — Accounting and Reporting (Mosofin)

Builds an **IPO readiness roadmap** covering **accounting, reporting, controls, audit readiness, and
disclosure requirements** for becoming a public company.

**In plain words:** a private company closes its books when it gets round to it, fixes last quarter when
someone notices, and keeps the share register in a spreadsheet. A public company has weeks-not-months
deadlines, an auditor testing its controls, and no ability to quietly correct history. This maps the
distance between the two and what it takes to cross it.

It is **workspace-scoped**: the historical financials, the close timing evidence, the manual-entry profile
and the period-integrity signals come from tool calls against a company file connected to your Mosofin
workspace in this conversation, or from something you supplied by hand and that is labelled as such.

## The readiness question the workspace can actually answer

**Most IPO readiness assessments run on self-reported information.** Somebody says the close takes five
days, the reconciliations are done monthly, and the books are clean. **The workspace can check several of
those claims directly**, and that is where it earns its place in this skill:

1. **How long the close actually takes.** **[auto]**, and **the single most valuable measurement here.**
   **Entry posting dates against the period they belong to are readable.** Not "the close takes five days"
   — **"80% of entries for the period were posted by working day 6; the last adjusting entry landed on day
   23."** **A public company files a 10-Q within 40 days of quarter end**, with review, tie-out and
   certification inside that window. **The gap between the measured close and that requirement is the
   roadmap's most important number.**
2. **How much of the close is manual.** **[auto]**: the proportion of period-end movement arriving by
   manual journal rather than through a transactional process. **A close carried by manual entries does not
   scale to a public-company cadence and does not survive ICFR testing** — every one of those entries needs
   a control, a preparer, a reviewer and evidence.
3. **How many years of comparable data exist.** **[auto]**: **an S-1 needs audited financial statements for
   multiple years**, and comparability across them matters. **Whether the system even holds consistent data
   that far back — same chart, same entity, same basis — is checkable**, and a discontinuity is a real
   problem discovered far too late in most processes.
4. **Whether closed periods stay closed.** **[auto]**, and it is an **audit-readiness signal auditors care
   about intensely**: entries posted into periods already reported, prior-period adjustments, and figures
   that have changed since they were last presented. **A company that routinely reopens history is not ready
   for an environment where history is filed with a regulator.**
5. **Where the reconciliation discipline is weak.** **[auto]**: suspense and uncategorized balances, their
   size and their age.
6. **What systems exist.** **[gated]**: Gate 1's connected list is a partial systems inventory.

**What stays firmly outside:** the cap table and every valuation, the control environment, contracts and
revenue arrangements, audit status, and every policy memo — **all `[manual]`, and all of them substantial
workstreams in their own right.**

**One thing to be clear about:** **this skill produces a roadmap, not compliance.** Nothing here makes a
company ready; it measures distance and sequences work. **And the equity workstream in particular is
largely beyond the workspace** — see `equity-compensation-accounting`, where the same wall appears.

**Mosofin is read-only.** It cannot change a process, remediate a control or file anything. Every
recommendation below is a *proposal*.
