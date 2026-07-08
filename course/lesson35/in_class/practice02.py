"""
[难度: ⭐⭐]
[所属知识点: BERT 前向传播与隐藏状态]
[预计完成时间: 10 分钟]

用 AutoModel.from_pretrained("bert-base-chinese") 加载
模型,对一条输入(input_ids 形状 (1, 8))做 forward,
打印 last_hidden_state 的形状。提示: 需同时传入
attention_mask。本题目需要联网下载模型。

示例:
    >>> hidden = bert_forward(model, input_ids, mask)
    >>> print(hidden.shape)
    torch.Size([1, 8, 768])
"""

from transformers import AutoModel
import torch

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def bert_forward(model, input_ids, attention_mask):
    """返回 last_hidden_state"""
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    model = AutoModel.from_pretrained("bert-base-chinese")
    # 测试 1: 全 1 注意力掩码
    input_ids = torch.randint(0, 21128, (1, 8))
    mask = torch.ones(1, 8, dtype=torch.long)
    hidden = bert_forward(model, input_ids, mask)
    print("last_hidden_state shape:", hidden.shape)
    # 测试 2: 最后一个token位置
    print("last token shape:", hidden[:, -1, :].shape)
    pass
