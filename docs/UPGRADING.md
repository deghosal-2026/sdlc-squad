# Upgrading sdlc-squad — your file vs. the kit's

The kit has one customization point (the org glossary) and two distribution paths
(`pip` and clone). Both would overwrite a filled glossary **if** it lives inside the
kit. This page is the fix: keep your customization outside the kit, and upgrades never
touch it.

## The rule: your personalization lives outside the kit

- **Your** file: a filled copy of the org glossary, kept wherever you like —
  `my-org.md` (any name). At load step 2, paste **your** file in place of the shipped
  `shared/glossary-and-org.md`.
- **Why:** `pip install --upgrade sdlc-squad` replaces the installed tree (including a
  filled `shared/glossary-and-org.md` under `site-packages`); `git pull` conflicts with
  an edited tracked file. A file **outside the kit** survives both.
- The shipped `shared/glossary-and-org.md` stays the clean template; the filled example
  is `shared/glossary-and-org.EXAMPLE.md` (fictional org — copy its shape, not its facts).

## Upgrade paths

### pip (file distribution)

```bash
pip install --upgrade sdlc-squad   # replaces the kit files; your my-org.md is untouched
sdlc-squad                          # prints the new kit path + load order + version
```

Your `my-org.md` lives wherever you keep it — not under `site-packages` — so the
upgrade replaces the kit and nothing of yours.

### clone

```bash
git pull                            # fast-forwards the kit
```

Keep `my-org.md` **untracked** (add it to `.gitignore`) or outside the repo entirely.
Never edit the tracked kit files to hold org facts — that is the conflict you are
avoiding.

## Ownership table

| Yours | The kit's |
|---|---|
| Your filled org glossary (`my-org.md`) | Every file in the repo/package |
| Your destination profiles (`my-jira.md`, `my-confluence.md`, `my-github.md` — [`DESTINATION-PROFILES.md`](DESTINATION-PROFILES.md)) | The profile *templates* the kit ships |
| Generated artifacts and saved outputs (`output/`, git-ignored) | `shared/`, `roles/`, `skills/`, `usage/`, `docs/` |

- **Extend in place, never fork** the kit's files — the standing rules in
  [`EXTENDING.md`](EXTENDING.md) apply (one canonical copy; the RACI mirror rule).
- If you *do* customize more than the glossary (a schema, a role, a skill), you have a
  fork — and you own its upgrade and regression routine (EXTENDING Paths 2–4).

## What 0.1.2 adds

Upgrading from 0.1.1 to 0.1.2 adds docs and tooling; **nothing of yours moves.**

- New pages: [`LIMITATIONS.md`](LIMITATIONS.md), [`PILOT.md`](PILOT.md),
  [`DESTINATION-PROFILES.md`](DESTINATION-PROFILES.md),
  [`GITHUB-TEMPLATES.md`](GITHUB-TEMPLATES.md), [`ANTI-PATTERNS.md`](ANTI-PATTERNS.md), and
  this docs [`index`](README.md).
- `docs/REVIEWING-OUTPUT.md` gains the claim tags, the assumption-vs-fact split, the
  clean-artifact rule, and a PII pre-paste check; `docs/MODELS.md` gains a 60-second
  benchmark and an evidence-gated failure table.
- Your `my-org.md` — and any destination profiles — are **untouched** (they live outside the
  kit). No schema, skill, or CLI behaviour changed.

## After an upgrade

1. `sdlc-squad` — confirm the version and the new kit path.
2. Confirm your `my-org.md` is intact and still pasted at load step 2.
3. If you use session bundles, regenerate them from the new kit (`make bundles`) so they
   are not stale.

## Team use (sharing one setup)

- **One shared `my-org.md`**, one owner: a private repo or a shared drive. It is the
  single source of truth for org facts — nobody edits a private copy.
- **Generated artifacts** live locally in the git-ignored `output/`, or in the system of
  record (Jira/Confluence/GitHub). Never commit real org data to the kit.
- **Across people, not just sessions:** the relay (PMT → TPM → SDM → SDE) carries an
  artifact from one person's session to the next the same way it carries it between one
  person's sessions — the artifact and the unresolved `[CONFIRM]`s (the relay recipe,
  `usage/RELAY.md`, ships with the lifecycle items).

## Related

- [`EXTENDING.md`](EXTENDING.md) — the four customization paths and their rules
- [`../usage/USER-GUIDE.md`](../usage/USER-GUIDE.md) — the load order this page assumes
