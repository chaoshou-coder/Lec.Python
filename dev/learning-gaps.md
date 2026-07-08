# 学习断层修复文档

> 课程在 6 个节点出现根本性跳跃（P0 断层），本文档按优先级排序，记录问题描述、影响范围与具体修复建议（含可插入 slides.md 的草稿片段）。

---

## 优先级总览

| 编号 | 断层位置 | 缺口 | 建议微课时长 |
|---|---|---|---|
| P0-1 | Day11 | 第三方库入门 | 10 分钟 |
| P0-2/3 | Day18 | sklearn 标准 workflow | 半日（30 分钟理论 + 实操） |
| P0-4 | Day26 | 数学基础（偏导数 + 链式法则） | 15 分钟 |
| P0-5 | Day41 | 强化学习术语 | 15 分钟 |
| P0-6 | Day49 | 异步编程极简入门 | 20 分钟 |

---

## P0-1: Day11 缺少第三方库入门

### 问题描述

Day11 一上来就 `import numpy as np`，但 Day01–10 从未教过"第三方库"这一概念。学生不知道 `pip install` 是什么、`as` 别名的意义，遇到 `ModuleNotFoundError` 也无从排查。

### 影响范围

Day11–20 全部受影响。所有 `import numpy / pandas / matplotlib` 的练习都建立在未被讲解的前置知识上。

### 修复建议

在 Day11 `slides.md` 开头插入 **10 分钟**"第三方库入门"微课时。可插入的草稿片段（直接追加到 slides.md 顶部）：

```markdown
## 第 0 讲:第三方库入门(10 分钟)

Python 自带的功能是"标准库"。第三方库是别人写好的工具包,
用之前需要先安装。

### 安装

```bash
pip install numpy          # 安装
pip install numpy==1.24    # 安装指定版本
```

### 导入

```python
import numpy                       # 每次都要写全称
import numpy as np                  # 起别名,以后只写 np
from sklearn.linear_model import LinearRegression   # 只导入需要的
```

### 常见报错

```
ModuleNotFoundError: No module named 'numpy'
```

原因:没安装。解决:`pip install numpy`。

### 动手

```bash
pip install python
python -c "import numpy as np; print('ok')"
```

跑通说明环境正常,后面 Day11 的练习才能进行。
```

---

## P0-2/3: Day18 缺少 sklearn 标准 workflow

### 问题描述

Day18 假设学生已掌握 `train_test_split` / `fit` / `predict` / `score` / `LinearRegression`，但这些从未教过。学生直接掉进机器学习 API 的细节，无法建立"标准套路"的心智模型。

### 影响范围

Day18 当天 + 后续所有机器学习练习。

### 修复建议

在 Day18 `slides.md` 开头插入 **半日**"sklearn 标准 workflow"微课时（30 分钟讲解 + 30 分钟动手）。可插入的草稿片段：

```markdown
## 第 0 讲:sklearn 标准 workflow(30 分钟)

不管你以后用 sklearn 的哪个模型,都离不开这个固定套路:

```python
# 1. 准备数据
X = ...  # 特征(二维表格)
y = ...  # 目标(一维序列)

# 2. 切分数据
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# 3. 创建模型
from sklearn.xxx import SomeModel
model = SomeModel()

# 4. 训练(拟合)
model.fit(X_train, y_train)

# 5. 预测
y_pred = model.predict(X_test)

# 6. 评估
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))
```

这个 6 步套路贯穿 Module 1 所有机器学习课。

### 动手:运行一个最简单的线性回归

数据已准备好,请按上面 6 步补全代码:

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# 数据
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# 下面请按 6 步套路补全
...
```

跑通 `mean_squared_error` 接近 0,说明套路已掌握。
```

---

## P0-4: Day26 缺少数学基础

### 问题描述

Day26 直接讲链式法则 / 矩阵求导，但从未教过偏导数。学生看到 `∂L/∂w` 完全陌生，后续反向传播的推导无法跟进。

### 影响范围

Day26 当天及其后所有涉及梯度推导的练习。

### 修复建议

在 Day26 `slides.md` 开头插入 **15 分钟**"偏导数 + 链式法则"速学。可插入的草稿片段：

```markdown
## 第 0 讲:偏导数 + 链式法则(15 分钟)

