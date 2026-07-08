# Day38 · 分词与数据准备

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day37 已掌握 HF 工具链、模型选型;Transformer / 自回归 / 注意力深入
> 关键问题: 模型只吃 token ID 序列,中文句子怎么变成一串整数?训练数据长什么样?
> 一句话: 今天给模型准备"饲料"——饲料配方错了,再好的模型也训歪。

---

## 0. 引入(5 分钟)

- **破冰**(3 分钟): 在黑板上写 "我爱机器学习",问学员"这句话进模型之前变成什么?"——引出整数序列 `[1234, 5678, 9012, 3456]`,强调**模型不懂文字,只懂数字**。
- **赏玩 demo**(2 分钟): 终端跑 `tokenizer.encode("Hello 世界")` —— 同样的 "Hello" 在不同模型 tokenizer 下 ID 完全不同,引出"为什么不能换 tokenizer"。

---

## 1. 第一讲(15 分钟) —— Tokenizer 原理复习 + 坑

### 知识点 1.1 子词分词:BPE 一句话回顾

BPE 从字符开始,反复合并最高频的相邻 pair,直到词表达到预设大小。

```
"low"  出现 5 次, "new" 出现 6 次, "newest" 出现 3 次
词表大小低 → 切成 "low", "new", "est"
词表大小高 → 直接保留 "newest" 一个 token
```

> 要点: 词表大小决定了"切得多细"。Qwen 词表 150K+,LLaMA 是 32K——每个中文字不一定是一个 token,一个字 1~3 个 token 都有可能。

### 知识点 1.2 为什么微调时不能换 tokenizer

模型的第一层是 **nn.Embedding(vocab_size, hidden_dim)**,shape 由训练时的词表决定。换 tokenizer = 换词表 = 所有 ID 都对不上 = **白训了**。

```python
# 正确: 用预训练模型自带的 tokenizer
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")

# 错误示范(不要这样做):
# tok = AutoTokenizer.from_pretrained("bert-base-chinese")
```

> 🔴 教学红线(tokenizer 不一致): 新手最常见的翻车——用 LLaMA 模型加 BERT tokenizer,直接报 shape mismatch 或效果极差。**训哪个模型就用哪个模型的 tokenizer,没有例外**。必要时可微调 embedding 层(高级话题,本课不展开)。

### 知识点 1.3 `tokenizer()` 返回什么

```python
text = "Hello 世界"
out = tok(text, return_tensors="pt")  # pt = PyTorch tensor
print(out["input_ids"])       # tensor([[1234, 5678, ...]])
print(out["attention_mask"])  # tensor([[1, 1, ...]])  ← 1=实词,0=填充
```

