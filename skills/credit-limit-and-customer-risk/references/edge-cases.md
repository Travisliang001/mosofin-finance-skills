<!-- credit-limit-and-customer-risk · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Customer is a household-name large entity**: the limit may be set by **trading volume rather than risk
concerns**. Document the policy basis.

**Customer is a startup with no financials**: relies on **founder guarantees, deposits, or pre-pay
terms.** *Mosofin note*: where they are an existing customer, your own payment experience becomes the
primary evidence — and it is better evidence than absent financials.

**Customer is part of a group**: **assess at the contracting-entity level, but consider parent strength if
a guarantee is in place.** A guarantee that has not been signed is not a guarantee.

**Customer in a country with capital controls**: **even creditworthy customers may struggle to remit.
Consider a letter of credit or domestic invoicing.**

**Customer is also a vendor**: **net exposure is gross A/R minus gross A/P — can mitigate.** *Mosofin
note*: **directly detectable** by matching the customer against the vendor list. Also check whether a
formal right of set-off exists — netting without one is a commercial hope, not a legal position.

**Customer was previously written off and now wants to trade again**: **requires senior approval;
typically cash terms only until trust is rebuilt.** *Mosofin note*: **the write-off history is readable**,
so this cannot be forgotten — and it should be checked across every connected entity, not just the one
asking.

**Customer's financials are old (more than 12 months) or unaudited**: **discount their reliability.** Your
own payment data, by contrast, is current.

**Insurer cancels coverage on a customer**: **a signal of deteriorating credit. Lower the limit
immediately.** The insurer has information you do not.

**Concentration**: even with a "fine" customer, **if the entity has >20% of A/R in one customer,
concentration risk needs management attention.** *Mosofin note*: computed automatically, and **at group
level in a multi-entity workspace**.

**Customer financials computed from your own books** — *Mosofin-specific, and the error to avoid above all
others here*. Your ledger cannot produce their current ratio. Never present any Step 2 metric unless the
customer's own financials were supplied.

**Days-to-pay from too few invoices** — *Mosofin-specific*. Three invoices is not a payment pattern. State
the sample size beside every figure, and fall back to qualitative assessment where it is thin.

**Terms applied differ from terms on record** — *Mosofin-specific and directly detectable*. A customer
invoiced on longer terms than their record shows is receiving credit nobody approved.

**A limit set below current exposure** — *Mosofin-specific*. Detectable immediately, and it needs a plan
rather than a number: the balance has to come down, and how is a commercial conversation.

**The same customer under several records** — *Mosofin-specific*. Duplicate or near-duplicate customer
records split the exposure and hide the true position. Check for near-matching names before computing
concentration.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say that the
group exposure is therefore understated. In this skill an omitted entity understates risk, which is the
dangerous direction.

**A result comes back with `mock: true`** — *Mosofin-specific*. Never make an adverse assessment of a
real, named business on fixture data.

**A stored tier or assessment is reused** — *Mosofin-specific*. Assessments are state and go stale. Persist
the policy; re-derive the assessment.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's ceilings to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
