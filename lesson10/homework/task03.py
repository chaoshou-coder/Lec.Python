"""
[难度: ⭐⭐⭐⭐]
[所属知识点: def + 循环 + 字符串拼接]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 reverse_string(s),返回字符串 s 的逆序,
    不使用 [::-1],用循环实现。

示例:
    >>> reverse_string("hello")
    'olleh'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result


# 示例调用
print("逆序:", reverse_string("hello"))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常字符串
    print(f"测试1: {reverse_string('hello')}")

    # 测试 2: 单个字符
    print(f"测试2: {reverse_string('a')}")

    # 测试 3: 空字符串
    print(f"测试3: {reverse_string('')}")

    # 测试 4: 中文
    print(f"测试4: {reverse_string('你好')}")
