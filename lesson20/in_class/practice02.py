"""
[难度: ⭐⭐⭐]
[所属知识点: 继承 + 方法重写]
[预计完成时间: 15 分钟]

题目描述:
定义子类 Dog 和 Cat,继承 Animal,
重写 speak() 方法:
- Dog.speak() 返回 "汪汪"
- Cat.speak() 返回 "喵喵"

示例:
    >>> d = Dog("旺财")
    >>> d.speak()
    '汪汪'
    >>> c = Cat("小花")
    >>> c.speak()
    '喵喵'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: Dog 的 speak
    d1 = Dog("旺财")
    print(d1.speak())

    # 测试 2: Cat 的 speak
    c1 = Cat("小花")
    print(c1.speak())

    # 测试 3: 验证继承的 name 属性
    print(f"狗名字: {d1.name}")
    print(f"猫名字: {c1.name}")

    # 测试 4: isinstance 验证继承关系
    print(f"dog 是 Animal: {isinstance(d1, Animal)}")
