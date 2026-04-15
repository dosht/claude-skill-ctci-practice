# ctci-practice — a Claude Code skill for Cracking the Coding Interview

An AI-guided practice companion for working through *Cracking the Coding Interview, 6th Edition*. Adaptive roadmap anchored to the book's chapter order, just-in-time problem scaffolding, progressive hints that are context-aware against your actual code, automated validation, and full resumability across Claude Code sessions.

**Scope:** 133 problems across 11 chapters. Python-first environment (venv + pytest auto-scaffolded); other languages get the roadmap and hint loop but manage their own env.

## Demo

[![Watch the ctci-practice demo on YouTube](https://img.youtube.com/vi/aiNMqhg4q5Q/maxresdefault.jpg)](https://www.youtube.com/watch?v=aiNMqhg4q5Q)

> 2-minute walkthrough: onboarding → roadmap → solving a problem with progressive hints → validation.

---

## Why this exists

Studying CtCI alone leaves you doing the work of a coach — sequencing problems, judging your own solutions, deciding when to peek at hints. This skill is that coach: it picks the next problem based on your weakest topic, scaffolds the folder with a spec + starter + failing tests, gives hints only when you ask (and only as deep as you ask for), and validates via real pytest runs plus a code review. Your progress is plain markdown — editable, git-diffable, never locked in a database.

## Install

### Via `openskills` (recommended)

```bash
npx openskills install dosht/claude-skill-ctci-practice
```

This installs the skill to `~/.claude/skills/ctci-practice/`. Replace with `-g` / `--global` / `--universal` flags to change install location; see `npx openskills install --help`.

### Manual install (symlink, recommended for development)

```bash
git clone https://github.com/dosht/claude-skill-ctci-practice.git ~/src/claude-skill-ctci-practice
ln -s ~/src/claude-skill-ctci-practice ~/.claude/skills/ctci-practice
```

### Manual install (copy)

```bash
git clone https://github.com/dosht/claude-skill-ctci-practice.git /tmp/ctci
mkdir -p ~/.claude/skills/ctci-practice
cp -r /tmp/ctci/* ~/.claude/skills/ctci-practice/
```

### Verify

In a Claude Code session:
- The skill appears in the active skills list as `ctci-practice`
- Run `/ctci-practice start` in an empty directory — it should begin the 6-question onboarding

---

## Quick start

```bash
cd ~/my-ctci-practice   # any empty directory you want to use as your workspace
claude                  # start Claude Code
```

Then in the Claude Code session:

```
> /ctci-practice start
```

Answer the 6 onboarding questions (purpose, language, experience, target, topic coverage, hint default). The skill will:
- create a Python venv + install pytest
- write `ROADMAP.md` with your selected chapters and all problems marked `[ ]`
- write `SKILL_STATE.md` with your profile and preferences
- create `session_log.md`

Then:

```
> /ctci-practice next
```

The skill picks your first problem (lowest-scoring topic, book chapter order, easy-first), scaffolds `practice/block_NN_<topic>/p<N>_<slug>/` with a spec README, failing tests, and a starter `solution.py`, and marks the roadmap line `[-]`.

Implement `solution.py`. Then:

```
> /ctci-practice hint       # if stuck — context-aware L1 nudge, appended to HINTS.md
> /ctci-practice validate   # runs tests + reviews code, marks [x] on clean pass
```

## Verbs

| Verb | What it does |
|---|---|
| `start` | Onboarding + env setup (one time) |
| `status` | Progress summary with computed topic scores |
| `next` | Scaffold the next problem (picks by weakest topic + book order) |
| `hint` | Append the next hint (L1 → L2 → L3) to current problem |
| `validate` | Run tests + code review; mark complete on clean pass |
| `solve` | Reveal reference solution (marks `[x] (solved-by-reveal)`) |
| `explain <concept>` | Generate `explanations/<slug>.md` on any DS&A concept |
| `cheatsheet <topic>` | Generate a dense one-page reference for a topic |
| `replan [hours]` | Adjust roadmap given remaining time budget |
| `resume` | Re-orient at the start of a new session |
| `pause` | Log session summary and end cleanly |
| `accept` | Accept a `PASS_WITH_NITS` and mark complete despite nits |

Plain English also works: "give me a hint", "validate my solution", "what's next?", etc.

## Evaluation model

Topic scores are **computed** from `ROADMAP.md` on every read — not stored, not self-rated:

```
weight(easy) = 1, weight(medium) = 2, weight(hard) = 3
solved_weight([x]) = weight(difficulty)
solved_weight([x] (solved-by-reveal)) = 0.5 × weight(difficulty)

topic_score = Σ solved_weight / Σ weight  (across all problems in the topic)
```

Shown as: `Trees & Graphs — 4/11 solved (28% difficulty-weighted)`.

The `next` verb picks the topic with the lowest score that still has unsolved problems, using CtCI chapter order as tiebreaker.

## State files

Everything the skill knows about your progress lives in three plain markdown files in your workspace:

- `ROADMAP.md` — checklist source of truth (`[ ]` → `[-]` → `[x]`)
- `SKILL_STATE.md` — profile, preferences, runtime info
- `session_log.md` — append-only journal of sessions

Edit them by hand if you want; the skill reads fresh state on every invocation.

## What gets scaffolded per problem

```
practice/block_NN_<topic>/p<N>_<slug>/
├── README.md        # problem spec, I/O contract at TOP
├── solution.py      # starter with TODOs
├── test_basic.py    # examples — iterate here
├── test_full.py     # edge cases + perf — validate "submit" equivalent
├── HINTS.md         # append-only hint log (empty until you ask for one)
└── SOLUTION.md      # written only by the solve verb
```

## Design philosophy

- **Main thread orchestrates, subagents do the heavy lifting.** Keeps your context lean across long multi-session workflows.
- **Tests are authoritative.** Code review can flag nits but can't fail a solution whose tests pass.
- **Hints are progressive and context-aware.** Each hint inspects your actual code and points at the specific gap — not a generic "try BFS".
- **State is plain markdown.** Human-editable, git-diffable, no hidden database.
- **Roadmap edits are diff-style.** Never wholesale rewrites — prevents corruption.
- **Explicit preferences, not inferred.** The skill changes its behavior only when you say so.

See [docs/SKILL_DESIGN.md](docs/SKILL_DESIGN.md) for the full rationale.

## Repository layout

```
claude-skill-ctci-practice/
├── SKILL.md                    # the skill entrypoint
├── references/                 # rubrics read by subagents
│   ├── chapter_map.md          # 133 problems, difficulty-tagged
│   ├── hint_rubric.md          # L1/L2/L3 hint rules
│   ├── review_rubric.md        # validate verdict rules
│   ├── scaffold_template.md    # next-verb file generation rules
│   └── onboarding_flow.md      # start-verb conversation spec
├── templates/                  # skeleton files filled at runtime
│   ├── conftest.py
│   ├── ROADMAP.template.md
│   ├── SKILL_STATE.template.md
│   ├── problem_README.template.md
│   ├── solution.template.py
│   ├── test_basic.template.py
│   └── test_full.template.py
├── docs/
│   └── SKILL_DESIGN.md         # design rationale
├── README.md
├── LICENSE                     # MIT
├── CHANGELOG.md
└── .gitignore
```

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Python ≥ 3.10 (for the `match` statement and modern type hints)

## Contributing

Issues and PRs welcome. Areas of interest for v1.1:

- Second language support (Java is the natural next, since CtCI is Java-native)
- Spaced repetition scheduling
- Automatic pattern detection for assessment
- More rubric cases in `review_rubric.md` (specific interview anti-patterns)

See `CHANGELOG.md` for known v1 gaps.

## License

[MIT](LICENSE) © Mustafa Abdelhamid

## Acknowledgments

- Built against *Cracking the Coding Interview, 6th Edition* by Gayle Laakmann McDowell (book is required; this skill is a practice companion, not a replacement).
- Skill structure informed by Anthropic's [Claude Code skills](https://claude.com/claude-code) conventions.
- Universal install supported via [openskills](https://github.com/numman-ali/openskills).
- The [demo video](https://www.youtube.com/watch?v=aiNMqhg4q5Q) was generated entirely with AI: animation by [Remotion](https://www.remotion.dev) and voiceover by [Cartesia](https://cartesia.ai), both orchestrated through Claude Code skills.
