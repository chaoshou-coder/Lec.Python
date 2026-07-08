# Day20 · 线性回归+梯度下降直觉

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-19 已掌握 Python 核心 + 数据处理 + ML 工作流 + 数据预处理
> 关键问题: 如何用一条直线拟合数据?损失函数怎么衡量"好坏"?梯度下降如何
> 自动找最优解?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 数据预处理的三大步骤是什么?为什么
  训练集/测试集要 `random_state=42` 固定?目的: 唤醒"先处理数据再建模"的
  肌肉记忆,为今天"正式进入模型训练"铺路。
- **赏玩 demo**(3 分钟): 投屏展示"加利福尼亚房价预测"的 DEMO(只展示最终
  R² = 0.62 的效果和一条"真实 vs 预测"散点图),问:"这条'红色参考线'是怎
  么来的?今天就来拆解它"。

---

## 1. 第一讲(15 分钟) —— 线性回归模型:`y = wx + b` + 损失函数 MSE

### 知识点 1.1 线性回归直觉:"用一条直线拟合点"

- **单特征模型**: `ŷ = wx + b`,其中:
  - `x` = 输入特征(比如"收入")
  - `ŷ` = 预测值(比如"房价")
  - `w` = 权重(斜率),`b` = 偏置(截距)
- **多特征模型**: `ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b`,每个特征一个权重。

类比: 线性回归 = 找一条让"所有点到直线距离之和"最小的直线 —— 虽然用的是
"距离²"而非绝对距离(因为有 MSE,下文讲)。

### 知识点 1.2 损失函数 MSE:衡量"有多差"

- **MSE**(均方误差):
  `MSE = (1/n) Σ (yᵢ - ŷᵢ)²`
- 直觉: 预测值与真实值之差的**平方均值**。平方是为了:
  1. 避免正负抵消。
  2. 放大对**大错误**的惩罚(错的越多罚得越狠)。

```python
import numpy as np

y_true = np.array([3.0, 5.0, 2.5, 7.0])
y_pred = np.array([2.8, 5.2, 2.3, 6.5])

# 手动算 MSE
mse = np.mean((y_true - y_pred) ** 2)
print(f"MSE = {mse:.4f}")  # 0.0975
```

### 知识点 1.3 `sklearn.linear_model.LinearRegression`:正规方程

```python
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
print(f"训练 R² = {model.score(X_train, y_train):.4f}")
print(f"测试 R² = {model.score(X_test, y_test):.4f}")
print(f"权重数量: {len(model.coef_)} 个")
print(f"截距 b = {model.intercept_:.4f}")
```

