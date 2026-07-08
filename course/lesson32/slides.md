# Day 32 · 文本预处理 + 表示

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: 已掌握 Python、ML 基础、PyTorch 张量操作、梯度下降与反向传播
> 关键问题: 自然语言文本是非结构化数据,怎么把它转成机器学习模型能"吃"的数值向量?本节覆盖"清洗 → 分词 → 向量化"全流程,并引出词嵌入的直觉,为后续 Transformer 铺垫
>
> 代码环境: `pip install scikit-learn numpy`

---

## 0. 引入(5 分钟)

- **提问**(2 分钟): "一张图片是像素矩阵,一段音频是波形数组,一段中文 —— `我喜欢吃火锅` —— 怎么让计算机'看见'它?" 引出"文本表示"问题的独特性:离散、变长、有顺序、有语义冲突(多义词)。
- **赏玩 demo**(3 分钟): 现场跑一行 `TfidfVectorizer().fit_transform(["猫 坐在垫子上", "狗 在院子里跑"])` 展示稀疏矩阵 —— "看,句子变成了表!" 一句话吊胃口:**同样的流程,换模型就是 NLP**。

---

## 1. 第一讲(45 分钟) —— 文本清洗与分词

### 知识点 1.1 文本清洗:先把"垃圾"扔掉

原始文本充满噪声(标点、数字、HTML 标签、表情符号),清洗 = 让模型只看到"有用的字符"。

```python
import re

raw = "  震惊!!! 2024 年 AI 已经能写代码了~~~点击查看 http://xxx.com  "

# 1. 去 HTML 标签(若有)
clean = re.sub(r"<[^>]+>", "", raw)
# 2. 去 URL
clean = re.sub(r"http\S+", "", clean)
# 3. 去标点/特殊字符,保留中文/字母/数字
clean = re.sub(r"[^\w\s]", "", clean)
# 4. 去多余空格
clean = re.sub(r"\s+", " ", clean).strip()

print(clean)  # 震惊 2024 年 AI 已经能写代码了 点击查看
```

> 🔴 教学红线(清洗不是越干净越好): 情感分析中 `"!!!"` 是情绪强度信号,全删掉反而丢信息。清洗取决于任务 —— 垃圾邮件分类保留数字和反常符号,翻译任务保留标点(问号、句号决定句子边界)。

### 知识点 1.2 分词(tokenization):把句子切成分片

tokenization = 把一段文本拆成**标记(token)** 序列,是 NLP 的"第一道关卡"。三种粒度:

```python
sentence = "自然语言处理 很 有趣"

# 方法 1:按空格切(英文为主,中文不适用)
tokens_space = sentence.split()
print(tokens_space)  # ['自然语言处理', '很', '有趣']

# 方法 2:按字符切(中文常用,但 token 数爆炸)
tokens_char = list(sentence.replace(" ", ""))
print(tokens_char)   # ['自','然','语','言','处','理','很','有','趣']

# 方法 3:子词(tokenizer 工具,工业标准)
#   BPE (Byte Pair Encoding):高频合并字符对,最终形成"词表"
#   例: "playing" → ["play", "ing"],"lowest" → ["low", "est"]
#   优点:不会出现 OOV(未登录词),存储空间小
```

> 类比: 子词就像"乐高积木"。字母表=所有可买砖块(26 个),子词=常用组合砖块(play/un/ing 都是现成小块),整词=大件模型。子词在"词表大小"与"语义粒度"之间找平衡。

> 🔴 教学红线(中文不分空格): 中文"今天天气好"没有空格,按字符切导致 5 个 token 且机器不懂"今天"是一个词。现代预训练模型一律用子词 tokenizer(BERT 用 WordPiece,GPT 用 BPE),本节先理解"分词是什么"即可,实际代码调 Hugging Face tokenizer。

### 知识点 1.3 去停用词:去掉"废话词"

停用词(stop words) = 在文本中出现频率极高但携带信息极少的词("的"、"了"、"是"、"在"、"and"、"the"、"is")。

