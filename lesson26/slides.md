# Day 26 · 神经网络基础

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Python、NumPy、ML 概念(Day 24)、梯度下降直觉(Day 25)
> 关键问题: 什么是神经网络?它为什么能拟合任意复杂函数?
> 本节从生物神经元讲起,推导出感知机模型,再引入激活函数解决
> "线性不可分"问题,最终搭建多层感知机,给出前向传播 + 损失
> 函数的完整图景。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 线性回归的损失函数是
  什么?梯度下降中"梯度"的几何意义是什么? 目的: 唤醒
  "损失函数 + 梯度下降"记忆,为今天"神经网络也用同一套路"
  埋伏笔。
- **赏玩 demo**(3 分钟): 展示一张二分类数据集(线性不可分),
  问"一条直线能把两类点分开吗?"引出"我们需要弯折的决策
  边界",一句话吊足胃口 —— 神经网络就是这个弯折机器。

---

## 1. 第一讲(20 分钟) —— 感知机:M-P 模型与激活函数

### 知识点 1.1 M-P 模型:神经元的数学抽象

1943 年 McCulloch 与 Pitts 提出 M-P 模型,把生物神经元简化
成数学公式:

```
输入信号:    x1, x2, x3, ..., xn
连接权重:    w1, w2, w3, ..., wn
加权求和:    z = w1*x1 + w2*x2 + ... + wn*xn + b
激活输出:    a = activation(z)
```

> 口诀:**加权求和 + 激活函数 = 人工神经元**。

```python
import numpy as np

# 单个神经元的前向计算
def neuron_forward(x, w, b, activation):
    """x: 输入向量 (n,); w: 权重向量 (n,); b: 标量偏置"""
    z = np.dot(w, x) + b       # 加权求和
    a = activation(z)          # 激活函数
    return a

# 示例:3 个输入,权重 [0.5, -1.0, 0.3],偏置 0.1
x = np.array([1.0, 2.0, 0.5])
w = np.array([0.5, -1.0, 0.3])
b = 0.1
# 暂用恒等激活
output = neuron_forward(x, w, b, lambda t: t)
print(f"神经元输出 z = {output:.2f}")
```

> 🔴 教学红线(零维 vs 一维): 学员常把标量、一维向量、二维
> 矩阵混用。在 NumPy 中 `shape=(n,)` 和 `(n,1)` 完全不同。
> 建议画内存图: 标量是"点",向量是"线",矩阵是"面"。本节统一
> 用列向量 `(n,1)`, 与 PyTorch 约定对齐。

### 知识点 1.2 激活函数:为什么需要"非线性"

如果没有激活函数,多层神经元叠加等价于一个线性变换(矩阵
乘法),永远画不出弯折的决策边界。激活函数就是给每个神经元
加一道"非线性闸门"。

| 激活函数 | 公式 | 导数 | 特点 |
|---|---|---|---|
| Sigmoid | `1/(1+e^-z)` | `σ(1-σ)` | 输出 (0,1),易梯度消失 |
| Tanh | `(e^z-e^-z)/(e^z+e^-z)` | `1-tanh²` | 输出 (-1,1),仍梯度消失 |
| ReLU | `max(0, z)` | `z>0? 1: 0` | **最常用**,计算快,缓解梯度消失 |
| LeakyReLU | `max(0.01z, z)` | `z>0? 1: 0.01` | 修复 ReLU "神经元死亡" |

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 200)
plt.figure(figsize=(8, 5))
# 四种激活函数曲线
plt.plot(z, 1/(1+np.exp(-z)), label="Sigmoid")
plt.plot(z, np.tanh(z), label="Tanh")
plt.plot(z, np.maximum(0, z), label="ReLU")
plt.plot(
    z, np.where(z > 0, z, 0.01 * z),
    label="LeakyReLU", linestyle="--"
)
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.legend()
plt.title("四种激活函数曲线对比")
plt.savefig("demo/activation_functions.png", dpi=100)
print("激活函数对比图已保存")
```

> 🔴 教学红线(为什么 ReLU 是默认选择): Sigmoid 在 `|z|>3`
> 时梯度接近 0,多层叠加后梯度几乎消失(Day 27 会证明)。
> ReLU 在正区间梯度恒为 1,链式相乘不会衰减。
> **初学者记住:首选 ReLU,遇到神经元死亡改用 LeakyReLU**。

### 知识点 1.3 激活函数的选择口诀

- **二分类输出层** → Sigmoid(输出是概率)
- **多分类输出层** → Softmax(后面详述)
- **所有隐藏层** → ReLU(默认)/LeakyReLU

> 口诀:**隐藏一律 ReLU,二分类尾 Sigmoid,多分类尾 Softmax**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 手写 Sigmoid / Tanh /
  ReLU 函数,输入一组数值,打印对应的激活值(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 画出四种激活函数的图像,
  观察 Sigmoid 在 `|z|>3` 时曲线"贴地"的现象(⭐⭐,10 分钟)

> 巡场重点: 看学员是否用 NumPy 向量化实现(避免 for 循环),
> 这是后续训练效率的基础。同时检查 `np.exp(-z)` 是否写成
> `np.exp(-1*z)` —— 两者等价,但前者更简洁。

---

## 3. 第二讲(20 分钟) —— 多层感知机(MLP)结构

### 知识点 3.1 三层结构:输入层 / 隐藏层 / 输出层

```
输入层     隐藏层 1    隐藏层 2    输出层
x1 ──┐  ┌─ h1_1 ──┐
x2 ──┼──┤          ├─── h2_1 ──┐
x3 ──┘  └─ h1_2 ──┘            ├─── ŷ
                         h2_2 ──┘
