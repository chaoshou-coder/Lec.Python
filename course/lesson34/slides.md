# Day 34 · 注意力机制深入到底⚡

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: 已掌握 RNN/LSTM、PyTorch、反向传播、梯度下降
> 关键问题: RNN 遗忘远距离信息 —— 能不能**不靠顺序传递记忆**,而是让模型"直接看到整句话的任意位置"?本节从 0 推导注意力机制的核心公式,手算注意力权重,并实现 PyTorch 版 Scaled Dot-Product Attention —— 这是整个 transformer 的基石
>
> 代码环境: `pip install torch matplotlib`
> 特别说明: 本节是 Day 32-36 最难的课,节奏放慢,图示优先,公式必须手推

---

## 0. 引入(5 分钟)

- **提问**(2 分钟): "你读英文长句时,看到句尾的动词,需要回找主语 —— RNN 通过逐字记忆来找,但中间隔了 20 个词,记忆早就模糊了。你有什么更好的方法?" 引出"直接定位"vs"传承记忆"的对立。
- **赏玩 demo**(3 分钟): 展示两张注意力热力图(一行英文、一行中文的对齐权重),"看,模型自己学会了哪个中文词对应哪个英文词!" 一句话吊胃口:**"这个热力图背后的机制,就是 attention —— 本节课要亲手造它。"**

---

## 1. 第一讲(45 分钟) —— 为什么需要注意力:RNN 的三大死穴

### 知识点 1.1 RNN 的三个痛点:顺序处理 / 遗忘远程 / 不可并行

1. **顺序处理**: RNN 必须一个 token 一个 token 地读,(t 时刻必须等 t-1 时刻完成),GPU 并行能力浪费 —— 序列越长,训练越慢
2. **遗忘远程**: Day 33 的梯度消失实验已经证明 —— 超过 ~20 步以后,梯度往回传的长度受限,模型"记不住"长距离依赖
3. **信息瓶颈**: 整句话必须"挤"进一个固定大小的 hidden vector —— 不管是 10 个词还是 1000 个词,最后压缩成一个 h

```python
# 痛点演示:RNN 最后一步的 h_T 是不是"整句话的压缩"?
# 序列长度 5 vs 序列长度 200:同样一个 h(维度 64),能装下多少信息?
seq_short = torch.randn(5, 32)    # 5 步,embed_dim 32
seq_long  = torch.randn(200, 32)  # 200 步
rnn = nn.RNN(32, 64, batch_first=True)
_, h_short = rnn(seq_short.unsqueeze(0))
_, h_long  = rnn(seq_long.unsqueeze(0))
# h_short 和 h_long 的维度一样:(1, 1, 64) —— 这就是"瓶颈"
print(h_short.shape, h_long.shape)  # torch.Size([1, 1, 64]) 一样!
```

> 🔴 教学红线(RNN 不是"不够努力",是"结构不行"): RNN 再怎么调参,这三个痛点都是结构性的。**注意力机制不是"改善" RNN,而是"绕开"它** —— 让每个词直接看到所有其他词,通过权重"告诉"模型"我该看谁"。

### 知识点 1.2 注意力直觉:查字典类比 ( Query / Key / Value )

这是本节最关键的类比,讲三遍:

```text
你在图书馆查"attention 机制":
  - Query(查询) = 你想找的内容:"attention 机制"
  - Key(键) = 每本书脊上的标签:"机器学习"、"神经科学"、"深度学习"
  - Value(值) = 每本书的**实际内容**(不只是标签)
```

1. 用 Query 和每个 Key 算**相似度**(dot product) —— 匹配程度
2. 把相似度归一化(softmax) —— 得到**权重**
3. 用权重对 Value 做**加权和** —— 得到最终的"检索结果"

```text
           最终输出 = Σ (权重_i × Value_i)
权重_i    = softmax(Query · Key_i)
```

