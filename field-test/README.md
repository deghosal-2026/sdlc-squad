# field-test — the X2 validation run

Four **real, popular, actively-maintained** open-source projects, one feature each, run
through the kit's whole loop — PMT → TPM → SDM → SDE. This is the v0.1.x validation
(plan item **X2**): proof the kit produces usable artifacts on real work, not just
synthetic fixtures.

It doubles as a **showcase**: each folder holds the raw input, the kit's six artifacts, the
project's own real artifacts as an **answer key**, and a findings note.

## Method (raw input in, answer key held back)

For each repo we pick one feature and split its public record in two:

- **Input** — the *problem*: the issue/discussion/motivation, as the team stated it
  (redacted, cited). This is what a session would paste.
- **Answer key** — the *solution*: the merged design doc / RFC / KEP and the
  implementation PRs. Held back, then used to score the kit's artifacts.

Then we run the loop — PMT (`draft-prd`, `slice-mvp-and-stories`), TPM
(`program-roadmap-and-deps`), SDM (`sprint-planning-and-capacity`), SDE
(`technical-design-and-breakdown`, `generate-test-ideas-and-cases`) — and compare.

## The four projects

Live metadata from the GitHub API, **fetched 2026-11-25**:

| # | Folder | Repo | Stars | License | Last push | PMT/roadmap material |
|---|---|---|---|---|---|---|
| 01 | [`01-kubernetes/`](01-kubernetes/README.md) | `kubernetes/kubernetes` | 129,307 | Apache-2.0 | 2026-11-25 | Release milestones (`v1.x`) + KEPs in `kubernetes/enhancements` |
| 02 | [`02-grafana/`](02-grafana/README.md) | `grafana/grafana` | 78,151 | **AGPL-3.0** | 2026-11-25 | Release milestones (e.g. `11.6.x`) |
| 03 | [`03-deno/`](03-deno/README.md) | `denoland/deno` | 109,001 | MIT | 2026-11-17 | Release milestones (`2.x`) |
| 04 | [`04-rust/`](04-rust/README.md) | `rust-lang/rust` | 122,413 | Apache-2.0 / MIT | 2026-11-25 | Release milestones (`1.x`) + RFCs in `rust-lang/rfcs` |

Four different domains — platform, observability, runtime, language — so the field test
shows the kit is not tuned to one kind of project.

## Attribution & licensing

Every repo is public and its content is cited with a source link and a retrieval date.
Quote **minimally** and link generously — especially **Grafana (AGPL-3.0)**, where only
short quoted excerpts are used, never bulk copying. `[CONFIRM: confirm each project's
license terms before publishing a field test that quotes its content.]`

## Structure of each folder

```
<NN>-<repo>/
  README.md          # the repo, why it qualifies, the feature, the source links
  input.md           # the raw problem (cited, redacted)
  answer-key.md      # the project's real design + PRs (cited) — the ground truth
  artifacts/         # the kit's output, one file per skill run
  findings.md        # what the kit got right / invented / dropped, vs the answer key
```

## License clearance

Before publishing this field test, confirm each project's terms — the samples quote public
content, so keep quotes minimal and cite. `[CONFIRM: owner sign-off.]`

| # | Repo | License | Action |
|---|---|---|---|
| 01 | `kubernetes/kubernetes` | Apache-2.0 | Attribute; keep quotes short |
| 02 | `grafana/grafana` | **AGPL-3.0** | **Quote-minimal only** — no bulk copying |
| 03 | `denoland/deno` | MIT | Attribute |
| 04 | `rust-lang/rust` | Apache-2.0 / MIT | Attribute |

## Status

| Folder | Feature | Input | Answer key | Artifacts | Findings |
|---|---|---|---|---|---|
| 01-kubernetes | KEP-1287 — In-place Update of Pod Resources (`stable`) | ✅ | ✅ | ✅ | ✅ |
| 02-grafana | #77704 — "Go back to x" navigation *(decision only)* | ✅ | ✅ | ✅ | ✅ |
| 03-deno | #8327 — Node-compatible module loader API | ✅ | ✅ | ✅ | ✅ |
| 04-rust | RFC 3137 — `let-else` | ✅ | ✅ | ✅ | ✅ |

**All four are run.** Each folder holds the raw input, the project's real record as the answer
key, the kit's six artifacts, and a findings note. The roll-up review is in
[`FINDINGS.md`](FINDINGS.md).
