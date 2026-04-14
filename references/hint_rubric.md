# Hint Rubric — for the `hint` subagent

The `hint` subagent reads this rubric when generating each hint. Hints are progressive, context-aware against the user's actual code, and appended (never replacing prior hints).

## Level definitions

### L1 — Nudge
Observation or question pointing at the specific gap in the user's code. No solution sketch. Should be 1–3 sentences.

**Good L1 examples:**
- "Look at line 12 — you break out of the loop before checking the last element. What does your loop miss if the target is at index `n-1`?"
- "Your `parse()` function on line 8 doesn't appear in the spec. Re-read the I/O contract — what should each dict value be?"
- "Notice that you add to `visited` *after* `if node == target`. What happens when `src == dst`?"

**Bad L1 examples:**
- ❌ "Try BFS" (not pointed at their code)
- ❌ "Use a hash map" (not a nudge, it's a near-solution)
- ❌ "Your code is wrong" (not actionable)

### L2 — Direction
Name the technique and rough approach. Explain *why* it applies. Still don't write code.

**Good L2 examples:**
- "This is a classic BFS reachability problem. The idea: maintain a queue of nodes to visit and a visited set to avoid cycles. BFS (not DFS) is slightly preferred because — in the stretch case — you'd want shortest path."
- "Two pointers work here: one slow, one fast. The slow pointer advances once per iteration, the fast advances twice. When the fast hits None, slow is at the midpoint. Why? At every step, fast covers 2× slow's distance."

### L3 — Near-solution sketch
Pseudocode or structural outline. User still has to translate to Python, handle edge cases, and pick the right data structures. Cap at L3 — don't give the full solution.

**Good L3 examples:**
```
# BFS scaffold:
# queue = deque([src])
# visited = {src}
# while queue:
#     node = queue.popleft()
#     if node == target: return True
#     for neighbor in graph.get(node, []):
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)
# return False
```

## Selection rule

When invoked with `prior_hints_count = N`, emit the hint at level `min(N+1, 3)`.

- 0 prior → L1
- 1 prior → L2
- 2 prior → L3
- 3+ prior → still L3 (ask: "want to see the full reference solution via `/ctci-practice solve`? or stay stuck for another round?")

Never emit L2 when L1 wasn't already given, and so on. The user earned their way down the ladder.

## Context sources (in priority order)

1. **The user's `solution.py`** — this is what you critique. Every hint should reference specific lines/constructs in their code.
2. **Test failures** — run the tests silently. Which specific test fails, and what does it assert? The hint should target that failure.
3. **Prior hints (`HINTS.md`)** — don't repeat. Don't contradict. Build on.
4. **Problem `README.md`** — know the spec.
5. **User preferences from `SKILL_STATE.md`** — if `solution_style = iterative_preferred`, don't suggest recursion.

## Formatting rules

Each hint appended to `HINTS.md` uses this format:

```markdown
## Hint {n} — {YYYY-MM-DD HH:MM} — L{level}
{hint body}
```

Separate hints with `---` (horizontal rule).

## What the hint must NOT do

- Write the full solution, even in comments
- Rewrite the user's code
- Contradict a prior hint without explicitly calling that out ("Correcting hint 1 — I was wrong about X, here's why...")
- Give away the answer in L1 or L2
- Be generic ("think about edge cases") — always cite the user's specific code
