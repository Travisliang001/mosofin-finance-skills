# Restructuring under ASC 420 — Northbrook Trading Ltd, as at 30 September 2025

This run is manual: no Mosofin connection. Everything below comes from the files you uploaded.
Nothing has been posted, sent or changed. Every entry is a proposal for a person to post.

## Read-back

Accounting for the **2025 restructuring** at **Northbrook Trading Ltd** for the period ending
**30 September 2025**, in **USD**, under **ASC 420**, approved by the board on **3 October 2025** and
communicated to affected staff on **14 October 2025** (all-hands meeting; minutes said to be on
file), from **the plan summary and trial balance you uploaded**. **Two groups, 4 roles**, total
severance **37,700**; **no future service required**; one lease exit (overflow unit) with a
penalty of **15,000**; expected completion **31 December 2025**. Output to **the CFO only**. No names
recorded.

Taken from the plan file, not from your intake answers: the framework, the approval and
communication dates, the groups, the future-service answer, the lease penalty, the completion date
and the audience. I treat them as answered once you confirm this read-back. Company, period and
currency are as you stated them; no file names them.

## Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `restructuring_plan.md` | A one-page plan summary: approval and communication dates, a cost table by group (2 groups, 4 roles, 37,700), lease penalty, completion date | Company not named in the file (2025 plan; user-asserted Northbrook) | Yes. Group totals foot to 37,700 | Steps 1, 2, 4, 5 | **Accepted with a limit**: a summary, not the approved board paper, the communication evidence or the lease agreement. Every figure from it is user-supplied, not evidenced. No split of statutory versus discretionary severance |
| `restructuring_plan_final.csv` | A four-week shift rota for employees E08, E09, E10 (nights / days / off) | No company, date or amount | Not for this skill | No step uses it | **Rejected**. Despite the name, it is not a final version of the plan: it holds no cost, headcount by group or terms. It also carries employee identifiers this skill does not need. Set aside, not read into the work. If there is a final plan, please upload that |
| `trial_balance_2025-09-30.csv` | A trial balance, 33 accounts | No entity or currency in the file; date from the file name only (user-asserted) | Yes. Debits 6,546,018 = credits 6,546,018 | Steps 1 (ROU check), 3 (opening reserve) | **Accepted with a limit**: balances only, no transaction detail, so the reserve roll-forward and the four reserve challenge tests cannot run from it |

**Still missing:** the approved plan / board paper (required; a summary was received), the lease
agreement with the termination penalty (required for that cost), reserve account detail (required
for the roll-forward; the TB holds no restructuring account at all), and the communication
evidence (recommended). I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## Findings

**1. Nothing is recognised at 30 September 2025.** Both triggers fall after the period end: the
board approved the plan on 3 October and staff were told on 14 October. ASC 420 recognises a
one-time termination benefit on communication, so there is **no restructuring liability and no
restructuring expense in September**. Accruing the 37,700 (or 52,700 with the lease) in September
would book the cost a period early.

**2. Subsequent event, not an accrual.** If the September statements are issued after 14 October,
the plan is a **non-recognised subsequent event**: disclose its nature and the estimated cost
(severance 37,700; lease exit 15,000; total 52,700). See `subsequent-events-asc855`.

**3. Severance is recognised in October, in full.** No future service is required (stated in the
plan, for both groups), so the whole amount is recognised on 14 October 2025, in Q4:

| Cost type | Group | Headcount | Terms | Amount | Basis | Communicated | Evidence |
|---|---|---:|---|---:|---|---|---|
| Severance | Warehouse, night shift | 3 | 8 weeks' pay each | 26,000 | Immediate | 14 Oct 2025 | All-hands minutes (not uploaded) |
| Severance | Admin | 1 | 12 weeks' pay | 11,700 | Immediate | 14 Oct 2025 | All-hands minutes (not uploaded) |
| **Total severance** | | **4** | | **37,700** | | | |
| Contract termination | Overflow unit lease | — | Penalty | 15,000 | On termination | Not stated | Lease not uploaded |
| **Total plan cost** | | | | **52,700** | | | |

Implied weekly pay: 1,083.33 (warehouse, 26,000 / 24 weeks); 975.00 (admin, 11,700 / 12 weeks).
Please confirm whether any part is statutory redundancy pay or paid under a pre-existing severance
policy: either would change the recognition date for that part.

**4. The lease penalty is recognised when the lease is terminated, not on announcement.** No
termination date is given. The TB holds **no right-of-use asset and no lease liability**; the only
lease-related line is Rent (6100) at 81,000. Before building a 15,000 exit liability, confirm
which lease model applies: if the overflow unit is an ASC 842 lease, the exit is a lease
modification or ROU impairment, not an ASC 420 provision, and a separate 420 reserve would
double-count it. Route to `lease-accounting-asc842-ifrs16`.

**5. Reserve roll-forward at 30 September 2025:** opening 0 + additions 0 − payments 0 ± revisions
0 = **closing 0**. No restructuring liability account exists in the TB.

**6. Proposed entries (PROPOSED — NOT POSTED; for October 2025, not September)**

```
14 Oct 2025  DR Restructuring expense     37,700
               CR Restructuring liability       37,700   Severance, 2 groups, 4 roles
On termination DR Restructuring expense   15,000         (only if the lease is outside ASC 842)
               CR Restructuring liability       15,000   Overflow unit lease exit
On payment   DR Restructuring liability   xx,xxx
               CR Cash                          xx,xxx   Not through wages (6000)
```
The TB has no restructuring accounts; set them up under your own codes. I have not invented any.

**7. Disclosure draft (DRAFT):** nature, a reduction of 4 roles in warehouse night shift and
admin and the exit of the overflow unit; expected completion 31 December 2025; roll-forward nil at
30 September 2025.

## What was not done, and why

- **Reserve challenge tests A–D**: not run. There is no reserve yet and no ledger detail. Set up
  for Q4: Test C should watch Payroll Expense (6000) for severance paid through wages; Test D
  uses 31 December 2025.
- **Payment-pattern check** (were the 4 people still on payroll after 14 October?): needs October
  onward payroll detail.
- **Discounting**: not relevant on these figures (payments expected within Q4); no rate supplied.
- **Evidence of approval and communication**: not uploaded; dates are as stated in the summary.
- **Excel workbook**: not created. Do you want `Restructuring_2025_Northbrook Trading Ltd.xlsx`?

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, as at 30 Sep 2025, USD, all user-asserted; ASC 420; plan approved 3 Oct 2025, communicated 14 Oct 2025, completion 31 Dec 2025; source: upload. Files: plan summary (accepted with a limit), trial balance (accepted with a limit), shift rota (rejected) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Step 1 cost types | Done: severance and contract termination; facility costs none stated |
| Step 2 accrual model | Done with a limit: by group, from the summary; statutory split unknown |
| Step 3 roll-forward | Done with a limit: nil at 30 Sep from TB balances; no transaction detail |
| Step 3b challenge | **Not done**: needs reserve and payroll account detail from October onward |
| Step 4 entries | Done: proposed for October, not posted |
| Step 5 disclosures | Done as draft; subsequent-event disclosure flagged |
| Unknowns carried forward | Lease termination date and lease model; statutory vs discretionary split; pre-existing policy |
| Parameters | One plan; recognition immediate for both groups; no discount rate; Test D date 31 Dec 2025 |
