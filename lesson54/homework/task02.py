"""
[难度: ⭐⭐⭐]
[所属知识点: Token 近似 + 安全 Top-K]
[预计完成时间: 15 分钟]

实现 safe_topk 函数,给定 chunk 列表、相似度、K、max_tokens,
每个 chunk 按 1 token ≈ 4 字符估算,若拼接后超出 max_tokens,
返回满足限制的最大 Top-K 索引。

示例:
    >>> safe_topk(["abcd", "efgh"], [0.9, 0.5], 2, 2)
    [0]
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def safe_topk(
    chunks: list, scores: list, k: int, max_tokens: int
) -> list:
    """在 token 限制下返回最大 Top-K 索引。"""
    # TODO: 按分数降序排列索引
    # TODO: 逐个累加 token(len(chunk)/4 向上取整)
    # TODO: 超出 max_tokens 时停止,返回已选索引
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 只能取 1 个
    print(safe_topk(["abcd", "efgh"], [0.9, 0.5], 2, 2))
    # 测试 2: 全部可取
    print(safe_topk(["a", "b"], [0.8, 0.6], 2, 100))
    # 测试 3: max_tokens=0
    print(safe_topk(["abc"], [0.9], 1, 0))
    # 测试 4: 空列表
    print(safe_topk([], [], 3, 10))
