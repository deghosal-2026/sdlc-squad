---
name: customer-discovery-and-synthesis
description: Run customer discovery — a Mom Test interview guide, and synthesis of pasted notes into themes with verbatim quotes. Use when you need customer evidence before defining a problem.
role: pmt
status: built
created: 2026-11-22
---

# customer-discovery-and-synthesis — interview guide + feedback synthesis

## What it produces

Two artifacts, run separately or in sequence: (1) a **customer-discovery interview guide** —
objectives, screening criteria, the conversation flow, and open questions (never leading
ones); (2) a **feedback synthesis** — themes, verbatim quotes, needs, and the signals vs.
anecdotes split, from notes the user pastes back.

## RACI row

`Customer discovery & synthesis` — **PMT A/R** (`shared/raci.md`); TPM I · SDM I · SDE C.

## Inputs required

- The decision this research informs (feature, problem, segment)
- Who is reachable: customers, prospects, churned users, support threads
- Pasted interview notes / call transcripts / support threads, for the synthesis run

## Clarifying questions when inputs are missing

1. What decision changes depending on what we hear?
2. Who do we most need to hear from — and who did support already hear from?
3. What did they actually say? (Paste the notes; I quote, never paraphrase from memory.)

## Steps — guide run

1. **Pin the decision.** One line: what this research changes. No decision named → ask
   before drafting anything.
2. **Screening criteria.** Who is in, who is deliberately out (a happy user is not a churned
   user), and how to find them.
3. **The flow.** Open → their life → the problem → the past → close. Mom Test rules
   throughout: their life not your idea, specifics in the past not hypotheticals, listen
   more than talk.
4. **Open questions only.** "Tell me about the last time…" / "How do you handle it today?" /
   "What did that cost you?" Never "Would you use X?" — hypotheticals flatter, history is
   evidence. Compliments and pitches get deflected with "what did you try then?"
5. **Read-back pass.** No leading or double-barreled questions; the guide is runnable by
   someone who was not in the room when it was written.

## Steps — synthesis run

1. **Paste in, quote out.** Every claim about a customer carries a verbatim quote from the
   paste. No paraphrase-as-evidence.
2. **Cluster into themes.** With the count behind each theme (N of M interviews mentioned
   it — counts from the paste only).
3. **Needs, not solutions.** Each theme names the underlying need; a customer's proposed
   solution is recorded as their words, not adopted as the requirement.
4. **Signal vs. anecdote.** Repeated, specific, recent = signal; single, vague, or
   hypothetical = anecdote, labeled as such.
5. **Hand to the PRD.** Themes become Problem & context evidence; quotes become the
   verbatim evidence rows.

## Output binding

`shared/system-conventions.md` table rules; quotes verbatim or `[CONFIRM: source]`.

## Import target

Confluence — the research page for this initiative.

## Worked example

`tests/pmt/customer-discovery-and-synthesis/fixture.md` — full input + expected artifact
(synthetic, both runs). Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
