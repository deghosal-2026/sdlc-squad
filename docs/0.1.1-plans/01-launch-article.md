# 01 — Launch article: fix the dev.to draft before publication

Theme: every error and imprecision the fact-check found in the launch materials. These
block publication of the ROADMAP's open "Launch article — dev.to" item. No repo files
change here — the fixes land in the article draft, then it publishes.

- **Where the corrected draft lives (decision):** recommended in-repo as
  `docs/launch-article.md` — ships with the release, gives the A/B fixes and the
  pre-publish re-fact-check one addressable file, and lets the CHANGELOG cite it.
  Alternative: keep the draft in scratch outside the repo. Owner's call; noted here
  so the fixes have a home either way.

## A — Must-fix errors (block publication)

### A1. PMT is "Product Manager, Technical", not "Technical Product Manager"

- **Error:** the article's roles list expands PMT as "Technical Product Manager" (twice:
  the intro and the "What It Actually Is (And Isn't)" section). The breakdown carries
  the same expansion.
- **Evidence:** `README.md` ("PMT — Product Manager, Technical", The squad table) and
  `WHAT-THIS-IS.md` ("PMT (Product Manager, Technical)"). `PKG-README.md` gets it right
  too — the error is in the article draft only. The kit never uses "Technical Product
  Manager" anywhere.
- **Why it matters:** "Technical Product Manager" is a different, established role, and
  it collides head-on with the kit's own TPM (Technical Program Manager). Mislabeling
  the personas in the launch piece is the exact taxonomy failure this kit exists to
  police.
- **Fix:** replace every occurrence with "Product Manager, Technical"; keep
  "TPM (Technical Program Manager)", "SDM (Software Development Manager)",
  "SDE (Software Development Engineer)" as written.
- **Acceptance:** zero occurrences of "Technical Product Manager" in the published
  piece; the PMT expansion matches `README.md`/`WHAT-THIS-IS.md` verbatim.

### A2. The load order is four files, not three

- **Error:** the article says "You load three pieces in order — shared conventions +
  one role persona + one skill playbook", and its quick-start step 2 omits the glossary.
  The breakdown's "(shared conventions + role + skill)" has the same omission.
- **Evidence:** the kit's own CLI defines the canonical order — `sdlc_squad/__init__.py`
  `LOAD_ORDER`: `shared/system-conventions.md` → `shared/glossary-and-org.md` →
  `roles/<role>.md` → `skills/<role>/<skill>/SKILL.md`. `usage/USER-GUIDE.md` ("The
  60-second version", step 2) and `PKG-README.md` ("Run a session") print the same
  four. `docs/EXTENDING.md` calls the glossary "the intended single customization
  point."
- **Why it matters:** teaching the quick start without the glossary teaches a degraded
  run — every org fact surfaces as `[CONFIRM]` — and misstates the mechanic the shipped
  CLI itself prints.
- **Fix:** "three pieces" → "four files, in order"; quick-start step 2 gains the glossary
  step with the fill-your-org-slots note (slots may be left `[CONFIRM]` for a first
  try).
- **Acceptance:** the article's stated load order matches the CLI's printed `LOAD_ORDER`
  exactly — four entries, same order, glossary included.

### A3. "No vendor-specific tool schemas" is false as written

- **Error:** the breakdown's harness-agnosticism section claims the kit has "no
  vendor-specific tool schemas."
- **Evidence:** the output schemas are deliberately vendor-targeted:
  `shared/output-schemas/jira-epic-and-stories.md` (the README skills table says
  "Jira bulk import" for `slice-mvp-and-stories`), `confluence-prd-or-rfc.md`, and
  GitHub PR/issue targets; `docs/EXTENDING.md` Path 4 discusses "importers (Jira CSV,
  Confluence paste)".
- **Why it matters:** the kit's actual position is stronger and different: vendor-
  agnostic about the **chat harness** (no MCP/agent tool schemas, no IDE-plugin
  assumptions, runs anywhere text can be pasted, including a local model) and explicit
  about the **import targets** (GitHub, Jira, Confluence Markdown shapes). Claiming the
  wrong half invites the "so it's not really for Jira?" misread.
- **Fix:** reword to the split: harness-agnostic in the runner, vendor-targeted in the
  output schemas/import blocks.
- **Acceptance:** the claim no longer asserts an absence of vendor-targeted schemas; the
  harness vs. import-target distinction is stated once, plainly.

## B — Imprecisions to fix in the same pass

### B4. "No installer"

- **Current text:** "no server, installer, or executable workflow engine."
- **Fact:** `pip install sdlc-squad` is the installer — a file distribution
  (`pyproject.toml`, `PKG-README.md`: "no server, no code path beyond locating the
  files"). What is true: no server, no runner, no daemon, no workflow engine; the CLI's
  entire job is printing the kit path and the load order (`sdlc_squad/cli.py`).
- **Fix:** "no server, no runner, no executable workflow engine — the package just puts
  the Markdown on disk and prints where it landed."
- **Acceptance:** the piece no longer denies the existence of its own pip distribution.

### B5. Single-role rule attributed to AGENTS.md

- **Current text:** "Enforces single-role sessions via AGENTS.md."
- **Fact:** the one-role-per-session rule is charter law — `WHAT-THIS-IS.md`: "One role
  per session — personas blur in a shared context" — restated in `usage/USER-GUIDE.md`
  and `docs/EXTENDING.md` (standing rule 5). `AGENTS.md` implies it (its load steps
  name a single role file), but the charter is the binding source and overrides every
  other file, including `AGENTS.md`.
- **Fix:** attribute the rule to the kit's charter, not `AGENTS.md`.
- **Acceptance:** the rule's cited source is the charter.

### B6. "Zero configuration"

- **Current text:** "Zero configuration or plugin setup."
- **Fact:** true for a first try; not the intended steady state. `usage/USER-GUIDE.md`
  step 2 says fill the org slots (Jira project key, sprint length, on-call rotation…)
  in `shared/glossary-and-org.md` — the kit runs without it at the cost of
  wall-to-wall `[CONFIRM]`s.
- **Fix:** "zero setup to try it; fill your org glossary once for real runs" — pointing
  at the outside-the-kit copy ([F3](05-lifecycle.md)), not an edit inside the
  installed tree.
- **Acceptance:** the piece sets the expectation that the glossary fill is part of real
  use, and never tells the reader to edit files inside a pip-installed tree.

### B7. RACI customization is not "just edit"

- **Current text:** "you don't have to fork a codebase or rewrite API adapters — you just
  edit the shared Markdown conventions and glossary files" (in a sentence that also
  covers custom RACI boundaries).
- **Fact:** the glossary is genuinely single-file (`docs/EXTENDING.md` Path 1 — the
  intended single customization point). `system-conventions.md` changes only when
  tooling differs. But RACI changes carry the **mirror rule**: any change to
  `shared/raci.md` updates every affected role file in the same commit
  (`docs/EXTENDING.md` standing rules 1–2; `shared/raci.md` header). "Just edit"
  invites exactly the drift the kit forbids.
- **Fix:** split the claim — glossary: edit freely; RACI: the mirror rule applies
  (matrix + role mirrors, one commit).
- **Acceptance:** the customization guidance matches `docs/EXTENDING.md`'s paths and
  rules; no "just edit" phrasing attached to RACI.
