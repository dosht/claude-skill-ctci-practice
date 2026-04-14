# Changelog

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project uses [semver](https://semver.org/).

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
