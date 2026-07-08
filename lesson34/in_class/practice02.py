"""
[难度: ⭐⭐]
[所属知识点: 缩放点积注意力 Scaled Dot-Product Attention]
[预计完成时间: 10 分钟]

写 scaled_dot_product_attention(Q, K, V),用 PyTorch 实现:
先算 Q@K^T / sqrt(d_k),再做 softmax 得到权重,
最后乘 V 得到输出。返回 (weights, output)。
张量形状: Q/K/V 均为 (batch, seq_len, d_k)。

示例:
    >>> W, O = scaled_dot_product_attention(Q, K, V)
    >>> print(O.shape)
    torch.Size([1, 2, 2])
"""

import torch
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def scaled_dot_product_attention(Q, K, V):
    """缩放点积注意力,返回 (权重, 输出)"""
    d_k = Q.size(-1)
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(0)
    Q = torch.randn(1, 2, 4)
    K = torch.randn(1, 3, 4)
    V = torch.randn(1, 3, 4)
    # 测试 1: 输出形状
    W, O = scaled_dot_product_attention(Q, K, V)
    print("weights:", W.shape, "output:", O.shape)
    # 测试 2: 权重每行和为 1
    print("row sums:", W.sum(dim=-1))
    pass
