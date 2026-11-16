# Brief: simulate a skill on its sample data

Use this to run any skill in `skills/` on the **upload path** (no Mosofin connection; the Mosofin
tools are absent), then grade the run. Run each skill in two phases, strictly in order.

## Phase 1 — blind run

Do **not** open `samples/manifest.json` or `samples/README.md` yet: they hold the answer key.

1. Read `skills/<name>/SKILL.md` fully. For a card-format skill also read, in
   `references/`: `mosofin-protocol.md` (the sections *After an upload, validate the input before
   any work*, *Rules for the common cases* and *The coverage sheet on a manual run*), `method.md`,
   `edge-cases.md` and `output.md`. For a single-file skill those sections are in `SKILL.md`.
2. Get **only** the intake answers:
   `python3 -c "import json;print(json.load(open('skills/<name>/samples/manifest.json'))['intake_answers'])"`
   Anything not answered there is unanswered: apply the skill's stated default, or the rule for an
   unanswered question in *Rules for the common cases*.
3. The user uploads every file in `skills/<name>/samples/` except `manifest.json` and `README.md`.
   Read each one.
4. Do the mandatory validation step exactly as written: one verdict per file, applying *Rules for
   the common cases*. Show it before any work. Where the skill says to wait for the user, note that
   you would wait, then assume "go ahead with the accepted files".
5. Do the skill's work on the accepted files, following its method, with real arithmetic (use
   python via Bash). Post, send, pay and change nothing.
6. Write `simulations/<name>.md`: the read-back, the validation table, the findings with figures,
   what was not done and why, and the manual-run coverage sheet. Under about 120 lines, written as
   the skill's output to a user, not as commentary.

## Phase 2 — grade

Now read `skills/<name>/samples/manifest.json` and compare the Phase 1 output with
`expect.validation`, `expect.findings` and `expect.read_only`. Be strict: a finding counts as hit
only if the Phase 1 output actually states it. Do not edit the `.md`. Write
`simulations/<name>.json` with exactly these keys:

```json
{"skill": "<name>", "mode": "agent run, upload path", "round": 2, "samples": "corrected sample set",
 "result": "PASS|PARTIAL|FAIL", "validation": "PASS|FAIL", "read_only": "PASS|FAIL",
 "findings_hit": 0, "findings_total": 0, "missed": [], "unexpected": [],
 "skill_defects": ["quote the file and heading"], "sample_defects": ["show the arithmetic"],
 "summary": "one sentence, at most 200 characters"}
```

- **PASS**: validation PASS, read-only PASS, every expected finding hit.
- **PARTIAL**: validation and read-only PASS, one or more findings missed.
- **FAIL**: validation or read-only failed.
- **Validation PASS** needs the per-file verdict table shown before the work, and the deliberately
  wrong file rejected on its content, not its name.

## Rules

Modify nothing under `skills/`. Create files only under `simulations/`, and never in `simulations/round-1/` or
`simulations/before-fixes/`; do not read those two folders. Do not run git. Do not use Mosofin or any MCP tool.

When every assigned skill is done, reply with a table — skill | result | hit/total | one-line note —
then the skill defects and sample defects that matter most, most important first, quoting file and
heading.
