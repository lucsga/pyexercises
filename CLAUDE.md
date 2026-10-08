# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The student-facing template repository for a Python Programming course (SKEMA, MSc Digital Marketing). Students copy it via "Use this template" and work in Codespaces. The audience is marketers learning to program, not developers. Exercise briefs and final-project datasets live on K2 (the course page), not here.

- `examples/<topic>/*.py`: small, commented, runnable scripts per course topic (strings, numbers, operators, conditions, loops, lists, dictionaries, functions, io, files, libraries, interfaces). Each ends with a `# What to remember` block; keep that convention when adding or editing examples.
- `examples/files/sample_campaigns.csv`: deliberately messy (semicolon separator, decimal comma, unnamed empty column, a row with no impressions, a zero-conversion campaign). Don't "clean" it; see `examples/README_files_note.md`.
- `exercices/<n.m>_<name>.py`: the student's graded work, one file per exercise. Each opens with a docstring brief (what the program must do, four "ANSWER THESE FIRST" questions to answer in comments, "what the AI cannot know", "check it yourself") followed by `# 1. In: / 2. Process: / 3. Out:` comment stubs and a `# Your code below` marker. The comments and decisions are the student's own deliverable: do not fill in the answers or write the full solution, only give hints within the tutor rules below. Note the folder is spelled `exercices` (French), whereas `.gitignore` excludes `exercises/` (the K2 briefs); don't conflate them.
- `bonus/`: optional material (matplotlib/numpy), not graded.
- `tutor.py`: the course AI tutor (see below).

## Commands

- Run an example: `python examples/lists/indexing.py`
- Tutor: `python tutor.py --check` (test setup), `python tutor.py` (interactive), `python tutor.py "question"`, `python tutor.py --models`
- Dependencies: `pip install -r requirements.txt` (matplotlib, numpy, gradio, streamlit). `cowsay` is intentionally absent: students install it by hand in session 2.
- CI (`.github/workflows/python-app.yml`): Python 3.10, flake8 (hard-fail only on E9/F63/F7/F82; other warnings are non-blocking, max line length 127), then `pytest`. There are currently no tests. The devcontainer uses Python 3.12.

## tutor.py architecture

Single stdlib-only file (no pip dependencies, by design; uses `urllib`). It calls any OpenAI-compatible endpoint (default Mistral, configured via `.env`: `MISTRAL_API_KEY`, or `TUTOR_BASE_URL`/`TUTOR_TOKEN`/`TUTOR_MODEL`). The key design principle is that restrictions are enforced **in code on the model's output**, not only in the prompt:

- `scope_of` / `strip_scope`: the model must emit a `SCOPE: PYTHON|OFF` first line; `OFF` yields a canned refusal.
- `leash`: truncates code blocks at the second `def`/`class`, at an `if __name__` guard, or past `MAX_CODE_LINES` (22).
- `forbidden_tokens` / `redact`: anything data-like the student pasted (CSV fields, long numbers) is blanked from the answer so the tutor can't hand their own data back.
- `log_exchange`: every exchange is appended to `CONVERSATION.md`, a graded deliverable.

If you change the rules (line budget, scope, redaction), keep `tutor.py`, `.github/copilot-instructions.md` and the README's tutor section consistent: the same rules are stated in all three.

## Constraints to respect

- `.github/copilot-instructions.md` defines how Copilot answers students (no full programs, max one function and 22 lines, never echo pasted data). It is course policy, not generic advice.
- `.gitignore` deliberately excludes teacher material (`_teacher/`, `_correction/`, `*ANSWER_KEY*`, `*CORRIGE*`, solution/generator files, decks, `COURSE_FRAMEWORK*`, `SESSION_PLAN*`). Never add solutions or course-planning material to this repository, since students get a copy of it.
- Keep examples beginner-level and in the course's plain, comment-heavy style.
