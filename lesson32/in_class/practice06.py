"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 词向量 + 余弦相似度检索 (Word2Vec 思想)]
[预计完成时间: 20 分钟]

题目: 简易词向量最近邻检索
自己构造 5 个 4 维"词向量"(模拟 Word2Vec),
实现 most_similar(query, word_vectors, topn=3)
函数,用余弦相似度返回与查询词最相似的 topn 个词。

说明: 余弦相似度 = (A·B) / (||A|| * ||B||),
计算时可用 numpy。

示例:
    >>> wv = {"国王": np.array([0.8, 0.7, 0.1, 0.0]), ...}
    >>> most_similar("国王", wv, topn=2)
    [('皇帝', 0.99), ('君主', 0.95)]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np


def cosine_sim(a, b):
    """计算两个向量的余弦相似度"""
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def most_similar(query, word_vectors, topn=3):
    """返回与 query 最相似的 topn 个词及相似度"""
    if query not in word_vectors:
        return []
    query_vec = word_vectors[query]
    scores = []
    for word, vec in word_vectors.items():
        if word == query:
            continue
        sim = cosine_sim(query_vec, vec)
        scores.append((word, float(sim)))
    # 按相似度降序排序
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:topn]


# 5 个 4 维词向量 (模拟语义: 君主/皇室/动物)
word_vectors = {
    "国王":   np.array([0.9, 0.8, 0.1, 0.0]),
    "皇帝":   np.array([0.85, 0.82, 0.1, 0.05]),
    "君主":   np.array([0.88, 0.75, 0.15, 0.0]),
    "老虎":   np.array([0.1, 0.05, 0.9, 0.8]),
    "猫咪":   np.array([0.0, 0.05, 0.85, 0.9]),
}

# 查询
result = most_similar("国王", word_vectors, topn=3)
print("查询: 国王")
print("最相似的 top3:")
for word, sim in result:
    print(f"  {word}: {sim:.4f}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: top1 应是"皇帝"或"君主"
    top_words = [w for w, s in result]
    assert "皇帝" in top_words or "君主" in top_words
    print(f"测试1通过: 前三名 = {top_words}")

    # 测试 2: 返回数量不超过 topn
    assert len(result) == 3
    print("测试2通过: 返回 3 个结果")

    # 测试 3: 相似度降序且都在 (0, 1]
    sims = [s for _, s in result]
    assert sims == sorted(sims, reverse=True)
    assert all(0 < s <= 1.0 for s in sims)
    print("测试3通过: 相似度降序且合法")

    # 测试 4: 查询不存在的词返回空列表
    empty = most_similar("不存在", word_vectors)
    assert empty == []
    print("测试4通过: 未知词返回 []")
