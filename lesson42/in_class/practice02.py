"""
[难度: ⭐⭐]
[所属知识点: Perplexity 的前向计算]
[预计完成时间: 10 分钟]

写一个函数 compute_ppl(model, tokenizer, texts, device="cpu"),
对每条文本 tokenize 后做前向传播,
用 loss = forward(**inputs, labels=inputs).loss,
取 exp 得到单条 PPL,最后对所有文本取平均。
红线提示: 这里 texts 必须是没有参与训练的测试集。
用 dummy nn.Module 模拟 model 行为,验证函数流程。

示例:
    >>> compute_ppl(dummy_model, tok, ["hello", "world"])
    平均 PPL = 2.71
"""

# ======================
# 学员代码区
# ======================
import math
import torch
import torch.nn as nn

class DummyLM(nn.Module):
    """模拟语言模型,每次返回固定 loss=1.0"""
    def __init__(self):
        super().__init__()
        self.dummy = nn.Linear(1, 1)

    def forward(self, input_ids=None, labels=None):
        batch = input_ids.shape[0]
        # 返回一个带 loss 的对象
        loss = torch.tensor(1.0, requires_grad=True)
        return type("O", (), {"loss": loss})()

def compute_ppl(model, tokenizer, texts, device="cpu"):
    # 对 texts 逐条 tokenize,前向计算 loss,
    # 收集 exp(loss) 后返回平均 PPL
    pass

# ======================
# 测试区
# ======================
if __name__ == '__main__':
    class DummyTok:
        def __call__(self, text, return_tensors=None):
            # 模拟 tokenizer,返回 input_ids
            length = len(text)
            ids = torch.tensor([[1] * max(length, 1)])
            return {"input_ids": ids}

    tok = DummyTok()
    model = DummyLM()

    # 测试 1: 两条文本
    texts1 = ["hello", "world"]
    ppl1 = compute_ppl(model, tok, texts1)
    print(f"测试1 -> 平均 PPL = {ppl1:.4f}")

    # 测试 2: 单条文本
    texts2 = ["ppl is perplexity"]
    ppl2 = compute_ppl(model, tok, texts2)
    print(f"测试2 -> 平均 PPL = {ppl2:.4f}")

    # 测试 3: 空列表(边界)
    texts3 = []
    ppl3 = compute_ppl(model, tok, texts3)
    print(f"测试3 -> 平均 PPL = {ppl3}")
