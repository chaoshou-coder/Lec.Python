"""
[难度: ⭐]
[所属知识点: 固定大小 chunking]
[预计完成时间: 5 分钟]

实现 fixed_chunk 函数,接收文本与 chunk_size,
按字符等长切分,返回 chunk 列表。
末尾不足 chunk_size 时保留剩余部分。

示例:
    >>> fixed_chunk("abcdefghij", 3)
    ['abc', 'def', 'ghi', 'j']
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def fixed_chunk(text: str, chunk_size: int) -> list:
    """按固定大小等长切分文本,末尾保留剩余。"""
    # TODO: 参数校验,chunk_size <= 0 时返回空列表
    # TODO: 使用 range 步进切片,text[i:i+chunk_size]
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常切分,末尾不足
    print(fixed_chunk("abcdefghij", 3))
    # 测试 2: 整除,无剩余
    print(fixed_chunk("abcdef", 2))
    # 测试 3: chunk_size 大于文本长度
    print(fixed_chunk("hi", 5))
    # 测试 4: 边界 chunk_size=0
    print(fixed_chunk("abc", 0))
