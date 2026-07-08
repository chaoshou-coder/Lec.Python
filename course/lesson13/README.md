# Lesson13 · Pandas 基础(Series / DataFrame / 索引)

> 前置: Lesson11-12 已掌握 NumPy 数组 / 向量化 / 统计
> 重点: NumPy 只能存同类型数据,Pandas 的 DataFrame 是"带标签的二维表"

## 关键知识点
- Series:带索引的一维数组(像 Excel 的一列)
- DataFrame:二维表格,常用字典创建(键 = 列名,值 = 列数据)
- 从 CSV 创建:`pd.read_csv`(注意 encoding / sep / header / index_col)
- 基础属性:`shape` / `dtypes` / `columns` / `index`
- 快速查看:`head` / `tail` / `info` / `describe`
- 列选择:`df["A"]` 单列(Series) / `df[["A","B"]]` 多列(DataFrame)
- 行选择:`loc`(标签,含右端) vs `iloc`(整数位置,不含右端)

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 字典创建 DataFrame,Series 对比 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | read_csv 指定 encoding/index_col |
| 3 | `in_class/practice03.py` | ⭐⭐ | 15 分钟 | Titanic info() 找缺失值,describe 看年龄 |
| 4 | `in_class/practice04.py` | ⭐⭐ | 10 分钟 | 查看 index/columns/dtypes,修改列名 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 15 分钟 | loc/iloc 对比选取 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐ | 15 分钟 | loc 切片验证"含右端" |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | DataFrame 创建 |
| 2 | `homework/task02.py` | ⭐⭐⭐ | 15 分钟 | 数据查看与选择 |

## 小 / 中型项目
本节无小项目。

## 阶段复习要点
- DataFrame 按列构建,字典键 = 列名
- loc 用标签 / iloc 用整数位置,切片右端规则不同
- 选单列返回 Series,选多列返回 DataFrame
- `info()` 必看:Non-Null Count 找缺失值、类型错误
- 中文 CSV 常用 GBK,读取失败尝试 encoding="gbk"
