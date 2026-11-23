# 06 — Open decisions: the user's calls

Theme: nothing in this file is scheduled until the owner decides. Taking a decision
means amending this file and the affected plan files first, then working the item per
the kit's rules (one skill per ticket, fixtures in the same change, status flips only
when exercised).

## G1. CLI prompt assembly — `sdlc-squad prompt --role sdm --skill sprint-planning-and-capacity`

Prints the four files concatenated in load order — one copy-paste instead of four.
Charter-compatible (offline, no network, no behavior beyond relocating committed
Markdown) and the single biggest friction reducer. But it is new CLI behavior: semver
says minor (0.2.0), and it contradicts this patch's "no CLI behavior changes" scope
line. Options: (a) keep 0.1.1 docs-only — C6's bundles already deliver one-paste loads
without runtime changes — and schedule the subcommand for 0.2.0 as an
assembler/regenerator for bundles; (b) stretch 0.1.1 to include it — then amend the
scope rules here, add a real test that the concatenated output matches the four files
in order, and record the evidence. **Decision owner: user.**

## G2. Description-polish pass across the 20 `description:` frontmatter fields

The `description:` field is the only harness-facing hook the repo has (no JSON
registries exist; `CHANGELOG.md`: "the field agent harnesses route on"). Polishing all
20 to trigger-rich, accurate one-liners would help harness discovery. It edits all 20
`SKILL.md` files against this patch's "no SKILL.md changes" rule; descriptions don't
affect steps or fixtures, but the rule was set to keep the patch provably inert.
**Standard alignment (from the scan, [08](08-competitive-landscape.md)):** the Agent
Skills spec requires `description` to state what the skill does **and when to use it**
— several of the 20 already do (e.g., `draft-prd`), and any polish pass should align
the rest. If G4 (below) is taken, this pass and its compatibility check overlap —
decide them together. **Decision owner: user.**

## G3. One real-paste spot check

