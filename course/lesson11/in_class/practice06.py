"""
[难度: ⭐⭐]
[所属知识点: 统计函数(mean/sum/std/argmax)]
[预计完成时间: 15 分钟]

题目描述:
    给定一组学生成绩,请使用 NumPy 统计函数计算:
      1. mean(): 平均分
      2. sum(): 总分
      3. std(): 标准差
      4. argmax(): 最高分的索引

    这些函数对整个数组一次性计算,无需循环。

示例:
    >>> scores = np.array([78, 85, 92, 67, 88])
    >>> print(f"平均分: {scores.mean():.2f}")
    平均分: 82.00
    >>> print(f"最高分索引: {scores.argmax()}")
    最高分索引: 2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

import numpy as np

scores = np.array([78, 85, 92, 67, 88, 73, 95, 81])

# 任务 1: 平均分
avg = None  # 替换为 scores.mean()

# 任务 2: 总分
total = None  # 替换为 scores.sum()

# 任务 3: 标准差
std = None  # 替换为 scores.std()

# 任务 4: 最高分索引
max_idx = None  # 替换为 scores.argmax()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    print(f"成绩: {scores}")
    print(f"平均分: {avg:.2f}")
    print(f"总分: {total}")
    print(f"标准差: {std:.2f}")
    print(f"最高分索引: {max_idx}")
    print(f"最高分: {scores[max_idx]}")