> `attention_mask` 是让模型"别看填充位"的关键——Day 40 批次训练必用。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 对比同一个句子在 Qwen tokenizer 和 GPT-2 tokenizer 下的 token 数(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 给定 10 句中文,打印"句子 → [token IDs → 字"的对照表(⭐⭐⭐,10 分钟)

> 巡场重点: 学员常漏 `return_tensors="pt"`,拿到 list 而不是 tensor——后面模型推理时类型不匹配报错。

---

## 3. 第二讲(15 分钟) —— Chat Template 与指令数据格式

### 知识点 3.1 System / User / Assistant 三角色

现代 Chat 模型把一次对话切成"角色":

```
System:  你是一个乐于助人的助手    ← 定义人设
User:    写一首关于春天的诗          ← 用户提问
Assistant: 春眠不觉晓...            ← 模型回答
```

> 每段前面有固定分隔符(各模型不同),拼好后再 tokenize——这是模型训练时见过的格式。

### 知识点 3.2 Alpaca 格式(最常用微调格式)

```json
{
    "instruction": "写一首关于春天的诗",
    "input": "",                  ← 可选的上下文/空也可
    "output": "春眠不觉晓,处处闻啼鸟"
}
```

### 知识点 3.3 ShareGPT 格式(多轮对话)

```json
{
    "conversations": [
        {"from": "human", "value": "写一首关于春天的诗"},
        {"from": "gpt", "value": "春眠不觉晓..."},
        {"from": "human", "value": "帮我翻译成英文"},
        {"from": "gpt", "value": "Spring sleep unaware..."}
    ]
}
```

>选哪个? **Alpaca 单轮简单、ShareGPT 多轮强**,新手从 Alpaca 上手。

### 知识点 3.4 `apply_chat_template`:让库自动拼格式

```python
messages = [
    {"role": "system", "content": "你是一个乐于助人的助手"},
    {"role": "user", "content": "写一首关于春天的诗"},
]
# 自动生成带角色前缀的纯文本
prompt = tok.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,  # 关键!末尾加 "Assistant:"
)
print(prompt)
```

> 🔴 教学红线(add_generation_prompt): 忘加 `add_generation_prompt=True`,模型不知道自己该说话,会继续补用户的话。**微调时必有 system+user+assistant 三段,推理时必有 True**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 手写一条 Alpaca 格式数据,再用 `apply_chat_template` 转成 Chat 格式(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 给定 raw conversation,用 `dataset.map()` 批量转 Chat 格式(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常把 `role` 拼错("assistant" 拼成 "Assistant",大小写敏感)——应用小写或复制常量,不要手打。

---

## 5. 第三讲(15 分钟) —— 数据预处理:打包 / Padding / Truncation

### 知识点 5.1 `datasets.load_dataset()`加载 HF 数据集

```python
from datasets import load_dataset

# 加载 Alpaca 格式中文数据集
ds = load_dataset("silk-road/alpaca-data-gpt4-chinese", split="train")
print(ds[0])  # {'instruction': ..., 'input': ..., 'output': ...}
```

### 知识点 5.2 `dataset.map()`批量预处理

```python
def build_prompt(example):
    text = (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Input:\n{example['input']}\n\n"
        f"### Response:\n{example['output']}"
    )
    return {"text": text}

ds = ds.map(build_prompt, remove_columns=ds.column_names)
```

> `remove_columns` 删掉旧列,只保留 `text`——省内存、避免后面 dataset 字段冲突。

### 知识点 5.3 批次训练的三大策略

| 策略 | 做法 | 何时用 |
|---|---|---|
| Padding | 短句末尾补 `<pad>` 到批次最长 | 批次训练必须 |
| Truncation | 长句截断到 `model_max_length` | 长文本/显存紧张 |
| Packing | 多条短句拼到同一序列(不浪费 padding) | 生产级高效训练 |

```python
tok(
    text_list,
    padding="longest",       # 或 "max_length"
    truncation=True,
    max_length=512,
    return_tensors="pt",
)
```

> Colab T4 场景:`max_length=512` 通常够用,跑 0.5B 模型可适当拉到 1024。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 加载一个开源数据集,画 token 长度分布直方图,选 `max_length`(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员把所有长度都加进数据集,画图才发现 95% 的样本 ≤ 256——盲目设 2048 是浪费显存。**先画图,再设参数**。

## 7. 小项目(若本日有)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后填进 `teacher_notes.md`):
  1. 微调时换 tokenizer,白训一整晚
  2. `apply_chat_template` 忘加 `add_generation_prompt=True`
  3. 批量 tokenize 时漏 `padding=True` / `truncation=True`,批次报错
- **作业说明**: `homework/task01.py`(从 raw 数据做到 batches),下节课复盘。

---

## 易错点

1. **换 tokenizer**: 微调哪个模型就用哪个的 tokenizer,否则 embedding 不匹配。
2. **漏 add_generation_prompt**: 推理时必加,否则模型不知道该回答。
3. **padding 忘开**: 批次里不同长度必须 pad 到等长,报 shape error。
4. **max_length 拍脑袋**: 先画长度分布图再定,否则要么浪费显存要么截断太多。
5. **map 后列残留**: `remove_columns=ds.column_names` 免字段冲突。

## 延伸题

- **(Token 长度侦探, ⭐⭐)**: 给 10 句中文 + 10 句英文,看哪个在 Qwen 下 token 更长——理解"中文有时更贵"。
- **(Alpaca ↔ ShareGPT 互转, ⭐⭐⭐)**: 写一个函数把 Alpaca 转成 ShareGPT 格式,多轮对话怎么处理?
- **(Packing 手写, ⭐⭐⭐⭐)**: 给定 100 条长短不一的句子,手动"装箱"到 max_length=512 的序列里,画出 padding 比例对比图。
