"""
[难度: ⭐⭐]
[所属知识点: Causal Mask 因果掩码]
[预计完成时间: 10 分钟]

给定一个 4×4 的上三角 -inf 掩码(causal mask),
写 apply_mask(scores, mask),使未来位置对应权重
在 softmax 后趋于 0,实现自注意力中的"只看过去"。
scores 形状 (4, 4),mask 形状 (4, 4)。

示例:
    >>> masked = apply_mask(scores, mask)
    >>> print(masked)
    [[ 0.  -inf -inf -inf]
     [ 0.   0.  -inf -inf]
     [ 0.   0.   0.  -inf]
     [ 0.   0.   0.   0. ]]
"""

import torch
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def apply_mask(scores, mask):
    """将 mask 加到 scores 上,返回被 mask 的张量"""
    return pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(1)
    scores = torch.randn(4, 4)
    # 构造上三角 -inf 掩码
    mask = torch.triu(
        torch.full((4, 4), float('-inf')), diagonal=1
    )
    # 测试 1: 应用掩码
    masked = apply_mask(scores, mask)
    print("masked:\n", masked)
    # 测试 2: softmax 后上三角为 0
    attn = F.softmax(masked, dim=-1)
    print("softmax:\n", attn)
    pass
