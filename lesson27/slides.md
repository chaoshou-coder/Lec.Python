# Day 27 · 反向传播与梯度下降 ⚡ 深入到底

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 26 神经网络基础、矩阵求导链式法则、偏导数
> 关键问题: 神经网络有百万参数,怎么一次性算出每个参数该
> 往哪动、动多少?本节用计算图 + 手算数值例子,把反向传播
> 拆到最细粒度,让读者彻底告别"链式法则恐惧症"。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 为什么没有激活函数的
  多层网络等价于单层线性变换?ReLU 在正区间和负区间的导数
  分别是多少?目的: 唤醒"激活函数"记忆,为今天"逐层求导"埋伏笔。
- **赏玩 demo**(3 分钟): 展示一个 2 层网络的前向传播,问
  "输出错了 0.1,应该怪第一层的 w1 还是第二层的 w2?怪多少?"
  引出"梯度就是'怪罪分配单'"。

---

## 1. 第一讲(25 分钟) —— 计算图与链式法则直觉

### 知识点 1.1 计算图:把复合函数画成乐高积木

任何一个神经网络都是复合函数: `L = loss(f(g(x)))`。计算图
把每个基本运算(加、乘、exp、log)画成节点,数据流从左到
右(前向),梯度从右到左(反向)。

```
前向:  x → [×w] → [+b] → [σ] → [×w2] → L
反向:  x ← [×w] ← [+b] ← [σ] ← [×w2] ← L(∂L/∂L=1)
```

> 口诀:**前向算输出,反向传梯度;每个节点只关心自己和邻居**。

### 知识点 1.2 链式法则:复合函数求导的"剥洋葱"

若 `y = f(g(x))`, 则 `dy/dx = f'(g(x)) · g'(x)`。

展开到三层: `L = loss(z3), z3 = a2·w3, a2 = σ(z2), z2 = a1·w2`.

```
∂L/∂w2 = ∂L/∂z3 · ∂z3/∂a2 · ∂a2/∂z2 · ∂z2/∂w2
         (从后往前,一路相乘)
```

> 🔴 教学红线(链式法则 vs 偏导数 vs 梯度):
> - **偏导数** —— 单个自变量变化率(其他变量冻住)
> - **梯度** —— 所有偏导数拼成的向量 `∇f = [∂f/∂x1, ∂f/∂x2, ...]`
> - **链式法则** —— 算偏导/梯度时"穿层"的工具
> 三者关系:梯度用偏导数拼,偏导数靠链式法则算。

### 知识点 1.3 计算图的"局部梯度"与"全局梯度"

每个节点只需要算两件事:
1. **局部梯度**: 自己输出对输入的导数(如 `d(σ(z))/dz = σ(1-σ)`)
2. **全局梯度**: 上游传回的梯度 × 局部梯度

```python
import numpy as np

# Sigmoid 节点的反向传播
def sigmoid_backward(dout, z):
    """dout: 上游梯度; z: 前向时的输入"""
    a = 1 / (1 + np.exp(-z))      # 局部梯度 = a*(1-a)
    local_grad = a * (1 - a)
    return dout * local_grad       # 链式法则: 上游 × 局部

# 矩阵乘法的反向传播
def matmul_backward(dout, W, x):
    """ dout: 上游梯度 (out_dim,) """
    dW = dout[:, None] @ x[None, :]  # (out,1) @ (1,in) = (out,in)
    dx = W.T @ dout                  # (in,out) @ (out,) = (in,)
    return dW, dx
```

