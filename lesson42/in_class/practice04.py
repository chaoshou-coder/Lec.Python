"""
[难度: ⭐⭐⭐]
[所属知识点: BLEU 评测]
[预计完成时间: 15 分钟]

用 evaluate.load("bleu") 计算 BLEU 分数。
参考句: "the cat sat on the mat"
候选 1: 与参考完全一致,应得高分
候选 2: "a dog jumped",应得低分
对比两者差异,理解 BLEU 衡量 n-gram 重叠。

示例:
    >>> run()
    候选1 BLEU = 1.00
    候选2 BLEU = 0.00
"""

# ======================
# 学员代码区
# ======================
import evaluate

def run():
    bleu = evaluate.load("bleu")
    refs = [["the cat sat on the mat"]]

    # 候选 1: 完全一致
    pred1 = ["the cat sat on the mat"]
    s1 = bleu.compute(
        predictions=pred1, references=refs
    )["bleu"]

    # 候选 2: 完全不同
    pred2 = ["a dog jumped"]
    s2 = bleu.compute(
        predictions=pred2, references=refs
    )["bleu"]

    print(f"候选1 BLEU = {s1:.4f}")
    print(f"候选2 BLEU = {s2:.4f}")

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程
    run()

    # 测试 2: 部分重叠
    bleu = evaluate.load("bleu")
    refs2 = [["the cat sat on the mat"]]
    pred3 = ["the cat is on the mat"]
    s3 = bleu.compute(
        predictions=pred3, references=refs2
    )["bleu"]
    print(f"部分重叠 BLEU = {s3:.4f}")

    # 测试 3: 空候选(边界)
    pred4 = [""]
    s4 = bleu.compute(
        predictions=pred4, references=refs2
    )["bleu"]
    print(f"空候选 BLEU = {s4:.4f}")
