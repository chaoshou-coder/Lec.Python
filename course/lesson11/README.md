# Lesson11 · NumPy 基础(数组 / 广播 / 向量化)

> 前置: Lesson01-10 已掌握 Python 核心(变量 / 容器 / 函数 / 文件 / 异常)
> 重点: 为什么 Python 原生列表做数值运算慢?NumPy 如何用向量化加速 10-100 倍

## 关键知识点
- 数组创建:`np.array` / `np.zeros` / `np.ones` / `np.arange` / `np.linspace`
- 数组属性:`dtype` / `shape` / `ndim` —— 数组的"身份证"
- 向量化运算:告别 for 循环,整批处理
- 广播(broadcasting):不同形状也能算,从最后一个维度对齐
- 索引与切片:布尔索引、`:` 取所有行/列
- `reshape` 改变形状(注意视图 vs 副本)
- 常用数学函数:`np.sqrt` / `np.exp` / `np.log` / `np.mean` / `np.sum`

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | np.arange + reshape,打印 shape/dtype |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | zeros/ones 创建指定形状数组 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | 切片取子矩阵 + 布尔索引取偶数 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | 广播实现行减最小值(keepdims) |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | 随机数统计 + reshape 按行求和 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 数组创建与属性 |
| 2 | `homework/task02.py` | ⭐⭐⭐ | 15 分钟 | 向量化运算 |

## 小 / 中型项目
本节无小项目。

## 阶段复习要点
- 数组 dtype 隐式转换(混合 int/float → float,混合数字/字符串 → 字符串)
- 形状参数必须传元组 `np.zeros((2, 3))`
- 广播规则 + `keepdims=True` 保持可广播形状
- reshape 返回视图,修改可能影响原数组,独立副本用 `.copy()`