> 类比: 不是"完全匹配后返回一本书",而是**每本书都读一点,匹配度高的多读,匹配度低的少读**。	Value 才是真正的知识,Key 只是索引,Query 是你的需求。

### 知识点 1.3 从直觉到公式:Scaled Dot-Product Attention

把查字典类比翻译成数学:

```text
Attention(Q, K, V) = softmax(Q · Kᵀ / √d_k) · V
```

- `Q`: 查询矩阵,形状 `(n_q, d_k)` —— 当前关注的位置
- `K`: 键矩阵,形状 `(n_v, d_k)` —— 所有可索引的位置
- `V`: 值矩阵,形状 `(n_v, d_v)` —— 每个位置的实际信息
- `d_k`: Query 和 Key 的维度(缩放因子要用到)
- `√d_k`: 缩放因子(为什么?知识点 2.4 讲)

```python
import torch
import torch.nn.functional as F

def attention(Q, K, V):
    """版本 1:未缩放(后续改进为 Scaled)"""
    # Q: (n_q, d_k), K: (n_v, d_k), V: (n_v, d_v)
    scores = Q @ K.T                          # (n_q, n_v) 每个 query 对每个 key 的分数
    weights = F.softmax(scores, dim=-1)        # (n_q, n_v) 归一化
    output = weights @ V                       # (n_q, d_v) 对 Value 做加权和
    return output, weights
```

> 类比: `Q @ K.T` 是匹配分,softmax 是"把所有匹配分摊平成概率分布",`weights @ V`是"按概率读信息"。**三步合起来 = 一次注意力计算**。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 用"查字典"类比手工走一次:Q="猫",Keys=["猫:毛","狗:汪","鸟:飞"],操作三步得到输出(⭐⭐,15 分钟)
- 练习 2: `in_class/practice02.py` —— 把注意力写成 numpy(不用 torch),彻底理解 `(Q @ K.T) @ V` 的维度变化(⭐⭐⭐,20 分钟)

> 巡场重点: 练习 2 必须让学员画维度变化图:`(n_q,d_k) @ (d_k,n_v) → (n_q,n_v)`,再 `(n_q,n_v) @ (n_v,d_v) → (n_q,d_v)`。提示: 只要матри乘法维度对齐,具体 n_q/n_v/d_v 任意换。

---

## 3. 第二讲(45 分钟) —— 手算一个完整的注意力例子

### 知识点 3.1 手算:Q = [1, 0] 的例子

这是本节的"心脏"部分,逐步手推,让学员跟着算:

```text
假设:
  Q  = [1, 0]                  (维度 d_k = 2)
  K₁ = [1, 0], V₁ = [10, 0]    (词 1:指向"右边")
  K₂ = [0, 1], V₂ = [0, 10]    (词 2:指向"上边")

Step 1: 计算匹配分(点积)
  score₁ = Q · K₁ = 1×1 + 0×0 = 1
  score₂ = Q · K₂ = 1×0 + 0×1 = 0

Step 2: softmax 归一化
  weight₁ = e¹ / (e¹ + e⁰) = 2.718 / (2.718 + 1.0) ≈ 0.731
  weight₂ = e⁰ / (e¹ + e⁰) = 1.0   / (2.718 + 1.0) ≈ 0.269

Step 3: 对 Value 做加权和
  output = 0.731 × [10, 0] + 0.269 × [0, 10]
         = [7.31, 0] + [0, 2.69]
         = [7.31, 2.69]

解读: Q=[1,0] 和 K₁=[1,0] 匹配(都是"右边方向"),所以 V₁ 的权重 0.731,
     输出主要"指向右边" —— 这就是"注意力选择了相关信息的直观体现"! ✨
```

```python
import torch
import torch.nn.functional as F

Q  = torch.tensor([[1.0, 0.0]])
K  = torch.tensor([[1.0, 0.0],
                   [0.0, 1.0]])
V  = torch.tensor([[10.0, 0.0],
                   [ 0.0, 10.0]])

scores = Q @ K.T                     # [[1, 0]]
weights = F.softmax(scores, dim=-1)  # [[0.7311, 0.2689]]
output = weights @ V                 # [[7.31, 2.69]]
print(f"权重: {weights}")
print(f"输出: {output}")             # ≈ [7.31, 2.69] —— 以 V₁ 为主!
```

