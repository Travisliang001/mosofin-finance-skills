# Simulation runs

Each run is an agent playing the skill on the **upload path** (no Mosofin connection), using the
files in `skills/<name>/samples/`, then grading itself against `samples/manifest.json`.

- `<name>.md` — the run, written as the skill's output: read-back, validation table, findings, what was not done.
- `<name>.json` — the grade: result, findings hit, and the defects the run found in the skill and in the samples.
- `round-1/` and `before-fixes/` — earlier runs of skills that were re-run after their defects were fixed, kept for comparison.
- `BRIEF.md` — the instructions every run follows, so a run can be repeated.

The run is blind: the agent reads only the intake answers before working, and opens the answer key
afterwards. Results are recorded in [`../SKILL-TEST-TRACKER.md`](../SKILL-TEST-TRACKER.md).

**Round 1** (18 skills, first sample set): 17 pass, 1 partial. Every run rejected the wrong file on its
content and posted nothing. The runs found shared gaps in the upload rules and errors in the sample
data; both were fixed, and the affected skills were re-run as **round 2**.

**All 114 skills, then re-runs.** Every skill was run once on the sample data: 101 passed, 12 were
partial and 1 failed. Every run passed validation and read-only. The partials and the failure traced
to gaps in specific skills or to errors in the sample data and answer keys; both were fixed, and the
13 were re-run as **round 3**: 12 passed. The one remaining partial, fraud detection, missed a test
its own method lists (weekend postings); the skill is not at fault.

Two round-3 passes were judgment calls, recorded in their grades: scenario analysis said it would stop
for range acceptance and then carried on as the brief allows; year-end close listed the tax true-up as
not done rather than giving it an owner.

