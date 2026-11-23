# CHANGELOG.md

All notable changes to sdlc-squad are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the kit uses no semantic version tags
until its first release.

## [0.1.0] — 2026-11-22

### Added — the full kit

- All 20 skills built: full step playbooks replacing the skeletons, frontmatter `status: built`.
- New since the scaffold: PMT discovery trio (`customer-discovery-and-synthesis`,
  `survey-design`, `prioritize-asks`); TPM `program-status-review` (bi-weekly/monthly R/Y/G
  against objectives/Jira milestones, fixed definitions); SDM `sprint-retro` (last 2 sprints'
  done tickets → retro + action items) and `standup-execution` (daily round format + blocker
  log with aging/escalation); SDE `design-and-code-reviews` (author gate + reviewer pass +
  etiquette) and `deploy-plan-and-release` (deploy/release split, canary ladder,
  automatic-first rollback triggers, flag ledger).
- `tests/`: 20 synthetic fixtures (input + expected artifact + checks list per skill) and
  `tests/results/run-2026-11-22-v0.1.0.md` — 20/20 pass, 13 defects found and fixed in the
  same pass, none shipped open. `tests/README.md` added.
- RACI: 19 → 21 decision rows (`Sprint retrospective & action items`;
  `Standup execution & blocker log`); mirrors verified in `shared/raci.md` and all four role
  files; every skill's `## RACI row` section bound to its row(s).
- Roles: SDM routing + produces now cover standup and retro artifacts.
- ROADMAP restructured: v0.1.0 is the full kit (v0.2.0 absorbed); README badge, tree, and
  skill table now say 20/built.

## [Unreleased]

### Added — 2026-11-22

- Initial private scaffold: repo, MIT license, community files
  (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT).
- Kit governance: `WHAT-THIS-IS.md` (charter), `AGENTS.md`, `CONVENTIONS.md`, `ROADMAP.md`,
  this changelog, `USER-GUIDE.md`.
- Shared contracts: `shared/system-conventions.md`, `shared/glossary-and-org.md`.
- Five canonical output schemas in `shared/output-schemas/`: `confluence-prd-or-rfc.md`,
  `jira-epic-and-stories.md`, `sprint-plan-and-capacity.md`, `technical-design-doc.md`,
  `test-plan-and-cases.md`.
- Four role personas in `roles/`: `pmt.md`, `tpm.md`, `sdm.md`, `sde.md`.
- Twelve skill skeletons in `skills/` — frontmatter `status: planned`, purpose, required inputs,
  output bindings, import targets. Not yet playable playbooks; see ROADMAP.md for the build order.

### Changed — 2026-11-22 (roles restructure)

- All four roles (`roles/`) restructured onto the canonical `roles/_TEMPLATE.md` format:
  when-to-load routing, consumes/produces/depends-on contracts, per-role RACI column,
  reviews-in-others'-artifacts, failure modes & corrections, session behavior, tone &
  vocabulary, worked examples (synthetic, `[CONFIRM]`-demonstrating).
- Added `shared/raci.md` — the canonical decision-rights matrix: one **A** per decision, C/I
  kept minimal, the user ratifies every A. Each role file mirrors only its own column; the same
  change updates both (the mirror rule).
- `AGENTS.md` + `CONVENTIONS.md`: template rule, RACI mirror rule, session load order.
- README: layout tree now shows `shared/raci.md` and `roles/_TEMPLATE.md`.

### Added — 2026-11-22 (research + coverage pass)

- Six skills added to close the RACI↔skill match (every A/R row now has a skill; every skill
  names its row): PMT `customer-discovery-and-synthesis` (Mom Test grounding: past behavior,
  never hypotheticals), `survey-design` (bias-checked instrument + read-back),
  `prioritize-asks` (RICE — Reach × Impact × Confidence ÷ Effort — or the org's own stated
  framework); TPM `program-status-review` (bi-weekly/monthly cadence, fixed R/Y/G
  definitions: green on track, yellow named risk + open mitigation, red milestone missed/no
  credible path — never a mood); SDE `design-and-code-reviews` (author self-review first,
  small reviewable diffs, `nit:` etiquette), `deploy-plan-and-release` (deploy≠release split,
  canary stages, automatic-first rollback triggers, flag owner + removal date).
- All 18 `SKILL.md` files now carry a `## RACI row` section bound to `shared/raci.md`;
  `program-roadmap-and-deps` names its two rows (milestone sequence + dependency
  commitments).
- Roles enriched from the same research: PMT discovery/prioritization lens + interview drift
  correction; TPM program-review routing, status-report handoff, R/Y/G-with-evidence lens,
  yellow-as-a-feeling drift correction; SDM consumes the launch checklist (mirror gap
  closed); SDE review/deploy routing, small-diffs + flag-loan lens, rehearsed-rollback drift
  correction, review/deploy produces.
- README skills badge/table 12 → 18; ROADMAP v0.2.0 now lists all thirteen non-core skills.