"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 数据标准化(向量化)]
[预计完成时间: 20 分钟]

题目描述:
    在机器学习中,数据标准化是常见预处理步骤。

    Z-score 标准化公式:
      X_norm = (X - mean) / std

    请使用 NumPy 向量化运算对一组数据标准化。
    要求: 整个计算过程不能出现显式 for 循环。

    标准化后数据均值应为 0,标准差应为 1。

示例:
    >>> data = np.array([10, 20, 30, 40, 50])
    >>> normalized = standardize(data)
    >>> print(f"均值: {normalized.mean():.4f}")
    均值: 0.0000
    >>> print(f"标准差: {normalized.std():.4f}")
    标准差: 1.0000
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

import numpy as np

def standardize(data):
    """Z-score 标准化"""
    # 提示: (data - data.mean()) / data.std()
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    data = np.array([10, 20, 30, 40, 50])
    # 测试 1: 标准化
    normalized = standardize(data)
    print(f"原始数据: {data}")
    print(f"标准化后: {normalized}")
    # 测试 2: 验证均值和标准差
    print(f"均值: {normalized.mean():.4f}")
    print(f"标准差: {normalized.std():.4f}")
