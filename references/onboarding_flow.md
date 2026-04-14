# Onboarding Flow — for the `start` verb

The `start` verb runs this conversation once, at the very beginning. Ask ONE question at a time; each answer conditions the next.

**All multi-choice questions below are rendered via the `AskUserQuestion` tool (clickable options), not typed-number prompts.** Free-text answers (dates, hour counts) use conversational input.

## Writing style for all questions

Use plain, user-intent language. Avoid jargon (no "DS&A", no "structured concurrency", no abbreviations a beginner wouldn't know). Option labels read like how the user would describe themselves; descriptions say what happens if they pick it.

Files are written ONLY at the very end, after the user confirms. During Q1–Q6 the skill asks questions; no file writes.

## Question 1 — Why are you practicing?

Call `AskUserQuestion`:
- **Question:** "What brings you here?"
- **Header:** "Your goal"
- **Options:**
    - `I have an interview coming up` — "Target-specific prep for a real upcoming interview (company, role, date)"
    - `I want to learn algorithms from scratch` — "Build data structures and algorithms skills from the ground up; no deadline pressure"
    - `I'm sharpening rusty skills` — "Returning after a break; want a structured refresher"

Store the selected label as `purpose` in SKILL_STATE.md. Map to internal values:
- `I have an interview coming up` → `interview_prep`
- `I want to learn algorithms from scratch` → `dsa_foundations`
- `I'm sharpening rusty skills` → `general_refresh`

## Question 2 — Which programming language?

Call `AskUserQuestion`:
- **Question:** "Which language will you write your solutions in?"
- **Header:** "Language"
- **Options:**
    - `Python` — "I'll set up a virtual environment and pytest for you automatically"
    - `Another language` — "Roadmap and AI hints still work; you handle your own environment setup"

If `Another language` is selected, ask in conversation: "Which one? (e.g., Java, JavaScript, Go)". Store as-is. Let the user know: "Got it — I'll skip the Python-specific setup; you'll run and test your solutions yourself."

## Question 3 — How much practice do you already have?

Call `AskUserQuestion`:
- **Question:** "How familiar are you with coding interview problems?"
- **Header:** "Experience"
- **Options:**
    - `Totally new` — "I haven't solved algorithm problems before; explain things thoroughly"
    - `A little` — "I've dabbled with LeetCode or similar; give me moderate detail"
    - `Regular practice` — "I solve these often; keep explanations concise"

Store as `experience_level` (values: `new`, `some`, `regular`). This calibrates how much context the skill provides in explanations.

## Question 4 — When or how much?

Branches based on Q1:

**If they picked `I have an interview coming up`:**
- Ask in conversation: "When's the interview? (a date like 2026-05-15, or say 'I don't know yet' if it's not scheduled)"
- Parse as ISO date. If "don't know" / unparseable → `target_mode = "open_ended"`, `target_value = null`.
- Otherwise `target_mode = "interview_date"`, `target_value = <ISO string>`.

**Otherwise (learning from scratch or refreshing):**
- Ask in conversation: "How many hours per week can you realistically practice?"
- Parse as integer. If unparseable → re-ask once, then default to 3 and proceed.
- `target_mode = "weekly_hours"`, `target_value = <int>`.

## Question 5 — Which topics do you want to practice?

Call `AskUserQuestion`:
- **Question:** "Which topics do you want on your roadmap?"
- **Header:** "Topics"
- **Options:**
    - `Interview essentials` — "The 6 topics that cover most tech interviews: arrays/strings, linked lists, stacks/queues, trees/graphs, recursion/DP, sorting/searching (59 problems)"
    - `Everything in the book` — "All 11 chapters, 133 problems. Thorough but long."
    - `Just the core 3` — "Arrays/strings, trees/graphs, recursion/DP only — fastest path to practicing the most-common interview patterns (35 problems)"
    - `Let me pick` — "I'll tell you which chapter numbers I want"

On `Let me pick`, go to step 5b. Otherwise, apply the preset and proceed to Q6:
- `Interview essentials` → `arrays_strings, linked_lists, stacks_queues, trees_graphs, recursion_dp, sorting_searching`
- `Everything in the book` → all 11 slugs
- `Just the core 3` → `arrays_strings, trees_graphs, recursion_dp`

### Step 5b — custom selection (only if `Custom selection` chosen)

Ask in conversation:
> Which chapters? List by number, comma-separated. Available:
> - 1 Arrays & Strings
> - 2 Linked Lists
> - 3 Stacks & Queues
> - 4 Trees & Graphs
> - 5 Bit Manipulation
> - 6 Math & Logic
> - 7 Object-Oriented Design
> - 8 Recursion & DP
> - 10 Sorting & Searching
> - 16 Moderate
> - 17 Hard

Parse comma-separated integers. Map to topic slugs via `references/chapter_map.md`. Store as comma-separated `selected_topics` in SKILL_STATE.md.

## Question 6 — How much of a hint do you want?

Call `AskUserQuestion`:
- **Question:** "When you ask for a hint, how much do you want by default?"
- **Header:** "Hint depth"
- **Options:**
    - `A small nudge` — "Just a pointed question about your code, like 'did you notice line 12 skips the last element?' Solve it yourself."
    - `Name the technique` — "Say what approach applies (BFS, two pointers, hash map, etc.) and why. More help, still your solution to write."

Store as `hint_level_default` (1 for small nudge, 2 for technique). You can always ask for more hints — the second and third hint each go one level deeper.

## After all 6 answers

Acknowledge summary in conversation:
> Got it — here's your setup:
> - Goal: {purpose label}
> - Language: {language label}
> - Target: {target summary}
> - Topics: {topic count} chapters, {problem count} problems
> - Default hint depth: {nudge|technique}

Then call `AskUserQuestion`:
- **Question:** "Ready to create your practice workspace?"
- **Header:** "Create files"
- **Options:**
    - `Yes, set it up` — "Create the Python environment, roadmap, and profile files in this folder"
    - `Not yet` — "Don't create anything; I can re-run onboarding later"

On `Yes, set it up`:
1. Create `.venv/`, install pytest (Python only)
2. Write `conftest.py`, `.gitignore`
3. Write `SKILL_STATE.md` from `templates/SKILL_STATE.template.md` with the collected answers
4. Read `references/chapter_map.md`, filter by selected topics, emit `ROADMAP.md` (all entries `[ ]`)
5. Create `session_log.md` with a single "onboarding completed" entry
6. Print: `All set. Run /ctci-practice next to start your first problem.`

On `Not yet`: don't write anything. Tell the user: "No files created. Run `/ctci-practice start` whenever you're ready."

## Preference defaults (not asked at onboarding)

These are NOT asked during onboarding (too many questions up front). They default to:
- `explanation_style`: `full` for new users; `terse` for regular. User can override anytime via plain English: "use terse explanations".
- `diagrams_style`: `mermaid` (Claude Code renders it).
- `solution_style`: `no_preference`.

When a user makes a preference statement during a session, the skill acknowledges and writes it to SKILL_STATE.md — without any AskUserQuestion (preference statements are unambiguous).

## Re-onboarding

If `/ctci-practice start` is run when `SKILL_STATE.md` already exists, call `AskUserQuestion`:
- **Question:** "You've already got a practice setup here. What would you like to do?"
- **Header:** "Re-onboard"
- **Options:**
    - `Keep going where I left off` — "Don't change anything; show my current status"
    - `Change my preferences` — "Redo the questions; keep my problem progress"
    - `Start completely over` — "Erase everything (progress, files, environment) and start fresh — this cannot be undone"

On `Start completely over`, confirm via a second `AskUserQuestion`:
- **Question:** "Are you sure? This will delete your progress and all practice files."
- **Header:** "Confirm erase"
- **Options:**
    - `Cancel, keep my work` — "Don't delete anything"
    - `Yes, erase everything` — "Permanently delete practice/, ROADMAP.md, session_log.md, SKILL_STATE.md"

Only execute the delete on explicit `Yes, erase everything` selection.
