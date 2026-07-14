"""
[难度: ⭐⭐]
[所属知识点: 组合 vs 继承判断]
[预计完成时间: 10 分钟]

题目描述:
    每组选择一个正确答案:"用继承还是组合"?

    1. Order(订单) has-a Cart(购物车):
       A. class Order(Cart)    B. Order 持有 Cart 实例

    2. Dog(狗) is-a Animal(动物):
       A. Dog 持有 Animal 实例  B. class Dog(Animal)

    3. Car(汽车) has-a Engine(引擎):
       A. class Car(Engine)     B. Car 持有 Engine 实例

    4. ShoppingCart(购物车) has-a Product(商品):
       A. class ShoppingCart(Product)
       B. ShoppingCart 持有 Product 列表

    5. Student(学生) has-a SchoolCard(校卡):
       A. class Student(SchoolCard)
       B. Student 持有 SchoolCard 实例

    答案:1-B, 2-B, 3-B, 4-B, 5-B(除 2 外全用组合)
"""

# ======================
# 学员代码区
# ======================
# 请先独立判断,再运行下方验证

# 演示:组合(应该这样做)
class Cart:
    def total(self):
        return 100

class Address:
    def __init__(self, city):
        self.city = city

class Order:
    """组合:Cart + Address"""
    def __init__(self, cart, address):
        self.cart = cart        # has-a
        self.address = address  # has-a

# 演示:继承(应该这样做)
class Animal:
    def breathe(self):
        pass

class Dog(Animal):  # is-a
    def bark(self):
        pass

# 请创建实例验证两种方式都能用
cart = Cart()
addr = Address("北京")
order = Order(cart, addr)

dog = Dog()

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    assert order.cart.total() == 100
    assert order.address.city == "北京"
    # Dog is-a Animal
    assert isinstance(dog, Animal)
    # Order has-a Cart 而非 is-a Cart
    assert not isinstance(order, Cart)
    print("✅ 所有测试通过")
