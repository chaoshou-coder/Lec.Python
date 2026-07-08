# Day 33 · 序列模型 for Text

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: 已掌握 PyTorch、反向传播、CNN/RNN 直觉、梯度下降
> 关键问题: BoW 丢掉了词序 —— 要让模型"按顺序读"文本,该怎么做?本节学 RNN/LSTM 的"逐字阅读 + 记忆传递"机制,并亲手体验 RNN 的致命短板(梯度消失),为 Day 34 注意力机制做铺垫
>
> 代码环境: `pip install torch numpy`

---

## 0. 引入(5 分钟)

- **提问**(2 分钟): "我写了一部电影评论'剧情不精彩',BoW 看到的是{'剧情','不','精彩'}三个词 —— 模型知道'不'修饰'精彩'吗?" 引出"顺序建模"的必要性。
- **赏玩 demo**(3 分钟): 现场写一个 **字符级 RNN** 生成"猫坐在垫子上..." 的代际输出(第 1 代乱码 → 第 50 代像模像样),一句话吊胃口:**"这就是早期 ChatGPT 的雏形!"**

---

## 1. 第一讲(45 分钟) —— RNN:逐字阅读的"记忆读者"

### 知识点 1.1 RNN 直觉:像人逐字读书,边读边记

RNN(Recurrent Neural Network) = 每一步读一个 token,同时把"之前的记忆"通过**隐藏状态(hidden state)** 传给下一步。

```text
        读"猫"          读"坐在"         读"垫子"
          ↓                ↓                ↓
x₁ ─→ [ RNN 单元 ] ─→ [ RNN 单元 ] ─→ [ RNN 单元 ] ─→ 预测下一个字
          ↓                ↓                ↓
         h₁               h₂               h₃
      (记忆更新)        (记忆更新)        (记忆更新)
```

```python
import torch
import torch.nn as nn

# 字符级 RNN:输入一个字符,输出下一个字符的分布
class CharRNN(nn.Module):
    def __init__(self, vocab_size, embed_dim=32, hidden_dim=64):
        super().__init__()
        self.hidden_dim = hidden_dim
        # 把字符索引映射成稠密向量
        self.embed = nn.Embedding(vocab_size, embed_dim)
        # RNN 核心层:hidden_dim 是"记忆容量"
        self.rnn = nn.RNN(embed_dim, hidden_dim, batch_first=True)
        # 把隐藏状态映射回词表大小
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        # x: (batch, seq_len)
        x = self.embed(x)                          # → (batch, seq_len, embed_dim)
        out, hidden = self.rnn(x, hidden)          # out: (batch, seq_len, hidden_dim)
        logits = self.fc(out)                      # → (batch, seq_len, vocab_size)
        return logits, hidden
```

> 类比: RNN 就像读者边读边在心里"做笔记"(h),读新书时参考之前的笔记。**笔记只有一个**,每一页都会修改它。

### 知识点 1.2 隐藏状态(hidden state)的数学直觉

每一步的计算:

```text
h_t = tanh(W_h · h_{t-1} + W_x · x_t + b)
```

- `W_h`: 前一状态的权重 —— "如何整合旧记忆"
- `W_x`: 当前输入的权重 —— "如何吸收新信息"
- `tanh`: 把值压到 (-1, 1),防止爆炸

```python
# 单步计算演示(不依赖 nn.RNN)
import torch
import math

def rnn_step(x_t, h_prev, W_h, W_x, b):
    """手动写一步 RNN 计算"""
    return torch.tanh(W_h @ h_prev + W_x @ x_t + b)

# 假设 hidden_dim=4, embed_dim=3
h = torch.zeros(4)                    # 初始记忆:空白
x = torch.randn(3)                    # 当前输入(嵌入后的字符)
W_h = torch.randn(4, 4) * 0.1        # 旧记忆权重
W_x = torch.randn(4, 3) * 0.1        # 新输入权重
b = torch.zeros(4)
h_new = rnn_step(x, h, W_h, W_x, b)
print(h_new)  # 第一步记忆已被更新
```

