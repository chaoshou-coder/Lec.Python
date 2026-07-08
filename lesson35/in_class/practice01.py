"""
[难度: ⭐]
[所属知识点: HuggingFace Tokenizer 加载与使用]
[预计完成时间: 5 分钟]

从 transformers 加载 bert-base-chinese 的 tokenizer,
打印其词表大小(vocab_size),并对字符串
"自然语言处理" 做 encode,打印 token ids。
注意: 本题目需要联网下载模型,首次运行会缓存。

示例:
    >>> tokenizer = load_tokenizer()
    >>> print(tokenizer.vocab_size)
    21128
"""

from transformers import AutoTokenizer

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def load_tokenizer():
    """加载 bert-base-chinese tokenizer"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    tokenizer = load_tokenizer()
    # 测试 1: 打印词表大小
    print("vocab_size:", tokenizer.vocab_size)
    # 测试 2: 编码中文句子
    ids = tokenizer.encode("自然语言处理")
    print("token ids:", ids)
    pass
