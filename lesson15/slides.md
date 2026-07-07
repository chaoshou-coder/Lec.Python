# Day15 · 数据可视化(Matplotlib/Seaborn)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day11-14 已掌握 NumPy/Pandas 数据处理
> 关键问题: 数据处理完了,如何"看见"数据?一张好的图表胜过千行数字 —— 本节学习用代码"画"出折线图、柱状图、散点图、热力图。

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `df.groupby("城市")["GDP"].mean()` 计算的是什么?(各城市平均 GDP)如果想把结果"画成柱状图",需要用什么库?(matplotlib.pyplot)目的: 唤醒数据处理记忆,引出"数据 → 图形"的需求。
- **赏玩 demo**(3 分钟): 现场用 Titanic 数据集,一行代码 `df["Age"].hist()` 画出年龄分布直方图,再一行 `sns.heatmap(df.corr(), annot=True)` 画出相关性热力图 —— 展示"数据可视化让规律一目了然"。

---

## 1. 第一讲(15 分钟) —— Matplotlib 基础:折线/柱状/散点/直方

### 知识点 1.1 基本图形绘制

```python
import matplotlib.pyplot as plt

# 折线图
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)

# 必须调用 show() 显示图表
plt.show()
```

> Matplotlib 的"套路":准备数据 → 调用绘图函数 → 添加标注 → `plt.show()` 显示。

### 知识点 1.2 四种常用图形

```python
import matplotlib.pyplot as plt

x = ["北京", "上海", "广州", "深圳"]
y = [2.1, 2.4, 1.8, 1.6]  # GDP 万亿

# 1. 柱状图(比较各类别大小)
plt.bar(x, y)
plt.title("2024 各城市 GDP")
plt.show()

# 2. 散点图(看两个变量的关系)
height = [160, 165, 170, 175, 180]
weight = [55, 60, 68, 72, 78]
plt.scatter(height, weight)
plt.title("身高体重关系")
plt.show()

# 3. 直方图(看数据分布)
import numpy as np
ages = np.random.normal(30, 5, 1000)  # 1000 个年龄
plt.hist(ages, bins=20)
plt.title("年龄分布")
plt.show()

# 4. 饼图(看占比)
sizes = [30, 25, 25, 20]
labels = ["Python", "Java", "C++", "其他"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("编程语言占比")
plt.show()
```

> 记忆口诀:**折线看趋势,柱状比大小,散点看关系,直方看分布,饼图看占比**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用 `plt.plot` 画出 12 个月的销量折线图,添加标题和轴标签(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `plt.bar` 画出各科平均成绩柱状图,调整颜色(⭐⭐,10 分钟)

> 巡场重点: 看学员是否忘记 `plt.show()` —— 没有这行代码图表不会显示。

---

## 3. 第二讲(15 分钟) —— 图表标注与子图

### 知识点 3.1 图表标注:标题/轴标签/图例/颜色

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label="平方", color="red", linestyle="--")
plt.plot(x, y2, label="线性", color="blue", marker="o")

