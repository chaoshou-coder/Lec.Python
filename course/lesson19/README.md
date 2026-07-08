# Lesson19 · 数据预处理(sklearn)

> 前置: Lesson01-18 已掌握 Python 核心 + 数据处理 + ML 工作流
> 重点: 原始数据不能直接喂给模型,如何系统化完成"脏数据→特征向量"的转换?

## 关键知识点
- `SimpleImputer` 三种填充:mean(正态) / median(有异常值) / most_frequent(类别)
- fit 只在训练集做,测试集只能 transform,否则数据泄露
- 缩放:`StandardScaler`(Z-score,均值 0 方差 1) vs `MinMaxScaler`([0,1])
- 编码:`LabelEncoder`(有序) vs `OneHotEncoder`(无序,每个值独立一列)
- 树模型不需要缩放,但线性模型 / KNN / SVM 必须
- `ColumnTransformer`:不同列绑定不同流程(num + cat)
- `Pipeline`:预处理 + 模型端到端,天然防止数据泄露
- `remainder="passthrough"` 保留未指定列

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | SimpleImputer 填充缺失值 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | 三种填充策略对模型影响 |
| 3 | `in_class/practice03.py` | ⭐⭐ | 10 分钟 | StandardScaler vs MinMaxScaler + KNN |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | OneHot / Label 编码对比 |
| 5 | `in_class/practice05.py` | ⭐⭐ | 10 分钟 | ColumnTransformer 手写 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 20 分钟 | Pipeline + 随机森林泰坦尼克 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 综合预处理练习 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | Pipeline 端到端建模 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 20 分钟 | 多模型对比 |

## 小 / 中型项目
`mini_project/titanic_pipeline/`:
- 泰坦尼克完整预处理 Pipeline(数值 + 类别)
- 分别喂给 LogisticRegression / RandomForest / KNN
- 对比三模型准确率

## 阶段复习要点
- SimpleImputer fit 只在 X_train,X_test 只能 transform
- OneHotEncoder 默认返回稀疏矩阵,调试加 `sparse_output=False`
- ColumnTransformer `remainder` 默认 "drop",没指定的列会消失
- 树模型不需要缩放但线性模型必须,混淆导致分数异常低
- Pipeline 天然防数据泄露,生产代码首选
