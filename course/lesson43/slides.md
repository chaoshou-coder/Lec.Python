# Day43 · 部署

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day40 微调跑通、Day39 LoRA 适配器、Day42 评测
> 关键问题: 微调好的模型躺在服务器里,怎么让别人用?
> 一句话: 今天走完最后一步—— quantization → serve → API,让别人也能调用你的模型。

---

## 0. 引入(5 分钟)

- **破冰**(3 分钟): 打开 ollama.com 下载页,告诉学员"你花 7 天微调的模型,今天用 3 行命令变成在线服务"——起点到终点的仪式感。
- **赏玩 demo**(2 分钟): 教师在自己手机 App 里发一条请求,PC 屏幕上实时输出回答——展示"模型跑在本地,App 当客户端"。

---

## 1. 第一讲(15 分钟) —— 三种量化格式对比

### 知识点 1.1 GPTQ / AWQ / GGUF 怎么选

| 格式 | 运行环境 | 速度 | 量化精度 | 推荐场景 |
|---|---|---|---|---|
| **GPTQ** | GPU | 快 | 4/8bit | GPU 生产部署 |
| **AWQ** | GPU | 最快 | 4bit | GPU 高吞吐 |
| **GGUF** | CPU+GPU | 中 | 2~8bit | **本地 / 消费级 / Ollama** |

> **课程选 GGUF + Ollama**:消费级设备友好、一条命令跑起来,适合学习者。

### 知识点 1.2 GGUF 命名规则

```
qwen2.5-7b-instruct-q4_k_m.gguf
│          │    │         │
│          │    │         └─ 量化变体: Q4_K_M 是 4bit 量化
│          │    └─ Instruct 版
│          └─ 7B 参数
└─ 模型家族
```

> 常见量化等级:Q2(最小) / Q4_K_M(甜点) / Q8_0(接近无损) / F16(全精度)
> 显存紧张选 Q4_K_M,显存宽裕选 Q8_0。

### 知识点 1.3 为什么不直接用 HF 原始权重部署

HF 原始权重 = 几十个 shard 文件,推理引擎(GPTQ / vLLM / Ollama)为了速度要转成专有格式(融合 kernel、量化压缩)。**"训练用 HF 格式,部署要换格式"**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 看一张 GGUF 文件命名表,让学员判断每个文件能跑在多大显存(⭐⭐⭐,15 分钟)

> 巡场重点: 学员常把 K_M / K_S / Q8 混为一谈——K_M 中等显存、K_S 更低、Q8 精度高但占空间。

---

## 3. 第二讲(15 分钟) —— Ollama:本地推理一条龙

### 知识点 3.1 装 Ollama

```bash
# macOS / Linux 一行搞定
curl -fsSL https://ollama.ai/install.sh | sh
# 启动服务
ollama serve
```

### 关键词 3.2 拉模型 + 对话

```bash
# 拉一个官方模型
ollama pull qwen2.5:7b

# 命令行对话(一次性)
ollama run qwen2.5:7b "写一首关于春天的诗"

# 起 API 服务,默认端口 11434
# 通过 HTTP API 调用(同 ChatGPT 接口)
curl http://localhost:11434/api/generate -d '{
    "model":"qwen2.5:7b",
    "prompt":"写一首关于春天的诗",
    "stream":false
}'
```

> Ollama 帮你管:下载 / 量化 / 调度 / GPU/CPU 分配——本地部署首选。

### 知识点 3.3 自定义 Modelfile:让你微调的模型上线

```dockerfile
# Modelfile(放在模型同目录)
FROM ./qwen2-alpaca-final.gguf
TEMPLATE "{{ if .System }}<|system|>{{ .System }}{{ end }}{{ if .Prompt }}<|user|>{{ .Prompt }}{{ end }}<|assistant|>"
PARAMETER temperature 0.7
PARAMETER num_ctx 2048
```

