# 02 — First-run experience: install → first artifact

> **Status (2026-11-23):** C2, C4, C6 **done**; C1, C3, C5, C7, C8 **not started**.
> Master table: [`README`](README.md).

Theme: everything between "landed on the README/PyPI page" and "first valid artifact in
front of me." The research pass's measured core fact: a session load today is
~340–370 lines pasted in strict order, every session — these items kill that cost.

## C1. The gold run — `usage/WALKTHROUGH.md`

- **What:** one complete, start-to-finish example: the messy raw input → the four files
  in load order → the clarifying questions and their answers → the finished artifact
  with its `[CONFIRM]`s → how the user resolves each one → the import-target block and
  where the artifact lands.
- **Anchor (zero invention):** `sdm/sprint-planning-and-capacity`, told with material
  that already exists in the repo. The sample input in `usage/prompts-sdm.md` §1 (Sprint
  14, 2026-12-07 → 2026-12-18; engineers A–F; PTO; ~6h/week meetings; weekly on-call;
  3 carry-overs; M1 8d, flaky-test fix 2d, dark mode unestimated) is the same story as
  the committed fixture `tests/sdm/sprint-planning-and-capacity/fixture.md`, and the
  recorded run (`tests/results/run-2026-11-22-v0.1.0.md` §1.11) walked it 5/5 checks
  clean. The walkthrough narrates that recorded run — it invents nothing.
- **Content shape:** (1) the raw input paste; (2) the four files named in load order;
  (3) the ≤3 clarifying questions the skill asks, with the answers used; (4) the
  emitted artifact — shown arithmetic, commitment split, risk flags; (5) the
  `[CONFIRM]` list and how each is resolved with real facts before pasting; (6) the
  import-target block: Confluence sprint note, Jira backlog.
- **Why:** the product is the artifact, and no doc today shows a whole run (gap review
  P1: "no demonstrated end-to-end customer workflow… publish a complete worked
  example"). Every fact traces to committed synthetic material (`tests/README.md`:
  every company, person, path, ticket, and date in a fixture is invented).
- **Acceptance:** a reader who has never opened the repo follows install → pasted
  artifact using only this doc; every fact in it traces to the committed fixture or
  prompt book; at least one `[CONFIRM]` is shown resolved; linked from README,
  USER-GUIDE, and PKG-README.

## C2. The five-minute first run — `usage/USER-GUIDE.md` section

- **What:** a numbered recipe right after "The 60-second version" that names **one**
  starter skill — `sdm/sprint-planning-and-capacity`, the same story as C1 so the docs
  read as one thread. `pip install sdlc-squad` → run `sdlc-squad` (it prints the path
  and the load order) → paste the four files it names (or the bundle, C6) → paste the
  sample input from `usage/prompts-sdm.md` §1 → answer the questions → one artifact.
  States plainly: no real data needed — the sample company (Meridian Outfitters) is
  fictional.
- **Pre-flight line (real runs):** four files in order (or one bundle) · glossary state
  known — template is fine for a trial, your `my-org.md` (F3) for real work · inputs
  redacted per `docs/EXPORTS.md` §Redaction.
- **Why:** today nothing tells a newcomer *which* skill to try first; the prompt books
  already carry the sample, so the missing piece is one guided path (gap P1: "first-use
  setup asks customers to do too much… include a minimal 'try it in five minutes'
  example").
- **Acceptance:** a cold-start user reaches one valid artifact using only committed
  files and this section; the path adds no new facts; "no real data needed" is stated.

## C3. Task-first chooser — `docs/START-HERE.md`

- **What:** "You need a ___" → role → skill → minimum inputs → **needs first** → import
  target → ready-paste prompt link. Rows are reshuffled from the README skills table
  (Role/Skill/Produces/Import target) plus each `SKILL.md`'s "Inputs required" section —
  quoting, not inventing. Sample rows: "You need a PRD" → PMT/draft-prd; "a sprint plan
  that survives PTO and on-call" → SDM/sprint-planning-and-capacity; "a rollback plan"
  → SDE/pr-plan-and-rollback-notes.
- **Needs-first column (new):** which prior artifacts a skill requires, derived from
  the role files' `Consumes` "Blocking?" flags — e.g., `slice-mvp-and-stories` needs an
  accepted PRD; `sprint-planning-and-capacity` needs a candidate backlog;
  `technical-design-and-breakdown` needs requirements; `standup-execution` needs
  nothing.
- **Prompt-book links (new):** each row links its `usage/prompts-<role>.md` entry —
  grep shows no `SKILL.md` links its prompt-book entry today (only
  `skills/_TEMPLATE.md` mentions them), so START-HERE becomes the cross-link point
  and the `SKILL.md` files stay untouched.
- **Scenario recipes (new):** named end-to-end chains for the common jobs — "New
  feature" (draft-prd → slice-mvp-and-stories → sprint-planning-and-capacity →
  technical-design-and-breakdown → generate-test-ideas-and-cases), "Release readiness"
  (program-roadmap-and-deps → risk-raid-and-mitigations → release-readiness-check →
  deploy-plan-and-release), "Sprint recovery" (operational-health-review →
  scope-cut-and-tradeoffs → sprint-retro) — each naming its minimum inputs and the
  relay rows (F2) that connect the steps. Derived from the skills table and role
  contracts; no new claims. Acceptance for the recipes: they name real skills in
  their real load order with minimum inputs, and every hop traces to an F2 row.
