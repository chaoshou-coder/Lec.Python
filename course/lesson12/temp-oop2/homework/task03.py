"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 对比题-继承+重写 vs 纯 duck typing]
[预计完成时间: 30 分钟,选做]

题目描述:
    同一需求(Zoo 动物园)分别用两种方式实现。

    方式 A(继承):
    - `Animal` 基类 + `speak()` 返回 "..."
    - `Dog` / `Cat / Bird` 子类重写 speak()

    方式 B(鸭子类型):
    - 直接定义 `Dog` / `Cat` / `Bird`,不继承同一个父类
    - 各自实现 speak()

    分别创建各三只动物,验证两种方式结果相同。

    思考:方式 B 代码更少,为什么还要用方式 A?

示例:
    # 方式 A
    zoo_a = [Dog(), Cat(), Bird()]
    # 方式 B
    zoo_b = [Dog(), Cat(), Bird()]

    结果应相同,但扩展性不同。
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# ===== 方式 A:继承 =====
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    pass

# class Cat(Animal): ...
# class Bird(Animal): ...

# ===== 方式 B:鸭子类型 =====
class Dog2:
    pass

# class Cat2: ...
# class Bird2: ...

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 方式 A
    zoo_a = [Dog(), Cat(), Bird()]
    sounds_a = [a.speak() for a in zoo_a]

    # 方式 B
    zoo_b = [Dog2(), Cat2(), Bird2()]
    sounds_b = [a.speak() for a in zoo_b]

    # 结果应相同
    assert sounds_a == sounds_b
    print(f"方式 A: {sounds_a}")
    print(f"方式 B: {sounds_b}")

    # 验证方式 A 有继承链
    assert isinstance(Dog(), Animal)
    # 方式 B 没有
    assert not isinstance(Dog2(), Animal)
    print("✅ 所有测试通过")
