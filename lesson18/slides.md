# Day18 · ML 概念与工作流

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-17 已掌握 Python 核心 + 数据处理
>         (NumPy / Pandas / Matplotlib)
> 关键问题: 机器到底怎么"学"?训练集和测试集为什么必须分开?
>          "准确率 99%"一定是好模型吗?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— 处理缺失值有哪三种策略?
>   标准化和归一化公式分别是什么? 目的: 唤醒数据预处理记忆,
>   今天我们把这些"预处理动作"正式串成 ML 流水线。
- **赏玩 demo**(3 分钟): 现场用 1 行代码加载鸢尾花数据集,
>   再 3 行代码训练一棵决策树,打印出 0.97 的准确率。
>   问"这几行黑盒子里到底发生了什么?"吊胃口。

---

## 1. 第一讲(15 分钟) —— 三大范式 + 数据集划分

### 知识点 1.1 监督 / 无监督 / 直觉对比

```python
# 监督学习:数据自带"答案"(标签) —— 像有答案的练习题集
#   例:已知房源特征 + 房价 → 预测新房价(回归)
#   例:已知肿瘤特征 + 良/恶性 → 判断新肿瘤(分类)
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
# X:花萼/花瓣尺寸; y:0/1/2 三种鸢尾花

# 无监督学习:数据没答案 —— 让算法自己找结构
#   例:电商用户分群(聚类)
#   例:高维数据可视化(降维)
from sklearn.datasets import load_digits

digits = load_digits()
Xd, yd = digits.data, digits.target  # 8x8 手写数字图片
```

> 口诀:**有标签 → 监督;没标签 → 无监督;有奖惩 → 强化**。
>
> 强化学习暂时超纲,只记住"像训练动物做动作给零食"即可。

### 知识点 1.2 训练集 / 验证集 / 测试集

```python
from sklearn.model_selection import train_test_split

# 一次切:80% 训练 + 20% 测试
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% 做测试
    random_state=42,    # 固定随机种子,结果可复现
    stratify=y,         # 分层抽样,各类别比例与总体一致
)
print(X_train.shape, X_test.shape)
# (120, 4) (30, 4)  ← 鸢尾花一共 150 条
```

> 为什么要分三份?
> - **训练集**:模型学习参数。
> - **验证集**:调参(选哪棵树、哪个 K)。
> - **测试集**:只准**最后**看一次,模拟真实未见数据。
>
> 🔴 教学红线(数据泄露): 测试集信息在预处理时被"看见" ——
>   比如用**全量数据**的均值/方差做标准化,测试集信息
>   就"泄露"进训练了。正确做法:
>   **fit 只在训练集做,transform 同时作用于训练和测试**。
>   后面练习会演示错误 vs 正确写法。

### 知识点 1.3 random_state 的意义

```python
# random_state=42 不是神秘数字,就是"第 42 种切法"
# 同一 seed → 同一切分 → 不同人代码结果可对比
# 不调 seed → 每次跑准确率都在跳 → 调参无法归因
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用 `load_iris()` 加载数据,
  `train_test_split(test_size=0.2, random_state=42)` 切分,
  打印训练/测试的 shape 与各类别数量(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 对比分层抽样 vs 不开
  `stratify` 时测试集的类别分布差异,直观理解
  `stratify` 的必要性(⭐⭐⭐,15 分钟)

> 巡场重点: 是否写了 `random_state`,没有的话对比不了结果;
> 练习 2 让学员用 `np.bincount(y_test)` 看分布。

---

## 3. 第二讲(15 分钟) —— 过拟合 / 欠拟合 + 偏差方差

### 知识点 3.1 用多项式回归看"拟合程度"

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 30)
y_true = np.sin(x)
y = y_true + np.random.normal(0, 0.3, x.shape)  # 加噪声

X = x.reshape(-1, 1)
x_plot = np.linspace(0, 10, 200).reshape(-1, 1)

for deg, color, label in [
    (1, "green",  "欠拟合(1 次,太简单)"),
    (4, "blue",   "刚好(4 次)"),
    (15, "red",   "过拟合(15 次,记住了噪声)"),
]:
    model = make_pipeline(
        PolynomialFeatures(deg), LinearRegression()
    )
    model.fit(X, y)
    plt.plot(x_plot, model.predict(x_plot),
             color=color, label=label)

plt.scatter(x, y, c="black", s=10, label="训练点")
plt.legend(); plt.show()
```

