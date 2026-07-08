"""
[难度: ⭐⭐]
[所属知识点: ChatCompletion 单次调用]
[预计完成时间: 10 分钟]

调用 ChatCompletion 接口, 让模型返回一句关于"PyTorch 训练"
的励志鸡汤。要求:
1) 使用 gpt-4o-mini 模型
2) system 角色固定为"你是一位 AI 学习导师"
3) 返回完整 message 内容并打印

示例:
    >>> main()
    模型输出: 加油, 每一个 epoch 都在进化...
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def ask(sentence: str) -> str:
    """调用 ChatCompletion, 返回模型的回复文本"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "你是一位 AI 学习导师"},
            {"role": "user", "content": sentence},
        ],
    )
    return resp.choices[0].message.content


def main() -> None:
    out = ask("给我一句关于 PyTorch 训练的励志鸡汤")
    print(f"模型输出: {out}")


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常调用并返回非空字符串
    ans = ask("给我一句关于 PyTorch 训练的励志鸡汤")
    assert isinstance(ans, str) and len(ans) > 0
    print(f"长度: {len(ans)}")
    # 测试 2: user 输入为空时可以调用(模型自行处理)
    ans2 = ask("")
    assert isinstance(ans2, str)
    print(f"空输入回复长度: {len(ans2)}")
