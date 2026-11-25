# 04 — Adoption: team rollout, drift checks, ecosystem trust

> **Status (2026-11-25):** R1, R2, R3, R5, R6, R7, R8, R9 in scope for 0.1.2;
> R4 is a **forward-pointer to 0.2.0**. Master table: [`README`](README.md).

Theme: the review's Track 4 and its W4 weakness ("static artifacts drift … keeping them
synchronized remains manual") plus the rollout half of Track 3. Almost all docs-only;
one CI candidate.

## R1. CI doc-to-code + bundle drift checks — **0.1.2 (tooling, D2)**

- **Review claim:** GitHub Actions verifying skill frontmatter status, validating
  referenced file paths in READMEs/docs, and running `make check-bundles` on every PR.
- **Classification — 0.1.2 candidate (repo tooling, no runtime).** Depends on I7's
  targets. Needs [D2](06-open-decisions.md) (does the kit adopt CI at all) and
  [D6](06-open-decisions.md) (which actions, pinned).
- **Guard — supply chain:** the kit's promise is "no network, no telemetry"; a CI
  workflow runs on GitHub's runners and must use **pinned, first-party actions only**,
  hold **no secrets**, and contact nothing but GitHub itself. [D6](06-open-decisions.md).
- **Acceptance:** a workflow runs `make check-bundles`, `check-links`,
  `check-frontmatter`, and `test` on PRs; fails on drift; uses only pinned actions.

## R2. Pilot kit / 2-week rollout playbook — **0.1.2 (docs)**

- **Review claim:** a practical adoption playbook — run a 2-week trial with one squad,
  pick two high-pain skills, and measure time saved and defects caught.
- **Anchor:** the F1 `field-feedback` template already captures time-to-first-draft,
  edits required, paste result, and reuse intent; `docs/START-HERE.md` has scenario
  recipes; the review names the skills to start with (`sprint-planning-and-capacity`,
  `scope-cut-and-tradeoffs`, `pr-plan-and-rollback-notes`,
  `technical-design-and-breakdown`, `slice-mvp-and-stories`).
- **What:** `docs/PILOT.md` — pick two skills, co-design `my-org.md`, run two weeks,
  capture the metrics, decide go/no-go.
- **Classification — 0.1.2 docs.**
- **Acceptance:** the playbook names the skills, the metrics (all from F1 — no new
  instrumentation), and a decision point; links the feedback template; makes no claim
  about outcomes.

## R3. Examples across company sizes (synthetic) — **0.1.2 (docs)**

- **Review claim:** realistic, anonymized examples for a small startup squad, a
  platform/infra team, and a cross-functional product squad — "synthetic fixtures can
  feel too neat."
- **Guard:** **synthetic only** (the fixtures rule: every company, person, path, ticket,
  and date is invented). "Sanitized real-world" is satisfied by clearly-fictional
  scenarios; no real org data anywhere.
- **Classification — 0.1.2 docs** — extends `docs/EXAMPLES.md` / `usage/WALKTHROUGH.md`.
- **Acceptance:** three scenarios, all clearly fictional (the Meridian Outfitters
  family), each showing messy input → `[CONFIRM]`s → output; every fact traceable to a
  fixture.

## R4. Skill maturity / verification badges — **forward to 0.2.0 (D3)**

- **Review claim:** lifecycle tiers in skill metadata — `fixture-verified`,
  `paste-tested-github`, `paste-tested-jira`, `field-proven` — so users start with the
  battle-tested skills.
- **Classification — 0.2.0.** New frontmatter **semantics** across 20 `SKILL.md`
  (`CONVENTIONS.md`: the `status` field is the honesty mechanism; the 0.1.1 G2 precedent
  shows even description-only `SKILL.md` edits are a deliberate minor-class exception).
  A docs-only shadow — a **verification ledger page** (like I6) listing tiers without
  touching frontmatter — is possible now; [D3](06-open-decisions.md) decides.
- **Acceptance (when built):** a defined tier vocabulary, each assignment traceable to
  a fixture or recorded run; no tier without evidence.

## R5. Anti-pattern & hallucination cookbook — **0.1.2 (docs)**

- **Review claim:** a living catalog of real LLM failure modes in SDLC docs (invented
  velocity, fake dependency sign-offs, fabricated rollout dates, silent scope drops)
  mapped to the exact rule or guard that catches them.
- **Anchor:** `docs/EVIDENCE.md` already retells the 13 caught defects from the recorded
  pass — this is the **generalized, growing** catalog (see R8 for its feed).
- **Classification — 0.1.2 docs.**
- **Acceptance:** each entry = failure mode → the rule that catches it (cited to
  `CONVENTIONS.md`, the charter, or a playbook) → a real example from a fixture, a
  recorded run, or a field-feedback issue; no invented failure modes.

## R6. `docs/LIMITATIONS.md` — **0.1.2 (docs)**

- **Gap:** the review *is* effectively a limitations list, but the kit publishes none as
  such. Its four weaknesses are real and honest; publishing them first-class is exactly
  the "intellectual honesty" the review praises, and it pre-empts the objection.
- **What:** one page — prompt-level enforcement is not deterministic; manual paste/relay;
  destinations doc-derived and partly unobserved; static artifacts drift; one recorded
  runner; non-English docs absent. Each limit paired with the mitigation the kit ships
  (V2/V7, W6/W7, I6, W5/R1).
- **Classification — 0.1.2 docs.**
- **Acceptance:** every limit names its mitigation or its `[CONFIRM]`; no limit softened;
  links `REVIEWING-OUTPUT.md`, `TOOLS.md`, and I6.

## R7. Docs index / navigation — **0.1.2 (docs)**

- **Gap:** `docs/` has grown past fifteen files with no index; `START-HERE.md` is
  task-first, not a map of the docs themselves.
- **What:** `docs/README.md` (or a README section) indexing every `docs/` page by the
  question it answers.
- **Classification — 0.1.2 docs.**
- **Acceptance:** every `docs/` file is listed once with a one-line purpose; the root
  README tree and `PKG-README.md` link it.

## R8. Cookbook provenance mechanism — **0.1.2 (docs)**

- **Gap:** R5 needs a feed, or it will drift into invented failure modes.
- **What:** state that cookbook entries come only from (a) recorded runs, (b)
  field-feedback issues (F1), and (c) the `docs/EVIDENCE.md` retelling — never invented.
- **Classification — 0.1.2 docs** (a header section of R5).
- **Acceptance:** R5's header names its three sources; no entry without one.

## R9. `UPGRADING.md` 0.1.2 migration section — **0.1.2 (docs)**

- **Gap:** a user upgrading 0.1.1 → 0.1.2 should know what changed and that their
  `my-org.md` (and the new I1 overlays) are untouched.
- **What:** a short "What 0.1.2 adds" note; the **ownership table** gains the
  destination overlays to the "yours" column.
- **Classification — 0.1.2 docs.**
- **Acceptance:** the ownership table includes the I1 overlays; the note lists the new
  docs; no change to the upgrade mechanics.

## Related

- [`docs/UPGRADING.md`](../UPGRADING.md) — the ownership rule R9 extends
- [`docs/EVIDENCE.md`](../EVIDENCE.md) — the shipped defect retelling R5/R8 grow from
- [`.github/ISSUE_TEMPLATE/field-feedback.md`](../../.github/ISSUE_TEMPLATE/field-feedback.md) — the R2/R8 feed
- [`docs/START-HERE.md`](../START-HERE.md) — the task-first chooser R2 links
