"""
[难度: ⭐⭐]
[所属知识点: Chunk 数量估算]
[预计完成时间: 10 分钟]

实现 estimate_chunks 函数,给定文本长度、chunk_size、step,
返回滑动窗口下的 chunk 数量。纯数学计算。

示例:
    >>> estimate_chunks(10, 6, 3)
    2
    >>> estimate_chunks(20, 5, 5)
    4
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def estimate_chunks(
    text_len: int, chunk_size: int, step: int
) -> int:
    """纯数学估算滑动窗口 chunk 数量。"""
    # TODO: 参数非法(text_len<=0 或 chunk_size<=0 或 step<=0)
    #       返回 0
    # TODO: text_len < chunk_size 时返回 0
    # TODO: 公式: (text_len - chunk_size) // step + 1
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常估算
    print(estimate_chunks(10, 6, 3))
    # 测试 2: 整除无余
    print(estimate_chunks(20, 5, 5))
    # 测试 3: 文本短于 chunk_size
    print(estimate_chunks(3, 5, 2))
    # 测试 4: step=0 边界
    print(estimate_chunks(10, 3, 0))