```bash
# 用 Modelfile 创建一个自定义模型
ollama create my-assistant -f Modelfile
# 启动
ollama run my-assistant
```

> 🔴 教学红线(Modelfile 的 FROM 路径): FROM 后面是**相对路径**,写完 Modelfile 要在同目录才能 `ollama create`。

## 4. 当堂练 2(25 分钟)

- 练习 2: `in_class/practice02.py` —— 用 Python 调 Ollama HTTP API,写一个 5 行 chatbot(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常把 `stream: false` 忘设,收到的 response 是流式 chunk 拼接,直接 print 乱码。

---

## 5. 第三讲(15 分钟) —— vLLM 与 LoRA Adapter 合并

### 知识点 5.1 vLLM:PagedAttention 做高吞吐

vLLM 的核心创新 **PagedAttention** 把 KV Cache 像操作系统分页一样管理——显存利用率高,推理吞吐 2~4× vanillan transformers。

> 类比:传统推理 ="给每个进程连续分配内存",PagedAttention ="按需分页,显存不浪费"。vLLM 是生产级首选。

### 知识点 5.2 推理框架选型

| 框架 | 适合 | 上手难度 |
|---|---|---|
| **Ollama** | 本地 / 个人 | 一行命令 |
| **vLLM** | 生产高吞吐 | 需配 Python API |
| **TGI( Hugging Face)** | Docker 化生产 | 需配 Docker |

> 入门用 Ollama,生产部署再学 vLLM/TGI。

### 知识点 5.3 LoRA Adapter 合并回基座(收尾)

训练完的 LoRA 是独立小文件,推理时要挂载——多次推理下**合并回基座**减少计算开销。

```python
from peft import PeftModel

# 加载基座 + LoRA
base = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
model = PeftModel.from_pretrained(base, "./qwen2-alpaca-final")

# 合并 LoRA 回基座
merged = model.merge_and_unload()
# 导出成 HF 全量权重
merged.save_pretrained("./merged-full")
tok.save_pretrained("./merged-full")
```

> `merge_and_unload` 后模型变回标准 HF 格式,可转 GGUF 给 Ollama 用——**训练-部署闭环完成**。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 端到端合并 → 转 GGUF → Ollama serve → API 调用(⭐⭐⭐⭐⭐,整节)

> 巡场重点: `merge_and_unload` 后原 LoRA 适配器仍保留,如要恢复 adapter 需重新加载,不要覆盖。

## 7. 小项目(若本日有)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后填进 `teacher_notes.md`):
  1. Modelfile FROM 路径写错,ollama create 找不到文件
  2. LoRA 没合并直接挂多用户推理,延迟爆炸
  3. 部署完没测接口可用性,以为"启动就完事"
- **作业说明**: `homework/task01.py`(完成端到端部署,提交 API 调用截图)。

---

## 易错点

1. **GGUF 命名混淆**: Q4_K_M / Q8_0 / F16 各有显存/精度取舍;K_M ≠ K_S。
2. **Modelfile 路径**: FROM 后是相对路径,ollama create 要在同目录。
3. **忘设 stream:false**: Ollama HTTP API 默认流式,忘关返回 stream chunk。
4. **merge_and_unload 后覆盖 LoRA**: merge 是一次性操作,原 adapter 文件保留以备再训练。
5. **vLLM 没设 dtype**: 部署大模型没设 `dtype="half"` 显存翻倍——和训练同理。

## 延伸题

- **(vLLM 跑通, ⭐⭐⭐⭐)**: 安装 vLLM,启动一个 7B Qwen2.5 的服务,用 curl 调用 OpenAI 兼容接口。
- **(AWQ 部署, ⭐⭐⭐⭐⭐)**: 用 vLLM 的 AWQ 量化加载 7B 模型,对比和 Q4_K_M 的速度差异。
- **(GPU vs CPU 推理对比, ⭐⭐⭐)**: 用 Ollama 跑同一个问题,GPU 模式 vs CPU 模式计时,体会为什么高并发要 GPU。
