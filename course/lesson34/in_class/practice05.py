"""
[难度: ⭐⭐⭐]
[所属知识点: 正弦位置编码 Positional Encoding]
[预计完成时间: 15 分钟]

写 PositionalEncoding(nn.Module),用 sin/cos 函数
生成位置编码,PE(pos,2i)=sin(pos/10000^(2i/d_model)),
PE(pos,2i+1)=cos(pos/10000^(2i/d_model))。
max_len=50, d_model=32。打印前 10 个位置的编码。

示例:
    >>> pe = PositionalEncoding(d_model=32, max_len=50)
    >>> out = pe(torch.randn(1, 10, 32))
    >>> print(out.shape)
    torch.Size([1, 10, 32])
"""

import torch
import torch.nn as nn
import math

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class PositionalEncoding(nn.Module):
    def __init__(self, d_model=32, max_len=50):
        super().__init__()
        pass

    def forward(self, x):
        """x 形状 (batch, seq_len, d_model)"""
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    pe = PositionalEncoding(d_model=32, max_len=50)
    x = torch.randn(1, 10, 32)
    # 测试 1: 输出形状
    out = pe(x)
    print("output shape:", out.shape)
    # 测试 2: 前 10 位置编码
    print("PE first 10:\n", pe.pe[0, :10, :4])
    pass
