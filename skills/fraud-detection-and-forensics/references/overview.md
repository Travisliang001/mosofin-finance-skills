<!-- fraud-detection-and-forensics · overview.md · read for: background — the boundaries of this skill, and what a full-population read changes. Edit here, not in SKILL.md. -->

# Fraud Detection and Forensics (Mosofin)

Supports **fraud risk assessment**, **analytical detection**, and a **forensic investigation framework**.
Applies data analysis and forensic techniques to identify red flags, structures investigations objectively,
and quantifies losses. **Emphasizes evidence, objectivity, and proper escalation.**

**In plain words:** this looks through the accounting records for patterns that sometimes indicate theft or
manipulation — payments that look duplicated, suppliers that look invented, numbers that look shaped. It
finds patterns. **It does not find people.**

## Important boundaries — read before running anything

**This skill helps detect and analyze indicators and structure an investigation. It does NOT conclude that
a specific person committed fraud — that is a legal determination requiring due process. For actual
investigations, qualified forensic professionals (e.g. CFEs) and legal counsel must be involved, evidence
must be preserved properly, and rights respected. Claude assists analysis; it does not accuse
individuals.**

**Three things about the Mosofin workspace make those boundaries more important here, not less:**

1. **The analytical tests are trivially easy to run.** Most of Step 4 is a query rather than a project. When
   producing a list of anomalies costs one tool call, **the discipline of treating that list as questions
   rather than answers has to be deliberate.** An easy test does not produce a stronger conclusion; it
   produces the same weak indicator, faster.
2. **The output names real people.** Vendor masters and employee lists contain names, addresses and contact
   details of identifiable individuals. **A red-flag list is a document about people who have not done
   anything wrong until proven otherwise**, and it must be handled that way — in what you write, who you
   send it to, and what is never persisted.
3. **An API read is not preserved evidence.** A tool result in a conversation transcript has **no chain of
   custody**, no forensic image, no timestamped hash. **It is analysis, not evidence.** If a matter becomes
   a real investigation, the records must be preserved properly by people qualified to do it — and nothing
   read here substitutes for that.

**Mosofin being read-only is a safety feature in this skill specifically.** It cannot alter a record, cannot
delete a trail, and cannot tip anyone off by changing something they would notice. Keep it that way: **do
not propose that anyone go and change records** while a concern is open.

It is **workspace-scoped**: the transaction population, the vendor and employee masters and the balances
come from tool calls against a company file connected to your Mosofin workspace in this conversation, or
from something you supplied by hand and that is labelled as such.
