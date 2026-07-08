"""
[难度: ⭐⭐]
[所属知识点: 手算 BLEU]
[预计完成时间: 10 分钟]

写一个函数 manual_bleu(ref, pred, max_n=2),
简易实现 BLEU: 对 1~max_n 阶 n-gram
计算 pred 中与 ref 重叠的比例,取几何平均。
只考虑 precision(不做 brevity penalty)。
测试好候选句和差候选句。

示例:
    >>> manual_bleu(
        "the cat sat on the mat",
        "the cat sat on the mat", max_n=2
    )
    1.0
"""

# ======================
# 学员代码区
# ======================
from collections import Counter
import math

def ngram_counts(tokens, n):
    # 返回 n-gram 的 Counter
    pass

def manual_bleu(ref, pred, max_n=2):
    # 对每个 n 算 precision,取几何平均
    # 注意: pred 为空时返回 0
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 完全一致
    s1 = manual_bleu(
        "the cat sat on the mat",
        "the cat sat on the mat",
        max_n=2
    )
    print(f"完全一致 BLEU = {s1:.4f}")

    # 测试 2: 完全不同
    s2 = manual_bleu(
        "the cat sat on the mat",
        "a dog jumped over",
        max_n=2
    )
    print(f"完全不同 BLEU = {s2:.4f}")

    # 测试 3: 部分重叠
    s3 = manual_bleu(
        "machine learning is fun",
        "machine learning is boring",
        max_n=2
    )
    print(f"部分重叠 BLEU = {s3:.4f}")
