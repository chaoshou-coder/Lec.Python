# Day 36 · Hugging Face 实战

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: 已掌握 Transformer 架构、BERT/GPT 直觉、PyTorch 基础
> 关键问题: Day 35 清楚了架构差异,本节动手用 Hugging Face **完整走通 NLP 项目**:从加载预训练模型到微调部署,从 pipeline 一键调用到 Dataset 数据处理,覆盖"小样本 + 全流程"实战路径
>
> 代码环境: `pip install torch transformers datasets scikit-learn`

---

## 0. 引入(5 分钟)

- **提问**(2 分钟): "Day 35 我们讲完 BERT/GPT/T5 的架构差异 —— 但你现在有个实际任务(情感分析),从零训练一个 BERT 要 4 张 A100 跑几天。有没有'白嫖'别人的预训练权重、几分钟就跑出自己模型的捷径?" 引出 Hugging Face 生态。
- **赏玩 demo**(3 分钟): 一行代码完成情感分析 —— `pipeline("sentiment-analysis")("今天天气好心情也好")`,1 秒出结果 —— **一句话吊胃口:"今天的课 = 把这种一键能力,变成你自己完全掌控的工具。"**

---

## 1. 第一讲(45 分钟) —— Hugging Face 生态概览 + pipeline 零样本调用

### 知识点 1.1 Hugging Face 三件套

| 库 | 用途 | 核心类 |
|---|---|---|
| `transformers` | 预训练模型 + tokenizer + 训练 API | `AutoModel`, `AutoTokenizer`, `Trainer` |
| `datasets` | 开箱即用数据集,一行下载 | `load_dataset(...)` |
| `tokenizers` | 子词分词算法实现(BPE/WordPiece/Unigram) | `Tokenizer`, ` BertTokenizer` |

> 类比: transformers = "模型超市",datasets = "数据超市",tokenizers = "配套工具箱"。三个库相互独立，但 **90% 的情况一起用**。

### 知识点 1.2 pipeline():零样本调用NLP 任务

`pipeline()` 是 Hugging Face 的"黑盒"API —— 隐藏了 tokenizer + 模型 + 后处理:

```python
from transformers import pipeline

# 1. 情感分析(英文)
sentiment = pipeline("sentiment-analysis")
result = sentiment("I love this course! It's so helpful.")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]

# 2. 命名实体识别(NER)
ner = pipeline("ner", grouped_entities=True)
result = ner("我的名字是李雷,我在北京的 Google 工作。")
print(result)
# [{'entity_group': 'PER', 'word': '李雷', 'score': 0.998},
#  {'entity_group': 'LOC', 'word': '北京', 'score': 0.995},
#  {'entity_group': 'ORG', 'word': 'Google', 'score': 0.991}]

# 3. 文本摘要
summarizer = pipeline("summarization")
result = summarizer(
    "Natural language processing (NLP) is a subfield of linguistics, "
    "computer science, and artificial intelligence concerned with the "
    "interactions between computers and human language...",
    max_length=30, min_length=10,
)
print(result[0]['summary_text'])

# 4. 问答
qa = pipeline("question-answering")
result = qa(
    question="NLP 是哪个领域的子领域?",
    context="NLP 是语言学、计算机科学和人工智能的子领域。",
)
print(result)  # {'answer': '语言学、计算机科学和人工智能', 'score': 0.95}
```

> 类比: pipeline 就像外卖 app —— 你只需要点单("情感分析"),不需要知道cook 怎么做菜、用什么锅(trunk 内部自动处理 tokenizer + 模型 + 后处理)。

> 🔴 教学红线(pipeline 默认下载英文模型): `pipeline("sentiment-analysis") 默认用 distilbert-base-uncased-finetuned-sst-2-english`,中文会乱跑。必须指定 `model="uer/roberta-base-finetuned-chinanews-chinese"` 这样的中文微调模型。

### 知识点 1.3 datasets 库:一行下载数据集

```python
from datasets import load_dataset

# IMDB 影评数据集(英文,5 万条)
ds = load_dataset("imdb")
print(ds)
# DatasetDict({
#     train: Dataset({features: ['text','label'], num_rows: 25000}),
#     test:  Dataset({features: ['text','label'], num_rows: 25000}),
# })

# 中文情感数据集
ds = load_dataset("seamew/ChnSentiCorp")
print(ds["train"][0])
# {'text': '这本书不错,内容详实,推荐给朋友。', 'label': 1}
```

> 直觉: datasets = "sklearn fetch_california_housing 的 NLP 版",自动缓存、支持 Streaming 模式(无需下完全部才启动)。

## 2. 堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 用 pipeline 做情感分析,NER,摘要,问答,各写一行调用并打印结果(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 加载 seAGM dataset,用 `ds["train"].train_test_split(test_size=0.1)` 切分后统计每类数量(⭐⭐⭐,20 分钟)

