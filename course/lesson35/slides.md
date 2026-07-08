# Day 35 · Transformer + 预训练模型

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: 已掌握注意力机制(Scaled Dot-Product Attention、多头注意力、位置编码)、PyTorch 基础
> 关键问题: Day 34 讲清了注意力的"零件",本节拼成完整的 Transformer 编码器-解码器架构,并解析 BERT/GPT/T5 的"取捨之道" —— 不同预训练目标决定不同擅长任务
>
> 代码环境: `pip install torch transformers`

---

## 0. 引入(5 分钟)

- **提问**(2 分钟): "注意力是零件,Transformer 是整车 —— 把 Day 34 的 Q/K/V 计算铺满 N 层,就是 Transformer。但为什么一个架构能衍生出 BERT/GPT/T5 三种?" 引出"零件一样,组装方式 + 训练目标不同"。
- **赏玩 demo**(3 分钟): 现场用 Hugging Face pipeline 调用 BERT 做命名实体识别(NER),展示"北京"被识别为地点、"2024 年"被识别为时间 —— 一句话吊胃口:**"今天亲手看看这个模型内部长什么样。"**

---

## 1. 第一讲(45 分钟) —— Transformer 完整架构

### 知识点 1.1 原论文 Figure 1 拆解:左编码器 / 右解码器

```text
           编码器(共 N 层,通常 N=6)                    解码器(共 N 层)
  ┌──────────────────────────────┐      ┌──────────────────────────────┐
  │  输入 Embedding + PE          │      │  输出 Embedding + PE          │
  │       ↓                       │      │       ↓                       │
  │  ┌─────────────────────┐      │      │  ┌─────────────────────┐      │
  │  │ Multi-Head Attention │      │      │  │ Masked Multi-Head    │      │
  │  │ (自注意力,Q=K=V)     │      │      │  │ Attention (因果掩码) │      │
  │  └────────┬────────────┘      │      │  └────────┬────────────┘      │
  │           ↓ + 残差 + LayerNorm │      │           ↓ + 残差 + LayerNorm │
  │  ┌─────────────────────┐      │      │  ┌─────────────────────┐      │
  │  │ Feed-Forward Network │      │      │  │ Multi-Head Attention │      │
  │  │ (两层全连接+ReLU)    │      │      │  │ (交叉注意力 Q=解码    │      │
  │  └────────┬────────────┘      │      │  │   K=V=编码器输出)    │      │
  │           ↓ + 残差 + LayerNorm │      │  └────────┬────────────┘      │
  └──────────────────────────────┘      │           ↓ + 残差 + LayerNorm │
                                         │  ┌─────────────────────┐      │
                                         │  │ Feed-Forward Network │      │
                                         │  └────────┬────────────┘      │
                                         │           ↓ + 残差 + LayerNorm │
                                         └──────────────────────────────┘
```

> 类比: 编码器 = "读完整篇文章,记下每段的核心";解码器 = "看着笔记,一个字一个字写摘要" —— 交叉注意力是"看笔记"这一步。

### 知识点 1.2 残差连接(Residual Connection):高速公路直通道

每层 Attention / FFN 之后,都要把**输入加回来**:

```text
输出 = LayerNorm(x + SubLayer(x))
```

类比: 残差 = "高速公路上的应急车道" —— 底层信号可以绕过复杂变换直接传到高层,缓解深层网络梯度消失。没有残差,Transformer 只能叠 2-3 层,有了残差能叠 100+ 层(GPT-3 有 96 层)。

```python
class ResidualBlock(nn.Module):
    """残差连接的通用封装"""
    def __init__(self, d_model, dropout=0.1):
        super().__init__()
        self.norm = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, sublayer):
        # 关键点:x 直接加回来 —— 就像"保持原样"的保底选项
        return x + self.dropout(sublayer(self.norm(x)))
```

> 🔴 教学红线(LayerNorm 在残差之后): 有两种顺序 —— Pre-Norm(x + sublayer(norm(x)))和 Post-Norm(norm(x + sublayer(x)))。**2020 年以后几乎所有大模型都改用 Pre-Norm**,训练更稳定。初学者常把 LayerNorm 放错位置,导致训练震荡。

