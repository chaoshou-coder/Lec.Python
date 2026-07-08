"""
[难度: ⭐⭐⭐⭐]
[所属知识点: TransformerEncoderLayer 子层整合]
[预计完成时间: 20 分钟]

整合前 5 个模块,写 TransformerEncoderLayer(nn.Module):
结构: MultiHeadAttention → 残差 + LayerNorm →
      FFN(Linear→ReLU→Linear) → 残差 + LayerNorm。
参数: d_model=64, n_heads=8, d_ff=128, dropout=0.1。

示例:
    >>> layer = TransformerEncoderLayer()
    >>> out = layer(torch.randn(2, 5, 64))
    >>> print(out.shape)
    torch.Size([2, 5, 64])
"""

import torch
import torch.nn as nn

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class TransformerEncoderLayer(nn.Module):
    def __init__(
        self, d_model=64, n_heads=8, d_ff=128, dropout=0.1
    ):
        super().__init__()
        pass

    def forward(self, x):
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    torch.manual_seed(4)
    layer = TransformerEncoderLayer()
    x = torch.randn(2, 5, 64)
    # 测试 1: 输出形状与输入相同
    out = layer(x)
    print("output shape:", out.shape)
    # 测试 2: 多层堆叠
    y = layer(layer(x))
    print("stacked output shape:", y.shape)
    pass
