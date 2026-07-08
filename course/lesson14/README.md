# Lesson14 · Pandas 进阶(过滤 / 分组 / 合并 / 透视)

> 前置: Lesson13 已掌握 DataFrame 创建 / 查看 / 选择
> 重点: 多条件筛选、groupby 分组聚合、merge/join、透视表、缺失值处理

## 关键知识点
- 布尔索引多条件过滤:`&` `|` 必须加括号
- `query()` 方法:字符串写条件 + `@` 引用外部变量
- 排序:`sort_values`(单列 / 多列 / 升降序)
- `groupby`:split → apply → combine,`agg` 多聚合函数
- 命名聚合:`新列名=("原列名","函数名")`
- `merge`:inner / left / right / outer 连接 + `on` / `how`
- `concat`:纵向堆叠 / 横向拼接
- `pivot_table`:透视表(行 / 列 / 值 / 聚合函数)
- 缺失值处理:`isnull` / `dropna` / `fillna`(0 / 均值 / 前向)

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 布尔索引多条件筛选 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | query() 重写 + 排序 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | groupby 舱位计算生存率 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | 性别×舱位交叉分组 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 15 分钟 | merge inner/left 对比 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 过滤排序 |
| 2 | `homework/task02.py` | ⭐⭐⭐ | 15 分钟 | 分组聚合 |

## 小 / 中型项目
本节无小项目。

## 阶段复习要点
- 多条件过滤必须加括号 `(df["A"]>1) & (df["B"]<2)`
- merge 后检查 shape:内连接丢行、外连接增行、一对多膨胀
- groupby 后选列 `df.groupby("班级")["成绩"].mean()` 更精确
- `isnull().sum()` 是数据清洗第一步
- `fillna` 默认返回新对象,要 `inplace=True` 或赋值才能修改原数据