### 知识点 1.3 前馈网络(FFN):两层简单全连接

FFN 对每个位置单独做两次线性变换 + ReLU:

```text
FFN(x) = max(0, x·W₁ + b₁) · W₂ + b₂
```

- 扩展维度: d_model(512) → d_ff(2048) → d_model(512)
- 每个位置独立做(类似 1×1 卷积),不跨位置

```python
class FeedForward(nn.Module):
    def __init__(self, d_model=512, d_ff=2048, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),                    # 后续 GELU 更常用
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x):
        return self.net(x)
```

> 直觉: 注意力是"左右观望,整合信息",FFN是"每个人独立想一想,加深理解"。两者配合 = 先全局消化,再独立思考。

### 知识点 1.4 完整的 Transformer Encoder 层

```python
class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model=512, n_heads=8, d_ff=2048, dropout=0.1):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(
            d_model, n_heads, dropout=dropout, batch_first=True
        )
        self.ffn = FeedForward(d_model, d_ff, dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, src_key_padding_mask=None):
        # 子层 1:自注意力 + 残差 + LayerNorm (Pre-Norm)
        attn_out, weights = self.self_attn(
            x, x, x, key_padding_mask=src_key_padding_mask
        )
        x = x + self.dropout(attn_out)          # 残差 + dropout
        x = self.norm1(x)
        # 子层 2:FFN + 残差 + LayerNorm
        ffn_out = self.ffn(x)
        x = x + self.dropout(ffn_out)
        x = self.norm2(x)
        return x, weights
```

> 🔴 教学红线(`nn.MultiheadAttention` 接口): PyTorch 内置的 API 把 Q/K/V 合并成一个调用,**key_padding_mask**参数直接传 bool mask 即可,不需要自己手写 scaled_attention 那样处理 mask —— 这是 Day 34 手写到 Day 35 调库的衔接点。

## 2. 堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 实现一个 6 层的 `nn.TransformerEncoder`,输入一段随机 token 做前向传播,检查输出维度(⭐⭐⭐,20 分钟)
- 练习 2: `in_class/practice02.py` —— 用 `src_key_padding_mask` 把部分 token pad 掉,验证 self_attn 权重在 pad 位置接近 0(⭐⭐⭐⭐,25 分钟)

> 巡场重点: `nn.TransformerEncoder` 的 `mask` 参数有两个 —— `src_key_padding_mask`(bool,True 表示 pad)和 `src_mask`(L×L,防止信息泄露),学员常搞混。提示:key_padding_mask 用于 pad;causal mask 只用于解码器。

---

## 3. 第二讲(45 分钟) —— BERT/GPT/T5:架构差异 + 预训练目标

### 知识点 3.1 三大架构:取捨之道

| 模型 | 结构 | 自注意力方向 | 核心能力 |
|---|---|---|---|
| BERT | 只用编码器 | 双向(同时看左右) | 理解(分类/NER/问答) |
| GPT | 只用解码器 | 单向(只看上文) | 生成(写作/对话/代码补全) |
| T5 | 编码器 + 解码器 | 双向编码 + 单向解码 | 翻译/摘要(序列到序列) |

> 类比: BERT 是"做阅读理解"(看完文章后答题),GPT 是"续写小说"(只能看上文往下写),T5 是"翻译/摘要"(先读懂原文,再生成译文)。

### 知识点 3.2 BERT:双向编码器

BERT 的预训练任务:
- **Masked Language Model (MLM)**: 随机掩盖 15% 的 token,让模型预测被掩盖的词 —— 因为是双向的,模型能同时利用左右上下文
- **Next Sentence Prediction (NSP)**: 预测两个句子是否相邻 —— 学习句子间关系(后续研究证明 NSP 不太必要,BERT 之后的 RoBERTa 去掉了 NSP)

```text
输入: "我 [MASK] 吃火锅"
     ↓ 编码器(双向)
预测: [MASK] = "喜欢"(概率最高)

双向的优势: "喜欢"同时借助"我"(主语)和"吃火锅"(宾语)
单向的 GPT 只看到"我",预测受限
```

