# Design: Node-compatible module loader API

> **Field-test artifact** — the kit's `sde/technical-design-and-breakdown` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Status: Draft · Author: [CONFIRM: name] · Last updated: 2026-11-25

## Affected modules / services

| Service / repo / path | Change | Risk |
|---|---|---|
| `deno` runtime — module loading | Register and invoke Node-compatible loader hooks | High |
| `deno_core` — `ModuleMap` / `ModuleLoader` | Support replacing a specifier's target without re-evaluating | High |
| `ext/node` — loader polyfills | Expose the Node loader API surface | Medium |
| CLI — flags / permissions | Gate the capability (opt-in) | Low |
| Docs | Usage + migration notes | Low |

*The issue thread gives the design discussion, not file paths; symbol-level claims are
`[CONFIRM: read the implementation PRs #33763/#33849]`.*

## Data model & API / contract changes

- **New surface:** the **Node module-loader hook API**, matched by Deno (not a bespoke
  `Deno.loader`).
- **`require(ESM)`** — loading an ES module via `require` (already in v2.0).
- **Contract:** invalidation replaces a **specifier's target** with a new module; the old module
  is **not re-evaluated** (ES spec).

## Flow

1. A tool **registers loader hooks** (Node-compatible) and opts in (flag/permission).
2. On **resolve/load**, Deno invokes the hooks.
3. A tool **invalidates** a specifier; Deno points the specifier at a fresh module.
4. A subsequent `import`/`require` **uses the new module**; the old is retained but not
   re-evaluated.

## Failure modes & edge cases

| ID | Trigger | Behavior | Detection |
|---|---|---|---|
| FM-1 | Loader hook throws | error surfaced to the tool | loader error log |
| FM-2 | No loader registered | default fast path, no overhead | benchmark |
| FM-3 | Invalidated module re-imported | new module used; old not re-evaluated | test |
| FM-4 | Retained modules accumulate | memory growth | memory report / benchmark |
| FM-5 | Nested imports of a changed file | graph resolves to updated children | test |

## Observability

- **Logs** for loader errors (FM-1).
- **Benchmarks** for the default path (FM-2) and memory (FM-4).

## Rollback

1. The capability is **opt-in** — turning the flag/permission off restores the default path.
2. Revert the PRs; `require(ESM)` (independent) is unaffected.

## Sub-tasks (Jira-ready)

| ID | Task | Scope | DoD | Depends on |
|---|---|---|---|---|
| T-1 | Node loader hook surface | runtime + `ext/node` | Node-style registration invokes hooks | — |
| T-2 | `require(ESM)` | `ext/node` | `require('./x.mjs')` loads ESM | — |
| T-3 | Opt-in gating | CLI | off by default; unchanged default path | T-1 |
| T-4 | Invalidation without re-evaluation | `deno_core` ModuleMap | re-import uses the new module | T-1 |
| T-5 | Fast path + benchmarks | runtime | no measurable default regression | T-1 |
| T-6 | Docs + migration notes | docs | Node tooling usage documented | T-1 |

## Import target
Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the T-table as
sub-tasks.
