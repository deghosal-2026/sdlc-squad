# Program plan — Node-compatible module loader API

> **Field-test artifact** — the kit's `tpm/program-roadmap-and-deps` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

## Milestones

| Milestone | Target | Definition of done | Source |
|---|---|---|---|
| **`require(ESM)`** | Deno v2.0 | `require()` can load an ES module | deno#8327 (maintainer) |
| **Node loader API** | Deno 2.x | Node's loader hooks work in Deno | PRs #33763, #33849 |
| **Issue closed** | 2026-05-05 | No bespoke API; the Node one is adopted | deno#8327 |

## Dependency table

| ID | Depends on | Owning team | Needed by | Slack | Notes |
|---|---|---|---|---|---|
| DEP-1 | Node loader API surface | deno runtime | Node loader milestone | [CONFIRM] | blocks US-1 |
| DEP-2 | V8 / deno_core module-map support | deno_core | invalidation | [CONFIRM] | blocks US-4 |
| DEP-3 | Documentation + migration notes | deno docs | close-out | [CONFIRM] | blocks US-6 |

## Critical path

**DEP-1 (Node API) → loader hooks (US-1) → invalidation (US-4) → close.** `require(ESM)` (US-2)
shipped earlier and was independent.

- **Zero-slack links:** `[CONFIRM: the issue gives no per-link slack.]`
- **Named risk:** the **decision itself** — a bespoke API was prototyped for years; the critical
  path was gated on the *choice* to adopt Node's, not on engineering.

## Program risks (feeds RAID)

| ID | Risk | Early-warning signal | Mitigation | Fallback |
|---|---|---|---|---|
| R-1 | Ecosystem expects a bespoke `Deno.loader` | Tools written against the fork's API | Document Node-only clearly | Ship only Node compat; mark bespoke as won't-do |
| R-2 | Memory growth from retained modules | Memory reports from HMR users | Replace the specifier, don't retain | Document the limit |
| R-3 | Performance regression on the default path | Benchmarks | Fast path when no loader is registered | Keep the capability opt-in |

## Import target
Confluence — the program page. Jira — dependency links on the epic.
