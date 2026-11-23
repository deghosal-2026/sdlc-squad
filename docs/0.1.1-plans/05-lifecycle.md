# 05 — Lifecycle: keep using without breakage

> **Status (2026-11-23):** F1–F4 **done**. Master table: [`README`](README.md).

Theme: what happens after the first artifact — relays between roles, surviving kit
upgrades, sharing a setup across a team, and feeding evidence back. Includes the single
most severe defect the research pass found (the upgrade clobber, F3).

## F1. Opt-in field-feedback template — `.github/ISSUE_TEMPLATE/field-feedback.md`

- **What:** a short issue template (the `ISSUE_TEMPLATE` directory already ships):
  skill used; model + harness; time to first useful draft; major edits required; did
  the artifact paste cleanly into its target; would you reuse it; anything the model
  invented. Opt-in, user-submitted — the user types the numbers, the kit collects
  nothing (no telemetry, consistent with the charter and `SECURITY.md`).
- **Why:** gap P2 ("success is not yet defined from the customer's point of view") —
  and it feeds the ROADMAP v0.1.x validation with real-user evidence instead of waiting
  for it. The template is in scope; analyzing the results stays in v0.1.x.
- **Acceptance:** template live; ROADMAP v0.1.x references it as its evidence inlet;
  nothing is collected automatically, anywhere.

## F2. The relay recipe — `usage/RELAY.md`

- **Gap found:** the relay PMT → TPM → SDM → SDE requires the user to carry context
  between single-role sessions, and the kit specifies the handoffs *internally* — every
  role file carries `Consumes` / `Produces` / `Depends on` / `Handoff signals` tables
  (`roles/sdm.md` and the other three) — but no user-facing recipe exists. "I finished
  the PRD; what exactly do I paste into the TPM's session?" is unanswered anywhere
  (gap P1: "manual relay risks losing context").
- **What:** one row per transition, **derived from the four role files' `Consumes` /
  `Produces` / `Depends on` tables** — that is the authoritative set; do not hand-pick a
  subset. Preliminary set to verify against those tables: PMT→TPM (PRD → milestones),
  PMT→SDE (requirements → design feasibility), PMT→SDM (accepted stories → candidate
  backlog), TPM→SDM (roadmap + launch checklist → sprint fit), TPM→SDE (design/deps →
  build), SDM→SDE (committed scope → task breakdown), SDE→TPM (launch inputs),
  SDE→SDM (task sizes/DoD → commitment), and the PMT↔SDM scope-cut loop. Each row
  states: which artifact to paste into the next session, which glossary facts to carry,
  which open `[CONFIRM]`s must be resolved before hand-off (or explicitly carried as
  unresolved), and what the next role will ask for first — quoting the contracts, not
  inventing.
- **Competitive validation (from the scan, [08](08-competitive-landscape.md)):** two
  independent designs converged on the same answer — the closest competitor's
  "Recommended Flows" and Matt Pocock's composable skills with a `handoff` skill that
  compacts a session for the next agent. The kit's human-relay version (F2) is the
  same pattern with the user in the loop.
- **Scope note:** this is the docs-only half of the gap review's handoff ask; the
  schema-level carry fields stay deferred ([07](07-scope-and-release.md)).
- **Acceptance:** the row set is complete against the four role files'
  `Consumes`/`Produces`/`Depends on` tables (no hand-picked subset); every transition
  row traces to a role-file contract; a user completes a two-role hand-off by following
  one row without re-reading role files; no schema or skill file touched.

## F3. Upgrade safety — `docs/UPGRADING.md`: your data vs. the kit's

- **Gap found (the most severe usability defect in the research pass):** the glossary
  is the kit's only customization point, and **both distribution paths destroy it.**
  `pip install --upgrade sdlc-squad` replaces the installed tree, including the filled
  `shared/glossary-and-org.md` inside `sdlc_squad/kit/`; a `git pull` in a clone
  conflicts with the edited file. Grep across `usage/`, `docs/`, README, PKG-README:
  zero guidance on where user data lives — the only upgrade mention anywhere is the
  pip command itself (`PKG-README.md`). `docs/EXTENDING.md` Path 1 even says "your
  fork fills `shared/glossary-and-org.md`", steering users straight into the clobber.
- **What:**
  1. The convention: your filled org glossary is **your file**, kept outside the kit
     (`my-org.md` or any name); paste it in place of the template at load step 2 —
     bundles (C6) mark the slot.
  2. `docs/UPGRADING.md`: the convention above, the upgrade path for pip and clone
     users, and the **ownership table** — yours: filled org glossary + every generated
     artifact; the kit's: everything else, extend in place, never fork
     (`docs/EXTENDING.md` standing rules).
  3. Alignment edits: `PKG-README.md`'s upgrade line gains the safety note (E1);
     `docs/EXTENDING.md` Path 1 and `usage/USER-GUIDE.md` step 2 stop pointing at
     editing files inside an installed tree; C4's example doc points at the
     outside-the-kit copy.
- **Competitive validation (from the scan):** Matt Pocock's setup skill stores config
  in the *user's repo*, not in his skill files — the same user-space rule.
- **Why:** an adoption killer hiding in plain sight — the one file every real user
  fills is the one file the upgrade path overwrites.
- **Acceptance:** upgrade instructions exist for both pip and clone paths; the
  ownership table is complete; no doc instructs a user to edit inside an installed
  tree; a user can upgrade without losing their filled glossary.

## F4. Team-usage pattern — sharing one setup

- **What:** a short pattern (a section of `docs/UPGRADING.md` or its own small doc):
  how a small team shares one filled org glossary (a private repo or shared drive,
  one owner — single source of truth), where generated artifacts live (locally in the
  git-ignored `output/`; the system of record stays Jira/Confluence/GitHub), and how
  the relay (F2) works across people, not just sessions.
- **Why:** the kit is silent on multi-person use; the gap review flagged upkeep and
  drift (P2) — most of that anxiety dissolves once "your file vs the kit's file" is
  explicit.
- **Acceptance:** a 3-person team can share the setup without forking the kit or
  duplicating the glossary; the pattern introduces no new claims.
