"""
[难度: ⭐⭐]
[所属知识点: 默认参数]
[预计完成时间: 10 分钟]

题目描述:
    定义一个函数 power(base, exp=2),返回 base 的 exp 次方,
    默认 exp=2(即平方)。

示例:
    >>> power(5)
    25
    >>> power(2, 3)
    8
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def power(base, exp=2):
    result = 1
    for _ in range(exp):
        result *= base
    return result


# 示例调用
print("5^2 =", power(5))
print("2^3 =", power(2, 3))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认参数(平方)
    print(f"测试1: {power(4)}")

    # 测试 2: 指定指数
    print(f"测试2: {power(3, 4)}")

    # 测试 3: 指数为 0
    print(f"测试3: {power(5, 0)}")
