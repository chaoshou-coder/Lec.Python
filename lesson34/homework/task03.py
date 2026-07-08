"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 可学习位置编码与正弦位置编码]
[预计完成时间: 20 分钟]

实现两个模块:
1. position_encoding_sinusoidal(seq_len, d_model):
   返回 (seq_len, d_model) 的 sin/cos 位置编码张量
2. PositionalEmbedding(nn.Module):
   用 nn.Embedding 实现可学习的位置编码

示例:
    >>> pe = position_encoding_sinusoidal(10, 16)
    >>> emb = PositionalEmbedding(max_len=50, d_model=16)
    >>> print(pe.shape, emb(torch.randn(2,10,16)).shape)
    torch.Size([10, 16]) torch.Size([2, 10, 16])
"""

import torch
import torch.nn as nn
import math

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def position_encoding_sinusoidal(seq_len, d_model):
    """返回 (seq_len, d_model) 正弦位置编码"""
    pass


class PositionalEmbedding(nn.Module):
    def __init__(self, max_len=50, d_model=16):
        super().__init__()
        pass

    def forward(self, x):
        """x 形状 (batch, seq_len, d_model)"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正弦编码形状
    pe = position_encoding_sinusoidal(10, 16)
    print("sinusoidal shape:", pe.shape)
    # 测试 2: 可学习编码输出形状
    emb = PositionalEmbedding(max_len=50, d_model=16)
    x = torch.randn(2, 10, 16)
    out = emb(x)
    print("learnable output shape:", out.shape)
    pass
