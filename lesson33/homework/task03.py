"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 序列模型 / LSTM 语言模型 / 字符级文本生成]
[预计完成时间: 20 分钟]

用 LSTM 实现一个字符级语言模型 CharLM:
  - Embedding → LSTM → Linear 三层结构
  - fit_one_epoch(data_loader, optimizer): 训练整轮
  - sample(start, length): 给定起始字，自回归采样生成文本

任务:
  1. 实现 CharLM.__init__: 组合 Embedding/LSTM/Linear
  2. 实现 forward(x, hidden=None): 返回 logits (N,T,V) 与 hidden
  3. 实现 fit_one_epoch: 对每个 batch 调用 train_step 流程，
     返回本轮平均损失
  4. 实现 sample: 用 hidden 状态自回归生成 length 个字符

示例:
    >>> model = CharLM(vocab_size=4, embed_dim=8, hidden_dim=16)
    >>> model.fit_one_epoch(loader, opt)
    >>> print(model.sample("a", 30))
    "abcdabcdabcdabcdabcdabcdabcdab"
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# 字符表: a,b,c,d
chars = ['a', 'b', 'c', 'd']
char2idx = {c: i for i, c in enumerate(chars)}
idx2char = {i: c for i, c in enumerate(chars)}
vocab_size = len(chars)


class CharDataset(Dataset):
    """把长字符串切成 (input, target) 对，target 是 input 右移一位。"""

    def __init__(self, text, seq_len):
        self.x = []
        self.y = []
        for i in range(len(text) - seq_len):
            self.x.append([char2idx[c] for c in text[i:i + seq_len]])
            self.y.append([char2idx[c] for c in text[i + 1:i + seq_len + 1]])

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return (torch.tensor(self.x[idx], dtype=torch.long),
                torch.tensor(self.y[idx], dtype=torch.long))


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class CharLM(nn.Module):
    """字符级 LSTM 语言模型。"""

    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        # 嵌入层: 把字符索引映射成稠密向量
        self.embed = nn.Embedding(vocab_size, embed_dim)
        # LSTM 层: 序列建模核心
        self.lstm = nn.LSTM(embed_dim, hidden_dim,
                            batch_first=True)
        # 线性层: 把隐状态映射回词表空间
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        """前向传播。
        x: (N, T) 字符索引
        返回: logits (N, T, V), hidden
        """
        out = self.embed(x)                # (N, T, E)
        out, hidden = self.lstm(out, hidden)  # (N, T, H)
        logits = self.fc(out)              # (N, T, V)
        return logits, hidden

    def fit_one_epoch(self, data_loader, optimizer):
        """训练一整轮，返回平均损失。"""
        self.train()
        total_loss = 0.0
        n_batch = 0
        criterion = nn.CrossEntropyLoss()
        for batch_x, batch_y in data_loader:
            optimizer.zero_grad()
            logits, _ = self.forward(batch_x)
            # logits (N,T,V) → (N*T, V)，target (N,T) → (N*T)
            loss = criterion(logits.reshape(-1, vocab_size),
                             batch_y.reshape(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            n_batch += 1
        return total_loss / max(n_batch, 1)

    def sample(self, start, length):
        """自回归采样: 从 start 字符串起，生成 length 个字符。"""
        self.eval()
        # 把 start 转成索引张量 (1, len(start))
        inp = torch.tensor([[char2idx[c] for c in start]],
                           dtype=torch.long)
        hidden = None
        generated = list(start)
        # 先用 start 预热，拿到最后一步的 hidden
        with torch.no_grad():
            _, hidden = self.forward(inp, hidden)
            # 最后一个字符作为下一次输入
            last = inp[:, -1:]             # (1, 1)
            for _ in range(length):
                logits, hidden = self.forward(last, hidden)
                # 取最后一个时间步的 logits
                probs = torch.softmax(logits[:, -1, :], dim=-1)
                idx = torch.multinomial(probs, 1)  # (1, 1)
                generated.append(idx2char[idx.item()])
                last = idx
        return ''.join(generated)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 构造一个简单重复文本作为训练数据
    text = "abcd" * 200
    dataset = CharDataset(text, seq_len=8)
    loader = DataLoader(dataset, batch_size=16, shuffle=True)

    # 实例化模型与优化器
    model = CharLM(vocab_size=vocab_size, embed_dim=8,
                   hidden_dim=16)
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # 测试 1: 训练 1 轮，打印平均损失
    avg_loss = model.fit_one_epoch(loader, optimizer)
    print(f"训练 1 轮平均损失: {avg_loss:.4f}")

    # 测试 2: 从 "a" 起生成 30 个字符
    result = model.sample("a", 30)
    print(f"采样结果: {result}")
    assert len(result) == 30 + 1, \
        f"长度错误: 期望 31 实际 {len(result)}"
    print("测试通过: CharLM 训练与采样正常!")
