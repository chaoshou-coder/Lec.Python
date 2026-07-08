"""
[难度: ⭐]
[所属知识点: nn.RNN 基本使用]
[预计完成时间: 5 分钟]

题目描述: 请使用 torch.nn.RNN 构造一个循环神经网络,
    参数为 input_size=10, hidden_size=20, batch_first=True。
    然后传入一个形状为 (batch=2, seq_len=5, input_size=10)
    的随机张量, 打印输出和隐藏状态的 shape。

示例:
    >>> output, hidden = rnn(x)
    >>> print(output.shape)  # torch.Size([2, 5, 20])
    >>> print(hidden.shape)  # torch.Size([1, 2, 20])
"""

import torch
import torch.nn as nn

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 第一步: 构造 RNN, 指定 input_size=10, hidden_size=20,
#         batch_first=True
rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)

# 第二步: 构造输入张量, 形状 (2, 5, 10)
x = torch.randn(2, 5, 10)

# 第三步: 前向传播, 拿到 output 和 hidden
output, hidden = rnn(x)

# 第四步: 打印 shape
print("输出 output 的 shape:", output.shape)
print("隐状态 hidden 的 shape:", hidden.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape 应为 (2, 5, 20)
    assert output.shape == torch.Size([2, 5, 20]), \
        f"输出 shape 错误, 得到 {output.shape}"
    print("测试 1 通过: 输出 shape 是 (2, 5, 20)")

    # 测试 2: 隐状态 shape 应为 (1, 2, 20)
    assert hidden.shape == torch.Size([1, 2, 20]), \
        f"隐状态 shape 错误, 得到 {hidden.shape}"
    print("测试 2 通过: 隐状态 shape 是 (1, 2, 20)")
