# Day14 · Pandas 进阶(过滤/分组/合并/透视)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day13 已掌握 DataFrame 创建/查看/选择
> 关键问题: 如何从 10 万行数据中筛选出"年龄>30 且 城市=北京"的记录?如何按城市分组计算平均工资?多个表如何像 SQL 一样 join?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `df.loc[1:3]` 和 `df.iloc[1:3]` 取的行数一样吗?(不一样,loc 含右端取 3 行,iloc 不含右端取 2 行)目的: 唤醒 loc/iloc 切片差异记忆。
- **赏玩 demo**(3 分钟): 现场用 Titanic 数据集,一行代码 `df[df["Age"] > 60]` 筛选出所有老年乘客,再一行 `df.groupby("Pclass")["Fare"].mean()` 计算各舱位平均票价 —— 展示"数据查询可以如此简洁"。

---

## 1. 第一讲(15 分钟) —— 过滤与排序

### 知识点 1.1 布尔索引:按条件筛选

```python
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 35, 28, 42],
    "城市": ["北京", "上海", "北京", "深圳"]
})

# 单条件:年龄 > 30
print(df[df["年龄"] > 30])
#   姓名  年龄  城市
# 1  李四  35  上海
# 3  赵六  42  深圳

# 多条件:年龄 > 25 且 城市 = 北京
print(df[(df["年龄"] > 25) & (df["城市"] == "北京")])
# 注意:每个条件要用括号,& 表示 and,| 表示 or
```

> 🔴 教学红线(多条件过滤必须加括号): 学员常写 `df[df["年龄"] > 25 & df["城市"] == "北京"]`,报错 `TypeError`。原因: `&` 优先级高于 `>`,Python 会先算 `25 & df["城市"]`。**每个条件必须用括号包起来**(references.md §3.3)。

### 知识点 1.2 query() 方法:用字符串写条件

```python
# 等价于上面的多条件过滤,但更简洁
print(df.query("年龄 > 25 and 城市 == '北京'"))

# 支持变量引用
min_age = 25
print(df.query("年龄 > @min_age"))  # @ 表示引用外部变量
```

### 知识点 1.3 排序

```python
# 按年龄升序
print(df.sort_values("年龄"))

# 按年龄降序
print(df.sort_values("年龄", ascending=False))

# 多列排序:先按城市升序,再按年龄降序
print(df.sort_values(["城市", "年龄"],
                     ascending=[True, False]))
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用布尔索引筛选"成绩 >= 80 且 班级 == 'A'"的学生(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 query() 重写练习 1,再按成绩降序排列(⭐⭐,10 分钟)

> 巡场重点: 看学员是否在多条件时漏写括号 —— 这是本日最高频错误。

---

## 3. 第二讲(15 分钟) —— 分组聚合

### 知识点 3.1 groupby:分组 + 聚合

```python
df = pd.DataFrame({
    "班级": ["A", "B", "A", "B", "A"],
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "成绩": [85, 92, 78, 88, 95]
})

# 按班级分组,计算平均成绩
print(df.groupby("班级")["成绩"].mean())
# 班级
# A    86.0
# B    90.0
# Name: 成绩, dtype: float64
```

> groupby 三步曲:**split(分组) → apply(聚合) → combine(合并)**。

### 知识点 3.2 agg:多聚合函数

```python
# 同时计算多个统计量
print(df.groupby("班级")["成绩"].agg(["mean", "max", "min", "count"]))

# 对不同列应用不同聚合(命名聚合语法)
print(df.groupby("班级").agg(
    平均成绩=("成绩", "mean"),
    最高分=("成绩", "max")
))
```

> 命名聚合语法 `新列名=("原列名", "函数名")` 是 Pandas 0.25+ 的推荐写法,比字典写法更清晰。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 对 Titanic 数据按舱位(Pclass)分组,计算各舱位生存率(Survived 均值)(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 按性别和舱位交叉分组,同时计算平均年龄和生存率(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 3 学员常忘记 `Survived` 是 0/1 编码 —— 均值 = 生存率,这是二分类数据的常用技巧。

---

## 5. 第三讲(15 分钟) —— 合并与透视

### 知识点 5.1 merge:类似 SQL 的 JOIN

```python
df1 = pd.DataFrame({"id": [1, 2, 3], "name": ["张三", "李四", "王五"]})
df2 = pd.DataFrame({"id": [1, 2, 4], "score": [85, 92, 78]})

