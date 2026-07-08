"""
[难度: ⭐⭐⭐]
[所属知识点: 端到端评测实战]
[预计完成时间: 15 分钟]

实战: 用 Qwen2-0.5B(或 dummy)对若干测试句算 PPL,
再用相同模型生成候选后对参考句做 BLEU/ROUGE 评估。
注释强调: PPL ≠ 答案正确性,
PPL 只衡量模型对文本的"惊讶程度",
不能替代人工判断。
红线: 测试句必须未参与训练。

示例:
    >>> run()
    平均 PPL = 3.14
    BLEU = 0.25
    ROUGE-1 = 0.40
"""

# ======================
# 学员代码区
# ======================
import evaluate
import math
import torch
import torch.nn as nn

class DummyLM(nn.Module):
    """模拟生成模型,固定 loss=1.2"""
    def __init__(self):
        super().__init__()
        self.x = nn.Linear(1, 1)

    def forward(self, input_ids=None, labels=None):
        loss = torch.tensor(1.2, requires_grad=True)
        return type("O", (), {"loss": loss})()

def run():
    # 1. 准备测试句(未参与训练)
    test_texts = [
        "机器学习是人工智能的一个分支",
        "深度学习需要大量数据",
        "大语言模型可以生成文本",
    ]
    refs = test_texts

    # 2. 用 dummy 模型算 PPL
    model = DummyLM()
    ppls = []
    for t in test_texts:
        # 模拟 forward,取 exp(loss)
        out = model(input_ids=torch.tensor([[1]]),
                    labels=torch.tensor([[1]]))
        ppls.append(math.exp(out.loss.item()))
    avg_ppl = sum(ppls) / len(ppls)

    # 3. 模拟生成候选(这里直接截断参考)
    preds = [t[:4] for t in test_texts]

    # 4. 对候选做 BLEU/ROUGE
    bleu = evaluate.load("bleu")
    rouge = evaluate.load("rouge")
    b = bleu.compute(
        predictions=preds, references=[refs]
    )["bleu"]
    r = rouge.compute(
        predictions=[" ".join(p) for p in preds],
        references=[" ".join(r) for r in refs],
        rouge_types=["rouge1"],
    )["rouge1"]

    print(f"平均 PPL  = {avg_ppl:.4f}")
    print(f"BLEU      = {b:.4f}")
    print(f"ROUGE-1   = {r:.4f}")
    print("注意: PPL ≠ 答案正确性,需人工复核")

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    # 测试 1: 主流程
    run()

    # 测试 2: 空输入(边界)
    print("\n测试2 -> 空输入")
    try:
        bleu = evaluate.load("bleu")
        bleu.compute(predictions=[], references=[[]])
    except Exception as e:
        print(f"捕获异常: {type(e).__name__}")

    # 测试 3: 单句
    print("\n测试3 -> 单句")
    bleu = evaluate.load("bleu")
    s = bleu.compute(
        predictions=["机器学习"],
        references=[["机器学习"]],
    )["bleu"]
    print(f"单句 BLEU = {s:.4f}")
