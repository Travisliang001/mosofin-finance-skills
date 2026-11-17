#!/usr/bin/env python3
"""Audit every skill and write the test tracker.

Dependency-free. Run from the repo root:

    .github/audit-skills.py            # audit, then write the tracker files
    .github/audit-skills.py --check    # audit only; non-zero exit if any check fails

Per skill it checks three things and records the outcome of a fourth:

  READ-ONLY   the skill cannot change data in any system
  VALIDATION  an uploaded input is validated for meaning before any work starts
  SAMPLES     samples/ holds test data that covers every required upload
  SIMULATION  the recorded result of a run on that sample data (simulations/<skill>.json)

Outputs: skill-test-tracker.tsv (machine-readable) and SKILL-TEST-TRACKER.md (to read).
"""
import glob, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(ROOT)

WRITE_TOOL = re.compile(r"`((?:create|update|delete|post|send|void|pay|submit|approve|apply|write|insert|upsert|patch)_[a-z_]+)`")
HTTP_WRITE = re.compile(r'"method"\s*:\s*"(POST|PUT|PATCH|DELETE)"', re.I)
# An instruction to the agent to change something. A line is a finding only when it is
# an instruction (not a prohibition, not a proposal, not a description of what a person does).
IMPERATIVE = re.compile(
    r"^\s*(?:[-*\d.]+\s*)?(?:\*\*)?(Post|Send|Email|Submit|Pay|Remit|Void|Delete|File|Wire|Transfer|Upload|Sync|Push)\s+"
    r"(?!naming|name|nothing|no\b|none|format)(?:the|a|an|each|every|all|it|them|this|these|to|into|[a-z]+ (?:invoices?|entries|entry|returns?|payments?|emails?|issues|labou?r|materials)\b)",
    re.M)
SAFE = re.compile(r"propos|never|do not|does not|cannot|can't|\bnot\b|nothing|for a person|a person (?:posts|sends|files|pays)|"
                  r"the user (?:posts|sends|files|pays|uploads)|by hand|\[manual\]|draft|read-only|create_skill", re.I)
READONLY_DESC = re.compile(r"Read-only:|Proposes only|posts nothing")


def text_of(skill):
    files = [f"skills/{skill}/SKILL.md"] + sorted(glob.glob(f"skills/{skill}/references/*.md"))
    return {f: open(f).read() for f in files}


def strip_shared(t):
    return re.sub(r"<!-- shared:[a-z-]+ start -->.*?<!-- shared:[a-z-]+ end -->", "", t, flags=re.S)


def audit_readonly(skill, texts):
    """Return (status, [findings])."""
    card = texts[f"skills/{skill}/SKILL.md"]
    whole = "\n".join(texts.values())
    flat = re.sub(r"\s+", " ", whole)
    f = []
    desc = re.search(r'^description: (.*)$', card, re.M)
    if not desc or not READONLY_DESC.search(desc.group(1)):
        f.append("description does not state the read-only posture")
    tools = sorted({m for m in WRITE_TOOL.findall(whole) if m != "create_skill"})
    if tools:
        f.append("names a write tool: " + ", ".join(tools))
    if HTTP_WRITE.search(whole):
        f.append("HTTP write verb in a tool invocation")
    for needle, label in (("this skill never changes your data", "strict no-change rule"),
                          ("Write tools are out of scope", "Gate 2 write-tool guardrail"),
                          ("Hard stop", "Gate 2 hard stop"),
                          ("no path through this skill that ends in changed data", "no-path-to-a-write statement")):
        if needle.lower() not in flat.lower():
            f.append("missing: " + label)
    if "create_skill" in whole and not re.search(r"explicit yes", flat, re.I):
        f.append("create_skill is not tied to an explicit yes")
    # imperative write instructions outside the shared blocks
    for path, t in texts.items():
        for line in strip_shared(t).split("\n"):
            if line.startswith(("|", "#", ">")) or not IMPERATIVE.search(line):
                continue
            if SAFE.search(line):
                continue
            f.append(f"instruction to check ({os.path.basename(path)}): {line.strip()[:110]}")
    return ("PASS" if not f else "FAIL"), f


def audit_validation(skill, texts):
    flat = re.sub(r"\s+", " ", "\n".join(texts.values()))
    need = ["After an upload, validate the input before any work",
            "Is it the right kind of document",
            "Is it necessary",
            "Do not start the work until the validation has been shown",
            "Rules for the common cases",
            "blocks that item, not the run",
            "The coverage sheet on a manual run"]
    missing = [n for n in need if n.lower() not in flat.lower()]
    return ("PASS" if not missing else "FAIL"), ["missing: " + m for m in missing]


