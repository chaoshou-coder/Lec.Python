# Lesson20 · 线性回归 + 梯度下降直觉

> 前置: Lesson01-19 已掌握 Python 核心 + 数据处理 + ML 工作流 + 数据预处理
> 重点: 如何用一条直线拟合数据?损失函数怎么衡量"好坏"?梯度下降如何自动找最优解?

## 关键知识点
- 线性回归模型:y = wx + b(单特征) / y = w₁x₁ + ... + wₙxₙ + b(多特征)
- 损失函数 MSE:均方误差,避免正负抵消 + 放大对大错误的惩罚
- `LinearRegression`:正规方程(解析解),中小数据集首选
- 梯度下降直觉:碗里放球滚到最底,沿梯度反方向走一小步
- 学习率 lr:太小太慢 / 太大震荡 / 合适 0.01~0.1
- 三种梯度下降变体:BGD(全量) / SGD(1 个) / Mini-batch SGD(工业界默认)
- `SGDRegressor`:大数据默认,但必须 scale
- 评估指标:R² / MAE / MSE / RMSE(`squared=False`)
- Ridge / Lasso 正则化:L2 / L1 压缩系数

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | numpy 手写 MSE 对比 sklearn |
| 2 | `in_class/practice02.py` | ⭐⭐⭐⭐ | 15 分钟 | 单特征 LinearRegression 打 w/b/R² |
| 3 | `in_class/practice03.py` | ⭐⭐⭐⭐ | 15 分钟 | 手写梯度下降单特征拟合 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐⭐ | 15 分钟 | 4 种 lr 画损失下降曲线 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 15 分钟 | LinearRegression vs SGDRegressor 三指标 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐ | 10 分钟 | scale 前后 SGD R² 对比 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 手写 MSE + 梯度下降单特征 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | California Housing 四指标横向对比 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 20 分钟 | Ridge / Lasso 正则化(选做) |

## 小 / 中型项目
加利福尼亚房价预测完整流程:
- `fetch_california_housing` → train_test_split + StandardScaler
- LinearRegression / SGDRegressor / Ridge 三模型
- R² / MAE / MSE / RMSE 四指标横向对比 + Top-3 特征

## 阶段复习要点
- SGD 必须 scale,不 scale 几乎必然发散
- 回归不用 accuracy,`model.score()` 默认返回 R²
- 梯度下降更新是 `w = w - lr * grad`,`+` 方向发散
- 数据量 < 1 万用 LinearRegression(解析解),≥ 10 万用 SGD
- `mean_squared_error(y, y_pred, squared=False)` 才是 RMSE
