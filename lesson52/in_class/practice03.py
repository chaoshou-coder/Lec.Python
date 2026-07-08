"""
[难度: ⭐⭐]
[所属知识点: stream=True 流式调用]
[预计完成时间: 10 分钟]

开启 stream=True, 让模型边生成边输出, 提升交互体验。
请把流式 chunk 的增量内容逐块 print, 最后再 print 一行
"[结束]" 表示生成完毕。

示例:
    >>> main()
    今天天气真好
    ...
    [结束]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def stream_ask(prompt: str) -> None:
    """流式打印模型输出, 结束后打印 [结束]"""
    resp_stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in resp_stream:
        # chunk.choices[0].delta.content 可能为 None
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print("\n[结束]")


def main() -> None:
    stream_ask("用三句话介绍 Chain-of-Thought")


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 短 prompt 流式输出
    stream_ask("说你好")
    # 测试 2: 空 prompt 也不会崩溃
    stream_ask("")
