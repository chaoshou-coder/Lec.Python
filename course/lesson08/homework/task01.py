"""
[难度: ⭐⭐⭐⭐]
[所属知识点: @property 余额保护 + 存取款方法]
[预计完成时间: 25 分钟]

题目描述:
    设计 BankAccount 类,用 @property 保护余额(非负),
    提供 deposit(存款) 和 withdraw(取款) 方法,取款超额
    返回 False。体会"业务逻辑封装在类内部"。

示例:
    >>> acc = BankAccount("小明", 100)
    >>> acc.deposit(50)
    >>> acc.withdraw(30)
    True
    >>> print(acc.balance)
    120
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # 走 setter 校验

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("余额不能为负数")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"BankAccount(户主={self.owner}, 余额={self.balance})"

acc = BankAccount("小明", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常存取
    a = BankAccount("小明", 100)
    a.deposit(50)
    print(f"测试1: {a.balance}")  # 150
    ok = a.withdraw(30)
    print(f"测试2: {ok} {a.balance}")  # True 120

    # 测试 3: 取款超额失败
    ok = a.withdraw(999)
    print(f"测试3: {ok} {a.balance}")  # False 120

    # 测试 4: 负数存款失败
    ok = a.deposit(-10)
    print(f"测试4: {ok} {a.balance}")  # False 120

    # 测试 5: 构造时负数抛异常
    try:
        BankAccount("小红", -50)
        print("测试5: 未抛异常(错)")
    except ValueError as e:
        print(f"测试5: {e}")  # 余额不能为负数

    # 测试 6: __str__ 输出
    print(f"测试6: {a}")  # BankAccount(户主=小明, 余额=120)
