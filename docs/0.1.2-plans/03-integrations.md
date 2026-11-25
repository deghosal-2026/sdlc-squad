# 03 — Integrations: tool contracts, instance profiles, live context

> **Status (2026-11-25):** I1, I4, I5, I6, I7 in scope for 0.1.2; I3 is a
> **forward-pointer to 0.2.0**; I2 is **refused**. Master table: [`README`](README.md).

Theme: the review's Track 3 and its W3 weakness — "real-world Jira instances have
custom workflows, field vocabularies, and ADF/wiki formatting quirks … Confluence
storage/code-block paths and Jira Data Center remain untested." This file splits
docs-only work (profiles, compatibility notes, templates, a validation ledger) from a
script (0.2.0) and a charter refusal (live context).

## I1. Instance profile overlays (`my-jira.md` / `my-confluence.md` / `my-github.md`) — **0.1.2 (docs)**

- **Review claim:** a config template (`org-destinations.yaml` or `my-jira.md`) mapping
  real Jira issue types, priority names (Blocker/Critical/Major/Minor vs. P1/P2),
  story-point/T-shirt fields, and Confluence formatting rules — "directly solves the
  silent field-remapping problem (P1/P2 → Medium, Size → Labels)."
- **Classification — 0.1.2 docs.** Follows the shipped **F3 rule**: your files live
  **outside** the kit (`docs/UPGRADING.md`). Shipped as **Markdown** overlays, not YAML
  — the kit is Markdown-only and adding a `.yaml` config class is a new file type
  ([D7](06-open-decisions.md)). The templates ship as examples (the
  `shared/glossary-and-org.EXAMPLE.md` pattern); one docs page teaches the pattern.
- **Guard:** no skill, role, or CLI loads them; `LOAD_ORDER` is untouched; **no
  credentials or tokens** — the profile is names and mappings only
  (`SECURITY.md`; `docs/TOOLS.md` §Never).
- **Acceptance:** three overlay templates + one page; each maps priority names,
  estimate unit, and formatting rules; every value is user-supplied or
  `[CONFIRM: map …]`; no secrets; no skill/CLI change.

## I2. Read-only context pullers — **refused (charter)**

- **Review claim:** "opt-in, local-only helper scripts (using `gh`, Jira/Confluence
  exports, or local git logs)" that pull sanitized PRs/issues/tags into a local
  context folder, no daemon.
- **Classification — refused.** A script that calls `gh` or an API is a **network
  client**. The charter: "Not a client for anything"; `SECURITY.md`: "any proposal
  that adds a network call will be rejected on charter grounds." The **manual,
  user-operated** path already ships — `docs/EXPORTS.md` (C7) documents copying Jira
  exports, `gh issue list` output the **user** runs, PR hunks, and Confluence page
  exports.
- **What ships instead:** a one-line boundary statement in `docs/EXPORTS.md` (the kit
  ships no puller; you run the export yourself), and no script. [D5](06-open-decisions.md)
  confirms this.
- **Acceptance:** no puller script exists; `docs/EXPORTS.md` states the boundary;
  nothing in the kit fetches.

## I3. Jira CSV & issue-creation dry-run exporter — **forward to 0.2.0**

- **Review claim:** a deterministic formatter converting `slice-mvp-and-stories` / SDE
  sub-task tables into a validated CSV/JSON preview that highlights column mappings and
  unmapped fields before import.
- **Classification — 0.2.0.** A new script, and it **binds the CSV contract to the
  schema** (`shared/destinations/jira.md` + `shared/output-schemas/jira-epic-and-stories.md`)
  — schema/skill work. Note the contract is now **observed**: G3 recorded a real Jira
  CSV import (3/3 stories; priority P1/P2 → Medium; Size landed in Labels)
  (`tests/results/run-2026-11-23-g3-real-paste.md`).
- **Acceptance (when built):** an offline, zero-dependency exporter that prints the
  column mapping and flags unmapped fields; a recorded run.

## I4. Confluence compatibility mode — **0.1.2 (docs)**

