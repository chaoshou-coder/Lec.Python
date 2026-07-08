# Day22 · 梯度提升 + SVM 直觉

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day21 已掌握逻辑回归、决策树、随机森林;Day20 学过梯度下降直觉
> 关键问题: 随机森林是很多树"并排投票",还有另一种"串序修正错误"的集成功
  法是什么?为什么 SVM 叫"最大间隔分类器",这和 lr 有什么本质不同?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 随机森林的"双重随机"是什么决策树为
  什么容易过拟合?目的: 唤醒树模型记忆,为今天"串序+残差拟合"的梯度提升铺
  路。
- **赏玩 demo**(3 分钟): 在 2D 线性不可分数据(异或问题)上分别跑 lr、决策树、
  随机森林,展示决策边界。问:"这 3 个全崩了 —— 有什么算法能处理这种'曲
  线边界'?"引出 SVM 核技巧。

---

## 1. 第一讲(15 分钟) —— XGBoost / LightGBM:加法模型 + 残差拟合直觉

### 知识点 1.1 Boosting vs Bagging

- **Bagging**(随机森林): 多棵树**并排**训练(各自独立),最终投票。
- **Boosting**(XGBoost): 多棵树**串序**训练,每棵修上一棵的**残差**(错误),
  最终加权求和。

类比: Bagging = 问 10 个专家取平均值;Boosting = 请 1 个老师先考一次,把做
错的题重点讲,再考一次,反复提分。

### 知识点 1.2 残差拟合直觉("每次盯住错题本")

🔴 **教学红线(梯度提升只做直觉,不推公式)**: 学员容易陷入"残差 = 梯度"的
推导细节,本节**只讲直觉流程**:

1. 第 1 棵树:在所有数据上拟合,得到预测 ŷ₁。
2. 算残差 `r₁ = y - ŷ₁`(真实 - 预测 = 模型搞错的部分)。
3. 第 2 棵树:**在残差 r₁ 上拟合**,让这棵树专门"修上一棵的 bug"。
4. 第 3 棵树在 r₂ 上拟合,...直到 n 棵树全部训完。
5. 最终预测:ŷ = ŷ₁ + ŷ₂ + ... + ŷₙ(累加模型)。

> 板书画一条"收敛曲线":树越多 → 残差越小 → 预测越准 → 最终在训练集上
> "完美拟合"(过拟合风险!)。强调:**这就是为什么 Boosting 需要 early_stopping
> 防过拟合**。

### 知识点 1.3 XGBClassifier / LGBMClassifier 实战

```python
from xgboost import XGBClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# n_estimators = 树的数量;max_depth = 每棵树深度
model = XGBClassifier(
    n_estimators=100, max_depth=3,
    use_label_encoder=False, eval_metric="mlogloss"
)
model.fit(X_train, y_train)
print(f"XGBoost 准确率: {model.score(X_test, y_test):.4f}")

# LightGBM(工业界更省显存、更快)
from lightgbm import LGBMClassifier
model2 = LGBMClassifier(n_estimators=100, max_depth=3)
model2.fit(X_train, y_train)
print(f"LightGBM 准确率: {model2.score(X_test, y_test):.4f}")
```

