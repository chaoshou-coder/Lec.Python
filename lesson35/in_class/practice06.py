"""
[难度: ⭐⭐⭐⭐]
[所属知识点: nn.MultiheadAttention 与 TransformerEncoderLayer]
[预计完成时间: 20 分钟]

写 TransformerEncoderBlock(nn.Module),实现:
- 使用 nn.MultiheadAttention
- 配合 nn.TransformerEncoderLayer
- 堆叠 3 层
forward 接收 src 形状 (seq_len, batch, d_model),
输出相同形状。提示: batch_first=False。

示例:
    >>> block = TransformerEncoderBlock()
    >>> out = block(torch.randn(10, 2, 64))
    >>> print(out.shape)
    torch.Size([10, 2, 64])
"""

import torch
import torch.nn as nn

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class TransformerEncoderBlock(nn.Module):
    def __init__(self, d_model=64, nhead=8, n_layers=3):
        super().__init__()
        pass

    def forward(self, src):
        """src 形状 (seq_len, batch, d_model)"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(7)
    block = TransformerEncoderBlock()
    src = torch.randn(10, 2, 64)
    # 测试 1: 输出形状与输入相同
    out = block(src)
    print("output shape:", out.shape)
    # 测试 2: 不同 seq_len
    src2 = torch.randn(5, 1, 64)
    out2 = block(src2)
    print("output2 shape:", out2.shape)
    pass
