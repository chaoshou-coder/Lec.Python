"""
[难度: ⭐⭐]
[知识点: 余弦相似度计算]
[预计完成时间: 10 分钟]

场景: 实现 cosine_sim 函数(不用 sklearn,用 numpy 手动实现),
计算两个向量的余弦相似度,结果 float 保留四位小数。

示例:
    >>> a = np.array([1.0, 0.0])
    >>> b = np.array([0.0, 1.0])
    >>> cosine_sim(a, b)
    0.0
"""

import numpy as np


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    """手动用 numpy 计算两个向量的余弦相似度"""
    # TODO: 计算点积 a·b
    # TODO: 计算两个向量的 L2 范数
    # TODO: 返回 点积 / (范数a * 范数b),保留 4 位小数
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正交向量相似度为 0
    a = np.array([1.0, 0.0])
    b = np.array([0.0, 1.0])
    assert cosine_sim(a, b) == 0.0, "正交向量应返回 0.0"
    print("测试 1 通过: 正交向量 = 0.0")

    # 测试 2: 相同向量相似度为 1
    c = np.array([1.0, 2.0, 3.0])
    assert cosine_sim(c, c) == 1.0, "相同向量应返回 1.0"
    print("测试 2 通过: 相同向量 = 1.0")

    # 测试 3: 反向向量相似度为 -1
    assert cosine_sim(c, -c) == -1.0, "反向向量应返回 -1.0"
    print("测试 3 通过: 反向向量 = -1.0")
