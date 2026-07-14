# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What this repo is

This is a **courseware asset repo**, not a software project. It holds a 59-day "Python zero-base → AI-ready engineer" teaching plan for adult beginners / cross-track learners. The shipping product is **structured lesson directories** — slides, demo scripts, exercise files, and teacher notes — not an installable application.

**CLAUDE.md 的双重身份**:它既是 Claude Code 在本仓库的工作指南(工具),也是课程设计方法论的固化产物(项目交付物)。教案迭代一次,这里的规则就沉淀一次——它和 `course/`、`dev/skills/` 一样,是项目的一等公民,而非对方的附属工具。修改 CLAUDE.md 的流程与修改教案相同:评审 → commit → push → 可选 timestamp backup。

- **60 lesson directories** (`course/lesson01/` ~ `course/lesson60/`) = daily 6-hour classes
- **~513 exercise files** (342 `practice*.py` + 171 `task*.py`) across the 60 lessons
- **4 capability targets**: Machine Learning, LLM Fine-tuning, Web Scraping, AI Application Development
- **3 medium weekly projects** (`weekly_projects/week01_shopping_cart/`, `week02_library_manager/`, `week03_ecommerce_order_v2/`)
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
# Run a single demo / exercise script to verify it executes
python3 course/lessonXX/demo/<file>.py
python3 course/lessonXX/in_class/practice01.py

