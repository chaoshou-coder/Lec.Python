# 21 天 Python 零基 → OOP + 控制台小项目 · 重构计划

> 本目录 = v1 教学计划(21 天,178 道习题,3 个中型项目) + v2 迭代提案 + 市场参考素材池。
> **发布就绪**:所有路径已改为相对路径,可在 GitHub 上clone 并在任意设备开发。
>
> 旧课件 day01-day07 在 `../day01/` ~ `../dayXX/`(相对于本目录的父目录 `课件/`),与本计划**物理隔离**,不要拷贝或覆盖。

---

## 发布就绪性检查清单

| 项 | 状态 |
|---|---|
| 绝对路径(/Users/..) | ✅ 0 处 |
| .gitignore(DS_Store/.versions/.venv) | ✅ 已创建 |
| 外部计划文件 | ✅ 已复制到 dev/plans/ |
| 开发用 vs shipping 文件分类 | ✅ dev/ 目录隔离 |
| 跨设备路径 | ✅ 全部相对路径或 ./ 开头 |
| CLAUDE.md 入口 | ✅ 本文件 |

**第一次使用**(在任何设备上):
1. `git clone` 本仓库
2. 进入 `课件/重构计划/`
3. 读 `CLAUDE.md`(即本文件)
4. 按"怎么继续"开始

**克隆后父目录结构**:
```
课件/
├── day01/ ~ day07_code/   ← 旧 7 天课件(本计划不修改)
└── 重构计划/               ← 本目录,21 天新计划
```

---

## 这个项目是什么

一份面向成年零基础 / NIT 考证 / 跨考学员的 Python 入门到 OOP 教学计划,21 天全日制(每天约 6 小时)推进,终点作品是"控制台图书管理系统 v2(OOP + JSON 持久化 + CSV 导出 + 异常处理)"。课程节奏强调**练习密度**:每节 in_class 当堂练 + 每日 homework + 每周中型项目,远超廖雪峰/莫烦的"读懂为主"模式。

本目录**不是** Python 源码仓库,是**课程资产仓库**。每个 lesson 目录含讲义、习题、素材、教师备忘。

---

## 目录结构(发布就绪)

```
重构计划/
├── .gitignore                   ← 忽略 .DS_Store/.versions/.venv/编辑器文件
├── CLAUDE.md                    ← 本文件:项目入口,任何新 Claude 会话先读它
├── README.md                    ← 教师使用指南(每日流程 / 评分构成)
├── summary.md                   ← 21 天进度表 + Day01-Day07 缺陷修复清单
├── references.md                ← 市场素材池(14 门课程 / 100+ 习题 / 25 项红线)
├── CHANGELOG.md                 ← 版本变更日志
├── iteration-v2-plan.md         ← v2 迭代提案(三套方案 A/B/C)
├── lesson01/ ~ lesson21/        ← 21 个标准课时目录 = **shipping core**
│   ├── README.md                ← 每课概览(当堂表 / 课后表 / 小项目 / 阶段复习)
│   ├── slides.md                ← 教师讲义(含引入 / 三讲+练 / 总结节奏)
│   ├── demo/                    ← 演示脚本(每文件对应一个细分知识点)
│   ├── in_class/                ← 当堂练习(practice01.py ~ practiceNN.py)
│   ├── homework/                ← 课后作业(task01.py ~ taskNN.py)
│   ├── assets/                  ← 素材(xiongmao.txt / data*.txt 等)
│   ├── mini_project/            ← 每 2~3 天的综合小项目
│   └── teacher_notes.md         ← 教师备忘(课后填写"高频错 3 件事")
├── weekly_projects/             ← 3 个中型项目(购物车/图书 v1/图书 v2 OOP)
│   ├── week01_shopping_cart/
│   ├── week02_library_manager/
│   └── week03_book_manager_oop/
├── dev/                         ← **开发辅助文件**(不参与最终课程,但保留在仓库)
│   ├── plans/                   ← 从 ~/.claude/plans/ 复制来的计划本体
│   │   ├── day7-day7-os-glowing-crystal.md          ← 21 天计划 17 KB
│   │   └── day7-day7-os-glowing-crystal.references.md ← 调研素材池 20 KB(同根目录 references.md 调研版)
│   └── agent-artifacts/         ← agent 中间产物(可删除,不影响课程)
└── .versions/                   ← **本地备份**,已被 .gitignore 忽略
    └── lessons-v1-20260707-152921/  ← v1 完整备份
```

