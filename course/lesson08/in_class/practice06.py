"""
[难度: ⭐⭐⭐]
[所属知识点: __str__ 魔术方法]
[预计完成时间: 15 分钟]

题目描述:
    给 Dog 类加 __str__ 魔术方法,返回 "Dog(名字=旺财, 年龄=3)"。
    直接 print(实例) 就能看到友好信息,不用手动拼字符串。

示例:
    >>> dog = Dog("旺财", 3)
    >>> print(dog)
    Dog(名字=旺财, 年龄=3)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 魔术方法:print(实例) 时自动调用
    def __str__(self):
        return f"Dog(名字={self.name}, 年龄={self.age})"

dog = Dog("旺财", 3)
print(dog)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: print 直接输出友好信息
    d1 = Dog("旺财", 3)
    print(f"测试1: {d1}")  # Dog(名字=旺财, 年龄=3)

    # 测试 2: 不同实例不同输出
    d2 = Dog("小黑", 5)
    print(f"测试2: {d2}")  # Dog(名字=小黑, 年龄=5)

    # 测试 3: str() 转换
    s = str(d1)
    print(f"测试3: {s}")  # Dog(名字=旺财, 年龄=3)

    # 测试 4: f-string 中使用
    print(f"测试4: 我的狗是{d1}")  # 我的狗是Dog(名字=旺财, 年龄=3)
