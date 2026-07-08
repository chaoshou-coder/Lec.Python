# Day21 · 逻辑回归+树模型

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-20 已掌握 Python 核心 + 数据处理 + ML 工作流 + 数据预处理
>   + 线性回归
> 关键问题: 回归预测"多少",分类预测"是哪类"——Sigmoid 如何把实数压成概率?
>   决策树为何"不用 scale 却容易过拟合"?随机森林"双重随机"如何做到 1+1>2?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 线性回归的损失函数是什么?`R²` 越
  接近 1 代表什么?目的: 唤醒"连续值预测"记忆,为今天"离散值分类"做对比铺
  路。
- **赏玩 demo**(3 分钟): 现场跑一个"泰坦尼克生存预测"demo,输入乘客年龄/
  舱位/性别,模型输出"幸存 / 遇难"。问:"模型怎么输出'百分之多少会活'?"引
  出 Sigmoid + 概率。

---

## 1. 第一讲(15 分钟) —— 逻辑回归:Sigmoid 与决策边界

### 知识点 1.1 分类 vs 回归:任务目标变了

- **回归**: 预测连续值(房价、温度)→ 线性回归。
- **分类**: 预测离散标签(猫/狗、幸存/遇难)→ 逻辑回归。

> 关键区别: 输出不再是一个任意实数,而是一个 **0~1 之间的概率**。

### 知识点 1.2 Sigmoid 函数:压到 0~1 的"软开关"

$\sigma(z) = \frac{1}{1 + e^{-z}}$

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

x = np.linspace(-10, 10, 200)
plt.plot(x, sigmoid(x))
plt.axhline(0.5, color="gray", linestyle="--")
plt.axvline(0, color="gray", linestyle="--")
plt.title("Sigmoid: 越大越近 1,越小越近 0")
plt.show()
```

> 直觉: Sigmoid 把"任何实数"映射到 (0,1)。`z = 0` 时输出 0.5(决策分界);
> 正 `z` → 逼近 1;负 `z` → 逼近 0。

🔴 **教学红线(逻辑回归 ≠ 回归)**: 学员常误以为逻辑回归是回归算法。**强
调: 逻辑回归名字有"回归",实际是分类算法,输出的是概率**。

### 知识点 1.3 `LogisticRegression` 实战

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
# 简化为二分类:只取前 100 条(setosa vs versicolor)
X, y = X[:100], y[:100]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 逻辑回归要做 scale(基于距离)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_s, y_train)
print(f"准确率: {model.score(X_test_s, y_test):.4f}")
# 输出概率(不只给标签)
print(model.predict_proba(X_test_s[:3]).round(3))
```

> 笔记: `predict_proba()` 返回每类的概率,`predict()` 取概率最高的类。

