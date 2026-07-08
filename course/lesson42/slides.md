# Day42 · 评测

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day40 完整微调跑通、语言模型 perplexity 直觉、Transformer 生成深入
> 关键问题: 微调完了,怎么知道好不好?比昨天好还是差?比别的模型强不强?
> 一句话: 今天学"打分"——同一个模型在不同指标下差距惊人,评测本身是个学科。

---

## 0. 引入(5 分钟)

- **破冰**(3 分钟): 在白板上画两列:模型 A 幽默有梗但错误多,模型 B 干巴巴但准确。提问:哪个"更好"?引出**"评测和你的目标强相关"**。
- **赏玩 demo**(2 分钟): 现场跑一条数据,同一模型在 BLEU=0.4 但人工评分 9 分——让学员感受"自动指标 ≠ 人工感受"。

---

## 1. 第一讲(15 分钟) —— 困惑度 Perplexity

### 知识点 1.1 一句话:模型对测试文本有多"意外"

困惑度(Perplexity, PPL)回答:**模型平均在几个词之间犹豫?** 

```
PPL = exp(平均交叉熵损失)
PPL = 20  → 每步相当于从 20 个等概率词里选
PPL = 1   → 完全确定(过拟合风险)
PPL = vocab_size → 完全随机
```

> PPL 越低越好,但太低 = 过拟合;太高 = 啥也不懂。**下游任务看 PPL 只看"趋势",不看绝对值**。

### 知识点 1.2 怎么算(直觉,不推导公式)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained("./qwen2-alpaca-final")
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")

text = "春眠不觉晓,处处闻啼鸟"
inputs = tok(text, return_tensors="pt")
with torch.no_grad():
    loss = model(**inputs, labels=inputs["input_ids"]).loss
ppl = torch.exp(loss).item()
print(f"PPL = {ppl:.2f}")
```

> 🔴 教学红线(用训练集算 PPL): 在训练集上 PPL 永远漂亮,**测试集才是真金白银**。必须在**未参与训练的数据**上算,否则是自欺欺人。

### 知识点 1.3 PPL 的局限

- 不衡量事实准确性("地球平的" 也可以 PPL 低)
- 不衡量简洁度(啰嗦回答 PPL 可能更低)
- 不同 tokenizer 下 PPL 不可比

> PPL 是**"语言模型多自信"**,不是**"答案多正确"** —— 永远要看下游任务指标。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 算 Qwen2-0.5B 微调前后的 PPL 对比(⭐⭐⭐,15 分钟)

> 巡场重点: 学员常把 `labels=inputs["input_ids"]` 忘传——没 labels 时模型 forward 不返回 loss,算不出 PPL。

---

## 3. 第二讲(15 分钟) —— BLEU / ROUGE 生成指标

### 知识点 3.1 BLEU:机器翻译的"精确率"代理

BLEU 看生成句和参考句的 **n-gram 重合度**:

```
参考: "the cat sat on the mat"
生成 1: "the cat sat on the mat"     → BLEU ≈ 1.0 (完美)
生成 2: "the dog sat on the mat"     → BLEU ≈ 0.7
生成 3: "yesterday sunny weather"    → BLEU ≈ 0.0
```

> Precision-based: 偏"**没错**"而不是"**都答了**"。适合机器翻译这种有参考答案的任务。

### 知识点 3.2 ROUGE:摘要的"召回率"代理

ROUGE 看参考句的 n-gram **被生成句覆盖了多少**:

```
参考: "春眠不觉晓,处处闻啼鸟,夜来风雨声"
生成: "春眠不觉晓,夜来风雨声"
→ ROUGE-1 召回 = 4 / 6 ≈ 0.67
```

> Recall-based: 偏"**答全了**"。适合摘要、信息抽取。

### 知识点 3.3 它们的共同局限

- 只看词形,不看语义("猫" ≠ "猫咪" 得 0 分)
- 没有标准答案的任务(开放式对话)几乎没用
- **自动指标 ≠ 人工感受**已是学界共识

> 用它们要看场景:**有参考答案的机器翻译/摘要可以用,开放式问答要看别的方法**。

## 4. 当堂练 2(25 分钟)

- 练习 2: `in_class/practice02.py` —— 用 `evaluate` 库算同一模型的 BLEU 和 ROUGE(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员常把"生成句"和"参考句"参数顺序填反——evaluate 库接口 `predictions / references` 是列表套列表,注意维度。

---

## 5. 第三讲(15 分钟) —— 基准评测:MLM / GSM8K / HELLASWAG

### 知识点 5.1 公共基准是"行业考卷"

| 基准 | 测什么 | 典型题 |
|---|---|---|
| **MMLU** | 57 学科知识 | "光合作用中释放的气体是?" |
| **GSM8K** | 数学推理 | "小明有 5 个苹果,给了小红 2 个..." |
| **HELLASWAG** | 常识推理 | "人打开冰箱后最可能做什么?" |

> 这些基准让"我这个模型行不行"有公开比较基准,但**不要过拟合基准**——基准高了不等于实际好用。

### 知识点 5.2 用 `evaluate` 库跑基准

```python
import evaluate

# 加载 BLEU 指标对象
bleu = evaluate.load("bleu")
result = bleu.compute(
    predictions=["the cat sat on the mat"],
    references=[["the cat sat on the mat"]],  # 注意:双层列表
)
print(f"BLEU = {result['bleu']:.3f}")
```

> 🔴 教学红线(references 维度): references 必须是 `list[list[str]]`,外层是样本、内层是多个参考,漏双层直接报 shape error。

### 知识点 5.3 人工评测:Chatbot Arena

人类盲评:A vs B 两个匿名回答,评委选更好的——最终以 **ELO 分数**排名。

> 公认真金:**** BLEU 漂亮但 Arena 输 → 承认 Arena 输;BLEU 差但 Arena 赢 → 承认 BLEU 差**。模型的终极目标是让人满意,不是让指标漂亮。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 跑 MMLU 的 10 道题子集(用 `evaluate` + 小样本提示)(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 学员直接 zero-shot 跑准确率极低——提示添加"请从 A/B/C/D 中选择更易得分"。**评测也讲究 prompt 工程**。

## 7. 小项目(若本日有)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后填进 `teacher_notes.md`):
  1. 用训练集算 PPL,自欺欺人
  2. BLEU/ROUGE references 维度搞错直接报错
  3. 只用自动指标,标出来漂亮但实际答得烂
- **作业说明**: `homework/task01.py`(跑一个完整评测套件,对比微调前后),下节课复盘。

---

## 易错点

1. **训练集算 PPL**: 永远要隔离测试集,否则指标漂亮但假的。
2. **references 不是 list[str]**: 双层列表 `list[list[str]]`,shape 不对直接报错。
3. **PPL 绝对值跨 tokenizer 比**: 不同 tokenizer 下 PPL 没有可比性。
4. **BLEU 用在开放生成**: 适合有参考答案的翻译/摘要,不适合对话。
5. **只看自动指标忽略人工**: 自动指标不等于人的感受;Arena 式盲评更接近真相。

## 延伸题

- **(评测跑起来, ⭐⭐⭐)**: 用 `lm-eval-harness` 跑 MMLU 的 5 题子集,体会"跑基准"的整个流程。
- **(相关性分析, ⭐⭐⭐⭐)**: 在 100 条数据上同时算 BLEU 和收集 3 个人工评分,算 Spearman 相关系数——量化"自动指标到底多可信"。
- **(基准污染辩论, ⭐⭐⭐⭐⭐)**: 讨论"模型看过 MMLU 题,还能测吗"? 列出 2024 年主流解法(held-out / anti-contamination)。
