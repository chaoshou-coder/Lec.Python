"""
[难度: ⭐]
[所属知识点: 数组属性(dtype/shape/ndim)]
[预计完成时间: 10 分钟]

题目描述:
    给定一个 NumPy 数组,请输出它的三个核心属性:
      - dtype: 数据类型(如 int64, float64)
      - shape: 形状(各维度大小)
      - ndim: 维度数(几维数组)

    请分别创建一维、二维、三维数组并查看属性。

示例:
    >>> arr = np.array([[1, 2, 3], [4, 5, 6]])
    >>> print(arr.dtype)
    int64
    >>> print(arr.shape)
    (2, 3)
    >>> print(arr.ndim)
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

import numpy as np

# 一维数组
arr1 = np.array([1, 2, 3, 4, 5])
# 二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# 三维数组
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# 在此打印各数组的属性
# 提示: print(f"dtype: {arr.dtype}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    for i, arr in enumerate([arr1, arr2, arr3], 1):
        print(f"--- arr{i} ---")
        print(f"dtype: {arr.dtype}")
        print(f"shape: {arr.shape}")
        print(f"ndim: {arr.ndim}")