---

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用 numpy 手画 Sigmoid 曲线(z 从
  -10 到 10),并在图上标注 `z=0` 处的概率值(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 在 iris 二分类数据上跑
  `LogisticRegression`,对比"scale 前"和"scale 后"的准确率差异(⭐⭐⭐,15
  分钟)

> 巡场重点: 学员常忘记 `StandardScaler` 要 `fit_transform` 训练集、
> `transform` 测试集 —— 提示:"scaler 要在训练集上 fit,测试集只能
> transform,否则数据泄露"。

---

## 3. 第二讲(15 分钟) —— 决策树:可视化 + 过拟合红线

### 知识点 3.1 决策树直觉:一套 if-else

决策树就是人类决策流程的图形化 —— 每个节点问一个特征阈值,向下分叉,直到
叶子给出预测。

> 关键优点: **可解释性极高**,能直接画出来给非技术人员看。

### 知识点 3.2 分裂标准:基尼系数 / 信息增益(只讲直觉)

- **基尼系数**(Gini): 衡量"不纯度"。同一类扎堆 → Gini ≈ 0。
- **信息增益**(Entropy): 衡量"不确定性的减少"。

🔴 **严格边界 —— 本课不讲公式,只讲直觉**: 每一个节点选"能让子节点最纯"
的那种分裂方式,就像"问什么问题能把两类最快分开"。

### 知识点 3.3 `DecisionTreeClassifier` + 可视化

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 树模型不需 scale
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
print(f"测试准确率: {tree.score(X_test, y_test):.4f}")

# 可视化决策树
plt.figure(figsize=(16, 8))
plot_tree(
    tree, feature_names=load_iris().feature_names,
    class_names=load_iris().target_names, filled=True
)
plt.title("Decision Tree (max_depth=3)")
plt.show()
```

### 知识点 3.4 深度对比:欠拟合 vs 过拟合

```python
# 深度 = 3: 泛化好
tree_shallow = DecisionTreeClassifier(max_depth=3)
# 深度 = 20: 几乎完美记住训练集,测试集上崩
tree_deep = DecisionTreeClassifier(max_depth=20)

tree_shallow.fit(X_train, y_train)
tree_deep.fit(X_train, y_train)

print(f"depth=3  训练: {tree_shallow.score(X_train, y_train):.3f} "
      f"测试: {tree_shallow.score(X_test, y_test):.3f}")
print(f"depth=20 训练: {tree_deep.score(X_train, y_train):.3f} "
      f"测试: {tree_deep.score(X_test, y_test):.3f}")
```

🔴 **教学红线(max_depth 过大的过拟合)**: 这是决策树**最容易踩的坑**。
`max_depth=None` 默认不限制,树会一直分裂到每个叶子只剩一个样本 → 训练准
确率 100%,测试一塌糊涂。**强调: 调参第一件事就是限制 depth**。

> 教学口诀:**树不怕矮,不怕胖,就怕太深**。

---

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 在 iris 上分别设 `max_depth=2/5/
  20/None`,记录训练 / 测试准确率填入表格,画"深度-准确率"折线图(⭐⭐⭐
  ⭐,20 分钟)
- 练习 4: `in_class/practice04.py` —— 用 `plot_tree` 可视化 depth=2 的决
  策树,标出根节点用了哪个特征做分裂(⭐⭐⭐,10 分钟)

> 巡场重点: 学员常忘记 `plt.figure(figsize=...)` 导致树太小看不清。提示:
> "节点越多,figsize 越大"。

---

## 5. 第三讲(15 分钟) —— 随机森林:集成 + 特征重要性

### 知识点 5.1 集成思想:三个臭皮匠赛过诸葛亮

- **Single 决策树**: 容易过拟合,对噪声敏感。
- **随机森林**: 训练 **N 棵不同的树**,各自对数据 / 特征做"随机采样",
  最终**投票**决定类别。

### 知识点 5.2 "双重随机"具体指什么

1. **样本随机**: 每棵树从训练集做 Bootstrap 抽样(有放回抽样),每个树只看
   约 63% 的原始样本。
2. **特征随机**: 每个节点分裂时,只随机选 `sqrt(n_features)` 个特征候选。

> 双重随机让每棵树"见过的数据不一样、关注的角度不一样" → 树与树之间**互
> 相独立** → 投票结果方差小、泛化好。

### 知识点 5.3 `RandomForestClassifier` 实战

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,   # 100 棵树
    max_depth=5,        # 每棵树最多 5 层
    random_state=42
)
rf.fit(X_train, y_train)
print(f"随机森林准确率: {rf.score(X_test, y_test):.4f}")
```

> 类比: 100 个独立训练的学生去考同一张卷子,最后投票 —— 一般比单个学霸
> 更稳。

### 知识点 5.4 特征重要性:谁最重要?

```python
import pandas as pd

importances = rf.feature_importances_
feat_imp = pd.Series(importances, index=load_iris().feature_names)
feat_imp.sort_values().plot(kind="barh")
plt.title("Feature Importance")
plt.show()
```

> 用途: 特征选择 —— 把贡献极低的特征删掉,模型更快、更稳。

---

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 在 iris 上跑 `n_estimators=1/10/
  100/500`,画"树的数量-准确率"曲线,体会"越多越稳但收益递减"(⭐⭐⭐⭐,
  20 分钟)
- 练习 6: `in_class/practice06.py` —— 输出随机森林的特征重要性,找出 iris
  数据中**最重要**和**最不重要**的特征,并讨论"能否删掉最不重要特征"(⭐⭐
  ⭐,10 分钟)

> 巡场重点: 学员每跑一次都重新 fit,对比耗时太长。提示:**先在外层设
> `n_list = [1, 10, 100, 500]`,for 循环依次 fit + score,最后再画图**。

---

## 7. 小项目(若本日有,45 分钟)

**泰坦尼克生存预测(Kaggle 经典入门赛)**:

使用 `pd.read_csv("titanic.csv")` 或 seaborn 内置数据集,完成:

1. 数据预处理: 填充缺失值(`Age`/`Embarked`),把 `Sex`/`Embarked` 转数值。
2. 特征选择: 选 `Pclass`/`Sex`/`Age`/`Fare`/`Embarked` 作为 X,
   `Survived` 作为 y。
3. 分别跑逻辑回归 / 决策树 / 随机森林,对比测试集准确率。
4. 在随机森林上输出特征重要性,讨论"性别是不是决定性因素"。

🔴 **教学红线(分类不平衡只看准确率)**: 泰坦尼克中幸存比例约 38%,若直
接预测"全员遇难"也有 62% 准确率!课后作业引入 `classification_report`
(精确率 / 召回率 / F1)——今天的模型如果一个都不预测"幸存",准确率也可能
很高。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. 把逻辑回归误当回归算法,名字有"回归"实际是分类
  2. 决策树不设 `max_depth`,训练集完美、测试集"翻车"
  3. 随机森林和逻辑回归混用 scale —— 树模型不需要,逻辑回归需要
- **作业说明**: 课后 `homework/task01.py`(Kaggle Titanic 用随机森林跑通,
  准确率 0.78+)、`homework/task02.py`(决策树深度对比实验 + 过拟合可视化)、
  `homework/task03.py`(逻辑回归 vs 决策树 vs 随机森林三大模型横向对比表)。

---

## 易错点

1. **逻辑回归分类任务**: 名字带"回归"但做的是分类,输出概率。
2. **Sigmoid 压到 (0,1)**: 负无穷 → 0,0 → 0.5,正无穷 → 1。
3. **逻辑回归必须 scale**: 基于线性 + 梯度下降,大尺度特征主导损失。
4. **决策树容易过拟合**: `max_depth` 必须调,深度越大越容易记住噪声。
5. **树模型不需要 scale**: 决策树 / 随机森林按阈值分裂,与尺度无关。

## 延伸题

- **决策边界可视化(⭐⭐⭐)**: 在 2D 数据(iris 只取两个特征)上分别跑逻辑
  回归 / 决策树 / 随机森林,画 `contourf` 决策边界,直观感受直线 vs 阶梯
  vs 平滑边界的差异。
- **GridSearchCV 调参(⭐⭐⭐⭐)**: 用 `GridSearchCV` 在决策树上搜索最佳
  `max_depth`(1~20) + `min_samples_leaf`(1~10),看 `cv_results_` 输出。
- **OOB Score 直觉(⭐⭐⭐)**: 随机森林的 `oob_score_` 是在 Bootstrap 抽
  样中"没被抽到的样本"上评估,相当于自带验证集 —— 不需要
  `train_test_split` 就能自动估泛化。