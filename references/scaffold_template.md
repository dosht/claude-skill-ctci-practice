# Scaffold Rubric — for the `next`/scaffold subagent

The scaffold subagent creates a new problem folder when the user invokes `/ctci-practice next`. This rubric defines what to generate and how.

## Inputs received

- `chapter_number`, `chapter_name`, `problem_number` (e.g., "4.1"), `problem_slug`, `problem_title`, `difficulty`
- `topic_slug`
- `user_prefs` from `SKILL_STATE.md` (explanation_style, diagrams, solution_style, language)
- Path to `practice/block_NN_<topic>/p<N>_<slug>/` — already created as empty dir by main thread

## Files to generate

1. `README.md` — problem statement
2. `solution.py` — starter with TODOs
3. `test_basic.py` — example cases
4. `test_full.py` — edge cases + perf
5. `HINTS.md` — empty (header only, ready for first hint append)

## README.md rules

**Format** follows `templates/problem_README.template.md`. The I/O contract MUST be at the top — this was validated today as critical for preventing spec-misreading bugs.

**Source the problem statement** from your knowledge of the CtCI book, but DO NOT copy verbatim — paraphrase to avoid copyright issues. The spirit of the problem, not the exact wording.

**Examples block:** 2–3 concrete input/output pairs. Include an edge case as one of them.

**Edge cases list:** bullet list of things to think about:
- empty input
- single element
- all-same elements
- largest meaningful input (connect to complexity target)
- whatever is specific to the problem

**Complexity target:** if CtCI book gives one, use it. Otherwise state the best known.

## solution.py rules

- `from __future__ import annotations` at top (cheap, helps older Python compatibility)
- Module docstring with I/O contract repeated (belt-and-suspenders — user may open this file directly)
- Function signature with type hints
- Function docstring — 1 line summary
- Body: `raise NotImplementedError` with a `# TODO: implement` comment
- If the problem benefits from a helper class (e.g. linked list, tree node), include its definition above the function with standard structure. Don't over-engineer.

## test_basic.py rules

- Import: `from solution import {function_name}`
- 3–5 test functions covering the README examples
- Use `assert` directly (pytest-style) — no need for `unittest`
- Name tests descriptively: `test_example_from_readme()`, `test_two_items()`, etc.
- NO edge cases here — those go in test_full.py. These are the "iterate while developing" cases.

## test_full.py rules

- Import: `from solution import {function_name}` and `import pytest`
- 6–12 test functions covering:
  - Edge cases from the README's edge case list
  - Boundary conditions (empty, single, large)
  - Stress/perf test if the complexity target matters — mark with `@pytest.mark.timeout(N)` OR use a time assertion if timeout plugin isn't installed. Simple form:
    ```python
    def test_large_input_runs_fast():
        import time
        big_input = ...  # construct size matching target
        t0 = time.perf_counter()
        result = function_name(big_input)
        elapsed = time.perf_counter() - t0
        assert elapsed < 1.0  # or whatever is realistic
        assert result == expected
    ```
  - For problems with non-unique correct answers (e.g. topo sort), include a **validator helper** in the test file — don't compare to a specific ordering.

## HINTS.md rules

Start with just:
```markdown
# Hints — {{problem_number}} {{problem_title}}

> Hints are appended by `/ctci-practice hint`. Progressive L1 → L2 → L3.
> If you want to avoid spoilers, stop reading here.

---

```

Empty body — no hint until user asks.

## Preferences applied

- If `diagrams_style = mermaid`: README may include a small mermaid diagram for problems where visual aid helps (graph problems, tree structures). Skip for array/string problems.
- If `solution_style = iterative_preferred`: solution.py starter docstring can hint "iterative solution expected" — but user can choose.
- If `explanation_style = terse` (user owns book): README is briefer — skip verbose problem motivation, assume user knows the chapter intro.
- If `explanation_style = full`: README includes a motivation paragraph and background concepts relevant to the problem.

## What the scaffold subagent MUST NOT do

- Implement the solution
- Write hints to HINTS.md (that's the hint subagent's job)
- Write SOLUTION.md (that's the solve subagent's job)
- Modify ROADMAP.md (main thread does that)
- Fetch or scrape book content from the web
