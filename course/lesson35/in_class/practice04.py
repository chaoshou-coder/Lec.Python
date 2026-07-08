"""
[难度: ⭐⭐⭐]
[所属知识点: BERT + 线性分类头封装成 PyTorch 模块]
[预计完成时间: 15 分钟]

写 BERTClassifier(nn.Module),结构:
- backbone: AutoModel.from_pretrained("bert-base-chinese")
- 分类头: nn.Linear(768 -> num_labels=5)
forward 返回 logits。本题目需要联网下载模型。

示例:
    >>> clf = BERTClassifier(num_labels=5)
    >>> logits = clf(input_ids, mask)
    >>> print(logits.shape)
    torch.Size([2, 5])
"""

import torch
import torch.nn as nn
from transformers import AutoModel

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class BERTClassifier(nn.Module):
    def __init__(self, num_labels=5):
        super().__init__()
        pass

    def forward(self, input_ids, attention_mask):
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    clf = BERTClassifier(num_labels=5)
    input_ids = torch.randint(0, 21128, (2, 8))
    mask = torch.ones(2, 8, dtype=torch.long)
    # 测试 1: logits 形状
    logits = clf(input_ids, mask)
    print("logits shape:", logits.shape)
    # 测试 2: 单条推理
    logits1 = clf(input_ids[:1], mask[:1])
    print("single logits shape:", logits1.shape)
    pass
