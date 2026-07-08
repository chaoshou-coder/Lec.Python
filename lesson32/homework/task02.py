"""
[难度: ⭐⭐⭐]
[所属知识点: 词袋模型 BoW + 词汇表构建]
[预计完成时间: 15 分钟]

手写 compute_bow() 函数, 对任意句子列表返回词汇表(字典)和
BoW 矩阵(列表的列表, 不用 sklearn)。
  1. 遍历所有句子, 去重后按字典序排序构建词汇表
     {词: 索引};
  2. 对每句话统计每个词出现的频次, 生成一条向量;
  3. 返回 (vocabulary, bow_matrix)。

示例:
    >>> sents = ["我 喜欢 Python",
    ...          "Python 很 好用",
    ...          "我 很 开心"]
    >>> vocab, mat = compute_bow(sents)
    >>> # vocab = {"Python":0, "好用":1, ...}
    >>> # mat   = [[1,0,...],[1,1,...],...]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


def compute_bow(sentences: list) -> tuple:
    """对句子列表返回 (词汇表, BoW 矩阵)。

    参数:
        sentences: 已分词的句子, 每个句子为 list of token。
    返回:
        vocab: {词: 索引} 字典, 按字典序排列。
        matrix: 列表的列表, 每行对应一个句子的词频向量。
    """
    # 1. 收集所有 token, 去重并排序
    unique_tokens = set()
    for sent in sentences:
        for token in sent:
            unique_tokens.add(token)
    sorted_tokens = sorted(unique_tokens)

    # 2. 构建词汇表 {token: index}
    vocab = {}
    for idx, token in enumerate(sorted_tokens):
        vocab[token] = idx

    # 3. 构建 BoW 矩阵
    matrix = []
    for sent in sentences:
        vec = [0] * len(vocab)
        for token in sent:
            vec[vocab[token]] += 1
        matrix.append(vec)

    return vocab, matrix


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 3 句简单语料
    sents = [
        ["我", "喜欢", "Python"],
        ["Python", "很", "好用"],
        ["我", "很", "开心"],
    ]
    vocab, mat = compute_bow(sents)
    print(f"词汇表: {vocab}")
    print(f"BoW 矩阵:")
    for row in mat:
        print(f"  {row}")

    # 验证词汇表大小
    assert len(vocab) == 6, f"词汇表应为6, 实际 {len(vocab)}"
    # 验证矩阵行数 == 句子数
    assert len(mat) == 3, "矩阵行数应为 3"
    # 验证第一句"我 喜欢 Python"的词频
    assert sum(mat[0]) == 3, "第一句应有 3 个 token"

    # 测试 2: 含重复词
    sents2 = [
        ["苹果", "苹果", "好吃"],
        ["香蕉", "好吃"],
    ]
    vocab2, mat2 = compute_bow(sents2)
    assert len(vocab2) == 3, f"sents2 词表应为3, 实际 {len(vocab2)}"
    # 第一句"苹果"出现 2 次
    assert mat2[0][vocab2["苹果"]] == 2, "苹果频次应为 2"
    print(f"\n测试2通过: vocab={vocab2}, mat={mat2}")