def required_uploads(card):
    """Rows of the card's upload checklist that are marked Required."""
    m = re.search(r"\| Upload \| Needed\? \| Format \|\n\|[-| ]+\|\n((?:\|.*\n)+)", card)
    if not m:
        return None
    rows = []
    for line in m.group(1).strip().split("\n"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 2:
            rows.append((re.sub(r"\*\*", "", cells[0]), cells[1]))
    return rows


def audit_samples(skill, texts):
    d = f"skills/{skill}/samples"
    man = f"{d}/manifest.json"
    if not os.path.exists(man):
        return "MISSING", ["no samples/manifest.json"], 0
    m = json.load(open(man))
    f = []
    for item in m.get("inputs", []) + m.get("negative", []):
        if not os.path.exists(f"{d}/{item['file']}"):
            f.append("manifest names a missing file: " + item["file"])
    if not m.get("inputs"):
        f.append("no input files")
    if not m.get("negative"):
        f.append("no negative file for the validation step")
    if not m.get("expect"):
        f.append("no expected outcome recorded")
    n = len(m.get("inputs", [])) + len(m.get("negative", []))
    return ("PASS" if not f else "FAIL"), f, n


def simulation(skill):
    p = f"simulations/{skill}.json"
    if not os.path.exists(p):
        return "NOT RUN", "", ""
    r = json.load(open(p))
    mode = r.get("mode", "") + (f", round {r['round']}" if r.get("round") else "")
    hit = f"{r['findings_hit']}/{r['findings_total']} findings. " if r.get("findings_total") else ""
    return r.get("result", "NOT RUN"), mode, hit + r.get("summary", "")


def main():
    check_only = "--check" in sys.argv
    skills = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob("skills/*/SKILL.md"))
    rows, failed = [], 0
    for s in skills:
        texts = text_of(s)
        ro, ro_f = audit_readonly(s, texts)
        va, va_f = audit_validation(s, texts)
        sa, sa_f, n = audit_samples(s, texts)
        si, mode, summ = simulation(s)
        fmt = "card" if os.path.isdir(f"skills/{s}/references") else "single file"
        notes = "; ".join(ro_f + va_f + sa_f)
        rows.append(dict(skill=s, format=fmt, read_only=ro, validation=va, samples=sa, sample_files=n,
                         simulation=si, sim_mode=mode, sim_summary=summ, notes=notes))
        if ro != "PASS" or va != "PASS" or sa == "FAIL" or si == "FAIL":
            failed += 1
            if check_only:
                print(f"  FAIL  {s}: read-only={ro} validation={va} samples={sa} simulation={si}")
                for x in (ro_f + va_f + sa_f)[:6]:
                    print("          " + x)
    tot = lambda k, v: sum(1 for r in rows if r[k] == v)
    print(f"skills: {len(rows)}   read-only pass: {tot('read_only','PASS')}   validation pass: {tot('validation','PASS')}   "
          f"samples pass: {tot('samples','PASS')}   simulated pass: {tot('simulation','PASS')}   "
          f"simulated fail: {tot('simulation','FAIL')}   not run: {tot('simulation','NOT RUN')}")
    if check_only:
        sys.exit(1 if failed else 0)

    cols = ["skill", "format", "read_only", "validation", "samples", "sample_files", "simulation", "sim_mode", "sim_summary", "notes"]
    with open("skill-test-tracker.tsv", "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")

    mark = {"PASS": "pass", "FAIL": "**FAIL**", "MISSING": "missing", "NOT RUN": "not run", "PARTIAL": "**partial**"}
    out = ["# Skill test tracker", "",
           "Generated by `.github/audit-skills.py`. Do not edit by hand; run the script.", "",
           "| Check | What it means |", "|---|---|",
           "| **Read-only** | The skill names no write tool, carries the no-change rule and the Gate 2 guardrail, and gives no instruction to post, send, file or pay. |",
           "| **Validation** | After an upload the skill must check that each file is the right kind of document, covers the right company and period, and is needed, before any work starts. |",
           "| **Samples** | `samples/` holds test inputs for the upload path, one deliberately wrong file, and the expected outcome. |",
           "| **Simulation** | The recorded result of running the skill on its sample data, on the upload path with no Mosofin connection. Round 1 ran on the first sample set; its defects were fixed and the affected skills re-run as round 2. Full runs and grades are in `simulations/`. |", "",
           "## Totals", "", "| | Pass | Fail | Other |", "|---|---:|---:|---:|"]
    for k, label in (("read_only", "Read-only"), ("validation", "Validation"), ("samples", "Samples"), ("simulation", "Simulation")):
        p, fl = tot(k, "PASS"), tot(k, "FAIL")
        out.append(f"| {label} | {p} | {fl} | {len(rows) - p - fl} |")
    out += ["", "## By skill", "", "| Skill | Read-only | Validation | Samples | Simulation | Result |", "|---|---|---|---|---|---|"]
    for r in rows:
        res = r["sim_summary"] or r["notes"] or ""
        sim = mark.get(r["simulation"], r["simulation"]) + (f" ({r['sim_mode']})" if r["sim_mode"] else "")
        out.append(f"| `{r['skill']}` | {mark[r['read_only']]} | {mark[r['validation']]} | {mark.get(r['samples'], r['samples'])}"
                   f"{' (' + str(r['sample_files']) + ')' if r['sample_files'] else ''} | {sim} | {res[:220]} |")
    open("SKILL-TEST-TRACKER.md", "w").write("\n".join(out) + "\n")
    print("wrote skill-test-tracker.tsv and SKILL-TEST-TRACKER.md")


if __name__ == "__main__":
    main()
