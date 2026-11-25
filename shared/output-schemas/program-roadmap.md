# Output schema — Program roadmap

Bound by: `tpm/program-roadmap-and-deps`.

## Canonical shape

```markdown
# Program plan — [initiative]

> Status: Draft · Owner: [CONFIRM: name] · Last updated: YYYY-MM-DD

## Milestones
| Milestone | Target | Definition of done | Source |
|---|---|---|---|

## Dependencies
| ID | Depends on | Owning team | Needed by | Slack | Notes |
|---|---|---|---|---|---|
| DEP-1 | ... | ... | ... | ... | ... |

## Critical path
[The ordered chain; name zero-slack links and the named risk.]

## Program risks
| ID | Risk | Early-warning signal | Mitigation | Fallback |
|---|---|---|---|---|

## Import target
Confluence — the program page. Jira — dependency links on the epic.
```

## Rules

- **This page owns the milestones and the `DEP-n` IDs.** The PRD **references** it; it does not
  assert release dates (RACI: *Program roadmap & milestone sequence* and *Cross-team dependency
  commitments* are **TPM A/R**). Downstream artifacts (`jira-epic-and-stories`,
  `technical-design-doc`) reference these IDs — they never mint their own.
- Every dependency names its **owning team** or `[CONFIRM]`; **slack** is shown or `[CONFIRM]` —
  never assumed.
- The **critical path** is named end to end; **zero-slack links** are flagged.
- Cross-team by default: a multi-team / cross-SIG feature lives **here**, not in one squad's
  sprint plan (see `usage/RELAY.md`, cross-team mode).
