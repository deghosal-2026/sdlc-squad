# Limitations — what the kit does not do

Honesty is the product, so the limits are stated as plainly as the strengths. Every limit
below is paired with the mitigation the kit ships; where there is no mitigation yet, it says
so.

## Enforcement is a prompt convention, not a program

The `[CONFIRM]` discipline and the schema binding live in **instructions**. A model that
ignores instructions can still invent a date or skip a marker — "zero `[CONFIRM]`s is a
defect" is a useful heuristic, not a guarantee. **Mitigation:** the reviewer's checklist
([`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md)) catches what the model misses, and the
[`ANTI-PATTERNS.md`](ANTI-PATTERNS.md) catalog names the failure modes. A deterministic
linter is future work (0.2.0).

## The relay is manual (copy-paste between sessions)

Running the loop PMT → TPM → SDM → SDE means pasting an artifact between single-role
sessions. The kit does not automate that hand-off, and an artifact is only as accurate as
what you paste in. **Mitigation:** session bundles and `sdlc-squad prompt` cut the load cost;
[`../usage/RELAY.md`](../usage/RELAY.md) and [`../usage/FEATURE-RELAY.md`](../usage/FEATURE-RELAY.md)
make the carry explicit.

## Destination fit is partly unobserved

Import behavior varies by instance. The observed/unobserved state is recorded in the
[`../shared/destinations/`](../shared/destinations/) ledger — Jira Data Center and
Confluence's storage-format and code-block paths are **not** validated. **Mitigation:** the
ledger marks each unobserved path `[CONFIRM]`; test against your own instance first.

## Static artifacts drift from live systems

A sprint plan, RAID log, or design goes stale the moment scope shifts or someone takes
unplanned PTO. The kit drafts the artifact; it does not keep it in sync. **Mitigation:** the
revision path ([`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) §5) and re-running the skill on
fresh exports; a diff-aware update mode is future work (0.2.0).

## One recorded runner

The recorded runs were produced with the model named in
[`MODELS.md`](MODELS.md) — the only model statement with evidence. **Mitigation:** the
one-session self-check certifies *your* model before you trust it.

## English only

The documentation is English. **Mitigation:** none yet — noted honestly rather than
promised.

## Related

- [`MODELS.md`](MODELS.md) — certify your model; the evidence-gated failure table
- [`TOOLS.md`](TOOLS.md) — supported vs. adaptable vs. never
- [`../shared/destinations/README.md`](../shared/destinations/README.md) — the validation ledger
