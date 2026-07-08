# Lesson15 · 数据可视化(Matplotlib / Seaborn)

> 前置: Lesson11-14 已掌握 NumPy / Pandas 数据处理
> 重点: 用代码"画"出折线图、柱状图、散点图、直方图、箱线图、热力图

## 关键知识点
- Matplotlib 基础:`plt.show()` 必须调用
- 四种图形:折线(趋势) / 柱状(比大小) / 散点(关系) / 直方(分布) / 饼图(占比)
- 图表标注:标题 / 轴标签 / 图例 / 颜色 / 网格
- 子图:`plt.subplots` + `axes[i,j]` + `tight_layout`
- Seaborn 高级图表:箱线图 / 热力图 / pairplot
- 图表导出:`savefig`(dpi=300 印刷级,bbox_inches="tight")
- 中文乱码:`plt.rcParams["font.sans-serif"] = ["SimHei"]`

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 折线图 + 标题轴标签 |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | 柱状图 + 调整颜色 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | 1×3 子图(折线/柱状/散点) |
| 4 | `in_class/practice04.py` | ⭐⭐ | 10 分钟 | 图例 / 网格 / 自定义颜色 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 15 分钟 | Seaborn 箱线图 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐ | 15 分钟 | heatmap 相关性热力图 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 基础图形 |
| 2 | `homework/task02.py` | ⭐⭐⭐ | 15 分钟 | Seaborn 高级图表 |

## 小 / 中型项目
本节无小项目。

## 阶段复习要点
- `plt.show()` 必须调用,Jupyter 有 `%matplotlib inline` 除外
- Seaborn 传 DataFrame:`sns.boxplot(x="col1", y="col2", data=df)`
- savefig 放在 show 之前,否则保存空白图(show 会清空画布)
- Seaborn 与 Matplotlib 混用时,多子图用 `set_title()` 而非 `plt.title()`
