"""Auto-injected by ctci-practice skill.

Adds each per-problem directory to sys.path so test files can `import solution`
from within the problem folder without package boilerplate.
"""
import sys
from pathlib import Path


def pytest_collection_modifyitems(config, items):
    for item in items:
        problem_dir = Path(item.fspath).parent
        if str(problem_dir) not in sys.path:
            sys.path.insert(0, str(problem_dir))