> 巡场重点: 练习 1 中文任务必须手动指定中文模型 (`uer/roberta-base-finetuned-chinanews-chinese` / `uer/roberta-base-finetuned-jd-binary-chinese`),否则结果不可信。

---

## 3. 第二讲(45 分钟) —— AutoModel + AutoTokenizer:自定义模型

### 知识点 3.1 AutoModel / AutoTokenizer 一一对应

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# "Auto" 自动根据 model_name 加载正确的配置和权重
model_name = "bert-base-chinese"

tokenizer = AutoTokenizer.from_pretrained(model_name)       # 加载 tokenizer
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=2                                 # 分类头 = 随机初始化
)
# model.classifier 层是随机初始化的 —— 需要微调!
```

> 🔴 教学红线(Tokenizer 必须对齐预训练模型): 这是 NLP 头号坑:
> - 用 `"bert-base-chinese"` 的模型 + `"gpt2"` 的 tokenizer → 词表完全不同 → **输出毫无意义**
> - 用 BERT 的 tokenizer + RoBERTa → 特殊 token 不一致 → **结果乱码**
> - 正确做法: **模型名即 tokenizer 名**,从同一个 `model_name` 加载

```python
# 正确:名字一致
tok = AutoTokenizer.from_pretrained("bert-base-chinese")
mod = AutoModelForSequenceClassification.from_pretrained("bert-base-chinese", num_labels=2)

# 错误:名字不一致(同一个 tokenizer 不能服务不同词表的模型!)
tok = AutoTokenizer.from_pretrained("gpt2")
mod = AutoModelForSequenceClassification.from_pretrained("bert-base-chinese", num_labels=2)
# 运行不会报错,但输出是乱码 —— 这是最难排查的 Bug 之一
```

### 知识点 3.2 完整的分词(tokenization)流程

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")

# 单句编码
encoded = tokenizer("我喜欢深度学习")
print(encoded)
# {
#   'input_ids': [101, 1762, 1962, 1399, 7306, 6963, 102],
#   'token_type_ids': [0, 0, 0, 0, 0, 0, 0],    # 句子对任务用(单句全 0)
#   'attention_mask': [1, 1, 1, 1, 1, 1, 1],     # 1 = 真实词,0 = pad
# }

# 批量编码(自动 pad 到最长、自动截断)
texts = ["这部电影真好", "太烂了,浪费时间", "强推"]
encoded = tokenizer(
    texts,
    padding=True,           # pad 到本批最长
    truncation=True,        # 超过 max_length 就截断
    max_length=64,          # 最大长度
    return_tensors="pt",    # 返回 PyTorch tensor
)
print(encoded["input_ids"].shape)     # torch.Size([3, 64])
print(encoded["attention_mask"].shape)
```

> 🔴 教学红线(`max_length` + `padding` + `truncation` 三合一是必须的): 光写 `tokenizer(texts)` 不 pad → 矩阵大小不一,模型报错;不 truncation → 长句爆显存。**三参数必须配套**。

### 知识点 3.3 手写微调循环:用预训练 BERT 做情感分析

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import DataLoader
from datasets import load_dataset
import torch

# 1. 加载模型 + tokenizer
model_name = "bert-base-chinese"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=2
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# 2. 数据预处理函数
def tokenize_fn(batch):
    return tokenizer(
        batch["text"],
        padding="max_length",
        truncation=True,
        max_length=128,
    )

ds = load_dataset("seamew/ChnSentiCorp")
ds = ds.map(tokenize_fn, batched=True)
ds = ds.rename_column("label", "labels")      # Trainer 要求 labels 列
ds.set_format("torch", columns=["input_ids","attention_mask","labels"])
train_loader = DataLoader(ds["train"], batch_size=16, shuffle=True)

# 3. 训练循环
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
for epoch in range(3):
    model.train()
    for batch in train_loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print(f"Epoch {epoch} done")
```

> 学习路径: 手写训练循环(理解每一步)→ 改用 `Trainer` API(简化,Day 36 下节讲)

## 4. 堂练 2(30 分钟)

- 练习 3: `in_class/practice03.py` —— 对 ChnSentiCorp 数据做 tokenization + DataLoader,跑 3 个 epoch 观察 loss 下降曲线(⭐⭐⭐⭐,30 分钟)
- 练习 4: `in_class/practice04.py` —— **故意**用 `bert-base-chinese` 的模型 + `gpt2` 的 tokenizer,观察输出 —— 体验"Tokenizer 没对齐"的恶果(⭐⭐⭐,15 分钟)

> 巡场重点: 练习 4 是"地雷演习" —— 让学员亲自踩一次坑(`tokenizer` 和 `model` 名不一致时模型不报错,但输出乱码),加深印象。

---

## 5. 第三讲(30 分钟) —— Trainer API + 评估 + 保存

### 知识点 5.1 Trainer API:让训练循环"隐形"

Hugging Face 封装的 `Trainer` 等价于手写 DataLoader 循环,但支持混合精度、梯度累积、wandb 集成:

```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",              # 模型保存路径
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    warmup_steps=100,                    # 前 100 步学习率慢慢升
    weight_decay=0.01,                   # L2 正则
    evaluation_strategy="epoch",         # 每个 epoch 后评估
    save_strategy="epoch",               # 每个 epoch 后保存
    logging_dir="./logs",
    logging_steps=50,
    fp16=torch.cuda.is_available(),      # 混合精度(省显存)
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=ds["train"],
    eval_dataset=ds["validation"],
    tokenizer=tokenizer,
)