> `LinearRegression` 用**正规方程**(解析解)直接求解,不需要迭代。适合中小
> 数据集。大数据用 `SGDRegressor`(见第三讲)。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用 numpy 手写 MSE 函数,验证
  `sklearn.metrics.mean_squared_error` 结果一致(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 对加利福尼亚房价只用`MedInc`一个特征
  跑 `LinearRegression`,打印 w、b、R²(⭐⭐⭐⭐,15 分钟)

> 巡场重点: 学员易把 `model.score()` 当成准确率 —— 强调:**回归任务里
> `score()` 默认返回 R²,不是 accuracy**。

---

## 3. 第二讲(15 分钟) —— 梯度下降直觉:碗-球模型 + 学习率

### 知识点 3.1 梯度下降直觉:"碗里放球,滚到最底"

把损失函数 `MSE(w)` 想象成一个**碗**(碗底是损失最小的 `w*`);现在你在碗
壁某处放一个球,球会**沿最陡方向**(梯度反方向)往下滚 —— 这就是梯度下降。

三步循环:
1. 给定当前 `w`,算梯度 `∇MSE(w)`。
2. 更新:`w = w - lr * ∇MSE(w)`(沿梯度反方向走一小步)。
3. 重复直到 MSE 不再下降(收敛)。

### 知识点 3.2 学习率 lr:太大震荡/太小太慢

- **lr 太小**(如 0.001): 球滚得很慢,要很久才到碗底。
- **lr 太大**(如 1.0): 球直接滚过碗底到对面,**来回震荡**甚至发散。
- **合适 lr**(如 0.01~0.1): 稳定下降直至收敛。

```python
import matplotlib.pyplot as plt
import numpy as np

# 一个简单碗函数:J(w) = (w - 3)² + 1,最小值在 w=3
def J(w):
    return (w - 3) ** 2 + 1

def grad_J(w):
    return 2 * (w - 3)

lr = 0.3          # 合适学习率
w = 0.0           # 初始值
ws = [w]
for _ in range(20):
    w = w - lr * grad_J(w)
    ws.append(w)

print(f"收敛到 w = {w:.4f}, J = {J(w):.4f}")
```

### 知识点 3.3 三种梯度下降变体

| 变体 | 每次用多少样本 | 特点 |
|---|---|---|
| **BGD**(批量) | 全部 n 个 | 稳但慢,不适合大数据 |
| **SGD**(随机) | 1 个 | 快但震荡,易挣脱局部最小 |
| **Mini-batch SGD** | 小批 b 个(如 32) | 工业界默认,平衡速度与稳定 |

🔴 **教学红线(梯度下降只讲直觉,不推导偏导)**: 学员容易卡在链式推导,
本节只需记住:**梯度 = 最陡上升方向,lr = 步长,减去梯度 = 沿最陡下降方向
走一小步**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 手动实现单特征线性回归 + 梯度下降
  (numpy,手写梯度 `∇ = (2/n) * Xᵀ(Xw - y)`),对比 `LinearRegression` 的 w(⭐⭐⭐
  ⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 固定数据集,分别设 `lr=0.001/0.01/0.1/0.5`,
  画 4 条"损失 vs 迭代次数"下降曲线,体会学习率(⭐⭐⭐⭐,15 分钟)

> 巡场重点: 学员常把 `w = w - lr * grad` 写成 `w = w + lr * grad` —— 强调:
> **梯度是上升方向,要反方向走才下降**。

---

## 5. 第三讲(15 分钟) —— 实战:`SGDRegressor` + 评估指标 R²/MAE/MSE

### 知识点 5.1 `SGDRegressor`:大数据默认解法

```python
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

# SGD 对特征尺度敏感,必须 scale!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

sgd = SGDRegressor(
    max_iter=1000, random_state=42, eta0=0.01
)
sgd.fit(X_train_scaled, y_train)
print(f"SGD 测试 R² = {sgd.score(X_test_scaled, y_test):.4f}")
```

> 🔴 教学红线:**SGD 必须 scale**。不 scale 的 SGD 几乎肯定发散或收敛极
> 慢。对比 LinearRegression(解析解,不必 scale)的差异。

### 知识点 5.2 回归四大评估指标

| 指标 | 公式(直觉) | 注意 |
|---|---|---|
| **R²** | 1 - (残差²/总方差) | 1=完美,0=与均值预测持平,可负 |
| **MAE** | mean(\|y - ŷ\|) | 平均绝对误差,单位同 y |
| **MSE** | mean((y - ŷ)²) | 单位是 y²,不直观 |
| **RMSE** | √MSE | 单位同 y,常用 |

```python
from sklearn.metrics import (
    r2_score, mean_absolute_error, mean_squared_error
)

y_pred = sgd.predict(X_test_scaled)
print(f"R²   = {r2_score(y_test, y_pred):.4f}")
print(f"MAE  = {mean_absolute_error(y_test, y_pred):.4f}")
print(f"RMSE = {mean_squared_error(y_test, y_pred, squared=False):.4f}")
```

> `squared=False` 返回 RMSE;`squared=True`(默认)返回 MSE。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 在加利福尼亚房价上跑
  `LinearRegression` 与 `SGDRegressor`**对比**,打 R²/MAE/RMSE 三指标(⭐⭐⭐
  ⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 故意**不 scale** 跑 SGD,再**scale**后跑
  一遍,对比两次 R²,体会 scale 对 SGD 的决定性影响(⭐⭐⭐,10 分钟)

> 巡场重点: 学员易把 `model.score(X_test, y_test)` 当成固定指标 —— 强调:
> **R² 只是线性回归的默认`,分类任务看 accuracy,两者不要搞混**。

---

## 7. 小项目(若本日有,45 分钟)

**加利福尼亚房价预测完整流程**:

1. 加载 `fetch_california_housing()` → 查看特征名 + 描述
2. `train_test_split` + `StandardScaler` 做预处理
3. 同时跑 3 个模型:`LinearRegression` / `SGDRegressor` / `Ridge`
4. 用 4 项指标(R²/MAE/MSE/RMSE)做横向对比表
5. 打印 Top-3 重要特征(`abs(model.coef_)`)

最终产出一份 Markdown 小报告(模型名 + 指标表 + 结论一句话)。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. SGD 不做 scale 直接跑(几乎必然发散)
  2. 把 `model.score()` 在回归上当成 accuracy(回归默认是 R²)
  3. 手写梯度下降写成 `w + lr * grad`,方向反了结果发散
- **作业说明**: 课后 `homework/task01.py`(手写 MSE + 梯度下降单特征)、
  `homework/task02.py`(用加利福尼亚房价跑 4 评估指标横向对比表)、
  `homework/task03.py`(波士顿房价 + Ridge/Lasso 正则化选做)。

---

## 易错点

1. **SGD 必须 scale**: SGD 是对特征尺度敏感的优化算法,不 scale 几乎发散。
2. **回归不用 accuracy**: `model.score()` 在回归器上默认返回 R²,不是分类
   的 accuracy。想用多指标看 R² + MAE + RMSE。
3. **学习率方向**: 更新梯度是 `w = w - lr * grad`,不是 `+`,+ 方向是上升
   (往山顶走,永远发散)。
4. **NormalEquation vs SGD**: 数据量 < 1 万直接用 `LinearRegression`(
   解析解,不需要 scale + lr);大数据 ≥ 10 万用 `SGDRegressor`。
5. **RMSE 与 MSE 的 `squared` 参数**: `mean_squared_error(y,y_pred,
   squared=False)` 才是 RMSE,忘记设就是 MSE。

## 延伸题

- **梯度下降可视化动画(⭐⭐⭐⭐)**: 搜 "gradient descent animation
  contour",看小球如何在等高线图上沿最陡方向滚到碗底。
- **Ridge/Lasso 正则化实验(⭐⭐⭐⭐)**: 对加利福尼亚房价分别用
  Ridge(L2)/Lasso(L1)/ElasticNet,看哪个能把不重要特征的系数压缩到 0。
- **正规方程推导(⭐⭐⭐⭐⭐)**: 对学有余力同学,看 Andrew Ng 推导
  `w* = (XᵀX)⁻¹Xᵀy` 的矩阵求导过程。重点理解"XᵀX 可逆即解析解存在"。