> 口诀:**局部乘上游,矩阵转置救**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 给定 `y = x² · sin(x)`,
  手动求导后,用计算图反向传播验证(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 练习 `matmul_backward`,
  给定 `dout, W, x`, 算出 `dW, dx`, 手写一遍再验算(⭐⭐,10 分钟)

> 巡场重点: 看学员是否把矩阵乘法的两个梯度 `dW` 和 `dx` 搞混。
> 记住:`dW` 用外积,`dx` 用 W 转置乘 dout。

---

## 3. 第二讲(30 分钟) —— 反向传播手算演示(数值例子)

### 知识点 3.1 问题定义:2→2→1 网络,Sigmoid 全激活

```
输入 x = [0.5, 0.3]
权重 W1 = [[0.1, 0.2],    b1 = [0.0, 0.0]
           [0.3, 0.4]]
权重 W2 = [[0.5, 0.6]]     b2 = [0.0]
标签 y_true = 1
损失 L = ½(y_true - a2)²
```

### 知识点 3.2 前向传播(逐步计算)

```python
import numpy as np

x = np.array([[0.5], [0.3]])      # (2,1)
y_true = 1.0

W1 = np.array([[0.1, 0.2],
               [0.3, 0.4]])       # (2,2)
b1 = np.zeros((2, 1))
W2 = np.array([[0.5, 0.6]])       # (1,2)
b2 = np.zeros((1, 1))

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# === 前向传播 ===
z1 = W1 @ x + b1                  # (2,1)
# z1 = [[0.1*0.5 + 0.2*0.3], [0.3*0.5 + 0.4*0.3]]
#     = [[0.11], [0.27]]
a1 = sigmoid(z1)
# a1 = [[sigmoid(0.11)], [sigmoid(0.27)]]
#     ≈ [[0.5275], [0.5671]]
z2 = W2 @ a1 + b2                  # (1,1)
# z2 = 0.5*0.5275 + 0.6*0.5671 = 0.6040
a2 = sigmoid(z2)
# a2 ≈ sigmoid(0.6040) ≈ 0.6465

print(f"z1 = {z1.ravel()}")
print(f"a1 = {a1.ravel()}")
print(f"z2 = {z2[0,0]:.4f}")
print(f"a2 = {a2[0,0]:.4f}")
```

### 知识点 3.3 损失计算

```python
L = 0.5 * (y_true - a2[0,0])**2
# L = 0.5 * (1 - 0.6465)² = 0.5 * 0.1250 = 0.0625
print(f"Loss = {L:.4f}")
```

### 知识点 3.4 反向传播(逐步求梯度)

**第 1 步: 对 a2 求导**

```python
dL_da2 = -(y_true - a2[0,0])        # -0.3535
```

**第 2 步: 通过 Sigmoid 反向**

```python
# dL/dz2 = dL/da2 · da2/dz2
# da2/dz2 = a2*(1-a2)
da2_dz2 = a2[0,0] * (1 - a2[0,0])   # 0.6465 * 0.3535 ≈ 0.2286
dL_dz2 = dL_da2 * da2_dz2            # -0.3535 * 0.2286 ≈ -0.0808
```

**第 3 步: 对 W2 和 b2 求导**

```python
# dL/dW2 = dL/dz2 · a1^T
dL_dW2 = dL_dz2 * a1.T              # (-0.0808) * [0.5275, 0.5671]
#                               ≈ [[-0.0426, -0.0458]]
dL_db2 = dL_dz2                      # -0.0808
```

**第 4 步: 把梯度传回 a1**

```python
# dL/da1 = W2^T · dL/dz2
dL_da1 = W2.T * dL_dz2
#         = [[0.5], [0.6]] * (-0.0808)
#         ≈ [[-0.0404], [-0.0485]]
```

**第 5 步: 通过第一层 Sigmoid 反向**

```python
da1_dz1 = a1 * (1 - a1)
#         ≈ [[0.5275*0.4725], [0.5671*0.4329]]
#         ≈ [[0.2492], [0.2455]]
dL_dz1 = dL_da1 * da1_dz1
#        ≈ [[-0.0404*0.2492], [-0.0485*0.2455]]
#        ≈ [[-0.0101], [-0.0119]]
```

**第 6 步: 对 W1 和 b1 求导**

```python
dL_dW1 = dL_dz1 @ x.T
#        = [[-0.0101], [-0.0119]] @ [[0.5, 0.3]]
#        ≈ [[-0.0050, -0.0030],
#            [-0.0059, -0.0036]]
dL_db1 = dL_dz1
#        ≈ [[-0.0101], [-0.0119]]
```

### 知识点 3.5 梯度汇总

```
参数      梯度值                 含义
W1[0,0]  -0.0050      减小 w1[0,0] 能降低 loss
W1[0,1]  -0.0030      减小 w1[0,1] 能降低 loss
W1[1,0]  -0.0059      减小 w1[1,0] 能降低 loss
W1[1,1]  -0.0036      减小 w1[1,1] 能降低 loss
W2[0,0]  -0.0426      减小 w2[0,0] 能降低 loss
W2[0,1]  -0.0458      减小 w2[0,1] 能降低 loss
```

> 🔴 教学红线(梯度符号的意义): 梯度为负 → 增大参数能降低
> loss;梯度为正 → 减小参数能降低 loss。**更新公式是
> `w = w - lr * grad`,所以负梯度自然让 w 变大**。学员常在这
> 里搞反,牢记"减号 + 负梯度 = 加"。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 换一组 W1, W2 数值,
  重做上面的手算例,算出全部 8 个梯度,与给出的答案对比
  (⭐⭐⭐⭐,20 分钟)

> 巡场重点: 让学员分组讨论,每人算一步,互相校验。重点检查:
> 1. 链式法则的相乘顺序(上游在前,局部在后)
> 2. 矩阵乘法的维度(尤其 `dL_dW2 = dout * a1.T`)
> 3. 梯度更新的符号(负梯度 = 参数增加)

---

## 5. 第三讲(25 分钟) —— 梯度下降的三种姿态

### 知识点 5.1 梯度下降直觉:在最陡的方向迈一步

想象你在雾中下山,看不见路,只能感受脚下坡度。每一步都
往最陡的方向(负梯度方向)走一小步(学习率 η):

```
w_new = w_old - η · ∂L/∂w
```

### 知识点 5.2 SGD vs 动量 vs Adam:峡谷地形对决

想象一个峡谷(纵轴梯度大,横轴梯度小):

```
        SGD                动量(Momentum)          Adam
     ↗   ↘                 →  →  →               → → →
    ↗     ↘              (沿峡谷方向             (沿峡谷方向
   ↗       ↘              加速冲)                加速,且步长
  ↗         ↘                                    自动调)
- 走 Z 字形摆动        - 历史方向加权平均          - 一阶矩(方向)
- 横向慢,纵向快        - 冲出横向慢区              + 二阶矩(步长)
                                             = 又快又稳
```

```python
import numpy as np

# SGD: 最朴素
def sgd_update(w, grad, lr=0.01):
    return w - lr * grad

# 动量: 积累历史方向
v = 0
def momentum_update(w, grad, lr=0.01, beta=0.9):
    global v
    v = beta * v - lr * grad
    return w + v

# Adam: 自适应学习率(完整实现)
m, v_t = 0, 0
t = 0
def adam_update(w, grad, lr=0.01, beta1=0.9, beta2=0.999, eps=1e-8):
    global m, v_t, t
    t += 1
    m = beta1 * m + (1 - beta1) * grad          # 一阶矩(均值)
    v_t = beta2 * v_t + (1 - beta2) * grad**2    # 二阶矩(方差)
    m_hat = m / (1 - beta1**t)                  # 偏差修正
    v_hat = v_t / (1 - beta2**t)
    return w - lr * m_hat / (np.sqrt(v_hat) + eps)
```

> 口诀:**SGD 纯看当下,Momentum 记历史,Adam 自动调步**。

### 知识点 5.3 学习率:太大震荡 / 太小太慢

| 学习率 | 现象 | 解决方案 |
|---|---|---|
| 太大(η>1) | loss 震荡甚至发散 | 减小 η,或用 Adam |
| 合适(η~0.01) | 稳定下降 | 保持 |
| 太小(η<1e-5) | 下降极慢,易陷局部最优 | 增大 η,或加衰减 |

**学习率衰减策略**: 前期大学习率快速下降,后期小学习率精细调。

```python
# 指数衰减
lr = initial_lr * (decay_rate ** (epoch // step_size))

# 余弦退火
lr = final_lr + 0.5 * (initial_lr - final_lr) * (
    1 + np.cos(np.pi * epoch / total_epochs)
)
```

> 🔴 教学红线(梯度消失/爆炸的直觉):
> - **梯度消失**: 多个 <1 的数连乘 → 趋近 0(如 Sigmoid 导数
>   最大 0.25,5 层后 0.25⁵ ≈ 0.001,梯度几乎消失)
> - **梯度爆炸**: 多个 >1 的数连乘 → 趋近 ∞(如 w=2,5 层后
>   2⁵ = 32,梯度爆炸)
>   **解决方案**: BatchNorm 稳定中间层分布,+ He 初始化让
>   权重初始方差 = 2/n_in, + ReLU 替代 Sigmoid(正区间导数=1)。

## 6. 当堂练 3(25 分钟)

- 练习 4: `in_class/practice04.py` —— 用 SGD、动量、Adam
  三种方式优化 `f(x)=x²+10cos(x)`,画三种优化轨迹对比图,
  体会"峡谷地形"中的差异(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否画出"等高线 + 优化路径"图,这是理解
> 优化器差异的关键可视化。Adam 应该最快到达谷底,SGD 最慢。

---

## 7. 小项目(45 分钟)

**项目:NumPy 手写 2 层网络 forward + backward**

要求:
1. 网络结构: 2→4→1, Sigmoid + BCE
2. 完整实现 `forward(x)`, `backward(x, y)`, `train(X, Y, epochs)`
3. 用 Day 26 的 XOR 数据,对比「Day 26 数值近似梯度」vs
   「今天精确反向传播」的训练速度
4. 画出精确梯度下的损失曲线 vs 数值近似的损失曲线
5. 最终 XOR 4 个样本预测概率误差均 < 0.05

```python
import numpy as np

class TwoLayerNet:
    def __init__(self, input_dim, hidden_dim, output_dim):
        # He 初始化
        self.W1 = np.random.randn(
            hidden_dim, input_dim
        ) * np.sqrt(2.0 / input_dim)
        self.b1 = np.zeros((hidden_dim, 1))
        self.W2 = np.random.randn(
            output_dim, hidden_dim
        ) * np.sqrt(2.0 / hidden_dim)
        self.b2 = np.zeros((output_dim, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def forward(self, x):
        """前向传播,返回输出 + 缓存中间结果"""
        z1 = self.W1 @ x + self.b1
        a1 = self.sigmoid(z1)
        z2 = self.W2 @ a1 + self.b2
        a2 = self.sigmoid(z2)
        cache = (x, z1, a1, z2, a2)
        return a2, cache

    def backward(self, y_true, cache):
        """反向传播,返回所有参数的梯度"""
        x, z1, a1, z2, a2 = cache
        # 输出层梯度
        dL_dz2 = a2 - y_true                      # BCE + Sigmoid 合并
        dW2 = dL_dz2 @ a1.T
        db2 = dL_dz2
        # 隐藏层梯度
        dL_da1 = self.W2.T @ dL_dz2
        dL_dz1 = dL_da1 * a1 * (1 - a1)           # Sigmoid 导数
        dW1 = dL_dz1 @ x.T
        db1 = dL_dz1
        return {"dW1": dW1, "db1": db1,
                "dW2": dW2, "db2": db2}

    def update(self, grads, lr=0.1):
        self.W1 -= lr * grads["dW1"]
        self.b1 -= lr * grads["db1"]
        self.W2 -= lr * grads["dW2"]
        self.b2 -= lr * grads["db2"]

    def loss(self, y_true, y_pred):
        eps = 1e-7
        y_pred = np.clip(y_pred, eps, 1 - eps)
        return -np.mean(
            y_true * np.log(y_pred) +
            (1 - y_true) * np.log(1 - y_pred)
        )

# 训练 XOR 数据
X = np.array([[0,0],[0,1],[1,0],[1,1]]).T  # (2,4)
Y = np.array([[0, 1, 1, 0]])               # (1,4)
net = TwoLayerNet(2, 4, 1)
for epoch in range(10000):
    a2, cache = net.forward(X)
    grads = net.backward(Y, cache)
    net.update(grads, lr=0.5)
    if epoch % 2000 == 0:
        print(f"Epoch {epoch}, Loss = {net.loss(Y, a2):.4f}")
print(f"最终预测: {net.forward(X)[0].ravel()}")
```

> 🔴 教学红线(BCE + Sigmoid 合并求导): 单独对 BCE 求
> `dL/da2`, 再对 Sigmoid 求 `da2/dz2`,二者合并后刚好等于
> `a2 - y_true`。这个简化是面试必考,务必讲透推导过程。

> 巡场重点: 提醒学员先跑通「单样本训练」(循环 4 个样本),
> 再扩展到「批量训练」(一次性处理全部 4 个)。批量训练的梯
> 度是单样本梯度的均值。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进
  `teacher_notes.md`):
  1. 梯度更新方向搞反(该加写成减,或相反)
  2. 矩阵乘法的梯度 `dW` 和 `dx` 搞混(外积 vs 转置乘)
  3. 多节点链式法则漏乘某个局部梯度(尤其 Sigmoid 导数)
- **作业说明**: 课后 `homework/task01.py`(把今天的手算例
  扩展到 2→3→1 网络,重算一遍)、`homework/task02.py`(给
  TwoLayerNet 加 ReLU 选项),下节课前 10 分钟复盘。

---

## 易错点

1. **梯度更新的符号**: `w = w - lr * grad`,负梯度 → 参数变大,
   不要写反。
2. **矩阵乘法的梯度**: `dW = dout`(外积)`x^T`, `dx = W^T dout`,
   两者形式完全不同。
3. **链式法则的顺序**: 上游梯度 × 局部梯度,不是反过来。
4. **梯度消失/爆炸的根因**: 多层连乘 → 多个 <1 数乘趋 0,
   多个 >1 数乘趋 ∞。
5. **学习率是超参**: 不是网络自己学的,是人调的;Adam 虽
   自动调步,但其初始学习率也是人定的。

## 延伸题

> 以下素材来自外部课程,教师可按需选用或替换当堂练。

- **(CS231n Lecture 4, ⭐⭐⭐⭐)**: 阅读 CS231n 笔记中
  "Backpropagation, Intuitions"一节,完成其中一道手算题。
- **(Andrej Karpathy micrograd, ⭐⭐⭐⭐)**: 阅读 Karpathy
  的 `micrograd` 仓库,理解 autograd 引擎的实现。
- **(3Blue1Brown, ⭐⭐⭐)**: 看"反向传播微积分"那一集,把
  今天的手算例对照视频末尾 10 分钟,加深直觉。
