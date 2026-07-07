# 前置知识要求(PREREQUISITES)

> 本课程为 **Python 主线** 的 60 天 AI 就绪工程师培养方案。
> 以下知识**不在课程内讲授**,学员需在课前具备或课程进行中同步补足。
> 每项标注「最低要求」:课前掌握 / 可同步学习 / 可课后深入。

---

## 1. 数学基础

### 1.1 线性代数(服务于 NumPy / 深度学习)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| 向量(加减、数乘、模长) | NumPy 数组即向量,DL 中每层输入输出都是向量 | **课前掌握** | 3Blue1Brown "线性代数的本质" Ep1-4 |
| 矩阵(乘法、转置、逆) | 神经网络每层是矩阵乘法,PCA 是矩阵分解 | **课前掌握** | 3Blue1Brown "线性代数的本质" Ep5-9 |
| 点积与投影 | 余弦相似度、注意力机制(Q·K)的核心运算 | **课前掌握** | 3Blue1Brown "点积" |
| 特征值/特征向量(直觉) | PCA 降维的数学基础 | 可同步学习(Module 1 降维前补) | StatQuest "PCA" |

### 1.2 微积分(服务于梯度下降 / 反向传播)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| 导数(变化率、切线) | 梯度 = 多变量导数,反向传播 = 链式求导 | **课前掌握** | 3Blue1Brown "微积分的本质" Ep1-4 |
| 偏导数 | 损失函数对每个参数求偏导 | 可同步学习(Module 2 Day27 前补) | Khan Academy "偏导数" |
| 链式法则 | 反向传播的数学核心 | 可同步学习(Module 2 Day27 前补) | 3Blue1Brown "链式法则" |
| 梯度(多变量导数向量) | 梯度下降 = 沿负梯度方向更新参数 | 可同步学习(Module 2 Day27 前补) | 3Blue1Brown "梯度" |

### 1.3 概率与统计(服务于 ML 模型 / 评估)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| 条件概率 / 贝叶斯定理 | 朴素贝叶斯分类器、贝叶斯优化 | 可同步学习(Module 1 Day18 前补) | StatQuest "贝叶斯定理" |
| 常见分布(正态/二项/均匀) | 数据分布假设、异常值检测 | 可同步学习(Module 1 Day19 前补) | Khan Academy "分布" |
| 均值/方差/标准差 | 数据描述、特征缩放、模型评估 | **课前掌握** | 高中数学 |
| 假设检验/p-value(直觉) | 模型显著性、A/B 测试 | 可课后深入 | StatQuest "p-value" |
| 最大似然估计(直觉) | 损失函数的理论基础(交叉熵/MLE 等价) | 可课后深入 | StatQuest "MLE" |

### 1.4 信息论基础(服务于决策树 / DL)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| 熵(信息量) | 决策树分裂标准(信息增益)、交叉熵损失 | 可同步学习(Module 1 Day22 前补) | StatQuest "Entropy" |
| KL 散度(直觉) | 模型蒸馏、VAE、扩散模型损失 | 可课后深入 | 了解即可 |

---

## 2. 计算机系统

### 2.1 Linux/命令行(服务于环境管理 / 部署)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| 基础命令(`ls`/`cd`/`pwd`/`mkdir`/`rm`) | 课程全程使用命令行操作 | **课前掌握** | Linux Journey "命令行" |
| 文件权限(`chmod`/`chown`) | 部署时配置文件权限 | 可同步学习(Module 6 部署前补) | Linux Journey "权限" |
| 进程管理(`ps`/`top`/`kill`) | 训练任务管理、服务监控 | 可同步学习(Module 6 部署前补) | Linux Journey "进程" |
| SSH 远程登录 | 连接云服务器训练/部署 | 可同步学习(Module 4 LLM 微调前补) | 了解即可 |

