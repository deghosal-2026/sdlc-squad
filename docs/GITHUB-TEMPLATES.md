# GitHub templates — ready to drop into your repo

Ready-to-use `.github/` templates aligned with the kit's SDE skills
([`technical-design-and-breakdown`](../skills/sde/technical-design-and-breakdown/SKILL.md),
[`pr-plan-and-rollback-notes`](../skills/sde/pr-plan-and-rollback-notes/SKILL.md),
[`deploy-plan-and-release`](../skills/sde/deploy-plan-and-release/SKILL.md),
[`design-and-code-reviews`](../skills/sde/design-and-code-reviews/SKILL.md)). Copy the
blocks below into your own repo's `.github/` — the kit's own templates are for contributing
to the kit, not for your project.

## `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What this changes

<!-- One change. Link the issue/story it closes. -->

Closes #

## Rollback

<!-- From pr-plan-and-rollback-notes: what undoes this, and what it does NOT undo. -->

- Rollback step:
- What rollback does **not** undo:
- Blast radius if this is wrong (one-way or two-way door):

## Deploy / release

<!-- From deploy-plan-and-release: deploy != release. -->

- Deploy step:
- Release gate (flag? canary? audience?):
- Flag owner + removal date (if flagged):

## Review

- [ ] Self-reviewed first (small, reviewable diff)
- [ ] Tests cover the change
- [ ] No secrets, no real customer data
- [ ] `nit:` used for non-blocking comments
```

## `.github/ISSUE_TEMPLATE/design.md`

```markdown
---
name: Design request
about: Ask for a technical design before implementation
title: "[design] "
labels: design
---

**Problem / requirement** (link the PRD or story):

**Constraints** (services touched, estimate scale, deadlines):

**Out of scope** (what this design explicitly does not cover):

**Decisions needed** (the open questions this design must answer):
```

## How to use these

1. Copy the blocks into your repo's `.github/` (keep your existing templates).
2. Adjust the sections to your team's norms — these are the kit's defaults, not a mandate.
3. The kit's skills emit artifacts that fill these shapes; the template and the skill
   should agree (see [`../shared/destinations/github.md`](../shared/destinations/github.md)).

## Related

- [`../shared/destinations/github.md`](../shared/destinations/github.md) — the GFM contract
- [`DESTINATION-PROFILES.md`](DESTINATION-PROFILES.md) — mapping the kit to your instance
- [`../skills/sde/`](../skills/sde/) — the skills these templates mirror
