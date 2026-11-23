# 08 — Competitive landscape (web scan, 2026-11-23)

Reference file, not a work list: what the scan found, and where each finding lands in
the plan. Retrieved 2026-11-23 with live web access (user's go). It feeds
[06-open-decisions.md](06-open-decisions.md) (G4, G5, G2) and shades C/D/E/F items.
Scan-time observations, not commitments — treat them like the kit treats any input:
verify before claiming.

## What was scanned

- The Agent Skills standard (`anthropics/skills`) and the skills.sh registry (Vercel)
- The two most relevant open-source competitors: `mattpocock/skills` (deep-dive in
  [09](09-external-skills-mattpocock.md)) and `GustavoGutierrez/engineering-skills`,
  plus the PM prompt-library ecosystem on GitHub
- One commercial anchor (ChatPRD pricing) and the 2026 PM-tool listicles
- Not scanned (still unverified): Agensi, Clink — the earlier marketplace notes about
  them remain secondhand

## Layer 1 — the Agent Skills ecosystem

| Fact | Source (retrieved 2026-11-23) |
|---|---|
| A skill = folder with a `SKILL.md` entrypoint; frontmatter requires only `name` (lowercase, hyphens, ≤64 chars) + `description` (what it does + when to use it); optional `scripts/`, `references/`, `assets/` alongside | anthropics/skills README + spec links |
| `anthropics/skills`: ~199k stars, ~23.3k forks, 64 commits; Apache-2.0 example skills; Claude Code plugin-marketplace registration shown in its README | github.com/anthropics/skills |
| skills.sh (Vercel, `vercel-labs/skills`): "The Open Agent Skills Ecosystem"; install via `npx skills add <owner/repo>`; ~18 listed compatible agents (Claude Code, Cursor, Codex, GitHub Copilot, Windsurf, Gemini, Cline, AMP, OpenCode, VS Code, Zed, …); sections: leaderboard, Topics, Packs, Official, security audits | skills.sh homepage |
| Publication on skills.sh is telemetry-based: public repo + valid frontmatter + synchronized README + shared install command; indexed as users install via the CLI; public skill URL drops the `skills/` folder segment | GustavoGutierrez/engineering-skills README (the publication pattern to copy) |
| Demand for the kit's exact categories (skills.sh all-time leaderboard, mattpocock/skills): `triage` ~1.1M · `codebase-design` ~988K · `code-review` ~927K · `to-prd` ~351.6K · `to-issues` ~339.1K · `to-questionnaire` ~607K · `retro` ~389.7K · `domain-modeling` ~1.0M · `to-spec` ~841K | skills.sh leaderboard |
| Two `skills.sh.json`-style registry manifests exist in the wild (`idaibin/skills` ships `skills-index.json` + `skills.sh.json`); VS Code extensions for browsing skills.sh exist (marketplace + open-vsx) | search-located repos |

Leaderboard-name caveat: `to-prd`/`to-issues` still appear on the leaderboard, but Matt
Pocock's current README catalog shows `to-spec`/`to-tickets` in their place — skills
evolve between indexing and now. Treat leaderboard names as demand evidence; the
source README as current truth.

## Layer 2 — open-source competitors

### mattpocock/skills (full deep-dive in [09](09-external-skills-mattpocock.md))

~331k stars, 27.8k forks, 559 commits. **MIT license** (`Copyright (c) 2026 Matt
Pocock` — verified from the LICENSE file itself). "Skills for Real Engineers… not vibe
coding." Anti-framework positioning: small, adaptable, composable skills; explicitly
contrasts with GSD/BMAD/Spec-Kit "owning the process." Taxonomy the kit lacks:
**user-invoked** (orchestrators) vs **model-invoked** (reusable discipline). A
`/setup-matt-pocock-skills` config skill (issue tracker, triage labels, doc locations)
— his equivalent of the kit's glossary fill. Ships `GLOSSARY.md` (shared language) and
ADR discipline inside `grill-with-docs`.

### GustavoGutierrez/engineering-skills (closest full-lifecycle competitor)

27 skills across 6 groups (foundation, requirements, spec/architecture,
governance/traceability, planning/validation/quality gates, release/observability).
Flat `skills/{skill-name}/SKILL.md` + optional scripts/references/assets. Install:
`npx skills add gustavogutierrez/engineering-skills --all` / `--skill <name>` /
`--list`. **"Recommended Flows"** — 8 named multi-skill flows (Product-to-Spec,
Architecture Design, …). Positioning: "AI-Native Engineering Governance System." PDF of
flow diagrams. MIT. Per its README (as retrieved — not a code audit): **no
`[CONFIRM]`-style anti-hallucination discipline, no persona/role isolation, no
fixtures or recorded runs, no RACI, no org-glossary customization, no import-target
blocks.**

### The PM prompt-library ecosystem

- `deanpeters/product-manager-prompts` — 119 prompt assets; **two-layer design**: the
  visible prompt + comment blocks teaching *why* it works. Idea: a teaching layer in
  the kit's prompt books.
- `aakashg/pm-prompt-library` — 25 free prompts + 82 paid (**freemium prompt
  library** — monetization signal).
- `Bhavya/gen-ai-prompts` — organized by role and use case (the kit's shape).
- `rajann44/pm-skills`, `urspavankalyan/pm-skills` — PM skills in skills.sh/Anthropic
  format (experiments, metrics, pricing, GTM, growth, failure analysis).
- `MohGanji/skills` — "skills is the new dotfiles"; curated Claude Code skills for a
  "fully agentic SDLC"; install once, bootstrap your repo.

## Layer 3 — commercial (ChatPRD anchor, retrieved 2026-11-23)

- **Free $0** (3 chats, basic model, basic templates) · **Pro $15/mo** ($179/yr) ·
  **Teams $29/seat/mo** ($349/seat/yr) · Enterprise (SSO, admin).
- What Pro converts on: premium models, **document scorecards**, custom templates,
  projects with saved knowledge, Product+Feature Knowledge Map, competitor tracking,
  all integrations + MCP connectors, hosted MCP & REST API, **built-in prototypes
  (beta)**, "Open in v0, Cursor, Lovable, Replit."
- What Teams converts on: shared workspace/templates, real-time collaboration,
  enterprise search (Atlassian, Google Drive, Teams, SharePoint), usage analytics.
- Trust posture as a paid feature: "SOC 2 Type II · Your data never trains AI models."
- 2026 PM-tool listicles (self-serving where ChatPRD ranks itself #1; directionally):
  Claude for PRDs, Dovetail for research synthesis, Miro AI for retros/sprint planning,
  Notion AI, Aha! — AI PM tooling is a crowded, paid category.

## Ideas brought back, mapped

### Adopt now — charter-safe (feeds existing plan items)

| Idea | Feeds | Note |
|---|---|---|
| Flows concept (two independent designs converged on it) | F2 relay | Competitor "Recommended Flows" + Matt's composable skills — the kit's relay is the same pattern with the human in the loop; keep F2 high priority |
| Visual flow diagrams | E3 Mermaid | Competitor ships a PDF; Mermaid in the README is the lighter, native version |
| Scorecard framing | D3 | ChatPRD charges $15/mo for "document scorecards" — D3 is the free, local, user-controlled version; frame it that way |
| Teaching layer in prompts | C-items / prompt books | deanpeters' two-layer design: one "why this works" note per prompt-book entry |
| Privacy as a paid feature | D2, E2 | "Your data never trains models" sells at $29/seat; the kit's version is stronger at the kit layer — nothing leaves at all |
| User-space config | F3 | Matt's setup skill stores config in the user's repo, not his skill files — same rule as `my-org.md` |

### Adopt with a decision

- **skills.sh / Agent Skills publication** → G4 (evidence now in hand).
- **mattpocock/skills leverage** → G5 (MIT verified; three tracks in [09](09-external-skills-mattpocock.md)).

### New candidate skills for 0.2.x+ (roadmap inputs only — NOT 0.1.1)

- From engineering-skills: ADR/decision-record skill; traceability manager (the same
  problem as the deferred cross-artifact carry fields); observability design;
  compliance/governance gate; a `judge`-style independent adjudicator with an explicit
  APPROVED/CHANGES-REQUESTED verdict.
- From mattpocock/skills: `triage` (intake state machine — binds the kit's existing
  "Ask intake & prioritization" RACI row), `grilling` (adversarial interview until
  every branch is resolved), `to-questionnaire` (async decision extraction from one
  person), `handoff` (agent-session compaction — the machine version of F2). Full
  mapping in [09](09-external-skills-mattpocock.md).

### Monetization signals

- ChatPRD anchors paid PM-AI at $15–29/user/mo.
- Freemium prompt libraries exist (25 free / 82 paid).
- The skills.sh ecosystem is free — differentiation there is evidence and discipline,
  not price.
- Agensi's 70% creator rev share remains unverified secondhand.

### Refuse with posture (charter)

- Integrations, MCP connectors, hosted API, enterprise search — ChatPRD's paid tiers
  are largely what the charter refuses; position as the local-first alternative.
- Prototypes-from-spec (beta) — code generation; charter: "Not a code generator."
- Telemetry of any kind. (skills.sh's install telemetry is the registry's, not the
  kit's — the kit makes zero calls.)

## What the scan validates about the kit's direction

The relay/flows pattern (independently invented twice), privacy-as-feature,
verb-first skill naming, and real demand for PRD/issue/retro/triage skills at
scale. Markdown skills are an ecosystem, not a niche — a 199k-star reference repo and
a registry with ~18 agents confirm the format the kit already ships.

## Gaps competitors leave that the kit already owns

Per competitor READMEs as retrieved: no one in the scan ships a per-skill recorded
pass/fail run, a `[CONFIRM]`-style anti-invention discipline, role isolation with a
RACI, an org-glossary single customization point, or import-target blocks. Positioning
line (evidence-backed): **the only kit in this scan that ships a recorded run for
every skill it claims.**

## Sources (retrieved 2026-11-23)

- github.com/anthropics/skills (README; LICENSE page; repo stats)
- skills.sh (homepage, leaderboard, agents list)
- github.com/mattpocock/skills (README; LICENSE raw file) — deep-dive in [09](09-external-skills-mattpocock.md)
- github.com/GustavoGutierrez/engineering-skills (README)
- chatprd.ai/pricing
- Search-located repos (READMEs via search results): deanpeters/product-manager-prompts,
  aakashg/pm-prompt-library, erikholmberg/ai-pm-toolkit,
  oboffil/Prompt-Engineering-for-Project-Managers, Bhavya/gen-ai-prompts,
  rajann44/pm-skills, urspavankalyan/pm-skills, MohGanji/skills, idaibin/skills
- InfoQ on Vercel skills.sh (Feb 2026); VS Code extensions for skills.sh
  (marketplace.visualstudio.com, open-vsx.org)
