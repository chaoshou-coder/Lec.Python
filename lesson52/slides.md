# Day 52 · LLM API 集成 + Prompt 工程

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 51 已搭建 FastAPI 服务骨架;已了解 token/context/sampling
>    基础概念;已具备 Python 类型注解(Pydantic)基础
> 关键问题: 如何把 OpenAI / 通义 / 智谱 / 本地 Ollama 统一封装成一个
>    可切换、可重试、可流式的 LLM 调用模块?本节封装可复用模块

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— FastAPI 的 Pydantic 模型有什么作用?
    依赖注入 `@app.get` 里怎么用?目的:唤醒"请求体 + 校验"认知,为今
    天"封装 LLM 调用"埋伏笔。
- **赏玩 demo**(3 分钟): 现场跑一段代码,终端里字符逐个蹦出(流式
    输出),问:"怎么做才能让这种'打字机效果'跑起来?"引出
    `stream=True` + 逐 chunk 读取。

---

## 1. 第一讲(20 分钟) —— OpenAI SDK 调用

### 知识点 1.1 安装与初始化

```bash
pip install openai python-dotenv
```

```python
# llm_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    # base_url 可切换为本地或兼容服务(后文讲)
)
```

> 为什么用 `client` 对象? `openai` 库 >= 1.0 改为客户端模式,所有调用
>    走 `client.chat.completions.create(...)`,比旧版 `openai.ChatCompletion`
>    更规范、更利于切换兼容服务。

### 知识点 1.2 messages 结构:多轮对话的灵魂

`messages` 是角色 + 内容的数组,三种角色:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是一个Python助教,回答简洁"},
        {"role": "user", "content": "什么是闭包?"},
        {"role": "assistant", "content": "闭包是能访问外部变量的函数"},
        {"role": "user", "content": "举个例子"},
    ],
)
print(response.choices[0].message.content)
```

> 口诀:**system 设定人设,user 问,assistant 答,多轮按顺序排**。
>
> 🔴 教学红线(messages 顺序错乱): 把 assistant 消息放在 user 消息之前
>    语义错乱。对话必须严格按"时间线"排列,系统提示始终最前。

### 知识点 1.3 关键参数速查

| 参数 | 作用 | 推荐值(日常) |
|---|---|---|
| `model` | 模型名 | `"gpt-4o-mini"` |
| `temperature` | 随机性,0=固定,2=很随 | 0.7 |
| `max_tokens` | 最多输出 token 数 | 1024 |
| `top_p` | 核采样,与 temperature 二选 | 1.0 |
| `n` | 返回几个候选 | 1 |

> 新手只需关注 `temperature` 和 `max_tokens`,其他参数用默认即可。

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 创建 `client`,发一条单轮请求,
    `max_tokens=50`,打印回复和 `usage`(prompt_tokens、completion_tokens)
    (⭐⭐,15 分钟)

> 巡场重点: 看学员是否设置了 `max_tokens`(默认可能不返回 usage);看
>    是否检查了 `response.choices[0].message` 是否有内容。

---

## 3. 第二讲(25 分钟) —— 兼容 API 统一接口 + 错误处理

### 知识点 3.1 统一接口:多模型切换不改业务代码

通过 `base_url` 参数,同一套代码可切 OpenAI / 智谱 / 通义 / Ollama:

```python
PROVIDERS = {
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "gpt-4o-mini",
    },
    "zhipu": {
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "api_key": os.getenv("ZHIPU_API_KEY"),
        "model": "glm-4-flash",
    },
    "ollama": {
        # 本地服务,不需要真正的 key,占位即可
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "model": "llama3.1:8b",
    },
}

def get_client(name: str) -> tuple[OpenAI, str]:
    cfg = PROVIDERS[name]
    client = OpenAI(base_url=cfg["base_url"], api_key=cfg["api_key"])
    return client, cfg["model"]
```

> 价值:Prompt 研发阶段用便宜模型(flash/mini),上线时切高级模型(4o),
>    业务代码零改动 —— 只需改配置。

### 知识点 3.2 错误处理:重试 + 超时

网络抖动/限频(429)/服务错误(500)都需要兜底:

```python
from openai import APIConnectionError, RateLimitError, APITimeoutError
import time

def safe_chat(client, model, messages, retries=3):
    for i in range(retries):
        try:
            return client.chat.completions.create(
                model=model,
                messages=messages,
                timeout=30.0,  # 单次请求 30 秒超时
            )
        except RateLimitError:
            # 限频:等一段时间再试
            wait = 2 ** i * 5
            print(f"限频,等待 {wait}s 后重试...")
            time.sleep(wait)
        except (APIConnectionError, APITimeoutError) as e:
            if i == retries - 1:
                raise  # 最后一次还失败,抛出
            print(f"连接异常:{e},重试中...")
            time.sleep(2)
    return None
