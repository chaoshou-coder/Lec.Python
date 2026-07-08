# Lesson12 · NumPy 进阶(线性代数 / 随机数 / 统计)

> 前置: Lesson11 已掌握 NumPy 数组创建 / 向量化 / 广播 / 索引
> 重点: 矩阵乘法 vs 逐元素乘法、按行/按列聚合、随机数可复现

## 关键知识点
- 矩阵乘法:`np.dot` / `@` 运算符,与逐元素乘法 `*` 的区别
- 线性代数:`a.T` 转置 / `np.linalg.det` / `np.linalg.inv` / `np.linalg.eig`
- 聚合函数:`sum` / `mean` / `std` / `max` / `min` / `argmax`
- axis 参数:`axis=0` 跨行(剩列)、`axis=1` 跨列(剩行)
- 随机数生成:`np.random.seed` / `rand` / `randn` / `normal` / `randint`
- 文件读写:`np.save` / `np.load` / `np.savez` / `loadtxt` / `savetxt`

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 两种乘法对比,验证结果不同 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | 行列式 + 逆矩阵,验证 A@inv(A)=I |
| 3 | `in_class/practice03.py` | ⭐⭐ | 15 分钟 | 成绩矩阵按人/按科聚合 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 15 分钟 | 正态分布随机数验证均值/标准差 |
| 5 | `in_class/practice05.py` | ⭐⭐ | 15 分钟 | .npy/.csv 保存加载验证 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐ | 15 分钟 | loadtxt 读取含表头 CSV |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | 矩阵运算 |
| 2 | `homework/task02.py` | ⭐⭐⭐ | 15 分钟 | 统计计算 |

## 小 / 中型项目
本节无小项目。

## 阶段复习要点
- `*` 对位乘 vs `@` 行乘列,矩阵乘法不满足交换律
- axis 方向口诀:"axis=0 跨行 → 剩列"
- 随机种子保证可复现,机器学习实验必须设 seed
- 读取中文 CSV 指定 `encoding="utf-8"` 或 `"gbk"`
