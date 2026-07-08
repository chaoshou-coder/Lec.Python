"""
[难度: ⭐⭐⭐]
[所属知识点: 语义相似句检索]
[预计完成时间: 15 分钟]

场景: 给定 query 句子和候选集,求最相似的 top1 句子。
列表为 ["如何用 Python 读取文件","今天天气真好","深度学习入门指南"],
query="怎么打开 txt 文件",应返回 index 0。

示例:
    >>> top1_search("怎么打开 txt 文件")
    0
"""

import numpy as np
from sentence_transformers import SentenceTransformer


_model = SentenceTransformer("all-MiniLM-L6-v2")

CANDIDATES = [
    "如何用 Python 读取文件",
    "今天天气真好",
    "深度学习入门指南",
]


# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def top1_search(query: str) -> int:
    """返回候选集中与 query 最相似的句子索引"""
    # TODO: 对 query 编码
    # TODO: 对 CANDIDATES 批量编码
    # TODO: 计算 query 与每个候选的余弦相似度
    # TODO: 返回相似度最高者的索引
    pass


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    """辅助: 计算两个向量的余弦相似度"""
    # TODO: 返回 dot(a,b) / (norm(a) * norm(b))
    pass


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: query 关于文件,应匹配索引 0
    idx = top1_search("怎么打开 txt 文件")
    assert idx == 0, f"应返回 0,实际返回 {idx}"
    print("测试 1 通过: top1 索引 =", idx)

    # 测试 2: query 关于天气,应匹配索引 1
    idx2 = top1_search("外面阳光明媚")
    assert idx2 == 1, f"应返回 1,实际返回 {idx2}"
    print("测试 2 通过: top1 索引 =", idx2)
