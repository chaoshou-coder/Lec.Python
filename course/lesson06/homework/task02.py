"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Employee 薪资系统(多态引入)]
[预计完成时间: 25 分钟,选做]

题目描述:
    扩展 Day05 的员工薪资系统。

    - 基类 `Employee(name, base_salary)`
    - 子类 `Manager(name, base, bonus)`
    - 子类 `Sales(name, base, commission)`
    - 子类 `Engineer(name, base, overtime_pay)`
      - pay() = base + overtime_pay

    写函数 `show_pay(emp)`,打印某员工的薪资。
    (先"能跑"即可,允许用 isinstance,
    但 Day07 会重构去掉它)

    创建各类型一个实例,
    放入列表遍历调用 show_pay。

示例:
    >>> show_pay(Manager("李四", 8000, 3000))
    李四 薪资: 11000
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

# class Manager(Employee): ...
# class Sales(Employee): ...
# def show_pay(emp): ...

# emps = [Employee("张三", 5000), Manager("李四", 8000, 3000)]
# for e in emps:
#     show_pay(e)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    emps = [
        Employee("张三", 5000),
        Manager("李四", 8000, 3000),
        Sales("王五", 5000, 2000),
    ]
    expected = [5000, 11000, 7000]
    actual = [e.pay() for e in emps]
    assert actual == expected, f"预期 {expected},实际 {actual}"

    # __str__ 友好
    for e in emps:
        s = str(e)
        assert e.name in s
    print("✅ 所有测试通过")
