"""
[难度: ⭐⭐⭐⭐]
[所属知识点: def + 循环 + return]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 factorial(n),返回 n 的阶乘(用循环实现)。
    约定 0! = 1。

示例:
    >>> factorial(5)
    120
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 示例调用
print("5! =", factorial(5))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常值
    print(f"测试1: {factorial(5)}")

    # 测试 2: 0 的阶乘
    print(f"测试2: {factorial(0)}")

    # 测试 3: 1 的阶乘
    print(f"测试3: {factorial(1)}")

    # 测试 4: 较大值
    print(f"测试4: {factorial(10)}")
