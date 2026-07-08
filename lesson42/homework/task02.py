"""
[难度: ⭐⭐⭐]
[所属知识点: 多指标聚合评测]
[预计完成时间: 15 分钟]

写一个函数 evaluate_multiple(preds, refs),
同时计算 BLEU / ROUGE / 各句 PPL(用 dummy)。
返回 dict:
{"bleu": float, "rouge1": float, "rougeL": float,
 "ppl_per_sentence": list}
测试 3 条中英文混合句子。
红线: 各指标意义不同,PPL 低不代表 BLEU 高。

示例:
    >>> evaluate_multiple(
        ["a b c", "x y z"],
        ["a b c", "x y z"],
    )
    {"bleu": 1.0, ...}
"""

# ======================
# 学员代码区
# ======================
import evaluate
import math

def evaluate_multiple(preds, refs):
    # 1. 算 BLEU
    # 2. 算 ROUGE(中文按字切分)
    # 3. 用固定 dummy loss=1.0 算每条 PPL
    # 返回聚合 dict
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 完全一致
    res1 = evaluate_multiple(
        ["机器学习", "hello world", "test"],
        ["机器学习", "hello world", "test"],
    )
    print(f"测试1 -> {res1}")

    # 测试 2: 部分不同
    res2 = evaluate_multiple(
        ["深度学习", "cat sat", "foo"],
        ["机器学习", "the cat sat on mat", "bar"],
    )
    print(f"测试2 -> {res2}")

    # 测试 3: 单条
    res3 = evaluate_multiple(
        ["single sentence"],
        ["single sentence"],
    )
    print(f"测试3 -> {res3}")
