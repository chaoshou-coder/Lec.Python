# Day 54 · RAG 全流程

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 53 已构建向量知识库;Day 52 已封装 LLM 调用模块;了
>    解 context window 与 token 限制
> 关键问题: 如何让 LLM 在回答时"先翻书再答题",而不是凭记忆瞎编?
    本节从 0 构建一个文档问答系统

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— Chroma 的 `query` 返回的 `distances`
    是越小越像还是越大越像?为什么切片时要 overlap?目的:唤醒检索 +
    分块认知,为今天"检索 → 拼接 → 生成"埋伏笔。
- **赏玩 demo**(3 分钟): 现场对一个 PDF 问"第三章讲了哪些算法?",
    LLM 准确引用原文回答 —— "它没背这本书,但它能翻书回答你"。引
    出 RAG。

---

## 1. 第一讲(20 分钟) —— RAG 架构总览

### 知识点 1.1 什么是 RAG

RAG = **R**etrieval **A**ugmented **G**eneration(检索增强生成)

传统方式:把整本书塞进 prompt(不可能,context 有限,还贵)
RAG 方式:先检索相关片段,只把"最相关的几段"塞给 LLM

```
用户提问 → [检索] → 相关片段 → [拼接 prompt] → LLM → 回答
              ↑
        向量知识库
```

> RAG 解决三大痛点:
> 1. 省钱 —— 只传相关片段,不传全书
> 2. 省时 —— 不用重新训练
> 3. 改答案 —— 改文档重启服务即可,无需微调

### 知识点 1.2 完整流水线

```
1. 文档加载         ← 读 PDF / TXT / HTML
2. 文档分块         ← 固定 / 滑动窗口 / 语义
3. 嵌入(Embedding)  ← 每块变向量
4. 索引构建         ← 存入向量库
5. 检索(Query)      ← 用户问题 → 查 top-k 相关块
6. 重排序(可选)     ← 更精确地排顺序
7. 上下文拼接       ← 把 top-k 块拼进 prompt
8. LLM 生成         ← 带着"参考资料"回答
```

> 口诀:**文档切块 → 向量化 → 存库 → 查库 → 拼 prompt → 生成**。

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 用 RAG 流程图描述"用户问
    'Python 装饰器怎么用'时,系统内部经历了哪 8 步?"手绘或 ASCII
    图 + 文字说明(⭐⭐,15 分钟)

> 巡场重点: 看学员是否能独立画完 8 步,而不是简单背"检索+生成"。

---

## 3. 第二讲(25 分钟) —— 分块策略

### 知识点 3.1 为什么不能整本书丢进去

假设一本书 30 万字,切 token 约 45 万,token 成本是 GPT-4o-mini 的
$0.15/MTok = $0.0675 一次 —— 还不算回答。更要命的是:
1. context window 有限(通常 8k-128k 输入)
2. 长文本中间部分 LLM 容易"忘"(Lost in the Middle 论文结论)

### 知识点 3.2 三种分块策略

```python
# 策略 1: 固定大小分块(最简单)
def chunk_fixed(text, size=200, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap  # 步长 = size - overlap
    return chunks

# 策略 2: 滑动窗口(同上,按 token 而非字符更准确)
# 用 tiktoken 库: tokens = tiktoken.encoding_for_model("gpt-4o").encode(text)

# 策略 3: 语义分块(更高级,理解即可)
# 用 embedded模型检测相邻句子的相似度,相似度突降的地方切一刀
# LangChain 的 SemanticChunker 已实现,无需手写
```

| 策略 | 优点 | 缺点 |
|---|---|---|
| 固定大小 | 简单、快 | 可能切断句子 |
| 滑动窗口 | 保留跨块信息 | 有重复内容 |
| 语义分块 | 按意义切,更连贯 | 慢,依赖模型 |

> 🔴 教学红线(不 overlap): 不加 overlap 会导致"问题的一半在块 A,
    另一半在块 B",LLM 拼不出完整信息。建议 overlap = 20%-30%
    块大小。

### 知识点 3.3 分块效果对比

