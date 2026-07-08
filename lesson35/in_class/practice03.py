"""
[难度: ⭐⭐]
[所属知识点: BERT 序列分类与 logits 输出]
[预计完成时间: 10 分钟]

用 AutoModelForSequenceClassification.from_pretrained
("bert-base-chinese", num_labels=3) 加载分类模型,
对一条输入做 forward,打印 logits 形状。
本题目需要联网下载模型。

示例:
    >>> logits = clf_forward(model, input_ids, mask)
    >>> print(logits.shape)
    torch.Size([1, 3])
"""

from transformers import AutoModelForSequenceClassification
import torch

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def clf_forward(model, input_ids, attention_mask):
    """返回 logits 张量"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    model = (
        AutoModelForSequenceClassification
        .from_pretrained("bert-base-chinese", num_labels=3)
    )
    # 测试 1: 单条样本
    input_ids = torch.randint(0, 21128, (1, 6))
    mask = torch.ones(1, 6, dtype=torch.long)
    logits = clf_forward(model, input_ids, mask)
    print("logits shape:", logits.shape)
    # 测试 2: batch=2
    input_ids2 = torch.randint(0, 21128, (2, 6))
    mask2 = torch.ones(2, 6, dtype=torch.long)
    logits2 = clf_forward(model, input_ids2, mask2)
    print("logits2 shape:", logits2.shape)
    pass
