# Day 55 · Agent 框架

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 54 已实现 RAG 问答;Day 52 已封装 LLM 调用模块;了
>    解 function calling 概念(模型输出函数调用而非纯文字)
> 关键问题: 如何让 AI 不只是"问答机",而是能自主决定"查数据库、
    调搜索、执行代码"的多步任务执行者?本节构建有工具调用能力的 Agent

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— RAG 的流程是?为什么 system prompt 里
    必须写"不知道就说不知道"?目的:唤醒 RAG 全流程认知,为今天"LLM
    决定何时调用工具"埋伏笔。
- **赏玩 demo**(3 分钟): 问 Agent"今天北京的天气怎么样?帮我查文件里
    有没有关于它的报告" —— Agent 先调天气 API,再用 RAG 搜报告,最后
    把两部分答案整合。"它会自己做决策",引出 Agent。

---

## 1. 第一讲(20 分钟) —— Agent 概念与工具调用

### 知识点 1.1 什么是 Agent

Agent = LLM(决策引擎) + Tools(工具集) + Memory(记忆) + Planning(规划)

```
用户目标: "查一下张三的订单,然后告诉他明天天气"
      ↓
   [LLM 规划]
      ↓
   ① 调用 get_order("张三") → 得到订单
   ② 调用 get_weather("北京") → 得到天气
   ③ 整合结果,生成最终回复
```

> Agent 的核心:**LLM 不直接回答,而是决定下一步做什么**,循环直到任务
>    完成或达到最大迭代次数。

### 知识点 1.2 Function Calling:LLM 调用工具的标准协议

告诉 LLM 你能提供哪些工具,LLM 自己判断"该调哪个":

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名,如 北京"
                    },
                },
                "required": ["city"],
            },
        },
    }
]

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "北京今天天气如何?"}],
    tools=tools,
)

# LLM 不是直接回答,而是返回"我想调用 get_weather"
call = resp.choices[0].message.tool_calls[0]
print(call.function.name)      # get_weather
print(call.function.arguments) # '{"city": "北京"}'
```

> 🔴 教学红线(把 LLM 返回当纯文本): 很多学员只看 `message.content`,
>    但 function calling 时 content 是 None,真正内容在 `tool_calls`。

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 定义一个 `get_time(city)` 工具,
    用 function calling 让 LLM 决定调不调、传什么参数,手动执行工具
    并把结果再传回 LLM 得到最终回答(⭐⭐⭐,15 分钟)

> 巡场重点: 看学员是否处理了"LLM 不调用 tool 直接回答"的情况;
>    看是否做了"工具执行结果加入 messages"的二次调用。

---

## 3. 第二讲(25 分钟) —— LangChain Agent

### 知识点 3.1 LangChain 一(LCEL 链式调用

LCEL = LangChain Expression Language,用 `|` 把各步骤串起来:

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "用一句话解释:{concept}"
)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 链:prompt → llm → 字符串输出
chain = prompt | llm | StrOutputParser()
print(chain.invoke({"concept": "闭包"}))
```

> LCEL 的好处:每一段可单独测试、可复用,组合灵活。

### 知识点 3.2 Tool 装饰器:函数秒变工具

```python
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """获取指定城市的当前天气,输入城市中文名"""
    # 实际项目这里调第三方 API
    weather_db = {"北京": "晴 22℃", "上海": "多云 26℃"}
    return weather_db.get(city, f"未找到 {city} 天气")

tools = [get_weather]
```

> `@tool` 装饰器自动从函数签名 + docstring 生成 OpenAI 兼容的 tools
>    描述 —— 这就是 OpenAI function calling schema。

### 知识点 3.3 构建 ReAct Agent

ReAct = Reasoning + Acting,LLM 每步先想再行动:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个助手,可以使用工具帮助用户"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),  # Agent 的思考过程
])

llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# verbose=True 会打印推理轨迹,教学时必开!
result = executor.invoke(
    {"input": "北京和上海哪座城市今天更热?"}
)
print(result["output"])
```

输出轨迹(观察 LLM 的思考过程):
```
> 我要先查北京天气
调用 get_weather('北京') → 晴 22℃
> 再查上海
调用 get_weather('上海') → 多云 26℃
> 比较:上海 26℃ > 北京 22℃
回答:上海更热
```

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 实现两个工具:`search_web(query)`
    和 `calculator(expr)`,让 Agent 回答"圆周率前 5 位乘以 100 是多少"
    (需要先用计算器工具)(⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否开了 `verbose=True` 来观察推理轨迹;看
>    tool description 是否足够清晰(LLM 靠 description 判断用哪个)。

---

## 5. 第三讲(20 分钟) —— 工具集成与 Agent 进阶

### 知识点 5.1 常见工具类型

| 工具 | 用途 | 关键注意 |
|---|---|---|
| 搜索引擎 | 获取实时信息 | 限频率,cache 结果 |
| 数据库查询 | 内部数据 | 防 SQL 注入 |
| 代码执行 | 动态计算 | 必沙箱隔离 |
| API 调用 | 外部服务 | 加超时、重试 |
| RAG 检索 | 私有知识 | Day 54 已实现 |

```python
# 把 Day 54 的 RAG 作为 Agent 工具
@tool
def search_knowledge(question: str) -> str:
    """在内部知识库中搜索与问题相关的段落"""
    results = collection.query(
        query_texts=[question], n_results=3
    )
    return "\n".join(results["documents"][0])
```

### 知识点 5.2 Agent 必须设最大迭代次数

```python
executor = AgentExecutor(
    agent=agent, tools=tools,
    max_iterations=5,        # 最多工具调用 5 次
    early_stopping_method="generate",  # 超限后强制生成
    verbose=True,
)
```

> 🔴 教学红线(不设 max_iterations): 当工具总返回"错误",LLM 会不断
>    重试,陷入无限循环 —— 烧 token 且用户等不到结果。生产环境必设,
>    max_iterations 通常 5-10。

### 知识点 5.3 错误处理与兜底

```python
@tool
def safe_search(query: str) -> str:
    """带错误处理的搜索工具"""
    try:
        resp = requests.get(
            "https://api.search.com/q",
            params={"q": query},
            timeout=10,
        )
        return resp.json()["results"]
    except Exception as e:
        # 工具返回错误信息(不让 Agent 无限重试)
        return f"搜索失败({type(e).__name__}),请换个关键词"
```

> 工具里的异常**绝不能 raise**,必须返回字符串 —— 否则 Agent 框架会报
>    错退出,整个任务失败。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 构建一个"数据分析 Agent":提供
    `read_csv(path)` 和 `plot_chart(data_type)` 两个工具,让 Agent 根据
    用户指令选择合适的工具和参数(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员是否在工具里做了异常处理(return 而非 raise);看是否
>    设了 max_iterations。

---

## 7. 小项目(45 分钟) —— 有工具调用能力的 Agent

完成 `agent_app/`:

```
agent_app/
├── agent.py      # 构建 Agent + tools
├── tools/
│   ├── weather.py    # 调第三方天气 API
│   ├── knowledge.py  # 接入 Day 54 的 RAG
│   └── memory.py     # 会话历史
└── run.py        # CLI 交互
```

Agent 能力:
- 3 个工具以上
- 工具 description 明确,LLM 选择准确
- 流式输出推理轨迹
- 工具执行错误不影响整体

挑战题(选做):
- 加 persistence:用 Chroma/Redis 保存 session 历史,重启后仍能继续对话

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 没设 max_iterations,工具返回错误时 Agent 死循环,卡了 3 分钟
     Token 烧完
  2. tool 里 raise 异常而非 return 字符串,整个 Agent 崩溃退出
  3. tool 描述太模糊("做一件事"),LLM 搞不清什么时候该调,直接回答
- **作业说明**: 课后 `homework/task01.py` —— 为 Agent 加一个"计算器"
    工具,让 Agent 处理包含简单数学的问题(如"年利率 5%,10000 元 3
    年后本息多少?"),下节课复盘。

---

## 易错点

1. **不设 max_iterations**: 必设,通常 5-10。
2. **工具里 raise 异常**: Agent 框架无法处理,应用 `return` 错误信息。
3. **tool description 太简略**: LLM 靠它判断,写清楚"做什么 + 何时用"。
4. **verbose=False 教学阶段**: 推理轨迹是理解 Agent 行为的关键,
    教学必开。
5. **Function calling 时只看 content**: content 是 None,应在 `tool_calls`
    取值。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(CrewAI 多 Agent, ⭐⭐⭐⭐)**: 用 CrewAI 实现"研究员 + 写手"
    两个 Agent 协作,研究员调工具获取素材,写手生成报告。
- **(持久化记忆, ⭐⭐⭐)**: 用 LangChain 的 `ConversationBufferMemory`
    保存多轮对话,下一轮仍能引用上文信息。
- **(流式 Agent, ⭐⭐⭐⭐⭐)**: 用 `executor.astream_events` 实现
    逐字输出 + 工具调用过程实时展示,适合前端集成。