# Batch-verify every exercise in a lesson (syntax check only)
for f in course/lessonXX/in_class/*.py; do python3 -m py_compile "$f" && echo "OK $f"; done

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
├── student-notebooks/   ← Day 1-19 学生版 Jupyter Notebook(自学用, ~900 cells, h3+h4, 执行跟踪, 趁热打铁)
├── weekly_projects/                       ← 3 medium projects = SHIPPING CORE
│   ├── week01_shopping_cart/  week02_library_manager/  week03_ecommerce_order_v2/
├── dev/                 ← DEV convenience + ephemeral (not shipping)
│   ├── plans/           ← backup of the Claude plan corpus
│   ├── agent-artifacts/ ← intermediate agent output (safe to delete)
│   ├── skills/          ← 课程开发经验沉淀(排版规范/知识地图/学习顺序/试题集/OOP教学设计/通用教学法)
│   ├── learning-gaps.md ← 学习断层修复指南(6 个 P0 断层的修复建议)
│   └── module0-mapping.md ← new-day → old-lesson → exercise mapping
└── .versions/           ← LOCAL timestamp backups, gitignored
```

### Six modules (pedagogical spine)

```
Module 0 (Day 1-16)   Python Core + Data Foundations
Module 1 (Day 17-23)  Machine Learning (scikit-learn)
Module 2 (Day 24-29)  Deep Learning (PyTorch)
Module 3 (Day 30-34)  NLP & Transformers
Module 4 (Day 35-41)  LLM Fine-tuning (Hugging Face + LoRA)
Module 5 (Day 42-48)  Web Scraping
Module 6 (Day 49-58)  AI Application Development (RAG/Agent/Deploy)
```

- **Stage review days**: Day 10, 17, 39, 59(期末答辩).
- **Emphasis**: AI Application (10d) > Web Scraping (7d) > LLM (7d) > ML (8d) > DL (6d).
- **Terminal deliverable**: Student-chosen capstone (4 directions: AI App / LLM Fine-tuning / Data+Scraping / ML Engineering).

### Three-layer project system

Exercises are reinforced by a cumulative project ladder:

| Layer | Cadence | Example | Goal |
|---|---|---|---|
| **Mini Project** | every 2–3 days | Student 类 / 矩阵运算 | 单点综合,当堂完成 |
| **Weekly Project** | 3 total | 购物车 v1 / 图书 v1 / 电商订单 v2(OOP L1-L4) | 模块综合,周五交付 |
| **Capstone** | Day 56-58 | 四选一(AI/LLM/爬虫/ML) | 跨模块,产品级 |

Each weekly project ships a `README.md` with a验收 checklist.

### OOP 4-day ladder (Day 05–08)

OOP 占 4 天,按 L1–L4 认知递进,详见 `dev/skills/06_OOP_教学方案设计.md`:

| Day | Level | 主题 | 关键新增 | 门控任务 |
|---|---|---|---|---|
| 05 | L1 | 封装 | `class`/`__init__`/`self`/`@property`/`__str__`/`类属性` | `BankAccount`(property 校验余额) |
| 06 | L2 | 继承 | 单继承/`super()`/方法重写/MRO/`isinstance` | `Animal` 继承体系 + `Employee→Manager/Sales` |
| 07 | L3 | 多态+契约 | 鸭子类型/`abc.ABC`/`@abstractmethod`/接口 | `Payment(abc)` 支付系统(NCDL 驱动) |
| 08 | L4 | 组合+Pythonic | 组合优于继承/`__add__`/`__len__`/`__iter__`/`__eq__` | `ShoppingCart.__add__` + `Order` 聚合 |

**业务叙事锚点**:电商订单系统贯穿 4 天,从"散落的 dict"演进到"可合并的购物车"。
**语法点独立样本**:MRO/`isinstance` 反模式等无法嵌入电商系统的语法点,用最小示例单独演示。

### Lesson directory ↔ Day mapping (important)

The `lessonXX` directory number **is** the Day sequence — never renumber. But the *content* inside may still reflect an older 60-day layout. When in doubt:

- Read `course/lessonXX/slides.md` first line → confirms the Day title.
- Read `course/lessonXX/README.md` → confirms the topic table.
- Cross-check against `summary.md` "59 天总进度" table for the canonical Day → topic mapping.
- For Module 0 (Day 1-16), `dev/module0-mapping.md` maps new Day → old lesson → exercise source.

**OOP 4 天目录状态**(2026-07-14 重构后):

| Day | lesson 目录 | 状态 |
|---|---|---|
| 05 | `lesson05/` | ✅ 新 OOP L1 骨架(README+slides+TODO 占位) |
| 06 | `lesson06/` | ✅ 新 OOP L2 骨架 |
| 07 | `lesson07/` | ✅ 新 OOP L3 骨架(NCDL 核心落地) |
| 08 | `lesson08/` | ✅ 新 OOP L4 骨架 |

旧内容已归档到 `.versions/old-lessons-archive/lesson{05-08}_old_*/`。

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
| Day01 | **`def`** and **`class`** |
| Day02–04 | **`class`** (def allowed) |
| Day05–17 | — (all core Python allowed; no libs beyond NumPy/Pandas until Day 10) |
| Day18–25 | — (scikit-learn allowed, no PyTorch) |
| Day26–31 | — (PyTorch allowed, no HF/transformers) |
| Day32–43 | — (Hugging Face allowed, no LangChain) |
| Day44–60 | — (all stdlib + data/AI libs allowed) |

**Key corrections vs the old table**: Day02 teaches `def`(函数入门) — so `def` is only forbidden on Day01. Day05 starts OOP 封装 — so `class` is allowed from Day05 onward. An exercise authored for Day04 must not contain `class`; a Day02 exercise must not contain `def`. Always cross-check the target lesson's topic in `summary.md` before writing.

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

### Universal teaching methods (全项目通用教学法)

以下方法论从 OOP 设计中提炼,推广到全 60 天课程。详见 `dev/skills/06_OOP_教学方案设计.md`。

**1. 双层覆盖教学法(Dual-Layer Coverage)**
- **叙事锚点**(80% 教学时间):用一个可演进的业务系统贯穿整个模块,语法点被"需求升级"逼出来
- **语法点独立样本**(20% 教学时间):无法嵌入叙事的语法点用最小可复现实例单独演示
- 适用:所有"语法体系 vs. 真实应用"有落差的模块(ML/DL/爬虫/AI 应用)

**2. NCDL — 负案例驱动学习(Negative-Case-Driven Learning)**
- 四步循环:Code-Along(正向) → Break It(故意破坏) → 读 Traceback/出问题 → Fix & Discussion
- 与普通"错题本"的区别:错题本是学生做错后复盘;NCDL 是教师**在学生犯错之前先展示"常见错法"**
- 适用:所有有反模式的模块(ML 漏标准化/DL 忘 zero_grad/爬虫触发 429/安全 SQL 注入)
- 不适用于:纯数学/概念(反向传播推导没有"错法"给学生 break)

**3. 消费者函数即门控(Consumer-Function Gate)**
- 不检查学生代码里有没有 if-elif;让消费者函数要求学生代码必须是多态的
- 给一个**结构性约束强的骨架**(消费者函数 ≤4 行),学生只能通过正确实现来完成
- 适用:所有"设计让学生证明自己理解某个机制"的 Gate 题

## Version control scheme

The repo uses **git + timestamp backup** for versioning:

```bash
# 1. Before any major edit, make a timestamp backup(see Common commands)
# 2. git add / commit / push for versioned releases
```

Current version: **v2.3.0** (2026-07-14) — 60 days / 6 modules / h3+h4 / execution trace / 趁热打铁 / OOP 4 天(L1-L4) / 双层覆盖+NCDL+消费者门控.

## Out of scope (don't do)

- **Don't delete exercise files** — move to 选做(optional), never delete.
- **Don't introduce third-party packages** without checking against the per-Day boundary table (stdlib + NumPy/Pandas/sklearn/PyTorch/HF only).
- **Don't reorder / re-number lesson directories** — the number in `lessonXX` is the Day sequence.
- **Don't front-load syntax the student hasn't reached** — see the per-Day boundary table.
- **Don't put hidden files in lesson directories** (`.DS_Store` is an OS artifact, exempt).

## Key file index

| I need… | Read this |
|---|---|
| 59-day schedule + capability targets | `summary.md` |
| Teacher daily flow + grading breakdown | `README.md` |
| Complete user guide(for teachers / students / self-learners) | `USER_GUIDE.md` |
| Non-Python prerequisites (math/CS) | `PREREQUISITES.md` |
| Per-lesson topic distribution | `course/lessonXX/README.md` |
| Market course comparison / exercise pool | `references.md` |
| Canonical exercise-file example | `course/lesson01/in_class/practice01.py` |
| Day 1-19 student Jupyter Notebooks(h3+h4 / execution trace / 趁热打铁) | `student-notebooks/` |
| Jupyter 排版规范(gold standard = Day 08 v6 + 7 踩过的坑) | `dev/skills/05_Jupyter_Notebook_排版规范.md` |
| 学习断层修复指南(6 个 P0 断层) | `dev/learning-gaps.md` |
| 知识地图推理 / 学习顺序编排 / 试题集组织 | `dev/skills/01-04_*.md` |
| OOP 4 天教学设计(L1-L4 / 双层覆盖/NCDL / 消费者门控) | `dev/skills/06_OOP_教学方案设计.md` |
| New-day → old-lesson exercise mapping | `dev/module0-mapping.md` |
