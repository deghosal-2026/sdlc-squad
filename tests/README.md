# tests/ — fixtures and recorded runs

- `tests/<role>/<skill>/fixture.md` — one fixture per skill: synthetic input, the expected
  artifact skeleton, and the **Checks** list (the skill's acceptance, per CONVENTIONS.md).
  Every company, person, path, ticket, and date in a fixture is invented.
- `tests/results/` — recorded runs: each playbook executed against its fixture, the
  read-back against the checks, and every defect found & fixed in the pass. Committed kit
  evidence — unlike `output/`, which is git-ignored user work.

Never paste real customer data into a fixture; if a real run supplied the shape, the
fixture is rewritten synthetic. `output/` at the repo root is the scratch space for live
runs — never committed, never pushed.