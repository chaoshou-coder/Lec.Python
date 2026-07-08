"""
[难度: ⭐⭐⭐]
[所属知识点: 字符级 next-char 预测 + CrossEntropyLoss]
[预计完成时间: 15 分钟]

题目描述: 给定短序列 "hello", 使用上一题的 CharLSTM 做
    字符级 next-char 预测并计算损失。规则如下:
    - 编码 "hello" 得到索引序列 [7,4,11,11,14]
    - 输入 input = "hell" (前 4 个字符)
    - 目标 target = "ello" (后 4 个字符, 即下一个字符)
    - 前向传播得到 logits, 用 CrossEntropyLoss 计算 loss

示例:
    >>> loss = criterion(logits.view(-1, vocab_size),
    ...                 target.view(-1))
    >>> print(loss.item())  # 正数, 如 3.2958
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class CharLSTM(nn.Module):
    """与上一题相同的 CharLSTM, 供本题使用"""

    def __init__(self, vocab_size, embed_dim, hidden_size):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(
            embed_dim, hidden_size, batch_first=True
        )
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        emb = self.embed(x)
        lstm_out, _ = self.lstm(emb)
        logits = self.fc(lstm_out)
        return logits


# 字符表定义
chars = "abcdefghijklmnopqrstuvwxyz "
char_to_idx = {ch: i for i, ch in enumerate(chars)}
vocab_size = len(chars)  # 27

# 模型参数
embed_dim = 16
hidden_size = 32
model = CharLSTM(vocab_size, embed_dim, hidden_size)
model.eval()  # 仅前向, 关闭 dropout

# 编码 "hello"
word = "hello"
ids = [char_to_idx[ch] for ch in word]
print(f"'{word}' 编码: {ids}")

# 输入 = 前 4 个字符 "hell"
input_ids = torch.tensor([ids[:-1]])   # (1, 4)
# 目标 = 后 4 个字符 "ello"
target_ids = torch.tensor([ids[1:]])   # (1, 4)

print(f"输入 shape:  {input_ids.shape}")
print(f"目标 shape:  {target_ids.shape}")

# 前向传播
logits = model(input_ids)
print(f"logits shape: {logits.shape}")  # (1, 4, 27)

# 计算 CrossEntropyLoss
# 需要把 logits reshape 成 (N, C)
loss = F.cross_entropy(
    logits.view(-1, vocab_size), target_ids.view(-1)
)
print(f"损失值: {loss.item():.4f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: loss 应为正数标量
    assert loss.dim() == 0, "loss 应为标量"
    assert loss.item() > 0, \
        f"loss 应为正数, 得到 {loss.item()}"
    print(f"测试 1 通过: loss = {loss.item():.4f} > 0")

    # 测试 2: logits shape 应为 (1, 4, 27)
    assert logits.shape == torch.Size([1, 4, vocab_size]), \
        f"logits shape 错误, 得到 {logits.shape}"
    print("测试 2 通过: logits shape 是 (1, 4, 27)")

    # 测试 3: loss 应为有限数值
    assert torch.isfinite(loss).item(), \
        "loss 不是有限数值"
    print("测试 3 通过: loss 是有限数值")
