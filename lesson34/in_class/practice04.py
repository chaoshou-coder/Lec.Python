"""
[难度: ⭐⭐⭐]
[所属知识点: 多头注意力 Multi-Head Attention]
[预计完成时间: 15 分钟]

手写 MultiHeadAttention(nn.Module),实现:
1. 将 Q/K/V 线性投影到 d_model,再拆成 h 个头
2. 对每个头做 scaled dot-product attention
3. concat 所有头,再做线性投影
参数: d_model=64, n_heads=8, 因此 d_k = d_v = 8。

示例:
    >>> mha = MultiHeadAttention(d_model=64, n_heads=8)
    >>> out = mha(x, x, x)      # x: (2, 5, 64)
    >>> print(out.shape)
    torch.Size([2, 5, 64])
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=64, n_heads=8):
        super().__init__()
        assert d_model % n_heads == 0
        pass

    def forward(self, Q, K, V):
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(2)
    mha = MultiHeadAttention(d_model=64, n_heads=8)
    x = torch.randn(2, 5, 64)
    # 测试 1: 输出形状
    out = mha(x, x, x)
    print("output shape:", out.shape)
    # 测试 2: 不同 seq_len
    x2 = torch.randn(1, 10, 64)
    out2 = mha(x2, x2, x2)
    print("output2 shape:", out2.shape)
    pass
