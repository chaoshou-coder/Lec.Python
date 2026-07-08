"""
[难度: ⭐⭐⭐]
[所属知识点: TF-IDF + 余弦相似度 (检索排序)]
[预计完成时间: 15 分钟]

题目: 智能问答候选检索排序
给定一个查询句和 3 句候选回复,请用 TfidfVectorizer
把文本转成向量,再用 cosine_similarity 计算
查询与每个候选的相似度,按得分从高到低排名。

说明: 先用 jieba 分词,空格拼接后再喂给向量化器。

示例:
    >>> query = "我想学 Python"
    >>> print排名结果
    候选1: 0.85
    候选2: 0.42
    候选3: 0.10
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def tokenize(text):
    """jieba 分词后用空格拼接"""
    return " ".join(jieba.lcut(text))


# 查询句与候选句
query = "我想学习 Python 编程"
candidates = [
    "Python 是一门非常适合初学者的编程语言",
    "今天天气很好适合出门散步",
    "推荐一本 Python 入门教程和学习路线",
]

# 第 1 步: 把所有句子分词
all_texts = [tokenize(query)] + [tokenize(c) for c in candidates]

# 第 2 步: 用 TfidfVectorizer 转向量
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_texts)

# 第 3 步: 计算查询与每个候选的余弦相似度
query_vec = tfidf_matrix[0]
cand_vecs = tfidf_matrix[1:]
sims = cosine_similarity(query_vec, cand_vecs).flatten()

# 第 4 步: 按相似度从高到低排序
ranking = np.argsort(-sims)
print("查询:", query)
print("排名:")
for rank, idx in enumerate(ranking, 1):
    print(f"  第{rank}名 (相似度 {sims[idx]:.4f}): {candidates[idx]}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 相似度最高的候选应包含"Python"
    top_idx = ranking[0]
    assert "Python" in candidates[top_idx]
    print(f"测试1通过: 最相关候选 = {candidates[top_idx]}")

    # 测试 2: 相似度数组长度为 3
    assert len(sims) == 3
    # 所有相似度在 [0, 1] 之间
    assert all(0 <= s <= 1 for s in sims)
    print("测试2通过: 相似度范围合法")

    # 测试 3: 排名顺序正确(降序)
    sorted_sims = [sims[i] for i in ranking]
    assert sorted_sims == sorted(sims, reverse=True)
    print("测试3通过: 排名为降序")
