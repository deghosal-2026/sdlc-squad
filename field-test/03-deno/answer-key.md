# Answer key — what the project actually shipped

> **Source:** `denoland/deno` issue #8327 (resolution) + linked PRs. Retrieved **2026-11-25**.
> <https://github.com/denoland/deno/issues/8327> Held back from `input.md`; used to score the
> kit's artifacts in `findings.md`.

## The outcome

- **Closed as completed, 2026-05-05.** Maintainer (bartlomieju): *"Done in **#33763** and
  **#33849**. We're not gonna do a bespoke API, the one from Node should work just fine."*
- **`require(ESM)` is supported as of Deno v2.0** (maintainer, in-thread).

So Deno **did not invent a Deno-specific loader API** — it **adopted Node's**, closing the gap
for Node-compatible tooling.

## The shape of the solution

- **Align to the Node API**, not a bespoke `Deno.loader`:
  - the Node **module loader hooks** surface, and
  - **`require(ESM)`** (loading ES modules via `require`).
- **Cache handling:** ES modules are still not re-evaluated (the spec forbids it); the
  supported path is Node's, which the ecosystem (Vite, SvelteKit, etc.) already targets.
- **Implementation PRs:** [#33763], [#33849] (2026).

## Why not a bespoke API (the decision that matters)

The thread ran five years with strong demand and a working prototype (a `Deno.loader` fork),
but the maintainers chose **compatibility over novelty** — a bespoke API would fragment the
ecosystem and diverge from Node. That is the key product decision the kit's artifacts must land
on.

[#33763]: https://github.com/denoland/deno/pull/33763
[#33849]: https://github.com/denoland/deno/pull/33849
