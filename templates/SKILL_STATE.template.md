# Skill State — ctci-practice

> This file is written and read by the `ctci-practice` skill. Edit with care — all fields are structured. The skill reads this on every verb other than `start`.

## Profile
- **Purpose:** {{purpose}}
- **Language:** {{language}}
- **Experience level:** {{experience_level}}
- **Created:** {{created_date}}

## Target
- **Mode:** {{target_mode}}  <!-- "interview_date" | "weekly_hours" | "open_ended" -->
- **Value:** {{target_value}} <!-- date string or hours/week or null -->

## Scope
- **Topics included:** {{selected_topics}}  <!-- comma-separated slugs -->

## Preferences
- **Hint depth default:** L{{hint_level_default}} ({{hint_level_label}})
- **Explanation style:** {{explanation_style}}  <!-- "terse" | "full" -->
- **Diagrams:** {{diagrams_style}}  <!-- "mermaid" | "ascii" | "none" -->
- **Solution style:** {{solution_style}}  <!-- "iterative_preferred" | "recursive_preferred" | "no_preference" -->

## Runtime
- **Python version detected:** {{python_version}}
- **Venv path:** {{venv_path}}
- **Pytest version:** {{pytest_version}}

## Notes
Preferences are updated only when the user explicitly states a preference.
The skill never infers preferences silently.