- **Why:** the README catalog is role-first; users arrive task-first (gap P2/P3). The
  USER-GUIDE's "Choosing a role" stays; this is its task-first complement, linked from
  README and PKG-README.
- **Acceptance:** a user arriving with a task reaches the right skill, its minimum input
  list, its prerequisites, and its ready-paste prompt on one page; every row traces to
  the README table, a `SKILL.md` "Inputs required" section, or a role-file Consumes
  row.

## C4. Filled glossary example — `shared/glossary-and-org.EXAMPLE.md`

- **What:** the glossary's exact structure (Roles · Working terms · Org placeholders —
  all 11 slots, Jira project key through Estimate scale · How to use this file) with
  every slot filled in for the fictional org (Meridian Outfitters), so a first-timer
  sees a *finished* glossary, not just the template.
- **Guards:** the header states this is an example, never loaded into a session, never
  a second canonical glossary — your filled copy lives **outside the kit** as your own
  file (F3), pasted in place of the template at load step 2. No skill, role, or CLI
  reference ever loads it; `LOAD_ORDER` is untouched. All values are clearly fictional
  (fake Jira key, fake space, fake services), consistent with the fixtures'
  synthetic-everything rule.
- **Why:** the USER-GUIDE says "fill your org slots" but nobody has shown a filled one
  (gap P1: "many first-time users will not know which slots are required… or whether
  the glossary is reusable").
- **Acceptance:** all 11 slots shown filled; structure identical to the real glossary;
  clearly labeled fictional and example-only; the doc points readers to their own
  outside-the-kit copy (F3), never to editing inside an installed tree; zero references
  from session material.

## C5. Two ways to run — the agent-native path, documented

- **What:** a README + USER-GUIDE box presenting both run modes:
  1. **Any chat (today's only documented path):** paste the four files in order (or the
     bundle, C6), paste inputs, get the artifact.
  2. **A repo-reading agent (exists today, documented nowhere):** open the kit repo in
     the agent and just ask — *"run sdm sprint-planning with this input."* The repo's
     own agent files carry the load order: `.github/copilot-instructions.md` is
     committed and points agents at `AGENTS.md`, which defines the role+skill load and
     the working rules.
- **Why:** this is a real, already-working function that the "paste into any chat"
  framing completely hides — the reframing (agent-native repo, not a manual-paste kit)
  costs zero code and answers the recurring "how is this native to GitHub" question.
  Evidence: `.github/copilot-instructions.md` (11 lines, committed) and `AGENTS.md`
  step 3.
- **Acceptance:** both paths documented with their trade-offs; the agent path claims
  only what the committed files guarantee (Copilot reads `.github/copilot-instructions.md`;
  agents that read `AGENTS.md` get the same); no unverifiable claims about any specific
  vendor's tool behavior.

## C6. Session bundles — one paste instead of four

- **The measured problem:** a session load today is `shared/system-conventions.md` (47
  lines) + `shared/glossary-and-org.md` (52) + a role file (178–184) + a skill
  (64–90) ≈ **340–370 lines, roughly 3,000 words, pasted in strict order, manually,
  every session, for every skill.** A missed file or wrong order degrades the run
  silently. This is the kit's single largest recurring usability cost.
- **What:** `usage/bundles/<role>-<skill>.md` — 20 generated files, each the skill's
  full load pre-concatenated in load order.
- **Format decision (was ambiguous):** each bundle carries the **template** glossary
  inline, at its load-order position, under a banner: *"replace this section with your
  own `my-org.md` for real runs."* So the "slot" *is* the inline template section, not
  an empty gap. A trial run is one paste (the bundle alone); a real run is two (bundle
  + your glossary pasted after it).
- **Mechanism (defined):** `make bundles` runs a small POSIX `sh` concatenator
  committed as `scripts/build-bundles.sh` — the repo's first build script, alongside
  the Makefile's existing `make sync`. Packaging tooling, not kit runtime: it never
  runs in a session and the CLI stays inert. Shell only — no new language or
  dependency. `make check-bundles` regenerates into a temp dir and `diff`s against
  `usage/bundles/`.
- **Generation discipline (no second canonical copy):** bundles are generated, never
  hand-edited; each carries a header: "Generated from the four canonical files by
  `make bundles` — do not edit; regenerate on upgrade." A stale bundle fails the
  release gate (`make check-bundles`).
- **Distribution (defined):** `usage/` already rides into the pip package — `make sync`
  copies `shared/`, `roles/`, `skills/`, `tests/`, `usage/`, and `docs/` into the
  gitignored `sdlc_squad/kit/` (verified in the v0.1.0 wheel, run log §3), and
  `package-data` ships `kit/**/*.md`. Bundles are `.md` under `usage/`, so they need no
  manifest change — confirm the `usage/bundles/` paths in the wheel during the release
  gate (I.5).
- **Size note:** 20 bundles each inline the 52-line template glossary — accepted,
  because bundles are *generated* from the canonical files (the no-second-copy rule
  forbids a hand-maintained copy, not a generated artifact); the freshness gate is what
  keeps them honest.
- **Scope note (updated 2026-11-23):** the Makefile target is packaging tooling, not
  kit runtime. G1 is now **decided** — `sdlc-squad prompt` ships in 0.1.1 as a live
  assembler; the committed bundles (this item) stay for pip users who want files on
  disk. They overlap on purpose: bundles = static, CLI = on-demand.
- **Why:** kills the paste burden without adding behavior; the four canonical files
  remain the single source of truth.
- **Acceptance:** 20 bundles committed; one paste completes a session load (plus the
  user's glossary for real runs); the freshness gate runs in the release checklist;
  every bundle header carries the generated warning.

## C7. Input acquisition — `docs/EXPORTS.md` (+ the redaction recipe)

- **What:** how to get pasteable text OUT of the systems the kit writes toward,
  user-operated, offline-compliant (the inbound mirror of the import-target story):
  - **Jira** — issue-navigator exports for backlogs, sprint boards, done-ticket
    history (feeds sprint-planning, retro, ops-health, status-review).
  - **GitHub** — issue lists, PR diffs, flaky-run logs (feeds ops-health,
    design-and-code-reviews).
  - **Confluence** — page exports of prior PRDs/status pages (feeds draft-prd revision,
    program-status-review).
  - **Working data that is not in those three** — roster/PTO, capacity, ceremony hours,
    and estimate scale usually live in a spreadsheet or an HRIS. The recipe here is a
    paste-the-CSV/table recipe (redaction applied), not a system export; the org's
    actual source stays `[CONFIRM]`.
  Each recipe states what the export looks like and which skills consume it — verified
  against real exports on first use (the same `[CONFIRM]`-style honesty the kit applies
  to itself; do not assert export menus no one has checked).
- **§Redaction recipe:** find-and-replace conventions so "redact before pasting" is a
  2-minute mechanical job, not a vague warning: names → `PERSON-A`/`PERSON-B`, emails →
  `[EMAIL]`, keys/tokens → `[REDACTED]`, customer identifiers → `CUST-n`, free-text
  customer quotes → paraphrase + mark. Cross-linked from USER-GUIDE "While you work"
  and D2.
- **Why:** skills demand inputs (`[PASTE: roster / PTO calendar / candidate backlog
  with estimates]`) but no doc explains how to obtain them; the kit's privacy
  instruction is currently a warning with no method.
- **Acceptance:** every skill's named inputs map to an acquisition recipe — a system
  export (Jira/GitHub/Confluence) or the working-data recipe for roster/PTO/capacity/
  scale; the redaction recipe is mechanical and complete for the data types skills ask
  for; everything is user-operated; unverified export specifics are marked, not
  asserted.

## C8. Supported-and-adaptable matrix — `docs/TOOLS.md`

- **What:** one page stating plainly what works out of the box, what adapts by editing
  Markdown, and what requires real changes:
  - **Out of the box:** paste-ready Markdown artifacts for GitHub (issue/PR bodies —
    GFM-clean per `CONVENTIONS.md`), Jira (ticket descriptions; the story table is
    CSV-ready per the `jira-epic-and-stories` schema), Confluence (PRD/RFC pages).
  - **Adaptable by editing Markdown:** a different tracker/docs tool (edit the
    source-of-truth table and import-target language in `shared/system-conventions.md`,
    per `docs/EXTENDING.md` Path 1 — e.g., Azure DevOps + Confluence); org vocabulary
    (`my-org.md`, F3).
  - **Requires real changes:** import formats beyond paste (a validated Jira CSV
    header contract — G6), new artifact shapes (new schemas, EXTENDING Path 4).
  - **Never (a hard boundary, not a gap):** any API integration, auto-import, or
    telemetry — the charter's "not a client for anything."
- **Why:** gap review P2 ("the supported-tool story may be narrower than customers
  expect… publish a clear supported and adaptable matrix") — buyers currently have to
  reverse-engineer this from EXTENDING.
- **Acceptance:** every row traces to `system-conventions.md`, `docs/EXTENDING.md`, or
  a charter refusal; nothing claims validated import compatibility (D1's wording
  applies); linked from README and START-HERE.
