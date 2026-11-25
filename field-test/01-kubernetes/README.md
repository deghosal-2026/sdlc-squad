# 01 — kubernetes/kubernetes

Platform / container orchestration. **The strongest X2 candidate**: Kubernetes defines an
"enhancement" as a cross-team, staged, rollout-bearing feature — exactly the relay's shape.

| Field | Value |
|---|---|
| Repo | `kubernetes/kubernetes` |
| Stars | 129,307 |
| License | Apache-2.0 |
| Language | Go |
| Last push | 2026-11-25 |
| Open issues | 3,215 |

*(Live metadata fetched 2026-11-25 via the GitHub API.)*

## Why it qualifies

- **Popular & active** — 129k stars, pushed the day this field test was created.
- **Milestones (PMT/TPM material)** — release milestones (`v1.x`); the enhancement
  process lives in `kubernetes/enhancements` (KEPs + tracking issues).
- **Design docs** — each KEP is a design doc (Motivation, Goals/Non-Goals, Design,
  Test Plan, rollout stages alpha → beta → GA).
- **Ground truth** — the KEP + the merged implementation PRs in `kubernetes/kubernetes`.

## The feature

`[CONFIRM: select a KEP that reached beta or GA — so a design, a rollout, and merged PRs
all exist to score against.]`

Selection criteria:
- cross-SIG (exercises TPM dependencies);
- a staged rollout alpha → beta → GA (exercises the PRD's rollout + the roadmap);
- a real design decision and a Test Plan (exercises SDE);
- an originating issue/discussion separate from the KEP (the raw input).

## Input quality & leakage

- **Input quality: rich.** The raw input is the KEP's own **Motivation** section — a full problem statement with goals, non-goals, and examples.
- **Leakage risk: medium.** The Motivation is a *section of the design doc*; using it as "the raw problem" is close to using the design itself. The originating issue/discussion would be cleaner.

## Sources

- Repo: https://github.com/kubernetes/kubernetes
- Enhancements (KEPs): https://github.com/kubernetes/enhancements
- KEP directory: https://github.com/kubernetes/enhancements/tree/master/keps

## Files (to fill during the run)

- `input.md` — the raw problem (the motivating issue/discussion, cited, redacted)
- `answer-key.md` — the KEP's design + Test Plan + the merged PRs (cited)
- `artifacts/` — the kit's six artifacts
- `findings.md` — kit vs. answer key
