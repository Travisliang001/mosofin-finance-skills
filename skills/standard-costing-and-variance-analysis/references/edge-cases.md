<!-- standard-costing-and-variance-analysis · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section.)*

**No quantities in the accounting system.** Only price and spending variances are computable; usage, efficiency and volume variances are not. **Say so rather than deriving quantities by dividing value by standard price** — that assumes the answer and produces a usage variance of exactly zero by construction.

**A standard reset mid-period.** Variances before and after are measured against different baselines and must not be summed as though they were comparable. **Effective dates matter**, which is why Step 1 requires them. `[auto]` to detect the discontinuity.

**Freight and duties inconsistently treated.** Step 1 makes their inclusion in standard price a **policy**. If the standard includes freight and the actual purchase price excludes it — or the reverse — **every PPV carries a systematic offset.** `[auto]` for the signal: a small, highly consistent variance proportional to purchase value. This is the most common cause of an unexplained residual in the bridge.

**Purchases and production in different periods.** PPV recognises at purchase and usage at consumption, so a period of heavy buying and light production shows a large PPV and a small usage variance without anything unusual having happened. **Do not read the two as a single period's performance.**

**Adverse variances being capitalised into inventory.** Where policy permits capitalisation and the variances are persistently adverse, **inventory is carried above efficient cost** and may exceed net realisable value. `[auto]` to quantify the exposure. See `inventory-obsolescence-and-reserve`.

**A standard set to recent actuals.** Bakes in existing inefficiency; the variance goes to zero and stops measuring anything. **Zero variance is not a good result** — it usually means the standard was reset to whatever was happening.

**Mix variance masquerading as usage variance.** Where several products with different standard costs share a production line, a shift in mix moves the aggregate variance without any change in efficiency. `[auto]` to separate **where a product dimension exists**; `[manual]` where it does not, and in that case the aggregate variance is not decomposable and should not be presented as though it were.

**Scrap treated inconsistently.** Standard usage is *BOM plus expected scrap.* If actual scrap is recorded outside the production accounts, or not recorded at all, the usage variance absorbs it invisibly. Establish where scrap is recorded.

**Overhead absorbed at a rate based on a budget nobody revisited.** The fixed overhead rate depends on planned volume. **A rate built on a volume plan that is two years old produces volume variances that measure the age of the plan.** Same failure as the stale standard, in a different account.

**Multi-currency purchases.** A material bought in another currency carries an FX movement inside what looks like a price variance. **Separate the FX effect from the genuine price effect**, or the root-cause analysis will chase a supplier who never changed their price.
