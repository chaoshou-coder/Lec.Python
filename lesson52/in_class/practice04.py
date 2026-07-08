"""
[难度: ⭐⭐]
[所属知识点: ChatCompletion 多轮对话 history 拼接]
[预计完成时间: 10 分钟]

请补全下面 chat_with_history 函数, 让模型能根据对话历史进行回复。
已给出的示例:
1) 先调用 client.chat.completions.create
2) messages 列表应把 history 与新 user message 拼接
3) 返回模型生成的纯文本内容

示例:
    >>> history = [{"role":"user","content":"我叫小明"},
    ...            {"role":"assistant","content":"你好小明"}]
    >>> chat_with_history(history, "我今年 20 岁")
    "好的小明, 已记录你的年龄 20..."
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def chat_with_history(history: list, user_msg: str) -> str:
    """拼接历史和新消息, 调用模型并返回回复"""
    messages = []
    # TODO: 把 history 所有轮追加到 messages
    # TODO: 再加入新 user message
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    # TODO: 返回 choices[0].message.content
    return ""


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 空历史首次对话
    h = []
    ans = chat_with_history(h, "你好")
    assert isinstance(ans, str) and len(ans) > 0
    print(f"回复长度: {len(ans)}")

    # 测试 2: 多轮历史
    h = [
        {"role": "user", "content": "我叫小红"},
        {"role": "assistant", "content": "你好小红"},
    ]
    ans = chat_with_history(h, "帮我写首诗")
    assert isinstance(ans, str) and len(ans) > 0
    print(f"多轮回复长度: {len(ans)}")
