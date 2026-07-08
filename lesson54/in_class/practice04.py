"""
[难度: ⭐⭐]
[所属知识点: 上下文拼接]
[预计完成时间: 10 分钟]

实现 build_context 函数,接收 chunk 列表与索引列表,
换行拼接成 prompt context,返回字符串。
需保证顺序与完整度。

示例:
    >>> build_context(["a", "b", "c"], [2, 0])
    'c\na'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def build_context(chunks: list, indices: list) -> str:
    """按 indices 从 chunks 取片段,换行拼接。"""
    # TODO: 过滤越界索引,忽略无效项
    # TODO: 用列表推导取片段,join('\n') 拼接
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常拼接
    print(build_context(["a", "b", "c"], [2, 0]))
    # 测试 2: 包含越界索引
    print(build_context(["x", "y"], [1, 5, 0]))
    # 测试 3: 空 indices
    print(build_context(["x", "y"], []))
    # 测试 4: 单条
    print(build_context(["only"], [0]))
