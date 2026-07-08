"""
[难度: ⭐⭐⭐]
[所属知识点: 因果自注意力 Causal Self-Attention]
[预计完成时间: 15 分钟]

写 CausalSelfAttention(nn.Module),实现:
- d_model=32, n_heads=4 -> d_k=8
- 线性投影 Q/K/V,拆头,带 causal mask 的 SDPA
- 验证: 位置 i 的输出只依赖 ≤i 的输入

示例:
    >>> sa = CausalSelfAttention()
    >>> out = sa(torch.randn(1, 6, 32))
    >>> print(out.shape)
    torch.Size([1, 6, 32])
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class CausalSelfAttention(nn.Module):
    def __init__(self, d_model=32, n_heads=4):
        super().__init__()
        pass

    def forward(self, x):
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(6)
    sa = CausalSelfAttention()
    x = torch.randn(1, 6, 32)
    # 测试 1: 输出形状
    out = sa(x)
    print("output shape:", out.shape)
    # 测试 2: 修改位置 5 不应影响位置 3 输出
    x2 = x.clone()
    x2[:, 5, :] = 999
    out2 = sa(x2)
    print("pos3 unchanged:", torch.allclose(
        out[:, 3, :], out2[:, 3, :]
    ))
    pass
