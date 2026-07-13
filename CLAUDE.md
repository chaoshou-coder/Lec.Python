# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is a **courseware asset repo**, not a software project. It holds a 60-day "Python zero-base → AI-ready engineer" teaching plan for adult beginners / cross-track learners. The shipping product is **structured lesson directories** — slides, demo scripts, exercise files, and teacher notes — not an installable application.

- **60 lesson directories** (`course/lesson01/` ~ `course/lesson60/`) = daily 6-hour classes
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
python3 course/lessonXX/demo/<file>.py

# Create a timestamped backup before any major edit
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p .versions
cp -r course/lesson*/ weekly_projects/ .versions/lessons-v${VERSION}-${TIMESTAMP}/

# Check git status before pushing
git status
git diff --stat
```

The most frequent operation is **authoring a new exercise file** (`practiceNN.py` / `taskNN.py`).

## Architecture (the big picture)

### Directory layout

```
Lec.Python/
├── CLAUDE.md / README.md / summary.md / references.md / PREREQUISITES.md / USER_GUIDE.md
├── course/lesson01/ ~ course/lesson60/            ← 60 standard lesson dirs = SHIPPING CORE
│   ├── README.md / slides.md / teacher_notes.md
│   ├── demo/          ← instructor demo scripts
│   ├── in_class/      ← practice01.py ~ practiceNN.py (当堂练)
│   ├── homework/      ← task01.py ~ taskNN.py (课后作业/选做)
│   ├── mini_project/  ← small project every 2–3 days
│   └── assets/        ← materials
├── student-notebooks/   ← Day 1-17 学生版 Jupyter Notebook(自学用, ~900 cells, h3+h4, 执行跟踪, 趁热打铁)
├── weekly_projects/                       ← 3 medium projects = SHIPPING CORE
│   ├── week01_shopping_cart/  week02_library_manager/  week03_book_manager_oop/
├── dev/                 ← DEV convenience + ephemeral (not shipping)
│   ├── plans/           ← backup of the Claude plan corpus
│   ├── agent-artifacts/ ← intermediate agent output (safe to delete)
│   ├── skills/          ← 课程开发经验沉淀(排版规范/知识地图/学习顺序/试题集)
│   ├── learning-gaps.md ← 学习断层修复指南(6 个 P0 断层的修复建议)
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

File naming: `course/lessonXX/in_class/practiceNN.py` or `course/lessonXX/homework/taskNN.py` — `NN` is zero-filled. Every exercise file **must** contain this exact anatomy:

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

### Heading hierarchy (h3/h4 only)

```
✅ ### Day 08 · OOP           ← h3(唯一天标题)
✅ #### __init__ 构造函数     ← h4(小节标题)
✅ **逐行解剖**                ← 正文加粗(不是标题)
❌ # Day 08 · OOP             ← H1 字体 ~28px,太大
❌ ## 第一讲                  ← H2 字体 ~22px,太大
❌ ### 知识点                 ← 嵌套标题,页面碎
```

**Why:** H1/H2 字体太大,页面拥挤;多层标题让阅读低效。

**Rules:**
- `###` 只用一次(当天标题)
- `####` 用于每个知识点的标题
- 不再往下嵌套(不用 `#####`)
- 解释用 **加粗** + 正文,不额外加标题层级

### Loop structure per knowledge point (趁热打铁)

Each complete knowledge point = a mini cycle:

1. **Concept md:** pain point(why) → analogy(life example) → explanation(what)
2. **Example code:** per-line Chinese comments + execution trace(`# --- 执行过程 ---`)
3. **Line-by-line breakdown md:** explain syntax and parameters
4. **Socratic guidance md:** guiding questions(not direct answers)
5. **Student code area:** `pass` placeholder
6. **Reference answer:** complete runnable code + comments

### Execution trace

Every code cell must contain an execution trace comment(starting with `# --- 执行过程 ---`).

**Format:**
```python
# --- 执行过程 ---
# 第 X 行 code:
#   ① what happens first
#   ② what happens next
```

**Why:** Students run code and only see the final output, don't know what happened in between.

### Socratic guidance

Every exercise must have guiding questions before the answer(leading students to think, not giving answers directly).

**Example:**
```
> Ask yourself:
> - Which concept from today does this exercise need?
> - What does "XX" in the problem correspond to?
> - If it errors, what to check?
```

## Version control scheme

The repo uses **git + timestamp backup** for versioning:

```bash
# 1. Before any major edit, make a timestamp backup(see Common commands)
# 2. git add / commit / push for versioned releases
```

Current version: **v2.2.0** (2026-07-09) — 63 days / 6 modules / h3+h4 headings / execution trace / 趁热打铁 loop / OOP 3 天(封装/继承/抽象).

## Out of scope (don't do)

- **Don't delete exercise files** — move to 选做(optional), never delete.
- **Don't introduce third-party packages** without checking against the per-Day boundary table (stdlib + NumPy/Pandas/sklearn/PyTorch/HF only).
- **Don't reorder / re-number lesson directories** — the number in `lessonXX` is the Day sequence.
- **Don't front-load syntax the student hasn't reached** — see the per-Day boundary table.
- **Don't put hidden files in lesson directories** (`.DS_Store` is an OS artifact, exempt).

## Key file index

| I need… | Read this |
|---|---|
| 63-day schedule + capability targets | `summary.md` |
| Teacher daily flow + grading breakdown | `README.md` |
| Complete user guide(for teachers / students / self-learners) | `USER_GUIDE.md` |
| Non-Python prerequisites (math/CS) | `PREREQUISITES.md` |
| Per-lesson topic distribution | `course/lessonXX/README.md` |
| Market course comparison / exercise pool | `references.md` |
| Canonical exercise-file example | `course/lesson01/in_class/practice01.py` |
| Day 1-17 学生版 Jupyter Notebook(h3+h4 / 执行跟踪 / 趁热打铁) | `student-notebooks/` |
| Jupyter 排版规范(gold standard = Day 08 v6 + 7 踩过的坑) | `dev/skills/05_Jupyter_Notebook_排版规范.md` |
| 学习断层修复指南(6 个 P0 断层的修复建议) | `dev/learning-gaps.md` |
| 知识地图推理 / 学习顺序编排 / 试题集组织 | `dev/skills/01-04_*.md` |
| New-day → old-lesson exercise mapping | `dev/module0-mapping.md` |
