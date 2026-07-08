"""
[难度: ⭐⭐⭐]
[所属知识点: BERT vs GPT Tokenizer 编码差异]
[预计完成时间: 15 分钟]

写 compare_bert_gpt() 函数:
- 分别加载 bert-base-chinese 与 gpt2 的 tokenizer
- 对 "人工智能很有趣" 做 encode
- 打印两份 tokenizer 的 token 长度差异
- 并解释为什么长度不同
需要联网下载模型。

示例:
    >>> compare_bert_gpt()
    bert: 7 tokens, gpt: ? tokens
"""

from transformers import AutoTokenizer

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def compare_bert_gpt():
    """对比 BERT 与 GPT tokenizer 编码差异"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 中文句子
    compare_bert_gpt()
    # 测试 2: 英文对照
    bert_tok = AutoTokenizer.from_pretrained(
        "bert-base-chinese"
    )
    gpt_tok = AutoTokenizer.from_pretrained("gpt2")
    en = "Artificial intelligence is fun"
    print("bert len:", len(bert_tok.encode(en)))
    print("gpt len:", len(gpt_tok.encode(en)))
    pass
