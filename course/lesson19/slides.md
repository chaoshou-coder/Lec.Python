# Day19 · 数据预处理

> 本节时长: 6 小时（约 6 节 × 45 分钟）
> 前置: Day01-18 已掌握 Python 核心 + 数据处理
>       （NumPy/Pandas/Matplotlib）+ ML 工作流基础
> 关键问题: 原始数据不能直接喂给模型，
>           如何系统化地完成"脏数据→特征向量"的转换？

---

## 0. 引入（5 分钟）

- **抽问上节**（2 分钟）:
  - train_test_split 的 test_size 一般填多少？（0.2~0.3）
  - 为什么要在训练前把数据随机打乱？（避免数据排序偏差）
- **赏玩 demo**（3 分钟）:
  - 运行 `demo/demo01_titanic_before_after.py`
  - 展示: 同样一个逻辑回归模型，预处理前准确率 62%，
    预处理后准确率 82%，"脏数据浪费了好模型"

---

## 1. 第一讲（15 分钟）—— 缺失值填充

### 知识点 1.1 为什么不能直接删掉缺失行？

- 数据量少时，删一行都是损失
- 缺失往往不是随机的（泰坦尼克: 年龄缺失者死亡率更高）
- 策略: 用**统计量**填充

### 知识点 1.2 SimpleImputer 三种填充策略

```python
from sklearn.impute import SimpleImputer
import numpy as np

X = np.array([[1, 2], [np.nan, 3], [7, 6]])

# 均值填充（适合近似正态分布的数值列）
imp_mean = SimpleImputer(strategy="mean")
print(imp_mean.fit_transform(X))
# [[1. 2.]
#  [4. 3.]      ← (1+7)/2 = 4
#  [7. 6.]]

# 中位数填充（适合有异常值的数值列）
imp_med = SimpleImputer(strategy="median")
print(imp_med.fit_transform(X))

# 众数填充（适合类别列）
imp_freq = SimpleImputer(
    strategy="most_frequent"
)
print(imp_freq.fit_transform(X))
```

> 🔴 教学红线: fit 必须只在训练集上做，
>   否则测试集会"偷看"到全局统计量 —— 数据泄露！

---

## 2. 当堂练 1（20 分钟）

- 练习 1: `in_class/practice01.py` ——
  用 SimpleImputer 对 Oakland 数据集填充缺失值
  （⭐⭐，10 分钟）
- 练习 2: `in_class/practice02.py` ——
  对比 mean / median / most_frequent 三种策略
  对最终模型分数的影响（⭐⭐⭐，15 分钟）

> 巡场重点: 检查学生是否对 X_test 用了 fit_transform，
>   正确做法是 transform（用训练集学到的统计量）

---

## 3. 第二讲（15 分钟）—— 缩放与编码

### 知识点 3.1 StandardScaler vs MinMaxScaler

```python
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler
)

X = np.array([[10, 200], [20, 300], [30, 400]])

# Z-score 标准化: 均值 0、方差 1
# 适合: 数据近似正态 / 模型假设正态（如线性回归）
scaler_z = StandardScaler()
print(scaler_z.fit_transform(X))

# Min-Max 归一化: 缩放到 [0, 1]
# 适合: 数据边界明确 / 神经网络 / KNN
scaler_m = MinMaxScaler()
print(scaler_m.fit_transform(X))
```

### 知识点 3.2 OneHotEncoder vs LabelEncoder

```python
from sklearn.preprocessing import (
    OneHotEncoder, LabelEncoder
)

colors = [["红"], ["蓝"], ["绿"], ["红"]]

# LabelEncoder: 转成 0/1/2
# 仅适合**有序**类别（如 小/中/大）
le = LabelEncoder()
print(le.fit_transform(["小", "中", "大", "中"]))
# [1 2 0 2]

# OneHotEncoder: 每个值独立一列
# 适合**无序**类别（如 红/蓝/绿）
# 🔴 否则模型会误以为 绿 > 蓝 > 红
ohe = OneHotEncoder(sparse_output=False)
print(ohe.fit_transform(colors))
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]
```

> 🟡 树模型（决策树/随机森林）不需要缩放，
>   但线性模型、KNN、SVM 必须缩放

---

## 4. 当堂练 2（25 分钟）

