"""
[难度: ⭐⭐⭐]
[所属知识点: GPT-2 自回归生成 vs BERT 不能直接 generate]
[预计完成时间: 15 分钟]

用 GPT2LMHeadModel.from_pretrained("gpt2") 和
GPT2Tokenizer 对 "Hello" 生成 10 个新 token,
打印生成文本。尝试对 bert-base-chinese 调用 generate,
观察报错并说明原因。需要联网下载模型。

示例:
    >>> text = gpt2_generate("Hello", max_new_tokens=10)
    >>> print(text)
    Hello, I'm a little bit nervous...
"""

from transformers import (
    GPT2LMHeadModel, GPT2Tokenizer
)

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def gpt2_generate(prompt, max_new_tokens=10):
    """用 GPT-2 生成文本"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 生成文本
    text = gpt2_generate("Hello", max_new_tokens=10)
    print("generated:", text)
    # 测试 2: BERT 无 generate
    from transformers import AutoModel
    bert = AutoModel.from_pretrained("bert-base-uncased")
    print("bert has generate:",
          hasattr(bert, "generate"))
    pass
