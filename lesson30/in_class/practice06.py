"""
[难度: ⭐⭐⭐]
[所属知识点: nn.LSTM 变长序列处理]
[预计完成时间: 15 分钟]

题目描述:
用 nn.LSTM 处理一批变长序列(合成数据),打印 output、hidden state、
cell state 的 shape。场景:你在做文本分类,RNN 组同事让你
"先跑通一个最小 LSTM 看各个输出的维度"。

LSTM 参数:
    input_size=10(每个时间步的特征维)
    hidden_size=20(隐状态维)
    num_layers=2(堆叠 2 层)

合成数据:
    batch=4 个序列,长度分别为 5、4、3、2。
    先用 pad_sequence 补齐,再 pack_padded_sequence 喂给 LSTM。

示例:
    >>> output shape: torch.Size([4, 5, 20])
    >>> h_n shape:    torch.Size([2, 4, 20])
    >>> c_n shape:    torch.Size([2, 4, 20])
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence

# 4 个变长序列,每个时间步特征维=10
seqs = [
    torch.randn(5, 10),
    torch.randn(4, 10),
    torch.randn(3, 10),
    torch.randn(2, 10),
]
lengths = [5, 4, 3, 2]

# pad_sequence 补 0
from torch.nn.utils.rnn import pad_sequence
padded = pad_sequence(seqs, batch_first=True)  # [4, 5, 10]

# pack
packed = pack_padded_sequence(padded, lengths,
                              batch_first=True,
                              enforce_sorted=False)

# LSTM
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2,
               batch_first=True)

output,(h_n, c_n) = lstm(packed)

print("output shape:", output.data.shape)
print("h_n shape:   ", h_n.shape)
print("c_n shape:   ", c_n.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: h_n/c_n shape = [num_layers, batch, hidden_size]
    assert h_n.shape == torch.Size([2, 4, 20]), \
        f"h_n 期望 [2,4,20],实际 {h_n.shape}"
    assert c_n.shape == torch.Size([2, 4, 20]), \
        f"c_n 期望 [2,4,20],实际 {c_n.shape}"
    print("测试 1 通过")

    # 测试 2: output 总时间步数 = sum(lengths) = 14
    total_steps = output.data.shape[0]
    assert total_steps == 14, \
        f"output 总步数期望 14,实际 {total_steps}"
    print("测试 2 通过")
