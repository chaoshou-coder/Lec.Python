"""
[难度: ⭐⭐⭐]
[所属知识点: ROUGE 评测]
[预计完成时间: 15 分钟]

用 evaluate.load("rouge") 计算中文 ROUGE 分数。
参考摘要: "机器学习是人工智能的子领域"
候选摘要: "机器学习属于 AI"
输出 ROUGE-1 与 ROUGE-L 的 fmeasure。
注意: 中文需以字或词粒度切分,
本例直接按字符列表传入。

示例:
    >>> run()
    ROUGE-1 = 0.33, ROUGE-L = 0.33
"""

# ======================
# 学员代码区
# ======================
import evaluate

def run():
    rouge = evaluate.load("rouge")
    # 中文按字切分,避免 tokenizer 把中文整体当 token
    ref = [" ".join("机器学习是人工智能的子领域")]
    pred = [" ".join("机器学习属于 AI")]

    res = rouge.compute(
        predictions=pred,
        references=ref,
        rouge_types=["rouge1", "rougeL"],
    )
    print(f"ROUGE-1  = {res['rouge1']:.4f}")
    print(f"ROUGE-L  = {res['rougeL']:.4f}")

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程
    run()

    # 测试 2: 完全一致
    rouge = evaluate.load("rouge")
    r2 = " ".join("机器学习是人工智能的子领域")
    s2 = rouge.compute(
        predictions=[r2], references=[r2],
        rouge_types=["rouge1", "rougeL"]
    )
    print(f"完全一致 ROUGE-1 = {s2['rouge1']:.4f}")

    # 测试 3: 完全不同的句子
    bad = " ".join("今天天气真好啊")
    g = " ".join("深度学习模型训练")
    s3 = rouge.compute(
        predictions=[bad], references=[g],
        rouge_types=["rouge1", "rougeL"]
    )
    print(f"完全不同 ROUGE-1 = {s3['rouge1']:.4f}")
