"""
[难度: ⭐⭐]
[所属知识点: chat template]
[预计完成时间: 10 分钟]

给定 2 条 messages (含 system / user / assistant),
使用 tokenizer.apply_chat_template 将对话转成
模型可识别的 chat 格式字符串,并打印对比结果。

注意: 需要联网下载模型。

示例:
    >>> prompt = tokenizer.apply_chat_template(
    ...     msgs, tokenize=False, add_generation_prompt=True
    ... )
    >>> print(prompt)
    '<|im_start|>system\n...<|im_end|>...'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from transformers import AutoTokenizer

# 需要联网下载模型
tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2-0.5B-Instruct"
)

# 对话 1: 简单问答
messages_1 = [
    {"role": "system", "content": "你是一个乐于助人的助手。"},
    {"role": "user", "content": "Python 怎么写 for 循环?"},
]

# 对话 2: 含 assistant 的多轮
messages_2 = [
    {"role": "system", "content": "你是一个翻译官。"},
    {"role": "user", "content": "翻译成英文: 早上好"},
    {"role": "assistant", "content": "Good morning."},
    {"role": "user", "content": "再见"},
]

# 学员: 对 messages_1 调用 apply_chat_template (tokenize=False)
prompt_1 = ""  # 替换为 pass 并实现
pass

# 学员: 对 messages_2 调用 apply_chat_template (tokenize=False)
prompt_2 = ""  # 替换为 pass 并实现
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 两条 prompt 都应为非空字符串
    assert isinstance(prompt_1, str) and len(prompt_1) > 0
    assert isinstance(prompt_2, str) and len(prompt_2) > 0

    # 测试 2: 应包含 <|im_start|> 格式标记
    assert "<|im_start|>" in prompt_1
    assert "<|im_start|>" in prompt_2

    print("=== 对话 1 ===")
    print(prompt_1)
    print("\n=== 对话 2 ===")
    print(prompt_2)
