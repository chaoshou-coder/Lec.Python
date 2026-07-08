"""
[难度: ⭐⭐]
[所属知识点: Memory 记忆系统]
[预计完成时间: 10 分钟]

场景: 用 langchain_community.chat_message_histories
.InMemoryChatMessageHistory 保存 2 轮对话,
取出验证历史长度等于 4 (每轮含 human + ai)。

示例:
    >>> from langchain_community.chat_message_histories import (
    ...     InMemoryChatMessageHistory
    ... )
    >>> from langchain_core.messages import HumanMessage, AIMessage
    >>> history = InMemoryChatMessageHistory()
    >>> history.add_message(HumanMessage("你好"))
    >>> history.add_message(AIContent("你好!"))
    >>> len(history.messages)
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from langchain_community.chat_message_histories import (
    InMemoryChatMessageHistory
)
from langchain_core.messages import HumanMessage, AIMessage

history = InMemoryChatMessageHistory()
history.add_message(HumanMessage(content="你好"))
history.add_message(AIMessage(content="你好!有什么可以帮你?"))
history.add_message(HumanMessage(content="什么是 LangChain?"))
history.add_message(AIMessage(content="LangChain 是一个 LLM 框架。"))

msgs = history.messages

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 历史长度等于 4
    assert len(msgs) == 4
    print("测试 1 通过: 历史长度 =", len(msgs))
    # 测试 2: 第一条是 HumanMessage
    assert isinstance(msgs[0], HumanMessage)
    print("测试 2 通过: 第一条是人类消息")
    # 测试 3: 总共 2 轮对话
    human_msgs = [m for m in msgs if isinstance(m, HumanMessage)]
    assert len(human_msgs) == 2
    print("测试 3 通过: 共 2 轮人类提问")
