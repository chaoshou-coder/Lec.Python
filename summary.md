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
├── course/lesson01/ ~ course/lesson06/          ← 60 个标准课时目录
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

## 63 天总进度

> v2.1.0(2026-07-09): Day01-04 压缩为 1 天,Module 0 扩展 OOP 为 3 天(封装/继承/抽象)。总课程 60→63 天。
> 课时分配按优先级: AI 应用(10d) > 爬虫(7d) > LLM(7d) > ML(8d) > DL(6d)。
> 非 Python 知识(数学/网络/系统)列为前置,详见 `PREREQUISITES.md`。

### Module 0: Python 核心 + 数据处理(Day 1-17)

| Day | 主题 | 关键新增 | 当堂 / 课后 / 小项目 |
|---|---|---|---|
| 01 | **Python 基础语法** | `print` `input` 变量/字符串切片/f-string/`if-elif-else`/`while`/`for`/`range` | 综合 / 综合 / 🎯 购物车字典版 |
| 02 | 函数入门 | `def` 四种形式 `return` | 6 / 2 / 🎯 工具函数库 |
| 03 | 列表与字典 | CRUD:`append`/`pop`/`items()`/推导式 | 6 / 2 / 🎯 通讯录 v1 |
| 04 | 文件 I/O + 异常 | `with`/`JSON`/`try`-`except` | 5 / 2 / 🎯 日记本持久化 |
| 05 | **OOP 封装** | `class`/`__init__`/`self`/`@property`/`__str__` | 6 / 2 / 🎯 Student 类 |
| 06 | **OOP 继承** | 单继承/`super()`/方法重写/多态/`isinstance` | 6 / 2 / 🎯 动物继承体系 |
| 07 | **OOP 抽象** | `abc.ABC`/`@abstractmethod`/接口/魔术方法 | 6 / 2 / 🎯 形状面积计算器 |
| 08 | 模块与高级特性 | 包/生成器/装饰器/`import` | 6 / 3 /  |
| 09 | **阶段复习①** | Day01-08 综合 | 综合 / 综合 / 🌟 购物车(函数+OOP 版) |
| 10 | NumPy 基础 | 数组/广播/向量化 | 6 / 3 / 🎯 矩阵运算 |
| 11 | NumPy 进阶 | 线性代数/随机数/统计 | 6 / 3 /  |
| 12 | Pandas 基础 | Series/DataFrame/索引/过滤 | 6 / 3 / 🎯 数据探索 |
| 13 | Pandas 进阶 | 分组/合并/透视/清洗 | 6 / 3 /  |
| 14 | 数据可视化 | 折线/柱状/散点/热力图 | 6 / 2 / 🎯 数据报告配图 |
| 15 | 数据摄取 | CSV/JSON/Excel/SQL/API | 5 / 2 / 🎯 多源数据整合 |
| 16 | **阶段复习②(EDA 项目)** | Module 0 综合 | 综合 / 综合 / 🌟 EDA 分析报告 |
| 17 | 阶段缓冲/复习 | 薄弱点回练/项目完善 | - / - /  |

### Module 1: 机器学习(Day 18-24)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 18 | ML 概念与工作流 | 监督/无监督/过拟合/`train_test_split` | 手写数字探索 |
| 19 | 数据预处理 | 缩放/编码/缺失值/`ColumnTransformer` | 数据集清洗 |
| 20 | 线性回归+梯度下降 | MSE/SGD 直觉 | 房价预测 |
| 21 | 逻辑回归+树模型 | Sigmoid/决策树/随机森林 | 泰坦尼克预测 |
| 22 | 梯度提升+SVM | XGBoost 残差拟合/核技巧直觉 | Kaggle 入门赛 |
| 23 | 聚类+降维 | K-Means/PCA/t-SNE | 客户分群 |
| 24 | 模型评估+流水线 | ROC-AUC/交叉验证/`Pipeline`/`GridSearchCV` | 多模型对比 |

### Module 2: 深度学习(Day 25-30)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 25 | 神经网络基础 | 感知机/激活函数/前向传播 | 手写感知机 |
| 26 | **反向传播⚡深入** | 链式法则/SGD/Adam | 手动 BP 实现 |
| 27 | PyTorch 基础 | tensor/autograd/`nn.Module`/`DataLoader` | NumPy→PyTorch |
| 28 | 训练循环 | optimizer/loss/epoch/验证 | MNIST 训练 |
| 29 | CNN+RNN+正则化 | 卷积/池化/LSTM/Dropout | 图像分类器 |
| 30 | 迁移学习+DL 项目 | 预训练/冻结/微调 | CIFAR-10 |

