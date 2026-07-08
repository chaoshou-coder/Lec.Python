"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 文本向量化 + 词袋模型 + 类封装]
[预计完成时间: 20 分钟]

实现一个 TextVectorizer 类, 提供 fit / transform / fit_transform 方法,
并支持 binary 模式。
  1. fit(corpus): 从语料构建词汇表 {词: 索引};
  2. transform(corpus): 将语料转为 BoW 矩阵;
     - binary=False (默认): 词频计数;
     - binary=True: 0/1 出现标记;
  3. fit_transform(corpus): 等价于 fit 后再 transform。

示例:
    >>> corpus = [["我", "喜欢", "Python"],
    ...           ["Python", "很", "好用"]]
    >>> tv = TextVectorizer()
    >>> X = tv.fit_transform(corpus)
    >>> X_bin = tv.transform(corpus, binary=True)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================


class TextVectorizer:
    """简易 BoW 向量化器, 支持 binary 模式。"""

    def __init__(self):
        self.vocab = {}

    def fit(self, corpus: list) -> "TextVectorizer":
        """从语料 corpus (list of list of token) 构建词汇表。"""
        unique_tokens = set()
        for sent in corpus:
            for token in sent:
                unique_tokens.add(token)
        sorted_tokens = sorted(unique_tokens)
        self.vocab = {}
        for idx, token in enumerate(sorted_tokens):
            self.vocab[token] = idx
        return self

    def transform(self, corpus: list,
                  binary: bool = False) -> list:
        """将语料转为 BoW 矩阵。

        参数:
            corpus: list of list of token。
            binary: True 则 0/1 出现, False 则词频计数。
        返回:
            列表的列表, 每行是一个句子的向量。
        """
        matrix = []
        for sent in corpus:
            vec = [0] * len(self.vocab)
            for token in sent:
                if token in self.vocab:
                    if binary:
                        vec[self.vocab[token]] = 1
                    else:
                        vec[self.vocab[token]] += 1
            matrix.append(vec)
        return matrix

    def fit_transform(self, corpus: list,
                      binary: bool = False) -> list:
        """先 fit 再 transform 的快捷方法。"""
        self.fit(corpus)
        return self.transform(corpus, binary=binary)


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    corpus = [
        ["我", "喜欢", "Python", "Python"],
        ["Python", "很", "好用"],
        ["我", "很", "开心"],
    ]

    tv = TextVectorizer()

    # 测试 1: fit_transform 默认模式(词频)
    X = tv.fit_transform(corpus)
    print("词汇表:", tv.vocab)
    print("BoW 矩阵(词频):")
    for row in X:
        print(f"  {row}")
    assert len(tv.vocab) == 6, "词表应为 6"
    assert len(X) == 3, "矩阵行数应为 3"
    # 第一句: Python 出现 2 次
    python_idx = tv.vocab["Python"]
    assert X[0][python_idx] == 2, \
        f"Python 频次应为 2, 实际 {X[0][python_idx]}"

    # 测试 2: binary=True
    X_bin = tv.transform(corpus, binary=True)
    print("\nBoW 矩阵(binary):")
    for row in X_bin:
        print(f"  {row}")
    # binary 模式下所有值∈{0, 1}
    for row in X_bin:
        for v in row:
            assert v in (0, 1), f"binary 值只能是 0/1, 实际 {v}"
    assert X_bin[0][python_idx] == 1, \
        "binary 模式下 Python 应标记为 1"

    # 测试 3: 新实例 fit_transform binary
    tv2 = TextVectorizer()
    X2 = tv2.fit_transform(corpus, binary=True)
    assert X2 == X_bin, "fit_transform binary 应与 transform 一致"
    print("\n测试3通过: fit_transform binary = transform binary")
