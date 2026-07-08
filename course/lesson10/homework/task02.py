"""
[难度: ⭐⭐⭐⭐]
[所属知识点: def + 循环 + if + return]
[预计完成时间: 20 分钟]

题目描述:
    定义一个函数 is_prime(num),返回 True 如果 num 是质数,
    否则返回 False。质数定义为大于 1 且只能被 1 和自身整除。

示例:
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 示例调用
print("7 是质数?", is_prime(7))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 质数
    print(f"测试1: {is_prime(13)}")

    # 测试 2: 非质数
    print(f"测试2: {is_prime(15)}")

    # 测试 3: 边界 1
    print(f"测试3: {is_prime(1)}")

    # 测试 4: 边界 2
    print(f"测试4: {is_prime(2)}")
