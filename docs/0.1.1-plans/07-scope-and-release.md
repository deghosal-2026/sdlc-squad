# 07 — Out of scope + release mechanics

> **Status (2026-11-23):** **I done** — v0.1.1 shipped
> (`tests/results/run-2026-11-23-v0.1.1.md`); H is the out-of-scope / forward-pointer list,
> unchanged. Master table: [`README`](README.md).

Theme: the fence around the patch (what deliberately stays out, and why) and how the
release actually ships. The out-of-scope list applies to every file in this directory.

## H — Explicitly out of scope for 0.1.1

Rows pointing at `0.2.0` are **forward-pointers**: recorded so they are not lost,
never scheduled in this patch.

| Item | Where it belongs | Why not now |
|---|---|---|
| End-to-end run of one real feature through PRD → roadmap → sprint plan → design → tests, with real pastes into Jira/Confluence/GitHub and schema refinement where they miss | ROADMAP v0.1.x (open) | The roadmap's own next milestone, not a patch; the review's "validate the core promise" recommendation is the same work |
| Analysis of F1 feedback into success measures / pilot findings | v0.1.x | The template (F1) ships now; the findings need real users first |
| Cross-artifact carry fields (schema-level handoff data) | Minor version at earliest | Touches schemas and skill files; `CONVENTIONS.md` makes schema-shape work at least a minor. The user-facing relay recipe (F2) is in scope and covers the session-carry half. The playbook-edit variant — a "what changed from the source artifact?" continuity check in downstream skills — rides with it (same skill-file changes) |
| Artifact provenance footer (kit version · skill · date in the import-target block) | 0.2.0 schema candidate | Schema change; D3's resolution practice covers the user habit meanwhile |
| Formal `[CONFIRM]`-resolution schema convention | 0.2.0 schema candidate | The docs-only practice ships in D3; the schema encoding waits |
| skills.sh / Agent Skills publication | **Declined for now (G4, 2026-11-23)** | Distribution stays GitHub + PyPI; no separate skill publication. Revisit after v0.1.x validation |
| Vendoring third-party skills (Matt Pocock's or any other source) — G5 Track 2 | 0.2.x, one skill per ticket (**G5 decided: run**) | License verified (mattpocock/skills: MIT, retrieved 2026-11-23); every adopted skill needs attribution + kit stencil + fixtures per the evidence rule; charter refusals still apply (no code-generation, no network skills) |
| Agensi / Clink marketplaces | Decision needed, not scheduled | Still unverified — not scanned; claims come from secondhand notes only. Several proposed paid-skill concepts (network calls, API clients, metered use) conflict with the charter's "No code, no API clients, no network" (`docs/EXTENDING.md`, What not to do) |
| Multi-model observed-run table | Grows with recorded runs | Not deferred as a claim risk (see D5's classification) — one recorded runner today; rows added as runs are recorded, never projected |
| Integrations, API clients, auto-import, telemetry, env-var/token guidance | Never | Charter: "not a client for anything"; `SECURITY.md`: any proposal adding a network call is rejected on charter grounds. The kit's only "setup" is the glossary — names, not credentials |
| Invented benchmark numbers, "industry standard" stats, velocity figures, untested-model claims | Never | `CONVENTIONS.md` honesty discipline; the D5 model notes are explicitly *not* this class — recorded observation and user-run checklists assert no number |
| Non-English documentation | Known limitation, noted not promised | No evidence of demand yet; noting it honestly in docs costs one line, promising it costs credibility |
| Operating modes (quick draft / standard / high-assurance) inside the playbooks | 0.2.0 candidate | Skill-step changes across playbooks; the grill-first preface (G5 Track 3 / [09](09-external-skills-mattpocock.md)) is the docs-only precursor |
| Destination format contracts — **binding skills to emit per-contract** | 0.2.0 | **Drafting the contract docs is now in scope (G6, 2026-11-23)** — `shared/destinations/` written from fetched GitHub/Atlassian specs; only the schema/skill binding waits |

## I — Release mechanics (when the work is done)

1. **After** the tag and uploads: fixes A/B go into the article draft (home per G7); the
   corrected article publishes, closing the ROADMAP "Launch article — dev.to (open)"
   checkbox (G7 — build and ship first).
2. New files land: `usage/WALKTHROUGH.md`, `usage/RELAY.md`, `usage/bundles/` (20,
   generated), `docs/START-HERE.md`, `docs/REVIEWING-OUTPUT.md`,
   `docs/TROUBLESHOOTING.md`, `docs/MODELS.md`, `docs/EVIDENCE.md`,
   `docs/EXAMPLES.md`, `docs/EXPORTS.md` (with §Redaction), `docs/UPGRADING.md`
   (with the team-usage section, F4), `docs/TOOLS.md` (C8),
   `docs/COMPANION-SKILLS.md` (G5 T1), `shared/destinations/` (`github.md`, `jira.md`,
   `confluence.md` — G6), `shared/glossary-and-org.EXAMPLE.md`,
   `.github/ISSUE_TEMPLATE/field-feedback.md`. Edits land:
   `usage/USER-GUIDE.md` (five-minute run + pre-flight + data-path paragraph + D1
   line), `README.md` (why-not section, two-ways-to-run box, Mermaid relay diagram,
   links to new docs, layout tree update), `SECURITY.md` (Data path section),
   `PKG-README.md` (links, tagline, upgrade-safety note, the new CLI subcommand),
   `docs/EXTENDING.md` (Path 1 aligned with F3), `usage/prompts-*.md` (load-order header
   gains the bundle alternative, C6), the 20 `SKILL.md` `description:` fields (G2 — no
   steps or fixtures), and `sdlc_squad/cli.py` + its test (G1).
3. Later (0.2.x): G5 Track 2 vendors `triage`/grilling/`to-questionnaire` with a root
   `THIRD_PARTY_NOTICES.md`; G6's schema/skill binding lands then too. Neither ships in
   0.1.1.
4. Build: `scripts/build-bundles.sh` + the Makefile's `make bundles` generate
   `usage/bundles/` from the canonical files; `make check-bundles` (regenerate + diff)
   joins the release checklist — a stale bundle fails the gate.
5. **Release gate (recorded, per the v0.1.0 run-log precedent):** everything below runs
   *before* the tag and *before* any upload — internal-link check across every
   new/edited doc; README layout tree vs disk; `make check-bundles` green; the G1 CLI
   test (assembled output == the four files in order); security: trufflehog + git audit
   re-run, plus a synthetic-data check on all new content (Meridian Outfitters only — no
   real org data anywhere). Then the **packaging/upload sequence**, still gated on the
   above: `make sync` → `python -m build` → `twine check` → (on explicit go)
   `twine upload` → verify the CLI + kit tree from the public index → PyPI page render
   check (E1). Record the pass under `tests/results/` as `run-<date>-v0.1.1.md`. The
   article re-fact-check runs post-ship with the article (G7).
6. G3's real-paste results (GitHub + Confluence + Jira + CSV) land under `tests/results/`
   as a supplementary note and feed D1's wording.
7. The README layout tree gains every new file in the same commit — single source of
   truth (`CONVENTIONS.md`).
8. Version bump `0.1.0` → `0.1.1` in `pyproject.toml` / `sdlc_squad/__init__.py`;
   CHANGELOG entry in the same commit as the change (repo rule); ROADMAP gains a 0.1.1
   entry marked DONE, referencing this directory. **Semver note (G1/G2):** a new CLI
   behavior would normally be a minor; the owner chose to ship it as 0.1.1.
9. **Rollback:** a bad patch is reverted by commit; a bad PyPI upload is yanked from the
   index — last resort, one line in the gate note.
10. **Adoption signals (no telemetry):** PyPI download stats, GitHub stars/forks, and
    field-feedback issues (F1) are the observable metrics — read from public pages,
    never collected.
11. These plan files were committed as planning docs (`5d5b8de`); the 0.1.1 CHANGELOG
    entry lands with the release commit and references them — items either done or
    re-pointed, never silently dropped.
