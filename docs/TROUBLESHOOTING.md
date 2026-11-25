# Troubleshooting & recovery

The predictable ways a session goes wrong, and the one-move fix for each. Every remedy
restates a rule the kit already ships — nothing new is invented here.

## 1. The model ignored the schema

**Symptom:** the artifact's sections or columns don't match the skill's output binding.

**Recovery:** re-paste the skill's `SKILL.md` (or the session bundle) and say: *"Re-emit
the artifact bound to `shared/output-schemas/<schema>.md` — exactly its sections and
columns."* The binding is named in the skill's **Output binding** section.

## 2. The model invented a fact

**Symptom:** a date, owner, ticket key, SLA, or number appears with no source.

**Recovery:** quote the never-guess rule back: *"Per the kit's charter, never invent
ticket keys, dates, owners, SLAs, or numbers. Re-emit with `[CONFIRM: ...]` wherever you
didn't have a source."* Then check every number against your input
([`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md)).

## 3. Tables are mangled or un-pasteable

**Symptom:** broken alignment, HTML, collapsed sections, or pipes inside cell bodies.

**Recovery:** re-request bound to the schema's exact columns: *"Plain Markdown table:
header row + alignment row, no HTML, no collapsible sections, no pipes in cell bodies."*
(`../CONVENTIONS.md`, Markdown contracts.) Destination specifics:
[`../shared/destinations/`](../shared/destinations/).

## 4. The session drifts or hits the context limit

**Symptom:** quality falls off, the role blurs, or the model forgets the load.

**Recovery:** start a **fresh session**. Paste the four files (or the bundle) plus the
current artifact, and continue — still one role. Long sessions drift; a clean reload is
cheaper than nursing one.

**When the load itself is too big (the long-load recipe).** A full load is four files
≈ 340–370 lines, or one bundle. If that plus your input exceeds the model's context, drop in
this order — **never the last two**:

| Drop first | Keep always |
|---|---|
| The **template glossary** — once your `my-org.md` is in the session, the shipped template adds nothing | The **skill playbook** (`SKILL.md`) — it defines the steps and the output binding |
| The **role file** on a *repeat* run of the same role — its contract is already in the artifact | The **bound schema** (`shared/output-schemas/<schema>.md`) — the artifact's columns |

Never drop the skill or the schema: without them the artifact is unbound, and you are back
to step 1. If dropping the two optional files still isn't enough, **split the input** — feed
the skill only the part this artifact needs, and keep the rest for the next.

## 5. You need a revision after review

**Symptom:** a reviewer asked for changes; you don't want to start over.

**Recovery:** paste the load (or bundle) + the emitted artifact + the feedback, and ask
for the revision bound to the same schema. Never re-explain from scratch. Record resolved
`[CONFIRM]`s per [`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md) §4.

## 6. You're not sure it's working at all

**Symptom:** you can't tell if the model is following the kit.

**Recovery:** the one-session self-check in [`MODELS.md`](MODELS.md) — five things a
trustworthy run does. If they all pass, the kit is working; if not, step 1 or 2 above.

## Related

- [`MODELS.md`](MODELS.md) — certify your model in one session
- [`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md) — the pre-paste checklist
- [`../usage/USER-GUIDE.md`](../usage/USER-GUIDE.md) — the run sheet
