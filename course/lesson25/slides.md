# Day25 · 模型持久化 + ML 项目日

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day24 已掌握模型评估、Pipeline、GridSearchCV;Day18-Day24 已完成整个
  ML 流程训练
> 关键问题: 训练好的模型怎么存、怎么加载、怎么给别人用?Kaggle 项目怎么从
  0 跑到提交?本节**不教新算法,做端到端项目回溯** —— 这是 Module 1 的毕业
  作品。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 不平衡数据看什么指标?Pipeline 和手
  动预处理有什么本质区别?目的: 唤醒 Pipeline 记忆,为今天"持久化 pipeline
  整体"埋伏笔。
- **赏玩 demo**(3 分钟): 展示"训一个模型要 30 分钟,但加载现成模型只要 0.1
  秒" —— 引出 `joblib.dump` / `joblib.load`。

---

## 1. 第一讲(15 分钟) —— 模型持久化:存盘与加载

### 知识点 1.1 为什么需要持久化?

- 模型训练耗时(大模型甚至几天),每次用都重训不现实。
- 模型需要部署给后端工程师 / 产品 / API 调用。
- joblib 比 pickle 更适合大 NumPy 数组(sklearn 官方推荐)。

### 知识点 1.2 joblib.dump / joblib.load

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from joblib import dump, load

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# 存盘(一个文件包含全部参数 + 结构)
dump(model, "iris_model.joblib")
print("模型已保存到 iris_model.joblib")

# 加载
loaded_model = load("iris_model.joblib")
print("预测:", loaded_model.predict([[5.1, 3.5, 1.4, 0.2]]))
# 结果与新训模型完全一致
```

### 知识点 1.3 持久化整个 Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])
pipe.fit(X, y)

# 把 scaler + model 整体 dump
dump(pipe, "iris_pipeline.joblib")
loaded_pipe = load("iris_pipeline.joblib")

# 加载后**直接 predict**(scaler 已内嵌,不需手动 transform)
loaded_pipe.predict([[5.1, 3.5, 1.4, 0.2]])
```

> 🔴 教学红线: 学员常只 dump model 没 dump scaler,加载后拿到原始 X 直接
> predict —— 因为 scaler 没跟着读出,测试集仍是原始尺度,预测失真。**解法:
> dump 整个 Pipeline,而不是只 dump model**。

### 知识点 1.4 共享模型文件的注意点

- **Python / sklearn 版本要匹配**: 旧版 joblib 常不兼容新版 pickle。
- **只加载来源可信的文件**: pickle/joblib 本质是任意代码执行,加载恶意文件
  会被注入攻击(今天不讲安全,但要点到)。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 训 XGBoost on iris,`dump` 保存,另一
  文件 `load` 加载,验证预测一致(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 故意只 dump model 不 dump scaler,感受
  "预测结果不一致"的 bug(⭐⭐⭐,10 分钟)

> 巡场重点: 看学员在练习 2 是否意识到"Pipeline 整体 dump/load"是解法。

---

## 3. 第二讲(15 分钟) —— Kaggle 项目实战:0 到提交

### 知识点 3.1 Kaggle 简介与泰坦尼克项目

Kaggle = 机器学习竞赛社区,泰坦尼克生存预测是初学者 "Hello World" 项目:
根据乘客的 Pclass/Sex/Age/Fare 预测是否生还(二分类)。

评分标准:提交 `PassengerId,Survived` 的 CSV,平台计算 **accuracy**。

### 知识点 3.2 端到端代码骨架(40 行内)

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# 1. 加载(假设已下载 train.csv)
df = pd.read_csv("titanic/train.csv")
X = df[["Pclass", "Sex", "Age", "Fare", "Embarked"]]
y = df["Survived"]

# 2. 划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. 预处理 pipeline
preprocess = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), ["Age", "Fare"]),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder()),
    ]), ["Sex", "Embarked", "Pclass"]),
])

# 4. 建模 pipeline
pipe = Pipeline([
    ("preprocess", preprocess),
    ("model", RandomForestClassifier(n_estimators=200, random_state=42))
])
pipe.fit(X_train, y_train)

# 5. 评估
print(f"测试 accuracy: {pipe.score(X_test, y_test):.4f}")

