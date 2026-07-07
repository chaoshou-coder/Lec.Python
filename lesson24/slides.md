# Day24 · 模型评估 + 流水线

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day23 已掌握聚类/降维;Day18-Day22 已全面训练过分类模型;Day20 学过线
  性回归评估
> 关键问题: 准确率 99% 一定好吗?模型怎么"一次调参"—— 能不能让预处理+
  建模+调参一条龙自动化?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— 轮廓系数是什么 PCA 解释方差比意义?目
  的: 唤醒降维和聚类评估记忆,为今天"分类模型的全方位评估"做对比。
- **赏玩 demo**(3 分钟): 展示一个"99% 准确率"的模型在 1:100 不平衡数据上
  的实际表现(全猜多数类即可 99%)。问:"这 99% 到底是神话还是谎言?"引出
  **混淆矩阵**和 ROC-AUC。

---

## 1. 第一讲(15 分钟) —— 混淆矩阵 + 准确率 / 精确率 / 召回率 / F1

### 知识点 1.1 混淆矩阵(Confusion Matrix)

```python
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1]

cm = confusion_matrix(y_true, y_pred)
print(cm)
# [[4 1]   ← 真负(TN)=4, 假正(FP)=1
#  [1 4]]  ← 假负(FN)=1, 真正(TP)=4
```

| | 预测负 | 预测正 |
|---|---|---|
| **真实负** | TN(真负) | FP(假正) |
| **真实正** | FN(假负) | TP(真正) |

> 记住口诀:**第一个字母 = 真实?,第二个字母 = 预测?**。T/P/F/N = True/Pre
> dicted/False/Negative。

### 知识点 1.2 4 个核心指标

- **准确率**(Accuracy) = (TP + TN) / 总数
  —— **只在类别均衡时有意义**
- **精确率**(Precision) = TP / (TP + FP)
  —— **"你预测为正的中,多少真的正"**(宁可漏,不要错杀)
- **召回率**(Recall) = TP / (TP + FN)
  —— **"真实为正的中,你捞回多少"**(宁可错杀,不要漏)
- **F1** = 2 × P × R / (P + R)
  —— 精确率和召回率的**调和平均**,综合指标

🔴 **教学红线(不平衡时只看准确率的误导)**: 疾病筛查 10000 人,只有 50 人
得病 —— 模型全猜"没得病",准确率 99.5%,但**召回率 = 0**(一个患者都没捞
回),这种模型在临床上彻底 useless。**结论:不平衡数据首选 F1 或 ROC-AUC**。

类比: 精确率 = "你推荐的商品,用户买了多少?",召回率 = "用户会买的商品,你推
荐了多少?"。

### 知识点 1.3 `classification_report` 一键看全套

```python
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred, target_names=["负", "正"]))
#               precision    recall  f1-score   support
#           负       0.80      0.80      0.80         5
#           正       0.80      0.80      0.80         5
#     accuracy                           0.80        10
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 伪造不平衡数据(95 负 / 5 正),跑逻辑回
  归,看 accuracy 和 F1 差异(⭐⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `classification_report` 输出不平衡
  数据上 lr 和 XGBoost 对比,**讨论哪个 F1 更高**(⭐⭐⭐,15 分钟)

> 巡场重点: 学员常用 `model.score` 拿 accuracy 当唯一指标 —— 提示:"不平衡
> 场景请**永远**先看 F1"。

---

## 3. 第二讲(15 分钟) —— ROC-AUC + 交叉验证

### 知识点 3.1 ROC 曲线 + AUC

ROC 曲线:横轴 FPR(假正率 = FP / 负例总数),纵轴 TPR(真正率 = Recall)。

- AUC = 1:完美分类
- AUC = 0.5:瞎猜
- AUC < 0.5:比瞎猜还差(肯定哪里 bug)

```python
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt

# 使用概率而不是标签
y_prob = model.predict_proba(X_test)[:, 1]
RocCurveDisplay.from_predictions(y_test, y_prob)
plt.title("ROC 曲线")
plt.show()
```

> AUC 本质 = "随机抽一正一负,模型把正的打分高于负的概率"。**AUC 与阈值无
> 关**,综合评价模型在所有阈值下的表现。

### 知识点 3.2 交叉验证(Cross Validation)

单次 train_test_split 依赖切分,运气差就拿到偏。**K-Fold** 切 K 份,每次
用 1 份验证,循环 K 次取平均:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=5, scoring="f1_macro")
print(f"5-Fold F1: {scores.mean():.4f} ± {scores.std():.4f}")
# 5-Fold F1: 0.9600 ± 0.0300  ← 均值高 + 方差小 = 稳
```

