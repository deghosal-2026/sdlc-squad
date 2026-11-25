# Program plan — "Go back to x" + "Show history"

> **Field-test artifact** — the kit's `tpm/program-roadmap-and-deps` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

## Milestones

| Milestone | Target | Definition of done | Source |
|---|---|---|---|
| **Design doc + consensus** | 2023-11-17 | Agree the proposal | grafana#77704 |
| **"Go back to x" button** | `[CONFIRM: no milestone published]` | the control ships | grafana#77704 (decision) |
| **"Show history" epic** | `[CONFIRM]` | a new epic is opened | grafana#77704 (decision) |

## Dependency table

| ID | Depends on | Owning team | Needed by | Slack | Notes |
|---|---|---|---|---|---|
| DEP-1 | Frontend routing / URL state | grafana frontend platform | button | [CONFIRM] | blocks US-2 |
| DEP-2 | "Show history" epic scope | grafana frontend platform | history epic | [CONFIRM] | blocks US-5 |
| DEP-3 | Design review / UX sign-off | grafana design | button | [CONFIRM] | — |

## Critical path

**Consensus (done) → design → button (US-1/US-2) → release.** The history epic branches off and
does not gate the button.

- **Zero-slack links:** `[CONFIRM: the issue gives no per-link slack.]`
- **Named risk:** the public record is a **decision**, not a plan — the target and team are
  `[CONFIRM]`.

## Program risks (feeds RAID)

| ID | Risk | Early-warning signal | Mitigation | Fallback |
|---|---|---|---|---|
| R-1 | "Previous context" is ambiguous | Conflicting UX feedback | Define it in the design doc | Ship a conservative interpretation |
| R-2 | Scope creep into "Show history" | The epic grows | Keep it a separate epic | Defer history |
| R-3 | No milestone → no target | Work stalls | Attach a milestone | `[CONFIRM]` |

## Import target
Confluence — the program page. Jira — dependency links on the epic.
