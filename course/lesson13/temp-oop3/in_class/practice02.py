"""
[难度: ⭐⭐⭐]
[所属知识点: Day06 employee 多态重写]
[预计完成时间: 12 分钟]

题目描述:
    Day06 的 `Employee→Manager→Sales` 薪资系统,
    在 L2 时我们用 `isinstance` 做分发:

    def show_pay(emp):
        if isinstance(emp, Manager):
            return emp.base + emp.bonus
        elif isinstance(emp, Sales):
            return emp.base + emp.commission
        else:
            return emp.base

    今天用**多态重写** show_pay,去掉全部 if-elif!

    Employee 基类已有 `pay()` 方法,
    子类已重写 pay(),
    所以 show_pay 只需一行:
    return emp.pay()

    验证:去掉 if-elif 后,
    新增 Employee 子类无需修改 show_pay。
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

    def pay(self):
        return self.base

class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus

class Sales(Employee):
    def __init__(self, name, base, commission):
        super().__init__(name, base)
        self.commission = commission

    def pay(self):
        return super().pay() + self.commission

def show_pay(emp):
    # 不超过 2 行,不使用 if/elif/isinstance/type
    pass

# emps = [Employee("张三", 5000), Manager("李四", 8000, 3000)]
# for e in emps:
#     print(show_pay(e))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    emps = [
        Employee("张三", 5000),
        Manager("李四", 8000, 3000),
        Sales("王五", 5000, 2000),
    ]
    assert show_pay(emps[0]) == 5000
    assert show_pay(emps[1]) == 11000
    assert show_pay(emps[2]) == 7000

    # 验证新子类(Engineer)无需改 show_pay
    class Engineer(Employee):
        def __init__(self, name, base, overtime):
            super().__init__(name, base)
            self.overtime = overtime

        def pay(self):
            return super().pay() + self.overtime

    eng = Engineer("赵六", 10000, 2000)
    assert show_pay(eng) == 12000  # 不需要改 show_pay!
    print("✅ 所有测试通过")