> **`cv=5`** 表示 5 折;`scoring` 可以选 `accuracy` / `f1` / `roc_auc` /
> `neg_mean_squared_error` 等。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 在不平衡数据上同时画 lr 和 XGBoost 的
  ROC 曲线,**对比 AUC**(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 用 `cross_val_score` 评估同一模型在
  `cv=3` / `cv=5` / `cv=10` 下的 F1 稳定性(⭐⭐⭐,15 分钟)

> 巡场重点: 学员易把"交叉验证"和"多次 split 取最佳"搞混 —— 提示:**交叉验证
> 取平均**,不是**"挑最好那折当最终模型"**。

---

## 5. 第三讲(15 分钟) —— Pipeline 整合 + GridSearchCV 自动调参

### 知识点 5.1 Pipeline:把预处理和建模串成一条龙

🔴 **教学红线(超参过拟合验证集)**: 超参选得越多,相当于"针对模拟考做专项训
练",验证集被"透视"了。解决:(a) 留 hold-out 做最终测试;(b) 用**嵌套交叉
验证**评估泛化;(c) 调参时别看验证集以外的信息。

Pipeline 保证 train 上 fit,test 上只用 transform(自动防数据泄露):

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
# Pipeline 自动把 scaler 只 fit 到 train,transform train+test
```

### 知识点 5.2 GridSearchCV:网格搜索自动调参

在**指定范围**内暴力试遍所有超参组合,用**交叉验证评分**选最佳:

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "model__C": [0.01, 0.1, 1, 10],         # 逻辑回归正则化强度
    "model__penalty": ["l1", "l2"],          # 正则类型
}
grid = GridSearchCV(pipe, param_grid, cv=5, scoring="f1_macro")
grid.fit(X_train, y_train)

print("最佳参数:", grid.best_params_)
print("最佳 F1:", grid.best_score_)
print("测试集 F1:", grid.score(X_test, y_test))
```

### 知识点 5.3 Pipeline + GridSearchCV 整合 = 工业级 workflow

```python
# 完整工业级流程(预处理在内,绝对不会泄露)
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

param_grid = {
    "scaler": [StandardScaler(), MinMaxScaler()],            # 试两种 scaler
    "model__C": [0.1, 1, 10],
}

grid = GridSearchCV(pipe, param_grid, cv=5, scoring="f1_macro")
grid.fit(X_train, y_train)
print("最终最佳:", grid.best_params_)
```

> 这个 workflow: 调参在 **5-Fold CV 内**完成,数据从不泄露;最后 `grid.score`
> 评估 hold-out 测试集,给一个公正的最终分数。**这就是 Day4 以来所有主题的
> 最终归宿**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 加利福尼亚房价二值化数据集: 构建
  `Pipeline(scaler + LogisticRegression)`,用 `GridSearchCV` 调 `C` 和 `penalty`
  ,输出最佳参数和测试集 F1(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常把 `GridSearchCV` 的 `best_score_` 误认为是测试集分数 ——
> 提示:**`best_score_` 是 cv 平均验证分数**,要再调用 `grid.score(X_test,
> y_test)` 才是 hold-out 公评分。

---

## 7. 小项目(若本日有,45 分钟)

**完整评估 + 调参挑战赛**:

给加利福尼亚房价二值化数据集,每组:
1. 常规训练,输出 `classification_report` + AUC
2. 用 `cross_val_score` 评估稳定性
3. 用 `Pipeline + GridSearchCV` 自动调参
4. 在白板写下:(a) 最佳参数(b) cv 平均 F1(c) 测试集 F1(d) 是否过拟合

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. 不平衡数据用 accuracy 做唯一指标(应该用 F1 / AUC)
  2. `GridSearchCV.best_score_` 当成测试分数报告
  3. Pipeline 之外单独 fit scaler 导致数据泄露
- **作业说明**: 课后 `homework/task01.py`(Kaggle Titanic 上线:用
  `Pipeline + GridSearchCV` 跑完整流程,提交 kaggle 看分)、`homework/task02.py`
  (对比 lr/svm/xgb 在不平衡数据上的 ROC 曲线)。

---

## 易错点

1. **accuracy 在不平衡数据上彻底失信**: 首选 F1 / ROC-AUC。
2. **`precision` vs `recall` 搞混**: precision 看预测正中有多少真,recall 看
   真中有多少被你捞回。
3. **GridSearchCV 泄漏**: 把全数据 fit 了再调参 = 测试集也参与了选模型;一定
  要在 split 之后才 `grid.fit(X_train, y_train)`。
4. **`best_score_` 是 cv 均值**: 要单独再评 hold-out 测试集才是最终分数。
5. **Pipeline 里 scaler 会多次 fit**: GridSearchCV 会重新 cv 切分,每次 scaler
   在该折的训练部分重新 fit —— 这**不是**泄漏,是**正确行为**。

## 延伸题

- **混淆矩阵可视化(⭐⭐⭐)**: 用 `ConfusionMatrixDisplay` 画热力图,annot=True
  把数字写在格子里。
- **RandomizedSearchCV(⭐⭐⭐⭐)**: 超参太多时 `GridSearchCV` 太慢;随机采样 N
  组组合,90% 效果、10% 时间 —— 工业界常用。
- **嵌套交叉验证(⭐⭐⭐⭐⭐)**: 外层评估泛化,内层调超参,彻底解决"验证集过拟
  合"问题 —— 读 sklearn 官方 Nested CV 教程。
