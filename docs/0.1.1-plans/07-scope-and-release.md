# 07 — Out of scope + release mechanics

Theme: the fence around the patch (what deliberately stays out, and why) and how the
release actually ships. The out-of-scope list applies to every file in this directory.

## H — Explicitly out of scope for 0.1.1

| Item | Where it belongs | Why not now |
|---|---|---|
| End-to-end run of one real feature through PRD → roadmap → sprint plan → design → tests, with real pastes into Jira/Confluence/GitHub and schema refinement where they miss | ROADMAP v0.1.x (open) | The roadmap's own next milestone, not a patch; the review's "validate the core promise" recommendation is the same work |
| Analysis of F1 feedback into success measures / pilot findings | v0.1.x | The template (F1) ships now; the findings need real users first |
| Cross-artifact carry fields (schema-level handoff data) | Minor version at earliest | Touches schemas and skill files; `CONVENTIONS.md` makes schema-shape work at least a minor. The user-facing relay recipe (F2) is in scope and covers the session-carry half. The playbook-edit variant — a "what changed from the source artifact?" continuity check in downstream skills — rides with it (same skill-file changes) |
| Artifact provenance footer (kit version · skill · date in the import-target block) | 0.2.0 schema candidate | Schema change; D3's resolution practice covers the user habit meanwhile |
| Formal `[CONFIRM]`-resolution schema convention | 0.2.0 schema candidate | The docs-only practice ships in D3; the schema encoding waits |
| skills.sh / Agent Skills publication | G4 decision ([06](06-open-decisions.md)) | The registry and standard are verified real (retrieved 2026-11-23); publication mechanics are known; compatibility questions remain open (frontmatter extras, nested paths) |
| Vendoring third-party skills (Matt Pocock's or any other source) | G5 decision ([06](06-open-decisions.md)), then one-skill-per-ticket in 0.2.x | License verified per source (mattpocock/skills: MIT, retrieved 2026-11-23); every adopted skill needs attribution + kit stencil + fixtures per the evidence rule; charter refusals still apply (no code-generation skills, no network skills) |
| Agensi / Clink marketplaces | Decision needed, not scheduled | Still unverified — not scanned; claims come from secondhand notes only. Several proposed paid-skill concepts (network calls, API clients, metered use) conflict with the charter's "No code, no API clients, no network" (`docs/EXTENDING.md`, What not to do) |
| Multi-model observed-run table | Grows with recorded runs | Not deferred as a claim risk (see D5's classification) — there simply is only one recorded runner today; rows are added as runs are recorded, never projected |
| Integrations, API clients, auto-import, telemetry, env-var/token guidance | Never | Charter: "not a client for anything"; `SECURITY.md`: any proposal adding a network call is rejected on charter grounds. The kit's only "setup" is the glossary — names, not credentials |
| Invented benchmark numbers, "industry standard" stats, velocity figures, untested-model claims | Never | `CONVENTIONS.md` honesty discipline; the D5 model notes are explicitly *not* this class — recorded observation and user-run checklists assert no number |
| Non-English documentation | Known limitation, noted not promised | No evidence of demand yet; noting it honestly in docs costs one line, promising it costs credibility |
| Operating modes (quick draft / standard / high-assurance) inside the playbooks | 0.2.0 candidate | Skill-step changes across playbooks; the grill-first preface (G5 Track 3 / [09](09-external-skills-mattpocock.md)) is the docs-only precursor |
| Destination format contracts (`shared/destinations/`: GitHub GFM · Jira CSV/editor · Confluence paste) | G6 decision ([06](06-open-decisions.md)) | Contracts-as-docs are 0.1.1-able (option a); binding skills to emit per-contract is schema-shape work (0.2.0, option b) |

## I — Release mechanics (when the work is done)

1. Fixes A/B go into the article draft; the corrected article publishes, closing the
   ROADMAP "Launch article — dev.to (open)" checkbox.
2. New files land: `usage/WALKTHROUGH.md`, `usage/RELAY.md`, `usage/bundles/` (20,
   generated), `docs/START-HERE.md`, `docs/REVIEWING-OUTPUT.md`,
   `docs/TROUBLESHOOTING.md`, `docs/MODELS.md`, `docs/EVIDENCE.md`,
   `docs/EXAMPLES.md`, `docs/EXPORTS.md` (with §Redaction), `docs/UPGRADING.md`
   (with the team-usage section, F4), `docs/TOOLS.md` (C8),
   `shared/glossary-and-org.EXAMPLE.md`,
   `.github/ISSUE_TEMPLATE/field-feedback.md`, and — if the 01 draft-home decision is
   in-repo — `docs/launch-article.md`. Edits land:
   `usage/USER-GUIDE.md` (five-minute run + pre-flight + data-path paragraph + D1
   line), `README.md` (why-not section, two-ways-to-run box, Mermaid relay diagram,
   links to new docs, layout tree update), `SECURITY.md` (Data path section),
   `PKG-README.md` (links, tagline, upgrade-safety note), `docs/EXTENDING.md`
   (Path 1 aligned with F3), `usage/prompts-*.md` (each book's load-order header gains
   the bundle alternative from C6).
3. If G5 Track 1 is taken: `docs/COMPANION-SKILLS.md` joins the list above (docs-only;
   no content of Matt Pocock's is copied — see [09](09-external-skills-mattpocock.md)).
   If G5 Track 2 is taken later (0.2.x): `THIRD_PARTY_NOTICES.md` at repo root carries
   the retained MIT notices per file. If G6 option (a) is taken:
   `shared/destinations/` (`github.md`, `jira.md`, `confluence.md`) joins the list.
4. Makefile: `make bundles` generates `usage/bundles/` from the canonical files;
   `make check-bundles` (regenerate + diff) joins the release checklist — a stale
   bundle fails the gate.
5. **Release gate (recorded, per the v0.1.0 run-log precedent):** before the tag and
   the upload — internal-link check across every new/edited doc; README layout tree
   vs disk; `make check-bundles` green; security: trufflehog + git audit re-run, plus
   a synthetic-data check on all new content (Meridian Outfitters only — no real org
   data anywhere); pre-publish re-fact-check of the article (A1–B7 acceptance lines
   re-verified against the repo); packaging gates: `make sync` → `python -m build` →
   `twine check` → `twine upload` → verify the CLI + kit tree from the public index;
   PyPI page render check (E1). Record the pass under `tests/results/` as
   `run-<date>-v0.1.1-docs.md` — a docs patch gets recorded evidence too.
6. The README layout tree gains every new file in the same commit — single source of
   truth (`CONVENTIONS.md`).
7. Version bump `0.1.0` → `0.1.1` in `pyproject.toml` / `sdlc_squad/__init__.py`;
   CHANGELOG entry in the same commit as the change (repo rule); ROADMAP gains a 0.1.1
   entry marked DONE, referencing this directory.
8. **Rollback:** a docs-only patch is reverted by commit; a bad PyPI upload is yanked
   from the index — last resort, one line in the gate note.
9. **Adoption signals (no telemetry):** PyPI download stats, GitHub stars/forks, and
   field-feedback issues (F1) are the observable metrics — read from public pages,
   never collected.
10. No `SKILL.md`, schema, or CLI changes — unless a G-decision is taken, in which case
    the plan files are amended before the work starts.
11. These plan files commit with the 0.1.1 CHANGELOG entry — items either done or
    re-pointed, never silently dropped.
