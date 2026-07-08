"""
[难度: ⭐⭐⭐]
[所属知识点: RAG + Agent 协作]
[预计完成时间: 15 分钟]

场景: RetrievalTool 封装 + Agent 调用 tool
获取知识 → 回答, mock 实现, 含 2 个文档检索
与 1 个查询调用。验证 agent 能通过 tool 获得
知识。

示例:
    >>> docs = ["LangChain 是 LLM 框架", "RAG 是检索增强"]
    >>> retrieval = RetrievalTool(docs)
    >>> retrieval.invoke("什么是 LangChain?")
    'LangChain 是 LLM 框架'
    >>> agent = SimpleAgent([retrieval])
    >>> agent.run("什么是 LangChain?")
    'LangChain 是 LLM 框架'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from langchain_core.tools import tool


@tool
def retrieval(query: str) -> str:
    """从知识库检索相关文档"""
    docs = [
        "LangChain 是一个 LLM 应用开发框架",
        "RAG 是检索增强生成技术"
    ]
    for doc in docs:
        if query in doc or any(
            kw in doc for kw in query if len(kw) > 1
        ):
            return doc
    return "未找到相关文档"


class SimpleAgent:
    """简化版 Agent, 调用工具完成任务"""

    def __init__(self, tools):
        self.tools = {t.name: t for t in tools}

    def run(self, query: str) -> str:
        """mock: 直接调用 retrieval 工具"""
        tool = self.tools["retrieval"]
        return tool.invoke(query)


agent = SimpleAgent([retrieval])
answer1 = agent.run("LangChain")
answer2 = agent.run("RAG")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 查询 LangChain
    assert "LangChain" in answer1
    print("测试 1 通过:", answer1)
    # 测试 2: 查询 RAG
    assert "RAG" in answer2
    print("测试 2 通过:", answer2)
    # 测试 3: 查询未知内容
    a3 = agent.run("不存在的知识")
    assert a3 == "未找到相关文档"
    print("测试 3 通过:", a3)