> 直觉:**欠拟合 = 学得太少;过拟合 = 学得太多,把噪声当规律**。
>
> 测试集上:欠拟合 → 训练/测试都差;
> 过拟合 → 训练极好,测试拉胯。

### 知识点 3.2 偏差-方差权衡(不公式,只直觉)

```python
# 偏差(Bias):模型预测整体偏离真值的程度
#       → 欠拟合来源
# 方差(Variance):模型对训练数据微小波动的敏感度
#       → 过拟合来源
# 总误差 = Bias² + Variance + 不可约噪声
#
# 图示(记住这四格即可):
#             高方差          低方差
#   高偏差    随机猜测        欠拟合
#   低偏差    过拟合          理想模型  ← 目标
#
# 工程直觉:模型复杂度↑ → Bias↓ 但 Variance↑,
# 总误差呈"U 型",目标是最小值点(偏差方差权衡)。
```

> 🔴 教学红线(过拟合幻觉): 训练准确率 99% 不是胜利,
> 可能只是模型把答案背下来了。**永远要看测试集表现**,
> 这是新手最容易踩的坑。

## 4. 当堂练 2(25 分钟)

- 练习 1: `in_class/practice03.py` —— 模仿上面的多项式拟合,
  分别用 degree=1/4/15 拟合 `fetch_california_housing` 子集,
  打印三者在训练集和测试集上的 MSE,观察
  "训练 MSE 越来越低,但 test MSE 先降后升"(⭐⭐⭐,15 分钟)
- 练习 2: `in_class/practice04.py` —— 给出混淆矩阵四个格
  (TP/FP/TN/FN),让学员算 precision / recall(⭐⭐,10 分钟)

> 巡场重点: 练习 1 必须用 `mean_squared_error` 而不是
> accuracy(回归问题);练习 2 提醒 precision = TP/(TP+FP),
> recall = TP/(TP+FN)。

---

## 5. 第三讲(15 分钟) —— 完整 ML 工作流

### 知识点 5.1 七步流水线

```python
# ============ 完整 ML 流程(Classification) ============
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# 1. 数据加载
data = load_iris()
X, y = data.data, data.target

# 2. EDA(探索性分析) ——
#    本节略,用 Pandas 已在 Day 掌握

# 3. 切分(先切分!再做预处理,防止数据泄露)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2,
    random_state=42, stratify=y,
)

# 4. 预处理 —— fit 只在 train,transform 在两边
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)  # fit + transform
X_test_s  = scaler.transform(X_test)       # 只 transform!

# 5. 建模
clf = DecisionTreeClassifier(
    max_depth=3, random_state=42)
clf.fit(X_train_s, y_train)

# 6. 评估
y_pred = clf.predict(X_test_s)
print(classification_report(
    y_test, y_pred,
    target_names=data.target_names))

# 7. 调参(下节讲 GridSearch)
#    + 部署(第 20 天讲 ONNX/Flask)
```