```

> 🔴 教学红线(无重试直接raise): 很多学员的代码没有 try/except,一旦
>    网络抖一下整个服务 500。生产环境至少加 3 次指数退避重试。

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 写一个 `chat(provider, prompt)`
    函数,通过参数切换 openai/ollama,打印哪个模型回复;故意传错模型名,
    捕获异常并模型不存在提示(⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否在 `get_client` 里做了参数校验(不在 PROVIDERS
>    里应抛 ValueError,而非让 OpenAI SDK 报模糊错误)。

---

## 5. 第三讲(25 分钟) —— 流式调用 + Prompt 工程

### 知识点 5.1 stream=True:逐字输出

```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "背一下《静夜思》"}],
    stream=True,  # 开启流式
)

# 逐 chunk 拼接输出
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
# flush=True 很重要 —— 否则缓冲区满了才一次性打出
```

> 🔴 教学红线(流式输出忘记处理): 如果没写 `if delta:` 可能打一堆
>    `None`;`flush=True` 不加会等到换行才显示,无法实现"打字机效果"。

### 知识点 5.2 few-shot:用例子教会模型

在 `messages` 里放几个「用户提问→标准回答」的样本:

```python
messages = [
    {"role": "system", "content": "判断评论情感:positive/negative"},
    # few-shot 样本
    {"role": "user", "content": "这个手机太棒了!"},
    {"role": "assistant", "content": "positive"},
    {"role": "user", "content": "差到想退货"},
    {"role": "assistant", "content": "negative"},
    # 真正的问题
    {"role": "user", "content": "还行吧,能用"},
]
```

> 经验:3-5 个样本效果最好,过多反而浪费 token、拖慢速度。

### 知识点 5.3 Chain-of-Thought:让模型"想一步写一步"

```
system: 解数学题时,请先写出推理步骤,再给出最终答案。

user: 一个水池有进水管和出水管...
→ assistant: 首先算进水速度...然后...所以答案是 3 小时
```

> CoT 把推理过程"外显",让复杂任务准确率提升 15%-30%,代价是多花
>    一些 token。适用于推理/计算/分类任务,不适用于简单翻译。

### 知识点 5.4 结构化输出(JSON mode)

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    response_format={"type": "json_object"},  # 强制返回 JSON
)
import json
result = json.loads(response.choices[0].message.content)
print(result["sentiment"])
```

> ⚠️ JSON mode 只保证输出是合法 JSON,**不保证结构** —— 结构靠 prompt
>    约束 + 结果校验。后续 Day 54 会结合 tool calling 做更严格校验。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 实现情感分析:few-shot 样本 + JSON
    mode 返回 `{"sentiment": "positive/negative", "reason": "..."}`,
    对 5 条评论跑一遍并打印(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员是否在 prompt 里明确写了"输出 JSON,包含 sentiment
>    和 reason 两个 key";看是否处理了 `json.loads` 解析失败。

---

## 7. 小项目(45 分钟) —— 封装 LLM 调用模块

封装成可复用的 `llm/` 包,供后续 RAG/Agent 模块直接调用:

```
llm/
├── __init__.py
├── client.py     # get_client(provider)
├── chat.py       # chat(messages) + stream_chat(messages)
└── prompt.py     # render_prompt(template, variables)
```

核心 API:

```python
from llm import chat, stream_chat

# 单轮
resp = chat([{"role": "user", "content": "你好"}], provider="openai")

# 流式
for chunk in stream_chat([{"role": "user", "content": "你好"}]):
    print(chunk, end="", flush=True)
```

要求:
- 切换 provider 无需改业务代码
- 异常自动重试 3 次
- 流式接口用 `yield`(generator)

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. `response_format={"type": "json_object"}` 但没 `import json` 去 parse,
     直接当字符串用,取 key 就报错
  2. stream=True 里没写 `if delta:, flush=True`,终端一片空白
  3. 调通 OpenAI 后切 Ollama 失败,因为 `api_key` 填了空的 —— Ollama
     可以传占位但不可 None
- **作业说明**: 课后 `homework/task01.py` —— 用 `llm/` 模块做一个多轮
    聊天 CLI(用户输入 q 退出),维护 messages 历史,下节课复盘。

---

## 易错点

1. **旧版 openai 库**: `pip install openai>=1.0`,否则客户端模式不生效。
2. **messages 结构**: user/assistant/system 三种角色,多轮必须按时间线。
3. **stream 需要 flush**: 否则缓冲区满了才输出,看不出逐字效果。
4. **重试用指数退避**: `wait = 2 ** i * base`,别每次等同样久。
5. **JSON mode ≠ 结构保证**: 合法 JSON 但 key 名可能错,用 Pydantic 再校验。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(回调日志, ⭐⭐)**: 在 `safe_chat` 加 `logging.info` 打印每次调
    用的 model/耗时/tokens —— 生产环境做成本核算必备。
- **(成本估算, ⭐⭐⭐)**: 按 OpenAI 官网定价(4o-mini 输入 $0.15/MTok),
    累加一天的 `prompt_tokens + completion_tokens`,估算月度账单。
- **(prompt 版本管理, ⭐⭐⭐⭐)**: 把 prompt 模板存到 `prompts/v1.txt`,
    改一次就建一个新版本(如 `v2.txt`),业务代码引用版本号而非文件
    内容 —— 方便回滚和 AB 测试。
