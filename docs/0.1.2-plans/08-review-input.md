# 08 — The review input, reproduced and enumerated

Reference file, not a work list: the external review this plan responds to, kept whole
so every item in [01](01-verification.md)–[05](05-carry-over.md) can be traced back to
it. The review was supplied by the owner on 2026-11-25; it is **input**, treated the way
the kit treats any input — a claim to verify, not a fact. Nothing here was fetched (the
repo is offline by charter).

## What was reviewed

The dev.to post *"SDLC-Squad: 20 skills that write your PRDs and sprint plans without
making anything up"* (Nov 23, 2026) and this repository at **v0.1.1**.

## The review's assessment

### Strengths (keep these — [07](07-scope-and-release.md), S2)

1. **Treating unverified gaps as defects, not "helpfulness"** — `[CONFIRM: ...]` markers,
   and zero markers on raw notes read as a suspicious defect.
2. **Artifact relay over mega-prompts** — separate PMT/TPM/SDM/SDE sessions passing
   structured Markdown, reducing role bleed.
3. **Intellectual honesty in the post-mortem** — doc-vs-code drift (three files vs. four;
   "no installer" alongside `pip install`), silent Jira priority/label remapping, a
   fixture-total mismatch left unedited as evidence, bundle drift caught by
   `make check-bundles`.
4. **Zero-runtime, local-first simplicity** — plain Markdown, schemas, destination
   contracts, a thin CLI, no daemon/API-key lock-in.

### Weaknesses & risks (the core problems → mapped below)

1. **Prompt discipline is not deterministic enforcement** — grounding and `[CONFIRM]`
   live in prompts, not programmatic validation; weaker models can invent or skip
   markers.
2. **High manual workflow overhead ("squad" by copy-paste)** — the multi-stage relay and
   manual pasting introduce real friction; artifacts are only as good as what the human
   pastes.
3. **Destination contracts are brittle and partially unvalidated** — custom Jira
   workflows/field vocabularies/ADF quirks (the author's own P1/P2 → Medium, Size →
   Labels); Confluence storage/code-block paths and Jira Data Center untested.
4. **Static artifacts drift from live systems quickly** — sprint plans, RAID logs, and
   designs go stale; synchronization stays manual.

### Practical takeaways (adoption blockers)

1. Treat it as a drafting & review checklist, not a source of truth.
2. Test against your own Jira/Confluence instance first.
3. Keep org context externalized and versioned.
4. Feed in real repo/tracker context explicitly.

## The 20 concrete ideas (as the review grouped them)

**Grounding & Anti-Hallucination:** (1) automated `[CONFIRM]` linter & gatekeeper;
(2) source-citation footnotes on every claim; (3) arithmetic & capacity self-audit
block; (4) confidence & ambiguity scoring per section; (5) model-specific behavioral
profiles (`MODELS.md` matrix) + a 60-second benchmark prompt.

**Workflow & Friction Reduction:** (1) one-command clipboard copy (`--copy`/`--out`);
(2) guided interactive intake (`--interview`) / structured inputs; (3) diff-aware
artifact updates; (4) end-to-end "Feature Relay" pack; (5) role-to-role handoff
checklist.

**Integrations & Live Context:** (1) instance-specific Jira/Confluence profile generator
(`org-destinations.yaml` / `my-jira.md`); (2) safe read-only context pullers;
(3) Jira CSV & issue-creation dry-run exporter; (4) Confluence storage/Markdown
compatibility mode; (5) GitHub PR & issue template pack.

**Team Rollout & Ecosystem Trust:** (1) CI doc-to-code & bundle drift checks;
(2) 15-minute "pilot kit"; (3) sanitized real-world examples across company sizes;
(4) skill maturity & verification badges beyond "built"; (5) community anti-pattern &
hallucination cookbook.

## The deeper architectural breakdown (as the review specified)

- **Track 1 — Anti-Hallucination & Verification:** `scripts/lint_artifact.py` with a
  zero-confirm heuristic, an unresolved-placeholder audit (leftover brackets; `TBD`,
  `as needed`, `standard SLA`), and table/math reconciliation; a claim-to-source tagging
  convention (`[src: notes]`, `[src: prd-draft]`, `[src: org-glossary]`,
  `[CONFIRM: missing from input]`); explicit assumption-vs-fact separation with an
  Assumptions & Open Questions block; a model regression harness (golden set scored on
  refusal/flagging accuracy, schema fidelity, low-cost-model viability).
