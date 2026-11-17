<!-- audit-prep-pbc-list · overview.md · read for: background — what the books can prepare for an audit and what only people can supply. Edit here, not in SKILL.md. -->

# Audit Preparation / PBC List (Mosofin)

Builds and manages the audit-preparation process — the **PBC (prepared-by-client) list** of
schedules and evidence the auditors will request, organized by financial statement area, with
status tracking. Helps an entity prepare complete, **tie-out-ready** support so the audit runs
smoothly and efficiently.

**In plain words:** before an audit, the auditors send a long list of things they want you to
prepare and hand over — reconciliations, schedules, contracts, minutes. That list is the
**PBC list** ("prepared by client"). This skill builds that list, works out which items you
can already produce and which you cannot, assigns each one an owner and a date, and gets you
ready before the auditors arrive rather than during.

This skill is **framework- and audit-standard-aware** in structure — the specific procedures
are the *auditor's*; this skill prepares the *client* side — and **chart-of-accounts-agnostic**.

It is **workspace-scoped**: every balance, schedule and account name comes from a tool call
against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

**Two structural points, stated up front, because they shape every verdict below.**

1. **Mosofin can produce many of the *schedules*, but almost none of the *documents*.** A trial
   balance, an aging, a general ledger extract, revenue by month, a balance roll-forward — all
   readable. Bank statements, signed contracts, board minutes, debt agreements, physical count
   sheets, vendor statements, engagement letters, prior-year management letters — none of them
   are in an accounting datasource. Expect a PBC list that is roughly **half `[auto]` schedules
   and half `[manual]` documents**, and say so plainly. That split is itself useful planning
   information.
2. **A figure quoted in a chat is not audit evidence.** Auditors need support that is
   reproducible and traceable. Every schedule this skill produces must record **which tool
   produced it, with which parameters, as of when** — that provenance is what makes it
   defensible when the auditor asks where the number came from. And a schedule carrying
   `mock: true` fixture data must **never** be given to an auditor.

**Mosofin is read-only.** It cannot prepare a reconciliation into the books, sign anything,
respond to a confirmation, or deliver a file to an auditor. Everything below is a *proposal or
a schedule* for a human to review, approve, and hand over.
