# Day 53 · Embedding + 向量检索

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day 52 已封装 LLM 调用模块;已了解 token/上下文窗口概念;
>    具备线性代数基础(向量、矩阵)
> 关键问题: 如何让 AI 从"死记硬背"变成"随手查资料"?本节构建一个
    向量知识库,为 Day 54 RAG 全流程打基础

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 口答 —— OpenAI SDK 1.0+ 里 SSE 流式响应怎么
    开?messages 里 system 和 user 的顺序怎么放?目的:唤醒流式 + 消息
    结构认知,为今天"多文档拼接后传 LLM"埋伏笔。
- **赏玩 demo**(3 分钟): 展示 1000 篇文档,检索"Python 装饰器",
    0.1 秒返回最相关的 3 篇 —— "如何在几毫秒里从千篇中找到答案?"
    引出向量相似度 + 向量数据库。

---

## 1. 第一讲(20 分钟) —— 嵌入模型与向量

### 知识点 1.1 Embedding:把文字变成数字向量

LLM 把每个 token 变成一维向量(几百到几千维),embedding 模型把一句
话/一段文档变成一个固定长度的向量 —— 语义相近的句子,向量也相近。

```python
from openai import OpenAI

client = OpenAI()

# 单句嵌入
resp = client.embeddings.create(
    model="text-embedding-3-small",
    input="Python 装饰器是什么",
)
vector = resp.data[0].embedding
print(len(vector))    # 1536 ← 维度数
print(vector[:5])     # [0.0123, -0.0456, ...]
```

> 主流嵌入模型:
> - `text-embedding-3-small`(OpenAI): 1536 维,便宜,英文强
> - `text-embedding-3-large`(OpenAI): 3072 维,贵,更强
> - `BGE-m3`(BAAI 开源): 1024 维,中英双语都强,可本地跑

### 知识点 1.2 sentence-transformers:本地嵌入

不想每次调 API 花钱?用 HuggingFace 免费的本地模型:

```python
from sentence_transformers import SentenceTransformer

# 首次运行会自动下载(~90MB)
model = SentenceTransformer("BAAI/bge-small-zh-v1.5")

embeddings = model.encode(
    ["Python 装饰器",
     "闭包是嵌套函数",
     "今天天气真好"],
    normalize_embeddings=True,  # L2 归一化,方便算余弦相似度
)
print(embeddings.shape)  # (3, 512)
```

> 口诀:**有 GPU 用 GPU,没 CPU 也能跑,中文场景优先 BGE 系列**。

### 知识点 1.3 余弦相似度:计算"像不像"

两个向量夹角越小(余弦值越接近 1) → 语义越像。

```python
import numpy as np

def cosine_similarity(a, b):
    # a, b 都是一维 numpy 数组
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

v1 = model.encode(["Python 闭包"], normalize_embeddings=True)[0]
v2 = model.encode(["嵌套函数捕获外部变量"], normalize_embeddings=True)[0]
v3 = model.encode(["红烧肉怎么做"], normalize_embeddings=True)[0]

print(cosine_similarity(v1, v2))  # 0.82 ← 很像
print(cosine_similarity(v1, v3))  # 0.13 ← 不像
```

> 🔴 教学红线(不归一化): 不 normalize 就用点积比较 —— 长文本的向量范
>    数大,结果会偏向长文档。必须归一化后再比。

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 用 sentence-transformers 加载
    `bge-small-zh-v1.5`,对 5 个句子编码,计算相似度矩阵(5×5),
    热力图可视化(⭐⭐,15 分钟)

> 巡场重点: 看学员是否写了 `normalize_embeddings=True`;看是否用
>    `model.encode(list)` 而非循环调(批量编码快 10 倍)。

---

## 3. 第二讲(25 分钟) —— 向量数据库 Chroma

### 知识点 3.1 为什么需要向量数据库

暴力计算 N 个文档与查询的相似度是 O(N),十万个文档就慢。向量数据库
用 ANN(近似最近邻)算法,毫秒级检索。

| 工具 | 部署方式 | 适用场景 |
|---|---|---|
| Chroma | 本地/嵌入式 | 中小项目,开发首选 |
| FAISS | 本地(纯计算) | 只检索不存元数据时 |
| Milvus | 独立服务 | 生产,GPU 加速 |
| Qdrant | 独立服务 | 生产,支持过滤 |

> 本课程用 Chroma(本地存储)+ sentence-transformers(嵌入),无需联网
>    即可跑通整个流程。

### 知识点 3.2 Chroma 入门

```bash
pip install chromadb sentence-transformers
```

```python
import chromadb
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction,
)

# 客户端 + 集合(collection,类似数据库的表)
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="my_docs",
    embedding_function=SentenceTransformerEmbeddingFunction(
        model_name="BAAI/bge-small-zh-v1.5"
    ),
)
```

### 知识点 3.3 索引构建:添加文档

```python
documents = [
    "Python 装饰器是一种在不修改原函数前提下增强函数功能的语法糖",
    "闭包是嵌套函数捕获外部变量后形成的作用域",
    "多线程适合 IO 密集型任务,多进程适合 CPU 密集型任务",
    "Git rebase 可以把一条分支的提交移到另一条分支上",
    "Docker 容器是轻量级的进程隔离环境",
]

ids = ["doc_1", "doc_2", "doc_3", "doc_4", "doc_5"]

# 自动计算嵌入并索引
collection.add(documents=documents, ids=ids)
print(f"已索引 {collection.count()} 篇文档")
```

### 知识点 3.4 相似度检索

