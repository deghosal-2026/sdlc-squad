# Companion skills — wrapping other skill sets in kit conventions

The kit is not the only skill collection. **Matt Pocock's `mattpocock/skills`**
(https://github.com/mattpocock/skills, MIT © 2026 Matt Pocock) is the most-installed
engineering/PM set on the Agent Skills registry. You can use it **with** the kit: load the
kit's conventions *around* his skills, and his outputs inherit the kit's contracts —
`[CONFIRM]` discipline, ID prefixes, ISO dates, paste-clean tables, and an import-target
block.

The kit ships **none** of his files — you install his skills yourself; the kit only tells
you how to wrap them.

## 1. Install his skills (his terms)

His README asks you to pick **one** distribution per agent (a self-updating plugin *or*
the registry's editable files — installing both gives you every skill twice), then run his
`/setup-matt-pocock-skills` once per repo (issue tracker, triage labels, doc locations).
That setup is his, in your repo — it is not part of the kit.

## 2. The wrap pattern (the point)

In an agent session, load the kit's shared conventions **before** invoking one of his
skills:

1. `shared/system-conventions.md`
2. `shared/glossary-and-org.md` (or your `my-org.md`)
3. *his* skill

Then add one instruction: *"Follow the conventions above — mark every unknown
`[CONFIRM: ...]`, use ISO dates, keep tables paste-clean, and end with an `import target`
block."* His skill does the work; the kit's rules shape the output so it lands where your
work lives.

## 3. Which of his pairs with which of ours

| His skill | Kit role to wrap with | What the wrap adds |
|---|---|---|
| `to-spec`, `to-tickets` | PMT (`draft-prd`, `slice-mvp-and-stories`) | `[CONFIRM]` discipline, schema binding, import-target block instead of tracker writes |
| `code-review` | SDE (`design-and-code-reviews`) | the `nit:`/`large-diff-split` etiquette on top |
| `pr` | SDE (`pr-plan-and-rollback-notes`) | migration order + rollback stating what it does **not** undo |
| `to-questionnaire` | PMT (`survey-design`) | bias checks, counts that trace to the paste |
| `domain-modeling` | kit glossary | org slots you own + `[CONFIRM]`-over-invention |
| `grilling`, `grill-me` | any kit skill | a grill-first pass to cut `[CONFIRM]`s before drafting |

## 4. What stays outside the kit (charter)

His skills that generate code (`implement`, `tdd`, `prototype`, …), fetch the web
(`research`), or mutate your repo (his setup) are fine as **your** companions — the kit
ships none of them and calls nothing. "Refused to ship" ≠ "don't run": run his setup if you
want it.

## 5. Runtime caveat

His engineering skills assume a coding-agent runtime; in a plain web chat they work as
disciplined prompts minus tracker integration.

## Related (in the kit's plan)

- `docs/0.1.1-plans/09-external-skills-mattpocock.md` — the full analysis (license,
  three tracks, copyright mechanics)
