# ROADMAP.md — sdlc-squad build order

The kit builds in the order the charter sets: shared contracts first, roles next, the core loop of
skills, a real feature run end-to-end, then the rest. Each milestone lands before the next starts.

## Milestones

### v0.0.1 — private scaffold (2026-11-22) — DONE

- [x] Repo created, private, MIT-licensed
- [x] `shared/system-conventions.md` + `shared/glossary-and-org.md`
- [x] Five canonical output schemas in `shared/output-schemas/`
- [x] Four role personas in `roles/`
- [x] Twelve skill skeletons in `skills/` (`status: planned`)
- [x] OSS-mandatory community files (CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, CHANGELOG)

### v0.1.0 — the core loop

One skill per role, built in ticket order, each with fixtures/examples and `status: built`:

- [ ] `pmt/draft-prd`
- [ ] `tpm/program-roadmap-and-deps`
- [ ] `sdm/sprint-planning-and-capacity`
- [ ] `sde/technical-design-and-breakdown`
- [ ] `sde/generate-test-ideas-and-cases`

### v0.1.x — end-to-end validation

- [ ] Run one real feature/initiative through the core loop (PRD → roadmap → sprint plan → design
      → tests), inspect every artifact against its import target (real Confluence page, real Jira
      issue, real GitHub PR), and refine the schemas where they miss.

### v0.2.0 — the remaining seven skills

- [ ] `pmt/slice-mvp-and-stories`
- [ ] `pmt/define-success-metrics`
- [ ] `tpm/risk-raid-and-mitigations`
- [ ] `tpm/release-readiness-check`
- [ ] `sdm/scope-cut-and-tradeoffs`
- [ ] `sdm/operational-health-review`
- [ ] `sde/pr-plan-and-rollback-notes`

### v1.0.0 — OSS release

- [ ] Flip the repo public; verify community files render (README badges, issue templates, PR
      template).
- [ ] Verify no private material in history (org names, real tickets, real people).
- [ ] Publish the launch article (per the house pattern: every kit ships with its piece).

## Rules

- One skill per ticket; fixtures and examples land in the same change as the skill.
- `status: built` only after the skill's acceptance is actually exercised, never on static review.
- `CHANGELOG.md` entry in the same commit as the change.