```

- **输入层**: 每个节点对应一个特征,不做变换,只做分发
- **隐藏层**: 多个神经元并行,每层可以有多个节点,是
  "特征变换"的核心
- **输出层**: 分类用 Softmax/Sigmoid,回归用线性激活
  (或无激活)

### 知识点 3.2 前向传播:逐层计算直到输出

每一层的计算都是"矩阵乘法 + 激活函数":

```python
import numpy as np

# 激活函数
def relu(z):
    """ReLU: 负值截零,正值保留"""
    return np.maximum(0, z)

def sigmoid(z):
    """Sigmoid: 压缩到 (0,1)"""
    return 1 / (1 + np.exp(-z))

# 定义一个 2 层网络:3 → 4 → 1
np.random.seed(0)
W1 = np.random.randn(4, 3) * 0.1   # 第 1 层:3 输入 → 4 隐藏
b1 = np.zeros((4, 1))
W2 = np.random.randn(1, 4) * 0.1   # 第 2 层:4 隐藏 → 1 输出
b2 = np.zeros((1, 1))

# 前向传播
x = np.array([[0.5], [0.3], [0.2]])  # 3×1 输入
z1 = W1 @ x + b1
a1 = relu(z1)
z2 = W2 @ a1 + b2
a2 = sigmoid(z2)                     # 二分类输出概率
print(f"网络输出概率 = {a2[0,0]:.4f}")
```

> 口诀:**矩阵乘法 = 线性变换;激活函数 = 非线性闸门;
> 交替堆叠 = 万能函数逼近器**。

> 🔴 教学红线(前向传播的维度匹配): `(m,n) @ (n,p) = (m,p)`。
> 学员常把输入写成行向量 `(1,n)` 而权重是 `(n,h)`, 顺序反了
> 结果全错。约定:**样本是列向量 (n,1),权重在左 (h,n)**。

### 知识点 3.3 万能逼近定理(直觉,不证明)

单隐藏层 MLP 理论上能逼近任何连续函数,但"能逼近"不等于
"能用梯度下降找到"。实际工程中靠**深度**(多层)而非**宽度**
(单层很多神经元)来获得强表达力 —— 这就是深度学习"深"
的原因。

> 口诀:**宽度给能力,深度给效率;现代网络靠深度吃饭**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 手写 3→5→2 网络的
  前向传播,输入 3 维特征,输出 2 维 logits(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 给定一组权重,用 for
  循环实现前向传播(不用矩阵乘法),体会矩阵表达的高效
  (⭐⭐⭐,10 分钟)

> 巡场重点: 练习 4 是让学员感受"向量化 vs for 循环"的速度
> 差异。提示: 大数据集上矩阵乘法比 for 循环快 100 倍以上。
> 同时检查学员是否把 `W @ x + b` 写成 `x @ W + b`。

---

## 5. 第三讲(20 分钟) —— 损失函数

### 知识点 5.1 回归任务:MSE 损失

`MSE = (1/n) * Σ(y_true - y_pred)²`

```python
def mse_loss(y_true, y_pred):
    """均方误差:对大误差更敏感(平方放大)"""
    return np.mean((y_true - y_pred) ** 2)

y_true = np.array([1.0, 0.0, 1.0])
y_pred = np.array([0.9, 0.1, 0.8])
loss = mse_loss(y_true, y_pred)
print(f"MSE = {loss:.4f}")  # 0.0200
```

> MSE 对"大误差"更敏感(平方放大),常用于房价预测、温度
> 预测等回归任务。

### 知识点 5.2 分类任务:交叉熵损失

二分类: `-(y*log(ŷ) + (1-y)*log(1-ŷ))`

```python
def binary_cross_entropy(y_true, y_pred):
    """二分类交叉熵:配合 Sigmoid 时梯度更稳定"""
    eps = 1e-7  # 防止 log(0)
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(
        y_true * np.log(y_pred) +
        (1 - y_true) * np.log(1 - y_pred)
    )

