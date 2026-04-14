# Changelog

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project uses [semver](https://semver.org/).

## [1.0.1] — 2026-04-14

### Added
- Default / welcome handler for bare `/ctci-practice` invocation. New users see a self-contained guide + verb reference; returning users see a status summary (last session, progress, weakest topic, in-progress problem) with a suggested next action.
- `help` verb — compact reference of all verbs; no state mutation.

### Changed
- All multi-choice prompts now use the `AskUserQuestion` tool (clickable options) instead of typed-number lists or `y/N`. Affects:
  - Onboarding's 6 questions (purpose, language, experience, target, topics, hint depth)
  - The onboarding confirmation prompt
  - Re-onboarding branching (resume / re-run / wipe) + wipe confirmation
  - `solve` reveal confirmation
  - `accept` mark-complete confirmation
  - `replan` apply-changes approval
- Topic coverage question (Q5) now offers preset options (Interview essentials / All / Core algo only / Custom) because `AskUserQuestion` supports ≤4 options; custom mode falls back to conversational typed input.

## [1.0.0] — 2026-04-14

### Added
- Initial release.
- 13 verbs: `start`, `status`, `next`, `hint`, `validate`, `solve`, `explain`, `cheatsheet`, `rate`, `replan`, `resume`, `pause`, `accept`.
- Book-anchored roadmap spanning 133 problems across 11 CtCI chapters.
- Computed topic scoring (weight × solved, not self-rated).
- Progressive hint ladder (L1 nudge → L2 direction → L3 near-solution sketch).
- Subagent-delegated scaffolding, hint, validation, solve, explain, cheatsheet generation.
- Cross-session continuity via plain markdown state files (`ROADMAP.md`, `SKILL_STATE.md`, `session_log.md`).
- Python-only environment scaffold (venv + pytest + `conftest.py`).

### Known v1 gaps (tracked for v1.1)
- No automatic pattern detection (user behavior mining for assessment).
- No spaced repetition scheduling.
- Multi-language support limited to Python for environment scaffold (roadmap + hints work language-agnostically).
- No LeetCode/HackerRank integration.
- No preference inference — preferences must be stated explicitly.
