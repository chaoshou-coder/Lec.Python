"""
[难度: ⭐⭐]
[所属知识点: __init__ 构造函数 + self 绑定属性]
[预计完成时间: 10 分钟]

题目描述:
    给 Dog 类加 __init__,接收 name 和 age,用 self 绑定为
    实例属性。实例化时自动调用构造函数,打印狗的信息。

示例:
    >>> dog = Dog("旺财", 3)
    >>> print(dog.name, dog.age)
    旺财 3
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Dog:
    # 构造函数:实例化时自动调用
    def __init__(self, name, age):
        self.name = name  # 绑定实例属性 name
        self.age = age    # 绑定实例属性 age

# 实例化时传参给 __init__
dog = Dog("旺财", 3)
print(f"{dog.name} 今年 {dog.age} 岁")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常实例化
    d1 = Dog("旺财", 3)
    print(f"测试1: {d1.name} {d1.age}")  # 旺财 3

    # 测试 2: 不同实例属性独立
    d2 = Dog("小黑", 5)
    print(f"测试2: {d2.name} {d2.age}")  # 小黑 5

    # 测试 3: 修改属性不影响其他实例
    d1.age = 4
    print(f"测试3: {d1.age} {d2.age}")  # 4 5