### 2.2 网络基础(服务于爬虫 / AI 应用)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| HTTP 协议(请求方法/状态码/Headers) | 爬虫和 API 开发的直接基础 | **课前掌握** | MDN "HTTP 概述" |
| TCP/IP 与 DNS(直觉) | 理解网络请求的底层机制 | 可同步学习(Module 5 Day44 前补) | 了解即可 |
| Cookie / Session | 爬虫登录态维持、反爬应对 | 可同步学习(Module 5 Day49 前补) | MDN "Cookie" |
| REST API 设计(直觉) | AI 应用开发中的 API 调用与构建 | 可同步学习(Module 6 Day51 前补) | MDN "REST" |

### 2.3 数据库基础(服务于数据存储)

| 知识点 | 为什么需要 | 最低要求 | 推荐资源 |
|---|---|---|---|
| 关系型数据库概念(表/行/列/主键) | 数据存储与查询 | 可同步学习(Module 0 Day16 前补) | SQLBolt |
| 基础 SQL(`SELECT`/`WHERE`/`JOIN`/`GROUP BY`) | 数据摄取与清洗 | 可同步学习(Module 0 Day16 前补) | SQLBolt "Interactive Lessons" |
| SQLite(轻量本地数据库) | 爬虫数据存储、小型 AI 应用 | 可同步学习(Module 5 Day50 前补) | Python sqlite3 官方文档 |

---

## 3. 最低要求汇总(课前必须掌握的清单)

学员在 Day 1 之前必须具备以下知识,否则课程无法正常推进:

| 类别 | 必须掌握 | 自测方式 |
|---|---|---|
| 数学 | 向量/矩阵/点积/导数/均值方差 | 能解释"矩阵乘法为什么这样算""导数表示什么" |
| 数学 | 基本代数运算(方程/不等式/函数) | 初中数学水平 |
| 计算机 | 文件/目录概念、会打字、会用鼠标 | 课程前置要求(已有) |
| 计算机 | Linux 基础命令(`ls`/`cd`/`mkdir`) | 能独立创建目录、浏览文件 |
| 网络 | HTTP 基础(GET/POST/状态码 200/404) | 能解释"浏览器访问网页发生了什么" |

---

## 4. 同步学习时间表(与课程模块对齐)

| 课程模块 | 时间 | 需要同步补足的数学/CS 知识 |
|---|---|---|
| Module 0 Day1-10 | 第 1-2 周 | Linux 命令(如未掌握)、SQL 基础 |
| Module 0 Day11-17 | 第 2-3 周 | 线性代数(矩阵/点积)、统计(均值/方差) |
| Module 1 Day18-25 | 第 3-4 周 | 贝叶斯/分布/熵(随对应知识点同步) |
| Module 2 Day26-31 | 第 4-5 周 | 偏导/链式法则/梯度(Day27 前集中补) |
| Module 3 Day32-36 | 第 5-6 周 | 词嵌入的数学直觉(随知识点同步) |
| Module 4 Day37-43 | 第 6-7 周 | SSH/远程登录(LLM 微调需要) |
| Module 5 Day44-50 | 第 7-8 周 | HTTP 进阶/Cookie/SQLite(随知识点同步) |
| Module 6 Day51-60 | 第 8-9 周 | Docker 基础概念(随知识点同步) |

---

## 5. 推荐学习资源(免费+高质量)

| 资源 | 覆盖 | 链接 |
|---|---|---|
| 3Blue1Brown "线性代数的本质" | 线代直觉 | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab |
| 3Blue1Brown "微积分的本质" | 微积分直觉 | https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr |
| 3Blue1Brown "神经网络" | DL 直觉 | https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi |
| StatQuest with Josh Starmer | ML/统计直觉 | https://www.youtube.com/user/joshstarmer |
| Khan Academy | 数学全科 | https://www.khanacademy.org/ |
| Linux Journey | Linux 命令行 | https://linuxjourney.com/ |
| SQLBolt | SQL 交互教程 | https://sqlbolt.com/ |
| MDN Web Docs | HTTP/网络 | https://developer.mozilla.org/zh-CN/docs/Web/HTTP |

---

> **本文件结束**
> 编写原则:只列"为什么需要"+"最低要求"+"哪里学",不展开教学。
> 展开教学是课程内的事(Day18 讲 ML 时按需回顾贝叶斯,不单独开数学课)。