```python
# 中文停用词表示例(实际使用 jieba 或 nltk 的标准词表)
stop_words = {"的", "了", "是", "在", "和", "也", "都", "就"}

tokens = ["我", "喜欢", "深度", "学习", "的", "应用"]
filtered = [t for t in tokens if t not in stop_words]
print(filtered)  # ['我', '喜欢', '深度', '学习', '应用']
```

> 注意: 停用词表因任务而异 —— 情感分析中"不"不能删("不好"≠"好"),机器翻译中每个虚词都影响语法。本节只做启发,Day 36 Hugging Face 实战时再也不会手动去停用词了。

## 2. 当堂练 1(25 分钟)

- 练习 1: `in_class/practice01.py` —— 用正则清洗一段微博文本(去表情、去话题标签、去@用户),输出干净语料(⭐⭐,15 分钟)
- 练习 2: `in_class/practice02.py` —— 手写"空格分词 + 去停用词"处理英文影评,统计最高频 10 词(⭐⭐⭐,20 分钟)

> 巡场重点: 学员常在 re.sub 里正则写错(忘记 `r` 前缀、转义字符),提示:`r"http\S+"` 中 `\S` 是非空白字符;注意 `replace(" ", "")` 和 `strip()` 的区别。

---

## 3. 第二讲(30 分钟) —— 文本表示:BoW 与 TF-IDF

### 知识点 3.1 词袋模型( Bag of Words,BoW ):数一数每个词出现了几次

BoW 把整个语料库看成一个"大袋子",每篇文档 = 袋子里的词频统计,**完全忽略顺序**。

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "猫 喜欢 吃 鱼",
    "狗 喜欢 吃 骨头",
    "猫 和 狗 是 朋友",
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# 查看词表
print(vectorizer.get_feature_names_out())
# ['朋友' '和' '喜欢' '吃' '狗' '猫' '是' '骨头' '鱼']

# 查看矩阵
print(X.toarray())
# [[0 0 1 1 0 1 0 0 1]  ← 猫、喜欢、吃、鱼
#  [0 0 1 1 1 0 0 1 0]  ← 狗、喜欢、吃、骨头
#  [1 1 0 0 1 1 1 0 0]] ← 朋友、和、狗、猫、是
```

> 类比: BoW 就像"菜谱不看步骤,只看用了哪些食材"。两道菜都用盐和鸡蛋,BoW 向量就很像 —— 这就是 BoW 的盲点:**语序丢失**("猫吃鱼"和"鱼吃猫"一模一样)。

### 知识点 3.2 TF-IDF:让"罕见词"更有价值

BoW 的问题: "的"在每个文档都出现,词频高但没意义。TF-IDF 通过**逆文档频率**惩罚高频常见词。

```text
TF(词频):  某个词在文档中出现的次数 / 文档总词数
IDF(逆文档频率): log(文档总数 / 包含该词的文档数 + 1)
TF-IDF  = TF × IDF
```

- "鱼"只在文档 1 出现 → IDF 高 → 关键词
- "吃"在文档 1、2 都出现 → IDF 低 → 常见词
- "朋友"只在一篇出现 → IDF 高 → 关键词

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "猫 喜欢 吃 鱼",
    "狗 喜欢 吃 骨头",
    "猫 和 狗 是 朋友",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
# ['朋友' '和' '喜欢' '吃' '狗' '猫' '是' '骨头' '鱼']

# 查看 TF-IDF 值(已经是浮点数,范围 0~1)
import numpy as np
np.set_printoptions(precision=3)
print(X.toarray())
# [[0.    0.    0.423 0.423 0.    0.554 0.    0.    0.554] ← "猫""鱼"权重高
#  [0.    0.    0.423 0.423 0.554 0.    0.    0.554 0.   ]
#  [0.5   0.5   0.    0.    0.355 0.355 0.5   0.    0.   ]]
```

> 直观感受: 文档 1 的向量中,"鱼"(0.554)和"猫"(0.554)权重最高 —— 这两个词确实最能代表"这篇文档在讲什么"。

