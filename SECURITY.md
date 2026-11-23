# Security policy

## Reporting a vulnerability

sdlc-squad is a Markdown-only kit: no server, no telemetry, no credentials. Still, if you find
something that could mislead or harm a user — a prompt-injection path in a skill file, a fixture
that leaks real personal data, or anything a pasted document could exploit — please report it
privately:

1. Open GitHub → this repo → **Security** → **Private vulnerability reporting** (preferred), or
2. Open a draft security advisory.

Do not open a public issue with the details.

## Scope

- Skill files (`SKILL.md`), role files (`roles/`), shared contracts (`shared/`), and fixtures
  (`tests/`, once built) are in scope.
- Prompt-injection risks matter here by design: every skill treats pasted material as data, and
  any instruction embedded in user-pasted content must be flagged, never followed.
- Personal data in committed fixtures is a vulnerability: fixtures must be synthetic.

## Expectations

- The kit runs offline; any proposal that adds a network call will be rejected on charter grounds
  before it is a security question.
- Reports are acknowledged within a week (volunteer maintainer, best effort).

## Data path

The kit makes no network calls, sends no telemetry, and writes no files — it is Markdown
you paste. Your **chat provider's** handling of what you paste is separate, and yours to
verify; the kit cannot promise anything about a hosted model's data use. Full statement:
[`usage/USER-GUIDE.md`](usage/USER-GUIDE.md) §"Data path" — kept in one place on purpose.