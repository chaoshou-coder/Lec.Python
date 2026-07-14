"""
[难度: ⭐⭐⭐]
[所属知识点: 动物园体系 —— 继承 + 重写 + 多态引入]
[预计完成时间: 13 分钟]

题目描述:
    定义父类 `Animal`,方法 `speak()` 返回 "..."。
    定义子类 `Dog` 和 `Cat`,**重写** `speak()`:
    - Dog 返回 "汪汪"
    - Cat 返回 "喵喵"
    定义函数 `animal_sound(animal)`,调用 `animal.speak()`。

    虽然 animal_sound 不知道传入的是 Dog 还是 Cat,
    但能得到不同结果 —— 这就是**多态**的雏形。

示例:
    >>> animal_sound(Dog())
    汪汪
    >>> animal_sound(Cat())
    喵喵
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    pass

def animal_sound(animal):
    pass

# animals = [Dog(), Cat(), Dog()]
# for a in animals:
#     print(animal_sound(a))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    assert animal_sound(Dog()) == "汪汪"
    assert animal_sound(Cat()) == "喵喵"
    # 混合列表测试
    zoo = [Dog(), Cat(), Dog(), Cat()]
    sounds = [animal_sound(a) for a in zoo]
    assert sounds == ["汪汪", "喵", "汪汪", "喵"] or sounds.count("汪汪") == 2
    print("✅ 所有测试通过")