> 🔴 教学红线(Q 和 K 必须维度相同): `Q @ K.T` 要求 Q 和 K 的最后一维都是 d_k。学员经常 Q 用 embed_dim、K 用不同维度,导致矩阵乘法报错。

### 知识点 3.2 为什么除以 √d_k:缩放直觉

问题: 当 d_k 很大时,Q 和 K 的点积方差会随之增长,导致 softmax 输出**接近 one-hot**(最大的接近 1,其他接近 0) —— 梯度几乎为 0,训练不动。

```python
# 直觉演示:当 d_k = 100 和 d_k = 10000 时的差异
import torch
import math

d_k = 10000
# 标准正态分布的 Q,K
Q = torch.randn(1, d_k)
K = torch.randn(10, d_k)
raw_scores = Q @ K.T                # 未缩放
raw_std = raw_scores.std().item()
print(f"d_k={d_k} 时,点积标准差 ≈ {raw_std:.2f}")   # ≈ 100 = √d_k

# 除以后
scaled_scores = raw_scores / math.sqrt(d_k)
scaled_std = scaled_scores.std().item()
print(f"除 √d_k 后,标准差 ≈ {scaled_std:.2f}")    # ≈ 1.0 —— 正是我们想要的!
```

> 数学直觉: 当 Q、K 的元素均值 0 方差 1 时,点积的方差 = d_k。除以 √d_k 后,方差归一化到 1。**softmax 输入方差太大会"堵塞"梯度,方差太小又区分不了候选词,1.0 左右正合适**。

```python
def scaled_attention(Q, K, V):
    """版本 2: 加入缩放因子(这才是标准版)"""
    d_k = Q.size(-1)
    scores = Q @ K.T / math.sqrt(d_k)         # ⭐ 区别在这里
    weights = F.softmax(scores, dim=-1)
    output = weights @ V
    return output, weights
```

> 记忆口诀:"点积方差随 d_k 涨,除以 √d_k 拉回 1",这个√在几乎所有 Transformer 实现里都会出现。

### 知识点 3.3 多头注意力(Multi-Head):多个"视角"并行提取

单头注意力只能学一种关系(语法或语义或位置),多头 = 多个**独立的注意力头并行**,每头关注不同方面:

```text
   Head 1 (语法视角):   猫 → 坐(V₂)       关注"谁在做什么"
   Head 2 (语义视角):   猫 → 狗(猫科对比)   关注"同类/异类"
   Head 3 (位置视角):   猫 → 上一个词      关注"上下文衔接"
```

```python
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads       # 每头维度:512/8 = 64

        # Q/K/V 各自一个线性层(实现"投影到不同子空间")
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        # 多头拼接后的逆投影
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, Q, K, V, mask=None):
        batch_size = Q.size(0)
        # 1. 线性投影
        Q = self.W_q(Q)
        K = self.W_k(K)
        V = self.W_v(V)
        # 2. 拆成多头:(batch, seq, d_model) → (batch, n_heads, seq, d_k)
        Q = Q.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        K = K.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        V = V.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        # 3. 计算注意力(每个头独立)
        d_k = self.d_k
        scores = Q @ K.transpose(-2, -1) / math.sqrt(d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        weights = F.softmax(scores, dim=-1)
        context = weights @ V                    # (batch, n_heads, seq, d_k)
        # 4. 多头拼接
        context = context.transpose(1, 2).contiguous()
        context = context.view(batch_size, -1, self.d_model)
        return self.W_o(context), weights
```

> 类比: 单头 = 一个记者单视角报道;多头 = 8 个记者同时采访,最后**汇总**出全面报道。每个记者看同一事件的不同"维度"(谁、何时、为何、怎么)。

