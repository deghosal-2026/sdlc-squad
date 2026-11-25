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

**The converse is also true — a clean artifact is sometimes correct.** Zero markers is the
*right* answer when you supplied every fact (a structured backlog export, a filled roster, a
prior artifact) and the artifact used them. The defect rule flags **unexplained** cleanliness
over thin notes, not cleanliness itself. Ask one question: *did I paste the facts this
artifact claims?* If yes, clean is fine. If you pasted raw notes and still got zero markers,
something was invented.

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

### Tag what backs each claim (review by exception)

For a long or high-stakes artifact, annotate as you read with a compact tag — then read
only the claims that lack one:

| Tag | Means |
|---|---|
| `[src: notes]` | came from the input you pasted |
| `[src: prd-draft]` | came from another artifact — name it |
| `[src: org-glossary]` | came from your `my-org.md` / the glossary |
| `[CONFIRM: missing from input]` | nothing backs it yet |

Review by exception: the claims to inspect are exactly those **without a valid tag**, or
carrying `[CONFIRM: missing from input]`. (A schema-level provenance field is future work;
the tag is a reviewer's habit today — the same axis as the four claim types above.)

## 4. Separate assumptions from facts

An **assumption** is a guess that changes execution if it is wrong. The playbook's read-back
separates the two; your review enforces it:

- **Fact** — backed by a source: a paste, a quote, or a calculation shown from inputs.
- **Assumption** — the model's judgment, labeled as such — never dressed as a fact.
- **Open question** — a `Q-n`; a deliverable, not an apology.

High-impact guesses must be **inline-marked, not buried in prose**: a target release date, a
dependency owner, a migration/lock behavior, a capacity assumption. If you can't tell which
of the three a sentence is, treat it as an assumption and mark it — a fact with no visible
source is an assumption wearing a fact's clothes.

## 5. Resolving a `[CONFIRM]` on revision

When you fill one in:

1. Replace the marker with the **fact and its source** — not just the value.
2. Keep a short "**resolved in this revision**" list at the bottom of the artifact.
3. Leave the still-unresolved markers triaged by bucket (step 1).

A schema-level marking convention is future work; the practice above is yours to keep now.

## 6. Check for PII before it leaves your session

The artifact may carry facts that should not travel. Scan it before it goes anywhere:

| Replace | With |
|---|---|
| Real names | `PERSON-A`, `PERSON-B`, … |
| Email addresses | `[EMAIL]` |
| Tokens, keys, connection strings | `[REDACTED]` |
| Customer / account identifiers | `CUST-1`, `CUST-2`, … |
| Internal hostnames / URLs | `[INTERNAL-URL]` |

Full recipe: [`EXPORTS.md`](EXPORTS.md) §Redaction. This is a **human** check — the kit
detects nothing automatically (no scanner, no network). Redact, don't drop: a missing row
becomes a `[CONFIRM]` about the plan, not about a person.

## 7. Why every playbook ends with a read-back

Each skill runs a **read-back pass** on itself before handing over — every number sourced,
tables shaped, `[CONFIRM]`s placed. Your review is the second pass: the model checked
itself against the schema; you check it against **your reality**.

## Related

- [`../CONVENTIONS.md`](../CONVENTIONS.md) — the honesty discipline in full
- [`ANTI-PATTERNS.md`](ANTI-PATTERNS.md) — the failure modes these checks catch
- [`EXPORTS.md`](EXPORTS.md) — redaction, so what you paste back is safe
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — when the artifact is malformed, not just incomplete
