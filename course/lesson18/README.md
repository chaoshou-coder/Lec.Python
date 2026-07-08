# Lesson18 · ML 概念与工作流(sklearn 入门)

> 前置: Lesson01-17 已掌握 Python 核心 + 数据处理(NumPy/Pandas/Matplotlib)
> 重点: 机器到底怎么"学"?训练集和测试集为什么必须分开?"准确率 99%"一定是好模型吗?

## 关键知识点
- 三大范式:监督(有标签) / 无监督(没标签) / 强化(有奖惩)
- 数据集划分:`train_test_split`(`test_size` / `random_state` / `stratify`)
- 训练集 / 验证集 / 测试集分工,数据泄露概念
- 过拟合 / 欠拟合:学得太少 vs 把噪声当规律
- 偏差-方差权衡:总误差 = Bias² + Variance + 不可约噪声
- 完整 ML 七步流水线:加载 → EDA → 切分 → 预处理 → 建模 → 评估 → 调参
- 分类器一览:逻辑回归 / 决策树 / 随机森林 / SVM / KNN
- 评估指标:accuracy / precision / recall / F1 / 混淆矩阵

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | load_iris + train_test_split |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | 分层抽样 vs 不开 stratify |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | 多项式拟合 MSE 对比 |
| 4 | `in_class/practice04.py` | ⭐⭐ | 10 分钟 | 混淆矩阵算 precision/recall |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 15 分钟 | 七步流水线 + 数据泄露对比 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 15 分钟 | 5 个分类器对比表格 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | split_then_scale 函数 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | 多项式+逻辑回归可视化曲线 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 20 分钟 | California Housing 回归流水线 |

## 小 / 中型项目
鸢尾花分类器打包:
- 封装 `iris_pipeline(csv_out)` 函数
- 验收:`random_state=42` / StandardScaler 仅在训练集 fit / 输出 classification_report

## 阶段复习要点
- 分层抽样忘加 `stratify`,类别倾斜时测试集可能缺类
- `fit_transform` vs `transform`:测试集永远只能 transform
- `random_state` 不设:每次跑结果不同,调参无法归因
- 分类用 accuracy 评估不平衡数据会误导,需 F1、AUC
- 训练准确率 99% 可能是过拟合幻觉,永远要看测试集
