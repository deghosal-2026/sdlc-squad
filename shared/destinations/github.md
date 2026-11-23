# Destination contract — GitHub (issue and PR bodies)

**Format:** GitHub Flavored Markdown (GFM) — a strict superset of CommonMark. GitHub
renders GFM for issue bodies, PR descriptions, comments, and `.md` files, then performs
additional post-processing and sanitization after GFM is converted to HTML.

## What a kit artifact lands as

The kit's GitHub-bound artifacts (`sde/pr-plan-and-rollback-notes` PR descriptions,
`SDE` sub-task/issue bodies, `design-and-code-reviews` checklists) are pasted into an issue
or PR body. The schemas' Markdown is GFM-native, so it renders without conversion:

| Kit element | GFM feature (renders natively) |
|---|---|
| Header + alignment tables | Tables (extension §4.10) |
| PR checklists, review checklists | Task list items `- [ ]` / `- [x]` (extension §5.3) |
| `~~struck~~` change notes | Strikethrough (extension §6.5) |
| Fenced code blocks with language | Fenced code blocks (§4.5) |
| Bare issue/PR references, `@mentions` | Autolinks (extension §6.9); issue/PR autolinks |
| Section links | Auto-generated heading anchors |

## Do

- **Tables:** header row + alignment row (the kit's rule already matches GFM's table
  extension).
- **Code:** fenced blocks with an info string for the language.
- **Task lists:** `- [ ]` / `- [x]` for checklists (review, PR, release).
- **Headings:** one `# ` title, `##` per section — matches GFM ATX headings and gives
  GitHub's auto-generated anchors.
- **Alerts** (`> [!NOTE]`, `> [!WARNING]`, …) render — use sparingly, and only where the
  schema calls for a callout.

## Avoid

- **Raw HTML** beyond GitHub's allowed subset — GitHub sanitizes raw HTML; the kit's
  no-HTML rule sidesteps the difference entirely.
- **Emoji and collapsible sections in tables** — the kit's rule (`CONVENTIONS.md`) is
  already GFM-safe; keep it.
- **Relative links to non-existent paths** — they resolve on GitHub but break in a clone;
  prefer stable links or plain text in generated artifacts.

## Where it lands (skills)

- `sde/pr-plan-and-rollback-notes` → GitHub PR description
- `sde/technical-design-and-breakdown` → GitHub issue (sub-tasks) + Confluence RFC
- `sde/design-and-code-reviews` → GitHub PR template; Confluence review standards
- `sde/deploy-plan-and-release` → GitHub release issue; Confluence runbook

## Sources (retrieved 2026-11-23)

- GitHub Flavored Markdown Spec — `https://github.github.com/gfm/` (tables §4.10, task list
  items §5.3, strikethrough §6.5, autolinks §6.9, disallowed raw HTML §6.11; §1.1
  post-processing and sanitization)
- GitHub Docs — "Basic writing and formatting syntax"
  (`https://docs.github.com/en/get-started/writing-on-github/.../basic-writing-and-formatting-syntax`):
  headings, tables, task lists, alerts, footnotes, emoji codes, relative links, anchors
- **Observed 2026-11-23 (G3):** pasted into a real GitHub issue
  ([sdlc-squad#1](https://github.com/deghosal-2026/sdlc-squad/issues/1)) — headings,
  both tables (including empty trailing cells), bold, ISO dates, and `−`/`≤`/`→`
  rendered; `[CONFIRM: …]` appears **literally**. Not visually confirmed: column
  alignment, outline/TOC. Spot check — one artifact, one issue
  (`tests/results/run-2026-11-23-g3-real-paste.md`).
