# Answer key — what the project actually decided/shipped

> **Source:** `grafana/grafana` issue #77704 (consensus, 2023-11-17). Retrieved **2026-11-25**.
> <https://github.com/grafana/grafana/issues/77704> **AGPL-3.0 — quoted minimally.** Held back
> from `input.md`; used to score the kit's artifacts in `findings.md`.

## The decision

- **Build a "Go back to x" button** — a back-navigation affordance.
- **Create a new epic for "Show history"** — revisiting prior views.

## What the public record does *not* give

- **No design doc in the issue** — the issue names the *decision*, not the design.
- **No linked PRs** in the issue's development section (`None yet`).
- **No milestone** attached.

So the "answer key" here is a **decision**, not a design: the artifacts can be scored against
*the decision the team made*, but not against a shipped design. `[CONFIRM: the implementation
PRs and the "Show history" epic live elsewhere — search grafana/grafana for the epic.]`

## Why this is a useful field-test case

It is the **opposite** of the Kubernetes KEP: an **under-specified** public record. It tests
whether the kit (a) invents a design where none exists, or (b) marks the gap `[CONFIRM]` and
asks for the missing inputs — the honesty discipline under *thin* input, not rich input.
