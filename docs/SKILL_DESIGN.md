# ctci-practice — v1 MVP Design

**Goal (one sentence):** An AI-guided companion for working through *Cracking the Coding Interview*-style problems: onboarding, adaptive roadmap, just-in-time problem scaffolding, progressive hints, automated validation, and cross-session resumability.

**Scope discipline:** This is an MVP. Every feature below has a direct line to the goal above. Features with no line are in `NON_GOALS` at the bottom.

---

## 1. Installation & invocation

- **Install path:** `~/.claude/skills/ctci-practice/SKILL.md`
- **Invoke:** `/ctci-practice <verb> [args]` — or plain-English ("start CtCI practice", "give me a hint", "what's next?") auto-routes to the skill when it matches triggers in SKILL.md
- **Target directory:** the CWD Claude Code is launched in. Skill creates files there; does not assume a specific path.

---

## 2. File layout the skill creates

```
<project root>/
├── ROADMAP.md                 # single source of truth for progress
├── SKILL_STATE.md             # user profile, preferences, confidence scores
├── .venv/                     # python env (gitignored)
├── conftest.py                # adds per-problem dir to sys.path
├── .gitignore                 # venv + pycache + editor cruft
├── practice/
│   ├── block_01_<topic>/
│   │   ├── README.md          # block intro (generated on first entry)
│   │   ├── CHEATSHEET.md      # dense reference (generated on demand)
│   │   └── p<N>_<slug>/
│   │       ├── README.md      # problem spec — I/O contract at TOP
│   │       ├── solution.py    # starter with TODOs
│   │       ├── test_basic.py  # example cases — run while iterating
│   │       ├── test_full.py   # edge cases + perf — "submit" equivalent
│   │       ├── HINTS.md       # append-only log of hints given
│   │       └── SOLUTION.md    # ONLY written when user invokes `solve`
│   └── block_02_.../
├── explanations/
│   └── <concept>.md           # JIT-generated concept explainers
└── session_log.md             # one line per session — continuity across restarts
```

**Why this shape:**
- `ROADMAP.md` is a plain markdown checklist — humans can edit it directly, git-diffable, no lock-in.
- Per-problem folder mirrors what worked in today's cram session.
- `HINTS.md` is append-only — the hint history is visible and re-readable.
- `SOLUTION.md` written only on `solve` — unblocks temptation-free attempting.

---

## 3. State model

**Three files store all persistent state. No hidden database.**

### `ROADMAP.md` — progress, source of truth
Checkbox states:
- `- [ ]` — not started
- `- [-]` — in progress (started, not validated)
- `- [x]` — complete (tests passed AND code review clean)
- `- [!]` — blocked / needs help (user-marked)

Example:
```markdown
# Roadmap — Python / Interview / 2 weeks

## Block 1 — Python refresh (self-rated: 4/5)
- [x] drill1: async TaskGroup scraper
- [x] drill2: dataclass + match + Self

## Block 2 — Graphs (self-rated: 2/5)
- [x] p1: Route between nodes (BFS)
- [-] p2: Build order (Kahn's topo)
- [ ] p3: Validate BST

## Block 3 — Dynamic Programming (self-rated: 2/5)
- [ ] p1: Triple step
- [ ] p2: Robot in a grid
```

### `SKILL_STATE.md` — profile, prefs, confidence
```markdown
# Skill State

## Profile
- Purpose: interview prep
- Language: Python 3.13
- Target date: 2026-04-27
- Level (self-rated): fluent Python, rusty DS&A
- Source: CtCI 6th edition (Python folder)

## Confidence (1=weak, 5=strong) — user-rated, adjusted over time
- arrays_strings: 4
- linked_lists: 3
- stacks_queues: 3
- trees_graphs: 2
- dp: 2
- sorting_searching: 3
- python_language: 4

## Preferences (learned via explicit user statements)
- Explanations: skip basics, I own the book
- Diagrams: mermaid preferred
- Solution style: prefer iterative over recursive when comparable
- Hint depth: default L1 nudge
```

