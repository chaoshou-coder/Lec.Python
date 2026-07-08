"""
[难度: ⭐⭐]
[所属知识点: 序列模型 / RNN 前向传播 / one-hot 编码]
[预计完成时间: 10 分钟]

把字符序列 "abcd" 灌进一层 SimpleRNN，打印输出与隐状态的 shape。

任务:
  1. 建立字符到索引的映射 vocab = {'a':0,'b':1,'c':2,'d':3}
  2. 把 "abcd" 转成 one-hot 向量，构造形状 (1, 4, 4) 的输入张量
     (batch=1, seq_len=4, input_size=4)
  3. 定义一层 torch.nn.RNN(input_size=4, hidden_size=8,
     batch_first=True)
  4. 前向传播得到 output, hn
  5. 打印 output 与 hn 的形状

示例:
    >>> output, hn = rnn(x)
    >>> print(output.shape, hn.shape)
    torch.Size([1, 4, 8]) torch.Size([1, 1, 8])
"""

import torch
import torch.nn as nn

# 字符表: a,b,c,d 对应 0,1,2,3
vocab = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
seq = "abcd"
input_size = len(vocab)          # 4
hidden_size = 8

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 步骤 1: 把 "abcd" 转成索引序列，再 one-hot 编码
# hints: torch.nn.functional.one_hot(seq_idx, input_size)
seq_idx = torch.tensor([[vocab[ch] for ch in seq]])  # (1,4)
x = torch.nn.functional.one_hot(seq_idx, input_size)
x = x.float()                     # 转成浮点，便于 RNN 计算

# 步骤 2: 定义 SimpleRNN 模型
rnn = nn.RNN(input_size=input_size, hidden_size=hidden_size,
             batch_first=True)

# 步骤 3: 前向传播
output, hn = rnn(x)

# 步骤 4: 打印形状
print("output 的形状:", output.shape)
print("hn 的形状:   ", hn.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: output 形状应为 (1, 4, 8)
    assert output.shape == (1, 4, 8), \
        f"output shape 错误: 期望 (1,4,8) 实际 {output.shape}"
    # 测试 2: hn 形状应为 (1, 1, 8)
    assert hn.shape == (1, 1, 8), \
        f"hn shape 错误: 期望 (1,1,8) 实际 {hn.shape}"
    print("测试通过: shape 正确!")
