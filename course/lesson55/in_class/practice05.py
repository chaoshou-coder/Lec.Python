"""
[难度: ⭐⭐⭐]
[所属知识点: Agent 单步工具调用]
[预计完成时间: 15 分钟]

场景: 构造简化 Agent: 定义 1 个 mock tool + mock llm
(返回固定 JSON 动作), agent_executor 执行一步,
验证 tool 被调用。演示完整 tool 调用循环。
使用 langchain.agents 工具体系, 但用 mock 避免
真实 LLM。

示例:
    >>> from langchain_core.tools import tool
    >>> from langchain_core.language_models.fake import
    ...     FakeListChatModel
    >>> from langchain.agents import
    ...     create_tool_calling_agent, AgentExecutor
    >>> @tool
    ... def get_weather(city: str) -> str:
    ...     '''查询天气'''
    ...     return f"{city} 晴 25°C"
    >>> tools = [get_weather]
    >>> llm = FakeListChatModel(responses=[...])
    >>> agent = create_tool_calling_agent(llm, tools, prompt)
    >>> agent_executor = AgentExecutor(
    ...     agent=agent, tools=tools
    ... )
    >>> result = agent_executor.invoke({"input": "北京天气?"})
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models.fake import (
    FakeListChatModel
)
from langchain.agents import (
    create_tool_calling_agent, AgentExecutor
)


@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气"""
    return f"{city} 晴 25°C"


# 构造 mock LLM 返回固定工具调用 JSON
tool_call_json = (
    '{"id": "call_1", "function": '
    '{"name": "get_weather", '
    '"arguments": "{\\"city\\": \\"北京\\"}"}, '
    '"type": "function"}'
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个天气助手"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
tools = [get_weather]
llm = FakeListChatModel(responses=[tool_call_json])
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
result = agent_executor.invoke({"input": "北京天气?"})

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出包含 "北京"
    assert "北京" in result["output"]
    print("测试 1 通过:", result["output"])
    # 测试 2: 工具被调用过(输出含温度信息)
    assert "25°C" in result["output"]
    print("测试 2 通过: 工具被正确调用")
