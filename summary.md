# Python 零基入门到 AI 就绪工程师 · 60 天教学计划 v2.0.0

> 计划作者: Claude
> 适用对象: 成年零基础(转行 / NIT / 兴趣驱动)
> 节奏: 周一到周五,每天 6 小时(约 6 节 × 45 分钟)
> 前置要求: 能打字,会用鼠标,知道"文件 / 目录"概念(详见 `PREREQUISITES.md`)
> 终点能力: 机器学习 / LLM 微调 / Web 爬虫 / AI 应用开发
> 期末作品: 四选一(AI 应用 / LLM 微调 / 数据爬虫 / ML 工程)

---

## 目录结构

```
Lec.Python/
├── summary.md                     ← 本文件:60 天总进度
├── README.md                      ← 教师使用指南
├── CLAUDE.md                      ← AI 开发助手指南
├── PREREQUISITES.md               ← 数学/网络/系统前置知识
├── references.md                  ← 外部成熟课程参考(14 门课程对比 + 100+ 习题素材池)
├── lesson01/ ~ lesson06/          ← 60 个标准课时目录
│   ├── README.md                  ← 每课概览(主题 / 习题 / 项目)
│   ├── slides.md                  ← 教师讲义
│   ├── demo/                      ← 演示脚本
│   ├── in_class/                  ← 当堂练习(标注 当堂练/选做)
│   ├── homework/                  ← 课后作业(选做)
│   ├── assets/                    ← 素材
│   ├── mini_project/              ← 每 2~3 天的综合小项目
│   └── teacher_notes.md           ← 教师备忘(高频错 3 件事)
├── weekly_projects/
│   ├── week01_shopping_cart/      ← Day 10 阶段复习项目
│   ├── week02_library_manager/
│   └── week03_book_manager_oop/
└── dev/
    ├── module0-mapping.md         ← 新 Day → 旧 lesson 习题映射
    └── plans/                     ← 备份
```

---

## 每日 6 课时(360 分钟)节奏建议

| 节次 | 时长 | 名称 | 内容 |
|---|---|---|---|
| 第 1 节 | 45' | 复习 + 引入 | 抽问(5') + 赏 demo(5') + 第一讲(15') + 当堂练 1×2(20') |
| 第 2 节 | 45' | 第二讲 + 练 | 第二讲(15') + 当堂练 2×2(25') + 小结(5') |
| 第 3 节 | 45' | 第三讲 + 练 | 第三讲(15') + 当堂练 3×2(25') + 小结(5') |
| 第 4 节 | 45' | 小项目(若本日有) | 巡场 + 展示优秀作品 |
| 午休 | 60' |  |  |
| 第 5 节 | 45' | 小项目延续 / 第四讲 | 若 Day 无小项目,改为第四讲 |
| 第 6 节 | 45' | 总结 + 测验 + 作业布置 | 教师总结(5') + 错题本(5') + 闭卷小测(10') + 作业说明(5') + 自由问答(20') |

> 当堂练数量根据 Day 难度调整;阶段复习日(Day10/17/40)调整为 6 节全部做题 + 综合项目,期末答辩(Day60)为 Demo+问答+互评。

---

## 60 天总进度

> v2.0.0: 从"Python 零基→OOP"重构为"Python 零基→AI 就绪工程师"。
> 课时分配按优先级: AI 应用(10d) > 爬虫(7d) > LLM(7d) > ML(8d) > DL(6d)。
> 非 Python 知识(数学/网络/系统)列为前置,详见 `PREREQUISITES.md`。

### Module 0: Python 核心 + 数据处理(Day 1-17)

