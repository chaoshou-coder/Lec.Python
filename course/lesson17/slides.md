# Day17 · EDA 项目(综合实战)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day11-16 已掌握 NumPy/Pandas/可视化/数据摄取
> 关键问题: 面对一个陌生的数据集,如何从零开始"看懂"它?本节用真实数据集走完 EDA(探索性数据分析)全流程 —— 这是数据科学家每天的工作。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `pd.read_csv` 的 `na_values` 参数有什么用?(指定哪些值视为缺失)`response.json()` 返回什么?(解析后的字典/列表)目的: 唤醒数据摄取记忆。
- **赏玩 demo**(3 分钟): 展示一份完整的 EDA 报告(如 Titanic 生存率分析),包含数据概览 → 缺失值处理 → 单变量分布 → 多变量关系 —— 告诉学员"今天你们也能做出这样的报告"。

---

## 1. 第一讲(15 分钟) —— EDA 流程与数据清洗

### 知识点 1.1 EDA 标准流程

EDA(Exploratory Data Analysis)是拿到数据后的第一步,标准流程:

```
1. 数据概览: shape / info() / describe()
2. 缺失值处理: isnull().sum() → fillna / dropna
3. 异常值检测: boxplot / 3σ 原则
4. 类型修正: 字符串转数值、日期解析
5. 特征工程: 创建新特征(如从姓名提取称谓)
```

### 知识点 1.2 数据清洗实战

```python
import pandas as pd

df = pd.read_csv("titanic.csv")

# 第 1 步: 概览
print(df.shape)       # (891, 12) — 891 行 12 列
print(df.info())      # 看哪些列有缺失

# 第 2 步: 处理缺失值
print(df.isnull().sum())
# Age         177  ← 缺失较多
# Cabin       687  ← 缺失太多,考虑删除
# Embarked      2  ← 缺失很少,可以填众数

# Age 用中位数填充(对异常值更鲁棒)
df["Age"].fillna(df["Age"].median(), inplace=True)

# Cabin 缺失太多,直接删列
df.drop("Cabin", axis=1, inplace=True)

# Embarked 用众数填充
df["Embarked"].fillna(df["Embarked"].mode()[0],
                      inplace=True)

# 第 3 步: 类型修正(如有需要)
# df["Date"] = pd.to_datetime(df["Date"])
```