- **Track 2 — Workflow & Integration Friction:** CLI ergonomics (`--copy`, `--out`,
  `--context`, `doctor`); target-system profile overlays (`my-jira.md`,
  `my-confluence.md`, `my-github.md`); incremental update mode (`--mode update` →
  proposed changes / preserved items / new `[CONFIRM]`s); a relay Handoff Block
  (upstream sources, blocking `[CONFIRM]`s, next role & skill).
- **Track 3 — Team Rollout & Adoption:** a 2-week, 1-squad pain-first pilot (two skills);
  anchoring on concrete metrics; co-designing `my-org.md` early; making `[CONFIRM]` a
  culture signal; protecting against upgrade wipeouts and doc drift (customizations
  outside the upgrade path; CI checks for bundle drift, broken links, metadata
  consistency).

## Suggested order of attack (as the review stated)

- **Week 1 (Trust & Correctness):** post-generation linter + externalize
  `my-org.md` / destination overrides.
- **Week 2 (Speed & Ergonomics):** `--copy` / `--out` and `--mode update`.
- **Week 3–4 (Adoption):** a focused pilot with one squad on two skills.

*At the docs level this plan follows that order ([README](README.md) §Work order); the
Week-1 linter and Week-2 CLI flags are 0.2.0 here ([07](07-scope-and-release.md)).*

## Mapping — review idea → plan item

| Review idea | Plan item |
|---|---|
| `[CONFIRM]` linter & gatekeeper | [V1](01-verification.md) (0.2.0) |
| Source-citation footnotes | [V2](01-verification.md) (0.1.2) |
| Arithmetic / capacity self-audit | [V3](01-verification.md) (0.2.0) |
| Confidence & ambiguity scoring | [V4](01-verification.md) (0.2.0) |
| Model profiles + benchmark | [V5](01-verification.md) (0.1.2) |
| Model regression harness | [V6](01-verification.md) (0.2.0) |
| Assumption-vs-fact separation | [V7](01-verification.md) (0.1.2) |
| `--copy` / `--out` | [W1](02-workflow.md) (0.2.0) |
| `--context` assembly | [W2](02-workflow.md) (0.2.0) |
| `sdlc-squad doctor` | [W3](02-workflow.md) (0.2.0) |
| Interactive / structured intake | [W4](02-workflow.md) (0.2.0) |
| Diff-aware update mode | [W5](02-workflow.md) (0.2.0) |
| Feature Relay pack | [W6](02-workflow.md) (0.1.2) |
| Handoff checklist / block | [W7](02-workflow.md) (0.1.2) |
| Instance profile overlays | [I1](03-integrations.md) (0.1.2) |
| Read-only context pullers | [I2](03-integrations.md) (**refused**) |
| Jira CSV dry-run exporter | [I3](03-integrations.md) (0.2.0) |
| Confluence compatibility mode | [I4](03-integrations.md) (0.1.2) |
| GitHub template pack | [I5](03-integrations.md) (0.1.2) |
| CI drift checks | [R1](04-adoption.md) (0.1.2, D2) |
| Pilot kit | [R2](04-adoption.md) (0.1.2) |
| Examples across company sizes | [R3](04-adoption.md) (0.1.2) |
| Maturity / verification badges | [R4](04-adoption.md) (0.2.0, D3) |
| Anti-pattern cookbook | [R5](04-adoption.md) (0.1.2) |

## What the review did **not** say (added by this plan)

See [09](09-gaps.md) — the additions the review left unnamed: false-positive guidance,
a PII pre-paste check, a long-load recipe, the destination validation ledger, the make
gates, `LIMITATIONS.md`, the docs index, the cookbook feed, the upgrade note, a
landscape refresh, and the CI/overlay decisions.

## Sources

- The review text supplied by the owner, 2026-11-25 (reproduced above; not fetched).
- Repo state it was checked against: `main` @ `9ff4f22` (v0.1.1).