| Day | 主题 | 关键新增 | 当堂 / 课后 / 小项目 |
|---|---|---|---|
| 01 | Python 与开发环境 | `print` `input` `type` 变量 | 4 / 2 / 🎯 自我介绍 |
| 02 | 字符串与格式化 | f-string/切片/`isdigit` | 5 / 2 / 🎯 手机号脱敏 |
| 03 | 条件分支 | `if/elif/else` 嵌套、逻辑组合 | 6 / 3 / 🎯 BMI 计算器 |
| 04 | 循环入门 | `while` `for` `range` 累加/累乘 | 6 / 3 / 🌟 每日记账本 |
| 05 | 函数入门 | `def` 四种形式 `return` | 6 / 2 / 🎯 工具函数库 |
| 06 | 列表与字典 | CRUD:`append`/`pop`/`items()` | 6 / 2 / 🎯 通讯录 v1 |
| 07 | 文件 I/O + 异常 | `with`/`JSON`/`try`-`except` | 5 / 2 / 🎯 日记本持久化 |
| 08 | OOP 基础 | `class`/`__init__`/`@property` | 6 / 2 / 🎯 Student 类 |
| 09 | 模块与高级特性 | 包/生成器/装饰器/`import` | 6 / 3 /  |
| 10 | **阶段复习①** | Day01-09 综合 | 综合 / 综合 / 🌟 购物车(函数+OOP 版) |
| 11 | NumPy 基础 | 数组/广播/向量化 | 6 / 3 / 🎯 矩阵运算 |
| 12 | NumPy 进阶 | 线性代数/随机数/统计 | 6 / 3 /  |
| 13 | Pandas 基础 | Series/DataFrame/索引/过滤 | 6 / 3 / 🎯 数据探索 |
| 14 | Pandas 进阶 | 分组/合并/透视/清洗 | 6 / 3 /  |
| 15 | 数据可视化 | 折线/柱状/散点/热力图 | 6 / 2 / 🎯 数据报告配图 |
| 16 | 数据摄取 | CSV/JSON/Excel/SQL/API | 5 / 2 / 🎯 多源数据整合 |
| 17 | **阶段复习②(EDA 项目)** | Module 0 综合 | 综合 / 综合 / 🌟 EDA 分析报告 |

### Module 1: 机器学习(Day 18-25)

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

### Module 2: 深度学习(Day 26-31)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 26 | 神经网络基础 | 感知机/激活函数/前向传播 | 手写感知机 |
| 27 | **反向传播⚡深入** | 链式法则/SGD/Adam | 手动 BP 实现 |
| 28 | PyTorch 基础 | tensor/autograd/`nn.Module`/`DataLoader` | NumPy→PyTorch |
| 29 | 训练循环 | optimizer/loss/epoch/验证 | MNIST 训练 |
| 30 | CNN+RNN+正则化 | 卷积/池化/LSTM/Dropout | 图像分类器 |
| 31 | 迁移学习+DL 项目 | 预训练/冻结/微调 | CIFAR-10 |

### Module 3: NLP 与 Transformer(Day 32-36)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 32 | 文本预处理+表示 | 分词/BoW/TF-IDF/词嵌入 | 文档相似度 |
| 33 | 序列模型 for text | RNN/LSTM | 字符级文本生成 |
| 34 | **注意力机制⚡深入** | Q/K/V/缩放点积/多头注意力 | 手动 attention |
| 35 | Transformer+预训练模型 | BERT/GPT/T5 架构选型 | Transformer 解剖 |
| 36 | Hugging Face 实战 | `pipeline`/`AutoModel`/`Tokenizer` | 情感分析 |

### Module 4: LLM 微调(Day 37-43)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 37 | LLM 生态+HF 工具链 | 模型谱系/transformers/peft | 模型选型 |
| 38 | 分词与数据准备 | chat template/指令格式 | 构建微调数据集 |
| 39 | LoRA/QLoRA | 低秩分解/`LoraConfig` | LoRA 入门 |
| 40 | 训练实操 | `Trainer`/`TrainingArguments` | 微调对话模型 |
| 41 | RLHF/DPO 基础 | 奖励模型/PPO/DPO 概念 | 对齐论文精读 |
| 42 | 评测 | 困惑度/人工评测/`evaluate` | 模型评测 |
| 43 | 部署 | 量化/GGUF/Ollama 推理 | Ollama 部署 |

