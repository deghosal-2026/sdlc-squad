# Destination contract — Confluence (pages)

Confluence is the kit's documentation destination: PRD/RFC pages, program pages, sprint
notes, launch checklists, retros. A kit artifact is **pasted into the page editor**.

## What a kit artifact lands as

- **Confluence Cloud pastes Markdown.** Pasting plain-text Markdown into the editor
  converts it into Confluence formatting — headings, bold, inline code, bulleted/numbered
  lists, tables. **After paste it is Confluence format**, no longer editable as Markdown.
- **The legacy editor** inserts Markdown via **Insert → Markup → Markdown** (preview, then
  Insert).
- **Under the hood** Confluence stores pages in the **storage format** — an XHTML-based XML
  (with custom elements for macros). That matters only for API/macro authors; the human
  path is editor paste. `[CONFIRM: storage format only if you later script page creation]`.
- **Markdown coverage is not full.** The Cloud editor officially supports a specific
  subset of Markdown; some constructs convert, some do not. **Observed 2026-11-23 (G3,
  Cloud):** headings, a bullet list, and pipe-tables all converted (no literal pipes
  remained; every table column survived). `[CONFIRM: code-block paste — unobserved]`.

### Do / Avoid (editor paste)

- Keep the kit's paste-clean rules: header + alignment tables, **no HTML**, **no emoji in
  tables**, **no collapsible sections** (`CONVENTIONS.md`) — these are exactly the
  constructs most likely to convert poorly.
- One artifact = one page. The schema's `# Title` becomes the page title; `##` sections
  become the page's sections.
- Prefer plain Markdown tables over macro-based layouts; the schema's table columns are the
  contract.
- The `[CONFIRM: ...]` markers paste as literal text — resolve them **before** pasting, or
  keep them visible as deliberate open items (see `docs/REVIEWING-OUTPUT.md`, when it
  ships).

### Callouts, status badges, code blocks (verify per instance)

These constructs are the ones most likely to differ between instances — treat them as
`[CONFIRM: verify on your instance]`:

- **Code blocks** — `[CONFIRM: code-block paste unobserved]`. When an artifact needs code,
  prefer a fenced block and check how it renders after paste.
- **Callouts / panels** — Confluence callouts are macro-based; a pasted Markdown blockquote
  becomes a **quote**, not a callout. Keep to blockquotes and do not rely on macros.
- **Status badges** — not Markdown. A plain `Status: On track` line is the paste-safe
  substitute for a badge.
- Keep the `CONVENTIONS.md` rules either way: **no HTML**, **no emoji in tables**, **no
  collapsible sections**.

## Where it lands (skills)

- `pmt/draft-prd`, `pmt/define-success-metrics`, `pmt/customer-discovery-and-synthesis`,
  `pmt/survey-design`, `pmt/prioritize-asks`
- `tpm/program-roadmap-and-deps`, `tpm/risk-raid-and-mitigations`,
  `tpm/release-readiness-check`, `tpm/program-status-review`
- `sdm/*` (sprint note, decision log, ops doc, retro, standup)
- `sde/technical-design-and-breakdown` (RFC), `sde/design-and-code-reviews` (standards),
  `sde/deploy-plan-and-release` (runbook)

## Sources (retrieved 2026-11-23)

- Confluence Cloud — "Available markdown commands"
  (`https://support.atlassian.com/confluence-cloud/docs/available-markdown-commands/`)
- Confluence Cloud — "Insert Confluence wiki markup" (Markdown insert path,
  `https://support.atlassian.com/confluence-cloud/docs/insert-confluence-wiki-markup`)
- Confluence Storage Format (XHTML-based XML) — Atlassian documentation
  (`https://confluence.atlassian.com/…/Confluence+Storage+Format`; Data Center migration
  notes)
- Paste-converts-Markdown behavior — Atlassian Community threads + independent write-ups
  (2026)
- **Observed 2026-11-23 (G3, Cloud):** pasted into a real page — headings, a bullet list,
  and tables converted (no literal pipes), `[CONFIRM: …]` literal, `−`/`≤`/`→` preserved
  (`tests/results/run-2026-11-23-g3-real-paste.md`).
- **Open `[CONFIRM]`s:** code-block paste (unobserved); the storage-format path for
  scripted page creation (out of scope for a manual paste); Data Center editor behavior.
