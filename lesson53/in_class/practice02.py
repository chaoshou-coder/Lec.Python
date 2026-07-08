"""
[难度: ⭐⭐]
[所属知识点: 单句嵌入计算]
[预计完成时间: 10 分钟]

场景: 实现 encode_sentence 函数,把一个中文句子编码为向量(ndarray),
并返回。打印其 shape 与 dtype。

示例:
    >>> vec = encode_sentence("自然语言处理很有趣")
    shape: (384,)  dtype: float32
"""

import numpy as np
from sentence_transformers import SentenceTransformer


# 全局模型(复用,避免重复加载)
_model = SentenceTransformer("all-MiniLM-L6-v2")


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def encode_sentence(sentence: str) -> np.ndarray:
    """将单句编码为向量,打印并返回 ndarray"""
    # TODO: 调用 _model.encode 对 sentence 编码
    # TODO: 打印 "shape: ...  dtype: ..."
    # TODO: 返回嵌入向量
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 中文句子返回 ndarray
    v = encode_sentence("自然语言处理很有趣")
    assert isinstance(v, np.ndarray), "返回值应为 ndarray"
    assert v.ndim == 1, "应为一维向量"
    print("测试 1 通过: 返回一维 ndarray")

    # 测试 2: 再次调用,验证 shape 一致
    v2 = encode_sentence("今天天气很好")
    assert v.shape == v2.shape, "同一模型输出 shape 应一致"
    print("测试 2 通过: 两次 shape 一致 =", v.shape)
