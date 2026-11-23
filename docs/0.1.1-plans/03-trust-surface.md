# 03 — Trust surface: make the honesty discipline feel like quality

Theme: the kit's differentiator is anti-hallucination — but discipline a user can't
see, verify, or recover from feels like friction. These items turn the honesty rules
into visible, usable product qualities.

## D1. Import-target wording: paste destination, not validated import format

- **Gap found:** the README skills table says "Jira bulk import" for
  `slice-mvp-and-stories`, and artifacts end with import-target blocks — but no
  artifact has ever been pasted into a real Jira, Confluence, or GitHub destination.
  The ROADMAP's v0.1.x milestone (open) is exactly that validation: "inspect every
  artifact against its import target (real Confluence page, real Jira issue, real
  GitHub PR)". Until it runs, "import-ready" language can overstate.
- **Patch fix (wording only, no schema edits):** one clarifying line in
  `usage/USER-GUIDE.md` (and, if it fits naturally, the README import-target note):
  import targets name **paste destinations**; fit against the real tools is what v0.1.x
  validates — until then, treat every target as an intended destination, not a
  validated import format.
- **Not doing in 0.1.1:** touching `shared/output-schemas/` or any skill file; CSV
  export templates (a real suggestion from the review, but it is a feature — import
  work belongs with the v0.1.x validation pass that can test it).
- **Acceptance:** no repo doc claims validated import compatibility; the USER-GUIDE
  states the paste-destination reality in one place a first-time reader will hit.

## D2. Data-path wording: the kit's guarantee vs. the provider's

- **Gap found:** "nothing leaves your machine" is a kit-layer guarantee (the repo
  fetches nothing, sends nothing, keeps nothing — charter contract point 4). But the
  runtime is the user's chosen chat, which may be a hosted service; the kit cannot
  promise anything about the provider's data handling, and a security-conscious reader
  can misread the guarantee's reach.
- **Patch fix (two places):**
  1. `usage/USER-GUIDE.md` — a short paragraph ("While you work" or its own note):
     the kit transmits nothing and stores nothing; your chat provider's data handling
     is yours to verify; for sensitive input use a fully local model or redact
     (recipe: `docs/EXPORTS.md` §Redaction); the sample inputs in
     `usage/prompts-<role>.md` exist so a first run needs no real data.
  2. `SECURITY.md` — a "Data path" section carrying the same statement.
     `SECURITY.md` today covers reporting, scope, and expectations (including
     "any proposal that adds a network call will be rejected on charter grounds") but
     does not state the kit-vs-provider distinction; enterprises read SECURITY.md
     before anything else.
- **Acceptance:** a reader can tell which guarantees are the kit's and which belong to
  the model/provider, without inferring a privacy promise the kit cannot make; both
  files carry the same statement, not two versions of it.

## D3. Review-the-output guide — `docs/REVIEWING-OUTPUT.md`

- **What:** how to read an artifact: `[CONFIRM]` triage in three buckets — *blocks a
  decision* / *needed before implementation* / *can be filled later*; the pre-paste
  verification list (dates ISO, owners real, every number sourced, high-impact claims
  checked); what "an artifact with zero `[CONFIRM]`s and zero user-supplied inputs is a
  defect" means for the reviewer (`CONVENTIONS.md` honesty discipline); why every
  playbook ends in a read-back step and what the user's part of it is.
- **`[CONFIRM]`-resolution practice (new):** the convention for resolving markers on
  revision: replace the marker with the fact **and its source**; keep a "resolved in
  this revision" list at the bottom; unresolved markers stay triaged by bucket. A
  formal schema-level convention is 0.2.0 territory — this item ships the user
  practice, not a schema change.
- **Claim-type marking (new):** teach the reviewer to see which claims are which —
  **source-backed fact** (carries its paste/quote), **calculation** (arithmetic shown
  from inputs; the SDM capacity tables are the exemplar), **inference** (the model's
  judgment, labeled as such), and **open question** (`Q-n`). The read-back step
  already enforces this on the model's side; this puts the reviewer's eye on the same
  axis. A schema-level marking convention is 0.2.0 territory.
- **Commercial framing (from the scan, [08](08-competitive-landscape.md)):** ChatPRD
  charges $15/month for "document scorecards" — the paid version of this discipline.
  Frame D3's checklist as a scorecard the user runs locally, for free, with no data
  leaving their machine.
