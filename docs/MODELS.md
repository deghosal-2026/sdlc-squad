# Models — what we know, and how to certify yours

The kit is harness-agnostic: it runs in any chat, including a fully local model. This page
says what is actually observed, and gives you a one-session check for **your** model.

## The observed record

The recorded runs (`../tests/results/run-2026-11-22-v0.1.0.md`) were executed with the
**`GLM-5.3` session model**. That is the only model statement with evidence today; the
record grows only as runs are recorded. There are no performance or quality scores here —
this is provenance, not a benchmark.

## Structural requirements (a fact about the prompt's shape)

A session load is a multi-file, table-heavy prompt (four files ≈ 340–370 lines, or one
bundle). The model must hold that context and emit **clean Markdown tables** bound to the
schema. That is a requirement of the input, not a claim about any model.

If the load plus your input exceeds the model's context, see the long-load recipe in
[`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) §4 — which files are droppable, and which are
not.

## Certify your model in one session

Run the five-minute first run ([`../usage/USER-GUIDE.md`](../usage/USER-GUIDE.md)) and
check that the output does all five:

- [ ] Keeps the schema's table columns (header + alignment row).
- [ ] Marks unknowns `[CONFIRM: ...]` instead of inventing.
- [ ] Stays in **one role** (no persona blending).
- [ ] Ends with the `import target` block.
- [ ] Asks ≤3 clarifying questions, then drafts anyway.

All five pass → the kit is working in your harness. Any fail → see
[`TROUBLESHOOTING.md`](TROUBLESHOOTING.md).

## Report what you observed

Use the **field-feedback** issue template
([`.github/ISSUE_TEMPLATE/field-feedback.md`](../.github/ISSUE_TEMPLATE/field-feedback.md)):
skill, model, harness, time to first draft, edits needed, would you reuse it. Opt-in and
user-typed — the kit collects nothing.

## Related

- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — recovery moves
- [`../tests/results/run-2026-11-22-v0.1.0.md`](../tests/results/run-2026-11-22-v0.1.0.md) —
  the recorded runs
