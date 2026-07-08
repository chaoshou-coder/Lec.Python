# Day40 · 训练实操

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day39 LoRA/QLoRA、Day38 数据准备、反向传播深入
> 关键问题: LoRA 配好了、数据准备好了,怎么跑起来?跑得稳?
> 一句话: 今天每个人在自己的卡上跑出第一个微调 checkpoint,是本课程的"成人礼"。

---

## 0. 引入(5 分钟)

- **破冰**(3 分钟): 在白板上列一张时间预算表:加载数据 2min + LoRA 加载 3min + 训练 15min + 保存 1min——告诉学员"今天 30 分钟能走完全流程"。
- **赏玩 demo**(2 分钟): 教师展示一张 W&B 截图——loss 曲线平滑下降,指标的视觉冲击让学员产生"我要跑这个"的冲动。

---

## 1. 第一讲(15 分钟) —— TrainingArguments 解剖

### 知识点 1.1 训练超参就像"健身房训练计划"

```python
from transformers import TrainingArguments

args = TrainingArguments(
    output_dir="./outputs/qwen2-alpaca",  # ckpt 保存目录
    num_train_epochs=3,                   # 过几遍数据
    per_device_train_batch_size=4,        # 单卡 batch
    gradient_accumulation_steps=4,        # 等效 batch = 4×4 = 16
    learning_rate=2e-4,                   # LoRA 学习率比全量大 10×
    warmup_ratio=0.05,                    # 头 5% 步线性升温
    lr_scheduler_type="cosine",           # 余弦退火
    logging_steps=10,                     # 每 10 步打一次日志
    save_strategy="epoch",                # 每个 epoch 存一次
    evaluation_strategy="epoch",          # 每个 epoch 评估
    fp16=True,                            # 混合精度,省一半显存
    report_to="none",                     # 不开 W&B 时写 none
)
```

> 🔴 教学红线(忘开 fp16): 不开 `fp16=True`,模型/梯度/激活全是 fp32——显存翻倍,7B 直接 OOM。Colab T4 / RTX 30 系列必须开。A100/H100 改用 `bf16=True`。

### 知识点 1.2 关键超参选型直觉

- **learning_rate**: 全量微调 1e-5; LoRA 1e-4~3e-4(LoRA 参数是旁路,可大学习率)
- **gradient_accumulation_steps**: 显存不够时用这个"虚拟放大 batch",不影响效果
- **warmup_ratio**: 防止训练初期大学习率把 LoRA 参数炸飞
- **per_device × accumulation = effective_batch**: 稳定训练最少 16

### 知识点 1.3 学习率为什么 LoRA 比全量大

全量微调时大学习率会破坏预训练学到的庞大知识;LoRA 是旁路,大学习率只会让"新知识学得快",不伤基座。

```
全量微调:  lr ~ 1e-5   ← 温柔地修旧书
LoRA:      lr ~ 2e-4   ← 大胆地插新章节
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 给定 target effective_batch=32,per_device=4,算 gradient_accumulation_steps(⭐⭐,5 分钟)
- 练习 2: `in_class/practice02.py` —— 手写 `TrainingArguments`,教师改一个错误让学员找 bug(⭐⭐⭐,15 分钟)

> 巡场重点: 学员常忘了 `report_to="none"`,打开笔记本突然让你登录 W&B——记着**没配 API key 就写 "none"**。

---

## 3. 第二讲(15 分钟) —— Trainer 与混合精度 / 梯度检查点

### 知识点 3.1 `Trainer`:用 5 行代码接管训练

```python
from transformers import Trainer

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    data_collator=collator,  # 批次 pad 的函数
)
trainer.train()              # 训练开始!
trainer.save_model("./final")# 保存 LoRA 适配器
```

> `Trainer` 内部帮你管:调度器 / 日志 / 保存 / 混合精度 / 分布式——HF 的招牌封装。

### 知识点 3.2 混合精度(fp16 / bf16)一句话

- 权重主副本保持 fp32,forward/backward 用 fp16——省一半显存,几乎不掉点
- **T4 / RTX 30**: `fp16=True`(不支持 bf16)
- **A100 / H100 / RTX 40**: `bf16=True`(更稳)

> 🔴 教学红线(fp16 vs bf16 选错): 在 T4 上开 `bf16=True` 会报错——确认自己显卡型号再填。

### 知识点 3.3 梯度检查点(Gradient Checkpointing)

用**时间换显存**:不存中间激活,backward 时重算一层。

```python
model.gradient_checkpointing_enable()  # 一行开
```

> 显存缩小 60%,速度慢 20%~30%——Colab 跑 7B 的必选项,跑 0.5B 可以不开。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 补全 Trainer 初始化代码,5 处空(⭐⭐⭐,15 分钟)

> 巡场重点: `data_collator` 学员常忘传——没有它批次长度不等直接报错。

---

## 5. 第三讲(15 分钟) —— 完整微调脚本

### 知识点 5.1 端到端微调和

下面脚本完整可跑(以 Qwen2-0.5B + Alpaca 中文 + QLoRA 为例),本课**要求学员在自己的机器上跑通**。

```python
import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    TrainingArguments, Trainer,
    DataCollatorForLanguageModeling,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model

