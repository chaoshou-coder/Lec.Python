"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 继承 + 方法重写 + 业务逻辑]
[预计完成时间: 30 分钟]

题目描述:
定义一个基类 Account,包含 balance 属性和 withdraw(amount) 方法;
子类 SavingsAccount:有 interest_rate 属性,提供 add_interest() 方法;
子类 CheckingAccount:有 overdraft_limit 属性,可透支取款。
withdraw() 在余额不足时抛出 ValueError。

示例:
    >>> sa = SavingsAccount(1000, 0.05)
    >>> sa.add_interest()
    >>> sa.balance
    1050.0
    >>> ca = CheckingAccount(500, 200)
    >>> ca.withdraw(600)
    >>> ca.balance
    -100
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: SavingsAccount 加利息
    sa = SavingsAccount(1000, 0.05)
    sa.add_interest()
    print(f储蓄余额: {sa.balance}")

    # 测试 2: SavingsAccount 超额取款
    try:
        sa.withdraw(2000)
    except ValueError as e:
        print(f"异常: {e}")

    # 测试 3: CheckingAccount 透支取款
    ca = CheckingAccount(500, 200)
    ca.withdraw(600)
    print(f"支票余额: {ca.balance}")

    # 测试 4: CheckingAccount 超出透支额度
    try:
        ca.withdraw(200)
    except ValueError as e:
        print(f"异常: {e}")
