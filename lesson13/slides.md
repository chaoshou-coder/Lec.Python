# Day13 · Pandas 基础(Series/DataFrame/索引)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day11-12 已掌握 NumPy 数组/向量化/统计
> 关键问题: NumPy 数组只能存同类型数据,如何像 Excel 表格一样存"姓名(string)+年龄(int)+成绩(float)"?Pandas 的 DataFrame 就是"带标签的二维表"。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `np.array([1, "a", 3])` 的 dtype 是什么?(`<U11`,全部变成字符串)目的: 唤醒"数组必须同类型"的记忆,引出"现实数据是异构的,需要新工具"。
- **赏玩 demo**(3 分钟): 现场打开一个 CSV 文件(学生成绩表),用 Pandas 一行代码 `pd.read_csv` 加载,打印前 5 行,展示"这就是你们未来每天打交道的核心数据结构"。

---

## 1. 第一讲(15 分钟) —— Series 与 DataFrame 创建

### 知识点 1.1 Series:带索引的一维数组

```python
import pandas as pd

# 从列表创建 Series(自动分配 0-based 索引)
s = pd.Series([10, 20, 30, 40])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 自定义索引
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["b"])  # 20  ← 用标签访问,不像数组只能用数字
```

> Series 就像 Excel 的"一列" —— 有值,有标签(index)。

### 知识点 1.2 DataFrame:二维表格

```python
# 从字典创建(最常用)
data = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [20, 21, 19],
    "成绩": [85.5, 92.0, 78.5]
}
df = pd.DataFrame(data)
print(df)
#   姓名  年龄   成绩
# 0  张三  20  85.5
# 1  李四  21  92.0
# 2  王五  19  78.5
```

> 🔴 教学红线(DataFrame 是"列优先"): 字典的**键 = 列名**,字典的**值 = 列数据**。初学者常把数据按行写(每个子列表是一行),实际应该按列写(每个子列表是一列)。演示错误写法 `pd.DataFrame([["张三", 20, 85.5], ["李四", 21, 92.0]])` —— 这样也能跑,但列名变成 0/1/2,容易混淆。

### 知识点 1.3 从 CSV 文件创建

```python
# 最常用的一行代码
df = pd.read_csv("students.csv")

# 常用参数
df = pd.read_csv("students.csv",
                 encoding="utf-8",   # 编码
                 sep=",",            # 分隔符
                 header=0,           # 第几行是表头
                 index_col=0)        # 第几列作为索引
```

