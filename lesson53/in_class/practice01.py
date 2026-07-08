"""
[难度: ⭐]
[所属知识点: sentence-transformers 模型加载]
[预计完成时间: 5 分钟]

场景: 请加载预训练模型 "all-MiniLM-L6-v2" 并返回模型实例。
用 sentence_transformers.SentenceTransformer 加载,打印模型已加载。

示例:
    >>> model = load_model()
    模型已加载: ...SentenceTransformer...
"""

from sentence_transformers import SentenceTransformer


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def load_model():
    """加载并返回 all-MiniLM-L6-v2 预训练模型实例"""
    # TODO: 使用 SentenceTransformer 加载模型 "all-MiniLM-L6-v2"
    # TODO: 打印 "模型已加载: " 与模型对象
    # TODO: 返回模型实例
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 模型加载成功,返回非空对象
    model = load_model()
    assert model is not None, "模型加载失败"
    print("测试 1 通过: 模型加载成功")

    # 测试 2: 模型可正常编码单个句子
    vec = model.encode("测试句子")
    assert vec.shape[0] > 0, "嵌入向量维度应大于 0"
    print("测试 2 通过: 嵌入维度 =", vec.shape[0])
