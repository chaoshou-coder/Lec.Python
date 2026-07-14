"""
[难度: ⭐⭐⭐]
[所属知识点: def + if/else + return]
[预计完成时间: 15 分钟]

题目描述:
    定义一个函数 find_max(a, b, c),返回三个数中的最大值,
    不使用内置 max 函数。

示例:
    >>> find_max(3, 7, 5)
    7
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# 示例调用
print("最大值:", find_max(3, 7, 5))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 最大值在中间
    print(f"测试1: {find_max(1, 9, 5)}")

    # 测试 2: 全部相等
    print(f"测试2: {find_max(4, 4, 4)}")

    # 测试 3: 负数
    print(f"测试3: {find_max(-5, -1, -3)}")
