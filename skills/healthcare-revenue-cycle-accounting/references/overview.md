<!-- healthcare-revenue-cycle-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Healthcare Revenue Cycle Accounting (Mosofin)

Builds a **healthcare revenue cycle accounting workflow** that ties **clinical / billing system activity to
the GL and financial statements**, including **estimation of contractual allowances and reserves**.

**In plain words:** a healthcare provider bills a list price almost nobody pays. Insurers pay contracted
rates, patients pay a share, some claims are refused, and some bills were never going to be collected at
all. The accounting job is to work out what the care actually earned, hold the right reserves against what
will not arrive, and prove that the billing system and the general ledger tell the same story.

It is **workspace-scoped**: the general ledger AR, the revenue and contra revenue accounts, the cash
receipts and the realization history come from tool calls against a company file connected to your Mosofin
workspace in this conversation, or from something you supplied by hand and that is labelled as such.

## Protected health information — read first

**Healthcare data about identifiable individuals is protected health information (PHI)**, subject to legal
protections that ordinary financial data is not. **A connected accounting system in a healthcare setting
frequently contains patient names as customers**, and patient-level AR detail alongside them.

**Rules for this skill, without exception:**

- **Work at the aggregate level wherever the task allows** — by payer, by payer class, by service line, by
  aging bucket. **Nearly every step below is an aggregate question**, and the few that are not should be
  answered by count rather than by name.
- **Never reproduce patient names, account numbers, dates of service tied to an individual, diagnoses or
  any clinical detail** in a workpaper, a summary, or a message.
- **Never persist any patient identifier** — not in a skill bundle, not in a preference file, not in a note
  for next time. See Step 7.
- **If a task genuinely requires patient-level detail**, say so and let a person work in the source system
  under its own access controls. **The convenience of having it in the conversation is not a reason to
  bring it there.**

This is stricter than the pack's general privacy discipline, and deliberately so.

## The two-systems problem

**The revenue cycle does not live in the general ledger.** Charges, claims, adjudications, remittance
detail, denial reason codes and patient responsibility all live in a **clinical or billing system** — and
that is not an accounting datasource. The GL receives a **summarised result**.

**So the deliverable of this skill is the bridge between the two, and Mosofin owns exactly one end of it.**

**What the workspace gives you, precisely:**

1. **The GL side of every tie-out.** AR balances, revenue, contra revenue, cash. **Step 3 is half `[auto]`
   by construction**, and it is the step that matters most at close.
2. **The historical realization rate — the empirical anchor for the largest estimate in the skill.**
   **[auto]**: where gross charges and contractual adjustments are posted to separate accounts, **net
   revenue divided by gross charges, by period, is a direct read.** That is the realization the contractual
   allowance estimate should be tested against, and it is the difference between an estimate anchored in
   this provider's actual experience and one anchored in assertion.
3. **Cash received, and unapplied cash.** **[auto]**, and unapplied cash is both a reconciling item and a
   revenue-cycle failure worth surfacing.
4. **Adjustment and denial *amounts* over time**, where they are posted to identifiable accounts — enough
   to trend, though **not enough to explain**, since reason codes stay in the billing system.
5. **Payer mix by revenue**, where payers are set up as customers or classes.

**What stays outside:** the billing system in its entirety, **payer contracts and fee schedules**, denial
reason codes and appeal outcomes, charity care eligibility determinations, and the clinical record.

**And the central domain warning: gross charges are not revenue.** The chargemaster rate is a list price
that essentially no payer pays. **Reporting gross charges as revenue is the classic healthcare
misstatement**, and under the revenue standard the difference is not merely an allowance — it is an
**implicit price concession** measured in arriving at the transaction price.

**Mosofin is read-only.** It cannot post an adjustment, a reserve or a write-off. Every entry below is a
*proposal*.