plt.title("平方 vs 线性", fontsize=16)
plt.xlabel("X 轴", fontsize=12)
plt.ylabel("Y 轴", fontsize=12)
plt.legend()           # 显示图例(依赖 plot 的 label 参数)
plt.grid(True)         # 显示网格
plt.show()
```

> 格式参数速查: `color`="r/g/b/k"(红绿蓝黑), `linestyle`="-/--/-./:"(实线/虚线/点划线/点线), `marker`="o/s/*"(圆/方块/星)。

### 知识点 3.2 子图:subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# 2×2 子图布局,画布大小 10×8 英寸

# 左上角
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title("折线图")

# 右上角
axes[0, 1].bar(["A", "B", "C"], [10, 20, 15])
axes[0, 1].set_title("柱状图")

# 左下角
axes[1, 0].scatter([1, 2, 3], [1, 2, 3])
axes[1, 0].set_title("散点图")

# 右下角
axes[1, 1].hist([1, 1, 2, 2, 2, 3], bins=3)
axes[1, 1].set_title("直方图")

plt.tight_layout()  # 自动调整子图间距
plt.show()
```

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 创建 1×3 子图画出折线/柱状/散点三种图形(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 给图表添加图例/网格/自定义颜色(⭐⭐,10 分钟)

> 巡场重点: 练习 3 学员常把 `axes[0, 0]` 写成 `axes[0][0]` —— 两种写法都可以,但前者是 NumPy 风格更统一。

---

## 5. 第三讲(15 分钟) —— Seaborn 高级图表

### 知识点 5.1 Seaborn 简介

Seaborn 基于 Matplotlib,默认样式更美观,且与 Pandas DataFrame 无缝集成。

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 设置样式
sns.set_theme(style="whitegrid")
```

### 知识点 5.2 常用高级图表

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 加载示例数据集
tips = sns.load_dataset("tips")

# 1. 箱线图(看分布 + 异常值)
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("各天消费箱线图")
plt.show()

# 2. 热力图(看相关性矩阵)
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("变量相关性热力图")
plt.show()

# 3. pairplot(多变量两两关系)
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()
```

> 🔴 教学红线(Seaborn 与 Matplotlib 混用): Seaborn 画图后仍可以用 Matplotlib 添加标题/标签。但注意: `plt.title()` 只对当前子图有效,Seaborn 多子图时要用 `set_title()`。

### 知识点 5.3 图表导出

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
# 导出为图片
fig.savefig("output.png", dpi=300, bbox_inches="tight")
# dpi: 分辨率(300 是印刷级)
# bbox_inches="tight": 裁剪空白边
```

> 📝 导出建议: 屏幕展示用 `dpi=100`,印刷/报告用 `dpi=300`,保存 PNG 格式最通用。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 用 Seaborn 画出 Titanic 数据集的"舱位×性别"生存率箱线图(⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 用 `heatmap` 画出 Iris 数据集相关性热力图,标注数值(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 5 学员常忘记 `data=df` 参数 —— Seaborn 推荐用 DataFrame + 列名写法,而不是传 Series。

## 7. 小项目(若本日有,45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 忘记 `plt.show()`,图表不显示
  2. Seaborn 多子图时用 `plt.title()` 加错标题位置
  3. `savefig` 时忘记 `bbox_inches="tight"`,图片有白边
- **作业说明**: 课后 `homework/task01.py`(基础图形)、`homework/task02.py`(Seaborn 高级图表),下节课前 10 分钟复盘。

---

## 易错点

1. **`plt.show()` 必须调用**: 没有这行代码图表不显示(Jupyter 除外,有 `%matplotlib inline`)。
2. **子图索引**: `axes[0, 0]` 比 `axes[0][0]` 更 NumPy 风格,推荐统一。
3. **Seaborn 传 DataFrame**: 推荐 `sns.boxplot(x="col1", y="col2", data=df)` 而不是传 Series。
4. **中文乱码**: Matplotlib 默认字体不支持中文,需要设置 `plt.rcParams["font.sans-serif"] = ["SimHei"]`。
5. **图表导出**: `savefig` 放在 `show()` 之前,否则会保存空白图(show 会清空画布)。

## 延伸题

> 以下素材来自外部课程(references.md §2.3),教师可按需选用或替换当堂练。

- **(DataCamp Visualization ⭐⭐)**: 画出股票价格折线图 + 移动平均线 —— 巩固折线图。
- **(Seaborn 官方文档 ⭐⭐⭐)**: 用 pairplot 展示 Iris 数据集多变量分布 —— 巩固 pairplot。
- **(Kaggle Learn ⭐⭐⭐⭐)**: 用 Housing 数据集画"面积×价格"散点图 + 趋势线 —— 综合应用。