> 🔴 教学红线(`inplace=True` 的陷阱): `inplace=True` 直接修改原数据,不返回新对象。初学者常写 `df2 = df.fillna(0, inplace=True)`,结果 `df2` 是 `None`。正确写法: 要么 `df.fillna(0, inplace=True)`(修改原数据),要么 `df2 = df.fillna(0)`(返回新数据)**二选一**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 加载 Titanic 数据,完成数据概览 + 缺失值统计 + 填充(⭐⭐⭐,15 分钟)
- 练习 2: `in_class/practice02.py` —— 检测 Age 列的异常值(用箱线图 + 3σ 原则),处理异常值(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 1 学员常把 `df["Age"].median()` 写成 `df["Age"].mean()` —— 提示:"有异常值时用 median,没有时用 mean"。

---

## 3. 第二讲(15 分钟) —— 可视化探索与洞察

### 知识点 3.1 单变量分布

```python
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic_clean.csv")

# 数值变量:直方图
df["Age"].hist(bins=30)
plt.title("年龄分布")
plt.show()

# 分类变量:计数柱状图
sns.countplot(x="Pclass", data=df)
plt.title("各舱位人数")
plt.show()
```

### 知识点 3.2 多变量关系

```python
# 生存率按舱位分组
print(df.groupby("Pclass")["Survived"].mean())
# Pclass
# 1    0.63
# 2    0.47
# 3    0.24  ← 头等舱生存率是三等舱的 2.6 倍!

# 可视化
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("各舱位生存率")
plt.show()

# 相关性热力图
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("变量相关性")
plt.show()
```

> EDA 的核心是**回答业务问题**: "谁更可能生存?"→ 按性别/舱位/年龄分组,找规律。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 画出"性别 × 舱位"分组生存率柱状图,写出 2 条洞察(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 画出 Age-Fare 散点图,按生存状态着色,观察规律(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 3 学员常只画图不写洞察 —— 提示:"图是证据,洞察是结论,必须写一句话总结"。

---

## 5. 第三讲(15 分钟) —— 项目报告撰写

### 知识点 5.1 EDA 报告结构

一份完整的 EDA 报告包含以下部分:

```markdown
# XXX 数据集 EDA 报告

## 1. 数据概览
- 数据集大小: X 行 Y 列
- 变量说明: ...

## 2. 数据质量
- 缺失值: Age(177), Cabin(687) → 处理方式
- 异常值: ...

## 3. 关键发现
- 发现 1: 头等舱生存率 63%,三等舱仅 24%
- 发现 2: 女性生存率 74%,男性仅 19%
- 发现 3: 儿童(<10岁)生存率显著高于成人

## 4. 可视化
(插入关键图表)

## 5. 结论与建议
- 总结 3 条核心洞察
- 后续分析方向
```

### 知识点 5.2 报告撰写要点

> 好报告的三个标准:
> 1. **每张图配一句话结论** —— 图不是装饰,是证据
> 2. **洞察要量化** —— "头等舱生存率高"不如"头等舱生存率是三等地的 2.6 倍"
> 3. **讲故事而不是列数字** —— 从"数据是什么" → "为什么" → "怎么办"

## 6. 当堂练 3(综合项目,90 分钟)

### 项目:EDA 报告实战

学员自选数据集(Iris/Titanic/Housing),完成一份完整的 EDA 报告。

**要求**:
1. 数据概览 + 缺失值处理(15 分钟)
2. 至少 3 种不同类型的图表(20 分钟)
3. 至少 3 条量化洞察(15 分钟)
4. 撰写报告(Markdown 格式)(20 分钟)
5. 展示与点评(20 分钟)

**验收 checklist**:
- [ ] 数据加载正确,`info()` 已执行
- [ ] 缺失值已处理(说明处理方式)
- [ ] 至少包含:1 张分布图 + 1 张分组柱状图 + 1 张相关性图
- [ ] 每条洞察有量化数据支撑("X% 的 Y 具有 Z 特征")
- [ ] 报告结构完整,图表配文字说明

> 巡场重点: 学员常陷入"画图 → 没洞察 → 继续画图"的循环。提醒:"画一张图,停下来,写一句话结论,再画下一张"。

## 7. 小项目(若本日有,45 分钟)

本节的小项目就是上面的综合 EDA 报告实战。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. `inplace=True` 和赋值混用,`df2 = df.fillna(0, inplace=True)` 得到 None
  2. 只画图不写洞察,报告=图表堆砌
  3. 用 mean 填充有异常值的列,应该用 median
- **作业说明**: 课后 EDA 报告完善 + 下模块预习,下节课前 10 分钟复盘。

---

## 易错点

1. **`inplace=True` 返回 None**: 要么 `df.xxx(inplace=True)` 要么 `df2 = df.xxx()`,不能混用。
2. **填充策略**: 有异常值时用 median 填充,没有时用 mean;分类变量用众数。
3. **EDA 报告 = 洞察**: 图是证据,结论才是核心,每张图必须配一句话。
4. **corr() 需要 numeric_only**: 混合类型 DataFrame 需要 `df.corr(numeric_only=True)`。
5. **分块读取大数据**: 超大数据集用 `pd.read_csv("f.csv", chunksize=10000)` 分块处理。

## 延伸题

> 以下素材来自外部课程(references.md §2.3),教师可按需选用或替换当堂练。

- **(Kaggle Titanic ⭐⭐⭐)**: 完整 Titanic EDA + 特征工程 —— 巩固 EDA 全流程。
- **(DataCamp EDA ⭐⭐⭐⭐)**: 对 Housing 数据集做完整 EDA,找出影响房价的关键因素 —— 综合应用。
- **(Kaggle Learn ⭐⭐⭐⭐⭐)**: 竞赛级 EDA:从数据清洗到特征工程到建模 —— 进阶挑战。
