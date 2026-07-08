"""
[难度: ⭐⭐]
[所属知识点: PyTorch 张量运算实现注意力]
[预计完成时间: 10 分钟]

给定三个 2×3 张量 Q、K、V,用 PyTorch 实现
attention = softmax(Q @ K^T / sqrt(3)) @ V,
返回结果张量。注意转置与 softmax 维度。

示例:
    >>> out = simple_attention(Q, K, V)
    >>> print(out.shape)
    torch.Size([2, 3])
"""

import torch
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def simple_attention(Q, K, V):
    """Q,K,V 形状 (2,3),返回 (2,3) 张量"""
    d_k = Q.size(-1)
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(5)
    Q = torch.randn(2, 3)
    K = torch.randn(2, 3)
    V = torch.randn(2, 3)
    # 测试 1: 输出形状
    out = simple_attention(Q, K, V)
    print("output shape:", out.shape)
    # 测试 2: 具体数值检查
    print("output:\n", out)
    pass
