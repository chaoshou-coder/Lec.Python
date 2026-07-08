"""
[难度: ⭐]
[所属知识点: Perplexity 与 NLL]
[预计完成时间: 5 分钟]

给定 5 个 next-token 概率,手算平均 NLL 和 perplexity 并打印。
红线提示: perplexity 必须在未参与训练的数据上计算,
用训练集算 perplexity = 数据泄露。

示例:
    >>> compute(0.7, 0.5, 0.8, 0.6, 0.9)
    NLL = 0.42, PPL = 1.52
"""

# ======================
# 学员代码区
# ======================
import math

def avg_nll_and_ppl(probs):
    # 请计算每个概率的 -log(p) 的平均值,
    # 再取 exp 得到 perplexity
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 5 个给定概率
    probs1 = [0.7, 0.5, 0.8, 0.6, 0.9]
    nll1, ppl1 = avg_nll_and_ppl(probs1)
    print(f"测试1 -> NLL = {nll1:.4f}, PPL = {ppl1:.4f}")

    # 测试 2: 全部概率接近 1(理想模型)
    probs2 = [0.99, 0.98, 0.97, 0.99, 0.96]
    nll2, ppl2 = avg_nll_and_ppl(probs2)
    print(f"测试2 -> NLL = {nll2:.4f}, PPL = {ppl2:.4f}")

    # 测试 3: 全部概率都很低(差模型)
    probs3 = [0.1, 0.2, 0.15, 0.1, 0.25]
    nll3, ppl3 = avg_nll_and_ppl(probs3)
    print(f"测试3 -> NLL = {nll3:.4f}, PPL = {ppl3:.4f}")
