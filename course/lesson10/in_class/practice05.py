"""
[难度: ⭐⭐⭐⭐]
[所属知识点: def + 循环 + in + return]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 count_vowels(s),返回字符串 s 中
    元音字母(a/e/i/o/u,不区分大小写)的个数。

示例:
    >>> count_vowels("Hello World")
    3
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


# 示例调用
print("元音个数:", count_vowels("Hello World"))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常英文
    print(f"测试1: {count_vowels('Hello World')}")

    # 测试 2: 全元音
    print(f"测试2: {count_vowels('aeiou')}")

    # 测试 3: 空字符串
    print(f"测试3: {count_vowels('')}")

    # 测试 4: 大写
    print(f"测试4: {count_vowels('AEIOU')}")
