"""
[难度: ⭐⭐⭐⭐]
[所属知识点: MRO 方法解析顺序 + isinstance 反模式]
[预计完成时间: 13 分钟]

题目描述:
    1. 查看 `Dog -> Mammal -> Animal` 的 MRO 顺序
    2. 判断 `isinstance` 沿继承链追溯
    3. 读下面代码,找出 if-elif 类型分发的 3 个坏味道

反模式代码:
    def pay(employee):
        if isinstance(employee, Manager):
            return employee.base + employee.bonus
        elif isinstance(employee, Sales):
            return employee.base + employee.commission
        elif isinstance(employee, Employee):
            return employee.base
        # 新加类型都要改这里!

坏味道(答案):
    1. 新加员工类型要改 pay 函数 (违反开闭原则)
    2. pay 随着类型增加越来越长
    3. 应该用多态而非类型检查(留到 Day07)

示例:
    >>> Animal.__mro__
    (<class '__main__.Animal'>, <class 'object'>)
    >>> isinstance(Dog(), Animal)
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

dog = Dog()

# 查看 MRO
print(Dog.__mro__)

# 判断类型
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Mammal))   # True(爷爷也算)
print(isinstance(dog, Animal))   # True
print(isinstance(dog, str))      # False

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # MRO 验证
    mro = Dog.__mro__
    assert Dog in mro
    assert Mammal in mro
    assert Animal in mro
    assert object in mro

    # isinstance 沿继承链追溯
    dog = Dog()
    assert isinstance(dog, Dog)
    assert isinstance(dog, Mammal)
    assert isinstance(dog, Animal)
    assert not isinstance(dog, str)
    assert not isinstance("hello", Dog)

    # issubclass
    assert issubclass(Dog, Animal)
    assert issubclass(Dog, Dog)  # 自己算自己的子类
    assert not issubclass(Animal, Dog)
    print("✅ 所有测试通过")
