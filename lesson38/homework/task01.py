"""
[难度: ⭐⭐]
[所属知识点: tokenizer 对比]
[预计完成时间: 10 分钟]

对比 "机器学习很有趣" 在 Qwen2-0.5B-Instruct 和
bert-base-chinese 两个 tokenizer 下的 token 数差异,
并打印各自的 token 列表,直观感受不同分词器的切分方式。

注意: 需要联网下载模型。

示例:
    >>> compare_tokenizers("机器学习很有趣")
    Qwen2  token 数: 6
    BERT   token 数: 9
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from transformers import AutoTokenizer


def compare_tokenizers(text):
    """对比两个 tokenizer 的切分结果。"""
    # 需要联网下载模型
    qwen_tok = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2-0.5B-Instruct"
    )
    bert_tok = AutoTokenizer.from_pretrained(
        "bert-base-chinese"
    )

    # 学员: 分别 encode
    qwen_ids = []  # 替换为 pass 并实现
    pass
    bert_ids = []  # 替换为 pass 并实现
    pass

    print(f"文本: {text}")
    print(f"Qwen2 token 数: {len(qwen_ids)}")
    print(f"BERT   token 数: {len(bert_ids)}")
    print(f"Qwen2 ids: {qwen_ids}")
    print(f"BERT   ids: {bert_ids}")

    return len(qwen_ids), len(bert_ids)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    text = "机器学习很有趣"
    q_len, b_len = compare_tokenizers(text)

    # 测试 1: 两者都应产生非空结果
    assert q_len > 0, "Qwen2 结果不能为空"
    assert b_len > 0, "BERT 结果不能为空"

    # 测试 2: 两者 token 数通常不同
    print(f"\n差异: {abs(q_len - b_len)} 个 token")
    print("说明: 不同分词器对中文切分粒度不同")
