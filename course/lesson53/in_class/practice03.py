"""
[难度: ⭐⭐]
[所属知识点: 多句嵌入 + 批量编码]
[预计完成时间: 10 分钟]

场景: 实现 batch_encode 函数,接收句子列表,返回二维 ndarray。
验证 batch_size=2 工作正常。

示例:
    >>> vecs = batch_encode(["我爱 Python", "机器学习", "深度学习"])
    >>> vecs.shape
    (3, 384)
"""

import numpy as np
from sentence_transformers import SentenceTransformer


_model = SentenceTransformer("all-MiniLM-L6-v2")


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def batch_encode(sentences: list) -> np.ndarray:
    """批量编码句子列表,返回二维 ndarray"""
    # TODO: 调用 _model.encode(sentences, batch_size=2)
    # TODO: 返回二维 ndarray
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    sentences = ["我爱 Python", "机器学习", "深度学习"]

    # 测试 1: 返回二维 ndarray,行数等于句子数
    vecs = batch_encode(sentences)
    assert isinstance(vecs, np.ndarray), "应为 ndarray"
    assert vecs.ndim == 2, "应为二维数组"
    assert vecs.shape[0] == 3, "行数应等于句子数量"
    print("测试 1 通过: shape =", vecs.shape)

    # 测试 2: batch_size=2 处理 4 句也不报错
    four = ["A", "B", "C", "D"]
    v4 = batch_encode(four)
    assert v4.shape[0] == 4, "4 句应返回 4 行"
    print("测试 2 通过: 4 句批量编码 shape =", v4.shape)
