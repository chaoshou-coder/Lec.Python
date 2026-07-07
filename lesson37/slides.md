# Day37 · LLM 生态 + HF 工具链

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Python / ML / DL / PyTorch / Transformer / Attention / HF pipeline
> 关键问题: 面对上百个开源模型,怎么选?HF 生态里那么多库各管什么?显存不够怎么办?
> 一句话: 今天是"地图日"——知道战场长什么样,才谈得上打仗。

---

## 0. 引入(5 分钟)

- **破冰**(3 分钟): 打开 Hugging Face Hub,让学员亲眼看到——当前已有 100 万+ 模型、20 万+ 数据集。提问:"你想让模型写代码 / 做客服 / 写中文小说,都能找到现成的,但选哪个?"
- **赏玩 demo**(2 分钟): 终端里 `huggingface-cli whoami` 登录态 + 随便搜一个模型页,展示 README、文件结构、社区讨论——让学员感受"开源不是下 zip,而是逛 GitHub 一样的生态"。

---

## 1. 第一讲(15 分钟) —— 开源模型谱系

### 知识点 1.1 五大家族速览:谁是谁?能干啥?

| 系列 | 出品方 | 开源许可 | 语言强项 | 典型参数 |
|---|---|---|---|---|
| LLaMA 3 | Meta | 商用友好(需申请) | 英/多语 | 8B / 70B |
| Qwen 2.5 | Apache | Apache-2.0(商用自由) | 中英双强 | 0.5B~72B |
| Mistral | Mistral AI | Apache-2.0 | 英/欧 | 7B / MoE-8x7B |
| Phi-3 | MIT | MIT(最宽松) | 英文 | 3.8B |
| Gemma 2 | Google | Gemma License | 英文 | 2B~27B |

> 选型口诀: **看许可 → 看语言 → 看参数量**。做中文项目优先 Qwen,做研究最爱 Phi(许可最松),追 LLaMA 需填表但生态最大。
>
> 🔴 教学红线(许可陷阱): 部分模型"开源权重但禁商用"(如 LLaMA 早期需申请)。用于公司项目前**必须**看 LICENSE,否则吃官司。课堂默认推荐 Apache-2.0 模型。

### 知识点 1.2 参数量:1 个参数 ≈ 2 字节(fp16)

参数量决定三件事:**能力 / 推理速度 / 显存**。

```
显存 ≈ 参数 × 字节数
7B fp16  ≈ 7×10⁹ × 2  ≈ 14 GB
7B 4bit  ≈ 7×10⁹ × 0.5 ≈ 3.5 GB
70B fp16 ≈ 140 GB(必须多张卡)
```

> 消费级显卡(RTX 3060 12GB / 4090 24GB)只能跑 7B 级别,且要量化。Colab T4(15GB)跑 Qwen2-0.5B / TinyLlama 1.1B 最稳。

### 知识点 1.3 量化版(GGUF)vs 全精度

- **全精度(fp16)**: 显存大、精度高 —— 训练 / 高精度推理
- **GGUF(GPT-Generated Unified Format)**: CPU 可跑、压缩比高 —— 本地部署(Ollama 后端)
- **GPTQ / AWQ**: GPU 量化的另一种路线,比 GGUF 快但需显卡

> 本日不展开量化实现(Day 43 讲),只建立"精度换显存"的直觉。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 用公式手算 Qwen2-7B 在 fp16 / 8bit / 4bit 下的显存(⭐⭐,5 分钟)
- 练习 2: `in_class/practice02.py` —— 浏览 HF Hub,找出 3 个"中文 + Apache-2.0 + ≤3B"的模型,填表(⭐⭐⭐,15 分钟)

> 巡场重点: 学员常把"参数量"和"显存"混为一谈——参数只是因素之一,还有优化器状态(训练时约 3× 模型大小)。强调 **推理 ≈ 模型、训练 ≈ 4×模型**。

---

## 3. 第二讲(15 分钟) —— Hugging Face 工具链全景

### 知识点 3.1 六大库各管什么?

```
🤗 生态
├── transformers   ← 模型加载 / tokenizer / forward / generate
├── datasets       ← 数据集加载 / map / filter / 流式加载
├── peft           ← 参数高效微调(LoRA / QLoRA / Adapter)
├── trl            ← 对齐训练(SFT / DPO / PPO)
├── accelerate     ← 多卡 / 混合精度 / 分布式封装
└── evaluate       │ 评测指标(accuracy / BLEU / ROUGE / 困惑度)
```

> 记忆口诀: **transformers 管模型,datasets 管数据,peft 微调,trl 对齐,accelerate 加速,evaluate 打分**。

