# 63 天 AI 就绪 Python 工程师 · 教学计划

> 版本: v2.2.0 | 2026-07-09
> 适用对象: 零基础(能打字、会用鼠标、知道"文件/目录"概念)
> 终点能力: 机器学习 / LLM 微调 / Web 爬虫 / AI 应用开发
> 前置知识: 见 [`PREREQUISITES.md`](PREREQUISITES.md)(数学/网络/系统,假设已具备或同步补足)

## 如何使用本计划

### 每日教学流程

1. **课前**:看 `course/lessonXX/README.md` 与 `course/lessonXX/slides.md`,确认当日当堂练选题
2. **课中**:用 `demo/` 演示 → 当堂练(每节 2-3 题)→ 巡场点评
3. **课后**:学员做 `homework/`(含当堂练未完成部分 + 选做)→ 教师写 `teacher_notes.md`
4. **每 7-10 天**:阶段复习日(Day 09/16/39)或 期末答辩(Day 59)

### 各目录角色

| 目录 | 谁写 | 何时用 |
|---|---|---|
| `slides.md` | 教师可改 | 授课主线(课前备好) |
| `demo/` | 当堂课演示 | 演示用 |
| `in_class/` | 当堂练(每题标注 当堂练/选做) | 学员课上写 |
| `homework/` | 课后作业(选做) | 学员课后写 |
| `assets/` | 教师按需放 | 素材 |
| `mini_project/` | 每 2~3 天的综合项目 | 综合运用 |
| `teacher_notes.md` | 教师课后写 | 错题积累 |

### 评分构成(建议)

- 当堂小作品 30%(60 次,取最高 20 次)
- 期末作品(Demo + 文档 + 答辩) 40%(四选一)
- 每周中型项目 20%(3 个,可选做)
- 出勤与错题本 10%

### 期末作品四选一(Day 58-59)

| 方向 | 作品示例 | 串联 Domain |
|---|---|---|
| **AI 应用** | RAG+Agent 智能助手 | H+F+E+G |
| **LLM 微调** | 垂直领域客服模型 | F+E+G+B |
| **数据+爬虫** | 大规模数据采集与分析平台 | G+B+C |
| **ML 工程** | 端到端预测系统 | C+D+B+H |

每个方向提供:脚手架代码(项目结构/关键函数签名)+ 验收 checklist + 参考案例 + 推荐技术选型。

### 项目设计逻辑

本课程采用**三层项目体系**,从单点综合运用 → 模块综合 → 跨模块大项目,逐步培养工程能力:

#### 第一层:Mini Project(每 2-3 天,当堂完成)

| 设计原则 | 说明 |
|---|---|
| **即时巩固** | 每个 Mini Project 紧跟对应知识点,当天学当天练,防止"学了后面忘了前面" |
| **单点综合** | 聚焦 1-2 个核心知识点,综合运用而非单一语法复制 |
| **当堂可完成** | 设计为 45 分钟(一节课)内可完成,保持学员成就感 |

**Mini Project 清单**:

| Day | 项目 | 整合知识点 |
|---|---|---|
| 01 | 自我介绍 | print/input/f-string/变量 |
| 02 | 手机号脱敏 | 切片/isdigit/条件判断 |
| 03 | BMI 计算器 | if/elif/else/f-string |
| 04 | 每日记账本 | while 循环/列表/累加 |
| 05 | 工具函数库 | def/return/多种参数形式 |
| 06 | 通讯录 v1 | 列表/字典 CRUD/in 运算 |
| 07 | 日记本持久化 | 文件读写/JSON/异常 |
| 08 | Student 类建模 | class/__init__/@property/__str__ |
| 11 | 矩阵运算 | NumPy 数组/广播/向量化 |
| 13 | 数据探索 | Pandas DataFrame/过滤/排序 |
| 15 | 数据报告配图 | Matplotlib/Seaborn 多图组合 |
| 16 | 多源数据整合 | read_csv/read_json/read_sql → 合并 |

#### 第二层:Weekly Project(每周五,2 小时+课后)

| 设计原则 | 说明 |
|---|---|
| **模块综合** | 整合一整周(5 天)知识点,完成一个中等复杂度系统 |
| **分阶段交付** | 周五课堂搭建骨架 → 周末完善细节,培养项目管理意识 |
| **代码结构** | 引入函数封装、模块化、异常处理等工程规范 |

**Weekly Project 清单**:

| Week | Day | 项目 | 整合能力 | 工程规范 |
|---|---|---|---|---|
| 1 | 10 | 购物车 v1 | Day01-09 Python 全部 | 函数封装 / 菜单循环 / 异常处理 |
| 2 | 17 | EDA 报告 | NumPy+Pandas+可视化 全流程 | 数据清洗 / 可视化 / 洞察表达 |
| 3 | 25 | Kaggle ML Pipeline | ML 全流程(train→eval→tune) | Pipeline / GridSearch / joblib 持久化 |

#### 第三层:期末 Capstone(Day 58-59,3 天集中)