### 文件角色分类

| 类别 | 目录 | 是否推 GitHub | 说明 |
|---|---|---|---|
| **Shipping core** | `lesson*/` `weekly_projects/` 根目录 `.md`(CLAUDE.md/README/SUMMARY/references/CHANGELOG/iteration) | ✅ 是 | 课程主资产 |
| **Dev convenience** | `dev/plans/` | ✅ 是 | 外部计划文件副本,方便跨设备恢复上下文 |
| **Dev ephemeral** | `dev/agent-artifacts/` | ⚠️ 可选 | agent 中间产物,删了不影响课程 |
| **Local backup** | `.versions/` | ❌ 否(.gitignore) | 本地时间戳备份 |
| **OS / 编辑器** | `.DS_Store` `.vscode/` `.idea/` `.venv/` | ❌ 否(.gitignore) | 系统/工具产物 |

### 习题文件的硬规则(写入新题必须遵守)

命名:`lessonXX/in_class/practiceNN.py` 或 `lessonXX/homework/taskNN.py`,`NN` 两位数零填充(01,02,...,09,10,...)。

每个题文件**必须**包含:

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

约束清单:
- 所有字符串用中文
- 每行 ≤ 100 字符
- 学员区以 `pass` 占位(或留部分脚手架代码),**不能出现学员还没学的语法**(参考 lesson 所在 Day 的知识点边界)
- 测试区至少 2 个用例,覆盖边界条件(空输入 / 零 / 负数 / 单一元素等)
- Day01-Day06 不出现函数;Day07-Day09 出现函数但不出现类;Day10-Day17 出现函数/异常/文件操作但不出现类;Day18-Day21 才出现类/继承/多态

---

## 版本控制(无 git,手动方案)

父目录非 git 仓库(课件机构资产),不能 `git init`。采用**时间戳 + CHANGELOG** 的原始版本控制:

```bash
# 1. 任何重大修改前,先做时间戳备份:
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p .versions
cp -r lesson*/ .versions/lessons-v${NEXT_VERSION}-${TIMESTAMP}/

# 2. 在 CHANGELOG.md 更新对应版本段(格式见该文件)

# 3. 必要时从 .versions/ 还原
```

当前版本:
- **v1.0.0**(2026-07-07):初始版本,21 天 / 178 道题 / 3 个中型项目。备份见 `.versions/lessons-v1-20260707-152921/`

---

## 当前进度(任何新会话的起始点)

### 已完成
- [x] 21 天完整习题库(178 道)
- [x] 21 个 lesson README 实际内容(非占位)
- [x] 21 个 lesson slides.md(含主题标题 + 节奏骨架)
- [x] 3 个 weekly_projects README(含验收 checklist)
- [x] references.md 市场调研(14 门主流课程 / 100+ 习题 / 25 项教学红线)
- [x] CHANGELOG.md 版本日志
- [x] iteration-v2-plan.md v2 迭代提案(三套方案)

### 待做(按优先级)
1. **(高)** 补 178 个自动评测脚本 `test_NN.py`(每 in_class 题 1 个,参考 iteration-v2-plan.md §4.1 模板)
2. **(中)** 补 7 道缺口题(装饰器 2 + 生成器 2 + 正则 1 + 日志 1 + ABC 1),嵌入 lesson11/12/14/16/20
3. **(中)** 调整 Day17/18 阶段复习日分配(详见 iteration-v2-plan.md §A.3)
4. **(低)** v2 结构迭代(重新排布 Day11-14,Day20 引入调试+测试专项)
5. **(长期)** 练习量从 178 冲至 300+(每日一题 + Mini Case Study)

---

## 不在 scope 里(避免踩雷)

- **不要修改 `../day01/` ~ `../day07/`**(相对于本目录的父目录) — 这些是旧课件,本计划物理隔离
- **不要引入第三方包** — 除了 `colorama`(已用过 1 次),全程标准库
- **不要跳 Day 序重构 lesson 目录** — 文件名里的数字 = Day 顺序,到处被引用
- **不要把学员已"通关"的知识前置** — Day04 的题不能出现 `def`,Day10 的题不能出现 `class`
- **不要在 lesson 目录放隐藏文件**(`.DS_Store` 除外,操作系统产物)