```python
results = collection.query(
    query_texts=["怎么写一个函数装饰器"],
    n_results=2,  # 返回最相关的 2 篇
)

for doc, score in zip(
    results["documents"][0], results["distances"][0]
):
    print(f"[距离={score:.3f}] {doc}")
# 输出:[距离=0.41] Python 装饰器是...语法糖
#      [距离=0.68] 闭包是嵌套函数...作用域
```

> Chroma 默认用距离(distance),不是相似度:距离越小越像。可以转换:
>    余弦距离 = 1 - 余弦相似度。

## 4. 当堂练 2(20 分钟)

- 练习 2: `in_class/practice02.py` —— 准备 10 篇课程笔记片段(txt),
    用 Chroma 建索引,输入一个查询,打印 top-3 相关文档片段及其分数
    (⭐⭐⭐,20 分钟)

> 巡场重点: 看学员是否做了文档切片(整本书直接 put 进去检索不精确);
>    看是否判断了 `ids` 唯一性。

---

## 5. 第三讲(20 分钟) —— FAISS + 元数据检索

### 知识点 5.1 FAISS:Meta 出品的高效检索库

FAISS 只管"算距离 + 建索引",不管存储 —— 适合对性能敏感的场景。

```python
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
docs = ["Python 装饰器...", "闭包...", "多线程..."]
vectors = model.encode(docs, normalize_embeddings=True)

# 建索引(精确检索,适合 < 10 万条)
dim = vectors.shape[1]
index = faiss.IndexFlatIP(dim)  # IP = 内积 = 余弦(已归一化)
index.add(vectors.astype(np.float32))

# 检索
query_vec = model.encode(
    ["装饰器怎么用"], normalize_embeddings=True
).astype(np.float32)

top_k = 3
scores, indices = index.search(query_vec.reshape(1, -1), top_k)
for i, score in zip(indices[0], scores[0]):
    print(f"[相似度={score:.3f}] {docs[i]}")
```

### 知识点 5.2 带元数据的检索:filter by 属性

Chroma 支持在检索时按元数据过滤:

```python
# 添加时带上元数据
collection.add(
    documents=["Python 装饰器..."],
    ids=["doc_1"],
    metadatas=[{"category": "python", "source": "官方教程"}],
)

# 检索时过滤:只找 python 类的文档
results = collection.query(
    query_texts=["函数相关概念"],
    n_results=3,
    where={"category": "python"},  # 元数据过滤条件
)
```

> 元数据过滤很常见:FAQ 系统按部门过滤、论文搜索按年份过滤。

## 6. 当堂练 3(25 分钟)

- 练习 3: `in_class/practice03.py` —— 用 FAISS 重建练习 2 的知识库,
    对比 Chroma 与 FAISS 结果差异;加上"source"元数据过滤,观察结果
    (⭐⭐⭐⭐,25 分钟)

> 巡场重点: 看学员是否对向量做了 `astype(np.float32)` —— FAISS 必须
>    是 float32;看查询向量是否做了 reshape(1, -1)。

---

## 7. 小项目(45 分钟) —— 向量知识库

构建一个命令行问答知识库 `vector_kb/`:

```
vector_kb/
├── ingest.py     # 把 docs/ 下的 txt 切片 → 嵌入 → 存入 Chroma
├── query.py      # 接收用户输入 → 检索 top-k → 打印结果
└── docs/         # 放几段 wiki / 课程笔记
```

`ingest.py` 关键流程:
1. 读取 txt 文件
2. 切片(每段 200 字,重叠 50 字)
3. 批量 encode(一次传 list)
4. 存入 Chroma(带 source + chunk_index 元数据)

`query.py` 关键流程:
1. 加载已有 collection
2. 循环接受 input → 检索 → 打印 top-3 + 距离

要求:
- 切片逻辑封装成 `split_text(text, chunk_size, overlap)`
- 检索后若最低相似度低于 0.5,提示"未找到相关文档"

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. FAISS 索引用 float64 计算 —— 必须转 float32
  2. 切片时没加 overlap,丢失跨块信息(如"函数定义"被切成"函"和
     "数定义")
  3. 查询向量没 normalize,相似度结果跟长度相关而非语义相关
- **作业说明**: 课后 `homework/task01.py` —— 把一个小 txt 文档(任意
    一本书的一段)用滑动窗口切片,建索引,下节课复盘。

---

## 易错点

1. **FAISS 只接受 float32**: 默认 numpy float64 会报错。
2. **Chroma 查询结果第一层是 list**: `results["documents"][0]`才是第一篇查询的结果,别忘 `[0]`。
3. **不 normalize 就用点积**: 会导致长文档得分虚高。
4. **不切片直接丢整本书**: 嵌入模型有 token 上限(通常 512),超长文本
    自动截断,检索精度暴跌。
5. **ids 重复**: `collection.add` 会静默覆盖,应先检查是否存在。

## 延伸题

> 以下素材为选做,教师可按需选用。

- **(HNSW 索引, ⭐⭐⭐)**: FAISS 里用 `IndexHNSWFlat` 替代
    `IndexFlatIP`,检索速度提升 10 倍(百万级必备)。
- **(增量更新, ⭐⭐⭐)**: Chroma 用 `upsert` 替代 `add`,允许对同一 id
    更新文档和嵌入,适合在线追加新文档。
- **(嵌入模型选型, ⭐⭐⭐⭐)**: 用 MTEB 排行榜(
    huggingface.co/spaces/mteb/leaderboard)对比 3 个中文嵌入模型,
    在相同文档库检索同一批 query,看 top-1 命中率。