### Module 5: Web 爬虫(Day 44-50)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 44 | HTTP+requests | 方法/头/状态码/`Session` | 基础爬虫 |
| 45 | HTML 解析+正则 | BeautifulSoup/CSS 选择器/`re` | 结构化数据提取 |
| 46 | 动态页面 | Playwright 无头浏览器 | 动态网站爬取 |
| 47 | Scrapy | spider/item/pipeline | 全站爬取 |
| 48 | API+反爬 | REST API/认证/限速/代理 | 大规模数据采集 |
| 49 | 数据存储+并发 | SQLite/`asyncio`/`aiohttp` | 万级数据采集 |
| 50 | **爬虫项目日** | 综合 | 为 AI 应用构建数据集 |

### Module 6: AI 应用开发(Day 51-60)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 51 | 环境管理+FastAPI | venv/`requirements`/`FastAPI` 路由 | API 服务骨架 |
| 52 | LLM API+Prompt 工程 | OpenAI SDK/流式调用/CoT | AI 对话 API |
| 53 | Embedding+向量检索 | 嵌入模型/FAISS/Chroma | 向量知识库 |
| 54 | RAG 全流程 | 分块/检索/重排序/生成 | 文档问答系统 |
| 55 | Agent 框架 | LangChain/LlamaIndex 工具调用 | Agent 实战 |
| 56 | UI+Docker | Streamlit/`Dockerfile` | 应用容器化 |
| 57 | 部署+监控 | 云平台/健康检查 | 上线部署 |
| 58 | **选题+开发启动** | 4 方向选 1 | 作品开发 |
| 59 | **作品冲刺** | 开发+文档 | 作品开发 |
| 60 | **期末答辩** | Demo+问答+互评 | 答辩评审 |

---

## 六年段"知识闭环图"(需要逐 Day 形成笔记)

```
Module 0 (Day 1-17)    Python 核心 + 数据基础: 变量/函数/OOP/NumPy/Pandas
Module 1 (Day 18-25)   机器学习: 监督/无监督/评估/流水线
Module 2 (Day 26-31)   深度学习: NN/BP⚡/PyTorch/CNN/RNN
Module 3 (Day 32-36)   NLP 与 Transformer: Attention⚡/BERT/GPT/HF 实战
Module 4 (Day 37-43)   LLM 微调: LoRA/训练/评测/部署
Module 5 (Day 44-50)   爬虫: HTTP/解析/Scrapy/反爬/并发
Module 6 (Day 51-60)   AI 应用: FastAPI/RAG/Agent/部署 ★重点
```

---

## 验收点

### 阶段测
- Day 10: 购物车项目(函数+OOP 版)完整可跑
- Day 17: EDA 项目(数据清洗+可视化+洞察)交付
- Day 25: ML 端到端项目(Kaggle 竞赛/California Housing 预测)
- Day 40: DL vs ML 对比报告 + CIFAR-10 分类器

### 期末作品(Day 58-60 四选一)
- **AI 应用方向**: RAG+Agent 智能助手完整可跑
- **LLM 微调方向**: 垂直领域模型微调→评测→部署
- **数据+爬虫方向**: 大规模数据采集→清洗→分析平台
- **ML 工程方向**: 端到端预测系统→API 服务→部署

评审标准(见 `lesson60/FINAL_PROJECT_RUBRIC.md`):
- 功能完整性(30%) + 技术深度(30%) + 演示表达(20%) + 文档质量(20%)

---

## 每日交付节奏

- **当日上午**:教师按 `slides.md` + `demo/` 讲,学员用 `in_class/` 练习
- **当日下午**:继续讲 + 小项目 + 测验
- **教师课后**:更新 `teacher_notes.md`(错 3 件事)
- **学生课后**:做 `homework/`,次日课前 10 分钟复盘
- **每周五**:下一周周一之前,教师把 `lessonXX+1 ~ lessonXX+5` 全部文件扫一遍,确认题目跑得通

---

## 配合本计划的其他资源

- `references.md`: 外部成熟课程参考(14 门课程 / 100+ 习题 / 25 项教学红线)
- `PREREQUISITES.md`: 数学(线代/微积分/概统) / 网络 / 系统 前置知识完整清单
- `CLAUDE.md`: AI 开发助手的项目指南(含 per-Day 语法禁忌 / 版本控制)
- `weekly_projects/`: 3 个中型项目(购物车/图书 v1/图书 v2 OOP)