### 知识点 3.2 `huggingface_hub`:下载模型的标准姿势

```python
from huggingface_hub import snapshot_download

# 自动下载整个模型仓库到本地缓存
path = snapshot_download(
    repo_id="Qwen/Qwen2-0.5B-Instruct",
    repo_type="model",
    local_dir="./models/qwen2-0.5b",  # 指定本地目录
    local_dir_use_symlinks=False,
)
print(f"模型已下载到: {path}")
```

> `snapshot_download` 比 `hf_hub_download` 更常用——它拉整个仓库(权重 + tokenizer + config),不会漏文件。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— `snapshot_download` 下载 Qwen2-0.5B 到本地,打印目录结构(⭐⭐⭐,15 分钟)
- 练习 4: `in_class/practice04.py` —— 用 `transformers.AutoModelForCausalLM.from_pretrained()` 加载刚下载的模型,跑一句推理(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 第一次跑 HuggingFace 会自动下几百 MB,网速慢的教室要**提前**让全班登录并下载好,否则 20 分钟全在等进度条。建议课前 `snapshot_download` 跑一遍。

---

## 5. 第三讲(15 分钟) —— 模型选型实战指南

### 知识点 5.1 场景 → 模型尺寸速查

| 场景 | 推荐尺寸 | 代表模型 | 显卡要求 |
|---|---|---|---|
| 学习 / Colab 跑通 | 0.5B~1.5B | TinyLlama / Qwen2-0.5B | 6GB(均可) |
| 个人项目 / 单机 | 7B | Qwen2.5-7B / Mistral-7B | 24GB(fp16) |
| 生产级推理 | 13B~70B | Qwen2.5-72B(量化) | A100×2 |
| 专家领域(代码/数学) | 专用 | DeepSeek-Coder / Qwen2-Math | 同尺寸 |

### 知识点 5.2 Instruct 版 vs Base 版

- **Base 版**: 只学"接下一个词",不会对话 —— 适合做研究 / 微调起点
- **Instruct 版 / Chat 版**: 经过 SFT + RLHF,开箱即用对话 —— 适合直接部署

> 🔴 教学红线(选错版本): 拿 Base 版直接写 Chatbot,效果极差。**开箱即用选 Instruct,微调研究选 Base**。

### 知识点 5.3 安装本日所需工具链

```bash
pip install transformers datasets peft trl accelerate evaluate \
    bitsandbytes huggingface_hub
```

> Colab 通常预装 transformers 和 datasets,但 peft / trl 每天都要重装——它们版本迭代快,pip 不会提示更新,导致 API 报错。养成"每次新 notebook 先 pip"的习惯。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 给定场景(中文客服 / 个人助手 / 代码补全),写选型报告(模型 + 版本 + 量化方案)(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常"选最大的"——要纠正:70B 量化在单卡能跑但推理慢,7B 微调后效果常常反超 70B 原始版。**微调 > 堆参数**。

## 7. 小项目(若本日有)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后填进 `teacher_notes.md`):
  1. 把 Base 版当 Chat 开箱用,对话一塌糊涂
  2. 忘记检查 LICENSE 就把模型接入商业项目
  3. 在 Colab 上直接跑 7B fp16,显存爆掉(OOM)
- **作业说明**: `homework/task01.py`(手算显存)、`homework/task02.py`(写选型报告),下节课前复盘。

---

## 易错点

1. **Base vs Instruct 不分**: Base 只续写不对话,开箱对话必选 Instruct。
2. **LICENSE 不看**: "开源"≠"商用自由",尤其 LLaMA 系列要看清条款。
3. **显存估算漏系数**: 推理 ≈ 模型大小;训练 ≈ 4×(模型 + 优化器 + 梯度)。
4. **snapshot_download 漏 local_dir**: 缓存模式下 `from_pretrained` 可能找不到文件。
5. **Colab 没提前下载**: 全班同时等几百 MB 进度条,课前要预跑一次。

## 延伸题

- **(Explore the Hub, ⭐⭐)**: 上 HF Hub 找出 3 个"Lora 适配器"模型,看它们都挂载在什么基座上——为 Day 39 埋伏笔。
- **(模型解剖, ⭐⭐⭐)**: 打开 Qwen2 的 `config.json`,找出 `hidden_size` / `num_attention_heads` / `num_hidden_layers`,和课堂讲的 Transformer 架构对应。
- **(License Detective, ⭐⭐⭐)**: 给 5 个热门模型的 LICENSE 分类(Apache / MIT / 自定义 / 禁商用),讨论"能不能接公司项目"。