```
原文:"装饰器是一种特殊的函数,它接受一个函数作为参数,
     并返回一个新的函数,常用于日志、鉴权等场景。"

# 简单切(每 20 字,无 overlap)
["装饰器是一种特殊的函数,它接受一个", "函数作为参数,并返回一个新的
函数,常用于日志、鉴权等场景。"]
→ 第一块结尾断了,LLM 无法理解

# 滑动窗口(每 20 字,overlap=5)
["装饰器是一种特殊的函数,它接受一个", "它接受一个函数作为参数,并返
回一个新的函数,常用于日志、鉴权等场景。"]
→ 跨块信息保留
```

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 对一个长 txt(>5000 字)用两种
    策略分块,统计 chunk 数量、平均长度,对比结果(⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否写了"跨块信息保留"(overlap 后 chunk 内容有重
>    复);看是否在边界处打标记检查连续性。

---

## 5. 第三讲(25 分钟) —— 检索 + 拼接 + 生成

### 知识点 5.1 Top-K 检索:K 值怎么选

```python
results = collection.query(
    query_texts=[user_question],
    n_results=5,  # K=5: 通常 3-5 最佳
)
```

| K 值 | 效果 | 适用 |
|---|---|---|
| K=1 | 精准但风险高,唯一片段可能不相关 | 简单 FAQ |
| K=3 | 平衡,大多数场景首选 | 一般问答 |
| K=10 | 全但可能引入噪声,消耗更多 token | 研究型 |

> 实战经验:从 K=3 开始调;增加 K 后反而答不准,说明嵌入/分块有问题。

### 知识点 5.2 上下文拼接:构造 RAG prompt

```python
SYSTEM_PROMPT = """你是一个严谨的问答助手。必须基于下面提供的参考
文档回答问题,不要编造文档中找不到的信息。如果文档不足以回答,请说
"根据现有资料无法确定"。

参考文档:
{context}

现在请回答用户问题。"""

def build_prompt(question, chunks):
    # 给每个片段标号,方便 LLM 引用
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        context_parts.append(f"[文档{i}] {chunk}")
    context = "\n\n".join(context_parts)
    return SYSTEM_PROMPT.format(context=context)
```

### 知识点 5.3 完整 RAG 问答

```python
def rag_answer(question, collection, k=3):
    # 1. 检索
    results = collection.query(
        query_texts=[question], n_results=k
    )
    chunks = results["documents"][0]

    # 2. 拼接
    prompt = build_prompt(question, chunks)

    # 3. 调用 LLM
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question},
        ],
    )
    return resp.choices[0].message.content
```

> 🔴 教学红线(检索返回无关文档): 如果 prompt 里塞了不相关片段,LLM
>    会"偏题乱答"。分块太大/K 值太高/嵌入模型不匹配都会导致此问题。
>    对策:1) 缩小分块 2) 降低 K 3) 加元数据过滤。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 用练习 2 的分块结果建 Chroma
    索引,实现 `rag_answer`,故意提问一个"文档里没有"的问题,观察 LLM
    是否如实说"不知道"(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员是否在 system prompt 里有明确"不要编造"的指令;
>    看是否处理了"未知问题"场景。

---

## 7. 小项目(45 分钟) —— 文档问答系统

实现 `doc_qa/`:

```
doc_qa/
├── ingest.py     # txt/PDF → 切片 → 嵌入 → Chroma
├── qa.py         # 用户提问 → 检索 → 拼接 → 流式回答
└── data/         # 放待问答的资料(如课程 wiki)
```

`qa.py` 核心要求:
- 用 `stream_chat`(Day 52)逐字输出
- 每段末尾标注"参考来源: [文档x]"
- 低于相似度阈值的问题输出"未找到相关资料"

对比实验(选做):
- 同样问题,分别用 K=1 / K=3 / K=5 提问,看答案差异
- 同一文档,用 overlap=0 与 overlap=50 分别建库,检索同一问题

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 分块时不加 overlap,答案跨两块被截断,LLM 答非所问
  2. K 取 20 导致多个不相关片段混进 prompt,答案跑偏
  3. system prompt 没写"文档找不到就说不知道",LLM 自由发挥一通
- **作业说明**: 课后 `homework/task01.py` —— 对 data/ 下的文档建索引,
    写 5 个不同类型问题(有答案/没答案/边界问题),记录 LLM 回答质量,
    总结规律。

---

## 易错点

1. **分块不加 overlap**: 边界信息丢失,RAG 质量暴跌。
2. **K 值过大**: 噪声片段多,LLM 更容易"跑题"。
3. **不标注来源**: 用户无法验证 LLM 的引用是否真实。
4. **prompt 没约束"不知道就说不知道"**: LLM 幻觉严重,编造答案。
5. **一次性处理超大文件**: 建议先 100 篇切片 → 嵌入 → 存库,再下一批。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(重排序 rerank, ⭐⭐⭐)**: 检索出的 top-20 用 cross-encoder
    模型(如 `bge-reranker-v2-m3`)重排,取 top-3 进 prompt —— 准确度提升
    明显,但多一次模型调用。
- **(混合检索, ⭐⭐⭐⭐)**: 向量检索 + BM25 关键词检索各取 top-k,
    合并去重后给 LLM —— 同时利用语义和关键词匹配,适合含
    专业术语的场景。
- **(RAG 评估, ⭐⭐⭐⭐⭐)**: 用 ragas 库计算忠实度(faithfulness)
    和相关性(answer_relevancy),编写 10 条 case 跑评估,输出分数并
    分析低分原因。
