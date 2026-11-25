# 06 — Open decisions: the owner's calls

> **Status (2026-11-25):** all open. Master table: [`README`](README.md).

Theme: nothing in this file is scheduled until the owner decides. Taking a decision
means amending the affected plan file first, then working the item per the kit's rules
(one change per ticket, evidence in the same change, status flips only when exercised).

## D1. Is 0.1.2 a docs-only patch, or does it absorb minor-version work?

- **What:** the review's CLI items — W1 (`--copy` / `--out`), W2 (`--context`), W3
  (`doctor`) — are **new CLI behaviour**, which `CONVENTIONS.md` puts at a minor. The
  0.1.1 plan took its G1 CLI assembler as a **deliberate exception** to a docs-only
  fence.
- **Options:**
  - (a) **Keep 0.1.2 docs-only** — schedule W1–W3 for 0.2.0. *(Recommended: preserves a
    provably-inert patch and keeps the fence honest.)*
  - (b) Pull **W1 only** (`--copy` / `--out`) into 0.1.2 with a real test, amending the
    fence here and in [07](07-scope-and-release.md).
  - (c) Pull all three (W1–W3).
- **Decision owner: user.**

## D2. Does the kit adopt CI (R1) now?

- **What:** R1 adds a GitHub Actions workflow. The kit's promise is "no network, no
  telemetry"; a workflow runs on GitHub's own runners.
- **Options:**
  - (a) **Add a pinned, first-party-only workflow** running the make gates on PRs.
    *(Recommended if the docs keep growing — it is the automated form of the 0.1.1
    release gate.)*
  - (b) Defer CI to 0.2.0; keep the release gate manual.
  - (c) Never — keep every check manual.
- **Decision owner: user.**

## D3. Skill maturity / verification badges (R4) — which shape?

- **Options:**
  - (a) **Docs-only verification ledger now** (an I6-style page listing tiers), metadata
    later. *(Recommended: docs-only, and it sets the vocabulary before it becomes
    frontmatter.)*
  - (b) Frontmatter metadata now (`fixture-verified`, `paste-tested-*`, `field-proven`)
    — a minor-class `SKILL.md` change.
  - (c) Defer entirely to 0.2.0.
- **Decision owner: user.**

## D4. Where does the end-to-end validation run (X2) land?

- **Options:**
  - (a) **Record the run in 0.1.2; forward the schema fixes it surfaces to 0.2.0.**
    *(Recommended: the run is evidence, not behaviour; the fixes are schema-shape work.)*
  - (b) Leave the whole v0.1.x milestone to 0.2.0.
  - (c) Pull the schema fixes into 0.1.2 (makes 0.1.2 a minor).
- **Decision owner: user.**

## D5. Context pullers (I2) — confirm the refusal?

- **Options:**
  - (a) **Confirm refused; add only a one-line boundary statement to
    `docs/EXPORTS.md`.** *(Recommended: the manual export path already ships; a puller
    script would be a network client.)*
  - (b) Document a **user-side** pattern in more depth (still no script shipped).
  - (c) Reconsider — would require a charter change (`WHAT-THIS-IS.md`); not recommended.
- **Decision owner: user.**

## D6. CI supply chain (if D2 = yes) — which actions?

- **Options:**
  - (a) **Pinned first-party actions only** (`actions/checkout@<sha>`,
    `actions/setup-python@<sha>`), no secrets. *(Recommended.)*
  - (b) Shell-only workflow that runs `make` directly with the runner's tooling.
  - (c) Third-party actions (discouraged — supply-chain surface the kit does not need).
- **Decision owner: user.**

## D7. Destination overlay file type & location (I1)

- **Options:**
  - (a) **Markdown overlays outside the kit** (`my-jira.md`, `my-confluence.md`,
    `my-github.md`), the shipped F3 pattern. *(Recommended: the kit is Markdown-only.)*
  - (b) A single `my-destinations.md` covering all three.
  - (c) A YAML config (`org-destinations.yaml`) — adds a non-Markdown file class;
    discouraged.
- **Decision owner: user.**

## Related

- [`07-scope-and-release.md`](07-scope-and-release.md) — the fence each decision amends
- [`../0.1.1-plans/06-open-decisions.md`](../0.1.1-plans/06-open-decisions.md) — the 0.1.1 decision precedent (G1)
