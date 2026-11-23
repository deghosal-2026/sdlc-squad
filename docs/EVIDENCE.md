# Evidence — how the kit catches itself

The honesty discipline is the product. Here is proof it works: the catches recorded in the
kit's own v0.1.0 run. Every row traces to
[`../tests/results/run-2026-11-22-v0.1.0.md`](../tests/results/run-2026-11-22-v0.1.0.md) —
the run log is the source of record.

## Caught in the recorded pass

| Skill | What the model tried to do | What caught it | The correction |
|---|---|---|---|
| `pmt/draft-prd` | Invent a baseline ("~400") | every-number-sourced check | `412` `[source: paste]` |
| `pmt/slice-mvp-and-stories` | Slice the chatbot as a story | vertical-slice rule | moved to **non-goal**, not sliced |
| `pmt/define-success-metrics` | Ship a guardrail with no threshold | no-guardrail-without-threshold | `[CONFIRM: threshold]` discipline |
| `pmt/customer-discovery-and-synthesis` | Ask a "would you use" hypothetical | Mom Test rule | a **past-behavior** question |
| `pmt/prioritize-asks` | Invent effort numbers | effort-not-invented rule | `[CONFIRM: SDE/SDM estimate]` |
| `tpm/risk-raid-and-mitigations` | A risk row with no fallback | risks-must-be-complete | fallback made mandatory |
| `tpm/release-readiness-check` | Omit the support-runbook gap | all-sections-present | listed as a **gap** |
| `tpm/program-status-review` | Green R1 from one datum | R/Y/G-with-evidence | **yellow** + open mitigation |
| `sdm/standup-execution` | Add a yesterday-recap column | no-recap-theater | column removed |
| `sdm/scope-cut-and-tradeoffs` | Silently trim dark mode | every-cut-explicit | an explicit **Cut** row |
| `sdm/operational-health-review` | Assert "felt slow" | measurement-first | `[CONFIRM: unmeasured]` + propose the measurement |
| `sde/technical-design-and-breakdown` | Make an unquoted module claim | every-code-claim-quoted | quoted the paste |
| `sde/generate-test-ideas-and-cases` | Silently drop a load-test row | empty-layer-says-why | coverage note + reason |
| `sde/deploy-plan-and-release` | Set bake time to the fastest signal | slowest-signal rule | corrected to the slowest signal |

The log's summary table reports the count; its **per-skill notes are the source of record**.
Where a summary number and the per-skill notes disagree, the notes win — noted here rather
than smoothed over (the kit's own rule, applied to the kit).

## Why this matters

Each catch is the discipline firing: a number with no source, a green with no evidence, a
cut with no name. None of these is a model failure the kit hides — they are the checks
doing their job, recorded so you can see them. Flip through
[`../tests/results/`](../tests/results/) for the full pass.

## Related

- [`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md) — run the same checks on your own artifact
- [`../tests/README.md`](../tests/README.md) — what a fixture and a recorded run are