> 🔴 教学红线(稀疏矩阵): BoW/TF-IDF 产生的矩阵**极度稀疏**(绝大多数元素是 0)。词表 10 万、文档 1 万,矩阵大小 10^9,但非零元素不到 0.1%。这就是"维度灾难",也是后续词嵌入要解决的问题 —— 把 10 万维稀疏向量压成 300 维稠密向量。

### 知识点 3.3 文本分类实战:用 TF-IDF + 朴素贝叶斯做情感分析

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 训练数据(实际用成千上万条)
texts = [
    "这部电影太棒了,剧情很精彩",
    "演员演技很烂,浪费时间",
    "音乐和画面都很美",
    "太差了,都看不下去",
    "强烈推荐,值得一看",
    "真的很失望,不值票价",
]
labels = [1, 0, 1, 0, 1, 0]  # 1=正面,0=负面

# 构 pipeline: TF-IDF + 分类器
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(texts, labels)

# 预测
test = ["画面很美,推荐观看"]
print(model.predict(test))  # [1] —— 正面
```

> 为什么后续要学神经网络? TF-IDF 丢掉了词序和语义("这部电影 vs 不推荐这部电影" 共享高频词,BoW 向量几乎一样,但意思相反)。这是引入词嵌入和 Transformer 的核心动机。

## 4. 当堂练 2(30 分钟)

- 练习 3: `in_class/practice03.py` —— 对 IMDB 影评数据做 TF-IDF 向量化,用逻辑回归跑基线,输出前 10 个高权重正向词和负向词(⭐⭐⭐,25 分钟)
- 练习 4: `in_class/practice04.py` —— 用手写的"向量余弦相似度"找两条影评最相近,理解"TF-IDF 能衡量语义距离的局限性"(⭐⭐⭐⭐,25 分钟)

> 巡场重点: 练习 4 常有人直接 `cosine_similarity(X[0], X[1])`,但忘记 scipy 稀疏矩阵要 `.toarray()`;提示: TF-IDF 返回的是 scipy 稀疏矩阵,`cosine_similarity` 函数直接吃稀疏矩阵,**不需要转 dense**。

---

## 5. 第三讲(25 分钟) —— 词嵌入直觉:Word2Vec / GloVe

### 知识点 5.1 为什么需要词嵌入:BoW 的三个致命弱点

1. **维度灾难**: 词表 10 万 → 每条文档是 10 万维稀疏向量
2. **语义缺失**: "猫"和"喵星人"在 BoW 中是两个完全不同的维度,模型不知道它们是近义词
3. **OOV 无解**: BoW 词表里没有 "ChatGPT" 这个词,直接当 0 处理

词嵌入(word embedding) = 把每个词映射到**固定长度的稠密向量**(通常 50~300 维),意义相近的词向量夹角小。

### 知识点 5.2 Word2Vec 直觉:用邻居猜你 / 用你猜邻居

Word2Vec 两种变体:
- **Skip-gram**: 给定中心词,预测周围词(小数据集效果好)
- **CBOW (Continuous Bag of Words)**: 给定周围词,预测中心词(大数据集速度快)

> 类比: 你做"完形填空"时,看到上下文猜中间缺的词,这个直觉就是 CBOW。模型在"猜词"的过程中被迫学会了语义 —— "猫"和"喵"常出现在相似的上下文,所以它们的向量也相似。

### 知识点 5.3 GloVe:在全局共现统计上做文章

GloVe(Global Vectors)和 Word2Vec 目标一样,但方法论不同:
- Word2Vec: 在**局部窗口**内预测(在线学习)
- GloVe: 先统计整个语料库的**词-词共现矩阵**,再做矩阵分解

> 类比: Word2Vec 像"边读边学"(每天读一篇新闻更新理解),GloVe 像"读完整个图书馆再做总结"(先统计所有词共现再压缩)。实际效果相近,GloVe 在中小语料库上通常更稳定。

### 知识点 5.4 向量空间中的语义关系:国王 - 男人 + 女人 = 女王

词嵌入最著名的性质:

```text
vector("国王") - vector("男人") + vector("女人") ≈ vector("女王")
vector("巴黎") - vector("法国") + vector("日本") ≈ vector("东京")
```

```python
import numpy as np

