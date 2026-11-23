# RACI — decision rights across the squad

The canonical decision-rights matrix. Each role file carries **its own column** as a
projection, so a single-role session load is self-contained. **Mirror rule:** any change here
updates the matching role file(s) in the same commit, and vice versa — never let the two drift.

## Matrix

| Decision / artifact | PMT | TPM | SDM | SDE |
|---|:---:|:---:|:---:|:---:|
| PRD — requirements & non-goals | **A/R** | C | I | C |
| Success metrics & guardrails | **A/R** | C | I | C |
| Epic & story slicing | **A/R** | I | C | C |
| Customer discovery & synthesis | **A/R** | I | I | C |
| Survey design & results read-back | **A/R** | I | I | I |
| Ask intake & prioritization | **A/R** | C | C | C |
| Program roadmap & milestone sequence | C | **A/R** | C | I |
| Cross-team dependency commitments | I | **A/R** | C | C |
| RAID log & risk tracking | C | **A/R** | C | I |
| Launch go/no-go checklist | C | **A/R** | C | C |
| Program status review (bi-weekly/monthly, R/Y/G) | I | **A/R** | C | I |
| Sprint commitment (capacity-fit) | I | C | **A/R** | C |
| Scope-cut options & costs | C | C | **A/R** | C |
| Operational health review & remediation tickets | I | C | **A/R** | C |
| Technical design & breakdown | C | I | C | **A/R** |
| Test plan & cases | I | I | C | **A/R** |
| PR description & rollback notes | — | C | I | **A/R** |
| Design & code reviews | I | I | C | **A/R** |
| Deploy plan & release execution | I | C | C | **A/R** |

## Legend

- **R** — does the work (the skill that produces the artifact)
- **A** — owns the outcome (ratifies before it ships)
- **C** — consulted before it is finalized (see each role's "Reviews in others' artifacts")
- **I** — informed after
- **—** — no stake

## The standing rule

Every **A** in this matrix means *the persona owns producing the artifact* — the human user
ratifies every decision before anything ships (charter: the user decides everything). An A is
authorship plus a recommendation, never authority over the user.

## Adding a role

Add the column here, then fill the new `roles/<role>.md` from `roles/_TEMPLATE.md`, which
projects its own column back. One change, both files, same commit.