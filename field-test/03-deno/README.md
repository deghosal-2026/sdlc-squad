# 03 — denoland/deno

JavaScript/TypeScript runtime (developer tooling). Frequent, milestone-driven releases
and a well-run issue tracker.

| Field | Value |
|---|---|
| Repo | `denoland/deno` |
| Stars | 109,001 |
| License | MIT |
| Language | Rust / TypeScript |
| Last push | 2026-11-17 |
| Open issues | 1,754 |

*(Live metadata fetched 2026-11-25 via the GitHub API.)*

## Why it qualifies

- **Popular & active** — 109k stars, pushed within the last two weeks.
- **Milestones (PMT/TPM material)** — release milestones such as `2.7.0`, `2.5.0`,
  `2.4.0` (each with a due date and a set of issues).
- **Developer-facing features** — clear user problems with concrete acceptance.

## The feature

`[CONFIRM: select a feature with an issue/discussion (problem) plus a design and merged
PRs.]`

Selection criteria:
- a developer-facing problem with a measurable outcome (PMT);
- dependencies across subsystems (TPM);
- a design decision + tests (SDE).

## Input quality & leakage

- **Input quality: medium.** A five-year issue thread with the problem and a prototype — but the **resolution was a decision** ("adopt Node's API"), not a published design.
- **Leakage risk: medium.** The PRD's Goals state "align with the Node API" — the held-back decision is *inferable* from the thread, so the run does not cleanly separate inferred from decided.

## Sources

- Repo: https://github.com/denoland/deno
- Issues: https://github.com/denoland/deno/issues
- Milestones: https://github.com/denoland/deno/milestones

## Files (to fill during the run)

- `input.md` — the raw problem (issue/discussion, cited, redacted)
- `answer-key.md` — the merged design/PRs (cited)
- `artifacts/` — the kit's six artifacts
- `findings.md` — kit vs. answer key
