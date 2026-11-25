# 09 — Gaps: what the review left unnamed

> **Status (2026-11-25):** additions proposed at planning time. Master table:
> [`README`](README.md).

Reference/work file: the review is thorough, but reading it against the actual repo
surfaces work it never names. These are the additions; each is classified the same way
as the rest of the plan (0.1.2 docs/tooling · 0.2.0 · refused). Where an addition is a
new item it carries a new ID; where it extends an existing file, the target is named.

## Additions to the verification track ([01](01-verification.md))

- **V8. False-positive / "legitimately clean" guidance** — the review says a zero-confirm
  output is "a useful heuristic, not a guarantee." The plan must say the converse too:
  when **every** fact was supplied by the user, a clean artifact is correct. The
  reviewer checklist (V2/V7) and the future linter (V1) need an explicit "clean is
  sometimes right" rule, or they will teach reviewers to distrust good artifacts.
  *0.1.2 docs.*
- **V9. PII / hostname pre-paste check** — the review's regression harness names "subtle
  PII/hostnames" as a tricky input, but no *reviewer* step checks for them. Add a
  pre-paste PII check to the review workflow, cross-linked to `docs/EXPORTS.md`
  §Redaction (C7). *0.1.2 docs.*

## Addition to the workflow track ([02](02-workflow.md))

- **W8. Long-load / context-budget recipe** — the review's W2 (relay friction) and its
  "artifacts only as accurate as what you paste" point imply a failure the plan did not
  schedule: what to do when a four-file load plus input **exceeds** a model's context.
  `docs/TROUBLESHOOTING.md` (D4 §4) already has "start fresh," but a partial-load
  recipe (which files are droppable, which are not) belongs with W6/W7. *0.1.2 docs.*

## Additions to the integrations track ([03](03-integrations.md))

- **I6. Destination validation ledger** — the review's W3 names untested paths
  (Confluence storage/code-block, Jira Data Center) but no single observed/unobserved
  matrix exists. *0.1.2 docs.* (In [03](03-integrations.md).)
- **I7. `make check-links` + `make check-frontmatter`** — the 0.1.1 gate checked links
  and the README tree by hand; the review's R1 wants it automated. Formalize as Makefile
  targets. *0.1.2 tooling.* (In [03](03-integrations.md).)

## Additions to the adoption track ([04](04-adoption.md))

- **R6. `docs/LIMITATIONS.md`** — the review *is* a limitations list; the kit publishes
  none as such. Publishing its four weaknesses first-class is the honesty the review
  praises. *0.1.2 docs.*
- **R7. Docs index / navigation** — `docs/` has passed fifteen files with no index.
  *0.1.2 docs.*
- **R8. Cookbook provenance mechanism** — R5 needs a feed or it will invent failure
  modes; entries come only from recorded runs, field feedback (F1), and
  `docs/EVIDENCE.md`. *0.1.2 docs.*
- **R9. `UPGRADING.md` 0.1.2 migration section** — tell upgrading users what changed and
  that their `my-org.md` and the new I1 overlays are untouched. *0.1.2 docs.*

## Addition to the carry-over track ([05](05-carry-over.md))

- **X4. Refresh the competitive-landscape scan** — the only scan on file is dated
  2026-11-23; the review is a fresh external input. Optional, offline, owner-run.
  *0.1.2 docs.*

## Additions to the decisions ([06](06-open-decisions.md))

- **D6. CI supply chain** — if R1 is adopted, which actions (pinned first-party only).
- **D7. Destination overlay file type & location** — Markdown overlays vs. YAML.

## The guard the review's strengths imply

- **S2. What must not regress** — the review's four strengths (and the kit's recorded
  honesty) are load-bearing; every 0.1.2 change keeps them. Stated in
  [07](07-scope-and-release.md), S2.

## Why these were missed

The review was written from the outside (the post + a repo read); it optimizes for the
**user's** pain (enforcement, friction, import fidelity, rollout). The additions above
are the **maintainer's** half: honesty about limits (R6), navigability (R7), the feed
that keeps a catalog from drifting (R8), the check that keeps the repo from rotting
(I7/R1), the edge case the heuristic breaks on (V8), and the privacy step the redaction
recipe implies but no reviewer step enforces (V9). None of them change the review's
verdict; they close the space around it.

## Related

- [`08-review-input.md`](08-review-input.md) — the review, enumerated
- [`README.md`](README.md) — the merged item list and build status
