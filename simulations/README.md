# Simulation runs

Each run is an agent playing the skill on the **upload path** (no Mosofin connection), using the
files in `skills/<name>/samples/`, then grading itself against `samples/manifest.json`.

- `<name>.md` — the run, written as the skill's output: read-back, validation table, findings, what was not done.
- `<name>.json` — the grade: result, findings hit, and the defects the run found in the skill and in the samples.
- `round-1/` — the first runs of skills that were re-run after their defects were fixed.

The run is blind: the agent reads only the intake answers before working, and opens the answer key
afterwards. Results are recorded in [`../SKILL-TEST-TRACKER.md`](../SKILL-TEST-TRACKER.md).

**Round 1** (18 skills, first sample set): 17 pass, 1 partial. Every run rejected the wrong file on its
content and posted nothing. The runs found shared gaps in the upload rules and errors in the sample
data; both were fixed, and the affected skills were re-run as **round 2**.
