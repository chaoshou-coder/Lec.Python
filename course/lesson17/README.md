# Lesson17 · EDA 项目(综合实战)

> 前置: Lesson11-16 已掌握 NumPy / Pandas / 可视化 / 数据摄取
> 重点: 用真实数据集走完 EDA(探索性数据分析)全流程 —— 数据科学家每天的工作

## 关键知识点
- EDA 标准流程:概览 → 缺失值 → 异常值 → 类型修正 → 特征工程
- 数据清洗:`info()` / `isnull().sum()` → `fillna`(均值/中位数/众数) / `dropna`
- `inplace=True` 陷阱:要么 `df.xxx(inplace=True)` 要么 `df2 = df.xxx()`,不能混用
- 单变量分布:直方图(hist) / 分类计数(countplot)
- 多变量关系:groupby 分组聚合 / barplot / 相关性热力图
- EDA 报告结构:概览 → 质量 → 发现 → 可视化 → 结论
- 报告标准:每张图配一句话结论 / 洞察要量化 / 讲故事不堆数字

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐⭐ | 15 分钟 | Titanic 概览 + 缺失值填充 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | 箱线图 + 3σ 异常值处理 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | 性别×舱位生存率分组柱状图 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | Age-Fare 散点图按生存着色 |

## 课后作业
课后完善 EDA 报告,下节前 10 分钟复盘。

## 小 / 中型项目
本节小项目即综合 EDA 报告实战:
- 自选数据集(Iris / Titanic / Housing)
- 数据概览 + 缺失值处理 + 至少 3 种图表 + 3 条量化洞察
- 撰写 Markdown 格式报告

## 阶段复习要点
- `inplace=True` 返回 None,不能赋值
- 有异常值时用 median,没有时用 mean;分类变量用众数
- `corr()` 需要 `numeric_only=True`(混合类型 DataFrame)
- 每张图必须配一句话洞察,报告 ≠ 图表堆砌
- 超大数据集用 `pd.read_csv(..., chunksize=10000)` 分块处理
