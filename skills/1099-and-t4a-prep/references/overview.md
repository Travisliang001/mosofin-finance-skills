<!-- 1099-and-t4a-prep · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Vendor Information Return Preparation (Mosofin)

Prepares annual vendor information returns for any jurisdiction, **using the live books
connected to your Mosofin workspace** as the evidence base.

**In plain words:** once a year, most tax authorities want you to tell them how much you
paid each outside contractor, landlord, or professional you used — the people who work for
you but are not on payroll. This skill finds those people in your books, adds up what you
paid each of them, checks you have the paperwork you need on file for each one, and hands
you a filing-ready list. The formal name for this kind of filing is an **information
return** (a report you file *about someone else's* income, not your own).

This skill is **jurisdiction-agnostic** in structure but applies the **specific
jurisdiction's rules the user identifies**. It does not assume any jurisdiction's
thresholds, form codes, or due dates — it asks for them, or applies what the user has
provided.

It is **not** system-agnostic. It is **workspace-scoped**: every figure comes from a tool
call against a company file connected to your Mosofin workspace in this conversation, or
from something you supplied by hand and that is labelled as such.

**Mosofin is read-only.** Nothing here files anything, posts anything, or changes your
books. Every output is a *proposal* — a workpaper for a human to review, sign off, and
file.