# 内连接(默认):只保留两边都有的 id
print(pd.merge(df1, df2, on="id"))
#    id name  score
# 0   1  张三     85
# 1   2  李四     92

# 左连接:保留左边所有行
print(pd.merge(df1, df2, on="id", how="left"))
#    id name  score
# 0   1  张三   85.0
# 1   2  李四   92.0
# 2   3  王五    NaN  ← 右边没有,填 NaN
```

### 知识点 5.2 concat:纵向/横向拼接

```python
# 纵向拼接(堆叠,默认 axis=0)
df3 = pd.concat([df1, df1], ignore_index=True)
# ignore_index=True 重新编号,避免索引重复

# 横向拼接(axis=1)
df4 = pd.concat([df1, df2["score"]], axis=1)
```

### 知识点 5.3 pivot_table:透视表

```python
df = pd.DataFrame({
    "日期": ["周一", "周一", "周二", "周二"],
    "城市": ["北京", "上海", "北京", "上海"],
    "销量": [100, 150, 120, 130]
})

# 行=日期,列=城市,值=销量
print(df.pivot_table(index="日期", columns="城市",
                     values="销量", aggfunc="sum"))
# 城市  上海  北京
# 日期
# 周一   150   100
# 周二   130   120
```

> 🔴 教学红线(merge 后行数变化): 初学者常以为 merge 后行数不变。实际: 内连接可能减少(丢缺失匹配),左/右连接可能不变,外连接可能增加(一对多匹配)。merge 后务必检查 `shape`。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 用 merge 合并"学生信息表"和"成绩表",分别用 inner/left 连接观察差异(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 5 学员常忘记 merge 后检查 `shape` —— 提示:"merge 后立刻 print(df.shape),确认行数符合预期"。

---

## 7. 缺失值处理(补充,15 分钟)

### 知识点 7.1 检测与处理缺失值

```python
df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})

# 检测缺失值
print(df.isnull())      # True/False 矩阵
print(df.isnull().sum())  # 每列缺失数量

# 删除含缺失值的行
print(df.dropna())

# 填充缺失值
print(df.fillna(0))           # 填 0
print(df.fillna(df.mean()))   # 填列均值
print(df.fillna(method="ffill"))  # 前向填充(用前一个值)
```

> 缺失值处理是数据清洗的核心 —— 删还是填?填 0 还是均值?取决于业务场景,没有标准答案。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 多条件过滤漏写括号,`&` 优先级导致报错
  2. merge 后不检查 shape,不知道丢了一行
  3. groupby 后忘记选列,`df.groupby("班级").mean()` 会对所有数值列聚合
- **作业说明**: 课后 `homework/task01.py`(过滤排序)、`homework/task02.py`(分组聚合),下节课前 10 分钟复盘。

---

## 易错点

1. **多条件过滤必须加括号**: `(df["A"] > 1) & (df["B"] < 2)`,不能省略括号。
2. **merge 后检查 shape**: 内连接可能丢行,外连接可能增行,一对多会膨胀。
3. **groupby 后选列**: `df.groupby("班级")["成绩"].mean()` 比 `df.groupby("班级").mean()` 更精确。
4. **缺失值检测**: `isnull().sum()` 是数据清洗第一步,不要跳过。
5. **fillna 不修改原数据**: 默认返回新 DataFrame,要 `inplace=True` 或赋值才能修改。

## 延伸题

> 以下素材来自外部课程(references.md §2.3),教师可按需选用或替换当堂练。

- **(DataCamp Pandas ⭐⭐⭐)**: 对超市销售数据做 groupby + agg,计算各品类总销售额和平均单价 —— 巩固分组聚合。
- **(Kaggle Learn ⭐⭐⭐)**: 用 merge 合并订单表和客户表,分析各城市客户消费 —— 巩固合并。
- **(Pandas 官方文档 ⭐⭐⭐⭐)**: 用 pivot_table 制作"月份×产品"销售热力图数据 —— 巩固透视表。