### `session_log.md` — continuity
Append-only, one block per session:
```markdown
## 2026-04-13 10:42 → 12:15 (93min)
- Completed: block1 drill1, drill2
- In progress: block2 p1 (route_between_nodes) — tests passing, bidirectional stretch skipped
- Next: block2 p2 (build order)
- Notes: user prefers terse readmes, asked for mermaid on Kahn's
```

---

## 4. Commands (the verbs)

Every command is a subagent-delegated job when it involves generation or code review. Main thread only orchestrates.

### `/ctci-practice start`
- Onboarding conversation (Q&A flow — see §5)
- Generates `SKILL_STATE.md`, `ROADMAP.md`, venv, `conftest.py`, `.gitignore`
- Ends with: "ready. run `/ctci-practice next` to begin."

### `/ctci-practice status`
- Reads state files, summarizes:
  - current block + current in-progress problem
  - overall progress (X/Y problems complete)
  - weakest topic (lowest confidence)
- Suggests next action.

### `/ctci-practice next`
- If nothing is `- [-]`, picks next `- [ ]` using selection rule (§6).
- Subagent scaffolds the problem folder (README, solution.py, test_basic.py, test_full.py, empty HINTS.md).
- Marks `- [ ]` → `- [-]` in ROADMAP.md.
- Tells user: "open `practice/.../README.md`, implement `solution.py`, run tests, call `hint` or `validate` when ready."

### `/ctci-practice hint`
- Identifies current `- [-]` problem.
- Subagent reads: problem README + current `solution.py` + existing `HINTS.md`.
- Writes the next hint (context-aware, calibrated by how many hints already given + how stuck the code looks).
- Appends to `HINTS.md` with timestamp + hint level.
- Returns the hint to the user.

**Hint progression rubric (for the subagent):**
- 0 hints given → **L1 nudge**: a question or observation pointing at the bug/approach
- 1 hint given → **L2 direction**: name the technique + rough sketch
- 2+ hints given → **L3 near-solution**: pseudocode, leave user to translate to Python

### `/ctci-practice validate`
- Identifies current `- [-]` problem.
- Subagent runs `pytest` on both test files, reads `solution.py`, writes verdict:
  - **All tests pass + code clean** → mark `- [x]`, suggest git commit, show strongest/improvable aspects.
  - **Tests pass + code issues** → leave `- [-]`, return review notes, suggest fixes.
  - **Tests fail** → return failing test names + L1 hint on which test and why.
- Never reveals the reference solution (that's `solve`'s job).

### `/ctci-practice solve`
- Confirms: "Are you sure? This reveals the reference solution and marks the problem as studied-not-solved."
- Subagent generates `SOLUTION.md` with reference implementation + explanation (mermaid if user pref is mermaid).
- Marks problem `- [x] (solved-by-reveal)` in ROADMAP — distinguishes from self-solved.

### `/ctci-practice explain <concept>`
- Subagent generates `explanations/<concept>.md`.
- Depth modulated by user's confidence in the related topic + explicit prefs ("I own the book" → terse; otherwise full walkthrough).
- Uses mermaid if `SKILL_STATE.md` says mermaid.

### `/ctci-practice cheatsheet <topic>`
- Subagent generates dense one-pager at `practice/block_NN_<topic>/CHEATSHEET.md` (code templates > prose).

### `/ctci-practice rate <topic> <1-5>`
- Updates confidence score in `SKILL_STATE.md`.
- Recomputes next-problem priority.

### `/ctci-practice replan [hours-remaining]`
- Given current state + time left, proposes adjusted roadmap.
- Can cut blocks, collapse topics, or generate cheat-sheet artifacts instead of more problems (cram-mode pivot).

### `/ctci-practice resume`
- Reads all state files.
- Reports: "Last session ended at block2 p2 in progress. Here's where you were: [summary]. Want to continue, or switch topic?"
- No file changes — just re-orients.

---

## 5. Onboarding flow (conversation spec)

Questions, in order. Skill asks **one at a time**; each answer conditions the next.

