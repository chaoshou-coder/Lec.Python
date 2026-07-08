"""
[难度: ⭐⭐⭐]
[所属知识点: 字符级 LSTM 模型定义]
[预计完成时间: 15 分钟]

题目描述: 请定义一个字符级 LSTM 模型 CharLSTM(nn.Module),
    结构如下:
    1. 嵌入层 nn.Embedding(vocab_size, embed_dim)
    2. LSTM 层 nn.LSTM(embed_dim, hidden_size,
       batch_first=True)
    3. 线性输出层 nn.Linear(hidden_size, vocab_size),
       用于把隐状态映射到词表大小的 logits。
    forward 方法接收形状为 (batch, seq_len) 的整数索引,
    返回形状为 (batch, seq_len, vocab_size) 的 logits。

示例:
    >>> model = CharLSTM(vocab_size=27, embed_dim=16,
    ...                  hidden_size=32)
    >>> x = torch.randint(0, 27, (2, 5))
    >>> logits = model(x)
    >>> print(logits.shape)  # torch.Size([2, 5, 27])
"""

import torch
import torch.nn as nn

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class CharLSTM(nn.Module):
    """字符级 LSTM 语言模型"""

    def __init__(self, vocab_size, embed_dim, hidden_size):
        super().__init__()
        # 嵌入层: 把整数索引映射为稠密向量
        self.embed = nn.Embedding(vocab_size, embed_dim)
        # LSTM 层, batch_first=True
        self.lstm = nn.LSTM(
            embed_dim, hidden_size, batch_first=True
        )
        # 线性层: 隐状态 → logits
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        """
        x: (batch, seq_len) 整数张量
        返回: (batch, seq_len, vocab_size) logits
        """
        # 第一步: 嵌入, (batch, seq_len) → (batch, seq_len, embed_dim)
        emb = self.embed(x)
        # 第二步: LSTM, 输出 (batch, seq_len, hidden_size)
        lstm_out, _ = self.lstm(emb)
        # 第三步: 线性层 → (batch, seq_len, vocab_size)
        logits = self.fc(lstm_out)
        return logits


# 参数设置
vocab_size = 27   # 26 字母 + 空格
embed_dim = 16
hidden_size = 32

# 构造模型
model = CharLSTM(vocab_size, embed_dim, hidden_size)

# 模拟输入: batch=2, seq_len=5
x = torch.randint(0, vocab_size, (2, 5))
print("输入 x shape:", x.shape)

# 前向传播
logits = model(x)
print("输出 logits shape:", logits.shape)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出 shape 应为 (2, 5, 27)
    assert logits.shape == torch.Size([2, 5, vocab_size]), \
        f"输出 shape 错误, 得到 {logits.shape}"
    print("测试 1 通过: 输出 shape 是 (2, 5, 27)")

    # 测试 2: logits 应为有限数值, 不含 NaN
    assert not torch.isnan(logits).any(), \
        "logits 中含有 NaN"
    print("测试 2 通过: logits 不含 NaN")

    # 测试 3: 改变 batch 与 seq_len 也应对
    x2 = torch.randint(0, vocab_size, (4, 10))
    logits2 = model(x2)
    assert logits2.shape == torch.Size([4, 10, vocab_size]), \
        f"shape 错误, 得到 {logits2.shape}"
    print("测试 3 通过: (4, 10) 输入 → (4, 10, 27) 输出")
