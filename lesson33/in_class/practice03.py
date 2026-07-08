"""
[难度: ⭐⭐]
[所属知识点: 字符表编解码]
[预计完成时间: 10 分钟]

题目描述: 给定字符表 chars="abcdefghijklmnopqrstuvwxyz "
    (26 个小写字母 + 空格, 共 27 个字符), 请编写:
    1. char_to_idx: 字符 → 索引 的字典
    2. idx_to_char: 索引 → 字符 的字典
    3. encode(s): 把字符串 s 转为索引列表
    4. decode(ids): 把索引列表转回字符串
    最后验证 "hello world" 编解码 round-trip。

示例:
    >>> idx = char_to_idx['h']   # 7
    >>> ch = idx_tochar[7]        # 'h'
    >>> encode("hello world")    # [7, 4, 11, 11, 14, 26, 22, 14, 17, 11, 3]
    >>> decode([7,4,11,11,14])   # 'hello'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# 定义字符表: 26 个小写字母 + 空格
chars = "abcdefghijklmnopqrstuvwxyz "
vocab_size = len(chars)  # 27

# 第一步: 构造 char_to_idx 字典
char_to_idx = {ch: i for i, ch in enumerate(chars)}

# 第二步: 构造 idx_to_char 字典
idx_to_char = {i: ch for i, ch in enumerate(chars)}

# 第三步: 编写 encode 函数
def encode(s):
    """把字符串 s 转为索引列表"""
    return [char_to_idx[ch] for ch in s]

# 第四步: 编写 decode 函数
def decode(ids):
    """把索引列表转回字符串"""
    return "".join(idx_to_char[i] for i in ids)

# 测试编解码
test_str = "hello world"
ids = encode(test_str)
recovered = decode(ids)
print(f"原字符串:  '{test_str}'")
print(f"编码结果: {ids}")
print(f"解码结果: '{recovered}'")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: round-trip 编解码应还原原字符串
    assert recovered == test_str, \
        f"round-trip 失败: '{recovered}'"
    print("测试 1 通过: 'hello world' round-trip 成功")

    # 测试 2: 空格也应正确编解码
    s2 = "a z"
    assert decode(encode(s2)) == s2, \
        "空格编解码失败"
    print("测试 2 通过: 空格编解码成功")

    # 测试 3: vocab_size 应为 27
    assert vocab_size == 27, \
        f"vocab_size 错误, 得到 {vocab_size}"
    print("测试 3 通过: vocab_size = 27")