- **Why:** the gap review's P1 (provenance: "include a final review checklist") and P2
  ("the `[CONFIRM]` mechanism may generate too much work") are the same user moment —
  this doc turns the honesty mechanism into a controlled workflow instead of a
  placeholder pile. Restates existing kit rules; invents none.
- **Acceptance:** a user can triage an artifact's unknowns and knows exactly what to
  verify before pasting; the resolution practice is unambiguous; every rule cited
  exists in `CONVENTIONS.md`, the charter, or a playbook.

## D4. Troubleshooting & recovery — `docs/TROUBLESHOOTING.md`

- **What:** the predictable failure modes and the recovery move for each:
  1. Model ignored the schema/structure → re-paste the skill file (or bundle) and
     require the artifact bound to its `shared/output-schemas/` schema.
  2. Model invented a fact (a date, owner, or number with no source) → quote the
     charter's never-guess rule back and require it re-emitted with
     `[CONFIRM: ...]`.
  3. Tables mangled or un-pasteable → re-request bound to the schema's exact columns;
     no HTML, no collapsible sections (`CONVENTIONS.md` Markdown contracts).
  4. Long session drifting or context limit hit → start a fresh session, paste the
     four files (or bundle) plus the current artifact, continue — one role still.
  5. **Iterate on feedback (new):** to revise an artifact after review — paste the
     load (or bundle) + the emitted artifact + the feedback; ask for the revision
     bound to the same schema. Never re-explain from scratch.
- **Why:** the difference between "it didn't work, uninstall" and "it recovered in one
  move" (gap P1 model-dependence: "provide a short recovery instruction for common
  failures"). Every remedy restates a rule the kit already ships.
- **Acceptance:** each failure mode has a one-paragraph recovery; no remedy invents new
  kit behavior; cross-linked from USER-GUIDE and MODELS.md.

## D5. Model notes — `docs/MODELS.md`

- **What:**
  1. **The observed record:** the recorded runs (`tests/results/run-2026-11-22-v0.1.0.md`)
     were executed with the runner named there. That is the only model statement with
     evidence today; the list grows only as runs are recorded.
  2. **Structural requirements:** the four-file load plus pasted input is a
     multi-file, table-heavy prompt — the model has to hold that context and emit
     clean Markdown tables. That is a fact about the prompt's shape, not a performance
     claim.
  3. **The one-session self-serve checklist** — how a user certifies *their* model
     before trusting it: keeps the schema's table columns; marks unknowns
     `[CONFIRM: ...]` instead of inventing; stays in one role; ends with the
     import-target block; asks ≤3 clarifying questions then drafts.
  4. How to report what you observed (links the F1 template).
- **Classification (corrected):** this is **not** a benchmark or velocity claim. The
  `CONVENTIONS.md` rule forbids benchmark / "industry standard" / velocity *numbers*
  without the user's own data behind them; a recorded observation of which model
  produced the recorded runs, plus a checklist the user runs themselves, asserts no
  such number — it is provenance, the same evidence class as `tests/results/`. The line
  the kit does not cross: naming untested models as working, or printing
  performance/quality scores.
- **Why:** harness-agnosticism is a strength the repo never explains; buyers ask "does
  this work with the AI I already use?" (gap P1: "publish observed model behavior and
  limitations, not unsupported claims").
- **Acceptance:** every model statement traces to a recorded run or is a structural
  fact; no performance numbers; no untested model named as working; the checklist is
  runnable by a user in one session.

## D6. Evidence page — `docs/EVIDENCE.md`: how the kit catches itself

- **What:** a user-facing retelling of the 13 defects found and fixed in the v0.1.0
  recorded pass (`tests/results/run-2026-11-22-v0.1.0.md`), each as: what the model
  attempted to invent or blur → which check or rule caught it → the correction. From
  the committed log: the invented "~400" baseline → corrected to the sourced 412/mo;
  R1 greened from one datum → yellow with an open mitigation; dark mode silently
  trimmed → an explicit Cut row; bake time set to the fastest signal → the
  slowest-signal rule; the "felt slow" ops claim → measurement-first; the
  would-you-use hypothetical → a past-behavior question.
- **Why:** it is proof the honesty discipline actually works — already recorded,
  already committed, and today invisible to any evaluating customer. This is the
  strongest trust artifact the kit can publish, at zero new-claim cost: every entry
  cites its own line in `tests/results/`.
- **Acceptance:** every entry cites the recorded run; no defect embellished or
  generalized beyond what the log records; linked from the README (E2's section), the
  walkthrough (C1), and PKG-README (E1).
