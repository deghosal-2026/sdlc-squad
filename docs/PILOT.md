# Pilot — a 2-week, one-team trial

How to try the kit with **one squad** and two skills, and get an honest read on whether it
helps — without a rollout, a mandate, or any new tooling. The metrics come from the shipped
field-feedback template ([`.github/ISSUE_TEMPLATE/field-feedback.md`](../.github/ISSUE_TEMPLATE/field-feedback.md));
nothing is collected automatically.

## 1. Pick one squad and two skills

Start where the pain is highest, not where the kit is broadest. Suggested pairs:

| Who | Skills to trial |
|---|---|
| EMs / TPMs | `sdm/sprint-planning-and-capacity` + `sdm/scope-cut-and-tradeoffs` |
| SDEs | `sde/pr-plan-and-rollback-notes` + `sde/technical-design-and-breakdown` |
| PMs | `pmt/slice-mvp-and-stories` + `pmt/draft-prd` |

## 2. Co-design `my-org.md` first

Before day one, fill the org glossary with the squad's real terms — service names, release
windows, escalation path, definition-of-done ([`UPGRADING.md`](UPGRADING.md)). Outputs that
use real internal terms on day one are what builds trust; a glossary full of `[CONFIRM]`s is
not a fair trial.

## 3. Run it for two weeks

Each run: load the skill (or a bundle), paste the real input, answer the questions, review the
artifact ([`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md)), then paste it into the real target.

## 4. Measure (before / after)

Capture the same few signals the feedback template asks for — no dashboards:

- time to a first useful draft;
- defects caught before review (missing acceptance criteria, missing rollback steps, an
  ungrounded number);
- review cycles per artifact;
- would the team reuse it?

## 5. Decide

At the end of two weeks, make one call: **adopt**, **adapt** (which skill, which glossary
change), or **stop**. Record it as a field-feedback issue — the honest result, including
"stopped", is the useful one.

## What this is not

Not a rollout, not a mandate, and not a metric to report upward — a trial whose purpose is to
learn whether the artifacts hold up on **this** team's real work.

## Related

- [`.github/ISSUE_TEMPLATE/field-feedback.md`](../.github/ISSUE_TEMPLATE/field-feedback.md) — the metrics, opt-in
- [`START-HERE.md`](START-HERE.md) — pick the skills by task
- [`UPGRADING.md`](UPGRADING.md) — the shared `my-org.md` and the ownership rule
