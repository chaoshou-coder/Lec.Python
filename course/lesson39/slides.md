# Day39 · LoRA / QLoRA 原理与配置

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day37 选型 + Day38 数据准备;反向传播、低秩矩阵、Transformer 注意力深入
> 关键问题: 7B 模型全量微调要 56GB+ 显存,单张消费卡怎么训?
> 一句话: 今天学"给大模型装小插件"——LoRA 用 1% 的参数达到 90% 的效果。

---

## 0. 引入(5 分钟)

- **破冰**(3 分钟): 在白板上写"全量微调 7B 模型"——写出梯度 + 优化器状态,让学员口算显存: 模型 14GB + 梯度 14GB + Adam 优化器 28GB ≈ **56GB**。提问:"你的显卡多大?"引出"必须降参数"。
- **赏玩 demo**(2 分钟): 展示一张"LoRA 适配器只有几 MB,挂到 7B 模型上"的示意图,直觉建立:"修车不用拆发动机,只换火花塞"。

---

## 1. 第一讲(15 分钟) —— 为什么需要参数高效微调

### 知识点 1.1 全量微调为什么贵(直觉 + 数字)

全量微调要更新所有参数,且 Adam 优化器要存**一阶矩 + 二阶矩**两份状态:

```
全量微调显存(7B fp16):
  模型权重:    7B × 2 bytes = 14 GB
  梯度:        14 GB
  优化器状态:  28 GB  ← Adam 的 m + v
  ─────────────────
  合计:       56 GB+   ← 即 A100 80GB 也要 gradient checkpointing
```

> 消费级卡(RTX 3060 12GB,Colab T4 15GB)连模型都放不下,别说训练。

### 知识点 1.2 三类参数高效微调(PEFT)

| 方法 | 思路 | 可训练参数 |
|---|---|---|
| Prompt Tuning | 只训练前缀软提示 | < 0.01% |
| Adapter | 在 Transformer 层间插小瓶颈层 | ~3% |
| **LoRA** | 给权重加低秩旁路 | **0.1%~1%** |

> LoRA 之所以胜出:**不引入推理延迟——训练完直接合并回基座,模型结构不变**。

### 知识点 1.3 LoRA 的数学直觉(类比,不推导)

大模型权重 W 的"任务相关变化" ΔW 通常**有效秩很低**:
```
原 forward:  y = Wx
LoRA:        y = Wx + ΔWx = Wx + BAx
             ↑ 冻结      ↑ 只训这两小矩阵
```
A (d×r), B (r×d), r << d,kernel 类比"小插头插在大主板的槽里"。

