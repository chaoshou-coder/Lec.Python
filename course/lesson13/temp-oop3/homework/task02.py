"""
[难度: ⭐⭐⭐⭐]
[所属知识点: NCDL 复盘 — 找错代码中的契约违反]
[预计完成时间: 25 分钟,选做]

题目描述:
    下面 3 段代码都是"能跑但有设计缺陷"的。

    **题目 1**:下面代码的 if-elif 为什么"能跑"但不该用?
    请指出 3 个坏味道。

        def pay(emp_type, amount):
            if emp_type == "alipay":
                print(f"支付宝 {amount}")
            elif emp_type == "wechat":
                print(f"微信 {amount}")
            elif emp_type == "apple":
                print(f"Apple {amount}")
            # 新加一种都要改这里!

    **题目 2**:下面 abc 用了但形同虚设。为什么?

        class Payment:          # 没有 abc.ABC!
            @abc.abstractmethod
            def execute(self, amount):
                ...

    **题目 3**:下面子类漏写 execute,但不会报错。
    为什么?如何修复?

        class Broken(Payment):
            pass

        Broken()  # 不报错,因为 Payment 不是 abc.ABC

请在下方学员代码区标出每段代码的修复方法。

    **答案参考**:
    1. if-elif 违反开闭原则 → 用多态
    2. 继承 abc.ABC 才能让 abstractmethod 生效
    3. Pizza Payment: => class Payment(abc.ABC):
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

# 题目 1:if-elif 为什么不好?
# 写在这里:
# 坏味 1: ___________
# 坏味 2: ___________
# 坏味 3: ___________

# 题目 2:为什么 abstractmethod 不生效?
# 原因: ___________
# 修复: ___________

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 验证修复后正确行为
    class Payment(abc.ABC):  # 修复:加 abc.ABC
        @abc.abstractmethod
        def execute(self, amount): ...

    class Alipay(Payment):
        def execute(self, amount):
            return True

    # 不实现 execute 会报错
    try:
        class BadPay(Payment): pass
        BadPay()
        assert False
    except TypeError:
        pass

    # 正常子类能用
    assert Alipay().execute(100) is True
    print("✅ 所有测试通过")
