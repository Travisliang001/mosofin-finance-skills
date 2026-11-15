<!-- aml-kyc-procedures · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# AML / KYC Procedures (Mosofin)

Supports **anti-money-laundering (AML)** and **know-your-customer (KYC)** compliance —
customer due diligence (CDD), enhanced due diligence (EDD), risk rating, sanctions/PEP
screening, beneficial ownership identification, transaction monitoring, and suspicious
activity escalation. Builds the framework and documentation for a **risk-based** AML program.

**In plain words:** the law requires businesses in regulated sectors to know who they are
actually dealing with, to check those people against official danger lists, to watch for
transactions that don't fit the customer's story, and to report anything genuinely
suspicious to the authorities — without telling the customer. This skill builds the
procedures for doing that, and runs the parts of the checking that your connected books can
actually support.

**Important**: AML/KYC is heavily regulated and jurisdiction-specific, with serious legal
consequences for non-compliance. This skill builds risk-based frameworks and procedures
aligned to common standards (e.g. the risk-based approach and **FATF** principles — the
international standard-setter for financial crime — as adopted locally) but does **not
replace a qualified compliance officer (MLRO / BSA officer), legal counsel, or the entity's
regulatory obligations**. Specific thresholds, forms, and filing requirements must be
confirmed against current local regulation. Suspicious activity determinations and filings
must be made by the responsible compliance function.

**A second, Mosofin-specific limit, stated up front because it is the most consequential
gap in this whole skill.** A Mosofin workspace connects **accounting and payment systems**.
It does not connect a sanctions list, a PEP list, an adverse-media feed, an identity
verification service, or a corporate registry. Therefore:

> **Screening (Step 5) cannot be performed from a Mosofin workspace. It is `[manual]` in
> every workspace, always.** This skill can build the screening procedure, produce the list
> of names and beneficial owners to be screened, and maintain the screening log — but the
> screening itself must be run against a real screening tool by the responsible compliance
> function. Never report a customer as "screened" or "clear" on the basis of anything read
> from an accounting datasource.

The same applies to identity verification and beneficial-ownership discovery: the books show
who you *invoiced*, not who *owns* them.

What the connected books **can** genuinely support is **Step 6 transaction monitoring** —
the size, frequency, timing, and pattern analysis that detects activity inconsistent with a
customer's known profile. That is real, evidence-backed work, and it is where this skill's
automated value sits.

This skill is **jurisdiction-agnostic** in structure and applies the rules the user
identifies. It is **not** system-agnostic: it is **workspace-scoped**, and every transaction
figure comes from a tool call in this conversation or from labelled user-supplied evidence.

**Mosofin is read-only.** It files nothing, freezes nothing, blocks no transaction, and makes
no suspicious-activity determination. Everything below is a *proposal or a record* for the
responsible officer.
