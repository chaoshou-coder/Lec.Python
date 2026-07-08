"""
[难度: ⭐⭐⭐]
[所属知识点: TF-IDF 手动实现 (numpy)]
[预计完成时间: 15 分钟]

题目: 手写 TF-IDF 计算器
给定 3 句已分词好的短句(列表的列表),请手写
compute_tfidf() 函数计算每个词在每个句子的
TF-IDF 值,返回 {句序号: {词: 值}} 的字典。

公式:
    TF(t,d) = 词 t 在句子 d 出现次数 / 句子 d 总词数
    IDF(t) = log(总句数 / 包含词 t 的句数)
    TF-IDF = TF * IDF

示例:
    >>> docs = [["猫", "吃", "鱼"], ["猫", "狗"]]
    >>> result = compute_tfidf(docs)
    >>> # result[0]["猫"] 应为一个浮点数
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
from collections import Counter


def compute_tfidf(docs):
    """手写 TF-IDF,返回 {句序号: {词: tfidf}}"""
    n_docs = len(docs)
    # 第 1 步: 统计每句的词频
    tf_list = []
    for doc in docs:
        count = Counter(doc)
        total = len(doc)
        tf = {word: cnt / total for word, cnt in count.items()}
        tf_list.append(tf)

    # 第 2 步: 计算每个词的 IDF
    df = Counter()
    for doc in docs:
        unique_words = set(doc)
        for w in unique_words:
            df[w] += 1

    idf = {}
    for w, freq in df.items():
        idf[w] = np.log(n_docs / freq)

    # 第 3 步: 组合 TF * IDF
    result = {}
    for idx, tf in enumerate(tf_list):
        result[idx] = {}
        for word, tf_val in tf.items():
            result[idx][word] = tf_val * idf[word]

    return result


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    docs = [
        ["猫", "吃", "鱼", "猫"],
        ["狗", "啃", "骨头"],
        ["猫", "和", "狗", "是", "宠物"],
    ]

    result = compute_tfidf(docs)

    # 测试 1: "猫"在句 0 的 TF-IDF 应 > 句 2
    # (句 0 里猫出现 2/4,TF 更大)
    tfidf_cat_0 = result[0]["猫"]
    tfidf_cat_2 = result[2]["猫"]
    print(f"句0'猫' tfidf: {tfidf_cat_0:.4f}")
    print(f"句2'猫' tfidf: {tfidf_cat_2:.4f}")
    assert tfidf_cat_0 > tfidf_cat_2

    # 测试 2: "骨头"只在句 1 出现,IDF > 1
    tfidf_bone = result[1]["骨头"]
    print(f"句1'骨头' tfidf: {tfidf_bone:.4f}")
    assert tfidf_bone > 0

    # 测试 3: 结构正确
    assert len(result) == 3
    for idx in range(3):
        assert isinstance(result[idx], dict)
    print("测试3通过: 结构正确")
