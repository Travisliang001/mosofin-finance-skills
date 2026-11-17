<!-- related-party-disclosures-asc850 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section. These are the situations the workflow above does not resolve on its own.)*

**A related party for part of the year only.** A director who resigned, a subsidiary sold mid-period, a shareholder who fell below the significance threshold. Transactions during the related period are disclosable; transactions after it generally are not. `[auto]` to split the transactions by date once the dates are known; `[manual]` for the dates. **The current list will not contain them** — this is why Step 5 asks for leavers.

**A relationship that exists but produced no transactions.** Still disclosable in many cases — the relationship itself, and any balance, may require disclosure even where nothing was transacted in the period. **The ledger cannot surface a party it never transacted with**, which is a structural blind spot of the entire completeness match. `[manual]`.

**Common control without ownership.** Two entities controlled by the same individual through different structures, or by close family members acting together. The cap table of either one alone shows nothing. `[manual]`, and one of the commonest ways a related party goes undisclosed.

**A transaction at no charge.** Free use of premises, unpaid services provided by a shareholder, a director not taking a salary. **These leave no trace whatsoever in a ledger** — the defining property of a nil-value transaction is that it is not recorded. Several frameworks require disclosure anyway. `[manual]`, entirely, and worth asking about directly because nobody volunteers it.

**A guarantee given or received.** Off-balance-sheet until called. Not in the accounts, disclosable, and easily forgotten. `[manual]`. See Step 4.

**An intermediated transaction.** The client transacts with an unrelated party who transacts with a related one. Whether this is disclosable depends on the framework and the substance. `[manual]`.

**The same person under different names.** Married names, transliterations, initials versus full names, a legal name that differs from the one everyone uses. **Fuzzy matching helps and does not solve it.** Where the client supplies alternative names, match on all of them.

**A vendor and customer with the same name who are genuinely unrelated.** Two businesses sharing a common surname or a generic trading name. The Sheet 6 candidate is a question, and sometimes the answer is no. **Record the "not related" conclusions with their reasoning**, so the same candidate is not re-raised every quarter.

**Framework differences.** ASC 850 and IAS 24 do not define key management personnel or close family identically, and IAS 24 has specific requirements around government-related entities. **Establish the framework at Gate 3** and apply it; do not blend them.

**Materiality.** Related-party disclosure requirements are not straightforwardly subject to a materiality threshold in the way most disclosures are — the fact of a relationship can matter regardless of amount. `[manual]`. Do not filter Sheet 3 by size without saying so.
