# 09 — Leverage mattpocock/skills (MIT) in sdlc-squad

The worked case for third-party skills: license verified, catalog mapped, three
leverage tracks, copyright mechanics included. Decisions live in G5
([06-open-decisions.md](06-open-decisions.md)); this file is the analysis.

## Why Matt Pocock's skills

- The most-installed engineering/PM skill set on skills.sh (all-time leaderboard,
  retrieved 2026-11-23): `triage` ~1.1M · `domain-modeling` ~1.0M ·
  `codebase-design` ~988K · `code-review` ~927K · `to-spec` ~841K ·
  `to-questionnaire` ~607K · `retro` ~389.7K · `to-prd` ~351.6K ·
  `to-issues` ~339.1K — with rollups showing millions more across the set.
- Repo scale: ~331k stars, 27.8k forks, 559 commits; "Skills for Real Engineers… not
  vibe coding"; ~60k-dev newsletter behind it.
- Philosophy adjacent to the kit's: anti-hallucination-adjacent ("no-one knows
  exactly what they want" → grilling), evidence-driven, hostile to frameworks that
  "take away your control."

## The license verdict (the "free + retain his copyrights" question)

**MIT — verified from the LICENSE file itself, retrieved 2026-11-23:**

> MIT License · Copyright (c) 2026 Matt Pocock
> Permission is hereby granted, free of charge, to any person obtaining a copy of this
> software… to deal in the Software without restriction, including without limitation
> the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell…
> The above copyright notice and this permission notice shall be included in all copies
> or substantial portions of the Software.

What this means for the kit:

- **Free:** no fee, no attribution-beyond-notice, no copyleft, no relicensing conflict
  with the kit's MIT.
- **"Retain his copyrights" = the MIT condition:** keep his copyright notice + the
  permission notice in all copies or substantial portions. That is the *entire*
  obligation, and it fits the kit's own provenance brand perfectly.
- The kit will over-attribute regardless: a Provenance block per adapted file, even
  where the adaptation is substantial, because provenance is the kit's product.

## His catalog → the kit (current README as truth; leaderboard names are historical)

His taxonomy: **user-invoked** skills (orchestrators, typed like `/grill-me`) vs
**model-invoked** (reusable discipline the agent reaches for automatically) — an axis
the kit doesn't have (input for G2/G4). Nested paths like ours:
`skills/engineering/…`, `skills/productivity/…`.

### Where the kit already exists (overlap — the kit adds discipline; his add runtime reach)

| His skill | Kit equivalent | What the kit adds on top | What his adds |
|---|---|---|---|
| `to-spec` (conversation → spec, publishes to tracker) | `pmt/draft-prd` + spec half of `sde/technical-design-and-breakdown` | `[CONFIRM]` discipline, schema binding, fixtures + recorded run, import-target block instead of tracker writes | Live tracker integration via his setup config |
| `to-tickets` (plan → tracer-bullet tickets with blocking edges) | `pmt/slice-mvp-and-stories` + `T-n` breakdown in technical-design | Vertical-slice honesty rule, Given/When/Then ACs, dependency rows with owners or `[CONFIRM]` | Native blocking links on a real tracker |
| `to-questionnaire` | `pmt/survey-design` / `customer-discovery-and-synthesis` | Bias checks, counts trace to paste, no extrapolation | Async "send to the one person who knows" framing |
| `code-review` (Standards + Spec axes, parallel subagents) | `sde/design-and-code-reviews` | Author gate before reviewer pass, `nit:` etiquette, split-too-large rule | Subagent parallelism (agent runtime) |
| `pr` (smallest visual, before/after evidence, merge-danger call) | `sde/pr-plan-and-rollback-notes` | Migration order, rollback stating what it does NOT undo | One-way/two-way door + blast-radius framing (a good 0.2.x input) |
| `domain-modeling` + `GLOSSARY.md` + ADRs | `shared/glossary-and-org.md` + working-terms table | Org slots the user owns, `[CONFIRM]`-over-invention | Project-domain vocabulary building |
| `handoff` (compact session for the next agent) | F2 `usage/RELAY.md` (planned) | Role-to-role human relay with artifact contracts | Agent-to-agent compaction |
| `grilling` / `grill-me` / `grill-with-docs` | The ≤3 clarifying questions in every playbook | Never-block-then-`[CONFIRM]` fallback (the kit drafts anyway; his skills grill until resolved) | The relentless-interview primitive behind five of his skills |

### Genuine gaps in the kit (adoption candidates — Track 2)

1. **`triage`** — move issues through a state machine of triage roles. The kit has
   standup blocker logs and ops-health but no incoming-ask intake. Binds the existing
   **"Ask intake & prioritization"** RACI row (PMT A/R) — no new row, no mirror-rule
   churn. Strongest candidate.
2. **`grilling`** — not a new skill so much as a **mode**: an optional grill-first
   preface (interview until every branch is resolved, *then* run the drafting skill) for
   `draft-prd`, `technical-design-and-breakdown`, `program-roadmap-and-deps`. Must
   stay optional — the kit's never-block principle ("ask up to 3, then build anyway,
   marking `[CONFIRM]`") is a feature for users who don't want interrogating.
3. **`to-questionnaire`** — async decision extraction from the one person who knows;
   near `survey-design` but a distinct job (a decision, not an instrument). Candidate
   after triage.

### Conflicts — never shipped inside the kit (fine as user companions)

- **Code generation:** `implement`, `implement-spec`, `prototype`, `tdd`, `wizard`,
  `diagnosing-bugs` — charter: "Not a code generator." Also all assume a coding-agent
  runtime (repo access, subagents, background agents), not any-chat.
