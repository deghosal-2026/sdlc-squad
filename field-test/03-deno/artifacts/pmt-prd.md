# Node-compatible module loader API

> **Field-test artifact** — the kit's `pmt/draft-prd` output from [`../input.md`](../input.md).
> Compare against [`../answer-key.md`](../answer-key.md) in [`../findings.md`](../findings.md).

> Status: Draft · Owner: [CONFIRM: name] · Last updated: 2026-11-25 · Reviewers: [CONFIRM: names]

## Problem & context

- ES Modules **cannot be hot-reloaded**: once resolved and instantiated, a module can't be
  replaced (source: deno#8327).
- `require.cache` does not affect `import`; there is **no supported way to invalidate** a loaded
  module (source: deno#8327).
- This blocks **HMR**, **module mocking**, and static-site re-rendering, and **porting Node
  projects** that rely on Node's loader API (source: deno#8327, in-thread use cases).

## Target users

- **Framework / dev-server authors** needing HMR without pre-processing user code.
- **Test authors** needing to mock/replace a module.
- **Developers porting Node projects** that use Node's experimental loader API.

## Goals

- Provide a supported way to **invalidate / replace** a loaded module so a re-import picks up
  the change.
- **Align with the Node API** rather than inventing a Deno-specific one, so existing tooling
  works unchanged.

## Non-goals

- A **bespoke `Deno.loader`** API.
- **Re-evaluating** an already-evaluated module (the ES spec forbids it).
- A global, unconditional cache clear with no opt-in.

## User journeys

| Step | User action | System behavior | Notes |
|---|---|---|---|
| 1 | A tool registers a loader / calls the Node API | Deno accepts it | Node-compatible surface |
| 2 | A file changes | the tool invalidates and re-imports | via the supported path |
| 3 | `require(ESM)` is used | an ES module loads via `require` | supported as of Deno v2.0 |

## Requirements

### Functional

- **REQ-1** Support the **Node module-loader API** surface (not a bespoke Deno API).
- **REQ-2** Support **`require(ESM)`**.
- **REQ-3** A tool can invalidate / replace a module for a subsequent import.
- **REQ-4** The capability is opt-in (flag / permission), not always-on.

### Non-functional

- **REQ-5** Do not **re-evaluate** an already-evaluated module (spec compliance) — replace the
  specifier's target, don't re-run the module.
- **REQ-6** Avoid unbounded **memory growth** from retained modules.
- **REQ-7** Loading performance must not regress for the common (no-loader) path.

## Edge cases

| EC | Trigger | Expected behavior |
|---|---|---|
| EC-1 | A module is re-imported after invalidation | the new module is used; the old is not re-evaluated |
| EC-2 | No loader registered | the normal path; no measurable overhead |
| EC-3 | Loader errors | surfaced to the tool, not swallowed |
| EC-4 | Nested imports of a changed file | children resolve to the updated graph |

## Open questions

| # | Question | Owner | Needed by |
|---|---|---|---|
| Q-1 | Exact Node API surface to match | [CONFIRM: deno runtime team] | [CONFIRM] |
| Q-2 | Flag vs permission gating | [CONFIRM: deno runtime team] | [CONFIRM] |

## Rollout & metrics

- **Staged:** the Node API + `require(ESM)` land across **Deno 2.x** (source: deno#8327 —
  `require(ESM)` as of v2.0; PRs #33763/#33849).
- **Metric:** `[CONFIRM: no product metric published]`.

## Import target
Confluence — the PRD/RFC page for this initiative.