### Module 3: NLP 与 Transformer(Day 31-35)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 31 | 文本预处理+表示 | 分词/BoW/TF-IDF/词嵌入 | 文档相似度 |
| 32 | 序列模型 for text | RNN/LSTM | 字符级文本生成 |
| 33 | **注意力机制⚡深入** | Q/K/V/缩放点积/多头注意力 | 手动 attention |
| 34 | Transformer+预训练模型 | BERT/GPT/T5 架构选型 | Transformer 解剖 |
| 35 | Hugging Face 实战 | `pipeline`/`AutoModel`/`Tokenizer` | 情感分析 |

### Module 4: LLM 微调(Day 36-42)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 36 | LLM 生态+HF 工具链 | 模型谱系/transformers/peft | 模型选型 |
| 37 | 分词与数据准备 | chat template/指令格式 | 构建微调数据集 |
| 38 | LoRA/QLoRA | 低秩分解/`LoraConfig` | LoRA 入门 |
| 39 | 训练实操 | `Trainer`/`TrainingArguments` | 微调对话模型 |
| 40 | RLHF/DPO 基础 | 奖励模型/PPO/DPO 概念 | 对齐论文精读 |
| 41 | 评测 | 困惑度/人工评测/`evaluate` | 模型评测 |
| 42 | 部署 | 量化/GGUF/Ollama 推理 | Ollama 部署 |

### Module 5: Web 爬虫(Day 43-49)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 43 | HTTP+requests | 方法/头/状态码/`Session` | 基础爬虫 |
| 44 | HTML 解析+正则 | BeautifulSoup/CSS 选择器/`re` | 结构化数据提取 |
| 45 | 动态页面 | Playwright 无头浏览器 | 动态网站爬取 |
| 46 | Scrapy | spider/item/pipeline | 全站爬取 |
| 47 | API+反爬 | REST API/认证/限速/代理 | 大规模数据采集 |
| 48 | 数据存储+并发 | SQLite/`asyncio`/`aiohttp` | 万级数据采集 |

### Module 6: AI 应用开发(Day 50-59)

| Day | 主题 | 关键新增 | 项目 |
|---|---|---|---|
| 50 | 环境管理+FastAPI | venv/`requirements`/`FastAPI` 路由 | API 服务骨架 |
| 51 | LLM API+Prompt 工程 | OpenAI SDK/流式调用/CoT | AI 对话 API |
| 52 | Embedding+向量检索 | 嵌入模型/FAISS/Chroma | 向量知识库 |
| 53 | RAG 全流程 | 分块/检索/重排序/生成 | 文档问答系统 |
| 54 | Agent 框架 | LangChain/LlamaIndex 工具调用 | Agent 实战 |
| 55 | UI+Docker | Streamlit/`Dockerfile` | 应用容器化 |
| 56 | 部署+监控 | 云平台/健康检查 | 上线部署 |
| 57 | **选题+开发启动** | 4 方向选 1 | 作品开发 |
| 58 | **作品冲刺** | 开发+文档 | 作品开发 |
| 59 | **期末答辩** | Demo+问答+互评 | 答辩评审 |

---

## 六年段"知识闭环图"(需要逐 Day 形成笔记)

```
Module 0 (Day 1-17)    Python 核心 + 数据基础: 变量/函数/OOP(3d)/NumPy/Pandas
Module 1 (Day 18-24)   机器学习: 监督/无监督/评估/流水线
Module 2 (Day 25-30)   深度学习: NN/BP⚡/PyTorch/CNN/RNN
Module 3 (Day 31-35)   NLP 与 Transformer: Attention⚡/BERT/GPT/HF 实战
Module 4 (Day 36-42)   LLM 微调: LoRA/训练/评测/部署
Module 5 (Day 43-49)   爬虫: HTTP/解析/Scrapy/反爬/并发
Module 6 (Day 50-59)   AI 应用: FastAPI/RAG/Agent/部署 ★重点
```

---

## 验收点

### 阶段测
- Day 09: 购物车项目(函数+OOP 版)完整可跑
- Day 16: EDA 项目(数据清洗+可视化+洞察)交付
- Day 24: ML 端到端项目(Kaggle 竞赛/California Housing 预测)
- Day 39: DL vs ML 对比报告 + CIFAR-10 分类器

### 期末作品(Day 57-59 四选一)
- **AI 应用方向**: RAG+Agent 智能助手完整可跑
- **LLM 微调方向**: 垂直领域模型微调→评测→部署
- **数据+爬虫方向**: 大规模数据采集→清洗→分析平台
- **ML 工程方向**: 端到端预测系统→API 服务→部署

评审标准(见 `course/lesson59/FINAL_PROJECT_RUBRIC.md`):
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
