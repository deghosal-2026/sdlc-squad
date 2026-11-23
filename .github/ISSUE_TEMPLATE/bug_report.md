---
name: Bug report
about: A skill produced a wrong or malformed artifact
title: "[bug] <skill-name>: <what the artifact got wrong>"
labels: bug
---

**Skill (role/name)**

**What the input was** (redact personal data before pasting)

**What the artifact got wrong**

**Which output-schema rule it broke** (see `shared/output-schemas/`)

- [ ] A `[CONFIRM]` was invented instead of marked
- [ ] A table did not match its schema columns
- [ ] An ID prefix was wrong (REQ-n / AC-n / US-n / T-n / R-n / DEP-n / M-n / TC-n)
- [ ] A non-ISO date appeared
- [ ] An owner/date/ticket key was fabricated
- [ ] The Import target block was missing or wrong

**Expected artifact shape**