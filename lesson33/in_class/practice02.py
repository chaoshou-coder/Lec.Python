"""
[难度: ⭐⭐]
[所属知识点: RNN 单步前向公式实现]
[预计完成时间: 10 分钟]

题目描述: 请手写一个单步 RNN 函数 manual_rnn_step, 实现公式:
    h_t = tanh(W_h @ h_prev + W_x @ x_t + b)
    其中:
        x_t:    当前时刻输入, 形状 (batch, input_size)
        h_prev: 上一时刻隐状态, 形状 (batch, hidden_size)
        W_h:    隐状态权重, 形状 (hidden_size, hidden_size)
        W_x:    输入权重, 形状 (input_size, hidden_size)
        b:      偏置, 形状 (hidden_size,)
    返回 h_t。

示例:
    >>> x_t = torch.randn(3, 8)
    >>> h_prev = torch.zeros(3, 5)
    >>> W_h = torch.randn(5, 5)
    >>> W_x = torch.randn(8, 5)
    >>> b = torch.zeros(5)
    >>> h_t = manual_rnn_step(x_t, h_prev, W_h, W_x, b)
    >>> print(h_t.shape)  # torch.Size([3, 5])
"""

import torch
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def manual_rnn_step(x_t, h_prev, W_h, W_x, b):
    """单步 RNN 前向: h_t = tanh(W_h@h_prev + W_x@x_t + b)"""
    # 注意: h_prev 与 W_h 相乘顺序为 h_prev @ W_h^T,
    # 等价于 (W_h @ h_prev^T)^T。这里 W_h 形状为
    # (hidden_size, hidden_size), 用矩阵乘法实现:
    h_t = torch.tanh(h_prev @ W_h.T + x_t @ W_x + b)
    return h_t


# 给定随机输入
inputs = torch.randn(3, 4, 8)  # (batch=3, seq_len=4, input_size=8)
batch, seq_len, input_size = inputs.shape
hidden_size = 5

# 初始化权重
W_h = torch.randn(hidden_size, hidden_size)
W_x = torch.randn(input_size, hidden_size)
b = torch.zeros(hidden_size)

# 逐时刻循环计算隐状态
h_prev = torch.zeros(batch, hidden_size)
for t in range(seq_len):
    x_t = inputs[:, t, :]
    h_prev = manual_rnn_step(x_t, h_prev, W_h, W_x, b)
    print(f"时刻 {t+1} 隐状态 shape: {h_prev.shape}")

print("最终隐状态 shape:", h_prev.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape 应为 (batch=3, hidden_size=5)
    assert h_prev.shape == torch.Size([3, 5]), \
        f"输出 shape 错误, 得到 {h_prev.shape}"
    print("测试 1 通过: 输出 shape 是 (3, 5)")

    # 测试 2: 全零输入时验证 tanh(b)=tanh(0)=0
    x_zero = torch.zeros(3, 8)
    h_zero = torch.zeros(3, 5)
    h_out = manual_rnn_step(x_zero, h_zero, W_h, W_x, b)
    assert torch.allclose(h_out, torch.zeros(3, 5), atol=1e-6), \
        "全零输入应输出全零"
    print("测试 2 通过: 全零输入输出为零")
