"""
[难度: ⭐]
[所属知识点: Q/K/V 手算注意力得分]
[预计完成时间: 5 分钟]

给定 Q = [[1, 0]], K = [[1, 0], [0, 1]], 用 numpy 手算 QK^T
得到注意力得分矩阵 scores,形状为 (1, 2)。
要求: 只计算矩阵乘法,不做 softmax 和缩放。

示例:
    >>> scores = compute_qk(Q, K)
    >>> print(scores)
    [[1 0]]
"""

import numpy as np

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def compute_qk(Q, K):
    """计算 Q 与 K 转置的矩阵乘积"""
    return pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    Q = np.array([[1, 0]])
    K = np.array([[1, 0], [0, 1]])
    # 测试 1
    scores = compute_qk(Q, K)
    print("scores:\n", scores)
    # 测试 2: 增大 Q 维度
    Q2 = np.array([[1, 0], [0, 1]])
    scores2 = compute_qk(Q2, K)
    print("scores2:\n", scores2)
    pass
