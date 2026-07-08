"""
[难度: ⭐⭐⭐]
[所属知识点: Streamlit Chat 完整实现( stateful )]
[预计完成时间: 15 分钟]

场景: 完整 Streamlit 聊天应用,使用 session_state 管理消息列表,
每次输入追加 user 消息 + mock 回复 "echo: {user_input}",
用 st.chat_message 区分角色渲染。
验证 2 轮交互后 session_state 长度 = 4。

示例:
    >>> app = ChatApp()
    >>> app.send("hello")
    >>> app.send("world")
    >>> assert len(app.messages) == 4
    >>> assert app.messages[1]["content"] == "echo: hello"
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ChatApp:
    """模拟 Streamlit 聊天应用( stateful 模式 )。"""

    def __init__(self):
        # 模拟 st.session_state,存储消息列表
        self.messages = []
        # 记录 render 调用过的角色,用于测试验证
        self.rendered = []

    def send(self, user_input: str):
        """追加用户消息与 mock 回复。"""
        pass

    def render(self):
        """遍历消息,按角色调用 st.chat_message。"""
        pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两轮交互后共 4 条消息
    app = ChatApp()
    app.send("hello")
    app.send("world")
    assert len(app.messages) == 4, (
        f"期望 4 条消息,实际 {len(app.messages)} 条"
    )
    assert app.messages[0]["role"] == "user"
    assert app.messages[0]["content"] == "hello"
    assert app.messages[1]["content"] == "echo: hello"
    assert app.messages[2]["content"] == "world"
    assert app.messages[3]["content"] == "echo: world"

    # 测试 2: render 按角色渲染,且调用次数正确
    app.render()
    assert len(app.rendered) == 4, (
        f"渲染次数应为 4,实际 {len(app.rendered)}"
    )
    assert app.rendered == [
        "user", "assistant", "user", "assistant"
    ]

    print("全部测试通过!")
