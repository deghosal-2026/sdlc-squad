# Epic: Node-compatible module loader API

> **Field-test artifact** — the kit's `pmt/slice-mvp-and-stories` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

| Field | Value |
|---|---|
| Epic key | [CONFIRM: assigned by Jira on import] |
| Type | Epic |
| Priority | [CONFIRM: per the org's scale] |
| Business value | Unblock HMR, module mocking, and Node-project ports by matching Node's loader API |
| Success metric | [CONFIRM: no metric published] |

## Why

ES modules can't be hot-reloaded, `require.cache` doesn't affect `import`, and Deno has no
supported loader API — blocking frameworks, tests, and Node ports. The decision that shapes the
slice: **align to Node's API**, not a bespoke `Deno.loader`. The cut below is the compatibility
path (Node API + `require(ESM)`), not a novel API.

## Stories

| ID | Summary | Type | Priority | Size | Dependencies |
|---|---|---|---|---|---|
| US-1 | Implement the Node module-loader hook surface | Story | [CONFIRM] | [CONFIRM] | DEP-1 |
| US-2 | Support `require(ESM)` | Story | [CONFIRM] | [CONFIRM] | — |
| US-3 | Opt-in gating (flag / permission) | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-4 | Invalidation / replace without re-evaluation | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-5 | No-overhead fast path when no loader is registered | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-6 | Docs + migration notes for Node tooling | Story | [CONFIRM] | [CONFIRM] | US-1 |

### US-1 — Node loader hook surface

**Description:** As a tool author, I can register loader hooks the same way as in Node.
**Acceptance criteria:**
- **AC-1** Given a Node-compatible loader registration, when Deno runs, then the hooks are
  invoked on module resolution/load.
- **AC-2** Given a project using Node's API, when run under Deno, then no bespoke API is needed.
**Dependencies:** DEP-1

### US-2 — `require(ESM)`

**Description:** As a developer porting from Node, `require()` can load an ES module.
**Acceptance criteria:**
- **AC-1** Given `require('./mod.mjs')` where `mod.mjs` is ESM, then it loads.
**Dependencies:** —

### US-3 — Opt-in gating

**Description:** As an operator, the loader capability is not always-on.
**Acceptance criteria:**
- **AC-1** Given no flag/permission, then the capability is off and the default path is
  unchanged.
**Dependencies:** US-1

### US-4 — Invalidate / replace

**Description:** As a tool author, I can make a subsequent import use an updated module.
**Acceptance criteria:**
- **AC-1** Given an invalidated specifier, when imported again, then the new module is used and
  the old one is **not re-evaluated**.
**Dependencies:** US-1

### US-5 — No-overhead fast path

**Description:** As a developer not using loaders, nothing changes.
**Acceptance criteria:**
- **AC-1** Given no registered loader, then module-loading performance is not measurably worse.
**Dependencies:** US-1

### US-6 — Docs

**Description:** As a Node user, I can find how to use the loader API in Deno.
**Acceptance criteria:**
- **AC-1** Given the Deno docs, then the Node-compatible loader usage is documented.
**Dependencies:** US-1

## Dependencies

| ID | On what | From | Blocks | Status |
|---|---|---|---|---|
| DEP-1 | Node loader API compatibility surface | Node.js / deno runtime | US-1 | [CONFIRM] |
| DEP-2 | V8 module-map support | deno_core / V8 | US-4 | [CONFIRM] |

## Import target
Jira — epic + stories via bulk import / CSV; paste each story's block into its ticket
description.
