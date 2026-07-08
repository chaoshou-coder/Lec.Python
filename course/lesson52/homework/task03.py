"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 完整 Chat 应用(多轮 + 流式 + 错误处理)]
[预计完成时间: 20 分钟]

场景: 实现 StreamChat 类,封装流式对话全流程,
支持多轮上下文、流式输出、异常兜底。
功能:
- __init__: 接收 system_prompt、model 名
- chat(user_input): 流式调用,返回完整回复字符串并保存历史
- 异常处理: APIError 时返回 "调用失败: {错误信息}"
- reset_history: 清空历史(保留 system)

示例:
    >>> chat = StreamChat("你是助手","gpt-4o-mini")
    >>> reply = chat.chat("你好")   # 流式打印
    >>> isinstance(reply, str)
    True
"""
import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from openai import OpenAI, APIError


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class StreamChat:
    """流式多轮对话,带错误兜底"""

    def __init__(
        self,
        system_prompt: str,
        model: str,
        client: Optional[OpenAI] = None,
    ):
        # TODO: 保存 system_prompt 与 model
        self.system_prompt = system_prompt
        self.model = model
        # TODO: 创建客户端(若无外部 client 则从 .env 加载)
        if client is not None:
            self.client = client
        else:
            load_dotenv()
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("缺少 OPENAI_API_KEY")
            self.client = OpenAI(api_key=api_key)
        # TODO: 初始化历史(首条为 system)
        self.history: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]

    def chat(self, user_input: str) -> str:
        """流式调用 LLM,累积并返回完整回复"""
        # TODO: 将用户输入追加到历史
        self.history.append({"role": "user", "content": user_input})

        try:
            # TODO: 调用流式接口
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                stream=True,
            )
            # TODO: 逐个 token 累积,并实时打印(模拟打字机)
            full_reply = ""
            print("助手: ", end="", flush=True)
            for chunk in stream:
                token = chunk.choices[0].delta.content or ""
                print(token, end="", flush=True)
                full_reply += token
            print()  # 换行
            # TODO: 将助手回复追加到历史
            self.history.append(
                {"role": "assistant", "content": full_reply}
            )
            return full_reply
        except APIError as e:
            # TODO: 异常兜底,返回 "调用失败: {错误信息}"
            return f"调用失败: {e}"

    def reset_history(self) -> None:
        """清空历史,仅保留 system 消息"""
        # TODO: 重置 history 为只含 system 的列表
        self.history = [
            {"role": "system", "content": self.system_prompt}
        ]


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 用 Mock 客户端测试,无需真实 API Key

    class _FakeDelta:
        def __init__(self, content):
            self.content = content

    class _FakeChoice:
        def __init__(self, content):
            self.delta = _FakeDelta(content)

    class _FakeChunk:
        def __init__(self, content):
            self.choices = [_FakeChoice(content)]

    class _FakeStream:
        """模拟流式返回"""
        def __init__(self, tokens):
            self._tokens = tokens

        def __iter__(self):
            for t in self._tokens:
                yield _FakeChunk(t)

    class _FakeCompletions:
        def __init__(self, tokens):
            self._tokens = tokens

        def create(self, model, messages, stream=True):
            # 顺手验证入参被正确传递
            assert isinstance(messages, list) and len(messages) >= 1
            return _FakeStream(self._tokens)

    class _FakeChat:
        def __init__(self, tokens):
            self.completions = _FakeCompletions(tokens)

    class _FakeClient:
        """无 Key 模拟客户端"""
        def __init__(self, tokens=("你", "好", "呀", "!")):
            self.chat = _FakeChat(tokens)

    # 测试 1: 多轮对话 + 流式累积正确
    fake = _FakeClient(tokens=("你", "好", "呀"))
    chat = StreamChat("你是助手", "gpt-4o-mini", client=fake)
    reply = chat.chat("打个招呼")
    assert reply == "你好呀", f"期望 '你好呀',实际 '{reply}'"
    # 历史应包含 system + user + assistant = 3 条
    assert len(chat.history) == 3, "历史轮次错误"
    print("测试1 通过: 多轮流式累积正确\n")

    # 测试 2: reset_history 后只剩 system
    chat.reset_history()
    assert len(chat.history) == 1, "reset 后应仅剩 system"
    assert chat.history[0]["role"] == "system"
    print("测试2 通过: reset_history 正确\n")

    # 测试 3: APIError 时返回兜底字符串
    class _FakeCompletionsErr:
        def create(self, model, messages, stream=True):
            raise APIError(
                message="余额不足",
                request=None,
                body=None,
            )

    class _FakeChatErr:
        completions = _FakeCompletionsErr()

    class _FakeClientErr:
        chat = _FakeChatErr()

    chat_err = StreamChat(
        "sys", "gpt-4o-mini", client=_FakeClientErr()
    )
    result = chat.err_chat = chat_err.chat("any")
    assert result.startswith("调用失败:"), f"期望兜底,实际 {result}"
    print("测试3 通过: 异常兜底正确")
