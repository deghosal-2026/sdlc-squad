# 02 — Workflow: cut the documented relay and copy-paste friction

> **Status (2026-11-25):** W6, W7, W8 in scope for 0.1.2; W1–W5 are
> **forward-pointers to 0.2.0**. Master table: [`README`](README.md).

Theme: the review's Track 2 and its W2 weakness — "a multi-stage relay across chat
sessions and manual pasting … introduces real human friction." The review proposes
CLI and skill changes (0.2.0) plus two docs-only wins (0.1.2). The kit already cut the
*load* cost with `make bundles` and `sdlc-squad prompt` (0.1.1, C6/G1); this file
attacks the *relay* cost.

## W1. `--copy` / `--out` on `sdlc-squad prompt` — **forward to 0.2.0 (D1)**

- **Review claim:** add `--copy` (clipboard) or `--out path/to/prompt.md` so an
  assembled prompt leaves the terminal without manual selection; clean fallback when
  no clipboard utility exists.
- **Classification — 0.2.0.** New CLI behaviour. The 0.1.1 plan took its G1 CLI
  assembler as a deliberate **exception** to a docs-only fence; the default here is to
  keep 0.1.2 provably inert and schedule flags for the minor.
- **Decision:** [D1](06-open-decisions.md) — the owner may pull it into 0.1.2 (the G1
  precedent), otherwise 0.2.0.
- **Acceptance (when built):** `--copy` and `--out` are tested
  (`tests/cli/`), behave on a machine with no clipboard tool, and change no other
  output.

## W2. `--context file1.md --context file2.md` assembly — **forward to 0.2.0 (D1)**

- **Review claim:** assemble a ready-to-run prompt package from extra context files in
  one step.
- **Classification — 0.2.0.** Same class as W1 (CLI behaviour); overlaps the shipped
  bundle mechanism, which already concatenates the four canonical files.
- **Acceptance (when built):** named context files are appended in a defined order
  after the load, tested, and documented in `usage/USER-GUIDE.md`.

## W3. `sdlc-squad doctor` — **forward to 0.2.0 (D1)**

- **Review claim:** a `doctor` subcommand verifying local `my-org.md` overrides,
  bundle freshness, and Python/CLI environment health.
- **Classification — 0.2.0.** New CLI behaviour; the freshness half already exists as
  `make check-bundles` (packaging tooling), and the `my-org.md` convention already
  ships (F3). `doctor` would surface both to end users.
- **Acceptance (when built):** `doctor` reports override presence, bundle freshness,
  and environment, exits non-zero on a stale bundle, and is covered by a test.

## W4. Guided / structured intake — **forward to 0.2.0**

- **Review claim:** `--interview` (3–5 targeted intake questions upfront) or accepting
  structured YAML/Markdown frontmatter inputs before drafting, so users get better
  artifacts on the first try.
- **Classification — 0.2.0.** This changes a **skill's steps** (intake before draft) —
  skill work. It also overlaps the kit's existing clarifying-questions step, which
  already asks ≤3 questions; the review's ask is to move that *before* the first
  draft and to accept structured input.
- **Acceptance (when built):** an intake mode defined in the affected playbooks, with a
  fixture showing the question-first path; no artifact produced before intake.

## W5. Diff-aware update mode — **forward to 0.2.0**

- **Review claim:** `--mode update` that takes an existing PRD/RAID log/sprint plan
  plus delta notes and emits **only** proposed changes, preserved items, and new
  `[CONFIRM]`s — "most SDLC work is iterative maintenance, not greenfield drafting."
- **Classification — 0.2.0.** A new output shape (change-set) is schema/skill work.
  The kit's shipped recovery path (`docs/TROUBLESHOOTING.md`, D4 §5: paste the artifact
  + feedback, ask for a revision bound to the same schema) is the manual precursor.
- **Acceptance (when built):** an update mode whose output names proposed changes,
  preserved items, and new `[CONFIRM]`s; a fixture exercises an update, not a fresh
  draft.

## W6. End-to-end "Feature Relay" pack — **0.1.2 (docs)**

- **Review claim:** one curated sample showing a single feature flowing PMT
  (`draft-prd` → `slice-mvp-and-stories`) → TPM (`program-roadmap-and-deps`) → SDM
  (`sprint-planning-and-capacity`) → SDE (`technical-design-and-breakdown`), so the
  four personas connect in practice rather than as isolated templates.
- **Anchor (zero invention):** the material already exists — `usage/WALKTHROUGH.md`
  (C1, one full SDM run) and `usage/RELAY.md` (F2, the transition rows). W6 is the
  **multi-role** companion: the same Meridian Outfitters feature crossing four
  sessions, with the artifact carried at each hop.
- **Classification — 0.1.2 docs.** New worked-example doc; no schema/skill change.
- **Acceptance:** every hop traces to an F2 relay row and a committed fixture or prompt
  book; the feature is the same across all four artifacts; at least one carried
  `[CONFIRM]` is shown resolved and one carried open; linked from `usage/RELAY.md` and
  the README.

## W7. Role-to-role handoff block — **0.1.2 (docs practice)**

- **Review claim:** standardized handoff metadata at the end of every artifact —
  upstream source(s) used; blocking `[CONFIRM]`s (must resolve before the next role
  starts); next recommended role & skill.
- **Anchor:** `usage/RELAY.md` already defines the transitions and their "resolve
  first (or carry as open)" column. W7 gives that a **copy-paste block shape** the
  user appends, extending the artifact's existing `## Import target` block.
- **Classification — 0.1.2 docs practice.** Emitting the block from the skill is the
  schema-level half, which is the 0.1.1 forward-pointer **"cross-artifact carry
  fields"** ([`../0.1.1-plans/07`](../0.1.1-plans/07-scope-and-release.md), H) → 0.2.0.
- **Acceptance:** `usage/RELAY.md` defines the Handoff Block (three fields, each
  traceable to a role-file contract); it introduces no field the role files don't
  already imply; no schema or skill file is touched.

## W8. Long-load / context-budget recipe — **0.1.2 (docs)**

- **Review claim (implicit):** the W2 friction and the "artifacts are only as accurate
  as what you paste" point imply a failure the plan did not schedule — what to do when
  a four-file load plus input **exceeds** the model's context window.
- **What:** a partial-load recipe — which files are **droppable** (the template
  glossary once your `my-org.md` is in; a role file on a repeat run) and which are
  **not** (the skill playbook, the bound schema), plus the fresh-session recovery.
  Extends the shipped `docs/TROUBLESHOOTING.md` (D4 §4, "context limit hit").
- **Classification — 0.1.2 docs.** Restates the load order and the shipped recovery
  step; no schema/skill/CLI change.
- **Acceptance:** the recipe names the non-droppable files and the recovery; cross-linked
  from `docs/MODELS.md` (structural requirements) and `docs/TROUBLESHOOTING.md`.

## Related

- [`usage/RELAY.md`](../../usage/RELAY.md) — the shipped relay recipe W6/W7 extend
- [`usage/WALKTHROUGH.md`](../../usage/WALKTHROUGH.md) — the shipped single-role run
- [`docs/TROUBLESHOOTING.md`](../TROUBLESHOOTING.md) — the shipped revision path (W5 precursor)
- [`sdlc_squad/cli.py`](../../sdlc_squad/cli.py) — the shipped `prompt` subcommand W1–W3 extend
