# Onboarding Flow — for the `start` verb

The `start` verb runs this conversation once, at the very beginning. Ask ONE question at a time; each answer conditions the next.

## Opening message

> I'll set up an AI-guided Cracking the Coding Interview practice workspace here. I'll ask 6 quick questions, then build your roadmap and a Python env. Ready?

Wait for acknowledgment. If the user says no or wants to discuss, don't push — answer questions, re-offer when they're ready.

## Question 1 — Purpose

> What's the goal?
> 1. Interview prep (company-specific)
> 2. DS&A foundations (building the skill from scratch)
> 3. General refresh (returning after a break)

Store as `purpose` in SKILL_STATE.md.

## Question 2 — Language

> Which language?
> 1. Python (recommended — v1 has full scaffolding)
> 2. Other (Java / JavaScript / etc. — basic support, no env scaffold yet)

Store as `language`. If "other", ask which, note as-is, and warn: "v1 has full support only for Python; for other languages, the skill will still manage roadmap + hints + review, but won't auto-setup your environment."

## Question 3 — Experience level

> How much problem-solving practice do you have?
> 1. New — this is my first structured DS&A practice
> 2. Some — I've done LeetCode/HackerRank casually
> 3. Regular — I practice often, want structured review

Store as `experience_level`. This calibrates how much context the skill includes in explanations (new = more hand-holding; regular = terse).

## Question 4 — Target

If Q1 was "interview prep":
> When's the interview? (date, or "don't know / open-ended")

If Q1 was "DS&A foundations" or "general refresh":
> How many hours per week can you commit?

Store as `target_mode` ("interview_date" | "weekly_hours" | "open_ended") and `target_value` (ISO date string, hours int, or null).

This drives pacing — a 2-week interview window means fewer total problems with more focus; 5 hours/week open-ended means full coverage across chapters.

## Question 5 — Topic coverage

Show the full CtCI chapter list (read `references/chapter_map.md` for the list). Ask:

> Which chapters? (type numbers comma-separated, or "all")
> 1. Arrays and Strings
> 2. Linked Lists
> 3. Stacks and Queues
> 4. Trees and Graphs
> 5. Bit Manipulation
> 6. Math and Logic Puzzles
> 7. Object-Oriented Design
> 8. Recursion and Dynamic Programming
> 10. Sorting and Searching
> 16. Moderate
> 17. Hard

Store selected topic slugs as comma-separated `selected_topics` in SKILL_STATE.md.

**Tip-based default:** if the user says "don't know, I want the interview essentials", auto-select: Arrays/Strings, Linked Lists, Stacks/Queues, Trees/Graphs, Recursion/DP, Sorting/Searching. These cover the vast majority of first-round FAANG questions.

## Question 6 — Hint default depth

> When you ask for a hint, how deep should the first hint be by default?
> 1. Nudge (L1) — a question pointing at your code (recommended)
> 2. Direction (L2) — name the technique + approach

Store as `hint_level_default` (1 or 2). User can always override per-request later.

## After all 6 answers

Acknowledge summary:
> Great — here's what I'm setting up:
> - Purpose: {purpose}
> - Language: {language}
> - Target: {target summary}
> - Topics: {topic count} chapters, {problem count} total problems
> - Default hint depth: L{N}

Then ask for a single confirmation:
> Shall I create the files and env? (y/N)

On `y` / `yes`:
1. Create `.venv/`, install pytest (if Python)
2. Write `conftest.py`, `.gitignore`
3. Write `SKILL_STATE.md` from `templates/SKILL_STATE.template.md` with the collected answers
4. Read `references/chapter_map.md`, filter by selected topics, emit `ROADMAP.md` (all entries `- [ ]` initially)
5. Create empty `session_log.md` with a single entry for "onboarding completed"
6. Print: "Setup done. Run `/ctci-practice next` to scaffold your first problem."

On `n` / `no`: don't write anything. Tell user they can re-run `/ctci-practice start` anytime.

## Preference defaults (not asked at onboarding — prompted later when relevant)

These are NOT asked during onboarding (too many questions up front). They default to:
- `explanation_style`: "full" (new user), "terse" (regular user). User can override anytime: "use terse explanations".
- `diagrams_style`: "mermaid" (modern default; Claude Code renders it)
- `solution_style`: "no_preference"

When a user makes a preference statement during a session, the skill acknowledges and writes it to SKILL_STATE.md.

## Re-onboarding

If `/ctci-practice start` is run when `SKILL_STATE.md` already exists:
> You already have a setup here. Options:
> 1. Resume existing (recommended — run `/ctci-practice status`)
> 2. Re-run onboarding (keeps existing practice/ but overwrites SKILL_STATE and ROADMAP)
> 3. Wipe everything and start over (will delete practice/, ROADMAP.md, session_log.md)

On (3), confirm twice before deleting anything.