# 假设我们已经有了训练好的词向量(实际用 gensim 加载预训练模型)
# 演示如何计算余弦相似度
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 伪代码:king - man + woman ≈ queen
# result = king_vec - man_vec + woman_vec
# closest = max(vocab, key=lambda w: cosine_sim(result, word_vec[w]))
# print(closest)  # "女王"
```

> 类比: 词向量就像"一组坐标","性别"是其中一个轴,"身份"是另一个轴。沿着"性别轴"平移,就能从"国王"走到"女王" —— 这揭示了神经网络能**线性解耦语义属性**。

> 🔴 教学红线(词嵌入是静态的): "苹果"在 Word2Vec 中是唯一向量,但"我买了一部苹果手机"和"苹果营养丰富"中,意思完全不同。**静态词嵌入无法处理多义词** —— 这是 ELMo、BERT 等动态词嵌入要解决的问题(Day 35 展开)。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 用 gensim 加载预训练 Word2Vec 模型,做"找近义词"和"类比推理"小工具(⭐⭐⭐,20 分钟)

> 巡场重点: 预训练模型文件通常 100MB+,学员易忘记下载。提示: 用 `gensim.downloader` API 在线加载(首次慢,后续用缓存);检查模型里有没有中文词向量,没有时类比推理题做不了 —— 这是 Day 35 转到 Hugging Face BERT 的部分动机(多语言支持完善)。

## 7. 小项目(45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 正则清洗时 `[^\w\s]` 没考虑中文,把汉字也删掉了(应改为 `[^\w\s一-鿿]` 或保留中文范围)
  2. BoW/TF-IDF 的稀疏矩阵转 dense `.toarray()` 导致内存溢出(10 万维 × 6 万条 ≈ 48GB)
  3. Word2Vec 词性类比题中忘了减去均值来降低高频词效应,结果跑偏
- **作业说明**: 课后 `homework/task01.py`(用 TF-IDF + SVM 跑完整情感分析)、`homework/task02.py`(手动实现 Skip-gram 简化版),下节课前 10 分钟复盘

---

## 易错点

1. **BoW 忽略顺序**: "猫吃鱼"和"鱼吃猫"的 BoW 向量完全相同,这是引入 RNN/Transformer 的根本动机。
2. **TF-IDF 是 task-dependent**: 情感分析中"不"不应被当作停用词删掉;机器翻译保留所有虚词。
3. **Word2Vec 是静态嵌入**: 同一个词在不同上下文中向量不变,无法处理多义词("苹果"在 iPhone vs 水果中向量相同)。
4. **稀疏矩阵别 `.toarray()`**: 除非矩阵很小,否则直接 `X.toarray()` 会爆内存,sklearn 的 classifier 都能直接吃稀疏矩阵。
5. **gensim 预训练模型**默认不自带中文词向量,中文 NLP 实际项目直接跳 BERT(Hugging Face)。

## 延伸题

> 以下素材来自外部课程(references.md),教师可按需选用或替换当堂练。

- **(Bag of Words Lab, 斯坦福 CS224N 简化版, ⭐⭐)**: 给 20 条影评人工统计 TF-IDF,输出"最能区分正负面的 5 个词" —— 巩固 TF-IDF 意义。
- **(Word2Vec Visualization, Stanford CS224N, ⭐⭐⭐)**: 用 t-SNE 把 1000 个词的 300 维向量降到 2 维画图,直观看到"动物聚一堆、国家聚一堆" —— 感受词嵌入的空间结构。
- **(Bias in Word Embeddings, MIT 6.S191, ⭐⭐⭐⭐)**: 跑 "男人 - 女人 + 程序员 = ?" 看输出是否偏向性别刻板印象 —— 引出 NLP 公平性问题(可作为 Day 36 课外延讨论)。
