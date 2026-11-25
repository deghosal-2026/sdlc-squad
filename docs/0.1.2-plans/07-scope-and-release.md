# 07 — Out of scope + release mechanics

> **Status (2026-11-25):** the fence is set; release mechanics are not started.
> Master table: [`README`](README.md).

Theme: the fence around the patch (what deliberately stays out, and why), the things
that must not regress, and how the release actually ships. The out-of-scope list
applies to every file in this directory.

## S1 — Explicitly out of scope for 0.1.2 (forward-pointers to 0.2.0)

Rows pointing at `0.2.0` are **forward-pointers**: recorded so they are not lost, never
scheduled in this patch.

| Item | Where it belongs | Why not now |
|---|---|---|
| V1 `[CONFIRM]` linter / gatekeeper | 0.2.0 | New script **plus** schema-level marker rules (which markers are mandatory where) — schema-shape work |
| V3 arithmetic / capacity self-audit block | 0.2.0 | Changes the artifact shape SDM/TPM emit — schema/skill work |
| V4 confidence & ambiguity scoring | 0.2.0 | Per-section labels are part of the emitted artifact — schema/skill work |
| V6 model regression harness | 0.2.0 | A new cross-skill `tests/` artifact class with a runner |
| W1 `--copy` / `--out` | 0.2.0 (D1) | New CLI behaviour; 0.1.1's G1 was a deliberate exception, not the default |
| W2 `--context` assembly | 0.2.0 (D1) | New CLI behaviour |
| W3 `sdlc-squad doctor` | 0.2.0 (D1) | New CLI behaviour |
| W4 guided / structured intake | 0.2.0 | Changes a skill's steps (intake before draft) |
| W5 diff-aware update mode | 0.2.0 | A new output shape (change-set) — schema/skill work |
| I3 Jira CSV dry-run exporter | 0.2.0 | New script **and** binds the CSV contract to the schema |
| R4 skill maturity / verification badges | 0.2.0 (D3) | New frontmatter semantics across 20 `SKILL.md` |
| I2 read-only context pullers | **Refused** | A script calling `gh`/APIs is a network client — charter: "not a client for anything" (`SECURITY.md`) |

**Still-open 0.1.1 forward-pointers** ([`../0.1.1-plans/07`](../0.1.1-plans/07-scope-and-release.md), H),
unchanged and not absorbed here: destination **binding** (skills emitting per-contract);
the **artifact provenance footer**; the formal **`[CONFIRM]`-resolution schema**
convention; **operating modes** (quick/standard/high-assurance); **G5 Track 2** vendoring
(`triage`/`grilling`/`to-questionnaire` with attribution); and **cross-artifact carry
fields**.

## S2 — What must not regress (a guard, not a work item)

The review's four strengths, and the kit's own recorded honesty, are load-bearing. Every
0.1.2 change keeps them:

1. **`[CONFIRM]` as a defect, not "helpfulness"** — an artifact with zero markers and
   zero supplied inputs is still a defect (`CONVENTIONS.md`).
2. **Artifact relay over mega-prompts** — one role per session stays charter law
   (`WHAT-THIS-IS.md`); nothing here merges roles.
3. **Recorded evidence** — the fixtures and recorded runs remain the only basis for a
   `built` claim (`WHAT-THIS-IS.md` contract point 6); V5's failure table and R5's
   cookbook cite them and invent nothing.
4. **Zero-runtime, local-first** — no network, no API client, no telemetry, no
   credentials (`SECURITY.md`; `docs/TOOLS.md` §Never). I2 is refused precisely to keep
   this.

## S3 — Release mechanics (when the work is done)

1. **New files land:** `docs/LIMITATIONS.md` (R6), `docs/PILOT.md` (R2), the docs index
   (R7), `docs/launch-article.md` (X1, per G7), the destination overlay templates + page
   (I1), the validation ledger (I6), the cookbook (R5), and — if D2 — a workflow under
   `.github/workflows/`. **Edits:** `docs/REVIEWING-OUTPUT.md` (V2/V7),
   `docs/MODELS.md` (V5), `docs/EXPORTS.md` (I2 boundary + I1 cross-link),
   `shared/destinations/confluence.md` (I4) and `README.md` (I6 ledger link),
   `docs/UPGRADING.md` (R9), `docs/EXAMPLES.md` (R3), `usage/RELAY.md` (W7),
   `.github/` templates (I5), `README.md` / `PKG-README.md` (links).
2. **Release gate (recorded, per the v0.1.0/v0.1.1 run-log precedent)** — everything
   below runs *before* the tag and *before* any upload: `make gate` green
   (check-bundles · check-links · check-frontmatter · test);
   README layout tree vs disk; trufflehog + git audit re-run; a synthetic-data check on
   all new content (Meridian Outfitters only — no real org data). Then the
   packaging/upload sequence: `make sync` → `python -m build` → `twine check` → (on
   explicit go) `twine upload` → verify the CLI + kit tree from the public index → PyPI
   page render check. Record the pass under `tests/results/` as
   `run-<date>-v0.1.2.md`.
3. **Version bump** `0.1.1` → `0.1.2` in `pyproject.toml` and
   `sdlc_squad/__init__.py`; CHANGELOG entry in the same commit (repo rule); ROADMAP
   gains the 0.1.2 entry at release (referencing this directory), the same order the
   0.1.1 plan followed.
4. **Article publish (X1)** closes the ROADMAP "Launch article — dev.to (open)"
   checkbox; the article re-fact-check runs with it.
5. **Rollback:** a bad patch is reverted by commit; a bad PyPI upload is yanked — last
   resort, one line in the gate note.
6. **Adoption signals (no telemetry):** PyPI download stats, GitHub stars/forks, and
   field-feedback issues (F1) — read from public pages, never collected.

## Related

- [`../0.1.1-plans/07-scope-and-release.md`](../0.1.1-plans/07-scope-and-release.md) — the 0.1.1 fence and gate this mirrors
- [`06-open-decisions.md`](06-open-decisions.md) — the decisions that amend this fence
- [`../../tests/results/run-2026-11-23-v0.1.1.md`](../../tests/results/run-2026-11-23-v0.1.1.md) — the last recorded release
