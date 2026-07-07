"""
[难度: ⭐⭐⭐]
[所属知识点: def + 算术]
[预计完成时间: 15 分钟]

题目描述:
    定义一个函数 celsius_to_fahrenheit(c),把摄氏度转华氏度,
    公式: F = C * 9/5 + 32。

示例:
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


# 示例调用
print("0°C =", celsius_to_fahrenheit(0), "°F")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 冰点
    print(f"测试1: {celsius_to_fahrenheit(0)}")

    # 测试 2: 沸点
    print(f"测试2: {celsius_to_fahrenheit(100)}")

    # 测试 3: 负温度
    print(f"测试3: {celsius_to_fahrenheit(-40)}")
