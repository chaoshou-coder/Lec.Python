"""
[难度: ⭐⭐⭐]
[所属知识点: 模型服务类封装]
[预计完成时间: 15 分钟]

写一个 ModelServer 类,封装 ollama.chat:
- __init__(model): 设定模型名,初始化空历史
- chat(system, user): 拼接 system + user 消息,
  调用 ollama.chat,保存到历史,返回回复
- reset(): 清空历史
历史最多保留 5 条消息,超出时丢弃最早的。
测试 3 轮对话,验证历史长度与 reset。
若 Ollama 未安装,try/except 友好提示。

示例:
    >>> s = ModelServer("qwen2.5:0.5b")
    >>> s.chat("简洁回答", "1+1=")
    2
    >>> s.reset()
"""

# ======================
# 学员代码区
# ======================
class ModelServer:
    def __init__(self, model):
        self.model = model
        self.history = []

    def chat(self, system, user):
        # 拼接 system + user 到消息列表
        # 调用 ollama.chat,返回回复
        # 维护 history 长度 <= 5
        pass

    def reset(self):
        # 清空 history
        pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 单轮对话
    s = ModelServer("qwen2.5:0.5b")
    try:
        r = s.chat("简洁回答", "1+1=")
        print(f"单轮回复: {r}")
        print(f"历史长度: {len(s.history)}")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 2: 3 轮对话
    s.reset()
    try:
        for i in range(3):
            r = s.chat("简洁回答", f"第{i+1}轮")
            print(f"第{i+1}轮回复: {r}")
        print(f"3轮后历史长度: {len(s.history)}")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 3: 连续发送触发上限(6 条,>5)
    s.reset()
    try:
        for i in range(6):
            s.chat("sys", f"msg{i}")
        print(f"6条后历史长度: {len(s.history)}")
    except Exception as e:
        print(f"异常: {e}")