y_true = np.array([1, 0, 1, 1])
y_pred = np.array([0.9, 0.1, 0.8, 0.3])
loss = binary_cross_entropy(y_true, y_pred)
print(f"BCE = {loss:.4f}")  # 0.2776
```

> 为什么分类不用 MSE? MSE 配合 Sigmoid 时容易出现梯度
> 饱和(输出接近 0 或 1 时梯度 → 0),交叉熵与 Sigmoid 配合后
> 梯度表达式更稳定(Day 27 证明)。

### 知识点 5.3 Softmax + 多分类交叉熵

多分类时输出层用 Softmax 把 logits 转为概率分布:

```python
def softmax(z):
    """Softmax:logits → 概率分布(防溢出)"""
    exp_z = np.exp(z - np.max(z))  # 防溢出技巧
    return exp_z / exp_z.sum(axis=1, keepdims=True)

logits = np.array([[2.0, 1.0, 0.1]])  # 3 分类
probs = softmax(logits)
print(f"Softmax 概率 = {probs}")
# [0.6590 0.2424 0.0986]
print(f"概率之和 = {probs.sum():.4f}")  # 1.0000
```

> 🔴 教学红线(Softmax 数值溢出): `exp(1000)` 会溢出为 inf。
> 标准做法是 `z - max(z)` 再做 exp,不改变概率分布,但消除
> 溢出风险。**学员必须记住这句口诀:减最大值,再 exp**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 手写 Softmax(带防溢出)
  + 多分类交叉熵,与 sklearn 的 `log_loss` 对比验证正确性
  (⭐⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否在分子分母同时 `+ eps` 或者忘记 log
> 里的 clip —— 忽略 clip 会在真值为 1 且输出极小时出现
> `log(0) = -inf`。同时检查 `axis=1` 是否写对。

## 7. 小项目(45 分钟)

**项目:从零搭建 XOR 分类器感知机**

- 数据集: 4 个 XOR 样本 `(0,0)→0`、`(1,1)→0`、`(0,1)→1`、
  `(1,0)→1`
- 要求:
  1. 搭建 2→4→1 网络,全部手写 NumPy(不调 torch)
  2. 用 Sigmoid 激活 + BCE 损失
  3. 梯度下降更新权重(先用 Day 25 学过的数值近似梯度,
     Day 27 再教精确梯度)
  4. 训练 5000 轮,观察损失下降曲线
  5. 最终预测概率误差 < 0.05 算通过

> 巡场重点: 这个项目只让学员建立"前向传播 + 损失函数"的
> 完整流程直觉,反向传播留到 Day 27。不要求精确调参,只看
> 趋势。提醒学员画损失曲线,比最终数值更有价值。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进
  `teacher_notes.md`):
  1. 忘记激活函数,多层网络退化为单层线性模型
  2. Softmax 实现未减最大值导致 exp 溢出
  3. MSE 用于分类任务,导致梯度饱和、训练不收敛
- **作业说明**: 课后 `homework/task01.py`(激活函数导数手推)、
  `task02.py`(前向传播向量化 vs for 循环计时对比),下节课前
  10 分钟复盘。

---

## 易错点

1. **没有激活函数的多层网络 = 单层线性变换**,这是初学者
   最容易忽略的"大坑"。
2. **Sigmoid 梯度在 `|z|>3` 时接近 0**,多层叠加后几乎无法
   学习 → 这就是"梯度消失"。
3. **MSE + Sigmoid 在分类任务中梯度饱和**,应改用交叉熵损失。
4. **Softmax 必须做 `z - max(z)` 防溢出**,否则大 logits 会
   导致 NaN。
5. **前向传播时矩阵维度要匹配**,`(m,n) @ (n,p) = (m,p)`,
   初学者常搞反行列。

## 延伸题

> 以下素材来自外部课程,教师可按需选用或替换当堂练。

- **(CS50AI Lecture 0, ⭐⭐)**: 手写感知机实现 AND / OR 逻辑门
  —— 巩固"单层感知机解决线性可分问题"。
- **(3Blue1Brown, ⭐⭐⭐)**: 观看"神经网络"系列视频第 1 集,
  画出三层网络结构草图 —— 强化直觉。
- **(d2l.ai §3.1, ⭐⭐⭐)**: 复现 d2l 书中 Softmax 从零实现,
  带防溢出,对比 torch.nn.CrossEntropyLoss —— 巩固多分类损失。
