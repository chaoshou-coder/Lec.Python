"""
[难度: ⭐⭐]
[所属知识点: 滑动窗口 chunking]
[预计完成时间: 10 分钟]

实现 sliding_window 函数,接收文本、chunk_size 与 step,
返回重叠窗口列表。chunk_size=6, step=3 测试。

示例:
    >>> sliding_window("abcdefghij", 6, 3)
    ['abcdef', 'defghi', 'ghij']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def sliding_window(
    text: str, chunk_size: int, step: int
) -> list:
    """滑动窗口切分,窗口之间可重叠。"""
    # TODO: 参数校验,step <= 0 或 chunk_size <= 0 返回 []
    # TODO: range(0, len(text) - chunk_size + 1, step)
    # TODO: 若文本短于 chunk_size,视需求保留或返回 []
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常滑动
    print(sliding_window("abcdefghij", 6, 3))
    # 测试 2: step=1,高重叠
    print(sliding_window("abcd", 2, 1))
    # 测试 3: 文本短于 chunk_size
    print(sliding_window("ab", 5, 2))
    # 测试 4: step=0 边界
    print(sliding_window("abcde", 2, 0))
