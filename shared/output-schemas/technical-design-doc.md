# Output schema — Technical design doc / RFC section

Bound by: `sde/technical-design-and-breakdown`.

## Canonical shape

```markdown
# Design: [Title]

> Status: Draft · Author: [CONFIRM: name] · Last updated: YYYY-MM-DD

## Affected modules / services
| Service / repo / path | Change | Risk |
|---|---|---|

[Every claim about existing code carries its source: the file/repo it was read from, or
CONFIRM.]

## Data model & API / contract changes
[Schema before/after; endpoint or event signatures; backwards-compatibility notes.]

## Flow
[Numbered sequence, text only: actor → step → observable state change.]

## Failure modes & edge cases
| ID | Trigger | Behavior | Detection |
|---|---|---|---|

## Observability
[What is logged/metric'd/alerted, and the query or dashboard that shows it.]

## Rollback
[Named steps, in order, back to the last good state. "Revert the PR" is a step, not a plan.]

## Sub-tasks (Jira-ready)
| ID | Task | Scope | DoD | Depends on |
|---|---|---|---|---|
| T-1 | ... | [files/services] | [observable completion] | — |

## Import target
Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the T-table
as sub-tasks.
```

## Rules

- Design sections cite the repository they read: file paths and symbols, quoted where it
  matters. Unread code is `[CONFIRM]`, never described from vibes.
- Every task has a Definition of Done that is observable by someone other than its author.
- Failure modes without detection paths are incomplete rows.