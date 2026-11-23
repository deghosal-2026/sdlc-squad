# ROADMAP.md — sdlc-squad build order

The kit builds in the order the charter sets: shared contracts first, roles next, the core loop of
skills, a real feature run end-to-end, then the rest. Each milestone lands before the next starts.

## Milestones

### v0.0.1 — private scaffold (2026-11-22) — DONE

- [x] Repo created, private, MIT-licensed
- [x] `shared/system-conventions.md` + `shared/glossary-and-org.md`
- [x] Five canonical output schemas in `shared/output-schemas/`
- [x] Four role personas in `roles/`
- [x] Eighteen skill skeletons in `skills/` (`status: planned`), each naming its `shared/raci.md` row
- [x] OSS-mandatory community files (CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, CHANGELOG)

### v0.1.0 — the full kit (all 20 skills) — DONE 2026-11-22

Every skill shipped with its full step playbook, its fixture
(`tests/<role>/<skill>/fixture.md`), and its recorded run
(`tests/results/run-2026-11-22-v0.1.0.md` — 20/20 pass; 13 defects found and fixed in the pass):

- [x] PMT (6): draft-prd · slice-mvp-and-stories · define-success-metrics ·
      customer-discovery-and-synthesis · survey-design · prioritize-asks
- [x] TPM (4): program-roadmap-and-deps · risk-raid-and-mitigations · release-readiness-check ·
      program-status-review
- [x] SDM (5): sprint-planning-and-capacity · standup-execution · scope-cut-and-tradeoffs ·
      operational-health-review · sprint-retro
- [x] SDE (5): technical-design-and-breakdown · generate-test-ideas-and-cases ·
      pr-plan-and-rollback-notes · design-and-code-reviews · deploy-plan-and-release
- [x] RACI: 21 decision rows, one Accountable each; every skill bound to its row(s); mirrors
      verified across `shared/raci.md` and all four role files
- [x] History audit: 4 commits scanned for secrets and private material — clean
- [x] Repo flipped **public** as part of this release; LICENSE, issue templates, and PR
      template verified rendering on the public repo
- [x] Released: tag `v0.1.0` + GitHub release

### v0.1.x — end-to-end validation

- [ ] Run one real feature/initiative through the core loop (PRD → roadmap → sprint plan → design
      → tests), inspect every artifact against its import target (real Confluence page, real Jira
      issue, real GitHub PR), and refine the schemas where they miss.

### Launch article — dev.to (open)

- [ ] Publish the kit's launch article (house pattern: every kit ships with its piece) —
      drafted from the kit's own worked examples and recorded runs.

## Rules

- One skill per ticket; fixtures and examples land in the same change as the skill.
- `status: built` only after the skill's acceptance is actually exercised, never on static review.
- `CHANGELOG.md` entry in the same commit as the change.