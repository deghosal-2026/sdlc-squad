# Reviewing an artifact before you paste it

A skill hands you one Markdown artifact. Your job before it ships is a short,
mechanical review — the same discipline the kit applies to itself. Think of it as a
**scorecard you run locally, for free, with nothing leaving your machine**.

## 1. Triage every `[CONFIRM]`

Markers are not failures — they are the kit refusing to invent. Sort them:

| Bucket | Meaning | Action |
|---|---|---|
| **Blocks a decision** | The recommendation can't be made without it (a size, a date, an owner) | Resolve now, or the artifact isn't decision-ready |
| **Needed before implementation** | Fine for review, fatal for build | Resolve before the work starts |
| **Can be filled later** | Formatting-completion, non-load-bearing | Fill whenever — or leave it |

An artifact with **zero `[CONFIRM]`s and zero user-supplied inputs** is a defect — something
was invented (`../CONVENTIONS.md`, honesty discipline). Go find it before you trust it.

## 2. Verify the high-impact facts

Before pasting, check the cells that would hurt if wrong:

- **Dates** are ISO (`YYYY-MM-DD`) and come from your input, not the model.
- **Owners** are real names — never a role title wearing a person's clothes.
- **Numbers** each carry a source (a paste, a quote) or a `[CONFIRM]`. Arithmetic is
  *shown*, not asserted (the capacity tables are the exemplar).
- **High-impact claims** — value, risk ratings, milestone dates — are the first things to
  inspect. A polished artifact can still be wrong.

## 3. Know what kind of claim you're reading

Tag each material statement as you read:

- **Source-backed fact** — carries its paste/quote. (Trust it; the source is visible.)
- **Calculation** — arithmetic shown from inputs. (Check the inputs once, not the math.)
- **Inference** — the model's judgment. (Labeled as such, never dressed as fact.)
- **Open question** — a `Q-n`. (A deliverable, not an apology.)

## 4. Resolving a `[CONFIRM]` on revision

When you fill one in:

1. Replace the marker with the **fact and its source** — not just the value.
2. Keep a short "**resolved in this revision**" list at the bottom of the artifact.
3. Leave the still-unresolved markers triaged by bucket (step 1).

A schema-level marking convention is future work; the practice above is yours to keep now.

## 5. Why every playbook ends with a read-back

Each skill runs a **read-back pass** on itself before handing over — every number sourced,
tables shaped, `[CONFIRM]`s placed. Your review is the second pass: the model checked
itself against the schema; you check it against **your reality**.

## Related

- [`../CONVENTIONS.md`](../CONVENTIONS.md) — the honesty discipline in full
- [`EXPORTS.md`](EXPORTS.md) — redaction, so what you paste back is safe
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — when the artifact is malformed, not just incomplete
