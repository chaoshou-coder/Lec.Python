"""
[难度: ⭐⭐⭐]
[所属知识点: def + return + 布尔]
[预计完成时间: 15 分钟]

题目描述:
    定义一个函数 is_even(num),返回 True 如果 num 是偶数,
    否则返回 False。

示例:
    >>> is_even(4)
    True
    >>> is_even(7)
    False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def is_even(num):
    return num % 2 == 0


# 示例调用
print("4 是偶数?", is_even(4))
print("7 是偶数?", is_even(7))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 偶数
    print(f"测试1: {is_even(10)}")

    # 测试 2: 奇数
    print(f"测试2: {is_even(9)}")

    # 测试 3: 零
    print(f"测试3: {is_even(0)}")

    # 测试 4: 负数
    print(f"测试4: {is_even(-3)}")