# 6. 持久化
dump(pipe, "titanic_pipe.joblib")
```

> `Pclass` 虽然是数字但应作为**无序类别**处理 —— 这是泰坦尼克项目的常见认
> 知陷阱。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 跑通上述骨架,提交 Kaggle,目标:
  accuracy ≥ 0.77(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员易把 Pclass 当数值特征(成了权重等比变化),提醒按类别处理。

---

## 5. 第三讲(15 分钟) —— 调参上分:GridSearchCV 调 Titanic

### 知识点 5.1 调参思路

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [3, 5, 7, None],
    "model__min_samples_leaf": [1, 3, 5],
}

grid = GridSearchCV(
    pipe, param_grid, cv=5,
    scoring="accuracy", n_jobs=-1,
)
grid.fit(X_train, y_train)
print(f"测试 accuracy: {grid.score(X_test, y_test):.4f}")
print(f"最佳参数: {grid.best_params_}")
```

### 知识点 5.2 进一步提分的工程技巧(选讲,学有余力者)

1. **特征工程**: 从 `Name` 提取 `Title`(Mr/Mrs/Master/Dr...)。
2. **共乘家庭**: `SibSp + Parch + 1 = family_size`。
3. **甲板信息**: 从 `Cabin` 提取首字母(A/B/C/...)。
4. **模型融合**: lr + xgb + 随机森林投票。
5. **调 Threshold**(0.5 → 0.4 等)优化 accuracy。

> Kaggle 竞赛之所以快乐,是因为"同行 code review + leaderboard 即时反馈" —
> 鼓励学有余力者课后继续刷。

## 6. 当堂练 3(25 分钟)

- 练习 4: `in_class/practice04.py` —— 至少做 1 项上面"提分技巧",看 accuracy
  有没有提升(⭐⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常"改一个 feature 就提交" —— 提示:**一次只改一处**,不然分
> 不清是谁的功劳。

---

## 7. 小项目(若本日有,45 分钟)

**ML 毕业设计 —— 加利福尼亚房价端到端**

组 3 人完成:
1. 数据加载 + EDA(画 3 张图)
2. Pipeline(缩放 + 模型)
3. GridSearchCV 调参(至少调 2 个超参)
4. `dump` Pipeline 到 `.joblib`
5. 加载 `.joblib` 重新预测,验证一致性
6. 提交到 GitHub:`README.md` + 代码 + `model.joblib`

这是 Module 1 的**毕业作品**,直接放作品集。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. 只 dump model 没 dump scaler → 加载后预测失真
  2. 泰坦尼克把 Pclass 当数值特征
  3. Kaggle 提交 CSV 列名写错(`PassengerId` 拼错罚零分)
- **作业说明**: 课后完成上述毕业作品,写一份 README,README 包括以下 6 点:
  (a) 数据描述(b) 建模思路(c) Pipeline 结构(d) GridSearchCV 最佳参数(e)
  测试集评估(f) 模型路径 + 一 Usage 示例。

---

## 易错点

1. **Pipeline 没整体 dump**: 只 dump model,scaler 和编码器丢失,新数据预测全部
  失真。
2. **Kaggle 提交 CSV 列名错误**: 必须 `PassengerId` 和 `Survived`,大小写对。
3. **把 Pclass 当成数值特征**: 它是无序类别,应用 OneHot。
4. **GridSearchCV `n_jobs=-1`**: 用全核并行,速度 xN;别忘写。
5. **测试集也丢进 GridSearchCV**: 必须只在 `X_train` 上调参,hold-out 只用来
   报最终分数。

## 延伸题

- **California Housing 回归版(⭐⭐⭐⭐)**: 用同样的 Pipeline 套路做回归,评
  价指标换为 R² 和 RMSE,用 `Ridge` / `Lasso` 做正则化。
- **MLflow 概述(⭐⭐⭐⭐⭐)**: 工业界常用 MLflow 管理实验 / 参数 / 模型版本。
  —— 后续 AI 课程 Module 3(MLOps)会深入。
- **模型部署入门(⭐⭐⭐⭐⭐)**: 把 `dump` 出的 `.joblib` 包装成一个 Flask/Fast
  API 接口,上传到云端 —— 工程综合大作业素材。
