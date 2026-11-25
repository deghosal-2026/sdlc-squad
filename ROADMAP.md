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

### v0.1.1 — first-run, destinations, paste-verified targets — DONE 2026-11-23

- [x] First-run experience: `usage/WALKTHROUGH.md`, the five-minute run in
      `usage/USER-GUIDE.md`, `docs/START-HERE.md`, `shared/glossary-and-org.EXAMPLE.md`
- [x] Session bundles (`usage/bundles/`, 20) + `scripts/build-bundles.sh` and
      `make bundles` / `make check-bundles`
- [x] Upgrade safety (`docs/UPGRADING.md`): keep the org glossary outside the kit
- [x] Trust surface: `docs/REVIEWING-OUTPUT.md`, `TROUBLESHOOTING.md`, `MODELS.md`,
      `EVIDENCE.md`, a Data-path section, and `docs/EXPORTS.md` (input + redaction)
- [x] Destination contracts `shared/destinations/{github,jira,confluence}.md`
- [x] CLI: `sdlc-squad prompt` + `tests/cli/test_prompt.py` (`make test`)
- [x] The 20 `SKILL.md` descriptions now state what + when
- [x] Real-destination spot check: GitHub, Jira editor, Jira CSV import, Confluence page
      all observed — `tests/results/run-2026-11-23-g3-real-paste.md`
- [x] `docs/0.1.1-plans/` — the patch plan with a living build status
- [ ] Launch article — still open (deferred to after this release; below)

### v0.1.2 — the field-test response — DONE 2026-11-25

- [x] The **X2 field test** (`field-test/`): four real OSS features — Kubernetes KEP-1287,
      Grafana #77704, Deno #8327, Rust RFC 3137 — run through the loop with the project's own
      record held back as an answer key; the deep review is `field-test/FINDINGS.md`
- [x] **Real-paste half**: GitHub, Jira (editor + CSV), and Confluence observed —
      `tests/results/run-2026-11-25-x2-real-paste.md`
- [x] The **11 kit gaps** folded in (0.1.2): `technical-design-doc`, `confluence-prd-or-rfc`,
      and `jira-epic-and-stories` amended; **two new schemas** — `program-roadmap.md` (the sixth)
      and `decision-record.md`; a **cross-team mode** in `usage/RELAY.md`
- [x] The trust & adoption docs from the external review (V2·V5·V7·V8·V9, W6·W7·W8,
      I1·I4·I5·I6·I7, R1·R2·R3·R5–R9, CI) — see `docs/0.1.2-plans/`
- [x] `docs/0.1.2-plans/` — the plan with a living build status and the remediation tracker

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