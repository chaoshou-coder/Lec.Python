"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 消费者函数即门控(checkout 骨架)]
[预计完成时间: 15 分钟]

题目描述:
    下方 `checkout` 函数由教师提供,**不可修改核心逻辑**。
    学员必须通过实现正确的子类让它跑通。

    约束:
    - checkout 函数内不使用 if/elif/isinstance/type
    - 函数体不超过 4 行
    - 漏写 execute 方法时,实例化阶段报 TypeError

    请补全下方的 `Alipay` / `WeChatPay` / `ApplePay`。

示例:
    >>> checkout(99.0, Alipay())
    支付宝支付 99.0 元
    True
"""

# ====================== 学员代码区(不可修改)=====================
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

def checkout(cart_total, payment):
    if cart_total <= 0:
        print("购物车为空")
        return False
    # payment.execute(amount) 是核心:统一接口,不同实现
    return payment.execute(cart_total)

# 请补全下面三个子类:
class Alipay(Payment):
    pass

# class WeChatPay(Payment): ...
# class ApplePay(Payment): ...

# ====================== 测试区(不可修改)=====================
if __name__ == '__main__':
    payments = [Alipay(), WeChatPay(), ApplePay()]
    for p in payments:
        result = checkout(99.0, p)
        assert result is True or result is False

    # 验证漏写 execute 会报错
    try:
        class BadPay(Payment):
            pass
        BadPay()
        assert False, "漏写 execute 应报 TypeError"
    except TypeError:
        pass

    # 验证 0 元被拒绝
    assert checkout(0, Alipay()) is False

    print("✅ 所有测试通过")
