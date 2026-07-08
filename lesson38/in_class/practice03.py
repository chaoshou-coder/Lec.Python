"""
[难度: ⭐⭐]
[所属知识点: add_generation_prompt 的重要性]
[预计完成时间: 10 分钟]

对同一条消息分别调用 apply_chat_template,
参数分别为 add_generation_prompt=True 和 False,
打印结果并观察末尾差异。

⚠️ 教学红线:
    忘记 add_generation_prompt=True 时,模板不会在末尾
    追加 assistant 起始标记,模型不知道该开始生成,
    导致生成空结果。这是 SFT 数据准备的高频 bug。

示例:
    >>> show_chat_template_effect(tokenizer)
    带 add_generation_prompt=True  末尾 -> '<|im_start|>assistant\n'
    带 add_generation_prompt=False 末尾 -> '<|im_end|>\n'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from transformers import AutoTokenizer


def show_chat_template_effect(tokenizer):
    """对比 add_generation_prompt 取不同值时的模板差异。"""
    messages = [
        {"role": "system", "content": "你是一个助手。"},
        {"role": "user", "content": "什么是大模型?"},
    ]

    # 学员: 调用 apply_chat_template, add_generation_prompt=True
    with_prompt = ""  # 替换为 pass 并实现
    pass

    # 学员: 调用 apply_chat_template, add_generation_prompt=False
    without_prompt = ""  # 替换为 pass 并实现
    pass

    print("=== add_generation_prompt=True (末尾) ===")
    print(repr(with_prompt[-60:]))
    print("\n=== add_generation_prompt=False (末尾) ===")
    print(repr(without_prompt[-60:]))
    print("\n⚠️ 红线提示: 忘记 True 会让模型生成空结果!")


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 需要联网下载模型
    tok = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2-0.5B-Instruct"
    )
    show_chat_template_effect(tok)

    # 测试 1: 两者长度应不同
    msgs = [{"role": "user", "content": "hi"}]
    a = tok.apply_chat_template(
        msgs, tokenize=False, add_generation_prompt=True
    )
    b = tok.apply_chat_template(
        msgs, tokenize=False, add_generation_prompt=False
    )
    assert len(a) != len(b), "两者应有长度差异"

    # 测试 2: True 的版本应以 assistant 起始标记结尾
    assert "assistant" in a[-40:], (
        "add_generation_prompt=True 应在末尾追加 assistant 标记"
    )