```python
# BERT 分类任务伪代码
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
model = BertForSequenceClassification.from_pretrained(
    "bert-base-chinese", num_labels=2
)

inputs = tokenizer("这部电影很精彩", return_tensors="pt")
outputs = model(**inputs)
pred_label = outputs.logits.argmax(dim=-1)   # 0 或 1(正/负)
```

> 适用任务: 情感分析、命名实体识别(NER)、文本分类、问答抽取(问答的两个 span 要从已给的上下文"理解"出来)

### 知识点 3.3 GPT:单向解码器

GPT 的预训练任务:
- **Causal Language Modeling**: 给定前面的 token,预测下一个 token(和 Day 33 的字符级语言模型一样,只是用 Transformer 解码器 + 子词)

```text
输入: "我 喜欢 吃"
     ↓ 解码器(单向)
预测: 下一个词 = "火锅"(概率最高)

单向的限制: 只能看上文,"吃"后面只能用"吃"和之前的信息
```

```python
# GPT 生成任务伪代码
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

inputs = tokenizer("今天天气真好,", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0]))
# "今天天气真好,我决定出门散步,享受这美好的阳光。"
```

> 适用任务: 文本生成、对话机器人、代码补全、机器翻译(效果比 T5 弱)、内容创作。
>
> 🔴 教学红线(GPT 是"不能看后文"的): GPT 在解码阶段用了 **causal mask**(下三角矩阵)—— 看到的是自己和之前的 token,看不到后面的。如果让 GPT 做"文本分类",它没见过下文做的判断不如 BERT,因为 BERT 是"看完全文再答"。

### 知识点 3.4 T5:编码器-解码器,序列到序列

T5(Text-to-Text Transfer Transformer)把**所有 NLP 任务都统一成"文本 → 文本"**:

```text
翻译:  "translate English to French: The cat is cute." → "Le chat mignon."
摘要:  "summarize: (长文)" → "(摘要)"
分类:  "cola sentence: The course is jumping well." → "acceptable"
```

- 编码器: 双向读原文,建立理解
- 解码器: 关键字逐个生成,通过**交叉注意力**读编码器输出

> 适用任务: 机器翻译、文本摘要、问题生成(从原文生成问题) —— 任何"输入一段文本,输出一段文本"的任务。

## 4. 堂练 2(30 分钟)

- 练习 3: `in_class/practice03.py` —— 用预训练 BERT 做新闻分类,微调最后一个分类头(⭐⭐⭐⭐,30 分钟)
- 练习 4: `in_class/practice04.py` —— 用预训练 GPT-2 续写一段故事,对比 temperature=0.5 和 1.5 的生成差异(⭐⭐⭐,20 分钟)

> 巡场重点: 练习 3 要让学员 **freeze BERT backbone,只训练分类头**(节省显存和时间);练习 4 要让学员理解 GPT 的 `generate()` 内部就是 Day 33 手动采样循环,但是批量 + 优化过的。

---

## 5. 第三讲(30 分钟) —— 模型选型指南

### 知识点 5.1 什么时候用哪个?选型对照表

| 场景 | 推荐模型 | 原因 |
|---|---|---|
| 情感分析/分类 | BERT/RoBERTa | 双向理解上下文 |
| 命名实体识别(NER) | BERT + CRF | 双向,需要词级别标注 |
| 抽取式问答(SQuAD) | BERT | 双向,需要看左右上下文定位答案 span |
| 写作/对话/代码补全 | GPT 系列/Llama | 单向生成,流出品自然 |
| 机器翻译 | T5/mBART/Marian | 编码器-解码器结构对称任务 |
| 文本摘要(抽象) | T5/BART | 需要"先读懂,再写"两步 |
| 长文档理解(>1000 字) | Longformer/BigBird | 标准 Transformer 的 O(n²) 计算复杂度无法承受 |

> 🔴 教学红线(架构不是"哪个更好",是"哪个更合适"): GPT 是最新最热的,但不是所有任务都该用 GPT。BERT 在分类/NER 上仍然优于 GPT —— **任务类型决定架构选择**。

### 知识点 5.2 预训练 + 微调两阶段范式

