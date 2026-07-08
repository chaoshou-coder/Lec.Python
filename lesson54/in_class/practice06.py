"""
[难度: ⭐⭐⭐⭐]
[所属知识点: RAG 完整系统 + 教学红线]
[预计完成时间: 20 分钟]

实现 MiniRAG 类,封装 chunk + embed + search + generate。
教学红线: 如果 Top-K 过大(导致总 context > max_chars),
应主动截断或 raise ValueError。

示例:
    >>> rag = MiniRAG(max_chars=100)
    >>> rag.index(["chunk1", "chunk2_long_..."])
    >>> rag.generate("问题", k=1)
    '答案上下文...'
"""
import hashlib
import heapq

class MiniRAG:
    """迷你 RAG 系统,封装全流程。"""

    def __init__(self, max_chars: int = 200, dim: int = 4):
        self.max_chars = max_chars
        self.dim = dim
        self.chunks = []
        self.vectors = []

    def _embed(self, text: str) -> list:
        """哈希取模伪向量。"""
        h = hashlib.md5(text.encode()).hexdigest()
        return [
            (int(h[i:i+2], 16) / 127.5 - 1)
            for i in range(0, self.dim * 2, 2)
        ]

    def _cosine(self, a: list, b: list) -> float:
        dot = sum(x*y for x, y in zip(a, b))
        na = sum(x*x for x in a) ** 0.5
        nb = sum(x*x for x in b) ** 0.5
        if na == 0 or nb == 0:
            return 0.0
        return dot / (na * nb)

    def index(self, texts: list):
        """加载并嵌入文档片段。"""
        # TODO: 重置 chunks/vectors,逐个 embed 存入
        pass

    def search(self, query: str, k: int) -> list:
        """返回 top-k 索引列表。"""
        # TODO: embed query,计算相似度,heapq.nlargest
        pass

    def generate(self, query: str, k: int = 2) -> str:
        """检索 + 拼接,超 max_chars 时 raise ValueError。"""
        # TODO: 调用 search,按索引取 chunks
        # TODO: 计算拼接后长度(含换行),超限时 raise
        # TODO: 返回 "上下文:\n" + "\n".join(chunks)
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常检索
    rag = MiniRAG(max_chars=500)
    rag.index(["Python 语言", "Java 语言", "Rust 语言"])
    print(rag.generate("Python", k=1))
    # 测试 2: 触发教学红线(超 max_chars)
    rag2 = MiniRAG(max_chars=5)
    try:
        rag2.generate("测试", k=3)
    except ValueError as e:
        print(f"触发红线: {e}")
    # 测试 3: 空索引
    rag3 = MiniRAG()
    print(rag3.generate("测试", k=1))