> 关键理解: RNN 每一步用的**权重完全一样**(参数共享),所以能处理任意长度序列 —— 就像"同一套做笔记的规则,读哪本书都适用"。

### 知识点 1.3 训练 RNN:随时间反向传播(BPTT)

```python
# 伪代码:训练一个"下一个字符预测"任务
model = CharRNN(vocab_size=100)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(100):
    hidden = None
    losses = []
    for char_input, char_target in dataloader:
        # char_input: (batch, seq_len)
        logits, hidden = model(char_input, hidden)
        # 展平后算交叉熵
        loss = criterion(logits.view(-1, 100), char_target.view(-1))
        loss.backward()        # BPTT:沿时间展开求梯度
        optimizer.step()
        optimizer.zero_grad()
        losses.append(loss.item())
    print(f"Epoch {epoch}: loss={sum(losses)/len(losses):.3f}")
```

> 🔴 教学红线(BPTT 不是火箭科学): BPTT = 把 RNN 沿时间展开成一个"超长链式网络",然后用普通反向传播。学员常觉得 BPTT 是一门新技术 —— 其实只是"展开 + 调用 autograd"。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 用 `nn.RNN` 实现"字符级语言模型",训练 50 个 epoch 后输出一段 50 字的生成文本(⭐⭐,20 分钟)
- 练习 2: `in_class/practice02.py` —— 打印 `model.rnn.weight_hh_l0` 和 `weight_ih_l0` 的维度,理解 RNN 的参数共享(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 1 常有人忘记每批开始时 detach hidden(`hidden.detach_()`),导致梯度图跨批累积 —— 提示:`.detach_()` 是截断 BPTT 的常用手段。

---

## 3. 第二讲(45 分钟) —— LSTM:门控机制拯救"长期记忆"

### 知识点 3.1 🔴 RNN 的核心痛点:梯度消失

RNN 的记忆是"覆盖式"的:每读一个新词,旧记忆被冲淡一点。长距离依赖("文章开头提到的名字影响结尾的指代")在数学上等价于:

```text
∂L/∂h₀ = ∂L/∂hₜ · (W_h)^t            # t 步反向传播的梯度
```

- 若 `W_h` 的特征值 < 1 → 连乘 t 次 → 梯度趋近 0(**梯度消失**)
- 若 `W_h` 的特征值 > 1 → 连乘爆炸(**梯度爆炸**,通常用梯度裁剪解决)

```python
# 直观演示:连乘小矩阵会让向量消失
W = torch.randn(4, 4) * 0.5     # 特征值 < 1
v = torch.ones(4)
for t in range(1, 51):
    v = W @ v
    if t in [1, 5, 10, 50]:
        print(f"连乘 {t} 次后,向量范数={v.norm():.6f}")
# 连乘 1 次后,向量范数=1.234567
# 连乘 5 次后,向量范数=0.023451
# 连乘 10 次后,向量范数=0.000104    ← 接近 0!
# 连乘 50 次后,向量范数=0.000000
```

> 🔴 教学红线(RNN 遗忘不是 Bug 是 Bug): RNN 遗忘远距离信息不是工程没做好,是**结构决定的**。LSTM 和 Transformer 是对症下药的两条路 —— 这是本节承上启下的关键认识。

### 知识点 3.2 LSTM 三门机制:遗忘 / 输入 / 输出

LSTM(Long Short-Term Memory)引入"细胞状态(cell state)C_t"作为长期记忆存储,用三道门控制信息流动:

```text
遗忘门 f_t = σ(W_f · [h_{t-1}, x_t])     # "哪些旧记忆该丢弃?"
输入门 i_t = σ(W_i · [h_{t-1}, x_t])     # "哪些新信息该存进去?"
候选状态 C̃_t = tanh(W_c · [h_{t-1}, x_t]) # "新信息的候选内容"
细胞状态 C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t  # "旧记忆×遗忘 + 新信息×输入"
输出门 o_t = σ(W_o · [h_{t-1}, x_t])     # "读了之后该输出什么?"
隐藏状态 h_t = o_t ⊙ tanh(C_t)            # "最终传递给下一步的记忆"
```

> 类比: 细胞状态 C_t 是"笔记本",三道门是三种操作:
> - 遗忘门 = 用橡皮擦(选择性擦除旧内容)
> - 输入门 = 拿钢笔写(选择性写入新内容)
> - 输出门 = 把笔记本上的内容口述给别人听
>
> RNN 只有一个 h(总在擦掉重写),LSTM 的 C 可以**长期保留**(只要遗忘门 ≈ 1)。

```python
import torch
import torch.nn as nn

class CharLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=32, hidden_dim=64):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.embed = nn.Embedding(vocab_size, embed_dim)
        # LSTM 层:参数比 RNN 多 4 倍(3 个门 + 候选状态)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embed(x)
        out, hidden = self.lstm(x, hidden)     # hidden = (h, c) 一对
        logits = self.fc(out)
        return logits, hidden
```

> 关键: LSTM 的 `hidden` 是 `(h, c)` 一对,h 是输出记忆(短期),c 是细胞状态(长期)。调用时 `hidden = (h, c)`。

### 知识点 3.3 GRU:门控循环单元,更轻量的替代

GRU(Gated Recurrent Unit)把细胞状态合并回隐藏状态,只有**重置门 + 更新门**:

```text
更新门 z_t = σ(W_z · [h_{t-1}, x_t])     # "多大程度上保留旧记忆?"
重置门 r_t = σ(W_r · [h_{t-1}, x_t])     # "多大程度上忽略旧记忆?"
候选状态 h̃_t = tanh(W · [r_t ⊙ h_{t-1}, x_t])
隐藏状态 h_t = (1 - z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t
```

> 对比: GRU 参数比 LSTM 少 1/3,在中小数据集上经常和 LSTM 打平。工业界 LSTM / GRU 都还在用,但**序列建模的主流已被 Transformer 取代**(Day 34 为什么)。

## 4. 当堂练 2(30 分钟)

- 练习 3: `in_class/practice03.py` —— 用 `nn.LSTM` 替换 `nn.RNN`,对比在"长序列(200 字符)预测任务"上的 loss 曲线,感受 LSTM 缓解梯度消失(⭐⭐⭐,25 分钟)
- 练习 4: `in_class/practice04.py` —— 可视化 LSTM 的遗忘门和输入门激活值,观察不同位置的"记忆强度"(⭐⭐⭐⭐,30 分钟)

> 巡场重点: 练习 3 需要保证 RNN/LSTM 的 hidden_dim 和训练参数完全一致(只换层),否则没有可比性。提示: 用 `torch.manual_seed(42)` 固定初始化。

---

## 5. 第三讲(30 分钟) —— 字符级语言模型:生成文本

### 知识点 5.1 文本生成:一张接一张地"掷骰子"

训练好的语言模型给出每个候选词的概率,采样得到的下个字符再拼回去当输入,循环往复:

```python
def generate(model, start_str, char2idx, idx2char, length=200, temperature=0.8):
    model.eval()
    input_seq = torch.tensor([[char2idx[c] for c in start_str]])
    hidden = None
    generated = list(start_str)
    for _ in range(length):
        with torch.no_grad():
            logits, hidden = model(input_seq[:, -1:], hidden)
        # temperature 高 → 分布平坦(更随机);温度低 → 更确定(更保守)
        probs = torch.softmax(logits[0, -1] / temperature, dim=-1)
        next_idx = torch.multinomial(probs, 1).item()
        generated.append(idx2char[next_idx])
        input_seq = torch.tensor([[next_idx]])
    return "".join(generated)

# 生成示例
# print(generate(model, "猫", char2idx, idx2char, length=100))
```

> 类比: temperature 就像"创造力旋钮"。temperature=0 → 永远选概率最高的词(机械、重复);temperature=2 → 胡言乱语;0.5~1.0 是常用区间。

### 知识点 5.2 为什么字符级语言模型"很慢但很直观"

| 维度 | 字符级 | 词级 |
|---|---|---|
| 词表大小 | ~100 | ~30000 |
| 训练难度 | 小 | 大 |
| 序列长度 | 长(每个字一个 token) | 短 |
| 生成效果 | 经常造词 | 更流畅 |

本节故意用字符级,因为**预训练 BERT/GPT 用的子词 tokenizer 还没讲**(Day 36)。但 Day 33 的直觉可直接推广到子词级别。

### 知识点 5.3 RNN/LSTM 在工业界的遗留角色

虽然 Transformer 主导 NLP,但 LSTM 在以下场景仍有优势:
1. **流式处理**(实时传感器数据)—— Transformer 需要看完整句子,LSTM 可以"一个字一个字实时处理"
2. **超小设备**(MCU / IoT)—— LSTM 参数少、推理快
3. **时间序列预测**(股票、气温) —— 没有"翻译"任务,双向结构没意义

## 6. 当堂练 3(30 分钟)

- 练习 5: `in_class/practice05.py` —— 调整 `temperature` 从 0.1 到 2.0,记录生成的文本差异,总结温度的作用(⭐⭐,20 分钟)
- 练习 6: `in_class/practice06.py` —— 把 LSTM 应用于一个时间序列预测任务(气温),感受"序列模型通用性"(⭐⭐⭐⭐,30 分钟)

> 巡场重点: 练习 6 要让学员把"字序列"替换成"数值序列",token embedding 换成线性层 —— 这样模型框架几乎不变,体现"序列模型通用性"。

## 7. 小项目(45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. LSTM hidden 是 `(h, c)` 一对,很多人只用一个 tensor,报错 `expected a tuple of (h, c)`
  2. 生成文本时忘记 `model.eval()`,导致 Dropout 还在运行,生成结果不稳定
  3. 实践"BPTT 截断"时忘记 `hidden.detach_()`导致 GPU 显存溢出
- **作业说明**: 课后 `homework/task01.py`(完成一个可交互的"诗人 LSTM")、`homework/task02.py`(可视化梯度范数沿时间步的衰减),下节课前 10 分钟复盘

---

## 易错点

1. **LSTM hidden 是 tuple**: `hidden = (h, c)`,不是单个 tensor;取隐藏状态输出要 `hidden[0]`,取细胞状态要 `hidden[1]`。
2. **detach hidden**: BPTT 跨 batch 累积会爆显存,每批结束应做 `hidden = (hidden[0].detach(), hidden[1].detach())`。
3. **temperature 是除不是乘**: `logits / temperature`,学员常写反。
4. **RNN/LSTM 的 hidden_dim 越大≠越好**: 大 hidden 容易过拟合,文本任务一般 128~512 就够用。
5. **BPTT 不是新算法**: 就是"把 RNN 沿时间展开 + autograd",不要和 RTRL(Real-Time Recurrent Learning)搞混。

## 延伸题

- **(LSTM Sentiment Classifier, Karpathy 2015 blog, ⭐⭐⭐)**: 在 IMDB 上用 LSTM 做情感分析,观察"长期依赖"在哪类评论上最有用(先扬后抑 / 先抑后扬的评论)。
- **(Visualizing LSTM Activations, Andrej Karpathy, ⭐⭐⭐)**: 把 LSTM 每一时间步的门激活值画出来,会发现有些神经元专门检测"引号内内容"、"段落结尾" —— 震撼学员的直观素材。
- **(The Unreasonable Effectiveness of RNN, Karpathy Blog, ⭐⭐⭐)**: 完整阅读 Karpathy 的经典博客,看"莎士比亚风格生成"的 demo —— 既是本节的应用,也是 Day 34 注意力登台的最好铺垫。