> 🔴 教学红线(编码问题): 中文 Windows 导出的 CSV 常用 GBK 编码,直接 `pd.read_csv("file.csv")` 会报 `UnicodeDecodeError`(references.md §3.3)。解决方案: `pd.read_csv("file.csv", encoding="gbk")`。最佳实践: 统一用 UTF-8,或在读取时尝试 `utf-8` → `gbk` 两种编码。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 从字典创建 DataFrame(含姓名/城市/年龄),打印 Series 和 DataFrame 对比(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `pd.read_csv` 读取本地 CSV,指定 encoding/index_col(⭐⭐,10 分钟)

> 巡场重点: 看学员是否把字典的键写成中文 —— 可以,但建议英文列名(避免后续编码问题)。

---

## 3. 第二讲(15 分钟) —— 基础属性与查看

### 知识点 3.1 基础属性

```python
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

print(df.shape)     # (3, 2)  ← 行数,列数
print(df.dtypes)    # 每列的数据类型
print(df.columns)   # Index(['A', 'B'], dtype='object')
print(df.index)     # RangeIndex(start=0, stop=3, step=1)
```

### 知识点 3.2 快速查看数据

```python
df = pd.read_csv("students.csv")

# 前 5 行(默认)
print(df.head())
print(df.head(10))  # 前 10 行

# 后 5 行
print(df.tail())

# 数据类型 + 非空计数 + 内存占用
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   姓名      100 non-null    object
#  1   年龄      100 non-null    int64
#  2   成绩       95 non-null     float64  ← 有 5 个缺失值!
# dtypes: float64(1), int64(1), object(1)
# memory usage: 2.5+ KB

# 数值列的统计摘要
print(df.describe())
#              成绩
# count  95.000000
# mean   82.347368
# std     8.123456
# min    55.000000
# 25%    78.000000
# 50%    83.000000
# 75%    89.000000
# max    99.000000
```

> `info()` 是**第一步** —— 加载数据后先看 `info()`,发现缺失值、类型错误。`describe()` 看数值分布,发现异常值。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 加载 Titanic 数据集,用 `info()` 找出哪些列有缺失值,用 `describe()` 看年龄分布(⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 查看 DataFrame 的 index/columns/dtypes,修改列名(columns 属性赋值)(⭐⭐,10 分钟)

> 巡场重点: 练习 3 学员常忽略 `info()` 的"Non-Null Count"列 —— 提示:"非空数 < 总数 = 有缺失"。

---

## 5. 第三讲(15 分钟) —— 列选择与行选择

### 知识点 5.1 列选择

```python
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

# 选单列(返回 Series)
print(df["A"])        # Series

# 选多列(返回 DataFrame)
print(df[["A", "B"]]) # DataFrame

# 用点号访问(仅当列名是合法标识符)
print(df.A)           # 等价于 df["A"]
```

### 知识点 5.2 行选择:loc vs iloc

```python
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]},
                  index=["x", "y", "z"])

# loc: 用**标签**选
print(df.loc["y"])       # 选 index="y" 的行
print(df.loc["x":"y"])   # 切片(注意:loc 切片**包含右端**!)

# iloc: 用**位置**选
print(df.iloc[0])        # 选第 0 行
print(df.iloc[0:2])      # 切片(iloc 切片**不包含右端**)

# 同时选行和列
print(df.loc["x":"y", "A"])     # x-y 行的 A 列
print(df.iloc[0:2, 0])          # 第 0-1 行的第 0 列
```

> 🔴 教学红线(loc vs iloc 混淆): 学员常搞混"标签"和"位置"。口诀:**loc = label(标签),iloc = integer(整数位置)**。另外 `loc` 切片包含右端,`iloc` 切片不包含右端 —— 这是 Pandas 最反直觉的设计之一,必须强调。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 用 loc 和 iloc 分别选取指定行/列,对比差异(⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 用 loc 切片选取连续多行多列,验证"loc 包含右端"(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 5 学员常写 `df.loc[0]` —— 如果 index 是默认整数索引,`loc[0]` 和 `iloc[0]` 结果一样;但如果 index 被改成字符串,`loc[0]` 会报错。提示:"loc 永远看标签,iloc 永远看位置"。

## 7. 小项目(若本日有,45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 字典键写成中文列名,后续编码出问题
  2. `loc` 和 `iloc` 混淆,切片右端是否包含搞错
  3. 加载数据后不看 `info()`,错过缺失值警告
- **作业说明**: 课后 `homework/task01.py`(DataFrame 创建)、`homework/task02.py`(数据查看与选择),下节课前 10 分钟复盘。

---

## 易错点

1. **DataFrame 按列构建**: 字典的键 = 列名,值 = 列数据;按行构建需要额外指定 columns。
2. **loc vs iloc**: loc 用标签(切片含右端),iloc 用整数位置(切片不含右端)。
3. **选单列返回 Series,选多列返回 DataFrame**: `df["A"]` 是 Series,`df[["A"]]` 是 DataFrame。
4. **`info()` 必看**: 加载数据后第一件事就是 `info()`,发现缺失值和类型错误。
5. **CSV 编码**: 中文 CSV 常用 GBK 编码,`pd.read_csv("file.csv", encoding="gbk")`。

## 延伸题

> 以下素材来自外部课程(references.md §2.3),教师可按需选用或替换当堂练。

- **(DataCamp Pandas ⭐⭐)**: 用 `read_csv` 加载 Iris 数据集,用 `describe()` 查看各列统计量 —— 巩固数据查看。
- **(Kaggle Learn ⭐⭐⭐)**: 用 loc/iloc 从 Housing 数据集中选取特定行/列 —— 巩固索引。
- **(Pandas 官方文档 ⭐⭐⭐)**: 从 JSON/Excel 多种格式创建 DataFrame —— 拓展数据源。
