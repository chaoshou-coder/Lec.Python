# 59 天 AI 就绪 Python 工程师 · 使用说明书

> 版本: v2.0.0 | 2026-07-07
> 适用对象: 教师 / 学员 / 自学者
> 配套课程: [README.md](README.md) · [summary.md](summary.md) · [PREREQUISITES.md](PREREQUISITES.md)

---

## 目录

| # | 章节 | 内容 |
|---|---|---|
| 1 | [课程概览](#1-课程概览) | 课程目标、终点能力、适用人群 |
| 2 | [仓库结构](#2-仓库结构) | 目录说明、文件角色 |
| 3 | [环境搭建](#3-环境搭建) | Python/Jupyter/第三方库安装 |
| 4 | [教师指南](#4-教师指南) | 每日教学流程、评分、课前准备 |
| 5 | [学员指南](#5-学员指南) | 每日学习流程、笔记本使用、练习规范 |
| 6 | [每日节奏](#6-每日节奏) | 6 节课的时间分配 |
| 7 | [59 天课表总览](#7-59-天课表总览) | 6 个 Module 的 Day 列表 |
| 8 | [阶段复习与测验](#8-阶段复习与测验) | Day 10/17/40 的复习安排 |
| 9 | [期末作品](#9-期末作品) | 四选一方向、评分标准、时间安排 |
| 10 | [常见问题 FAQ](#10-常见问题-faq) | 安装/学习/环境/评估 Q&A |
| 11 | [参考资料](#11-参考资料) | 教材/社区/求助渠道 |
| 12 | [学习断层与修复](#12-学习断层与修复) | 6 个 P0 断层及修复状态 |

---

## 1. 课程概览

### 1.1 课程目标

培养**能独立完成以下 4 项任务的 AI 工程师**:

| 终点能力 | 具体标准 | 对应模块 |
|---|---|---|
| **机器学习** | 基于 scikit-learn 完成端到端 ML 项目(数据→预处理→建模→评估→部署) | Module 1 (Day 17-23) |
| **LLM 微调** | 基于 Hugging Face + LoRA 微调开源大模型→评测→推理部署 | Module 4 (Day 35-41) |
| **Web 爬虫** | HTTP/API/动态页面爬虫→数据清洗→存储→构建数据集 | Module 5 (Day 42-48) |
| **AI 应用开发** | FastAPI + RAG + Agent + Docker 部署,上线 AI 应用 | Module 6 (Day 49-58) |

### 1.2 适用人群

| 角色 | 要求 | 建议 |
|---|---|---|
| **零基础学员** | 能打字、会用鼠标、知道"文件/目录"概念 | 按 Day 1-59 顺序学习 |
| **有 Python 基础** | 已掌握变量/函数/OOP | 从 Module 1 (Day 17) 开始 |
| **转行/跨考** | 需要项目作品支撑求职 | 重点做好期末作品 |
| **教师** | 有 Python 教学经验 | 参考教师指南 + slides.md |

### 1.3 学习周期

| 模式 | 周期 | 每日投入 |
|---|---|---|
| 全日制集训 | **59 天**(约 12 周) | 6 小时/天(360 分钟) |
| 业余学习 | 约 24 周 | 2-3 小时/天 |
| 加速模式 | 约 40 天 | 8-10 小时/天 |

---

## 2. 仓库结构

### 2.1 目录布局

```
Lec.Python/
├── USER_GUIDE.md                  ← 本文件:使用说明书
├── README.md                      ← 课程主文档(目标/流程/评分)
├── summary.md                     ← 59 天进度表 + 每天知识点
├── CLAUDE.md                      ← AI 开发助手操作指南
├── PREREQUISITES.md               ← 数学/网络/系统前置知识
├── references.md                  ← 14 门课程对比 + 100+ 习题素材池
│
├── course/lesson01/ ~ course/lesson59/          ← 59 个课时目录(每天 1 个)
│   ├── README.md                  ← 每课概览(主题 / 习题表)
│   ├── slides.md                  ← 教师讲义(当课主线)
│   ├── demo/                      ← 演示脚本(教师课堂演示)
│   ├── in_class/                  ← 当堂练习(practice01.py ~ practiceNN.py)
│   ├── homework/                  ← 课后作业(task01.py ~ taskNN.py)
│   ├── mini_project/              ← 每 2~3 天的综合小项目
│   ├── assets/                    ← 素材(数据集/文本/图片)
│   └── teacher_notes.md           ← 教师备忘(高频错 3 件事)
│
├── student-notebooks/             ← 学生版 Jupyter Notebook(Day 1-17)
│   ├── 00_JupyterNotebook使用教程.ipynb
│   ├── Day01_Python与开发环境.ipynb
│   ├── ...
│   └── Day17_EDA综合项目.ipynb
│
├── weekly_projects/               ← 3 个中型项目
│   ├── week01_shopping_cart/      ← Day 10 阶段复习(函数+OOP 版购物车)
│   ├── week02_library_manager/    ← Day 20 阶段复习
│   └── week03_book_manager_oop/   ← Day 21 阶段复习(OOP 版)
│
└── dev/                           ← 开发辅助(不推 GitHub)
    ├── module0-mapping.md         ← 新 Day → 旧 lesson 习题映射
    └── plans/                     ← 备份
```

### 2.2 各目录角色

| 目录/文件 | 作者 | 用途 | 何时用 |
|---|---|---|---|
| `lessonXX/slides.md` | 教师可改 | 授课主线(每节课的讲义) | 课前备好,课中讲授 |
| `lessonXX/demo/` | 教师/学员 | 演示脚本 | 当堂课演示知识点 |
| `lessonXX/in_class/` | 学员 | 当堂练(课堂上当场写) | 每节 2-3 题 |
| `lessonXX/homework/` | 学员 | 课后作业(回家写) | 课后自主完成 |
| `lessonXX/mini_project/` | 学员 | 综合小项目 | 每 2~3 天一次 |
| `lessonXX/assets/` | 教师 | 素材(数据/文本) | 练习所需 |
| `lessonXX/teacher_notes.md` | 教师 | 错题积累 | 课后填写 |
| `student-notebooks/` | 学员 | 交互式学习笔记 | 预习/复习用 |
| `weekly_projects/` | 学员 | 中型综合项目 | 每周五 |

---

## 3. 环境搭建

### 3.1 基础环境

| 软件 | 版本 | 安装方式 | 验证命令 |
|---|---|---|---|
| Python | 3.10+ | [python.org](https://python.org) 下载 | `python3 --version` |
| VSCode | 最新 | [code.visualstudio.com](https://code.visualstudio.com) | `code --version` |
| Jupyter Notebook | 7.x | `pip install jupyter` | `jupyter --version` |

### 3.2 数据科学库(Module 0 Day 11+ 需要)

```bash
# 一次性安装全部数据/AI 库
pip install numpy pandas matplotlib seaborn scikit-learn

# 深度学习库(Module 2+ 需要)
pip install torch torchvision

# NLP/LLM 库(Module 3+ 需要)
pip install transformers datasets pefttrl

# 爬虫库(Module 5+ 需要)
pip install requests beautifulsoup4 lxml playwright scrapy

# AI 应用库(Module 6+ 需要)
pip install fastapi uvicorn chromadb sentence-transformers
```

### 3.3 Jupyter Notebook 启动

```bash
# 进入课程目录
cd student-notebooks

# 启动 Jupyter
jupyter notebook

# 浏览器自动打开 http://localhost:8888
# 没有自动打开?手动在浏览器输入该地址
```

> 📖 **Jupyter 零基础?**先打开 `student-notebooks/00_JupyterNotebook使用教程.ipynb`,30 分钟学会基本操作。

---

## 4. 教师指南

### 4.1 每日教学流程

```
课前(30 分钟)                 课中(360 分钟)                    课后(30 分钟)
┌─────────────────┐     ┌──────────────────────────┐     ┌─────────────────┐
│ 1.看 slides.md   │     │ 第 1 节:引入+第一讲+练 2 题│     │ 1.写 teacher_   │
│ 2.看习题表       │     │ 第 2 节:第二讲+练 2 题    │     │   notes.md      │
│ 3.确认当堂练选题 │ →   │ 第 3 节:第三讲+练 2 题    │ →   │ (当课错 3 件事) │
│ 4.准备 demo      │     │ 第 4 节:小项目(若本日有)  │     │ 2.布置作业      │
│                  │     │ 第 5-6 节:延续+总结       │     │                 │
└─────────────────┘     └──────────────────────────┘     └─────────────────┘
```

### 4.2 课前准备清单

| 步骤 | 内容 | 时间 |
|---|---|---|
| 1 | 读 `lessonXX/slides.md` → 确认当日 3 个知识点 + 代码示例 | 10 分钟 |
| 2 | 读 `lessonXX/README.md` → 确认当堂练选题(6 题中选哪 2-3 题当堂做) | 5 分钟 |
| 3 | 运行一遍 `demo/` + `in_class/practice*.py` → 确认代码可跑、答案正确 | 10 分钟 |
| 4 | 准备"引入"环节的 demo(一个有趣的小脚本,吊足胃口) | 5 分钟 |

### 4.3 巡场重点

每节当堂练时,**走下讲台巡场**,关注三类学员:

| 信号 | 可能问题 | 干预方式 |
|---|---|---|
| 盯着屏幕不动,没敲键盘 | 不理解题目/不知道怎么开始 | 引导读题 → 拆解步骤 → 类比已做过的例题 |
| 疯狂删代码,焦躁 | 卡在一个 bug 上太久 | 提示"先读错误信息的最后一行" |
| 早就写完在玩 | 学得快/已掌握 | 让他做选做题或帮助同桌 |

### 4.4 教学红线(高频易错点)

每节课至少强调 **1 条 🔴 教学红线**(融入 slides.md):

| 模块 | 红线示例 |
|---|---|
| Module 0 | `=` 是赋值 `==` 是比较;缩进混用 Tab/Space 报错;`elif` 顺序敏感 |
| Module 1 | 训练集/测试集数据泄露;分类不平衡只用准确率被蛊惑 |
| Module 2 | 忘 `optimizer.zero_grad()` 梯度累积;验证忘 `model.eval()` |
| Module 3 | Tokenizer 没对齐预训练模型;Chat Template 忘 `add_generation_prompt` |
| Module 4 | 全量微调显存爆用 LoRA;DPO 必须有 ref_model |
| Module 5 | 高频请求触发 429;动态页面用 requests 拿不到内容 |
| Module 6 | API Key 硬编码用 .env;Agent 忘设 `max_iterations` |

### 4.5 评分构成(建议)

| 项 | 权重 | 说明 |
|---|---|---|
| 当堂小作品 | 30% | 59 次,取最高 20 次 |
| 期末作品 | 40% | 四选一(Demo+文档+答辩) |
| 每周中型项目 | 20% | 3 个(可选做) |
| 出勤与错题本 | 10% | 出勤 + teacher_notes.md |

---

## 5. 学员指南

### 5.1 每日学习流程

```
┌───────────────────────────────────────────────────────────────┐
│  你的一天(6 小时 = 360 分钟)                                   │
├─────────┬─────────────────────────────────────────────────────┤
│ 复习     │ 抽问上节(5') → 回顾昨日的 🔴 易错点                  │
├─────────┼─────────────────────────────────────────────────────┤
│ 第一讲   │ 听讲(15') + 当堂练 2 题(20') = 45 分钟              │
│ 第二讲   │ 听讲(15') + 当堂练 2 题(25') + 小结(5') = 45 分钟   │
│ 第三讲   │ 听讲(15') + 当堂练 2 题(25') + 小结(5') = 45 分钟   │
├─────────┼─────────────────────────────────────────────────────┤
│ 午休     │ 60 分钟                                              │
├─────────┼─────────────────────────────────────────────────────┤
│ 小项目   │ 延续或新做(45 分钟)                                  │
│ 总结     │ 总结+测验+作业布置(45 分钟)                          │
└─────────┴─────────────────────────────────────────────────────┘
```

### 5.2 当堂练规范

| 步骤 | 要求 |
|---|---|
| 1.读题 | 先完整读一遍题目,理解"要做什么"再动手 |
| 2.思考 | 用笔/伪代码写思路(30 秒),不要直接敲代码 |
| 3.写代码 | 学员代码区 `pass` 处开始写 |
| 4.测试 | 运行测试区 `if __name__ == '__main__':`,全部通过才举手 |
| 5.对答案 | 独立做完后再看教师的参考实现 |

### 5.3 Jupyter Notebook 学习法(Module 0 推荐)

```
适合场景:Day 1-17(Module 0 Python 核心 + 数据处理)

第 1 遍: 读 markdown → 理解概念
第 2 遍: 运行 code cell → 看输出,建立直觉
第 3 遍: 完成练习 cell → 自己写代码
第 4 遍: 用自己的话在空白 cell 写总结(费曼技巧)
```

### 5.4 遇到不会的怎么办?

| 问题 | 解决顺序 |
|---|---|
| 概念不懂 | ① 翻 slides.md 对应段落 → ② 看 notebook 的图解 → ③ 问同桌 → ④ 问老师 |
| 代码报错 | ① 读 Traceback 最后一行 → ② 复制错误信息到搜索 → ③ 检查语法(冒号/缩进/括号) → ④ 问老师 |
| 想做不出来 | ① 把问题拆成 3 个小步骤 → ② 每步单独写代码 → ③ 组合 → ④ 卡 15 分钟以上再求助 |

### 5.5 作业规范

| 项 | 要求 |
|---|---|
| 命名 | `task01.py` / `task02.py`,保持原文件名 |
| 填空 | 只在 `# 学员代码区` 写代码,保持其他部分不变 |
| 测试 | 运行 `python3 task01.py`,输出"所有测试通过!"才算完成 |
| 提交 | 按教师要求提交(可随时查看 homework/TODO.md 了解进度) |

---

## 6. 每日节奏

### 标准 6 节课安排

| 节次 | 时长 | 名称 | 内容 |
|---|---|---|---|
| 第 1 节 | 45' | 复习 + 引入 | 抽问(5') + 赏 demo(5') + 第一讲(15') + 当堂练 1×2(20') |
| 第 2 节 | 45' | 第二讲 + 练 | 第二讲(15') + 当堂练 2×2(25') + 小结(5') |
| 第 3 节 | 45' | 第三讲 + 练 | 第三讲(15') + 当堂练 3×2(25') + 小结(5') |
| 第 4 节 | 45' | 小项目(若本日有) | 巡场 + 展示优秀作品 |
| 午休 | 60' |  |  |
| 第 5 节 | 45' | 小项目延续 / 第四讲 | 若 Day 无小项目,改为第四讲 |
| 第 6 节 | 45' | 总结 + 测验 + 作业布置 | 教师总结(5') + 错题本(5') + 闭卷小测(10') + 作业说明(5') + 自由问答(20') |

### 阶段复习日调整

| Day | 调整 |
|---|---|
| Day 10 | 6 节全部做题 + 购物车中型项目(函数+OOP 版) |
| Day 17 | 6 节全部做题 + EDA 综合项目 |
| Day 40 | ML+DL 综合项目 + DL vs ML 对比报告 |
| Day 58 | 期末答辩(Demo + 问答 + 互评) |

---

## 7. 59 天课表总览

### Module 0: Python 核心 + 数据处理(Day 1-17)

| Day | 主题 | 关键新增 | 小/中型项目 |
|---|---|---|---|
| 01 | Python 与开发环境 | `print` `input` `type` 变量 | 🎯 自我介绍 |
| 02 | 字符串与格式化 | f-string/切片/`isdigit` | 🎯 手机号脱敏 |
| 03 | 条件分支 | `if/elif/else` 嵌套、逻辑组合 | 🎯 BMI 计算器 |
| 04 | 循环入门 | `while` `for` `range` 累加/累乘 | 🌟 每日记账本 |
| 05 | 函数入门 | `def` 四种形式 `return` | 🎯 工具函数库 |
| 06 | 列表与字典 | CRUD:`append`/`pop`/`items()` | 🎯 通讯录 v1 |
| 07 | 文件 I/O + 异常 | `with`/`JSON`/`try`-`except` | 🎯 日记本持久化 |
| 08 | OOP 基础 | `class`/`__init__`/`@property` | 🎯 Student 类 |
| 09 | 模块与高级特性 | 包/生成器/装饰器/`import` |  |
| 10 | **阶段复习①** | Day01-09 综合 | 🌟 购物车(函数+OOP 版) |
| 11 | NumPy 基础 | 数组/广播/向量化 | 🎯 矩阵运算 |
| 12 | NumPy 进阶 | 线性代数/随机数/统计 |  |
| 13 | Pandas 基础 | Series/DataFrame/索引/过滤 | 🎯 数据探索 |
| 14 | Pandas 进阶 | 分组/合并/透视/清洗 |  |
| 15 | 数据可视化 | 折线/柱状/散点/热力图 | 🎯 数据报告配图 |
| 16 | 数据摄取 | CSV/JSON/Excel/SQL/API | 🎯 多源数据整合 |
| 17 | **阶段复习②(EDA)** | Module 0 综合 | 🌟 EDA 分析报告 |

### Module 1: 机器学习(Day 17-23)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 18 | ML 概念与工作流 | 监督/无监督/过拟合/`train_test_split` | 手写数字探索 |
| 19 | 数据预处理 | 缩放/编码/缺失值/`ColumnTransformer` | 数据集清洗 |
| 20 | 线性回归+梯度下降 | MSE/SGD 直觉 | 房价预测 |
| 21 | 逻辑回归+树模型 | Sigmoid/决策树/随机森林 | 泰坦尼克预测 |
| 22 | 梯度提升+SVM | XGBoost 残差拟合/核技巧直觉 | Kaggle 入门赛 |
| 23 | 聚类+降维 | K-Means/PCA/t-SNE | 客户分群 |
| 24 | 模型评估+流水线 | ROC-AUC/交叉验证/`Pipeline`/`GridSearchCV` | 多模型对比 |
| 25 | **ML 项目日** | 模型持久化+端到端项目 | Kaggle 竞赛 |

### Module 2: 深度学习(Day 24-29)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 26 | 神经网络基础 | 感知机/激活函数/前向传播 | 手写感知机 |
| 27 | **反向传播⚡深入** | 链式法则/SGD/Adam | 手动 BP 实现 |
| 28 | PyTorch 基础 | tensor/autograd/`nn.Module`/`DataLoader` | NumPy→PyTorch |
| 29 | 训练循环 | optimizer/loss/epoch/验证 | MNIST 训练 |
| 30 | CNN+RNN+正则化 | 卷积/池化/LSTM/Dropout | 图像分类器 |
| 31 | 迁移学习+DL 项目 | 预训练/冻结/微调 | CIFAR-10 |

### Module 3: NLP 与 Transformer(Day 30-34)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 32 | 文本预处理+表示 | 分词/BoW/TF-IDF/词嵌入 | 文档相似度 |
| 33 | 序列模型 for text | RNN/LSTM | 字符级文本生成 |
| 34 | **注意力机制⚡深入** | Q/K/V/缩放点积/多头注意力 | 手动 attention |
| 35 | Transformer+预训练模型 | BERT/GPT/T5 架构选型 | Transformer 解剖 |
| 36 | Hugging Face 实战 | `pipeline`/`AutoModel`/`Tokenizer` | 情感分析 |

### Module 4: LLM 微调(Day 35-41)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 37 | LLM 生态+HF 工具链 | 模型谱系/transformers/peft | 模型选型 |
| 38 | 分词与数据准备 | chat template/指令格式 | 构建微调数据集 |
| 39 | LoRA/QLoRA | 低秩分解/`LoraConfig` | LoRA 入门 |
| 40 | 训练实操 | `Trainer`/`TrainingArguments` | 微调对话模型 |
| 41 | RLHF/DPO 基础 | 奖励模型/PPO/DPO 概念 | 对齐论文精读 |
| 42 | 评测 | 困惑度/人工评测/`evaluate` | 模型评测 |
| 43 | 部署 | 量化/GGUF/Ollama 推理 | Ollama 部署 |

### Module 5: Web 爬虫(Day 42-48)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 44 | HTTP+requests | 方法/头/状态码/`Session` | 基础爬虫 |
| 45 | HTML 解析+正则 | BeautifulSoup/CSS 选择器/`re` | 结构化数据提取 |
| 46 | 动态页面 | Playwright 无头浏览器 | 动态网站爬取 |
| 47 | Scrapy | spider/item/pipeline | 全站爬取 |
| 48 | API+反爬 | REST API/认证/限速/代理 | 大规模数据采集 |
| 49 | 数据存储+并发 | SQLite/`asyncio`/`aiohttp` | 万级数据采集 |
| 50 | **爬虫项目日** | 综合 | 为 AI 应用构建数据集 |

### Module 6: AI 应用开发(Day 49-58)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 51 | 环境管理+FastAPI | venv/`requirements`/`FastAPI` 路由 | API 服务骨架 |
| 52 | LLM API+Prompt 工程 | OpenAI SDK/流式调用/CoT | AI 对话 API |
| 53 | Embedding+向量检索 | 嵌入模型/FAISS/Chroma | 向量知识库 |
| 54 | RAG 全流程 | 分块/检索/重排名/生成 | 文档问答系统 |
| 55 | Agent 框架 | LangChain/LlamaIndex 工具调用 | Agent 实战 |
| 56 | UI+Docker | Streamlit/`Dockerfile` | 应用容器化 |
| 57 | 部署+监控 | 云平台/健康检查 | 上线部署 |
| 56 | **选题+开发启动** | 4 方向选 1 | 作品开发 |
| 57 | **作品冲刺** | 开发+文档 | 作品开发 |
| 58 | **期末答辩** | Demo+问答+互评 | 答辩评审 |

---

## 8. 阶段复习与测验

### Day 10: 阶段复习①(Python 核心)

| 时段 | 内容 |
|---|---|
| 第 1-3 节 | Day01-09 当堂练重做(挑选暴露高错的题目) |
| 第 4-5 节 | **购物车中型项目(函数+OOP 版)** |
| 第 6 节 | 阶段测验(可选) + 错题串讲 |

**验收点**:购物车完整可跑(商品列表/菜单循环/购物车累加/结算/函数封装)

### Day 17: 阶段复习②(数据处理)

| 时段 | 内容 |
|---|---|
| 第 1-4 节 | NumPy/Pandas/Matplotlib 实战综合题 |
| 第 5-6 节 | **EDA 综合项目**(真实数据集:泰坦尼克/California Housing) |

**验收点**:数据清洗→可视化→洞察,提交 EDA 分析报告

### Day 40: 阶段复习③(ML+DL)

| 时段 | 内容 |
|---|---|
| 第 1-3 节 | ML vs DL 对比讨论 + 综合建模题 |
| 第 4-6 节 | CIFAR-10 图像分类器实战 |

**验收点**:DL vs ML 对比报告 + 分类器可运行

---

## 9. 期末作品

### 9.1 四选一方向(Day 56-58)

| 方向 | 作品示例 | 串联 Domain | 难度 |
|---|---|---|---|
| **AI 应用** | RAG+Agent 智能助手 / Multi-Agent 协作系统 | H+F+E+G | ⭐⭐⭐⭐⭐ |
| **LLM 微调** | 垂直领域客服模型(爬取领域数据→LoRA 微调→部署) | F+E+G+B | ⭐⭐⭐⭐ |
| **数据+爬虫** | 大规模数据采集与分析平台 | G+B+C | ⭐⭐⭐⭐ |
| **ML 工程** | 端到端预测系统(数据→训练→评估→API 服务→部署) | C+D+B+H | ⭐⭐⭐⭐⭐ |

### 9.2 时间安排

| Day | 任务 | 产出 |
|---|---|---|
| Day 56 | 选题 + 开发启动(确定方向/技术栈/搭建脚手架) | 项目计划 + 代码骨架 |
| Day 57 | 作品冲刺(开发+测试+文档) | 完整可运行代码 + README |
| Day 58 | 期末答辩(Demo 演示 5' + 问答 5' + 互评) | Demo + 答辩记录 |

### 9.3 评分标准

| 项 | 权重 | 说明 |
|---|---|---|
| 功能完整性 | 30% | 核心功能全部实现,无明显 bug |
| 技术深度 | 30% | 技术选型合理,代码结构清晰,有工程思考 |
| 演示表达 | 20% | Demo 流畅,能清晰讲解架构和亮点 |
| 文档质量 | 20% | README 完整(安装/运行/架构/亮点/踩坑) |

> 📋 详细评分细则见 `course/lesson58/FINAL_PROJECT_RUBRIC.md`

### 9.4 每个方向提供的脚手架

| 方向 | 脚手架内容 |
|---|---|
| AI 应用 | FastAPI + LangChain + Chroma + Streamlit 项目模板 |
| LLM 微调 | Hugging Face + LoRA(PEFT) + Ollama 推理模板 |
| 数据+爬虫 | Scrapy + Pandas + Matplotlib 数据采集管线模板 |
| ML 工程 | sklearn Pipeline + FastAPI + Docker 服务化模板 |

---

## 10. 常见问题 FAQ

### 10.1 安装与环境

| 问题 | 解答 |
|---|---|
| Windows 还是 Mac? | 都支持,命令可能略有不同(Windows 用 `python` 而非 `python3`) |
| 需要 GPU 吗? | Module 0-3 不需要 GPU;Module 4-6 建议有 GPU(或用 Colab 云端) |
| Jupyter 启动后浏览器没打开? | 手动在浏览器输入终端显示的 URL(通常 `http://localhost:8888`) |
| `pip` 报错找不到命令? | 用 `python3 -m pip install xxx` 替代 |

### 10.2 学习过程

| 问题 | 解答 |
|---|---|
| Day 1 都听不懂? | 先看书/视频补基础概念(推荐 CS50P Week 0 或 B 站 Python 入门) |
| 代码报错看不懂? | 读 Traceback 最后一行 → 复制错误信息搜索 → 检查冒号/缩进/括号/中英文符号 |
| 当堂练做不完? | 标记"未完成",课后继续做(把进度记在 homework/TODO.md) |
| 想跳过 Module 0? | 如果你已掌握 Python 基础(变量/函数/OOP/文件),可从 Day 17 开始 |
| 每天 6 小时太多? | 可调整为 2-3 小时/天,延长总周期至 4-6 个月 |

### 10.3 项目与评估

| 问题 | 解答 |
|---|---|
| 期末作品必须组队吗? | 可单人也可组队(建议 1-3 人),组队时需明确分工 |
| 期末作品能参考开源吗? | 可以,但 README 需写明"自己的亮点"(改了什么/加了什么/解决了什么) |
| 阶段测不及格怎么办? | 找老师/同学补漏,回顾对应 Day 的 slides 和 notebook,重做当堂练 |

### 10.4 深度学习/LLM 环境

| 问题 | 解答 |
|---|---|
| 微调 LLM 需要什么显卡? | 7B 模型 LoRA 微调:RTX 3060(12GB)起步;QLoRA 可在 RTX 3060 跑 |
| 没有独显怎么办? | 用 Google Colab(T4 GPU,免费)或 AutoDL/恒源云(租用) |
| transformers 库安装失败? | 先 `pip install torch`,再 `pip install transformers`(PyTorch 是前置) |

---

## 11. 参考资料

### 11.1 课程内部文档

| 文档 | 用途 | 何时读 |
|---|---|---|
| `README.md` | 课程主文档(目标/流程/评分) | 开课前 |
| `summary.md` | 59 天进度表 + 每天知识点 | 每天课前 |
| `PREREQUISITES.md` | 数学/网络/系统前置知识 | 开课前/遇到不懂时 |
| `references.md` | 14 门课程对比 + 100+ 习题素材池 | 备课/选题时 |
| `CLAUDE.md` | AI 开发助手操作指南 | 用 Claude Code 辅助开发时 |

### 11.2 推荐外部资源

| 资源 | 链接 | 覆盖模块 |
|---|---|---|
| CS50P (Harvard) | https://cs50.harvard.edu/python/ | Module 0-1 |
| Kaggle Learn | https://www.kaggle.com/learn | Module 1, 3 |
| fast.ai | https://course.fast.ai/ | Module 2, 3 |
| Hugging Face NLP Course | https://huggingface.co/learn/nlp-course | Module 3-4 |
| Scrapy 官方文档 | https://docs.scrapy.org/ | Module 5 |
| FastAPI 官方文档 | https://fastapi.tiangolo.com/ | Module 6 |
| 3Blue1Brown | https://www.youtube.com/c/3blue1brown | 数学基础 |

### 11.3 求助渠道

| 问题类型 | 求助渠道 |
|---|---|
| 课程内容问题 | 课程教师 / 同学讨论 |
| Python 语法问题 | Stack Overflow / CSDN / 知乎 |
| 环境安装问题 | 搜索引擎报错信息 + GitHub Issues |
| LLM 微调问题 | Hugging Face Forums / r/LocalLLaMA |
| 爬虫反爬问题 | Scrapy GitHub Issues / 爬虫社区 |

---

## 12. 学习断层与修复

> 在 59 天课程研发过程中,我们梳理出 **6 个 P0 级学习断层**——这些是学员从"听懂"到"能干"之间最容易掉进去的坑。每个断层都附带了修复策略,落地到具体 Day 的具体课时。完整详情见 [`dev/learning-gaps.md`](dev/learning-gaps.md)。

### 12.1 P0 断层清单

| # | 断层名称 | 出现位置 | 断层表现 | 修复策略 | 状态 |
|---|---|---|---|---|---|
| P0-1 | **第三方库入门缺失** | Day 10 | 前 9 天从未教过"第三方库"概念,Day10 一上来就 `import numpy`,遇到 `ModuleNotFoundError` 无从排查 | Day10 slides.md 开头插入 10 分钟"第三方库入门"微课(pip install / import ... as / from ... import) | ✅ 已修复 |
| P0-2/3 | **sklearn 标准 workflow 缺失** | Day 17 | Day17 直接调 `train_test_split` / `fit` / `predict`,但学员从未见过这个固定套路,无法建立 ML 工作流心智模型 | Day17 slides.md 开头插入半日"sklearn 标准 workflow"微课(6 步套路 + 动手) | ✅ 已修复 |
| P0-4 | **数学基础(偏导数+链式法则)缺失** | Day 25 | Day25 直接讲链式法则 / 矩阵求导,学员看到 `∂L/∂w` 完全陌生,反向传播推导无法跟进 | Day25 slides.md 开头插入 15 分钟"偏导数 + 链式法则"速学 | ✅ 已修复 |
| P0-5 | **强化学习术语缺失** | Day 40 | Day40 假设学员懂 RLHF / DPO / PPO / Reward Model,但从未教过,学员面对缩写词堆砌无法理解动机 | Day40 slides.md 开头插入 15 分钟"RL 极简入门(驯狗类比)"微课 | 🔄 修复中 |
| P0-6 | **异步编程极简入门缺失** | Day 48 | Day48 把 `asyncio` / `aiohttp` / `threading` / SQL 四领域挤进一天,学员信息过载 | Day48 slides.md 开头插入 20 分钟"异步编程极简入门"微课(同步 vs 异步类比 + asyncio 三件套) | 🔄 修复中 |

### 12.2 修复原则

每个 P0 断层的修复都遵循三件套:

1. **可视化类比** — 把新概念映射到学员已熟悉的结构(如"参数是带名字的变量")
2. **对比练习** — 同一任务用新旧两种方式做,辨析适用场景
3. **错题锚定** — 在 `teacher_notes.md` 预设"本题高频错"位置,教师课后必填

### 12.3 使用说明

- **教师**:备课时扫一眼对应 Day 的断层提醒,课堂上主动踩坑处慢下来
- **学员**:遇到听不懂时,查阅 `dev/learning-gaps.md` 中对应断层的"自检问题"
- **课程维护者**:每个断层都有"修复状态"标签,迭代时优先处理 🔄 和 📋 项

> 📖 完整断层详情、自检题目、修复验证数据见 [`dev/learning-gaps.md`](dev/learning-gaps.md)

---

> **本文件结束**
> 配套课程: [59 天 AI 就绪 Python 工程师](https://github.com/chaoshou-coder/Lec.Python)
> 反馈/建议: 在 GitHub 提 Issue 或在课程中反馈给教师