- 练习 3: `in_class/practice03.py` ——
  对 Iris 数据集分别用 StandardScaler
  和 MinMaxScaler，对比 KNN 分数（⭐⭐，10 分钟）
- 练习 4: `in_class/practice04.py` ——
  对泰坦尼克的 Sex/Embarked 列做 OneHot，
  Pclass 列做 Label，观察差异（⭐⭐⭐，15 分钟）

> 巡场重点: OneHotEncoder 要用 sparse_output=False，
>   否则返回稀疏矩阵，学员看不懂

---

## 5. 第三讲（15 分钟）—— ColumnTransformer

### 知识点 5.1 为什么需要 ColumnTransformer？

- 数值列 → 填充 + 标准化
- 类别列 → 填充 + 独热编码
- 用 ColumnTransformer **一次性**绑定不同列到不同流程

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 假设数据有 3 列: age(数值), fare(数值), sex(类别)
num_features = ["age", "fare"]
cat_features = ["sex"]

num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

cat_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("ohe", OneHotEncoder(sparse_output=False)),
])

preprocess = ColumnTransformer([
    ("num", num_pipe, num_features),
    ("cat", cat_pipe, cat_features),
])
```

### 知识点 5.2 Pipeline + 模型端到端

```python
from sklearn.linear_model import LogisticRegression

clf = Pipeline([
    ("prep", preprocess),
    ("model", LogisticRegression(max_iter=1000)),
])

# 一行完成训练
clf.fit(X_train, y_train)
# 一行完成预测
print(clf.score(X_test, y_test))
```

> 🔴 教学红线: 如果把缩放 fit 在整个数据集上
>   再 split 就是数据泄露；Pipeline 天然避免这个错误

---

## 6. 当堂练 3（25 分钟）

- 练习 5: `in_class/practice05.py` ——
  手写 ColumnTransformer 对 California Housing
  分别处理经纬度（缩放）和房间数（缩放）（⭐⭐，10 分钟）
- 练习 6: `in_class/practice06.py` ——
  用 Pipeline 封装预处理 + 随机森林，
  对泰坦尼克预测生存率（⭐⭐⭐⭐，20 分钟）

> 巡场重点: ColumnTransformer 的 remainder 参数，
>   默认丢弃未指定列，可设 "passthrough" 保留

---

## 7. 小项目（若本日有，45 分钟）

- 项目: `mini_project/titanic_pipeline/`
- 目标: 用泰坦尼克公开数据集，
  构建完整预处理 Pipeline（数值 + 类别），
  分别喂给 LogisticRegression / RandomForest / KNN，
  对比三模型准确率
- 验收: 提交 `titanic_pipeline.py` + 结果截图

---

## 8. 总结（5 分钟）

- **本日错 3 件事**:
  1. 在 split 之前做了 fit_transform —— 数据泄露
  2. 对无序类别用 LabelEncoder —— 模型误判大小关系
  3. 对所有列统一用一种预处理方法 ——
     数值列和类别列的处理逻辑完全不同
- **作业说明**:
  - 完成 homework/task01.py ~ task03.py
  - 选做: task04.py（探索不同策略）

---

## 易错点

- SimpleImputer 的 fit 只在 X_train 上做，
  X_test 只能调 transform
- OneHotEncoder 默认返回稀疏矩阵，
  调试时加 `sparse_output=False`
- ColumnTransformer 的 `remainder` 默认 "drop"
  （没指定的列会消失，不怕的话改 "passthrough"）
- 树模型不需要缩放但线性模型必须缩放，
  混淆会导致分数异常低
- get_dummies（pandas）和 OneHotEncoder（sklearn）
  都能独热，但 Pipeline 里用后者才能防泄露

---

## 延伸题

1. 对泰坦尼克 Age 列做**分层填充**:
   按 Pclass 分组后用各自的中位数填充
2. 用 `FunctionTransformer` 自定义对数变换，
   接入 Pipeline 处理 Fare 右偏分布
3. 探索 `KBinsDiscretizer`: 把年龄离散化
   为 "儿童/青年/中年/老年" 四档
4. 对比 drop 一行 vs 中位数填充 vs
   迭代插补(IterativeImputer) 三种缺失策略
   对最终模型 AUC 的影响