> 🔴 教学红线(view vs transpose): 学员常写 `Q.view(batch, self.n_heads, -1, self.d_k)` 得到**错误拼接**,因为 view 后 n_heads 和 seq 维度可能错乱 —— 必须先 **transpose(1,2)** 让 n_heads 成为第二维度,再 view 拆。

## 4. 当堂练 2(30 分钟)

- 练习 3: `in_class/practice03.py` —— 实现 `scaled_attention` 函数,并在 Q/K 都加一个 padding 维度,验证 softmax 权重是否合理(⭐⭐⭐,20 分钟)
- 练习 4: `in_class/practice04.py` —— 修改 Q = [0, 1],重算手算例子,观察权重如何"倒向另一边"(⭐⭐,10 分钟)

> 巡场重点: 练习 4 是巩固 Q 改变 → 权重翻转 → 输出选择不同 V 的直觉链,务必让学员手写验证权重之和 = 1。

---

## 5. 第三讲(45 分钟) —— 位置编码:让模型知道词的位置

### 知识点 5.1 为什么注意力需要"位置编码"?

回顾 Scaled Dot-Product Attention 公式:

```text
Attention(Q, K, V) = softmax(Q · Kᵀ / √d_k) · V
```

**Q、K、V 都与位置无关** —— 只是把 token embedding 线性投影。如果把句子的词序打乱("垫子上坐猫"vs"猫坐在垫子上"),注意力输出完全一样!因为 attention 本身是"集合操作",不感知顺序。

```python
# 演示:打乱序的 Q/K/V 得到相同的注意力输出
Q_orig = torch.randn(1, 5, 8)       # 5 个 token
K_orig = torch.randn(1, 5, 8)
V_orig = torch.randn(1, 5, 8)
out1, _ = scaled_attention(Q_orig[0], K_orig[0], V_orig[0])

# 打乱 token 顺序
idx = torch.tensor([3, 0, 4, 1, 2])
out2, _ = scaled_attention(Q_orig[0, idx], K_orig[0, idx], V_orig[0, idx])
# out1 ≠ out2,但 out2 对应位置仍映射到打乱后的 token —— 模型感觉不到"顺序"
```

> 🔴 教学红线(没有位置编码的 Transformer 是词袋升级版): 没有位置编码,Transformer 退化成**"加权版 BoW"** —— 知道哪些词在一起,但不知道谁先谁后。加位置编码 = 给每个 token 戴个"工牌"。

### 知识点 5.2 位置编码公式:正弦余弦交替

Transformer 原论文(Attention is All You Need, Vaswani 2017)使用**固定位置编码**(不是学习出来的):

```text
PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
```

- `pos`:  token 在句子中的位置(0, 1, 2, ...)
- `i`:   维度的索引
- `d_model`: embedding 维度(通常 512)

```python
import torch
import matplotlib.pyplot as plt

def positional_encoding(max_len, d_model):
    """生成 (max_len, d_model) 的位置编码矩阵"""
    pe = torch.zeros(max_len, d_model)
    pos = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)  # (max_len, 1)
    div = torch.exp(torch.arange(0, d_model, 2).float()
                 * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = sin = torch.sin(pos * div)      # 偶数维:sin
    pe[:, 1::2] = cos = torch.cos(pos * div)      # 奇数维:cos
    return pe

# 可视化:位置编码矩阵(横轴=位置,纵轴=维度)
pe = positional_encoding(max_len=100, d_model=64)
plt.imshow(pe.T, cmap="viridis", aspect="auto")
plt.xlabel("位置 pos")
plt.ylabel("维度 i")
plt.title("位置编码热力图")
plt.colorbar()
plt.show()
# 观察:低频维度(顶部)随位置变化平滑,高频维度(底部)震荡剧烈
```

> 直觉: 每个位置的编码是独一无二的"ID 卡"(类似二进制表示),但用**连续函数**编码 —— 相近位置的编码也相近,模型能自然感知"相对位置"。

