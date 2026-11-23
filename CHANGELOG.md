# CHANGELOG.md

All notable changes to sdlc-squad are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); releases are tagged, starting at
v0.1.0.

### Added — 2026-11-22 (detailed test log)

- `tests/results/run-2026-11-22-v0.1.0.md` expanded from summary to **detailed log**: per-skill
  walkthrough (fixture, input, playbook steps, 97 checks itemized, recorded-pass defect, this-run
  verdict), structural gates (fixtures/frontmatter/RACI/prompt books), packaging gates (build,
  twine, wheel layout, sdist, clean-venv install + CLI — upload still deferred), security gates
  (trufflehog 0/0 on the full 11-commit history, git audit clean). Verdict: 20/20, zero open
  defects.

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

### Added — 2026-11-22 (usage directory + executable frontmatter)

- `usage/` created: `USER-GUIDE.md` moved in (links fixed in README, SUPPORT, CHANGELOG), plus
  four prompt books — `prompts-pmt.md`, `prompts-tpm.md`, `prompts-sdm.md`, `prompts-sde.md` —
  one ready-to-paste prompt per skill, all 20, with load order, realistic sample input, and
  import targets.
- Frontmatter made harness-executable: `description:` added to all 20 `SKILL.md` files (the
  field agent harnesses route on; name/role/status/created were already consistent).
- `skills/_TEMPLATE.md` added — the canonical skill stencil (frontmatter incl. description,
  contracts, steps, output binding, import target, worked example) with the standing rules.

### Changed — 2026-11-22 (public flip, in v0.1.0)

- The repo flipped **public** as part of v0.1.0 (the former v1.0.0 milestone absorbed into
  it): history audited clean (no secrets, no private material), community files verified
  rendering on the public repo (LICENSE, issue templates, PR template), release notes
  updated. README, AGENTS, ROADMAP, and this changelog re-framed: v0.1.0 is the major public
  release. Open: v0.1.x end-to-end validation; the dev.to launch article.

## [Unreleased]

### Added — 2026-11-22 (PyPI distribution)

- `sdlc-squad` on [PyPI](https://pypi.org/project/sdlc-squad/): `pyproject.toml` +
  `PKG-README.md` + `MANIFEST.in` + `Makefile` (`make sync` copies the kit into the package
  as a generated, gitignored build artifact — the repo root stays the single canonical copy).
- `sdlc_squad/` — the Python package: `sdlc-squad` CLI prints the kit path and the per-session
  load order. No server, no runner, no telemetry — a file distribution.
- `usage/USER-GUIDE.md` + README quick start: the optional `pip install sdlc-squad` path,
  alongside clone-and-paste. PyPI badge added.
- **v0.1.0 published to PyPI** (user's go, ~22:40 PST): `twine upload` → live at
  https://pypi.org/project/sdlc-squad/0.1.0/ → verified from the public index (JSON API +
  clean-venv `pip install sdlc-squad` → CLI exit 0). Test log section 3 records the ship +
  post-ship verification.

### Added — 2026-11-22 (docs + README tree fix)

- `WHAT-THIS-IS.md` (charter) caught up with the kit: twelve → twenty skills (PMT 6 · TPM 4 ·
  SDM 5 · SDE 5), persona enumeration now includes the consumes/produces/depends-on contracts
  and the RACI column + one-role-per-session rule, and the skill contract gains point 6 —
  `built` means fixture + recorded run, a status without evidence is a defect.
- README status badge: `private scaffold` → `v0.1.0 public` (stale from the scaffold era — the
  Status section, tree, skills table, and license line were already current).
- `docs/EXTENDING.md`: how to expand and customize — four paths (customize for your org via
  `shared/glossary-and-org.md`; add a skill; add a role; change a schema), the five standing
  rules (one canonical copy, mirror rule, CONFIRM-over-invention, honest statuses, one role
  per session), and the what-not-to-do list. Linked from CONTRIBUTING and the usage guide.
- README layout tree caught up with the repo: `tests/` (fixtures + recorded runs) and
  `skills/_TEMPLATE.md` (the skill stencil) added to the tree — both existed on disk since the
  v0.1.0 and usage commits but were missing from the tree. Badge (20 built), status (public),
  skills table, and usage/ block verified current against the audit.

### Added — 2026-11-22

- Initial private scaffold: repo, MIT license, community files
  (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT).
- Kit governance: `WHAT-THIS-IS.md` (charter), `AGENTS.md`, `CONVENTIONS.md`, `ROADMAP.md`,
  this changelog, `usage/USER-GUIDE.md`.
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