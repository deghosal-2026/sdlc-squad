# Anti-patterns — the failure modes, and the rule that catches each

The kit's honesty discipline is only as good as the checks behind it. This page catalogs
the **real** failure modes seen in SDLC drafting and maps each to the rule that catches it —
so a reviewer knows what to look for, and why each rule exists.

**Sources (never invented).** Every entry traces to one of three: a **recorded run** under
[`../tests/results/`](../tests/results/), a **field-feedback** issue
([`.github/ISSUE_TEMPLATE/field-feedback.md`](../.github/ISSUE_TEMPLATE/field-feedback.md)),
or the [`EVIDENCE.md`](EVIDENCE.md) retelling of the kit's own recorded pass. A failure mode
with no source does not belong on this page.

## The catalog

| Failure mode | What it looks like | The rule that catches it | Example (source) |
|---|---|---|---|
| **Invented baseline** | A number the input never gave ("~400") | every-number-sourced | `412 [source: paste]` — `pmt/draft-prd` ([`EVIDENCE.md`](EVIDENCE.md)) |
| **Invented estimate** | Effort/size with no owner input | effort-not-invented | `[CONFIRM: SDE/SDM estimate]` — `pmt/prioritize-asks` |
| **Green with no evidence** | A status that is a mood | R/Y/G-with-evidence | yellow + open mitigation — `tpm/program-status-review` |
| **Silent cut** | Scope trimmed without a name | every-cut-explicit | an explicit **Cut** row — `sdm/scope-cut-and-tradeoffs` |
| **Unmeasured claim** | "felt slow" asserted as fact | measurement-first | `[CONFIRM: unmeasured]` + propose the measure — `sdm/operational-health-review` |
| **Unquoted code claim** | A module claim with no paste | every-code-claim-quoted | quoted the paste — `sde/technical-design-and-breakdown` |
| **Hypothetical question** | "would you use …?" | Mom Test (past behavior) | a past-behavior question — `pmt/customer-discovery-and-synthesis` |
| **Threshold-less guardrail** | A metric with no line | no-guardrail-without-threshold | `[CONFIRM: threshold]` — `pmt/define-success-metrics` |
| **Risk with no fallback** | A risk row that stops at "risk" | risks-must-be-complete | fallback made mandatory — `tpm/risk-raid-and-mitigations` |
| **Missing section** | A readiness check minus a gap | all-sections-present | listed as a **gap** — `tpm/release-readiness-check` |
| **Recap theater** | A standup column that adds no signal | no-recap-theater | column removed — `sdm/standup-execution` |
| **Dropped layer** | A test layer silently empty | empty-layer-says-why | coverage note + reason — `sde/generate-test-ideas-and-cases` |
| **Fastest-signal bake** | Bake time set to the quickest metric | slowest-signal rule | corrected to the slowest — `sde/deploy-plan-and-release` |
| **Wrong unit of slicing** | A cross-cutting concern sliced as a story | vertical-slice rule | moved to **non-goal** — `pmt/slice-mvp-and-stories` |
| **Zero markers over raw notes** | A clean artifact from messy input | zero-`[CONFIRM]`-is-a-defect | [`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md) §1 |
| **PII pasted through** | Real names / hosts in the artifact | redact-before-pasting | [`EXPORTS.md`](EXPORTS.md) §Redaction |

The first fourteen rows trace to the recorded pass; the last two are the reviewer's own
checks. Where a recorded-run summary and its per-skill notes disagree, the notes win — the
kit's own rule, applied to the kit (see [`EVIDENCE.md`](EVIDENCE.md)).

## How to add a row

1. The failure mode must have a **source** — a recorded run, a field-feedback issue, or
   [`EVIDENCE.md`](EVIDENCE.md). No source, no row.
2. Name the **rule** that catches it. If no rule exists, that is a **gap to file**, not a
   row to invent.
3. Link the **example** to its source line, so a reviewer can see the catch.

## Related

- [`EVIDENCE.md`](EVIDENCE.md) — the recorded catches this page generalizes
- [`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md) — run the checks on your own artifact
- [`../tests/results/`](../tests/results/) — the recorded runs