### 知识点 5.3 把位置编码加到 embedding 上

```python
class TokenWithPosition(nn.Module):
    def __init__(self, vocab_size, d_model, max_len=512):
        super().__init__()
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.register_buffer("pe", positional_encoding(max_len, d_model))
        self.dropout = nn.Dropout(0.1)

    def forward(self, token_ids):
        # token_ids: (batch, seq_len)
        x = self.token_embed(token_ids)            # (batch, seq_len, d_model)
        seq_len = x.size(1)
        x = x + self.pe[:seq_len, :].unsqueeze(0)  # 加上位置编码
        return self.dropout(x)
```

> 🔴 教学红线(位置编码是"相加"不是"拼接"): 相加是 Vaswani 2017 的原始做法,后续研究也试过拼接,但相加在几乎所有版本中都效果更好(参数更少、维度不变)。不要让学生自创"拼接"做法。

## 6. 当堂练 3(30 分钟)

- 练习 5: `in_class/practice05.py` —— 实现完整的 Scaled Dot-Product Attention(带 mask),在一段"我 喜欢 Python __"上预测下一个词,输出注意力热力图(⭐⭐⭐⭐,30 分钟)
- 练习 6: `in_class/practice06.py` —— 实现 MultiHeadAttention 类,8 个头并行,可视化不同头学到的注意力模式差异(⭐⭐⭐⭐⭐,40 分钟)

> 巡场重点: 练习 5 要让学员画二维热力图(rows = query 位置, cols = key 位置,颜色 = 权重),**这是本节"真正的掌握标志"** —— 能画出来说明真会了。

## 7. 小项目(45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 多头注意力 view 之后 n_heads / seq_len 维度错乱,输出乱码 —— 必须先 transpose 再 view
  2. 手算例子中忘记除以 √d_k,当 d_k=64 时 softmax 已经接近 one-hot,梯度消失
  3. 忘记给位置编码做 `register_buffer`,导致模型.to(device) 时 pe 留在 CPU 上报错
- **作业说明**: 课后 `homework/task01.py`(手写 complete Transformer Encoder 层)、`homework/task02.py`(实现因果 mask 并可视化),下节课前 10 分钟复盘

---

## 易错点

1. **Q @ K.T 不是 K @ Q.T**: 顺序不能反,Q 的最后一维必须和 K 的最后一维一致(d_k)
2. **缩放因子 √d_k 是除不是乘**: 学员常写成 `score * math.sqrt(d_k)`,导致方差爆炸
3. **多头注意力的 view 前先 transpose**: `transpose(1,2).view(batch, -1, n_heads, d_k)`
4. **位置编码是加不是拼接**: `x = embed(x) + pe[:seq_len]`,不要 `torch.cat([embed, pe], dim=-1)`
5. **mask 必须加 -1e9 不是 0**: softmax(-1e9) ≈ 0,softmax(0) ≈ 不合理权重 —— `masked_fill(mask == 0, -1e9)`
6. **位置编码要用 register_buffer 注册**: 这样 `.to(device)` 时自动随模型移动,本身不被优化器更新

## 延伸题

- **(Attention Visualization, Berger 2020, ⭐⭐)**: 用 `BertViz` 工具可视化 BERT 不同层不同头的注意力模式,直观看到"有些头只关注局部、有些关注 `[SEP]` 分隔符"
- **(Transformer Anatomy, VLAD, ⭐⭐⭐⭐)**: 拆解原论文 Figure 1 的每个符号,对照 PyTorch 代码 —— 适合"读论文焦虑"的学员练手的位置
- **(Position Encoding Variants, ⭐⭐⭐⭐⭐)**: 对比 sinusoidal 固定编码 vs 可学习位置编码 vs RoPE(Rotary Position Embedding, LLaMA 使用)—— 这是当前大模型的研究前沿,可引导学员做小实验
