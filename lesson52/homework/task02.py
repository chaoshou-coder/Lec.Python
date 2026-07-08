"""
[难度: ⭐⭐⭐]
[所属知识点: 多轮对话缓冲区管理]
[预计完成时间: 15 分钟]

场景: 为大语言模型对话设计一个缓冲区,
自动裁剪过长历史,避免超出上下文窗口。
请实现 ConversationBuffer 类:
- __init__(self, system_prompt: str, max_turns: int = 6)
- add(role, content): 超过 max_turns 时丢弃最旧的用户-助手对
- build(): 返回含 system + 所有轮次的 messages 列表
- clear(): 清空历史

示例:
    >>> buf = ConversationBuffer("你是助手", max_turns=2)
    >>> buf.add("user", "你好")
    >>> buf.add("assistant", "你好呀")
    >>> buf.build()
    [{'role':'system','content':'你是助手'},
     {'role':'user','content':'你好'},
     {'role':'assistant','content':'你好呀'}]
"""
from typing import List, Dict


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ConversationBuffer:
    """多轮对话缓冲区,自动裁剪超长历史"""

    def __init__(self, system_prompt: str, max_turns: int = 6):
        # TODO: 保存 system_prompt 与 max_turns
        self.system_prompt = system_prompt
        self.max_turns = max_turns
        # TODO: 初始化空的历史列表(存 role/content 字典)
        self.history: List[Dict[str, str]] = []

    def add(self, role: str, content: str) -> None:
        """添加一条消息,超限时丢弃最旧的一对"""
        # TODO: 将 {"role": role, "content": content} 追加到 history
        self.history.append({"role": role, "content": content})

        # TODO: 当历史轮次超过 max_turns 时,从前面删除
        #       注意: 丢弃的是最旧的用户-助手对(2 条)
        while len(self.history) > self.max_turns * 2:
            self.history.pop(0)

    def build(self) -> List[Dict[str, str]]:
        """组装完整 messages: system + 历史"""
        # TODO: 返回 system 消息 + history 的完整列表
        system_msg = {"role": "system", "content": self.system_prompt}
        return [system_msg] + self.history

    def clear(self) -> None:
        """清空历史(保留 system_prompt)"""
        # TODO: 清空 history 列表
        self.history.clear()


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基本功能 —— build 包含 system + 历史
    buf = ConversationBuffer("你是助手", max_turns=3)
    buf.add("user", "A")
    buf.add("assistant", "B")
    msgs = buf.build()
    assert len(msgs) == 3, f"期望 3 条,实际 {len(msgs)}"
    assert msgs[0]["role"] == "system", "第一条应为 system"
    print("测试1 通过: build 结构正确")

    # 测试 2: 超限裁剪 —— max_turns=2,添加 3 对后应裁剪掉最旧一对
    buf2 = ConversationBuffer("sys", max_turns=2)
    buf2.add("user", "旧问题_1")
    buf2.add("assistant", "旧回答_1")
    buf2.add("user", "旧问题_2")
    buf2.add("assistant", "旧回答_2")
    buf2.add("user", "新问题_3")
    buf2.add("assistant", "新回答_3")
    msgs2 = buf2.build()
    # 应保留 system + 最新 2 对 = 5 条
    assert len(msgs2) == 5, f"期望 5 条,实际 {len(msgs2)}"
    # 最旧的 "旧问题_1" 应被裁掉
    contents = [m["content"] for m in msgs2]
    assert "旧问题_1" not in contents, "最旧对话未裁剪"
    print("测试2 通过: 超限裁剪正确")

    # 测试 3: clear 后只剩 system
    buf2.clear()
    assert len(buf2.build()) == 1, "clear 后应只剩 system"
    print("测试3 通过: clear 正确")