> 直觉: 大模型已经懂很多,新知识只需要"微调一个方向"。r 就是这个方向的自由度,8~64 就够了。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 给定 d=4096, r=16,手算 LoRA 参数占原权重比例(⭐⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— "类比练习":把 LoRA 类比成 3 个现实场景(⭐⭐,10 分钟,开放题)

> 巡场重点: 学员常以为 r 越大越好——要强调 r 过大失去参数效率,r 过小学不会,8~64 是甜点。

---

## 3. 第二讲(15 分钟) —— LoRA 四大超参

### 知识点 3.1 `LoraConfig` 四个关键参数

```python
from peft import LoraConfig

cfg = LoraConfig(
    r=16,                   # 秩:越小参数量越小,常用 8~64
    lora_alpha=32,          # 缩放系数:α/r 决定学习强度
    target_modules=[        # 套哪些层,最常套 q_proj/v_proj
        "q_proj",
        "v_proj",
    ],
    lora_dropout=0.05,      # 防过拟合,0~0.1
    bias="none",            # 偏置一般不训
    task_type="CAUSAL_LM",  # 任务类型:因果语言模型
)
```

### 知识点 3.2 各参数怎么定

- **r**: 8(小弟) / 16(甜点) / 64(小弟变大弟)
- **lora_alpha**: 常设 `2×r`,即缩放系数 = 2——学习率能被 α/r 重新缩放
- **target_modules**: 必含 `q_proj` 和 `v_proj`,可选 `k_proj/o_proj`/`gate_proj/up_proj`(更大覆盖)
- **lora_dropout**: 大数据集 0 / 小数据集 0.05~0.1

> 🔴 教学红线(target_modules 选错): 只套 `q_proj` 不套 `v_proj`——v_proj 承载"从输入提取什么",信息减半。新手**至少 q+v**,生产环境四路都套。

### 知识点 3.3 `get_peft_model()`把 LoRA 套到基座

```python
from peft import get_peft_model

model = get_peft_model(base_model, cfg)
model.print_trainable_parameters()
# trainable params: 3,932,160 || all params: 491,591,680 || 0.80%
```

> 看到"0.80%"就安心了——7B 模型只训 3.9M 参数,显存断崖式下降。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 加载 Qwen2-0.5B,套 LoRA,`print_trainable_parameters()`报告可训比例(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 对比 r=1 / r=8 / r=64 / r=256 的可训参数数(⭐⭐⭐⭐,10 分钟)

> 巡场重点: 学员漏 `task_type="CAUSAL_LM"`——套 Seq2Seq 模型时该写 `SEQ_2_SEQ_LM`,填错会报错。

---

## 5. 第三讲(15 分钟) —— QLoRA:让消费卡也能训

### 知识点 5.1 QLoRA = 4bit 量化基座 + LoRA 适配器

```
正常 LoRA:  基座(fp16, 14GB) + LoRA(几十 MB)  ← 仍吃显存
QLoRA:      基座(4bit NF4, 3.5GB) + LoRA(几十 MB) ← 单卡可训 7B
```

> 关键: LoRA 部分仍然**保持 fp16 精度**,只在基座用 NF4 量化——精度损失极小。

### 知识点 5.2 用 `BitsAndBytesConfig`加载 4bit 基座

```python
import torch
from transformers import BitsAndBytesConfig, AutoModelForCausalLM

bnb_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,  # 双量化:再省 0.4 bit/param
)
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2-0.5B-Instruct",
    quantization_config=bnb_cfg,
    device_map="auto",  # 自动分配 GPU/CPU
)
```

> `device_map="auto"` 是 accelerate 的暗号——显存不够时自动 offload 到 CPU,不会 OOM。

### 知识点 5.3 QLoRA 显存预算(7B 实测)

| 组件 | 显存 |
|---|---|
| 4bit 基座 | ~3.5 GB |
| LoRA 参数 + 梯度 + 优化器 | ~0.5 GB |
| 激活值(依赖 batch/seq) | ~2~5 GB |
| **合计** | **~6~9 GB** ← Colab T4 15GB 舒适 |

> 这就是为什么 QLoRA 是"民主化微调"神器:没有 A100 也能训 7B 模型。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 完整搭一个 QLoRA pipeline:BitsAndBytesConfig → PEFT LoraConfig → get_peft_model → 打印可训参数(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 学员常让 `from_pretrained` 先套 bnb 再套 LoRA,顺序反了会报错。必须先量化基座、再套 LoRA。

## 7. 小项目(若本日有)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后填进 `teacher_notes.md`):
  1. 漏 `q_proj` 或 `v_proj`,微调效果打折
  2. BitsAndBytesConfig 没写 `bnb_4bit_compute_dtype`,精度异常
  3. LoRA 套到未冻结的基座上(全参数可训),显存爆
- **作业说明**: `homework/task01.py`(QLoRA 跑通),下节课复盘。

---

## 易错点

1. **target-modules 不完整**: 至少套 `q_proj` + `v_proj`,否则信息损失严重。
2. **LoraConfig 忘 task_type**: 因果 LM 写 `CAUSAL_LM`,seq2seq 写 `SEQ_2_SEQ_LM`。
3. **先套 LoRA 再量化**: 顺序反了报错——先 BitsAndBytes 基座,再 get_peft_model。
4. **r 设太大**: r=256 接近全量微调,失去参数效率。
5. **基座没冻结**: `get_peft_model` 自动冻结基座,但手动 unfreeze 会让显存爆。

## 延伸题

- **(秩的秘密, ⭐⭐⭐)**: 打印训练前后的 `model.base_model.model.linear.lora_A`,看它奇异值分布——直觉理解"为什么说 LoRA 是低秩"。
- **(r 扫参实验, ⭐⭐⭐⭐)**: 固定其他超参,r ∈ {4, 16, 64, 256} 跑 500 步,看损失曲线对比。
- **(盲人调和分析, ⭐⭐⭐⭐⭐)**: 解读官方 QLoRA 论文 §A,列出"为什么 NF4 比 int4 好?"的三条实证理由。
