# Input — the raw problem (what a session would paste)

> **Source:** `denoland/deno` issue **#8327 — "Proposal: Module Loader API"** (opened
> 2020-11-10; closed completed 2026-05-05). Retrieved **2026-11-25**.
> <https://github.com/denoland/deno/issues/8327> Quoted/paraphrased; the resolution is held
> back in `answer-key.md`. Redaction: public project text; no personal data.

---

## Problem

With ES Modules it is effectively **impossible to "hot module reload"** a module: the ES Module
spec is strict that once a module is resolved and its two-pass instantiation is done, the module
cannot be replaced. When **mocking/testing**, it is valuable to change a module and "reload" it
via dynamic import. Node.js solves this with an **experimental loader API**; Deno has no
equivalent, and `require.cache` does not affect `import`.

The absence blocks:

- **HMR** (hot module reloading) for frameworks and dev servers;
- **module mocking** in tests;
- **static-site generators** that re-render a page when a file it depends on changes;
- porting **Node projects** that rely on the loader API.

## What is wanted

A supported way to **invalidate / replace a loaded module** so that a re-`import` picks up the
change — for tooling, without requiring users to pre-process their code.

*This is the input. `answer-key.md` holds what Deno actually shipped.*
