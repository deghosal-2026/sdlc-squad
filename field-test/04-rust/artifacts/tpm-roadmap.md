# Program plan — `let-else` (RFC 3137)

> **Field-test artifact** — the kit's `tpm/program-roadmap-and-deps` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

## Milestones

| Milestone | Target | Definition of done | Source |
|---|---|---|---|
| **RFC accepted** | 2021 | The RFC merges; the design is agreed | RFC 3137 |
| **Implementation (unstable)** | `[CONFIRM]` | Parser + type-checker behind a feature gate | Rust issue #87335 |
| **Stabilization** | `[CONFIRM: stabilized in Rust 1.65?]` | Feature-gate removed; docs shipped | `[CONFIRM]` |

## Dependency table

| ID | Depends on | Owning team | Needed by | Slack | Notes |
|---|---|---|---|---|---|
| DEP-1 | RFC / language-team sign-off | rust-lang/lang | RFC accepted | [CONFIRM] | blocks all |
| DEP-2 | `rustfmt` support | rust-lang/rustfmt | Implementation | [CONFIRM] | blocks US-7 |
| DEP-3 | Diagnostics infrastructure | rust-lang/compiler | Implementation | [CONFIRM] | blocks US-4/US-5 |

## Critical path

**DEP-1 (RFC) → parser (US-1) → desugar (US-2) → divergence + lints (US-4/US-5) → stabilization.**

- **Zero-slack links:** `[CONFIRM: the RFC gives no per-link slack.]`
- **Named risk:** the **if-let-chains interaction** (Q-1) — the RFC says neither feature
  should stabilize without considering the other, which can hold stabilization.

## Program risks (feeds RAID)

| ID | Risk | Early-warning signal | Mitigation | Fallback |
|---|---|---|---|---|
| R-1 | Conflict with if-let-chains | Lang-team flags the interaction | Explicit compatibility carve-outs (the two restrictions) | Stabilize one first with the carve-outs |
| R-2 | `rustfmt`/tooling lag | Unformatted let-else in the wild | Coordinate with rustfmt early | Ship the parser first; format later |
| R-3 | Grammar ambiguity (`else {} else {}`) | Bug reports | The "may not end with `}`" rule | Require parentheses |

## Import target
Confluence — the program page. Jira — dependency links on the epic.