trainer.train()      # 一行完成训练
results = trainer.evaluate()
print(results)       # {'eval_loss': 0.32, 'eval_runtime': 5.1, ...}
```

> 类比: 手写循环 = 骑自行车,Trainer = 开自动驾驶汽车 —— 都能到达目的地,后者更省心,但**前者更易定制**。生产环境用 Trainer,研究场景手写。

### 知识点 5.2 保存和加载模型

```python
# 保存
trainer.save_model("./my_chinese_sentiment_model")
tokenizer.save_pretrained("./my_chinese_sentiment_model")

# 加载(下游使用时)
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model = AutoModelForSequenceClassification.from_pretrained(
    "./my_chinese_sentiment_model"
)
tokenizer = AutoTokenizer.from_pretrained(
    "./my_chinese_sentiment_model"
)
# 直接跑推理
inputs = tokenizer("这个产品很棒!", return_tensors="pt")
with torch.no_grad():
    logit = model(**inputs).logits
pred = logit.argmax(dim=-1).item()
print("正面" if pred == 1 else "负面")
```

### 知识点 5.3 调参要点:Learning Rate 就是"水温"

| 超参数 | 典型值 | 过大的后果 | 过小的后果 |
|---|---|---|---|
| Learning Rate | 2e-5 ~ 5e-5 | 训练发散(loss 震荡) | 收敛太慢 / 陷入局部最优 |
| Batch Size | 16 ~ 32 | 显存爆炸 | 梯度噪声大 |
| Epochs | 2 ~ 5 | 过拟合 | 欠拟合 |
| Warmup | 总步数 5-10% | 无 | 前期震荡 |

> 🔴 教学红线(预训练模型微调的学习率必须小): 从头训练用 1e-3;**微调预训练模型用 2e-5**。初学者的最大误区:沿用从头训练的学习率,导致预训练权重被严重破坏,效果不如随机模型 —— 这是"灾难性遗忘"。

## 6. 当堂练 3(30 分钟)

- 练习 5: `in_class/practice05.py` —— 用 Trainer API 完成 ChnSentiCorp 微调,输出验证集准确率(⭐⭐⭐,25 分钟)
- 练习 6: `in_class/practice06.py` —— 保存模型,再加载,对比加载前后的输出一致性(⭐⭐,10 分钟)

> 巡场重点: 练习 6 看似 trivial,但学员常忘记保存 `tokenizer`,导致加载时 tokenizer 仍是旧的 —— 提示:"**模型 + tokenizer 必须一起保存,像一个硬币的两面**"。

## 7. 小项目(45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. Tokenizer 没对齐预训练模型,输出乱码 —— 这是 NLP 头号坑
  2. 微调学习率沿用从头训练的 1e-3,导致预训练权重被毁,loss 震荡不收敛
  3. 保存模型时漏了 tokenizer,加载后推理结果对不上
- **作业说明**: 课后 `homework/task01.py`(完整跑通一个情感分析项目:从 pipeline → Trainer → 保存),`homework/task02.py`(用 BertViz 可视化 BERT 注意力权重),下节课前 10 分钟复盘

---

## 易错点

1. **Tokenizer 必须对齐预训练模型**: 模型名 = tokenizer 名,从同一 `model_name` 加载。
2. **微调学习率用 2e-5**: 比从头训练小 3 个数量级,否则预训练权重被毁。
3. **padding + truncation + max_length 三合一是必须的**: 否则矩阵大小不一或长句爆显存。
4. **模型和 tokenizer 要一起保存**: 分开保存导致重新加载时对不上。
5. **pipeline 默认英文模型**: 中文任务必须显式指定中文微调模型(如 `uer/roberta-base-finetuned-chinanews-chinese`)。

## 延伸题

- **(Hugging Face 官方教程, ⭐⭐)**: 读 "Fine-tune a pretrained model"一节 —— 完全覆盖本节内容,是最佳复习。
- **(Prompt Engineering 初探, OpenAI 文档, ⭐⭐⭐)**: 学 zero-shot / few-shot prompting —— 不调权重,用 prompt 引导 GPT 完成任务,与"微调"互补。
- **(Parameter-Efficient Fine-Tuning (LoRA), ⭐⭐⭐⭐)**: 学习 LoRA、Adapter 等参数高效微调 —— 70B 模型也能在 1 张 A100 上微调,工业界标配。
