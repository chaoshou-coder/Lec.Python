"""
[难度: ⭐⭐⭐]
[所属知识点: 相似度矩阵]
[预计完成时间: 15 分钟]

场景: 实现 similarity_matrix 函数,接收句子列表,返回 NxN 相似度矩阵,
对角线元素为 1.0。用 numpy 构造与计算。

示例:
    >>> mat = similarity_matrix(["A", "B"])
    >>> mat.shape
    (2, 2)
"""

import numpy as np
from sentence_transformers import SentenceTransformer


_model = SentenceTransformer("all-MiniLM-L6-v2")


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def similarity_matrix(sentences: list) -> np.ndarray:
    """返回句子列表的 NxN 余弦相似度矩阵"""
    # TODO: 对句子批量编码,得到矩阵 E (N, D)
    # TODO: 计算 E 的 L2 范数 (按行)
    # TODO: 归一化得到 E_norm
    # TODO: 相似度矩阵 = E_norm @ E_norm.T
    # TODO: 返回矩阵,对角线应为 1.0
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    sentences = ["猫坐在垫子上", "小猫趴在垫子", "今天阳光很好"]

    # 测试 1: 形状为 NxN
    mat = similarity_matrix(sentences)
    assert mat.shape == (3, 3), f"形状应为 (3,3),实际 {mat.shape}"
    print("测试 1 通过: shape =", mat.shape)

    # 测试 2: 对角线近似 1.0
    diag = np.diag(mat)
    assert np.allclose(diag, 1.0), "对角线应为 1.0"
    print("测试 2 通过: 对角线 =", diag)

    # 测试 3: 矩阵对称
    assert np.allclose(mat, mat.T), "矩阵应是对称的"
    print("测试 3 通过: 矩阵对称")
