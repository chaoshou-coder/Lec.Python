"""
[难度: ⭐⭐⭐]
[所属知识点: Streamlit sidebar + session_state]
[预计完成时间: 15 分钟]

题目描述:
模拟实现带 sidebar 设置的 Streamlit 对话系统。
sidebar 通过 selectbox 切换模型(使用 mock 返回)。
session_state 同时存 messages 与 selected_model。
验证切换不同模型时返回不同 mock 回复。

示例:
    >>> chat = ChatWithSidebar()
    >>> chat.select_model("gpt-4")
    >>> chat.send("hi")
    >>> chat.messages[-1]["content"]
    '[GPT-4] hi'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ChatWithSidebar:
    """模拟 Streamlit 带 sidebar 的对话系统"""

    def __init__(self):
        """初始化 messages 与 selected_model"""
        self.messages = []
        self.selected_model = "gpt-3.5"

    def select_model(self, model: str):
        """sidebar selectbox 切换模型"""
        pass

    def send(self, user_input: str):
        """发送消息并追加 mock 回复"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认模型 gpt-3.5
    chat = ChatWithSidebar()
    chat.send("你好")
    assert len(chat.messages) == 2, "应有两条消息"
    assert chat.messages[1]["content"] == "[GPT-3.5] 你好"
    print("测试 1 通过: 默认模型返回正确")

    # 测试 2: 切换到 gpt-4
    chat.select_model("gpt-4")
    assert chat.selected_model == "gpt-4"
    chat.send("hi")
    assert chat.messages[-1]["content"] == "[GPT-4] hi"
    print("测试 2 通过: 切换模型后返回不同回复")