---

## 多设备 / 跨仓库工作流

### 设备 A(当前)
- 项目路径:`/Users/bang/Documents/learning/python/课件/重构计划/`
- Claude plans:`~/.claude/plans/day7-day7-os-glowing-crystal*.md`(已备份到 `dev/plans/`)

### 设备 B(新 clone)
1. `git clone <repo_url>`
2. `cd 课件/重构计划`
3. 读 `CLAUDE.md`(即本文件)→ 立刻就位
4. 如果要用 Claude 继续开发,把 `dev/plans/` 的 plan 文件复制到 `~/.claude/plans/`

### 为什么 dev/plans/ 要在仓库外再存一份
`~/.claude/plans/` 是 Claude Code 的全局目录,**不进任何仓库**。但它是本次开发的核心产物(21 天计划本体 + 调研素材池),丢了就得重新生成。所以在 `dev/plans/` 保留副本,**推送 clone 后任何设备都能恢复上下文**。

---

## 关键决策上下文

### 为什么是 21 天 178 题,而不是 28 天马黑马 / 30 天达内模式
市场课程练习密度偏低(廖雪峰"读懂为主"、莫烦视频驱动、黑马一天讲 8 节但只配 1~2 道例题)。本计划的核心差异是 **"讲→写→纠错→再写"循环完整**:每节 in_class 当场练 2~3 题,巡场点评,课后 homework 再巩固 2~3 题,每周五中型项目收尾。178 题 / 21 天 ≈ 每天 8.5 道,远超市面平均每天 2~3 道。

### 为什么终点是"控制台图书管理系统 v2"而不是 Flask/Pygame 项目
成年零基 / NIT 考证学员的第一门课目标是"理解编程思维 + 掌握基础工具链",不是做花哨的 GUI 或 Web。控制台图书管理串联了所有核心知识点(数据类型 → 容器 → 循环/分支 → 函数 → 文件 → 异常 → JSON/CSV → 类/继承/多态),是 Python.org Tutorial / Think Python / PyNative 推荐的"闭环项目"。

### OOP 为什么用 4 天(Day18-21)而不是 2 天
黑马 / 达内 OOP 讲 2 天,跑得快但学员只能背语法。本计划 Day18(封装:init/self/`_`/`__`/`@property`/`__str__`)→ Day19(继承+多态:`super()`/重写/类属性 vs 实例属性/ABC)→ Day20-21(综合项目)。这 4 天够学员真的"用 OOP 拆解问题"而不是"背 OOP 名词"。

---

## 怎么继续(一个会话该做什么)

新会话进这个目录,读完本 CLAUDE.md 后:

1. **确认当前版本**:读 `CHANGELOG.md` 顶部
2. **确认当前 task**:看"待做"清单挑一个推进
3. **写新文件 / 改旧文件**:遵守本文件里的命名和格式约束
4. **改完后**:更新 `CHANGELOG.md` 对应版本段,必要时 `.versions/` 留时间戳备份
5. **别做的事**:参见"不在 scope 里"清单

如果任务涉及重排 lesson 目录结构或新增 Day,先在 `iteration-v2-plan.md` 追加方案段落,**不要直接改 v1 文件** — v1 已可落地,重构应在 v2 分支(新目录或时间戳备份后改动)。

---

## 文件快速索引

| 我需要... | 读这个文件 |
|---|---|
| 21 天总进度 + 缺陷修复清单 | `summary.md` |
| 教师每日流程 + 评分构成 | `README.md` |
| 每课知识点分布 | `lessonXX/README.md` |
| 市场 14 门课程对比 / 100+ 习题素材 | `references.md` |
| v2 迭代方案(A/B/C) | `iteration-v2-plan.md` |
| 版本变更历史 | `CHANGELOG.md` |
| 某道题格式参考 | `lesson01/in_class/practice01.py`(标杆样例) |
| 计划本体(从 Claude plans 复制) | `dev/plans/day7-day7-os-glowing-crystal.md` |
| 市场调研原始版 | `dev/plans/day7-day7-os-glowing-crystal.references.md` |
| agent 中间产物 | `dev/agent-artifacts/`(可删) |
