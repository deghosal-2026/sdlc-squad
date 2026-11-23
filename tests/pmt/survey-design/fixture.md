# Fixture — pmt/survey-design

Synthetic end to end. Two runs: instrument, then read-back.

## Input (instrument run)

> "One question: do guest users trust an unauthenticated status page? Audience: recent
> order-email recipients. Expected n ≈ 200."

## Expected artifact — instrument (skeleton)

# Survey: guest status trust
## Objective (singular): does unauthenticated status page trust support self-serve rollout?
## Sampling: recent order-email recipients; self-selection risk named (responders skew engaged) — offset: send to every 5th recipient.
## Questions (typed, bias-checked)
| Q1 single | "How did you check your last order?" options incl. order email/carrier site/called | bias: none — past behavior |
| Q2 scale | "1=never … 5=daily: I trust pages that show my order without login" | endpoints stated; double-barrel checked: none |
| Q3 open | "What made you hesitate (if anything)?" | leading framing checked: none |
## Order: Q1 → Q3 → Q2 → demographics last.

## Input (read-back run)

> Pasted results: n=137 of 200; Q2 mean 3.2; open-ends: 41 mention "looks like a phish",
> 9 mention layout.

## Expected artifact — read-back (skeleton)

# Read-back: n=137 (68.5% response)
- Q2 mean 3.2 [paste], distribution chart from paste.
- Open-end quote (verbatim): "the link looks like a phish" — 41/137 mentions.
- Limits: self-selected sample; no extrapolation beyond the 137; Q2 phrasing caution noted.

## Checks

- [ ] One objective, stated before any question
- [ ] Every question carries its bias-check line
- [ ] Counts trace to the paste; no extrapolation to a population
- [ ] Limits section present, not a footnote