"""
[难度: ⭐⭐⭐]
[所属知识点: RAG Pipeline 全流程(模拟)]
[预计完成时间: 15 分钟]

完整流程: embedding 函数 mock → chunk → 检索 → 拼接 → 返回完整 prompt。
每个步骤可 print 中间结果。使用 mock 嵌入(哈希取模生成伪向量)。

示例:
    >>> rag_pipeline("hello world 长文本", "hello", 2)
    [打印各步骤中间结果]
    '根据以下上下文回答问题:\\nhello\\nworld\\n\\n问题: hello'
"""
import hashlib
import math

# TODO: mock_embed 生成伪向量(哈希取模)
def mock_embed(text: str, dim: int = 4) -> list:
    """用哈希取模生成 dim 维伪向量。"""
    # 取 md5 前若干字节,归一化到 [-1,1]
    pass

# TODO: cosine_sim 计算余弦相似度
def cosine_sim(a: list, b: list) -> float:
    # 返回 dot(a,b)/(|a||b|),分母为 0 时返回 0.0
    pass

def rag_pipeline(
    doc: str, query: str, k: int = 2, chunk_size: int = 6
) -> str:
    """模拟 RAG 全流程,返回最终 prompt。"""
    # 1. chunk 文档
    # 2. mock_embed 每个 chunk
    # 3. mock_embed query
    # 4. 计算相似度,topk_search
    # 5. build_context
    # 6. 拼接 system prompt + context + question
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常流程
    doc = "Python 是一种编程语言。Java 也是。Rust 较新。"
    print(rag_pipeline(doc, "Python 是什么", k=2))
    # 测试 2: K 大于 chunk 数
    print(rag_pipeline("短", "测试", k=5, chunk_size=2))
    # 测试 3: 空文档
    print(rag_pipeline("", "测试", k=1))