| 设计原则 | 说明 |
|---|---|
| **跨模块综合** | 串联 ≥ 5 个 Domain 的知识,模拟真实工作场景 |
| **学员自选** | 四选一(AI 应用/LLM/爬虫/ML),尊重兴趣导向 |
| **产品思维** | 不仅要"能跑",还要有 README、Demo、工程文档 |

**四方向设计逻辑**:

| 方向 | 核心问题 | 技术栈选择理由 |
|---|---|---|
| **AI 应用** | 如何把 LLM 变成可用的产品? | FastAPI+RAG+Agent=当前 AI 应用标准架构 |
| **LLM 微调** | 如何让大模型适配垂直领域? | Hugging Face+LoRA=参数高效微调事实标准 |
| **数据+爬虫** | 如何获取和构建训练数据? | requests+Scrapy=从数据源到数据集 |
| **ML 工程** | 如何把模型变成服务? | sklearn+FastAPI+Docker=ML 工程化标准链路 |

#### 项目难度递进曲线

```
复杂度 ↑
        │                                    ┌─ 期末 Capstone
        │                               ┌────┤ (跨 5+ 模块,产品级)
        │                          ┌────┤    └────
        │                     ┌────┤ W3 │
        │                ┌────┤ W2 │    │
        │           ┌────┤ W1 │    │    │
        │      ┌────┤ M7 │    │    │    │
        │ ┌────┤ M4 │    │    │    │    │
        │─┤ M1 │    │    │    │    │    │
        │ │    │    │    │    │    │    │
        └─┴────┴────┴────┴────┴────┴────┴────→ Day
          1    4    7   10   17   25   31   40   50-59

M = Mini Project(单点综合)  W = Weekly Project(模块综合)  ┌─ = Capstone(跨模块)
```

#### 评分 rubric 设计

| 维度 | Mini Project | Weekly Project | Capstone |
|---|---|---|---|
| 功能完整性 | 40% | 30% | 30% |
| 代码结构 | 30%(函数拆分) | 30%(模块+异常) | 30%(工程化) |
| 可读性 | 20%(命名+注释) | 20%(README) | 20%(文档+Demo) |
| 扩展功能 | 10%(额外加分) | 20%(创新点) | 20%(亮点) |

**设计意图**:
- Mini Project 侧重"能不能跑通"(功能 40%)
- Weekly Project 侧重"代码是否工程化"(结构 30%)
- Capstone 侧重"产品是否可用+可展示"(Demo+文档 40%)

### 四个终点能力

| 能力 | 终点标准 | 对应模块 |
|---|---|---|
| **机器学习** | 能基于 scikit-learn 完成端到端 ML 项目 | Module 1 (Day 18-24) |
| **LLM 微调** | 能基于 Hugging Face + LoRA 微调开源大模型 | Module 4 (Day 36-42) |
| **Web 爬虫** | 能写 HTTP/API/动态页面爬虫构建数据集 | Module 5 (Day 43-49) |
| **AI 应用开发** | 能开发 RAG/Agent/AI API 应用并部署 | Module 6 (Day 50-59) |

### 参考资料

- `references.md`: 外部成熟课程的习题 / 项目 / 教学思路素材库
- `PREREQUISITES.md`: 数学/网络/系统前置知识(不在课程内讲授)
- `summary.md`: 63 天总进度表

---

## 进度追踪(建议)

- Day 10: Python 核心阶段测 ≥ 70%
- Day 17: 数据处理阶段测 ≥ 70%
- Day 40: ML+DL 综合项目验收
- Day 59: 期末答辩(4 方向选 1)

---

## 快速启动清单

### 学生自学路径(Student Notebooks)

**完全零基础?** `student-notebooks/` 文件夹提供了 Day 1-17 的交互式学习笔记:

| 项 | 说明 |
|---|---|
| **内容** | 17 个 Jupyter Notebook(Day 01-17,Python 核心 + 数据处理) |
| **格式** | 每个知识点后紧跟练习,章节末尾附试题集链接 |
| **练习** | 83 个交互式练习(学员代码区 + 参考答案) |
| **链接** | 每章末尾指向 `course/lessonXX/in_class/` + `homework/` 的完整习题 |

**使用方式**:
1. 安装 Jupyter:`pip install jupyter numpy pandas matplotlib seaborn`
2. 启动:`cd student-notebooks && jupyter notebook`
3. 先打开 `00_JupyterNotebook使用教程.ipynb`(30 分钟上手)
4. 按 Day 01 → Day 17 顺序学习,每天约 6 小时
5. 每个 notebook 内:阅读 → 看示例 → 做练习 → 对答案

> 📖 Day 18-59(ML/DL/NLP/LLM/爬虫/AI 应用)暂未制作 Jupyter 版,使用 `course/lessonXX/` 的 slides + 习题自学。

---

- [ ] 阅读 `PREREQUISITES.md` → 确认前置数学/网络知识已具备
- [ ] 逐课看 `course/lessonXX/slides.md` + `course/lessonXX/README.md` → 确认当堂练选题
- [ ] 为每个 weekly_project 准备验收脚本(`test_week_N.py`)
- [ ] Day 58: 为 4 个期末作品方向准备脚手架代码