- **Network:** `research` (investigates against primary sources, runs as a background
  agent) — charter: no network.
- **Repo mutation:** `setup-matt-pocock-skills` (per-repo config wizard), and the
  tracker-publishing halves of `to-spec`/`to-tickets` — a kit-native adaptation ends
  with an import-target block instead; the user pastes.
- **Out of kit scope:** `ask-matt`, `teach`, `wait-what`, `grill-me`-as-brand (chat
  utilities / personal brand), `improve-codebase-architecture`, `wayfinder`,
  `codebase-design`, `domain-modeling` (coding-agent-native; companions only),
  `retro` — **name collision warning:** his `retro` improves the *coding agent's
  environment* after a session; the kit's `sprint-retro` is a people/process sprint
  retrospective. Different artifacts; never merge or alias them.

## The three leverage tracks

### Track 1 — Interop (0.1.1-able, docs-only, zero copyright exposure) — recommended start

Deliverable: `docs/COMPANION-SKILLS.md`. Content:

1. **Install guidance, in his terms:** his README says pick *one* distribution per
   agent (self-updating plugin vs skills.sh editable files — "installing both gives
   you every skill twice"); then run his `/setup-matt-pocock-skills` once per repo
   (tracker, triage labels, doc locations).
2. **The wrap pattern (the actual leverage):** in an agent session, load
   `shared/system-conventions.md` + `shared/glossary-and-org.md` (or `my-org.md`)
   *before* invoking his skill. His outputs then inherit the kit's contracts:
   `[CONFIRM]`-over-invention, `REQ-n`/`AC-n`/`US-n` ID prefixes, ISO dates,
   Confluence/Jira paste-clean tables, and an import-target block — ask the agent to
   end with one.
3. **The pairing table** (the overlap table above, user-facing): which kit role's
   conventions to wrap which of his skills with, and what each side adds.
4. **Charter note:** what his skills do at runtime (tracker writes, background
   research, code) is the user's agent, not the kit; the kit ships nothing of his and
   calls nothing.
5. **Runtime caveat, stated honestly:** his engineering skills assume a coding-agent
   runtime; in a plain web chat they work as disciplined prompts minus tracker
   integration.

Acceptance: a user can run `to-spec` wrapped in kit conventions and get an artifact
that carries `[CONFIRM]`s, kit ID prefixes, and an import-target block; the doc claims
nothing the kit does not already do.

### Track 2 — Vendor-with-attribution (0.2.x, one skill per ticket, license-cleared)

For each adopted skill (shortlist: `triage`, then grill-mode, then
`to-questionnaire`):

1. **Provenance block** in the adapted `SKILL.md` (kit style — it already requires
   sources behind claims): source repo, source path (`skills/engineering/triage/SKILL.md`),
   the commit/URL adapted from, and the notice line: "Adapted from
   mattpocock/skills, MIT © 2026 Matt Pocock."
2. **`THIRD_PARTY_NOTICES.md`** at repo root: the full MIT text verbatim + his repo
   URL + the list of adapted files. (Filename pattern already used across the
   ecosystem.)
3. **Full kit pipeline, no shortcuts:** stencil reformat; persona binding; RACI row
   (new row → mirror rule across all role files in the same commit; existing row →
   bind, like triage→"Ask intake & prioritization"); schema binding or a new schema;
   fixture + recorded run — `status` flips only when exercised; prompt-book entry;
   README row; CHANGELOG. One skill per ticket, per the kit's rules.
4. **Adaptation rules (kit-native re-expression, not porting):** strip runtime
   integrations (tracker writes → import-target block); add `[CONFIRM]` discipline
   and evidence rules; rewrite steps in the kit's voice. MIT covers this; the
   attribution stays regardless of how substantial the rewrite becomes.
5. **No auto-sync:** upstream updates are re-adapted by hand on review (an auto-sync
   would be a network behavior the charter forbids; note this in the notice file).

### Track 3 — Pattern inspiration (no copying; runs opportunistically)

- **Grill-first line** in USER-GUIDE/TROUBLESHOOTING (one paragraph): "Want fewer
  `[CONFIRM]`s? Run a grilling session first — ask the chat to interview you until
  every branch of the design is resolved, *then* load the skill files and draft."
- **One-way door / blast radius** framing as a 0.2.x input to
  `pr-plan-and-rollback-notes`.
- **User-invoked vs model-invoked** taxonomy as an input to G2 (description polish)
  and G4 (frontmatter/standard compatibility).
- **His setup-config pattern** already validates F3 (user-space config) — cited there.

## Copyright compliance checklist (the whole obligation, made concrete)

- [ ] MIT notice text retained verbatim in `THIRD_PARTY_NOTICES.md`
- [ ] Per-file Provenance block naming source repo + path + notice line
- [ ] No stripping of his name anywhere adapted content appears
- [ ] Adaptations marked as adaptations (kit voice ≠ silent reuse)
- [ ] MIT→MIT relicensing compatibility confirmed (it is; both permissive)
- [ ] Upstream changes re-adapted manually, never auto-fetched

## Recommendation

Run **Track 1 now** (0.1.1 docs candidate — pending the G5 go): the kit becomes the
governance layer over the most-installed engineering skills on the registry, at zero
legal exposure and zero copying. Hold **Track 2** for 0.2.x after v0.1.x validation,
starting with `triage` (existing RACI row, real gap, clean adaptation). **Track 3**
items ride along with their host items (D4, E-rows, F3) whenever those ship.
