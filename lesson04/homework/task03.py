"""
[难度: ⭐⭐⭐]
[所属知识点: while 循环与累乘]
[预计完成时间: 15 分钟]

题目描述:
  编写一个程序,使用 while 循环计算 n 的阶乘。
  输入一个非负整数 n,输出 n! 的结果。
  规定 0! = 1。

示例:
    >>> 输入: 5
    120
    >>> 输入: 0
    1
    >>> 输入: 7
    5040
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 5 的阶乘
    n = 5
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(result)
    assert result == 120

    # 测试 2: 0 的阶乘
    n = 0
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(result)
    assert result == 1

    # 测试 3: 7 的阶乘
    n = 7
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(result)
    assert result == 5040

    # 测试 4: 1 的阶乘
    n = 1
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(result)
    assert result == 1

    print("所有测试通过!")
