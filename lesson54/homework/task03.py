"""
[难度: ⭐⭐⭐⭐]
[所属知识点: LangChain 文本切分器]
[预计完成时间: 20 分钟]

用 langchain.text_splitter.RecursiveCharacterTextSplitter
切分一段长文本 → 验证切分结果数量;再调整 chunk_size 对比。

示例:
    >>> split_text(long_text, chunk_size=50)
    切分得到 5 个 chunk
    >>> split_text(long_text, chunk_size=20)
    切分得到 11 个 chunk
"""
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)

def split_text(
    text: str, chunk_size: int = 50, chunk_overlap: int = 0
) -> list:
    """使用 LangChain 切分器切分文本。"""
    # TODO: 实例化 RecursiveCharacterTextSplitter
    # TODO: 调用 split_text 方法返回列表
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    long_text = (
        "Python 是一种广泛使用的高级编程语言。"
        "它的设计哲学强调代码的可读性和简洁性。"
        "Python 支持多种编程范式，包括面向对象、"
        "命令式、函数式和过程式编程。"
    )
    # 测试 1: chunk_size=50
    chunks1 = split_text(long_text, chunk_size=50)
    print(f"size=50 → {len(chunks1)} 个 chunk")
    # 测试 2: chunk_size=20,对比数量
    chunks2 = split_text(long_text, chunk_size=20)
    print(f"size=20 → {len(chunks2)} 个 chunk")
    # 测试 3: 带 overlap
    chunks3 = split_text(
        long_text, chunk_size=30, chunk_overlap=5
    )
    print(f"size=30,overlap=5 → {len(chunks3)} 个 chunk")
