# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is a **courseware asset repo**, not a software project. It holds a 60-day "Python zero-base → AI-ready engineer" teaching plan for adult beginners / cross-track learners. The shipping product is **structured lesson directories** — slides, demo scripts, exercise files, and teacher notes — not an installable application.

- **60 lesson directories** (`lesson01/` ~ `lesson06/`) = daily 6-hour classes
- **~500+ exercise files** (in-class + homework) across the 60 lessons
- **4 capability targets**: Machine Learning, LLM Fine-tuning, Web Scraping, AI Application Development
- **3 medium weekly projects** (`weekly_projects/week01_shopping_cart/`, `week02_library_manager/`, `week03_book_manager_oop/`)
- Git remote: `chaoshou-coder/Lec.Python`. Repo root **is** the teaching plan; there is no parent app.

## How to continue in a new session

1. Read the top of `summary.md` → confirm current version and module scope.
2. Pick the highest-priority unfinished item(e.g. exercise gaps, slide depth).
3. Write/change files **following the hard rules below**.
4. After changes: commit and push to main, optionally make a timestamp backup(see Commands).
5. Don't do what the "Out of scope" section forbids.

## Common commands & operations

This repo has no build system, linter, or test runner. Verification is by inspection and by running demo scripts.

```bash
# Run a single demo script to verify it executes
python3 lessonXX/demo/<file>.py

# Create a timestamped backup before any major edit
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p .versions
cp -r lesson*/ weekly_projects/ .versions/lessons-v${VERSION}-${TIMESTAMP}/

# Check git status before pushing
git status
git diff --stat
```

The most frequent operation is **authoring a new exercise file** (`practiceNN.py` / `taskNN.py`).

## Architecture (the big picture)

### Directory layout

```
Lec.Python/
├── CLAUDE.md / README.md / summary.md / references.md / PREREQUISITES.md
├── lesson01/ ~ lesson06/                  ← 60 standard lesson dirs = SHIPPING CORE
│   ├── README.md / slides.md / teacher_notes.md
│   ├── demo/          ← instructor demo scripts
│   ├── in_class/      ← practice01.py ~ practiceNN.py (当堂练)
│   ├── homework/      ← task01.py ~ taskNN.py (课后作业/选做)
│   ├── mini_project/  ← small project every 2–3 days
│   └── assets/        ← materials
├── weekly_projects/                       ← 3 medium projects = SHIPPING CORE
│   ├── week01_shopping_cart/  week02_library_manager/  week03_book_manager_oop/
├── dev/                 ← DEV convenience + ephemeral (not shipping)
│   ├── plans/           ← backup of the Claude plan corpus
│   ├── agent-artifacts/ ← intermediate agent output (safe to delete)
│   └── module0-mapping.md ← new-day → old-lesson → exercise mapping
└── .versions/           ← LOCAL timestamp backups, gitignored
```

### Six modules (pedagogical spine)

```
Module 0 (Day 1-17)   Python Core + Data Foundations
Module 1 (Day 18-25)  Machine Learning (scikit-learn)
Module 2 (Day 26-31)  Deep Learning (PyTorch)
Module 3 (Day 32-36)  NLP & Transformers
Module 4 (Day 37-43)  LLM Fine-tuning (Hugging Face + LoRA)
Module 5 (Day 44-50)  Web Scraping
Module 6 (Day 51-60)  AI Application Development (RAG/Agent/Deploy)
```

- **Stage review days**: Day 10, 17, 40, 60(期末答辩).
- **Emphasis**: AI Application (10d) > Web Scraping (7d) > LLM (7d) > ML (8d) > DL (6d).
- **Terminal deliverable**: Student-chosen capstone (4 directions: AI App / LLM Fine-tuning / Data+Scraping / ML Engineering).

### The medium weekly projects

- Week01: console shopping cart (Day01–07 knowledge)
- Week02: library manager v1
- Week03: book manager v2 — the OOP capstone

Each ships a `README.md` with a验收 checklist.

## Hard rules when writing exercises

File naming: `lessonXX/in_class/practiceNN.py` or `lessonXX/homework/taskNN.py` — `NN` is zero-filled. Every exercise file **must** contain this exact anatomy:

```python
"""
[难度: ⭐~⭐⭐⭐⭐⭐]
[所属知识点: xxx]
[预计完成时间: N 分钟]

题目描述(中文,场景化,可独立运行)

示例:
    >>> 调用方式 / 示例输入 → 示例输出
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1
    # 测试 2
    pass
```

Constraints:
- All strings in Chinese; **≤ 100 chars per line**.
- Student section uses `pass` as placeholder (or partial scaffolding) — **no syntax the student hasn't been taught yet**.
- Test section has **≥ 2 cases** covering boundaries (empty input / zero / negative / single element).
- Each exercise is tagged **当堂练**(in-class) or **选做**(optional) in the lesson's README.md.

### Per-Day syntax boundary (the rule most often broken)

| Days | Forbidden |
|---|---|
| Day01–10 | **`def`** |
| Day11–17 | — (functions allowed, no external libs beyond NumPy/Pandas) |
| Day18–25 | — (scikit-learn allowed, no PyTorch) |
| Day26–31 | — (PyTorch allowed, no HF/transformers) |
| Day32–43 | — (Hugging Face allowed, no LangChain) |
| Day44–60 | — (all stdlib + data/AI libs allowed) |

An exercise authored for Day04 must not contain `def`; a Day08 exercise must not contain `class`. Check the target lesson's module in `summary.md` before writing.

## Version control scheme

The repo uses **git + timestamp backup** for versioning:

```bash
# 1. Before any major edit, make a timestamp backup(see Common commands)
# 2. git add / commit / push for versioned releases
```

Current version: **v2.0.0** (2026-07-07) — 60 days / 6 modules / 4 capability targets.

## Out of scope (don't do)

- **Don't delete exercise files** — move to 选做(optional), never delete.
- **Don't introduce third-party packages** without checking against the per-Day boundary table (stdlib + NumPy/Pandas/sklearn/PyTorch/HF only).
- **Don't reorder / re-number lesson directories** — the number in `lessonXX` is the Day sequence.
- **Don't front-load syntax the student hasn't reached** — see the per-Day boundary table.
- **Don't put hidden files in lesson directories** (`.DS_Store` is an OS artifact, exempt).

## Key file index

| I need… | Read this |
|---|---|
| 60-day schedule + capability targets | `summary.md` |
| Teacher daily flow + grading breakdown | `README.md` |
| Non-Python prerequisites (math/CS) | `PREREQUISITES.md` |
| Per-lesson topic distribution | `lessonXX/README.md` |
| Market course comparison / exercise pool | `references.md` |
| Canonical exercise-file example | `lesson01/in_class/practice01.py` |
| New-day → old-lesson exercise mapping | `dev/module0-mapping.md` |