- **Review claim:** formatting rules and optional variants for tables, callouts, status
  badges, and code blocks, tailored to how Confluence renders pasted Markdown vs.
  editor blocks.
- **Anchor:** `shared/destinations/confluence.md` already exists; G3 observed headings,
  a bullet list, and pipe-tables converting, with `[CONFIRM]` literal. **Code-block
  paste is still unobserved**, and the storage-format path is out of scope for a manual
  paste.
- **Classification — 0.1.2 docs.** Expand the contract with explicit **do/avoid** rows
  for callouts, status badges, and code blocks (the kit already forbids HTML, emoji in
  tables, and collapsible sections — `CONVENTIONS.md`), keeping the editor-paste vs.
  storage-format distinction.
- **Acceptance:** the contract names what converts and what to avoid for each
  construct; unobserved paths carry `[CONFIRM]`; no schema/skill change.

## I5. GitHub PR / issue template pack — **0.1.2 (repo templates)**

- **Review claim:** ready-to-use `.github/ISSUE_TEMPLATE` and `PULL_REQUEST_TEMPLATE.md`
  aligned with SDE skills (`pr-plan-and-rollback-notes`, `deploy-plan-and-release`,
  `design-and-code-reviews`).
- **Anchor:** templates already exist — `PULL_REQUEST_TEMPLATE.md`, `bug_report.md`,
  `field-feedback.md`, `new-skill.md` — but they are **governance/feedback-shaped**, not
  SDE-artifact-shaped. I5 **audits them first**, then adds an SDE-aligned template
  (rollback steps, the deploy/release split, blast radius, review etiquette) without
  duplicating what exists.
- **Classification — 0.1.2 repo presentation** (the same class as the 0.1.1
  `field-feedback.md`).
- **Delivered as `docs/GITHUB-TEMPLATES.md`** — ready-to-copy blocks for the *user's* repo.
  The kit's own `.github/` templates are for contributing to the kit, so the SDE-aligned
  templates ship as docs, not as the kit's own templates.
- **Acceptance:** existing templates audited and kept; new/aligned template(s) carry the
  fields the SDE skills already emit; no duplication; the charter checkboxes intact.

## I6. Destination validation ledger — **0.1.2 (docs)**

- **Gap (the review implies it):** W3 says Confluence storage/code-block and Jira Data
  Center are untested, but no single **observed vs. unobserved** matrix exists.
- **What:** one table (in `shared/destinations/README.md` or `docs/`) listing each
  destination path and its state — **observed**: GitHub issue ✓, Jira Cloud editor ✓,
  Jira CSV import ✓, Confluence Cloud page ✓; **unobserved**: Jira Data Center ✗,
  Confluence storage format ✗, Confluence code-block paste ✗.
- **Classification — 0.1.2 docs.** A ledger of what G3 observed and what remains
  `[CONFIRM]`.
- **Acceptance:** every row cites `tests/results/run-2026-11-23-g3-real-paste.md` or
  carries `[CONFIRM]`; no path marked observed without a recorded paste.

## I7. `make check-links` + `make check-frontmatter` — **0.1.2 (tooling)**

- **Gap:** the 0.1.1 release gate checked internal links and the README tree **by hand**;
  the review's R1 wants it automated. Formalize as Makefile targets — the same class as
  `make sync` / `make check-bundles` (packaging tooling, not kit runtime).
- **Classification — 0.1.2 tooling** (no runtime behaviour). Feeds R1.
- **Acceptance:** `make check-links` fails on a broken relative link; `make
  check-frontmatter` validates `SKILL.md` frontmatter keys/status; both run in the
  release gate and (if D2) in CI.

## Related

- [`shared/destinations/`](../../shared/destinations/) — the shipped destination contracts
- [`docs/EXPORTS.md`](../EXPORTS.md) — the shipped user-operated input path (I2)
- [`docs/TOOLS.md`](../TOOLS.md) — the shipped supported/adaptable matrix
- [`tests/results/run-2026-11-23-g3-real-paste.md`](../../tests/results/run-2026-11-23-g3-real-paste.md) — the observed pastes (I6)
