"""
[难度: ⭐]
[所属知识点: 数组创建]
[预计完成时间: 10 分钟]

题目描述:
    请使用 NumPy 完成以下数组创建:
      1. 用 np.array() 从列表 [1, 2, 3, 4, 5] 创建数组
      2. 用 np.zeros() 创建长度为 5 的全零数组
      3. 用 np.ones() 创建 2x3 的全一数组
      4. 用 np.arange() 创建 0~9 的整数数组

    注意: 需要先 import numpy as np

示例:
    >>> a1 = np.array([1, 2, 3, 4, 5])
    >>> print(a1)
    [1 2 3 4 5]
    >>> a2 = np.zeros(5)
    >>> print(a2)
    [0. 0. 0. 0. 0.]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

import numpy as np

# 任务 1: 从列表创建数组
arr1 = None  # 替换为 np.array([1, 2, 3, 4, 5])

# 任务 2: 全零数组(长度 5)
arr2 = None  # 替换为 np.zeros(5)

# 任务 3: 全一数组(2 行 3 列)
arr3 = None  # 替换为 np.ones((2, 3))

# 任务 4: 0~9 整数数组
arr4 = None  # 替换为 np.arange(10)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 列表创建
    print(f"arr1: {arr1}")
    # 测试 2: 全零
    print(f"arr2: {arr2}")
    # 测试 3: 全一
    print(f"arr3:\n{arr3}")
    # 测试 4: arange
    print(f"arr4: {arr4}")
