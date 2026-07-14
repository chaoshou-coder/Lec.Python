"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Payment(abc.ABC) + Alipay/WeChatPay]
[预计完成时间: 20 分钟,选做]

题目描述:
    实现支付系统:
    - `Payment(abc.ABC)`,抽象方法 `execute(amount) -> bool`
    - `Alipay(Payment)`:execute 输出 "支付宝支付 X 元",返回 True
    - `WeChatPay(Payment)`:execute 输出 "微信支付 X 元",返回 True

    完成下方给定的 checkout 函数(不超过 4 行),
    验证:
    1. 两个子类都能正常 checkout
    2. 漏写 execute 时报 TypeError
    3. 新增 ApplePay 时不需改 checkout

    **约束**:checkout 内禁止出现 if/elif/isinstance/type
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(Payment):
    pass

# class WeChatPay(Payment): ...

def checkout(cart_total, payment):
    # 不超过 4 行
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    for p in [Alipay(), WeChatPay()]:
        assert checkout(100, p) is True or checkout(100, p) is False

    try:
        class BadPay(Payment): pass
        BadPay()
        assert False, "漏写 execute 必须报错"
    except TypeError:
        pass

    # 新增不需改 checkout
    class ApplePay(Payment):
        def execute(self, amount):
            print(f"Apple Pay {amount}")
            return True

    assert checkout(99, ApplePay()) in (True, False)
    print("✅ 所有测试通过")