1. **Purpose?** interview prep / DS&A foundations / competitive programming / general refresh
2. **Language?** Python / Java / JS / … (MVP: Python only; others show "coming soon")
3. **Experience?** first time doing problem-solving / some LeetCode-style practice / regular practice
4. **Current level per topic:** user self-rates each of [arrays_strings, linked_lists, stacks_queues, trees_graphs, dp, sorting_searching, language_proficiency] on 1–5. Skill shows a one-line description of each topic to anchor the rating.
5. **Target date?** (if interview prep) → drives total block count and block length.
6. **Session length preference?** 30 / 60 / 90 min blocks.
7. **Language skill focus?** yes/no → if yes, generate language-specific drills alongside DS&A.
8. **Preferences confirmed:** defaults applied; user can override ("use mermaid", "skip basic explanations", "iterative over recursive").

End of onboarding → skill writes `SKILL_STATE.md` + `ROADMAP.md` (tailored to available time + confidence) + creates venv + installs pytest + creates `conftest.py`.

---

## 6. Next-problem selection rule (MVP)

Simplest rule that respects confidence + learning flow:

1. **If a `- [-]` problem exists → finish it first.** (Never surface new work when something's in progress.)
2. **Otherwise pick from the topic with lowest confidence score.** Ties broken by roadmap order.
3. **Within a topic, always go easy → hard.** (Respects book's progression.)
4. **Every 5th problem, surface a `- [x]` problem for a quick self-test review** (poor man's spaced repetition — user can skip).

No ML, no heuristics beyond this. Explainable: skill can always tell the user *why* this problem is next.

---

## 7. Hint mechanics — the critical UX

Hints are **generated on demand, context-aware, and append-only**. This is the single most important interaction to get right.

**Flow when user calls `hint`:**
1. Main thread identifies current problem + reads `HINTS.md` (prior hints).
2. Spawns subagent with: problem README, current `solution.py`, `HINTS.md`, user's confidence score for the topic, user's hint-depth preference.
3. Subagent:
   - Runs tests silently to see current failure state.
   - Reads user's code — identifies specific bug or missing piece.
   - Writes a hint at the appropriate level (see rubric in §4).
   - Appends to `HINTS.md`:
     ```markdown
     ## Hint 1 — 2026-04-13 10:55 — L1 nudge
     <hint content, pointed at THEIR code>
     ```
4. Hint shown to user + saved. User can re-read at any time.

**Invariant:** the skill never shows a hint that's more advanced than the last one. If user asks for another hint, they get L(n+1). No skipping ahead.

---

## 8. Validation mechanics

`validate` has three outcomes:

| Test result | Code review | ROADMAP action | User sees |
|---|---|---|---|
| All pass | Clean | `- [-]` → `- [x]` + suggest commit | "All tests pass, code is clean. Suggest: `git add . && git commit`. Next?" |
| All pass | Has nits | Stay `- [-]` | Specific improvement notes + "fix these, or accept as-is with `/ctci-practice accept`" |
| Any fail | N/A | Stay `- [-]` | Failing test names + L1 hint on one failure |

**Code review rubric** (for the subagent):
- Correctness — matches spec, handles edge cases named in README
- Complexity — meets the target stated in README (if stated)
- Idiomaticity — uses stdlib primitives appropriately (deque, heapq, defaultdict)
- Dead code / unused branches
- Variable naming
- Type hints present where they'd help interview presentation

The reviewer does NOT rewrite code. Only names issues.

---

## 9. Subagent usage (the architectural keystone)

Main thread stays lean: orchestration only. Every generation or review job is delegated.

| Job | Subagent input | Subagent output |
|---|---|---|
| Scaffold problem | topic + difficulty + user prefs | README, solution.py, test_basic, test_full, empty HINTS |
| Give hint | problem files + user's code + prior hints + user prefs | one hint, appended to HINTS.md |
| Validate | problem files + user's code + pytest output | ROADMAP patch + review notes |
| Explain concept | concept + user prefs + confidence | `explanations/<concept>.md` |
| Generate cheatsheet | topic + user prefs | CHEATSHEET.md for block |
| Generate reference solution | problem + user prefs | SOLUTION.md |

Why this matters: keeps main-thread context small, which means the skill can run over long sessions without context exhaustion.

---

## 10. Python environment (auto-setup)

On `start`, the skill:
1. Runs `python3 -m venv .venv`
2. Activates, upgrades pip, installs pytest
3. Creates `conftest.py`:
   ```python
   import sys
   from pathlib import Path

   def pytest_collection_modifyitems(config, items):
       for item in items:
           problem_dir = Path(item.fspath).parent
           if str(problem_dir) not in sys.path:
               sys.path.insert(0, str(problem_dir))
   ```
4. Creates `.gitignore` with `.venv/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, editor cruft.
5. Verifies: `pytest --version` — surfaces errors if Python version too old.

Skill assumes Python ≥3.10 (match statement, modern type hints). Falls back gracefully otherwise.

---

## 11. Multi-session continuity

**The skill must work across Claude Code session restarts.**

- On any verb other than `start`, first action is: read `SKILL_STATE.md` + `ROADMAP.md` + last entry of `session_log.md`.
- If state files are missing → prompt user to run `start` or ask if they want to import an existing roadmap.
- On session end (user types "goodbye" / "done for today" / `/ctci-practice pause`): append a session entry to `session_log.md` with what was done + what's next.

No hidden state. A user can delete and re-clone the project dir, and if they preserve the three markdown files, everything resumes correctly.

---

## 12. Explicit NON_GOALS (v1 does NOT have these)

- ❌ Automatic pattern detection from conversation (C-model assessment) — user self-rates only
- ❌ Spaced repetition scheduling with forgetting curves — only the "every 5th problem revisit" heuristic
- ❌ Mermaid kanban board or color-coded progress visualization — checklist only
- ❌ LeetCode / HackerRank integration — links only if user asks
- ❌ Multi-language — Python only; Java/JS/others deferred
- ❌ Voice / mock-interview simulation mode
- ❌ Auto-commit — skill *suggests*, user runs git themselves
- ❌ Preference-learning file that mutates without user confirmation — prefs change only on explicit user statement
- ❌ LLM-generated problems (all problems sourced from CtCI book references the user owns)

Each of these has an argument for inclusion. Each was cut to keep MVP shippable and validate the core loop first.

---

## 13. Success criteria (when is MVP "done"?)

MVP ships when:

1. A new user can run `/ctci-practice start` and reach their first problem in <3 minutes.
2. They can complete the `problem → hint → validate → next` loop without needing to edit state files manually.
3. They can close Claude Code, reopen it 3 days later, run `/ctci-practice resume`, and get correctly re-oriented in <10 seconds.
4. The `validate` verdict correctly distinguishes "clean", "nits", and "failing" on at least 5 test problems across different topics.
5. The `hint` verb produces progressively deeper hints across 3 consecutive calls on the same stuck problem, and each hint references the user's actual code.

If all 5 hold → ship. Then collect real usage data for v1.1.

---

## 14. What v1.1 will probably add (listening for signal in v1 usage)

- Pattern detection (C): watch for repeated bugs across problems, surface as feedback
- Spaced repetition (B): full forgetting-curve scheduling, optional
- Mermaid kanban view (generated on demand, not stored)
- Second language support (Java most likely next, since CtCI is Java-native)
- Commit-point suggestions
- Preference *inference* (currently explicit-only)

Gate: only add these after real users hit specific friction that these features solve.

---

## 15. Risks retained from v0 pre-mortem

From `BRAINSTORM.md`, the risks we must stay vigilant on:

- **Validation theater** — `validate` says clean when it isn't. Mitigation: `test_full.py` is authoritative; code review is advisory. Tests can't lie.
- **Over-engineering creep** — every v1.1 candidate in §14 adds complexity. Keep saying no until real usage pressure justifies.
- **Roadmap divergence** — AI rewrites corrupt it. Mitigation: roadmap patches are always diff-style (find + replace of a specific checkbox line), never wholesale rewrites. Audit every patch in subagent prompts.
