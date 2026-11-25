# CHANGELOG.md

All notable changes to sdlc-squad are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); releases are tagged, starting at
v0.1.0.

## [0.1.1] — 2026-11-23

### Added — 2026-11-23 (0.1.1 work in progress)

- `docs/0.1.1-plans/` — the v0.1.1 patch plan, split by theme (launch article, first-run
  experience, trust surface, storefront, lifecycle, open decisions, scope + release,
  competitive landscape, mattpocock/skills analysis), with a living build-status table.
- `docs/UPGRADING.md` — your files vs the kit's: keep the filled org glossary **outside**
  the kit (`my-org.md`) so upgrades never clobber it; pip + clone paths; team usage.
- `shared/destinations/` — paste-destination contracts `github.md`, `jira.md`,
  `confluence.md`, written from the vendor specs (doc-derived; not yet
  instance-validated — G3 closes the `[CONFIRM]`s).
- `shared/glossary-and-org.EXAMPLE.md` — a filled (fictional) glossary example.
- `usage/bundles/` — 20 generated session bundles, plus `scripts/build-bundles.sh` and
  the Makefile's `make bundles` / `make check-bundles` (freshness gate).
- `usage/USER-GUIDE.md` — a five-minute first run; the load step now points at your own
  `my-org.md`. `docs/EXTENDING.md` and `PKG-README.md` aligned to the same convention;
  the four prompt books' load-order headers name the bundle alternative.
- `docs/` — `START-HERE.md` (task chooser + scenario recipes), `EXPORTS.md` (getting input
  in + a redaction recipe), `REVIEWING-OUTPUT.md`, `TROUBLESHOOTING.md`, `MODELS.md`,
  `EVIDENCE.md`, `EXAMPLES.md`, `TOOLS.md` (supported & adaptable matrix),
  `COMPANION-SKILLS.md` (wrapping other skill sets in kit conventions).
- `usage/WALKTHROUGH.md` (one full run), `usage/RELAY.md` (role-to-role hand-off),
  `.github/ISSUE_TEMPLATE/field-feedback.md` (opt-in feedback).
- CLI: `sdlc-squad prompt --role <role> --skill <skill>` prints a skill's full session
  load, concatenated; `tests/cli/test_prompt.py` (`make test`) proves it equals the four
  canonical files, in order. The default CLI output now names the subcommand.
- `README` — two-ways-to-run, a "why not just ask the chat directly?" section, and the
  Mermaid relay loop; `SECURITY.md` — a Data-path section (kit vs. provider);
  `PKG-README.md` — links to the new docs, and the upgrade-safety note.
- The 20 `SKILL.md` `description:` fields now state what each skill does **and when to
  use it** — no step or fixture changes.
- `tests/results/run-2026-11-23-g3-real-paste.md` — the G3 real-destination spot check:
  GitHub issue paste, Jira Cloud editor paste, the Jira CSV bulk import, **and the
  Confluence Cloud page paste all observed** — headings/tables/bold/lists convert,
  `[CONFIRM: …]` literal everywhere; CSV: 3/3 stories landed, priority values must match
  the instance's scheme (P1/P2 → Medium), Size needs a custom-field target (landed in
  Labels). `shared/destinations/github.md` / `jira.md` / `confluence.md` `[CONFIRM]`s
  closed accordingly; the import-target wording in README and USER-GUIDE updated to say
  what is paste-verified vs. still intended. (Jira Data Center and Confluence's
  storage-format path remain unobserved.)
- `docs/assets/social-preview.png` (1280×640) + `docs/assets/social-preview.svg` — the
  repo social-preview card (E3), listed in the README layout tree; uploaded to the repo
  settings by the owner.

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

### Added — 2026-11-25 (0.1.2 work in progress)

- `docs/REVIEWING-OUTPUT.md` — claim-to-source tagging (review by exception), the
  assumption-vs-fact separation, the clean-artifact rule (when zero `[CONFIRM]`s is
  correct), and a PII/hostname pre-paste check (V2 · V7 · V8 · V9).
- `docs/ANTI-PATTERNS.md` — the failure-mode catalog mapped to the rule that catches each,
  seeded from the recorded pass; every entry traces to a recorded run, field feedback, or
  `EVIDENCE.md` (R5 · R8).
- `scripts/check-links.py` + `scripts/check-frontmatter.py` + `tests/docs/test_doc_checks.py`
  and the Makefile's `check-links` / `check-frontmatter` targets; `make test` now runs the
  doc-check tests alongside the CLI test (I7).
- `docs/DESTINATION-PROFILES.md` — the instance-profile pattern (`my-jira.md`,
  `my-confluence.md`, `my-github.md`), kept outside the kit, mapping priority names,
  estimate unit, and formatting rules (I1).
- `docs/GITHUB-TEMPLATES.md` — ready-to-copy `.github/` PR and design-issue templates
  aligned with the SDE skills (I5).
- `shared/destinations/confluence.md` — callouts / status-badge / code-block guidance (I4);
  `shared/destinations/README.md` — the observed/unobserved **validation ledger** (I6).
- `usage/RELAY.md` — the **Handoff Block** (from / carried-open / next), making a role
  hand-off mechanical (W7); `usage/FEATURE-RELAY.md` — the order-status feature threaded
  PMT → TPM → SDM → SDE (W6).
- `docs/TROUBLESHOOTING.md` §4 — the **long-load recipe** (which files are droppable, which
  are not); `docs/MODELS.md` cross-links it (W8).
- `Makefile` — a `gate` target aggregating the release checks (`check-bundles` ·
  `check-links` · `check-frontmatter` · `test`); `README.md` and `docs/START-HERE.md` link
  `usage/FEATURE-RELAY.md` (closes the I7 gate and the W6 README-link acceptance).

### Added — 2026-11-25 (0.1.2 planning)

- `docs/0.1.2-plans/` — the v0.1.2 plan, split by theme, derived from the external
  review of the launch post + this repo at v0.1.1: verification (`01`), workflow (`02`),
  integrations (`03`), adoption (`04`), carry-over (`05`), open decisions (`06`),
  scope + release (`07`), the review reproduced and enumerated (`08`), the gaps the
  review left unnamed (`09`), and the sequenced implementation plan with a Done (Y/N)
  tracker (`10`). Every review idea is classified **0.1.2 (docs-only)** /
  **0.2.0 (forward-pointer)** / **refused**, per `CONVENTIONS.md` — no schema, skill, or
  CLI change is scheduled in the patch without a decision.

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