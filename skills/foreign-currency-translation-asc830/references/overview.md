<!-- foreign-currency-translation-asc830 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Foreign Currency Translation and Remeasurement — ASC 830 / IAS 21 (Mosofin)

Handles foreign currency accounting for entities with transactions or subsidiaries in foreign currencies,
including:

- **Functional currency determination**
- **Remeasurement of foreign currency transactions**
- **Translation of foreign subsidiary financial statements**
- **Cumulative translation adjustment (CTA) in OCI**
- **Controls and disclosures**

**In plain words:** if part of the group earns and spends in euros but the accounts are published in
dollars, those euros have to be converted. Which rate you use depends on what the item is and why the
currency differs — and the leftover difference has to go somewhere. Getting the "which rate" part wrong is
easy and almost invisible, because the books still balance either way.

It is **workspace-scoped**: each entity's trial balance, home currency and intercompany balances come from
tool calls against company files connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

## This skill is multi-entity by nature — and CTA hides errors

Two things shape everything below.

**First: Gate 1 is not overhead here, it is Step 1's input.** Most skills in this pack treat the connected
company file list as scope-setting. **This one needs the entity structure as its primary input, and the
connected list is exactly that** — each company file, its `display_name`, and **its home currency, which is
readable from the company profile**. What the workspace does not give you is ownership percentages or the
group's legal structure; those stay `[manual]`.

**But the platform's home currency is not the functional currency.** The home currency is a setup choice
someone made when the file was created. **The functional currency is an accounting conclusion** about the
primary economic environment. They agree most of the time and, when they do not, **everything downstream is
wrong in a way that still balances.** Read the home currency, then ask whether it is right — never treat it
as the answer.

**Second, and more important: CTA is a plug, so a translation error does not fail to balance — it goes into
CTA.**

That is the single most consequential fact in this skill. The cumulative translation adjustment is computed
as **the amount required to make the translated balance sheet balance**. So:

> **If you translate an account at the wrong rate, the balance sheet still balances.** The error simply
> lands in CTA and sits in equity, indefinitely, looking exactly like a legitimate translation effect.

**Therefore "it balances" is not a control here.** The real control is to **prove CTA independently**:
compute what CTA *should* be from the movement in net assets and the movement in rates, then compare it to
the plug. **A difference between the derived CTA and the plugged CTA is a translation error**, and it is
the only way to find one. That check is built into Step 3b.

**Mosofin is read-only.** It cannot post a remeasurement, a translation entry or a CTA adjustment. Every
entry below is a *proposal*.
