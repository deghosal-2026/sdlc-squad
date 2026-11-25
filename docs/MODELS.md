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

## The 60-second benchmark (run it on your model)

The checklist above, as one paste. Load any skill (or a bundle), paste this, and watch:

```
Ignore the skill's task for a moment. Produce a small table with these columns exactly:
| ID | Owner | Date | Points | Source |
Add one row for each of: (a) a fact I gave you, (b) a number I did NOT give you, (c) a date
I did NOT give you. For anything I did not supply, put [CONFIRM: missing from input] in the
Source cell — do not invent it. Keep the header and alignment row intact. End with a line
starting "import target:".
```

Pass = the table keeps its columns, the unsupplied number/date carry `[CONFIRM: missing from
input]` (not a guess), and the import-target line is present. Fail = an invented value, a
dropped column, or a missing block. That is the whole kit in one screen.

## Failure modes (evidence-gated)

Where specific models have been **observed** to slip. Rows appear only after a recorded run
or a field-feedback issue; until then the table is empty on purpose — a model is never named
as working (or failing) without evidence.

| Model | Failure observed | Evidence |
|---|---|---|
| `[CONFIRM: run per model]` | `[CONFIRM]` | `[CONFIRM: recorded run or field-feedback issue]` |

## Report what you observed

Use the **field-feedback** issue template
([`.github/ISSUE_TEMPLATE/field-feedback.md`](../.github/ISSUE_TEMPLATE/field-feedback.md)):
skill, model, harness, time to first draft, edits needed, would you reuse it. Opt-in and
user-typed — the kit collects nothing.

## Related

- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — recovery moves
- [`../tests/results/run-2026-11-22-v0.1.0.md`](../tests/results/run-2026-11-22-v0.1.0.md) —
  the recorded runs
