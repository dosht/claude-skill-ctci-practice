# Review Rubric — for the `validate` subagent

The `validate` subagent reads this rubric when reviewing a user's `solution.py`. Verdict drives the ROADMAP.md state transition.

## Three verdicts

### PASS_CLEAN
All tests pass AND code is interview-quality. Mark `[-]` → `[x]`.

### PASS_WITH_NITS
All tests pass BUT code has issues worth calling out (dead code, wrong complexity, poor naming, missing type hints on public functions). Stay `[-]`. User can:
- fix the nits and re-run `validate`, or
- accept as-is with `/ctci-practice accept` (mark `[x]` despite nits — their call)

### FAIL
At least one test fails. Stay `[-]`. Return failing test names + one L1 hint on the most informative failure.

## Testing is authoritative

Code review CANNOT block a PASS if tests pass AND the issues are only stylistic. Only these issues justify `PASS_WITH_NITS` (not full pass):

1. **Wrong complexity.** If the README states O(n) time and the solution is O(n²), call it out. Example: "README target is O(n), your solution has a nested loop on lines 8–11 making it O(n²)."
2. **Dead code.** Unused variables, unreachable branches, commented-out blocks, unused imports.
3. **Idiomatic gaps that interviewers would call out.** Examples:
   - Manual list reversal instead of `reversed(lst)` or `lst[::-1]`
   - Building a dict with repeated `if key in d: d[key].append(x) else: d[key] = [x]` instead of `defaultdict(list)`
   - `for i in range(len(lst))` when `enumerate` would be cleaner
4. **Missing type hints on public signatures** — only for the target function (`{{function_name}}`), not internal helpers.
5. **Variable naming that hurts readability** — single-letter names outside loop indices, misleading names.

Everything else (extra comments, slightly different structure, preference differences) passes clean.

## What does NOT count as a nit

- Minor style differences that don't affect clarity
- Alternative valid approaches (iterative vs recursive when both are equally readable — unless user pref dictates)
- Extra helpful comments (comments aren't bad; only missing ones for non-obvious logic are)
- Docstrings (encourage them, don't require them)

## Output format (subagent response to main thread)

```markdown
## Verdict: {PASS_CLEAN | PASS_WITH_NITS | FAIL}

### Tests
- basic: {X/Y passing}
- full: {X/Y passing}
- Failing: {list of test names, or "none"}

### Code review
{for PASS_CLEAN: one sentence on strongest aspect}
{for PASS_WITH_NITS: numbered list of specific nits with line numbers}
{for FAIL: skipped — fix tests first}

### Recommendation
{for PASS_CLEAN: "Mark complete. Suggest: git commit -m '{problem_slug} solved'"}
{for PASS_WITH_NITS: "Stay [-]. Fix nits or accept as-is."}
{for FAIL: "Stay [-]. L1 hint: {one pointed nudge at most informative failure}."}

### ROADMAP patch
{exact diff-style patch — which line to find and replace. Example:
find:    - [-] 4.1 `route_between_nodes` | Route Between Nodes | easy
replace: - [x] 4.1 `route_between_nodes` | Route Between Nodes | easy
}
```

## Subagent MUST NOT

- Rewrite the user's code
- Reveal the reference solution
- Apply the ROADMAP patch itself (return it; main thread applies)
- Escalate past L1 hint on a FAIL (user can `/ctci-practice hint` for more)