### 知识点 5.2 常见分类器快速一览

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# 五选一替换上面的 clf 即可感受"同数据,不同模型"
classifiers = {
    "逻辑回归": LogisticRegression(max_iter=200),
    "决策树":   DecisionTreeClassifier(max_depth=3),
    "随机森林": RandomForestClassifier(n_estimators=100),
    "SVM":      SVC(kernel="rbf"),
    "KNN":      KNeighborsClassifier(n_neighbors=5),
}
# 跑同样流水线,对比 accuracy
# —— 这个对比就是下次课的主题
```

## 6. 当堂练 3(25 分钟)

- 练习 1: `in_class/practice05.py` —— 用 `load_digits()` 跑一遍
  七步流水线(切分 → 标准化 → 决策树 → 分类报告),
  故意先 `fit_transform(X)` 再切分,看准确率差异(⭐⭐⭐,15 分钟)
- 练习 2: `in_class/practice06.py` —— 用上面的字典跑 5 个分类器,
  输出表格 `[模型名, train_acc, test_acc]`,
  挑出最过拟合的那个(⭐⭐⭐⭐,15 分钟)

> 巡场重点: 练习 1 体感数据泄露 —— 虽然 Iris 这种简单集
> 差异不大,但学员要先建立"先切再预处理"的肌肉记忆;
> 练习 2 提醒 `train_acc >> test_acc` 就是过拟合信号。

---

## 7. 小项目(45 分钟) —— 鸢尾花分类器打包

- **目标**: 把七步流水线封装成 `iris_pipeline(csv_out)` 函数,
  接收任意相同格式的 CSV,返回分类报告字符串 + 模型对象。
- **验收要点**:
  1. `train_test_split(test_size=0.2, random_state=42)` ✅
> 2. `StandardScaler` 仅在训练集 `fit` ✅
> 3. 写出 `classification_report` 到 `report.txt` ✅
> 4. 最后一班展示:不同组对比 `max_depth=3` vs `None` 的
>    train/test accuracy
- **扩展(学有余力)**: 把 5 个分类器对比也写进去,
  用 Matplotlib 画出 bar 图:`accuracies.png`。

> 巡场重点: 埋一个 bug 给学员排查 —— 故意把
> `scaler.fit_transform(X_train)` 写成 `scaler.fit_transform(X)`,
> 让"数据泄露"这个概念从纸上谈兵变成切肤之痛。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. 数据没切分就先标准化 —— 测试集信息泄露,
     评估偏乐观。
  2. 只看训练准确率 —— 可能已经过拟合还自我感觉良好。
  3. 调参时在测试集上反复试 —— 等于把测试集当验证集用,
     最后的分数不可信,该用交叉验证(明天讲)。
- **作业说明**: 3 道 task ——
> 1) 手写一个 `split_then_scale()` 函数对比两种顺序的差异;
> 2) 在 `load_digits` 上跑多项式特征 + 逻辑回归,
>    可视化 degree=1/5/15 的 train/test 曲线;
> 3) 用 California Housing 数据集做回归版完整流水线,
>    输出 RMSE。

---

## 易错点

- **分层抽样忘加 `stratify`**: Iris 这种均衡数据集影响不大,
  但类别严重倾斜时(如欺诈检测 1:99),
  测试集可能直接少了某类。
- **`fit_transform` vs `transform`**: 测试集永远只能 `transform`,
  一旦 `fit` 就等于让模型"看了一眼答案"。
- **`random_state` 不设**: 每次跑准确率乱跳,调参无法归因,
  论文复现也做不了 —— 养成好习惯,切分、模型都设 seed。
- **分类用 accuracy 评估不平衡数据**: 99% 准确率可能只是
  全猜"多数类",下节讲 F1、AUC 补上这块。
- **多项式 degree 过大 + 没标准化**: 高次项数值爆炸,
  可能报 `overflow` 或收敛极慢。

## 延伸题

- **交叉验证**: 自己实现 5 折 CV(`KFold(n_splits=5)`),
  对比单切 test 的 RMSE 方差,
  体会为什么 CV 评估更稳。
- **Pipeline**: `from sklearn.pipeline import Pipeline`,
  把 `Scaler + Classifier` 串成 1 个对象,
  体会为什么生产代码宁可用 Pipeline 也不手写 `fit_transform`。
- **GridSearchCV**: 对 `max_depth` 在 `[1,3,5,None]` 上做网格搜索,
  用 CV 选最优参数,对比"单次切分调参"的方差差异。
- **混淆矩阵可视化**: 用
  `sklearn.metrics.ConfusionMatrixDisplay` 画 heatmap,
  并用中文标注 TP/FP/TN/FN,
  送"最清楚的一次课堂笔记"。