> 提前告知:XGBoost / LightGBM 不是 sklearn 自带,需要 `pip install xgboost
> lightgbm`。安装失败时本节可用 sklearn 的 `GradientBoostingClassifier` 替代。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 安装并运行 XGBoost on iris,调
  `n_estimators=10/50/200` 看准确率变化(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 小样本数据用 XGBoost 故意设
  `n_estimators=500, max_depth=10`,与正则化版(`max_depth=3,learning_rate=0.01`)
  **对比**训练/测试准确率,体会过拟合(⭐⭐⭐⭐,15 分钟)

> 巡场重点: 学员易把 `learning_rate` 当成"学习越快越好" —— 强调:**小学习
> 率 + 多树**往往比**大学习率 + 少树**更稳。

---

## 3. 第二讲(15 分钟) —— SVM:最大间隔 + 核技巧直觉

### 知识点 3.1 最大间隔直觉

逻辑回归找"能分开就行"的线;SVM 找"离两类**都最远**"的线 —— 即最大化支持
向量到决策边界的**间隔**(margin)。

类比:在两排人之间修一条路,最宽的修法是"刚好让离路最近的人能侧身过" —— 那
两个"最近的人"就是**支持向量**。

### 知识点 3.2 支持向量

只有支持向量(离分界线最近的几个点)影响决策边界。**移走其他点,边界不变**。

> 直觉: SVM 非常"节俭",整个模型只依赖少数几个样本,所以它对噪声有天然
> 的鲁棒性(相应的,换几个支持向量,整个模型可能变)。

### 知识点 3.3 核技巧:把数据"投射"到高维讲直觉

🔴 **严格边界 —— 本课不讲对偶,只讲直觉**: 线性不可分数据(异或问题),在 2D
上找不到直线。核函数把数据映射到高维空间(比如 3D),在 3D 上能切一个平面。

```python
# SVM 三件套:线性 / 多项式核 / RBF 核
from sklearn.svm import SVC

linear = SVC(kernel="linear")
poly = SVC(kernel="poly", degree=3)   # 多项式核
rbf = SVC(kernel="rbf")               # 高斯核(默认,也最常用)
```

| 核 | 适用场景 |
|---|---|
| `linear` | 数据线性可分 / 高维稀疏(如文本 TF-IDF) |
| `poly` | 特征交互重要的问题(degree 决定多项式次数) |
| `rbf` | **默认首选**,几乎总能 work,但解释性差 |

### 知识点 3.4 SVM 必须做缩放!

SVM 基于"距离"(间隔 = 两点距离),特征尺度直接影响边界位置。**不 scale 的
SVM 几乎肯定表现差**。

```python
# 标准流程
X_train_scaled = StandardScaler().fit_transform(X_train)
X_test_scaled = StandardScaler().fit_transform(X_test)  # ← 错误写法!
# 正确:scaler = StandardScaler().fit(X_train)
#      X_test_scaled = scaler.transform(X_test)
```

> 🔴 教学红线: SVM 是"必须 scale"的典型代表,学员常把它和树模型搞混。对
> 比:
> - **必须 scale**: lr、逻辑回归、SVM、KNN、神经网络
> - **不必 scale**: 决策树、随机森林、XGBoost

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 在 2D 异或数据(手动造 4 个簇)上分别跑
  SVC(kernel="linear") 和 SVC(kernel="rbf"),画决策边界对比(⭐⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— SVC on 加利福尼亚房价(二值化),分别
  对比"不 scale"和"scale"的准确率差异(⭐⭐⭐,10 分钟)

> 巡场重点: 学员画异或数据时需手动造 4 簇对角对称数据:
> ```
> (0,0) (1,1) = 类0
> (0,1) (1,0) = 类1
> ```

---

## 5. 第三讲(15 分钟) —— 四大分类器横向对比

### 知识点 5.1 一张表看差异

| 模型 | 决策边界 | 必 scale? | 适合的数据规模 | 可解释性 |
|---|---|---|---|---|
| 逻辑回归 | 直线/超平面 | ✅ | 大 | 高(看 coef_) |
| 决策树 | 阶梯曲线 | ❌ | 中 | 极高(plot_tree) |
| 随机森林 | 平滑曲线 | ❌ | 中 | 中(importance) |
| XGBoost | 平滑曲线 | ❌ | 中 | 中(importance) |
| SVM(rbf) | 任意曲线 | ✅ | 小样本 | 低 |

### 知识点 5.2 为什么工业界偏爱 XGBoost?

- 训练快,效果好,对缺失值鲁棒,可并行。
- Kaggle 竞赛获奖方案 ~70% 用 XGBoost / LightGBM。

> 但逻辑回归在小样本 + 高维文本上仍是 baseline 首选(配合 TF-IDF),不要一刀
> 切。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 在同一个数据集上跑 5 种分类器,汇总
  `model.score(X_test, y_test)` 和训练时间 `time.perf_counter()`,做横比表
  (⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常忽略"不 scale 跑 SVM 是 bug",导致 SVM 分数被错误拉低。提
> 示:**scale 之后所有距离模型,SVM 才会恢复真实水平**。

---

## 7. 小项目(若本日有,45 分钟)

**分类器选型挑战赛**:

给 3 个数据集:
1. 大样本连续特征(加利福尼亚房价二值化)
2. 小样本高维稀疏(iris + 加噪声特征)
3. 线性不可分(异或 + 高斯噪声)

每组讨论"该选什么模型",跑一遍验证假设,解释选择理由。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. SVM 不做 scale(直接"砸锅")
  2. XGBoost learning_rate 设太大,不收敛
  3. 把 "kernel trick" 当成"其实是把数据映射到高维再做线性 SVM"(只讲直觉,
     不扣定义)
- **作业说明**: 课后 `homework/task01.py`(Kaggle Titanic 用 XGBoost 跑通,准
  确率要在 0.80+)、`homework/task02.py`(SVM 三核横向对比 + 可视化边界)。

---

## 易错点

1. **SVM 必须 scale**: 它是距离尺度的模型,否则大尺度特征直接主导间隔。
2. **Boosting vs Bagging**: Boosting 串序修残差,Bagging 并排投票。XGBoost 是
   Boosting,随机森林是 Bagging —— 别搞混。
3. **XGBoost early_stopping**: 一定要设 `eval_set` + `early_stopping_rounds`,
   不然容易过拟合。
4. **SVM 在大样本上慢**: `SVC` 内部是 O(n²~n³),万级别样本就用 LinearSVC 或
   转 XGBoost。
5. **把 RBF 核当万能**: RBF 在小样本上效果好,但在工业大数据上 XGBoost 更实
   际。

## 延伸题

- **核技巧的可视化(⭐⭐⭐)**: 搜 "kernel trick visualization",看 2D 线性不
  可分数据如何被 RBF 核"拉直"。
- **学习率与 n_estimators 权衡实验(⭐⭐⭐⭐)**: `lr=0.1,n_estimators=100`
  对比 `lr=0.01,n_estimators=1000`,**对比**测试分数,体会"小步快跑 > 大
  步颠簸"。
- **SVM 对偶入门(⭐⭐⭐⭐⭐)**: 对学有余力的同学,推荐 Andrew Ng 笔记 Section
  7 —— 跳过拉格朗日推导,只重点看"`αᵢ ≠ 0` 的样本才是支持向量"这一结论。
