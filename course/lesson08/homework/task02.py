"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 电商订单系统 v2 雏形(L1-L4 整合)]
[预计完成时间: 30 分钟,选做]

题目描述:
    整合 L1-L4 全部知识,写一个可运行的系统。

    要求:
    - L1 封装:Product(@property 保护 price + __str__ + 类属性 tax_rate)
    - L2 继承:PhysicalProduct / DigitalProduct 子类(重写 shipping_cost)
    - L3 多态:Payment(abc.ABC) + Alipay/WeChatPay + checkout() 无 if-elif
    - L4 组合:Order 组合 Cart + Payment + Address
    - L4 运算符:ShoppingCart.__add__ / __len__ / __iter__
    - L4 协议:Product.__eq__ / __hash__

    验证:
    1. 创建商品 → 加入购物车 → 合并两车 → 创建订单 → checkout
    2. 新增支付方式不需改 checkout
    3. 新增产品类型不需改任何现有代码

示例:
    >>> p1 = Product("Python", 50)
    >>> p2 = Product("算法", 30)
    >>> cart = ShoppingCart([p1, p2])
    >>> order = Order(cart, Alipay(), Address("北京"))
    >>> print(order.summary())
    2 件,总价 80,送到 北京
    >>> checkout(80, Alipay())
    支付宝支付 80
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Product:
    tax_rate = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负")
        self._price = value

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"[{self.name}] {self.price} 元"

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount):
        ...

class Alipay(Payment):
    def execute(self, amount):
        print(f"支付宝 {amount}")
        return True

class WeChatPay(Payment):
    def execute(self, amount):
        print(f"微信 {amount}")
        return True

class ShoppingCart:
    def __init__(self, items=None):
        self.items = items or []

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        yield from self.items

class Address:
    def __init__(self, city):
        self.city = city

class Order:
    def __init__(self, cart, payment, address):
        self.cart = cart
        self.payment = payment
        self.address = address

    def summary(self):
        return f"{len(self.cart)} 件 -> {self.address.city}"

def checkout(total, payment):
    if total <= 0:
        return False
    return payment.execute(total)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p1 = Product("Python", 50)
    p2 = Product("算法", 30)
    cart = ShoppingCart([p1, p2])
    order = Order(cart, Alipay(), Address("北京"))
    print(order.summary())
    checkout(80, Alipay())
    checkout(80, WeChatPay())

    # 新增不需改
    class ApplePay(Payment):
        def execute(self, amount):
            print(f"Apple {amount}")
            return True

    checkout(80, ApplePay())
    print("✅ 所有测试通过")
