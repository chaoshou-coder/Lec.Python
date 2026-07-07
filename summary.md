# Python 零基入门到 OOP + 小项目 · 21 天教学计划(重构版 v2)

> 计划作者: Claude
> 适用对象: 成年零基础(转行 / NIT / 兴趣驱动)
> 节奏: 周一到周五,每天 6 小时(约 6 节 × 45 分钟)
> 前置要求: 能打字,会用鼠标,知道"文件 / 目录"概念
> 最终作品: OOP 图书管理系统 v2(JSON 持久化 / CSV 导出 / 异常)
> 与旧课件关系: 保留 day01-day07 完全不动;本计划独立存于 `重构计划/`,内容按新顺序重排

---

## 目录结构

```
重构计划/
├── summary.md                     ← 本文件:总览
├── README.md                      ← 教师使用指南
├── references.md                  ← 外部成熟课程参考(由 side-agent 并行搜集)
├── lesson01/ ~ lesson21/          ← 21 个标准课时目录
│   ├── README.md                  ← 每课概览(主题 / 习题 / 项目)
│   ├── slides.md                  ← 教师讲义
│   ├── demo/                      ← 演示脚本(每个文件对应一个细分知识点)
│   ├── in_class/                  ← 当堂练习(学生当场写)
│   ├── homework/                  ← 课后作业(学生回家写)
│   ├── assets/                    ← 素材(xiongmao.txt / data_1.txt 等)
│   ├── mini_project/              ← 每 2~3 天的综合小项目
│   └── teacher_notes.md           ← 教师备忘(高频错 3 件事)
└── weekly_projects/
    ├── week01_shopping_cart/
    ├── week02_library_manager/
    └── week03_book_manager_oop/
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

> 当堂练数量根据 Day 难度调整;阶段复习日(Day07/14/21)调整为 6 节全部做题 + 中型项目。

---

## 60 天总进度

> v2.0.0 重构: 从"Python 零基→OOP"重构为"Python 零基→AI 就绪工程师"。
> 课时分配按优先级: AI 应用(10d) > 爬虫(7d) > LLM(7d) > ML(8d) > DL(6d)。

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
Module 3 (Day 32-43)   NLP+LLM: Attention⚡/Transformer/LoRA 微调
Module 4 (Day 44-50)   爬虫: HTTP/解析/Scrapy/反爬/并发
Module 5 (Day 51-60)   AI 应用: FastAPI/RAG/Agent/部署 ★重点
```

---

## Day01-Day07 原有缺陷修复清单(必须在新 plan 同步落地)

重定向自 plan 内 §1.2 与 §1.3:

### Day01 缺陷
| # | 文件 | 问题 | 修复 |
|---|---|---|---|
| 1 | `04.使用变量来展示一个学生的信息.py` | 注释中混用 `%10d` 与 `f-string` 对齐,学员易混淆 | 新增 3 道对比练习 |
| 2 | `Exam01.py` | 单一测试,题型未覆盖 | 补充 2 道相似习题 |

### Day02 缺陷
| # | 文件 | 问题 | 修复 |
|---|---|---|---|
| 1 | `01.类型案例.py` | `isdigit/isalpha/isalnum` 一笔带过,学员不清楚应用场景 | 补充 3 道验证题 |
| 2 | `04.模拟一个抽奖的程序.py` | 重复了一段几乎完全相同的代码 | 改为循环,正是 Day05 循环课的铺垫题 |
| 3 | `07.for循环.py` | `for _` 教学示例薄弱 | 配 3 道"用 _ 优雅遍历 + 不用 _ 又怎么写"对比题 |
| 4 | `08.案例.py` | 三项统计一次性写,无梯度 | 变为 3 小题各 5 分钟 |

### Day03 缺陷
| # | 文件 | 问题 | 修复 |
|---|---|---|---|
| 1 | `01.循环的应用.py` | 最值排位法+循环嵌套同时出现 | 先讲单循环求最值;下节再讲嵌套 |
| 2 | `04.菜单选择.py` | `while 1:` 从未讲过 | 在 Day05 循环课先讲思路 |
| 3 | `05.print函数的详解.py` | `open('w')` 讲了,`open('r')` 跳了,`with … as` 两行 | 同一天 05 文件后追加"读 + with"小节 |
| 4 | `06/07 嵌套循环` | 鸡兔同笼 + 菱形打印 + 等腰三角形同一天爆 | 镶嵌到 Day05 + Day06 分讲 |
| 5 | `tt.py` + `data.txt` | `encoding='gbk'` 却无讲解 | Day03 讲 open 时追加 2 分钟"编码" |

### Day04 缺陷
| # | 文件 | 问题 | 修复 |
|---|---|---|---|
| 1 | `04.列表的增加操作.py` | `insert(50,200)` 无注释 | 加一行 `# 故意越界,观察会怎样` |
| 2 | `06.列表的修改和删除.py` | 嵌套 `stus[j][2] = sex` 突然用 | 补 2 道"一维 → 二维"桥梁题 |
| 3 | `09.深拷贝和浅拷贝.py` | `c[2].append(50)` 是 Bug,`c[2]` 是整数,会报 `AttributeError` | 修成 `c[3].append(50)` |
| 4 | `10.综合案例.py` | 80 行一次写完,无梯度 | V3 plan 拆成 5 步搭脚手架 |
| 5 | `字符串练习.py` | `.title()` Day03 从未讲 | 在 Day08 提升课时补讲 |

---

## 验收点

### 阶段测
- Day07: 小组项目"购物车"完整可跑
- Day14: Day08-Day13 函数综合应用题 ≥ 70% 正确率
- Day21: OOP 图书管理系统 v2 走通 7 项功能

### 期末作品
- 控制台图书管理系统 v2 必须过 7 项验收点
- Demo 录像 3 分钟
- 作品 README 写明"自己的亮点"

---

## 每日交付节奏

- **当日上午**:教师按 `slides.md` + `demo/` 讲,学员用 `in_class/` 练习
- **当日下午**:继续讲 + 小项目 + 测验
- **教师课后**:更新 `teacher_notes.md`(错 3 件事)
- **学生课后**:做 `homework/`,次日课前 10 分钟复盘
- **每周五**:下一周周一之前,教师把 `lessonXX+1 ~ lessonXX+5` 全部文件扫一遍,确认题目跑得通

---

## 配合本计划的其他资源

- 旧课件 day01-day07 参考源码路径:`../day01/`(相对于本目录的父目录) ~ `../day07_code/`
- 市场课程素材库:`references.md`
- 21 天详细 plan 本体:`day7-day7-os-glowing-crystal.md`(通常在 `~/.claude/plans/`)
