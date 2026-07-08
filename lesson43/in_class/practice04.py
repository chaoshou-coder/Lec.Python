"""
[难度: ⭐⭐⭐]
[所属知识点: Ollama Python Client 调用]
[预计完成时间: 15 分钟]

用 ollama python client 调用 ollama.chat,
model="qwen2.5:0.5b",
messages=[{"role":"user","content":"你好"}],
捕获并打印回复内容。
若 Ollama 未安装或未运行,try/except 友好提示。

示例:
    >>> run()
    模型回复: 你好!有什么可以帮你?
"""

# ======================
# 学员代码区
# ======================
def run():
    # 1. import ollama
    # 2. 调用 ollama.chat(...)
    # 3. 打印 message["content"]
    # 4. 捕获 ConnectionError / ModuleNotFoundError
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程
    run()

    # 测试 2: 多轮对话
    try:
        import ollama
        msgs = [
            {"role": "user", "content": "1+1="},
            {"role": "assistant", "content": "2"},
            {"role": "user", "content": "2+2="},
        ]
        r = ollama.chat(
            model="qwen2.5:0.5b",
            messages=msgs,
        )
        print(f"多轮回复: {r['message']['content']}")
    except ImportError:
        print("请先 pip install ollama")
    except Exception as e:
        print(f"异常: {e}")

    # 测试 3: 空消息(边界)
    try:
        import ollama
        r = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[{"role": "user", "content": ""}],
        )
        print(f"空消息回复: {r['message']['content']}")
    except ImportError:
        print("请先 pip install ollama")
    except Exception as e:
        print(f"异常: {e}")