### 偏导数

多元函数求导时,只对一个变量求导,其余当常数:

```python
# f(x, y) = x² + 3xy
# ∂f/∂x = 2x + 3y   (y 当常数)
# ∂f/∂y = 3x        (x 当常数)
```

### 链式法则

复合函数求导 = 逐层相乘:

```python
# y = f(g(x))
# dy/dx = f'(g(x)) · g'(x)

# 例: y = (2x + 1)²
# 令 u = 2x + 1, y = u²
# dy/dx = 2u · 2 = 4(2x + 1)
```

### 动手

用链式法则验证 `(x³ + 2)²` 的导数,并在 Python 中用数值差分近似验证。
```

---

## P0-5: Day41 缺少强化学习术语

### 问题描述

Day41 假设学生懂 RLHF / DPO / PPO / Reward Model，但这些从未教过。学生面对缩写词堆砌，无法理解强化学习的动机与术语关系。

### 影响范围

Day41 当天 + 后续所有 RL 相关练习。

### 修复建议

在 Day41 `slides.md` 开头插入 **15 分钟**"RL 极简入门（驯狗类比）"微课时。可插入的草稿片段：

```markdown
## 第 0 讲:强化学习极简入门(15 分钟)

### 驯狗类比

- **Agent**(智能体):狗
- **Environment**(环境):你家客厅
- **Action**(动作):坐下、打滚、咬拖鞋
- **Reward**(奖励):听话 +1,咬拖鞋 -1
- **Goal**:最大化累积奖励

### 与 ChatGPT 的对应

| 驯狗 | ChatGPT 对齐 |
|---|---|
| Agent | 语言模型 |
| Action | 生成的下一句话 |
| Reward | 人类打分 |
| Reward Model | 学习"人类打分的规律"的评价器 |
| PPO / DPO | 更新策略的算法 |

### 关键缩写速记

- **RLHF** = 用人类反馈做强化学习
- **PPO** = 一种稳定训练算法
- **DPO** = 不需要 Reward Model 的简化算法

### 一句话

> RLHF = 让模型生成回答 → 人类打分 → 训练 Reward Model → 用 PPO 更新模型。
```

---

## P0-6: Day49 四个领域挤一节

### 问题描述

Day49 把 `asyncio` / `aiohttp` / `threading` / SQL 四个全新领域挤进一天，学生信息过载。虽然 Day49 已是高年级课，但四个独立范式并列仍属根本性跳跃。

### 影响范围

Day49 当天及后续综合项目。

### 修复建议

在 Day49 `slides.md` 开头插入 **20 分钟**"异步编程极简入门"微课时。可插入的草稿片段：

```markdown
## 第 0 讲:异步编程极简入门(20 分钟)

### 同步 vs 异步

- **同步**:排队打饭,前一个人没打好,后一个人等着。
- **异步**:点完单拿号码牌,先去坐着,好了叫你。

### asyncio 三件套

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)       # 模拟等待
    return f"data from {url}"

async def main():
    # 并发执行两个任务,总耗时约 1 秒
    r1, r2 = await asyncio.gather(
        fetch("a.com"),
        fetch("b.com"),
    )
    print(r1, r2)

asyncio.run(main())
```

### 与 threading 的区别

| | threading | asyncio |
|---|---|---|
| 调度 | 操作系统 | 程序员(`await`) |
| 场景 | CPU 密集 / 阻塞 I/O | 大量网络 I/O |

### 动手

把下面同步代码改成异步,观察耗时差异。

```python
# 同步版(约 3 秒)
import time
for i in range(3):
    time.sleep(1)

# 请改成 asyncio 版(约 1 秒)
```
```

---

## 实施建议

1. **先修 P0-1 与 P0-2/3** ——这两个断层最早出现( Day11 / Day18 ),后续所有练习都依赖。
2. **再修 P0-4 与 P0-5** ——数学基础和 RL 术语是进入对应模块的门票。
3. **最后修 P0-6** ——Day49 是综合应用课,前置知识多,异步极简入门能显著降低认知负荷。
4. 每个微课草稿直接复制到对应 `lessonXX/slides.md` 顶部,教师可根据课堂节奏微调。
5. 修复完成后,在 `CHANGELOG.md` 中记录版本号与本次修复范围。
