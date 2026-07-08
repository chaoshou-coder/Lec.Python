"""
[难度: ⭐⭐]
[所属知识点: 词袋模型 BoW (CountVectorizer)]
[预计完成时间: 10 分钟]

题目: 把中文短句转为词袋矩阵
给定 3 句中文短句,请先用 jieba 把每句切成
空格分隔的词串,再用 sklearn 的 CountVectorizer
转为词袋矩阵,并打印词汇表和矩阵。

示例:
    >>> s = "猫 喜欢 鱼"
    >>> # CountVectorizer 后 vocabulary_ 包含 猫/喜欢/鱼
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import jieba
from sklearn.feature_extraction.text import CountVectorizer


# 原始 3 句中文
sentences = [
    "猫喜欢吃鱼",
    "狗喜欢啃骨头",
    "猫和狗都是宠物",
]

# 第 1 步: 用 jieba 分词,再用空格拼成字符串
tokenized = []
for s in sentences:
    words = jieba.lcut(s)
    tokenized.append(" ".join(words))

# 第 2 步: 用 CountVectorizer 转为 BoW 矩阵
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(tokenized)

# 第 3 步: 打印词汇表和矩阵
print("词汇表:", vectorizer.vocabulary_)
print("BoW 矩阵:")
print(bow_matrix.toarray())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 词汇表包含预期关键字
    vocab = vectorizer.vocabulary_
    assert "猫" in vocab
    assert "狗" in vocab
    assert "喜欢" in vocab
    print("测试1通过: 词汇表包含关键字")

    # 测试 2: 矩阵形状为 (3, n_features)
    assert bow_matrix.shape[0] == 3
    assert bow_matrix.shape[1] == len(vocab)
    print("测试2通过: 矩阵形状", bow_matrix.shape)