# ── 1. 基座 + tokenizer ──
MODEL = "Qwen/Qwen2-0.5B-Instruct"
tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
tok.pad_token = tok.eos_token  # Qwen 没 pad,用 eos 代替

bnb_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)
base = AutoModelForCausalLM.from_pretrained(
    MODEL, quantization_config=bnb_cfg, device_map="auto",
)

# ── 2. LoRA ──
lora_cfg = LoraConfig(
    r=16, lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
)
model = get_peft_model(base, lora_cfg)

# ── 3. 数据 ──
ds = load_dataset("silk-road/alpaca-data-gpt4-chinese", split="train[:1000]")

def fmt(x):
    text = f"### Instruction:\n{x['instruction']}\n\n### Response:\n{x['output']}"
    return tok(text, truncation=True, max_length=512)
ds = ds.map(fmt, remove_columns=ds.column_names)

# ── 4. 训练 ──
args = TrainingArguments(
    output_dir="./qwen2-alpaca",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    warmup_ratio=0.05,
    lr_scheduler_type="cosine",
    logging_steps=10,
    save_strategy="epoch",
    fp16=True,
    report_to="none",
)
trainer = Trainer(
    model=model, args=args,
    train_dataset=ds,
    data_collator=DataCollatorForLanguageModeling(tok, mlm=False),
)
trainer.train()
model.save_pretrained("./qwen2-alpaca-final")
```

> 上面的脚本在 Colab T4 + Qwen2-0.5B + 1000 条数据 + 3 epoch 下,**约 15~30 分钟**跑完。可训练参数仅 ~4M。

### 知识点 5.2 训练监控:看得见的 loss

```python
# 方式 1: 看 Trainer 自带日志(简单)
# 方式 2: W&B / MLflow(生产级,后续展开)
# 方式 3: 训练后画曲线
import json, matplotlib.pyplot as plt
logs = []
with open("./qwen2-alpaca/trainer_state.json") as f:
    for line in f:
        logs.append(json.loads(line))
losses = [l["loss"] for l in logs if "loss" in l]
plt.plot(losses); plt.title("Loss Curve"); plt.show()
```

## 6. 当堂练 3(25 分钟)

- 练习 4: `in_class/practice04.py` —— **在自己机器上跑通完整脚本**,截图 loss 曲线(⭐⭐⭐⭐⭐,整节)

> 巡场重点: OOM 是头号杀手——按这个顺序排查:`per_device ↓` → `gradient_accumulation_steps ↑` → `gradient_checkpointing` → `max_length ↓`。**先保能跑,再求快**。

## 7. 小项目(若本日有)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后填进 `teacher_notes.md`):
  1. 忘开 `fp16=True`,直接 OOM
  2. `tok.pad_token` 忘设,批次报错
  3. 训练完 `save_pretrained` 没跑,白训
- **作业说明**: `homework/task01.py`(在自己的卡上跑一条完整数据,提交 loss 曲线截图)。

---

## 错点

1. **fp16 忘开**: T4 必开,否则显存翻倍直接 OOM。
2. **pad_token 漏设**: 部分模型(qwen / llama)没 pad_token,批次报 error。
3. **learning_rate 过大**: > 5e-4 容易 NaN,从 2e-4 起步。
4. **DataCollatorForLanguageModeling 漏传**: PAD 填充逻辑全挂它身上。
5. **save_model 没跑**: Trainer 完别忘 `model.save_pretrained`——白训一场。

## 延伸题

- **(Batch size 扫参, ⭐⭐⭐)**: 固定 lr,per_device ∈ {1,2,4,8},看收敛速度和显存占用变化。
- **(W&B 集成, ⭐⭐⭐⭐)**: 把 `report_to="none"` 改成 `report_to="wandb"`,跑通 loss / lr / gradient norm。
- **(多卡训练, ⭐⭐⭐⭐⭐)**: 读 accelerate 文档,在 `TrainingArguments` 中增加 multi-GPU 设置,对比单卡速度。
