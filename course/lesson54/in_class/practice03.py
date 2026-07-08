"""
[难度: ⭐⭐]
[所属知识点: Top-K 检索接口]
[预计完成时间: 10 分钟]

实现 topk_search 函数,给定相似度分数列表与 K,
返回前 K 个最高分的索引列表(降序)。

示例:
    >>> topk_search([0.1, 0.9, 0.4, 0.7], 2)
    [1, 3]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import heapq

def topk_search(scores: list, k: int) -> list:
    """返回scores中前K个最大值的索引,按分数降序。"""
    # TODO: k <= 0 时返回 []
    # TODO: 可用 heapq.nlargest 或 enumerate+sorted
    # TODO: 只返回索引列表,不返回分数
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常 Top-2
    print(topk_search([0.1, 0.9, 0.4, 0.7], 2))
    # 测试 2: K 大于列表长度
    print(topk_search([0.3, 0.5], 5))
    # 测试 3: 相同分数
    print(topk_search([0.5, 0.5, 0.1], 2))
    # 测试 4: K=0
    print(topk_search([0.1, 0.2], 0))
