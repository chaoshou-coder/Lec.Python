"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 自回归字符采样生成]
[预计完成时间: 20 分钟]

题目描述: 请编写一个 generate 函数, 给定一个预训练
    (或随机初始化) 的 CharLSTM 模型与一个起始字符串
    start_str, 自回归地生成 length 个字符并返回完整
    字符串。每一步:
    - 把当前序列喂给模型, 取最后时刻的 logits
    - 用 softmax 转为概率, 按概率采样 (torch.multinomial)
      取下一个字符索引
    - 拼接结果, 把新生成的字符作为下一步输入

示例:
    >>> result = generate(model, "the ", char2idx,
    ...                   idx2char, length=50)
    >>> print(len(result))  # 54 (4 + 50)
    >>> print(result)       # 'the ...'
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class CharLSTM(nn.Module):
    """字符级 LSTM, 与上一题一致"""

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


# 字符表与映射
chars = "abcdefghijklmnopqrstuvwxyz "
char2idx = {ch: i for i, ch in enumerate(chars)}
idx2char = {i: ch for i, ch in enumerate(chars)}
vocab_size = len(chars)  # 27

# 模型(随机初始化, 仅供练习结构)
model = CharLSTM(vocab_size, embed_dim=16, hidden_size=32)
model.eval()


def generate(model, start_str, char2idx, idx2char, length=50):
    """
    自回归采样生成字符。
    参数:
        model: CharLSTM 实例
        start_str: 起始字符串
        char2idx: 字符 → 索引 字典
        idx2char: 索引 → 字符 字典
        length: 生成字符数
    返回:
        完整字符串 (start_str + 生成的字符)
    """
    # 把 start_str 转为索引列表
    input_ids = [char2idx[ch] for ch in start_str]
    result = list(start_str)

    with torch.no_grad():
        for _ in range(length):
            # 构造输入张量 (1, seq_len)
            x = torch.tensor([input_ids])
            # 前向传播, logits shape: (1, seq_len, vocab_size)
            logits = model(x)
            # 取最后时刻的 logits
            last_logits = logits[0, -1, :]  # (vocab_size,)
            # softmax 转概率
            probs = F.softmax(last_logits, dim=0)
            # 按概率采样下一个字符索引
            next_id = torch.multinomial(probs, 1).item()
            # 拼接到结果
            result.append(idx2char[next_id])
            # 把新字符加入输入序列
            input_ids.append(next_id)

    return "".join(result)


# 从 "the " 开始生成 50 个字符
start = "the "
output = generate(model, start, char2idx, idx2char, length=50)
print(f"起始:  '{start}'")
print(f"生成:  '{output}'")
print(f"长度:  {len(output)} (预期 {len(start) + 50})")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出长度应为 len(start) + length
    expected_len = len(start) + 50
    assert len(output) == expected_len, \
        f"长度错误, 期望 {expected_len}, 得到 {len(output)}"
    print(f"测试 1 通过: 输出长度 = {expected_len}")

    # 测试 2: 输出应以 start 开头
    assert output.startswith(start), \
        "输出未以 start_str 开头"
    print(f"测试 2 通过: 输出以 '{start}' 开头")

    # 测试 3: 生成的每个字符都应在字符表中
    for ch in output:
        assert ch in char2idx, \
            f"非法字符 '{ch}' 不在字符表中"
    print("测试 3 通过: 所有字符均合法")
