"""
[难度: ⭐⭐⭐]
[所属知识点: 默认参数 + 算术]
[预计完成时间: 15 分钟]

题目描述:
    定义一个函数 apply_discount(price, discount=0.1),
    返回打折后的价格,默认 9 折(即 discount=0.1)。

示例:
    >>> apply_discount(100)
    90.0
    >>> apply_discount(100, discount=0.2)
    80.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def apply_discount(price, discount=0.1):
    return price * (1 - discount)


# 示例调用
print("默认 9 折:", apply_discount(100))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 默认折扣
    print(f"测试1: {apply_discount(200)}")

    # 测试 2: 自定义折扣
    print(f"测试2: {apply_discount(200, discount=0.3)}")

    # 测试 3: 零折扣
    print(f"测试3: {apply_discount(150, discount=0)}")
