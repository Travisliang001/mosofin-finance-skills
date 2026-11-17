<!-- payroll-tax-filings · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Payroll Tax Filings (Mosofin)

Organizes and prepares **payroll tax filings and remittances** — periodic withholding and contribution
remittances, periodic returns, and year-end wage statements and reconciliations. **Ensures the figures tie
to the payroll records and the GL, and that deadlines and deposit schedules are met.**

**In plain words:** money deducted from people's pay belongs to a tax authority, and so does an employer
contribution on top. It has to be paid over on a set timetable and reported on set forms. Getting the
timetable or the amount wrong costs penalties, and in many places the people running the business are
personally on the hook for it.

## The rule that governs this entire skill

**This skill is jurisdiction-agnostic in structure and does NOT hardcode rates, wage-base ceilings, deposit
schedules, forms, or deadlines** — these vary by jurisdiction and year and are **confirmed against current
official sources.** **Payroll tax errors carry penalties; this skill organizes and reconciles, and flags
where local rules must be confirmed and professional review obtained.**

**In a Mosofin workspace that rule becomes sharper, not softer:**

> **None of those values exist on this surface.** **There is no rate table, no wage-base ceiling, no deposit
> schedule, no form and no deadline in any accounting datasource.** They come from the tax authority, and
> **they change every year.**
>
> **So every one of them is `[manual]`, with its source and its year recorded.** **Never supply a payroll
> tax rate, a threshold, a filing deadline or a deposit frequency from memory** — not as a default, not as
> an illustration, not as "typically". **A remembered rate applied to a real payroll produces a real
> underpayment with real penalties.**
>
> **This is the strictest instance in the pack of a rule that applies across it**, and it applies to the
> *deposit schedule* as much as to the rates: **an employer's required frequency changes with its size and
> history**, and last year's schedule used this year causes late deposits.

**What the workspace does contribute — and it is the half that matters operationally:**

1. **Both sides of the deposit reconciliation.** **[auto]**: **the liability balance from the GL** and
   **the deposits actually made from the payment records**, by payee and date. **Step 4 is the one step
   here that is substantially automatic.**
2. **Timeliness, given the due dates.** **[auto]** once dates are supplied: **payment dates are exact**, so
   **"deposited three days late" is a fact rather than an impression.**
3. **The GL leg of the year-end three-way tie.** **[auto]**, immediately available.
4. **Registration gaps, partially.** **[gated]**: **payments to a tax authority the entity has no liability
   accounts for**, or **liability accounts with no corresponding payments**, both point at obligations that
   may not be properly set up.

**And the distinction that matters most with a third-party provider:**

> **The payment leaving the company is `[auto]`. The deposit reaching the authority is not.** **A provider
> can take the money and fail to remit it**, and **the accounts will look perfectly settled while the
> liability is unpaid and penalties accrue.** **The employer remains liable.** **Confirming actual
> deposit is `[manual]`, from the authority's own record — request proof.**

**Payroll data is personal.** Wage statements are per-employee by nature; **build them from the register,
present them to the employer, and never persist or surface individual figures in workpapers or messages
beyond the statement data itself.**

**Mosofin is read-only.** It cannot remit, file or amend anything.