```text
阶段 1: 预训练(在超大规模语料上,几十 GB 文本,训练几天到几周)
  - BERT: 预测被掩码的词
  - GPT: 预测下一个词
  → 模型学会"通用语言能力"

阶段 2: 微调(在特定任务的小数据集上,几分钟到几小时)
  - 情感分析: 1000 条评论
  - 命名实体: 500 段标注文本
  → 把通用能力"适配"到具体任务
```

> 类比: 预训练 = 在医学院学五年(掌握人体、药理、诊断等);微调 = 在某个科室实习三个月(学心内科具体操作)。没有预训练就微调 = 刚毕业直接上手术台 —— 这是**少样本学习 / 零样本学习要解决的问题**(Day 36 展开)。

### 知识点 5.3 参数规模直觉

```text
BERT-Base:       1.1 亿参数   (12 层,768 维,12 头)
BERT-Large:      3.4 亿参数   (24 层,1024 维,16 头)
GPT-2:           1.5 亿参数   (48 层,1600 维)
GPT-3:           1750 亿参数  (96 层,12288 维)
Llama-2-7B:      70 亿参数
```

> 直觉: 参数量不是越大越好 —— 参数多 → 显存大(70B 模型需 140GB FP16 显存)、推理慢、微调贵。实际工程中 BERT-Base / 7B 级别最常见。

## 6. 当堂练 3(30 分钟)

- 练习 5: `in_class/practice05.py` —— 给 5 个任务选模型(分类/生成/NER/翻译/摘要),写 1-2 句话说明选型理由(⭐⭐,10 分钟)
- 练习 6: `in_class/practice06.py` —— 用 BERT 和 GPT-2 同时在同一段文本上做情感分析,对比输出结果差异(⭐⭐⭐⭐,30 分钟)

> 巡场重点: 练习 6 不需要微调,直接用预训练模型做 zero-shot / few-shot(通过 prompt 引导 GPT),让学员感受**同一个任务,架构不同的两个模型反应有何差异**。

## 7. 小项目(45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 把 `nn.TransformerEncoder` 的 `mask` 参数误用为 pad mask,应该传给 `src_key_padding_mask` 而不是 `mask`
  2. BERT 做生成任务时忘记切换 causal mask,导致训练时可以"偷看下文",实际使用时出现严重性能下降
  3. 选型时盲目追 GPT,结果把"文本分类"这种应该用 BERT 的任务硬用 GPT,效果反而差
- **作业说明**: 课后 `homework/task01.py`(完整实现一个 Transformer 编码器-解码器)、`homework/task02.py`(在 AG News 上微调 BERT 做分类),下节课前 10 分钟复盘

---

## 易错点

1. **关键参数:** `nn.TransformerEncoder(layer, n_layers)` 必须先构造一个 `TransformerEncoderLayer`,再传入编码器 —— 不能直接传配置。
2. **mask 用途区分:** `src_mask` = 防止信息泄露(上三角);`src_key_padding_mask` = 屏蔽 pad(bool 类型);两者可以合用。
3. **BERT/GPT 选错场景:** 分类/NER → BERT;生成 → GPT;翻译摘要 → T5。
4. **预训练和微调的关系:** 没有预训练就做任务 = 随机权重微调,效果惨不忍睹;先预训练再微调是标配。
5. **参数量 VS 任务需求:** 工业界常用 BERT-Base(1.1 亿)/7B 级别,不是越大越好,显存和推理延迟是硬约束。

## 延伸题

- **(Transformer 原论文精读, Vaswani 2017, ⭐⭐⭐⭐⭐)**: 逐段读 "Attention is All Need",对照 Day 35 Figure 1 理解每一行公式对应的代码。
- **(Visualizing Attention Distillation, ⭐⭐⭐)**: 用 `BertViz` 看 BERT 最后一层的注意力分布,观察"[MASK]"位置如何收集全局信息。
- **(Scaling Laws, Chinchilla, ⭐⭐⭐⭐)**: 读 Kaplan 2020 和 Hoffmann 2022,了解"参数量 × 数据量 = 常数"这一反直觉发现 —— 模型越大不是应该配更多参数,而是更多数据。