Take one artifact (the C1 walkthrough's, for continuity) and paste it manually into a
real GitHub issue/PR and one real Confluence page; record what rendered and what broke
under `tests/results/` as a supplementary note. It is the first slice of ROADMAP v0.1.x
import validation; doing it inside 0.1.1 makes D1's paste-destination wording
evidenced. Options: do it in 0.1.1, or leave it with v0.1.x where the roadmap already
has it. **Decision owner: user.**

## G4. Agent Skills standard + skills.sh publication — the kit as installable skills

- **What:** make the 20 skills installable through the Agent Skills open standard
  (spec: `anthropics/skills` / agentskills.io) and discoverable on skills.sh (Vercel's
  registry) — `npx skills add deghosal-2026/sdlc-squad --skill <name>`.
- **Evidence (from [08](08-competitive-landscape.md), retrieved 2026-11-23):**
  - The standard's only required frontmatter is `name` (lowercase, hyphens, ≤64 chars)
    and `description` (what it does + when to use it). The kit already ships both on
    every skill — added in the usage-directory commit as "the field agent harnesses
    route on." The kit is closer to native than the old "zero marketplace wiring" note
    assumed.
  - Publication on skills.sh is telemetry-based: public repo, valid frontmatter,
    synchronized README, shared install command — no listing to apply for.
  - The ecosystem is large: `anthropics/skills` shows ~199k stars; skills.sh lists
    ~18 compatible agents (Claude Code, Cursor, Codex, Copilot, Windsurf, Gemini,
    Cline, OpenCode, VS Code, Zed, …) with all-time leaderboard counts in the
    hundreds of thousands to millions per top skill — PM-adjacent skills included
    (`to-prd` 351.6K, `to-issues` 339.1K, `retro` 389.7K, `triage` 1.1M —
    mattpocock/skills).
- **Open compatibility questions (verify before any restructure):**
  1. Extra frontmatter fields — the kit carries `role`, `status`, `created` beyond
     the standard's two. A filed validator bug suggests extended frontmatter can be
     rejected by strict validators. Options if rejected: move the extras into the
     body (a "Kit metadata" block) or verify tolerance per agent.
  2. Directory shape — the ecosystem convention is
     `skills/{skill-name}/SKILL.md`; the kit nests by role
     (`skills/<role>/<skill>/SKILL.md`). Matt Pocock's repo also nests by category
     (`skills/engineering/…`, `skills/productivity/…`), which suggests nesting is
     workable — but whether nested paths index on skills.sh is unverified. Check
     with `npx skills add deghosal-2026/sdlc-squad --list` (a user-run verification;
     the kit itself still makes no calls).
- **Options:** (a) verify first — run the `--list` check; if nested paths index and
  frontmatter passes, publication costs nothing; (b) compatibility pass — flatten
  paths and/or relocate extra frontmatter, a structural change with fixture-path
  consequences (tests/, prompt books, bundles) — at least a minor version; (c) stay
  pip/clone-only and revisit after v0.1.x validation.
- **Charter note:** distribution via skills.sh adds no network behavior to the kit —
  the CLI stays inert; users install files, nothing calls home. (skills.sh's own
  install telemetry is the registry's, not the kit's.)
- **Decision owner: user.**

## G5. Leverage mattpocock/skills (MIT) — three tracks, pick which to run

- **What:** incorporate Matt Pocock's skills — the most-installed engineering/PM skill
  set on skills.sh — into the sdlc-squad orbit, for free, with his copyrights retained.
  License verified MIT (`Copyright (c) 2026 Matt Pocock`, retrieved 2026-11-23 — full
  analysis and mapping in [09](09-external-skills-mattpocock.md)).
- **The three tracks:**
  1. **Interop (0.1.1-able, docs-only, zero copyright exposure):** a
     `docs/COMPANION-SKILLS.md` teaching the wrap pattern — kit conventions
     (`shared/system-conventions.md` + glossary) loaded *around* his skills, so his
     outputs inherit `[CONFIRM]` discipline, ID prefixes, ISO dates, and
     import-target blocks. His install base meets the kit's governance layer; nothing
     of his is copied.
  2. **Vendor-with-attribution (0.2.x, one skill per ticket):** adapt the genuine gap
     fillers into kit format — candidates: `triage` (binds the existing "Ask intake &
     prioritization" RACI row, PMT), `grilling` (an optional grill-first mode),
     `to-questionnaire` (async decision extraction). Each carries a Provenance block
     + root `THIRD_PARTY_NOTOTICES` file (see 09 for exact mechanics). MIT permits
     this; the kit's own evidence rules make it real work.
  3. **Pattern inspiration (no copying, any license):** fold his patterns into
     existing kit material — the grill-first preface, the PR one-way-door/blast-radius
     framing for `pr-plan-and-rollback-notes`, his user-invoked vs model-invoked
     taxonomy as input to G2/G4.
- **Refusals even though MIT allows:** his `implement`/`implement-spec`/`prototype`/
  `tdd`/`wizard`/`diagnosing-bugs` (code generation — charter: "Not a code
  generator"), `research` (network), `setup-matt-pocock-skills` (repo mutation),
  the personal-brand skills. Fine as *user companions*; never shipped inside the kit.
- **Decision owner: user** — which tracks run, and in which order. Track 1 is the
  recommended start: largest leverage, zero legal exposure, pure docs.

## G6. Destination format contracts — `shared/destinations/` (GitHub / Jira / Confluence)

- **What:** the format specs behind "paste destination" — the compatible-format half of
  the native-compatibility question (GitHub for code/issues, Jira for issues,
  Confluence for docs). Three files: `github.md` (GFM contract for issue/PR bodies —
  what renders natively, what to avoid), `jira.md` (two contracts: editor-paste for
  descriptions; the CSV shape for bulk import — header structure, row-per-story,
  quoting rules, with version specifics `[CONFIRM: verify against your instance on
  first import]` — Cloud and Data Center differ, and importers can be admin-disabled),
  `confluence.md` (editor-paste contract; what the existing no-HTML/no-emoji rules
  already protect).
- **Origin:** the kit says "Jira bulk import" and "Confluence page" but defines no
  format contract anywhere, and none has been validated — the same wound D1 names.
- **Options:** (a) contracts-as-docs in 0.1.1 — write the three spec files as pure
  documentation, no schema/skill binding changes (patch-safe; the schemas already
  imply most of the content); (b) defer whole to 0.2.0 with binding — skills then
  emit per-contract (e.g., `slice-mvp-and-stories` emits the CSV block per `jira.md`),
  which is schema-shape work; (c) fold into ROADMAP v0.1.x — write the contracts FROM
  the real pastes instead of ahead of them.
- **Note:** G3 (one real-paste spot check) is the natural evidence source for (a) —
  contracts written from observed pastes, not guesses. The env-var/token half of the
  native-compatibility question is refused forever (charter; H table).
- **Decision owner: user.**
