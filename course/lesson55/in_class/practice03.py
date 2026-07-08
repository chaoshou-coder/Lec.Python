"""
[难度: ⭐⭐]
[所属知识点: Chain 链式调用]
[预计完成时间: 10 分钟]

场景: 用 pipe 将 prompt 与 mock llm 相连, 形成 chain。
mock llm 用 lambda 返回固定 "这是LLM 回复"。
chain.invoke({"topic":"Python"}) 返回 mock LLM 输出。

示例:
    >>> from langchain_core.prompts import PromptTemplate
    >>> prompt = PromptTemplate(
    ...     input_variables=["topic"],
    ...     template="请用一句话解释:{topic}"
    ... )
    >>> mock_llm = lambda x: "这是LLM 回复"
    >>> chain = prompt | mock_llm
    >>> chain.invoke({"topic": "Python"})
    '这是LLM 回复'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

prompt = PromptTemplate(
    input_variables=["topic"],
    template="请用一句话解释:{topic}"
)
mock_llm = RunnableLambda(lambda x: "这是LLM 回复")
chain = prompt | mock_llm
result = chain.invoke({"topic": "Python"})

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: topic=Python
    assert result == "这是LLM 回复"
    print("测试 1 通过:", result)
    # 测试 2: topic=AI
    r2 = chain.invoke({"topic": "AI"})
    assert r2 == "这是LLM 回复"
    print("测试 2 通过:", r2)
